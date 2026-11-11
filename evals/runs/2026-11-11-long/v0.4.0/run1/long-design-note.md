# Move user sessions from Postgres to Redis

I recommend that we move user session storage from Postgres to Redis, with AOF persistence enabled. Admin sessions stay in Postgres.

I need a decision before 21 November. The Postgres major upgrade starts on that date, and the schema is frozen until the upgrade is complete. If we do not decide before then, the migration waits until January.

The decision also sets where session state lives in our architecture from now on. This note puts the channel discussion of the last few weeks in one place.

## The problem

We store user sessions in the Postgres `sessions` table, as we did in the first version of the product. Every request that needs authentication reads that table, and every login writes to it. That was fine with a few thousand users.

The table grew a lot in the last two quarters. The p95 login latency is now 480 ms, and our target is 150 ms.

We tried indexes and table partitioning. Each helped a little, but neither got below 300 ms in the staging tests. Partitioning also made the nightly cleanup job more complicated.

## Options

- Memcached: rejected. It was fast in the tests and it is very simple to operate. Two people on the team used it before. It has no persistence, so a restart of the cache node logs out every user at once. We decided that this is not acceptable, because our users are often in the middle of a long form.
- Redis: recommended. In the staging tests, the p95 login latency fell to about 90 ms, which is comfortably under the target.

## Conditions of the proposal

- AOF persistence is a hard condition. Redis can persist data to disk, but only AOF protects us. With the default snapshot settings, a crash could still lose several minutes of sessions.
- Each session key gets an idle timeout of 30 minutes, the same as today.
- Admin sessions stay in Postgres. The compliance team requires a record of admin sessions for 1 year for the audit. Redis is not the right place for records that we must keep that long. The number of admin sessions is small, so they do not add to the latency problem.

## What we do not know

- A Redis failover may log out up to 2% of active users. That number comes from the replication lag we measured. It could be less, but we could not get it to zero.
- The latency numbers might not hold above 50k concurrent sessions. The setup behaved well in load tests up to 20k, and we did not test beyond 20k. We expect to reach 50k some time next year, so we need another test before then.

## Migration and rollback

For 14 days, we write sessions to both stores. We read from Redis, with a fallback to Postgres. After 14 days with no fallback reads, we stop writing user sessions to Postgres.

If anything goes wrong at any point, we set the flag `SESSION_STORE=postgres` and restart the API pods. That takes a few minutes and does not need a deploy.

## Monitoring

We add two alerts during the migration. The on-call rotation does not change.

- The first alert fires when fallback reads to Postgres go above 1% in the dual-write period. That would mean Redis is missing sessions it should have.
- The second alert fires when Redis memory use passes 75%. Above that level, eviction would silently log people out.

## Effort and cost

- I estimate about 6 engineering days, most of it in the session middleware. The mobile apps need no change, because they only ever see the cookie.
- The managed Redis instance with a replica costs about $340 per month. That is within the infrastructure budget already approved for this quarter.

Cut candidates: the sentence about the channel discussion, the team's earlier use of Memcached, the age of the `sessions` table.
