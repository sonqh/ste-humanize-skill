**Verdict:** The backend team cannot agree on this design doc yet, so it is not ready. The one gap that stops them most is that it has no way back and no flag in Rollout, and it ships to all customers at once.

| Question | Answered | Where | Gap |
|---|---|---|---|
| What problem do we solve, and for whom? | Yes | Problem | |
| What must the feature do, and what not? | Partly | Goals | No Non-goals |
| What do we propose? | Partly | Design | No interface, no CSV columns, no failure case |
| What else did we look at? | Partly | Options | One option. No "do nothing". No criteria. No reason it loses |
| What do we not know yet? | Partly | Open questions | Only the tax ID. No test for 120,000 invoices |
| How do we know that it works? | No | nowhere | No target with a number, no measure |
| How does it go out, and how do we go back? | Partly | Rollout | One date. No phases, no flag, no way back |
| What is still open? | Partly | Open questions | The `TBD` has no owner and no date |

- Cost: "about $4,000 a month" has no kind and no source. It may be an estimate or a guess. Say who worked it out and from what. Not checked.
- Design: the doc does not show that "the existing worker pool" can carry a job for 120,000 invoices. Mark this as an assumption, or name the test that checks it.
- Design: it names no failure case. Add what happens when the job fails halfway, and who sees the error.
- Rollout: the doc sets a release to all customers on 2026-12-15 and names no flag or switch that turns the export off. Add one.
- Options: the table is missing "do nothing" and any shared criteria. Score the sync button and the background job on the same criteria, and say why the button loses.
- Open questions: the tax ID `TBD` has no owner. Name the owner and a date, for example Finance. Also say what the team does if some invoices have no tax ID.
- Status: the page does not say who must agree, or by when. Add the decider and the date.

Lint: no hard findings.
