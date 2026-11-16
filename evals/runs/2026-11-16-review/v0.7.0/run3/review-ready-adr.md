The ADR is ready to merge after two small fixes. A maintainer who reads it a year later can say what the team decided, why, and what would make the decision wrong.

What works:

- The title states the decision. The status, the date, and who decided are in the second line.
- The context gives numbers with a source and a date: 2 jobs per second, up to 15 at the nightly import, from the production logs of September 2026.
- The criteria come before the options. The 150 jobs per second follows from 10 times the peak of 15.
- The options table scores each option on the same criteria. It marks what was measured (pg-boss, 350 jobs per second on staging) and what comes only from documentation (BullMQ, SQS, Kafka).
- The scope has an exception (the video transcode stays on its own worker) and a reason for the 10 minute line.
- The consequences name what gets harder and the event that reopens the decision.

Fix before merge:

1. The way back is incomplete. `JOBS_BACKEND=inline` runs the resize job in the web request again. The decision moves every job of 10 minutes or less, and a job of several minutes would time out in a web request. The ADR does not say what happens to the other jobs, or to jobs already in the pg-boss table, when someone sets the switch. Add one sentence for each case, or state that the switch covers only the resize job.
2. The scope has no plan. "Every background job of 10 minutes or less moves to pg-boss", but only the resize job has an owner and an order. Say who moves the rest and by when, or write "TBD (owner unknown)" and add it to the consequences.

Questions for the authors. Answer them in the ADR if the answer is short:

- The 350 jobs per second came from 4 workers on staging. How many workers run in production? A reader who sets up production needs that number to trust the margin.
- Was the test load resize jobs or empty jobs? The p95 of 120 ms is only as useful as the load that produced it.
- Why 10 minutes and not 15? The reason is the default limit of 15 minutes. The ADR does not say that 10 is a margin below it. If it is a margin, say so.

Minor:

- The context says "users see timeouts" with no count. One number from the logs would help a reader who asks how bad it was.
- The Kafka row says "No" for the new system with no reason. The row is clear to this team, but a later reader may not know that Kafka means a new cluster.

Cut candidates: none. The page is short and every part answers a question of the maintainers.
