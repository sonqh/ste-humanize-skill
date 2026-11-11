# ADR: Use pg-boss as the job queue

- Status: accepted
- Date: 2026-10-14
- Decided by: A, B, C, and D. All four agreed.
- Owner of the migration: D

## Decision

We use pg-boss for every background job that completes in 10 minutes or less. pg-boss is a job queue that keeps its jobs in a Postgres table. A job that takes longer than 10 minutes stays on the separate transcode worker, as it does today.

D moves the image resize job first. That job runs inside the web request today, and users see timeouts.

## Why pg-boss

- We already run Postgres, so the team of 4 gets no new system to operate, to back up, or to be paged for.
- It gives us retries and delayed jobs. It uses `SKIP LOCKED`, so workers do not compete for the same job.
- It has enough capacity. In a test on staging, D measured 350 jobs per second sustained with 4 workers before the queue table started to lag. We run about 2 jobs per second now. The peak is maybe 15 per second, during the nightly import. The measured limit is about 20 times that peak.

## Limits we accept

- The jobs table grows unless we tune autovacuum on that table. pg-boss archives and deletes completed jobs, but that alone does not stop the growth. D proposed a weekly check.
- Priorities are basic. Each job gets one number. There are no separate priority lanes.
- If Postgres is down, the queue is down. The app is down in that case too.
- pg-boss holds a job with an expiry, and the default is 15 minutes. This is the reason for the limit of 10 minutes. The video transcode takes about 25 minutes, so it stays on the worker box with its own script.

## Options we rejected

- BullMQ. It needs Redis, and we do not run Redis today. Redis would be one more system in the on-call runbook of a team of 4. The quality of BullMQ and the cost (about $90 a month for the small managed Redis) were not the reason. If we run Redis for another reason later, this reason no longer applies.
- SQS. It needs no servers and is fine in production. Local development needs localstack or a real AWS account for each developer. Our integration tests run offline in CI on purpose.
- Kafka. It is too much for 2 jobs per second. A estimated a month of work.

## When we decide again

We decide again when one of these conditions is true:

- The load passes 200 jobs per second sustained. This is well below the measured limit of 350.
- We need priority lanes.

Reader: an engineer who joins later and must find out why the team chose pg-boss and when to review the choice.
