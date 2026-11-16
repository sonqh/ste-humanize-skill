# ADR 7: Use pg-boss on Postgres for background jobs of 10 minutes or less

Status: Accepted, 2026-10-14. The backend team of four decided.

## Context

Image resize jobs run inside the web request today, and users see timeouts. We measured the load in the production logs of September 2026. It is about 2 jobs per second, and up to 15 per second during the nightly import. We run Postgres. We do not run Redis. The team has four people, and each new system adds to the on-call work.

## Decision

We will use pg-boss, a job queue that stores its jobs in a Postgres table. Every background job of 10 minutes or less moves to pg-boss. The resize job moves first. Dana owns it.

The line is 10 minutes because pg-boss stops a job after 15 minutes by default. The video transcode takes about 25 minutes, so it stays on its own worker.

To go back, set `JOBS_BACKEND=inline`. The resize job then runs in the web request again, as it does today.

## Criteria

- No new system to run and to page for.
- Room for at least 10 times the peak load of today, so 150 jobs per second.
- Integration tests run offline in CI.

## Options

| Option | No new system | Room for 150 jobs per second | Offline tests |
|---|---|---|---|
| Do nothing | Yes | Not needed | Yes |
| pg-boss | Yes | Yes. We measured 350 jobs per second with 4 workers on staging on 2026-10-10. Staging has the same Postgres size as production. | Yes |
| BullMQ | No. It needs Redis. | Yes, from its documentation. We did not test it. | Yes |
| SQS | No. It is an AWS service that we do not use today. | Yes, from its documentation. We did not test it. | No. It needs localstack or an AWS account for each developer. |
| Kafka | No | Yes, from its documentation. We did not test it. | No |

Doing nothing keeps the timeouts that started this decision. BullMQ lost only because it needs Redis. If we run Redis for another reason, look at it again.

## Consequences

- The jobs table grows. We tune autovacuum on that table. Dana checks its size each Monday and opens a ticket when it passes 5 GB.
- The queue adds load to the Postgres of the app. At 350 jobs per second on staging, the p95 latency of the app stayed under 120 ms.
- pg-boss has one number for the priority of a job. It has no separate lanes.
- When Postgres is down, the queue is down. The app is down in that case too.
- Decide again if the load stays above 200 jobs per second for 7 days, or if we need priority lanes. The target of 200 leaves room below the 350 that we measured.

Kept as-is: "Doing nothing keeps the timeouts that started this decision" and the table cells that say "from its documentation. We did not test it", because they mark which numbers are measured and which are not.
