# Proposal: use pg-boss for the background job queue

We propose pg-boss for background jobs. The platform team leans toward it because it adds no new system, and it reviews this proposal on 2026-11-20.

## Problem

Image resize jobs run inside the web request today. Users see timeouts on uploads larger than 5 MB.

## Load

Our load is about 2 jobs per second. It reaches 15 per second during the nightly import. In a staging test on 2026-10-10, pg-boss handled 350 jobs per second with 4 workers.

## Options

We looked at three options.

- pg-boss runs on our existing Postgres.
- BullMQ needs Redis. The managed plan costs about $90 a month, and the platform team would need to run it.
- SQS needs localstack or an AWS account for each developer in local development. Our integration tests run offline in CI.

## Risks

- The jobs table may grow without limit. We will monitor it.
- If Postgres is down, the queue is down.

## Review trigger

We will look at this decision again if the load passes 200 jobs per second.

Cut candidates: the mitigation "follow best practices" (it names no action).
