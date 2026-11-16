# Proposal: background job queue

The platform team leans toward pg-boss, because it adds no new system. The team will review this proposal on 2026-11-20.

## Problem

Image resize jobs run inside the web request today. Users see timeouts on uploads larger than 5 MB. A job queue for background work would fix this. Who decided that we need one: TBD (owner unknown).

## Load

Our load is about 2 jobs per second. It reaches 15 per second during the nightly import.

## Options

- Do nothing: the timeouts on uploads larger than 5 MB stay.
- pg-boss: it runs on our existing Postgres. In a staging test on 2026-10-10 it handled 350 jobs per second with 4 workers.
- BullMQ: it needs Redis. The managed plan costs about $90 a month, and the platform team would need to run it.
- SQS: local development needs localstack or an AWS account for each developer. Our integration tests run offline in CI.

## Risks

- The jobs table may grow without limit. Mitigation: TBD (owner unknown).
- If Postgres is down, the queue is down.

## When we decide again

We will look at this again if the load passes 200 jobs per second.
