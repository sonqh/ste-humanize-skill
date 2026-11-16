**Verdict:** The page is not ready for the backend team to agree on, because it gives no way back and no flag for a release to all customers on 2026-12-15.

| Question | Answered | Where | Gap |
|---|---|---|---|
| What problem do we solve, and for whom? | Yes | Problem | |
| What must the feature do, and what not? | Partly | Goals | No Non-goals |
| What do we propose? | Partly | Design | No interface, no CSV columns, no failure behavior of the job |
| What else did we look at? | Partly | Options | No "do nothing", one option, no criteria |
| What do we not know yet? | Partly | Open questions | The tax ID has no spike or test that answers it |
| How do we know that it works? | No | Nowhere | No target and no measure |
| How does it go out, and how do we go back? | Partly | Rollout | One date, no phases, no flag, no way back |
| What is still open? | Partly | Open questions | `TBD` with no owner and no date |

- Cost: "about $4,000 a month" has no kind and no source. Say who estimated it and from what. Cost of the job on the worker pool is not stated. Not checked.
- Rollout: no way back. Name the flag or the switch that turns the export off, and say whether all customers get it on one day.
- Design: risks are missing. Say what happens when the job fails part way, and who may open the emailed link to the S3 file during its 24 hours.
- Rollout: "2026-12-15" has no kind. Say whether it is a target or an estimate, and use "will" for the plan.
- Open questions: the `TBD` on the tax ID has no owner and no date. Finance wants a column, but Goals and Design do not mention it.
- Options: the sync button loses only because it "times out for large ones". Give the limit, with its source. Add "do nothing" first and score the options on the same criteria.
- Goals: "works for an account with 120,000 invoices" has no target. Name the time or the limit that counts as working, and how the team measures it. The 120,000 figure has no source or date. Not checked.

Lint: no hard findings.
