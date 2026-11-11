# Use pg-boss on Postgres for background jobs shorter than 10 minutes

- Status: Accepted
- Date: 2026-10-14
- Deciders: A, B, C, and D. All four agreed.
- Owner: D

## Context

Image resize jobs run inside the web request, and users see timeouts. We need a job queue that moves this work out of the request.

The facts on 2026-10-14:

- The load is about 2 jobs per second. The peak is about 15 jobs per second, during the nightly import.
- The team has 4 people. Each new system adds work to the on-call runbook: we operate it, back it up, and get paged for it.
- We run Postgres. We do not run Redis.
- The integration tests run offline in CI on purpose.
- The video transcode job takes about 25 minutes. It runs on a separate worker box with its own script.

## Decision

We will use pg-boss for background jobs. pg-boss is a job queue that keeps its jobs in a Postgres table. It gives us retries and delayed jobs. It uses `SKIP LOCKED`, so two workers do not take the same job.

- The scope is every background job that completes in 10 minutes or less.
- The exception is any job longer than 10 minutes. Such a job stays on the transcode worker, as it does today. pg-boss holds a job with an expiry, and the default is 15 minutes.
- The resize job moves first, because it is the one that hurts users. D owns that migration.

D tested pg-boss on staging. With 4 workers it sustained 350 jobs per second before the queue table started to lag. That is about 20 times the peak load.

## Options we rejected

- BullMQ. It needs Redis, and Redis is one more system for 4 people to operate. Managed Redis costs about $90 a month for the small size, and the cost was not the reason. BullMQ is a good tool with a good dashboard. If we run Redis for another reason, this reason no longer holds.
- SQS. It needs no servers and is fine in production. Local development needs localstack or a real AWS account for each developer, and that conflicts with offline integration tests.
- Kafka. It is too large for 2 jobs per second. A estimated a month of work to set it up.

## Consequences

We add no new infrastructure, because we already run Postgres. The costs:

- The jobs table bloats. pg-boss archives and deletes completed jobs, but the table grows unless we tune autovacuum for it. D proposed a weekly check of that table.
- Priorities are basic: one number for each job. There are no separate priority lanes.
- If Postgres is down, the queue is down. The app is down then too.

## When to decide again

- The load passes 200 jobs per second, sustained. That leaves a margin before the 350 limit of the staging test.
- We need priority lanes.
- We start to run Redis for another reason. Then compare BullMQ again.
