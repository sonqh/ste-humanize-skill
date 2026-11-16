Not ready for the backend team. The page has no way back and no success measure, so the team cannot agree on a rollout to all customers on 2026-12-15.

| Question | Answered | Where | Gap |
|---|---|---|---|
| What problem do we solve, and for whom? | Yes | Problem | |
| What must the feature do, and what not? | Partly | Goals | No Non-goals |
| What do we propose? | Partly | Design | No parts, columns, or interface for the job, the file, or the link |
| What else did we look at, and why not? | Partly | Options | No "do nothing". One option. No table or criteria. The chosen design is not compared |
| What do we not know yet? | Partly | Open questions | No test that shows 120,000 invoices finish in time on the worker pool |
| How do we know that it works? | No | nowhere | No target with a number, no way to measure it |
| How does it go out, and how do we go back? | Partly | Rollout | One date. No phases, no flag, no way back |
| What is still open? | Partly | Open questions | `TBD` has no owner and no date |

- Cost: "about $4,000 a month" has no kind and no source. Say who estimated it and from what, or mark it `TBD` with an owner. Not checked.
- Rollout: no way back. Name the flag or the switch that turns the export off for all customers.
- Design: the link in the email expires after 24 hours, but the page does not say who can open it. Name the access rule for the link and for the S3 file.
- Design: the page does not say what happens when the job fails or the email does not arrive. Name the retry and the message to the customer.
- Design: "Pages of 1,000" and "existing worker pool" are claims with no kind. Mark each as measured, estimate, target, or assumption, and give the source.
- Open questions: the tax ID question has no owner and no date. Name the owner, and say in Design that the column depends on the answer.
- Status: "draft" does not say who decides, or by when. Add both for the backend team.

Lint: no hard findings.
