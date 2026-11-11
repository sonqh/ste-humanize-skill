# Proposal: move user sessions from Postgres to Redis

I recommend that we move user session storage from Postgres to Redis, with AOF persistence enabled, and keep admin sessions in Postgres. I need your decision before 21 November. The Postgres major upgrade starts on that date, and the schema is frozen until the upgrade is complete. If we miss that date, the migration waits until January.

This is a performance problem. It is also a question about where session state lives in our architecture from now on.

## The problem

The p95 login latency is 480 ms, well above our 150 ms target. Since the first version of the product, we have stored user sessions in the Postgres `sessions` table. Every request that needs authentication reads that table, and every login writes to it. That was fine with a few thousand users, but the table grew a lot in the last two quarters.

We tried indexes and we tried partitioning. Each helped a little, but neither got us under 300 ms in the staging tests. Partitioning also made the nightly cleanup job more complicated.

## The options we tested

- We rejected Memcached. It was fast in the tests, it is very simple to operate, and two people on the team have used it. But it has no persistence, so a restart of the cache node logs out every user at once. We decided that was not acceptable, because our users are often in the middle of a long form.
- We propose Redis. In the staging tests, the p95 login latency came down to about 90 ms, which is comfortably under the target.

## Conditions of the proposal

- AOF persistence must be on. Treat this as a hard condition. Redis can persist data to disk, but with the default snapshot settings we could still lose several minutes of sessions on a crash.
- Admin sessions stay in Postgres. The compliance team requires a record of admin sessions for 1 year for the audit. Redis is not the right place for records kept that long. There are few admin sessions, so they do not add to the latency problem.
- Each session key gets an idle timeout of 30 minutes, the same as today.

## What we do not know

- During a Redis failover, we may log out up to 2% of active users. That number comes from the replication lag we measured. It could be less, but we could not get it to zero.
- We load tested the setup up to 20k concurrent sessions, and it behaved well. We have not tested beyond 20k, and the latency numbers might not hold above 50k. We expect to reach 50k some time next year, so we need another test before then.

## Migration and rollback

1. Write sessions to both stores for 14 days. In that period, read from Redis, with a fallback to Postgres.
2. After 14 days with no fallback reads, stop writing user sessions to Postgres.

If anything goes wrong at any point, set the flag `SESSION_STORE=postgres` and restart the API pods. That takes a few minutes and does not need a deploy.

We would add two alerts during the migration:

- One fires when the rate of fallback reads to Postgres goes above 1% in the dual-write period. That would mean Redis is missing sessions it should have.
- One fires when Redis memory use passes 75%, because eviction would silently log people out.

The on-call rotation does not change.

## Cost and effort

- The managed Redis instance with a replica costs about $340 per month. That is within the infrastructure budget already approved for this quarter.
- I estimate about 6 engineering days for the work, most of it in the session middleware.
- The mobile apps need no change, because they only ever see the cookie.

Cut candidates: the history of sessions in Postgres under "The problem", the note that two people know Memcached.
