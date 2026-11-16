# Design doc: invoice export as an async job

We propose an async export job that builds one CSV of a customer's invoices and emails a link. We cannot commit yet. Nobody has measured how long an export of 120,000 invoices takes, so we need a spike first. Cost and engineering time are not known. Minh will ask Huy.

This doc is for the backend team. We ask you to challenge the approach and the open questions before anyone starts work.

## Problem

Customers ask for all their invoices in one file. Support received 40 tickets tagged "export" in October 2026 (Zendesk report, pulled by Minh).

Today the only way is the API, which returns 100 invoices per page. The biggest customers have up to 120,000 invoices.

## Goal

Export tickets fall below 10 per month after launch. This target comes from Minh.

## Proposed design

1. The customer clicks Export.
2. We build a CSV in the background.
3. We put the file in S3.
4. We email the customer a link. The link expires after 24 hours.

We do not know the CSV columns yet. See the open question on the tax ID column.

## Not in scope

- PDF export.
- Scheduled exports.
- Export of objects other than invoices.

## Options we looked at

- Async export job (proposed). It works for the largest accounts. We have not tested how long it takes for 120,000 invoices. Huy thinks it is fine.
- Sync download button. It is fine for small accounts. It will time out for big ones.
- Keep telling customers to use the API. It costs us nothing to build, and the tickets stay.

## Risks and open questions

- Export time. Nobody knows how long a 120,000 invoice export takes. We need a spike before we commit.
- Data residency. We assume the S3 bucket in us-east-1 is acceptable for EU customers. Nobody has asked legal.
- Tax ID column. Finance wants one. We do not know if every invoice has a tax ID.
- Cost and engineering time. Not estimated. Minh will ask Huy.

## Rollout and way back

The feature goes behind the flag `invoice_export`. We start with a beta of 5 customers, then open it to everyone. To go back, turn the flag off.
