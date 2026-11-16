# Export all invoices as one CSV file

We propose an async export job. The customer clicks Export, we build a CSV in the background, store it in S3, and email a link that expires after 24 hours. Please review the design and agree that a spike comes first. Nobody has tested how long a 120,000-invoice export takes, so we do not commit before the spike.

## Why we need it

Support received 40 tickets tagged "export" in October 2026 (Zendesk report). Customers ask for all their invoices in one file.

Today the only way is the API, which returns 100 invoices per page. The biggest customers have up to 120,000 invoices.

The target is fewer than 10 export tickets per month after launch.

## What we will build

1. The customer clicks Export.
2. A background job builds a CSV of the customer's invoices.
3. The job puts the file in S3, in the bucket in us-east-1.
4. We email the customer a link to the file.
5. The link expires after 24 hours.

We do not build PDF export, scheduled exports, or export of objects other than invoices.

## Which options we looked at

| Option | What it does | Problem |
|---|---|---|
| Async export job (proposed) | Builds the file in the background and emails a link | Export time for a large account is not tested |
| Sync download button | Builds the file while the customer waits | Fine for small accounts. It will time out for big ones |
| Keep telling people to use the API | No new work | The customer still has no single file |

## How we roll it out and go back

The feature sits behind the flag `invoice_export`. We start with a beta of 5 customers, then open it to everyone. To go back, turn the flag off.

## What we do not know yet

- Export time. Huy thinks a 120,000-invoice export is fine, but nobody tested it. We need a spike before we commit.
- Data residency. We assume the S3 bucket in us-east-1 is ok for EU customers. Nobody has asked legal yet.
- Cost and engineering time. We have no estimate. Minh will ask Huy.
- Tax ID column. Finance wants one. We do not know if every invoice has a tax ID.
