# Design doc: export all invoices as one CSV file

Status: draft for review by the backend team, 2026-11-14.

We propose an async export job. The customer clicks Export, we build a CSV in the background, and we email a link to it. We have not tested how long the largest export takes. We need a spike before we commit to the design. Cost and engineering time are not known yet.

## Problem

Customers cannot get all their invoices in one file. The only way today is the API, which returns 100 invoices per page. The biggest customers have up to 120,000 invoices, so one full copy takes 1,200 requests.

Support received 40 tickets with the tag "export" in October 2026 (Zendesk report, pulled by Minh). Customers ask for all their invoices in one file.

## Goals

- A customer can get all their invoices in one CSV file.
- The export works for an account with 120,000 invoices.
- Export tickets fall below 10 per month after launch.

## Non-goals

- PDF export.
- Scheduled exports.
- Export of objects other than invoices.

## Proposed design

1. The customer clicks Export.
2. We build a CSV in the background.
3. We put the file in S3.
4. We email the customer a link to the file.
5. The link expires after 24 hours.

We assume that the S3 bucket in us-east-1 is acceptable for EU customers. Nobody has asked legal about data residency.

## Options we looked at

| Option | Works for 120,000 invoices | Customer effort | Status |
|---|---|---|---|
| Do nothing: keep telling customers to use the API | Yes, in 1,200 requests | High: the customer writes code | Does not remove the tickets |
| Sync download button | No: it will time out for big accounts | Low | Fine for small accounts only |
| Async export job (proposed) | Expected. Not tested | Low: one click and an email | Needs the spike |

The sync button loses because the largest customers are the ones who ask. Doing nothing loses because it keeps the cause of the 40 tickets.

## What we do not know yet

- How long a 120,000-invoice export takes. Huy thinks it is fine. Nobody has tested it. We will run a spike before the work depends on this design.
- Whether us-east-1 is acceptable for EU customers. This is an assumption.
- The cost and the engineering time. We have no estimate.

## How we measure success

The target is fewer than 10 export tickets per month after launch. Minh set the target. The baseline is 40 tickets in October 2026, from the same Zendesk tag.

## Rollout and way back

1. We ship behind the flag `invoice_export`.
2. We run a beta with 5 customers.
3. We open the feature to everyone.

To go back, turn the flag off.

## Open questions

- Cost and engineering time: TBD (Minh asks Huy, date unknown).
- Export time for 120,000 invoices: TBD (owner unknown, date unknown). The spike answers it.
- Data residency of us-east-1 for EU customers: TBD (owner unknown, date unknown). Legal must answer.
- Finance wants a tax ID column. It is unclear whether every invoice has a tax ID. TBD (owner unknown, date unknown).

Missing: cost, engineering time, owner and date of the spike, owner of the legal question, owner of the tax ID question, and the dates of all open questions.
