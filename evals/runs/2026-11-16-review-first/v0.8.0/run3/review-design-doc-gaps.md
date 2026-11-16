The page is not ready for the backend team, who must agree on it before the work starts: it never says what they are asked to agree on or by when, and it has no way back, no measure of success, and only one option besides the design.

| Question | Answered | Where | Gap |
|---|---|---|---|
| What problem do we solve, and for whom? | Yes | Problem | |
| What must the feature do, and what not? | Partly | Goals | No Non-goals |
| What do we propose? | Partly | Design | No columns, no interface, no access rule for the S3 link, no failure case |
| What else did we look at? | Partly | Options | No "do nothing", one option, no criteria, no table |
| What do we not know yet? | Partly | Open questions | The tax ID has no check that answers it. The 120,000 case has no test |
| How do we know that it works? | No | nowhere | No target and no way to measure it |
| How does it go out, and how do we go back? | Partly | Rollout | A date only. No phases, no flag, no way back |
| What is still open? | Partly | Open questions | `TBD` with no owner and no date |

- Cost: "about $4,000 a month" has no kind and no source. Say who estimated it and from what, or mark it TBD with an owner. Not checked.
- Rollout: all customers on one date with no way back. Name the flag or the switch that turns the export off.
- Design: the job runs on the existing worker pool, but the page does not say what load an export of 120,000 invoices adds, or what the job does when it fails. Not checked.
- Design: the "24 hours" expiry and the email link have no reason and no access condition. Mark the expiry as target or assumption, and say who may open the link.
- Open questions: the tax ID item has `TBD` with no owner and no date. Add both, and name the check that settles it before the build.
- Title and first lines: the page opens with a status line and gives no request. Add the decision the team makes and the date.
- Cost and Rollout sit before the unknowns and the success measure, and the page has no section for the measure. Move the open items up and add the measure.

Lint: no hard findings.
