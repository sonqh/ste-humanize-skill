# Proposal: background job queue

We ask you to approve pg-boss as our background job queue. It runs on our existing Postgres and adds no new system. The platform team leans toward pg-boss and will review this proposal on 2026-11-20. Who decided that we need a queue, and when: TBD (owner unknown).

## Why we need a queue

Image resize jobs run inside the web request today. Users see timeouts on uploads larger than 5 MB. If we do nothing, the timeouts stay.

## Options

We looked at three options: pg-boss, BullMQ, and SQS. Our load is about 2 jobs per second, and up to 15 per second during the nightly import.

- pg-boss runs on our existing Postgres. In a staging test on 2026-10-10 it handled 350 jobs per second with 4 workers.
- BullMQ needs Redis. The managed plan costs about $90 a month, and the platform team would need to run it.
- SQS needs localstack or an AWS account for each developer in local development. Our integration tests run offline in CI.

The new system decides it. pg-boss needs none. BullMQ needs Redis, and SQS needs localstack or AWS accounts.

## Risks

- The jobs table may grow without limit. Mitigation: TBD (owner unknown).
- If Postgres is down, the queue is down.

## When to decide again

We will look at this again if the load passes 200 jobs per second. Who owns that check: TBD (owner unknown).

## Open questions

- Who decided that we need a queue, and on what date?
- Who limits the growth of the jobs table, which action do they take, and which signal starts it?
- Who owns the check of the 200 jobs per second limit?

Cut candidates: "Both options have their merits, and the right choice depends on the needs of the team" (it gives no choice). "We will monitor closely and follow best practices" (it names no action).
