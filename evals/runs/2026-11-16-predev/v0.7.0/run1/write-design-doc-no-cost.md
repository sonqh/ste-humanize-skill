# Design doc: invoice export

We propose an async export job. The customer clicks Export, we build a CSV in the background, and we email a link to it. We ask the backend team to review this design, and to say whether a spike on export time must come before the work starts. Cost and engineering time are not known yet.

## Problem

Customers ask for all their invoices in one file. Support had 40 tickets with the tag "export" in October 2026 (Zendesk report, pulled by Minh).

Today the only way to get invoices out is the API. It returns 100 invoices per page. The biggest customers have up to 120,000 invoices, so one customer needs up to 1,200 requests.

## Goals

- A customer can get all their invoices in one CSV file.
- The export works for accounts with 120,000 invoices.
- Export tickets fall below 10 per month after launch.

## Non-goals

- PDF export.
- Scheduled exports.
- Export of objects other than invoices.

## Proposed design

1. The customer clicks Export.
2. We start an export job in the background.
3. The job builds a CSV of the invoices of the customer.
4. The job puts the CSV in S3.
5. We email the customer a link to the file.
6. The link expires after 24 hours.

We have not chosen the job runner, the CSV columns, or the interface between the UI and the job. The team decides these in review. Finance asks for a tax ID column. It is not known whether every invoice has a tax ID (see Open questions).

## Options

| Option | Works for 120,000 invoices | Removes the need for the API | Cost and engineering time |
|---|---|---|---|
| Do nothing: keep telling people to use the API | Yes, with 1,200 requests | No | None |
| Sync download button | No. It is fine for small accounts and will time out for big ones | Yes, for small accounts | TBD (Minh asks Huy, no date set) |
| Async export job (proposed) | Not tested. Huy thinks it is fine | Yes | TBD (Minh asks Huy, no date set) |

The "do nothing" option loses because it leaves the cause of the 40 tickets in place. The sync button loses because it fails for the biggest customers, who have the most invoices to export. The async job is the only option that is expected to work for every account size.

## What we do not know yet

- Export time. Nobody knows how long an export of 120,000 invoices takes. Huy thinks it is fine, but nobody tested it. We will run a spike on a 120,000 invoice account before we commit to the design.
- Data residency. We assume that the S3 bucket in us-east-1 is acceptable for EU customers. Nobody has asked legal yet.
- Cost and engineering time. Minh will ask Huy.

## Success measure

The target is fewer than 10 tickets per month with the tag "export" after launch. The baseline is 40 in October 2026. Support measures it with the same Zendesk report.

## Rollout and way back

1. Put the feature behind the flag `invoice_export`.
2. Run a beta with 5 customers.
3. Turn the flag on for everyone.

To go back, turn the flag off.

## Open questions

- Export time of 120,000 invoices: who runs the spike, and by when? TBD (owner unknown, no date set).
- Does every invoice have a tax ID, and does the CSV need that column? TBD (owner unknown, no date set).
- Is us-east-1 acceptable for EU customers? TBD (legal, not yet asked, no date set).
- What are the cost and the engineering time? TBD (Minh asks Huy, no date set).

Missing: cost and engineering time, the owner and date of the spike, the owner and date of the tax ID answer, the owner and date of the legal answer, and the job runner, CSV columns, and interface.
