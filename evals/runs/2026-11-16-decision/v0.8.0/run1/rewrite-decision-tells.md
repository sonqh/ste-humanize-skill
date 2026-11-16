# Proposal: background job queue

The platform team leans toward pg-boss as the job queue for background work. It runs on our existing Postgres and adds no new system. The platform team will review this proposal on 2026-11-20.

## Problem

We need a job queue for background work. Image resize jobs run inside the web request today. Users see timeouts on uploads larger than 5 MB.

Our load is about 2 jobs per second, and up to 15 per second during the nightly import.

## Options

We looked at three options.

- pg-boss runs on our existing Postgres. In a staging test on 2026-10-10 it handled 350 jobs per second with 4 workers.
- BullMQ needs Redis. The managed plan costs about $90 a month, and the platform team would need to run it.
- SQS needs localstack or an AWS account for each developer in local development, and our integration tests run offline in CI.

## Risks

- The jobs table may grow without limit. Mitigation: we will monitor the table. The limit, the alert, and the owner are TBD (owner unknown).
- If Postgres is down, the queue is down.

## When we decide again

We will look at this again if the load passes 200 jobs per second.

Kept as-is: "leans toward" and "may grow without limit", because the source states a lean and a possibility, not a fact.
Cut candidates: "scalable and reliable", "battle-tested and flexible", "enterprise-grade", "Both options have their merits...", and "follow best practices". They name no fact the approver can check.
