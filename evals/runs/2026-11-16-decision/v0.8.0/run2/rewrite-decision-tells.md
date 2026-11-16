# Proposal: use pg-boss for background jobs

We ask you to approve pg-boss as our background job queue. The platform team leans toward it because it adds no new system. The platform team will review this proposal on 2026-11-20.

Image resize jobs run inside the web request today. Users see timeouts on uploads larger than 5 MB. If we do nothing, these timeouts continue.

## Options

We looked at three options. The decision to add a queue was made earlier (decider: owner unknown).

| Option | What it needs | Evidence and cost |
|---|---|---|
| pg-boss | Our existing Postgres | In a staging test on 2026-10-10, it handled 350 jobs per second with 4 workers. |
| BullMQ | Redis, which the platform team would run | The managed plan costs about $90 a month. |
| SQS | An AWS account or localstack for each developer | Our integration tests run offline in CI, so SQS does not fit them. |

Our load is about 2 jobs per second, and up to 15 per second during the nightly import. The pg-boss staging result is more than 20 times the nightly peak.

## Risks and the way back

- The jobs table may grow without limit. Mitigation: TBD (owner unknown).
- If Postgres is down, the queue is down.

We will look at this decision again if the load passes 200 jobs per second.

## Open questions

- What is the mitigation for the growth of the jobs table? Owner unknown.

Cut candidates: "Both options have their merits, and the right choice depends on the needs of the team" (says nothing the options do not). The words "scalable", "reliable", "battle-tested", "flexible", and "enterprise-grade" (the numbers and needs carry the comparison). "We will monitor closely and follow best practices" (names no action, so it became the gap above).

Reader: the engineering manager who approves, with little time.
