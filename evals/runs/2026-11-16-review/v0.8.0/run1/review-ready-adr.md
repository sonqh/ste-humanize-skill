The ADR is ready for the maintainers of the job system. A maintainer can say what the team decided, why, and what would make the decision wrong, and the findings below are fixes that do not block the merge.

| Question | Answered | Where | Gap |
|---|---|---|---|
| What did we decide? | Yes | Title | |
| Is it still in force? | Yes | Status | |
| What forced a decision? | Yes | Context | |
| What exactly did we choose? | Partly | Decision | "Every background job" has no list. Only the resize job has an order and an owner. |
| What decides between the options? | Yes | Criteria | |
| What else did we look at, and why not? | Yes | Options | |
| What follows? | Yes | Consequences | |

- Decision, way back: `JOBS_BACKEND=inline` returns the resize job to the web request. The page names no way back for the other jobs, and a job of up to 10 minutes cannot run in a request that already times out. Say what the way back is for them, or say that it covers the resize job only.
- Decision, scope: "Every background job of 10 minutes or less" moves, but the page names only the resize job and the video transcode. List the other jobs and their order, or write `TBD` with an owner and a date.
- Decision, 15 minutes: the pg-boss default timeout has no source. It sets the 10 minute line, so name where the number comes from. Not checked.
- Decision, 25 minutes: "about 25 minutes" for the transcode has no kind. Say whether it is measured or an estimate.
- Consequences, 120 ms: the p95 of the app has no value from before the queue. Without it, a reader cannot tell what the queue costs.
- Consequences, 5 GB: the size that opens a ticket has no kind or reason. Say that it is a target, and why 5 GB.

Lint: no hard findings.
