# Proposal: background job queue

We recommend pg-boss for the background job queue, because it adds no new system. The platform team leans toward it and will review this proposal on 2026-11-20.

## Problem

Image resize jobs run inside the web request today. Users see timeouts on uploads larger than 5 MB. We decided that background work needs a proper job queue (who decided and when: TBD, owner unknown).

Our load is about 2 jobs per second, and up to 15 per second during the nightly import.

## Options

We looked at three options.

- pg-boss runs on our existing Postgres. In a staging test on 2026-10-10 it handled 350 jobs per second with 4 workers.
- BullMQ needs Redis. The managed plan costs about $90 a month, and the platform team would need to run it.
- SQS needs localstack or an AWS account for each developer in local development. Our integration tests run offline in CI.

## Risks

- The jobs table may grow without limit. Mitigation: TBD (owner unknown).
- If Postgres is down, the queue is down.

## When we look again

We will look at this again if the load passes 200 jobs per second. Who decided this: TBD (owner unknown).

Cut candidates: "Both options have their merits, and the right choice depends on the needs of the team" (no choice in it); "scalable and reliable", "battle-tested and flexible", "enterprise-grade" (quality words with no number); "we will monitor closely and follow best practices" (names no action).
