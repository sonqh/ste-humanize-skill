# Proposal: move user sessions from Postgres to Redis

I recommend that we move user session storage from Postgres to Redis, with AOF persistence enabled. Admin sessions stay in Postgres. I need a decision before 21 November. The Postgres major upgrade starts on that date, and the schema is frozen until the upgrade is complete. If we miss that date, the migration waits until January.

The login slowness is the trigger. The decision also sets where session state lives in our architecture from now on.

## The problem

The p95 login latency is 480 ms. Our target is 150 ms.

Postgres stores user sessions in the sessions table, as it did in the first version of the product. Every authenticated request reads that table, and every login writes to it. This worked for a few thousand users. The table grew a lot in the last two quarters.

We tested indexes and table partitioning. Both helped a little. Neither brought the p95 below 300 ms in the staging tests. Partitioning also made the nightly cleanup job more complicated.

## Options we tested

- Memcached. It was fast in the tests and it is very simple to operate. Two people on the team used it before. We rejected it because it has no persistence. A restart of the cache node would end the session of every user at once. Our users are often in the middle of a long form, so we decided that this is not acceptable.
- Redis. In the staging tests, the p95 login latency decreased to about 90 ms. That is comfortably below the target.

## Conditions of the proposal

- AOF persistence must be on. This is a hard condition. With the default snapshot settings, a crash could still lose several minutes of sessions.
- Each session key gets an idle timeout of 30 minutes, the same as today.
- Admin sessions stay in Postgres. The compliance team requires a record of admin sessions for 1 year for the audit. Redis is not the right place for records with a retention that long. The number of admin sessions is small, so they do not add to the latency problem.

## What we do not know

- A Redis failover may end the sessions of up to 2% of active users. We base this number on the replication lag that we measured. It could be less, but we could not get it to zero.
- We did not test above 20k concurrent sessions. Up to 20k, the setup behaved well. The latency numbers might not hold above 50k concurrent sessions. We expect to reach 50k some time next year, so we need another load test before then.

## Migration and rollback

1. For 14 days, the API writes sessions to both stores. It reads from Redis and uses Postgres as a fallback.
2. After 14 days with no fallback reads, we stop writing user sessions to Postgres.

To return to Postgres at any point, set the flag `SESSION_STORE=postgres` and restart the API pods. This takes a few minutes and does not need a deploy.

We would add two alerts during the migration:

- The rate of fallback reads to Postgres goes above 1% in the dual-write period. That would mean Redis is missing sessions that it should have.
- Redis memory use passes 75%. Eviction would end sessions with no warning to us.

The on-call rotation does not change.

## Cost and effort

- The managed Redis instance with a replica costs about $340 per month. That is within the infrastructure budget already approved for this quarter.
- I estimate about 6 engineering days. Most of the work is in the session middleware.
- The mobile apps need no change, because they only see the cookie.

Kept as-is: "After 14 days with no fallback reads" is the source wording. The source does not say which part of the 14 days must have no fallback reads.
Cut candidates: Postgres session history since the first version, "this worked for a few thousand users", two people on the team used Memcached before.
