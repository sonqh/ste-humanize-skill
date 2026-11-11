# Proposal: move user sessions from Postgres to Redis

I recommend that we move user session storage from Postgres to Redis, with AOF persistence enabled, and keep admin sessions in Postgres. We need your decision before 21 November. This fixes the slow login, and it also decides where session state lives in our architecture from now on.

## Why the date matters

The Postgres major upgrade starts on 21 November. The schema is frozen from that date until the upgrade is complete. If there is no decision before 21 November, the migration waits until January.

## The problem

User sessions have been in the Postgres `sessions` table since the first version of the product. Every request that needs authentication reads that table, and every login writes to it. The table grew a lot over the last two quarters. The p95 login latency is now 480 ms, and our target is 150 ms.

## What we tested

- Indexes and partitioning in Postgres. Both helped a little, but neither got below 300 ms in the staging tests. Partitioning also made the nightly cleanup job more complicated.
- Memcached. It was fast in the tests, it is simple to operate, and two people on the team have used it. It has no persistence, so a restart of the cache node would log out every user at once. We rejected it, because our users are often in the middle of a long form.
- Redis. The p95 login latency came down to about 90 ms in the staging tests, which is under the target.

## Conditions of the proposal

- AOF persistence is a hard condition. Redis protects sessions on disk only if AOF is on. With the default snapshot settings, a crash could still lose several minutes of sessions.
- Each session key gets an idle timeout of 30 minutes, the same as today.
- Admin sessions stay in Postgres. The compliance team requires a record of admin sessions for 1 year for the audit. Redis is the wrong place for records kept that long. There are few admin sessions, so they do not add to the latency problem.

## What we do not know

- A Redis failover may log out up to 2% of active users. That number comes from the replication lag we measured. It could be less, but we could not get it to zero.
- We load tested up to 20k concurrent sessions, and the setup behaved well. We did not test beyond 20k, and the latency numbers might not hold above 50k. We expect to reach 50k some time next year, so we need another test before then.

## Migration

1. For 14 days, write sessions to both stores. Read from Redis, with a fallback to Postgres.
2. After 14 days with no fallback reads, stop writing user sessions to Postgres.

We can go back at any point. Set the flag `SESSION_STORE=postgres` and restart the API pods. That takes a few minutes and needs no deploy.

## Monitoring

We add two alerts during the migration. The on-call rotation does not change.

- The first alert fires when fallback reads to Postgres go above 1% in the dual-write period. That rate would mean Redis is missing sessions it should have.
- The second alert fires when Redis memory use passes 75%. Eviction would log people out with no warning.

## Cost and effort

- The managed Redis instance with a replica costs about $340 per month. That is within the infrastructure budget already approved for this quarter.
- I estimate about 6 engineering days, most of it in the session middleware.
- The mobile apps need no change, because they only ever see the cookie.

Cut candidates: the Memcached history (who used it, how it tested), the history of the `sessions` table, the nightly cleanup job detail.
