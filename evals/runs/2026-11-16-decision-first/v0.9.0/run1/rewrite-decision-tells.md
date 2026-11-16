# Proposal: background job queue

The platform team leans toward pg-boss, because it adds no new system. The platform team will review this proposal on 2026-11-20. Decided by: TBD (owner unknown).

## Problem

Image resize jobs run inside the web request today. Users see timeouts on uploads larger than 5 MB. We need a job queue for background work. If we do nothing, the timeouts stay.

## Our load

Our load is about 2 jobs per second. It reaches up to 15 per second during the nightly import.

## Options

We looked at three options: pg-boss, BullMQ, and SQS.

| Option | What it needs | Evidence |
|---|---|---|
| pg-boss | Our existing Postgres. No new system. | Measured on staging on 2026-10-10: 350 jobs per second with 4 workers. |
| BullMQ | Redis. The platform team would need to run it. | The managed plan costs about $90 a month. |
| SQS | An AWS account or localstack for each developer in local development. | Our integration tests run offline in CI. |

The new system decides it. pg-boss needs none, and 350 jobs per second is far above our peak of 15.

## Risks

- The jobs table may grow without limit. Mitigation: TBD (owner unknown). The source says "monitor closely and follow best practices", which names no action, no owner, and no signal.
- If Postgres is down, the queue is down.

## When we look again

We will look at this again if the load passes 200 jobs per second.

## Open questions

- Who decided that we need a job queue, and when? (owner unknown)
- What action limits the growth of the jobs table, who does it, and at what size? (owner unknown)
- What does pg-boss cost in time and money? The source gives no figure.

Kept as-is: "leans toward", because the source says the platform team has not decided yet.
