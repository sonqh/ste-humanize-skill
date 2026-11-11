# Use pg-boss on Postgres for background jobs of 10 minutes or less

Status: Accepted

Date: 2026-10-14

Deciders: A, B, C, and D. All four agreed.

## Context

The image resize jobs run inside the web request, and users see timeouts. The team needed a job queue to move this work out of the request.

The facts on the date of the decision:

- The load is about 2 jobs per second. The peak is about 15 jobs per second, during the nightly import.
- The team has 4 people. Each new system adds to the on-call runbook.
- The team runs Postgres. The team does not run Redis.
- The integration tests run offline in CI on purpose.
- The video transcode job takes about 25 minutes. It runs on a separate worker box with its own script.

## Decision

We will use pg-boss for background jobs. pg-boss is a job queue that keeps its jobs in a Postgres table.

There is one exception. A job that runs longer than 10 minutes does not go in pg-boss. pg-boss holds a job with an expiry, and the default is 15 minutes. The video transcode job stays on the transcode worker, as it is today.

D owns the migration. The resize job moves first, because it is the job that hurts users.

## Why pg-boss

- It adds no new system to operate. The jobs sit in the database that the team already runs.
- It gives retries and delayed jobs.
- It uses `SKIP LOCKED`, so two workers do not take the same job.
- It has enough capacity. D tested it on staging with 4 workers. It held 350 jobs per second before the queue table started to lag. That is about 20 times the peak load.

## Options we rejected

- BullMQ. It needs Redis, and Redis would be one more system to operate, back up, and carry in the on-call runbook. That is the only reason. The team liked BullMQ and its dashboard. Managed Redis costs about $90 a month for the small instance, and the cost was not the problem. If the team runs Redis for another reason, this reason no longer applies.
- SQS. It works in production and needs no servers. Local development needs localstack or a real AWS account for each developer. That conflicts with the offline integration tests.
- Kafka. It is too large for 2 jobs per second. A estimated a month of work to set it up.

## Consequences

- The jobs table bloats. pg-boss archives and deletes completed jobs, but the table grows unless someone tunes autovacuum for it. D proposed a weekly check of the table.
- Priorities are basic. Each job has one priority number. There are no separate priority lanes.
- When Postgres is down, the queue is down. The app is down too in that case.
- Jobs longer than 10 minutes stay outside the queue, so the team keeps two ways to run background work.

## When to decide again

Decide again when one of these events occurs:

- The load passes 200 jobs per second sustained. That leaves room before the limit of 350 that the test showed.
- The team needs priority lanes.
- The team starts to run Redis for another reason. BullMQ becomes an option again.
