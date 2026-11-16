# Export all invoices as one CSV file

We propose an async export job. The customer clicks Export, a background job builds a CSV of all their invoices and puts it in S3, and we email a link. The link expires after 24 hours. We ask the backend team to review this approach and to agree to a spike on export time before we commit. We do not know the cost or the engineering time yet. Minh will ask Huy.

## Why do this

Support got 40 tickets tagged "export" in October 2026 (Zendesk report). Customers ask for all their invoices in one file.

Today the only way is the API, which returns 100 invoices per page. The biggest customers have up to 120,000 invoices, so one full export takes 1,200 requests.

Minh's target is fewer than 10 export tickets per month after launch.

## What we will not do

- PDF export.
- Scheduled exports.
- Export of objects other than invoices.

## Which options did we consider

| Option | What it means | Problem |
|---|---|---|
| Async export job | Build the CSV in the background, store it in S3, email a link | Export time for a large account is not tested |
| Sync download button | The customer clicks and the file downloads at once | Fine for small accounts. It will time out for big ones |
| Keep telling people to use the API | No change | This is the source of the tickets today |

We recommend the async job. The sync button does not work for the biggest customers, and the API path is what customers complain about now.

## What can go wrong

- Export time is unknown. Nobody has tested a 120,000-invoice export. Huy thinks it is fine. The spike must measure it before we commit.
- Data residency is unchecked. We assume the S3 bucket in us-east-1 is acceptable for EU customers. Nobody has asked legal.
- The tax ID column is undecided. Finance wants it. We do not know whether every invoice has a tax ID.

## How do we roll out and go back

The feature goes behind the flag `invoice_export`. We start with a beta for 5 customers, then open it to everyone. To go back, turn the flag off.

## What we do not know yet

- Cost and engineering time. Minh will ask Huy.
- How long a 120,000-invoice export takes.
- Whether legal accepts us-east-1 for EU customers.
- Whether every invoice has a tax ID.
