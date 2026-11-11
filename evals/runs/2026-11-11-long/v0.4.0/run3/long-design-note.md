# Move user sessions from Postgres to Redis

I recommend that we move user session storage from Postgres to Redis, with AOF persistence enabled. Admin sessions stay in Postgres. I need your decision before 21 November. The Postgres major upgrade starts on that date, and the schema is frozen until the upgrade is complete. If we miss that date, the migration waits until January.

This fixes the slow login. It also decides where session state lives in our architecture from now on.

## The problem

At 480 ms, the p95 login latency is well above our 150 ms target. We have stored user sessions in the Postgres `sessions` table since the first version of the product. Every authenticated request reads that table, and every login writes to it. That was fine with a few thousand users. The table grew a lot in the last two quarters.

## Options we tested

- Indexes and partitioning on the Postgres table. Both helped a little, but neither got p95 below 300 ms in the staging tests. Partitioning also made the nightly cleanup job more complicated.
- Memcached. It was fast in the tests and is very simple to operate, and two people on the team used it before. It has no persistence, so a restart of the cache node would log out every user at once. Our users are often in the middle of a long form, so we rejected it.
- Redis. The p95 login latency was about 90 ms in the staging tests, which is comfortably below the target.

## Conditions of the proposal

- AOF persistence must be enabled. Treat this as a hard condition. With the default snapshot settings, a crash could still lose several minutes of sessions.
- Admin sessions stay in Postgres. The compliance team requires a record of admin sessions for 1 year for the audit. Redis is not the right place for records that we must keep that long. Admin sessions are few, so they do not add to the latency problem.
- Each session key gets an idle timeout of 30 minutes, the same as today.

## What we do not know

- A Redis failover may log out up to 2% of active users. That figure comes from the replication lag we measured. It could be less, but we could not get it to zero.
- The latency numbers might not hold above 50k concurrent sessions. We load tested up to 20k concurrent sessions, and the setup behaved well. We did not test beyond 20k. We expect to reach 50k some time next year, so we need another test before then.

## Migration and rollback

For 14 days, we write sessions to both stores and read from Redis, with a fallback to Postgres. After 14 days with no fallback reads, we stop writing user sessions to Postgres.

If anything goes wrong at any point, we can return to Postgres. Set the flag `SESSION_STORE=postgres` and restart the API pods. This takes a few minutes and does not need a deploy.

We would add two alerts during the migration:

- The first fires when fallback reads to Postgres exceed 1% in the dual-write period. That rate would mean Redis is missing sessions it should have.
- The second fires when Redis memory use passes 75%, because eviction would silently log users out.

## Cost and effort

- I estimate about 6 engineering days, most of it in the session middleware.
- The mobile apps need no change, because they only see the cookie.
- The managed Redis instance with a replica costs about $340 per month. That is within the infrastructure budget already approved for this quarter.
- The on-call rotation does not change.

Kept as-is: "We have stored user sessions ... since the first version" (the storage continues today), and "log out" (the term the team uses for a lost session).
Cut candidates: how Postgres session storage works today, that two people on the team used Memcached before, that the on-call rotation does not change.
