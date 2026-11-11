# ADR: Use pg-boss for background jobs

- Status: accepted
- Date: 2026-10-14
- Decided by: A, B, C, and D. All four agreed.
- Owner: D

## Decision

We use pg-boss for each background job that takes 10 minutes or less. pg-boss is a job queue that keeps its jobs in a Postgres table. A job that takes more than 10 minutes stays on the transcode worker.

D moves the image resize job first, because that job hurts users now.

## Context

- The image resize jobs run inside the web request, and users see timeouts.
- The load is about 2 jobs per second now. The peak may be 15 per second, during the nightly import.
- The team has 4 people. Each new system is one more entry in the on-call runbook.
- We run Postgres today. We do not run Redis.
- The integration tests run offline in CI on purpose.

## Why pg-boss

- It needs no new infrastructure. The jobs are in the Postgres that we already operate.
- It gives us retries and delayed jobs.
- It uses `SKIP LOCKED`, so the workers do not compete for the same job.
- It has enough capacity. D tested it on staging: 350 jobs per second sustained with 4 workers, before the queue table started to lag. That is about 20 times our peak.

## Options we rejected

| Option | Why we rejected it |
|---|---|
| BullMQ | It needs Redis, a new system to operate, back up, and get paged for. The small managed Redis costs about $90 a month, but the cost was not the reason. BullMQ is a good tool with a good dashboard. If we run Redis for another reason, this answer can change. |
| SQS | It needs no servers and it is fine in production. Local development needs localstack or a real AWS account for each developer. Our integration tests must run offline. |
| Kafka | It is too large for 2 jobs per second. A estimated a month of work. |

## Limits and costs

- The jobs table bloats. pg-boss archives and deletes completed jobs, but the table grows unless we tune autovacuum on it. D proposed a weekly check.
- Priorities are basic. Each job gets one number. There are no separate priority lanes.
- If Postgres is down, the queue is down. In that case the app is down too.
- pg-boss holds a job with an expiry, and the default is 15 minutes. For this reason we put no job longer than 10 minutes in it.
- The video transcode takes about 25 minutes. It stays on the separate worker box with its own script, as it is today.

## When we decide again

We decide again when one of these conditions is true:

- The load passes 200 jobs per second sustained. That is well below the limit of 350.
- We need priority lanes.

Reader: a team member who reviews this decision later and was not in the thread.
