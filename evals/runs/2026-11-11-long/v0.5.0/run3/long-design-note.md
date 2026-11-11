# Proposal: move user sessions from Postgres to Redis

I recommend that we move user session storage from Postgres to Redis, with AOF persistence enabled. Admin sessions stay in Postgres. I need your decision before 21 November.

The Postgres major upgrade starts on 21 November. The schema is frozen from that date until the upgrade is complete. If we do not decide before then, the migration waits until January.

This proposal fixes the slow login. It also decides where session state lives in our architecture from now on.

## The problem

We have stored user sessions in the Postgres `sessions` table since the first version of the product. Each authenticated request reads that table, and each login writes to it. This was fine with a few thousand users.

The table grew a lot in the last two quarters. The p95 login latency is now 480 ms, and our target is 150 ms.

Indexes and table partitioning each helped a little. Neither brought the latency below 300 ms in the staging tests. Partitioning also made the nightly cleanup job more complicated.

## Why Redis

In the staging tests, Redis brought the p95 login latency down to about 90 ms. That is below the 150 ms target.

AOF persistence is a hard condition of this proposal. With the default snapshot settings, a crash could still lose several minutes of sessions. Redis protects the sessions only when AOF is on.

Each session key gets an idle timeout of 30 minutes, the same as today.

We tested Memcached first, because two people on the team know it and it is simple to operate. It was fast in the tests. We rejected it because it has no persistence. A restart of the cache node would log out every user at once, and our users are often in the middle of a long form.

## The exception: admin sessions

Admin sessions stay in Postgres. The compliance team requires a record of admin sessions for 1 year for the audit. Redis is not the right place for records that we must keep that long. There are few admin sessions, so they do not add to the latency problem.

## What we do not know

- A Redis failover may log out up to 2% of active users. This estimate comes from the replication lag we measured. The number could be lower, but we could not get it to zero.
- The latency numbers might not hold above 50k concurrent sessions. We load tested up to 20k concurrent sessions, and the setup behaved well. We did not test above 20k. We expect to reach 50k some time next year, so we need another test before then.

## Migration and rollback

1. Write sessions to both stores for 14 days. Read from Redis, with a fallback to Postgres.
2. After 14 days with no fallback reads, stop writing user sessions to Postgres.

We can go back at any point. Set the flag `SESSION_STORE=postgres` and restart the API pods. This takes a few minutes and does not need a deploy.

## Monitoring

We add two alerts during the migration:

- The first alert fires when fallback reads to Postgres go above 1% in the dual-write period. That rate would mean that Redis does not have sessions it should have.
- The second alert fires when Redis memory use goes above 75%. Eviction would log people out with no warning.

The on-call rotation does not change.

## Cost and effort

- The managed Redis instance with a replica costs about $340 per month. That is within the infrastructure budget already approved for this quarter.
- I estimate about 6 engineering days. Most of the work is in the session middleware.
- The mobile apps need no change, because they only see the cookie.

Cut candidates: the history of sessions in Postgres, the reason we tested Memcached first, the on-call sentence.
