# Proposal: move background jobs to pg-boss

We ask you to approve pg-boss as our background job queue. The platform team reviews this proposal on 2026-11-20. The platform team leans toward pg-boss because it adds no new system.

## Why we need a queue

Image resize jobs run inside the web request today. Users see timeouts on uploads larger than 5 MB. A job queue moves this work out of the request. Who decided that we need a queue, and when: TBD (owner unknown).

If we do nothing, the resize work stays in the request and the timeouts continue.

## Options

Our load is about 2 jobs per second, and up to 15 per second during the nightly import.

- pg-boss runs on our existing Postgres. We measured 350 jobs per second with 4 workers on staging on 2026-10-10. Cost: TBD (owner unknown).
- BullMQ needs Redis. The managed plan costs about $90 a month, and the platform team would need to run it.
- SQS needs localstack or an AWS account for each developer in local development. Our integration tests run offline in CI. Cost: TBD (owner unknown).

The deciding point is the new system. Only pg-boss adds none. Its measured rate is far above our peak of 15 jobs per second.

## Risks

- The jobs table may grow without limit. We have no mitigation yet: TBD (owner unknown).
- If Postgres is down, the queue is down.

## When we look again

We will look at this decision again if the load passes 200 jobs per second.

## Open questions

- Who decided that we need a queue, and on what date? TBD (owner unknown).
- What do pg-boss and SQS cost? TBD (owner unknown).
- What limits the growth of the jobs table, who checks it, and at what size? TBD (owner unknown).

Cut candidates: "follow best practices" and "monitor closely" (no action, no owner); "both options have their merits" and "the right choice depends on the needs of the team" (no content); the quality words "scalable", "reliable", "battle-tested", "flexible", and "enterprise-grade" (no number behind them).
