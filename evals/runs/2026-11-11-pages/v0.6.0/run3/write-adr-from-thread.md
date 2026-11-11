# Use pg-boss for background jobs of 10 minutes or less

- Status: Accepted
- Date: 2026-10-14
- Decided by: A, B, C, and D. All four agreed.

## Context

The image resize jobs run inside the web request, and users see timeouts. We need a job queue.

The facts on 2026-10-14:

- The team has 4 people. Each new system adds to the on-call runbook.
- We run Postgres. We do not run Redis.
- The load is about 2 jobs per second. The peak may reach 15 per second during the nightly import.
- The integration tests run offline in CI on purpose.

## Decision

We will use pg-boss for every background job that runs for 10 minutes or less. pg-boss is a job queue that stores its jobs in a Postgres table.

- pg-boss gives us retries and delayed jobs. It uses `SKIP LOCKED`, so two workers do not take the same job.
- Exception: a job that runs for more than 10 minutes does not go into pg-boss. pg-boss holds a job with an expiry, and the default is 15 minutes.
- The video transcode takes about 25 minutes. It stays on the separate transcode worker, which has its own script.
- The image resize job moves first, because it is the one that hurts users. D owns that migration.

D tested pg-boss on staging. It sustained 350 jobs per second with 4 workers before the queue table started to lag. That is about 20 times our peak load.

## Options we rejected

- BullMQ. It needs Redis, and Redis is one more system to operate, back up, and get paged for. We did not reject BullMQ on quality: it is a good tool with a good dashboard. We did not reject it on cost: the small managed Redis costs about $90 a month.
- SQS. It works in production and needs no servers. For local development, each developer needs localstack or a real AWS account. Our offline integration tests do not fit that.
- Kafka. It is too much for 2 jobs per second. A estimated a month of work.

## Consequences

Good:

- We add no new infrastructure. The queue runs on the Postgres that we already operate.

Harder:

- The jobs table grows. pg-boss archives and deletes completed jobs, but autovacuum must be tuned on that table. D proposed a weekly check of the table.
- Priorities are basic: one number for each job. There are no separate priority lanes.
- If Postgres is down, the queue is down. The app is down then anyway.
- Jobs of more than 10 minutes stay outside the queue, on the transcode worker.

## When to decide again

- The load passes 200 jobs per second sustained. That is well below the limit of 350 that we measured.
- We need priority lanes.
- We start to run Redis for another reason. Then the reason against BullMQ no longer applies.
