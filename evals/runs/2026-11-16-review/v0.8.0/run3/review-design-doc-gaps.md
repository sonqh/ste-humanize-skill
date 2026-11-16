The backend team can't agree on this yet: the doc is not ready. The one gap that stops them most is the rollout. It releases to all customers on one date with no phases, no flag, and no way back.

| Question | Answered | Where | Gap |
|---|---|---|---|
| What problem do we solve, and for whom? | Yes | Problem | |
| What must the feature do, and what not? | Partly | Goals | No non-goals |
| What do we propose? | Partly | Design | No interface for the job or the file, no CSV columns, no failure handling |
| What else did we look at? | Partly | Options | No "do nothing", one option only, no criteria, no reason it loses |
| What do we not know yet? | Partly | Open questions | No spike or test for any unknown |
| How do we know that it works? | No | Nowhere | No target with a number, no way to measure it |
| How does it go out, and how do we go back? | Partly | Rollout | One date for all customers, no flag, no way back |
| What is still open? | Partly | Open questions | The one `TBD` has no owner and no date |

- Cost: "about $4,000 a month" has no kind and no source. Say who estimated it and from what, or mark it as an assumption. Not checked.
- Design: the doc does not say what the job does if it fails, or how it handles an export that exceeds the 24-hour link limit. Add the failure cases and the retry rule.
- Design: the doc does not say whether the worker pool has room for a 120,000-invoice job. Add a measured number or mark it as an assumption. Not checked.
- Goals: "works for an account with 120,000 invoices" gives no time limit. Add a target, such as a maximum export time.
- Open questions: "Does every invoice have a tax ID? TBD." has no owner or date. Name the owner, such as Finance, and a date. Say what the design does if the answer is no.
- Rollout: the date 2026-12-15 has no kind. Say whether it is a target or a commitment.
- Problem: the "40 tickets" figure has a source and a month, but it gives no scale. Add the total of tickets that month, or the number of affected accounts.

Lint: no hard findings.
