# ADR: Use pg-boss for background jobs

- Status: accepted
- Date: 2026-10-14
- Decided by: A, B, C, and D. All four agreed.
- Owner of the first migration: D

## Decision

We use pg-boss for background jobs. pg-boss is a job queue that stores its jobs in a Postgres table.

One exception applies. A job that runs longer than 10 minutes does not go in pg-boss. Such a job stays on the separate transcode worker, as it does today.

D moves the image resize job first, because that job causes the timeouts that users see.

## Context

The image resize jobs run inside the web request, and users see timeouts.

- The load is about 2 jobs per second. The peak is about 15 jobs per second, during the nightly import.
- The team has 4 people. Each new system adds work to the on-call runbook.
- We run Postgres. We do not run Redis.
- The integration tests run offline in CI on purpose.

## Why pg-boss

- It adds no new infrastructure. The jobs are rows in the Postgres that we already operate.
- It gives us retries and delayed jobs.
- It uses `SKIP LOCKED`, so two workers do not take the same job.
- It has enough capacity. D tested it on staging and measured 350 jobs per second sustained with 4 workers. Above that rate, the queue table started to lag. That limit is about 20 times our peak.

## Options we rejected

| Option | Why we rejected it |
|---|---|
| BullMQ | It needs Redis, and Redis is one more system to operate, back up, and get paged for. |
| SQS | Local development needs localstack or a real AWS account for each developer. Our offline integration tests in CI cannot use it. |
| Kafka | It is too large for 2 jobs per second. A estimated a month of work. |

We did not reject BullMQ for its quality. B found it good and liked its dashboard. Cost was not the reason: the small managed Redis is about $90 a month. If we run Redis for another reason, examine BullMQ again.

SQS works in production. The problem is only local development and CI.

## Limits and risks

- The jobs table grows. pg-boss archives and deletes completed jobs, but the table still grows unless we tune autovacuum for it. D proposed a weekly check of the table size. No one owns that check yet.
- Priorities are basic. Each job has one priority number. pg-boss has no separate priority lanes.
- When Postgres stops, the queue stops. The app also stops in that case, so the queue adds no new failure.
- pg-boss holds a job with an expiry, 15 minutes by default. This is the reason for the 10-minute limit. The video transcode takes about 25 minutes, so it stays on the transcode worker with its own script.

## When to decide again

Decide again when one of these conditions occurs:

- The load passes 200 jobs per second sustained. That is well below the measured limit of 350.
- We need priority lanes.
- We start to run Redis for another reason.

Reader: a team member who reviews this decision now, or who must decide later whether it still applies.
