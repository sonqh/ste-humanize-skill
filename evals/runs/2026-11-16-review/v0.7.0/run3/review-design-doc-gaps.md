# Design doc: export all invoices as one CSV file

Status: draft, 2026-11-15.

## Problem

Customers ask support for all their invoices in one file. Support got 40 tickets with the tag "export" in October 2026. Today a customer can only page through the API, 100 invoices per page. The largest accounts have 120,000 invoices.

## Goals

- A customer exports all invoices as one CSV file.
- The export works for an account with 120,000 invoices.

## Non-goals

- TBD (owner unknown).

## Proposed design

The customer clicks Export. A background job builds the CSV and puts it in S3. We email a link to the file. The link expires after 24 hours.

The job runs on the existing worker pool. It reads invoices in pages of 1,000 and writes each page to the file.

## Other options

- Do nothing. Customers keep paging through the API, 100 invoices per page. This meets neither goal.
- A sync download button. It is fast for small accounts. It times out for large ones, so it does not meet the second goal.

## Cost

The S3 storage and the email cost about $4,000 a month. The source of this number, and whether it is measured or estimated: TBD (owner unknown).

## How we know it works

TBD (owner unknown). The page gives no target and no way to measure one.

## Rollout

We will release the feature to all customers on 2026-12-15. The phases, the flag or switch, and the way back: TBD (owner unknown).

## Open questions

- Does every invoice have a tax ID? Finance wants a column for it. TBD (owner unknown).
- What are the non-goals? TBD (owner unknown).
- What is the source of the $4,000 a month, and is it measured or estimated? TBD (owner unknown).
- What target shows that the export works, and how does the team measure it? TBD (owner unknown).
- What are the rollout phases, and how does the team go back? TBD (owner unknown).

Cut candidates: none.
