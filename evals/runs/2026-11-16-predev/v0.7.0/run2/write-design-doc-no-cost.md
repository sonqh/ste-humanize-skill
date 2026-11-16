# Export all invoices as a CSV file

We propose an async export job. The customer clicks Export, the backend builds a CSV in the background, and the customer gets an email with a link to the file. Please agree to the design, ask for a change, or add an open question.

Three facts are not known yet: how long a 120,000-invoice export takes, whether the S3 bucket may hold EU data, and what the work costs. We need a spike before we commit.

## What problem do we solve?

Support received 40 tickets tagged "export" in October 2026 (Zendesk report, pulled by Minh). Customers ask for all their invoices in one file.

Today the only way is the API, which returns 100 invoices per page. The biggest customers have up to 120,000 invoices, so one full copy takes 1,200 pages.

## Goals and non-goals

Goals:

- A customer can get all their invoices in one CSV file.
- The export works for accounts with up to 120,000 invoices.

Non-goals:

- PDF export.
- Scheduled exports.
- Export of objects other than invoices.

## What do we propose?

1. The customer clicks Export.
2. A background job builds a CSV of the customer's invoices.
3. The job puts the file in S3. We assume the bucket in us-east-1 is acceptable for EU customers. Nobody has asked legal about data residency yet.
4. The customer gets an email with a link to the file.
5. The link expires after 24 hours.

Finance wants a tax ID column. We do not know if every invoice has a tax ID, so the column is an open question.

## What else did we look at?

| Option | What it does | Result |
|---|---|---|
| Do nothing | Keep telling customers to use the API | The 40 tickets a month may continue. The biggest accounts need 1,200 requests for one copy. |
| Sync download button | The file downloads when the customer clicks | Fine for small accounts. The team expects it to time out for big accounts. Nobody tested this. |
| Async export job | The design above | Works for any size if the build time is acceptable. Build time for 120,000 invoices is not tested. |

We recommend the async export job. The sync button does not meet the goal for the biggest accounts.

## What do we not know yet?

- Build time for 120,000 invoices. Huy thinks it is fine, but nobody tested it. We need a spike before the work depends on the design. Spike: TBD (owner unknown).
- Data residency of the us-east-1 bucket for EU customers. This is an assumption. Legal: TBD (owner unknown).
- Cost and engineering time: TBD (Minh will ask Huy, date unknown).
- Tax ID on every invoice: TBD (owner unknown).

## How do we know that it works?

The target from Minh is fewer than 10 export tickets per month after launch. The baseline is 40 tickets in October 2026.

## How does it go out, and how do we go back?

The feature ships behind the flag `invoice_export`.

1. Turn the flag on for a beta with 5 customers.
2. Turn the flag on for everyone.

To go back, turn the flag off.

## What is still open?

- How long does a 120,000-invoice export take? Owner: TBD (owner unknown).
- Is the us-east-1 bucket acceptable for EU customers? Owner: TBD (owner unknown).
- What do the work and the run cost? Owner: Minh, with Huy.
- Does every invoice have a tax ID, and do we add the column? Owner: TBD (owner unknown).

Missing: an owner and a date for the spike, the legal question, and the tax ID question. The cost and the engineering time. The way the team measures the ticket target.
