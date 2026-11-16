Ready for the maintainers of the job system. A maintainer who reads it a year later can say what the team decided, why, and what would make it wrong. The findings below are small fixes, and none of them blocks the merge.

| Question | Answered | Where | Gap |
|---|---|---|---|
| What did we decide? | Yes | Title | |
| Is it still in force? | Yes | Status | |
| What forced a decision? | Yes | Context | |
| What exactly did we choose? | Yes | Decision | |
| What decides between the options? | Yes | Criteria | |
| What else did we look at, and why not? | Yes | Options | |
| What follows? | Partly | Consequences | No owner for the check of the 200 jobs per second limit |

- Consequences, last bullet: the trigger to decide again is "above 200 jobs per second for 7 days", but no one watches the load. Name who checks it, as the page does for the table size (Dana, each Monday).
- Decision, way back: `JOBS_BACKEND=inline` is described for the resize job only. Say whether it also works for the other jobs of 10 minutes or less that move later, because a job of that length may not fit in a web request.
- Decision, 15-minute stop: the default of pg-boss comes from its documentation, with no source on the page. Not checked. Add a link or the version.
- Options, pg-boss row: the page does not say which job the 350 jobs per second test ran. Not checked. A resize job and a short test job load Postgres in different ways, so name the job.
- Consequences, last sentence: "The target of 200" is a limit that triggers a new decision, not a target the work must reach. Name it a threshold.

Lint: no hard findings.
