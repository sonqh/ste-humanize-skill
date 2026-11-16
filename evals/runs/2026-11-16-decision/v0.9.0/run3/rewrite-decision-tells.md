# Proposal: use pg-boss for the background job queue

We ask you to approve pg-boss as our background job queue. The platform team reviews this proposal on 2026-11-20. pg-boss runs on our existing Postgres, so it adds no new system.

## Why we need a queue

Image resize jobs run inside the web request today. Users see timeouts on uploads larger than 5 MB. If we do nothing, the timeouts stay.

## Load

Our load is about 2 jobs per second. It reaches 15 per second during the nightly import.

## Options

- pg-boss: we measured 350 jobs per second with 4 workers on staging on 2026-10-10. It runs on our existing Postgres.
- BullMQ: it needs Redis. The managed plan costs about $90 a month, and the platform team would need to run it.
- SQS: local development needs localstack or an AWS account for each developer. Our integration tests run offline in CI.

The platform team leans toward pg-boss, because it adds no new system. pg-boss handled 350 jobs per second against a peak of 15, so we have room to grow.

## Risks

- The jobs table may grow without limit. Mitigation: TBD (owner unknown).
- If Postgres is down, the queue is down.

## When we look again

We will look at this choice again if the load passes 200 jobs per second. Who decided this: TBD (owner unknown).

## Open questions

- Who owns the action on table growth, and what size starts it?
- Who decided that we need a queue, and on what date?

Cut candidates: "Both options have their merits, and the right choice depends on the needs of the team" (three options, and it states no choice). "Scalable and reliable", "battle-tested and flexible", and "enterprise-grade" (no number). "We will monitor closely and follow best practices" (it names no action).
