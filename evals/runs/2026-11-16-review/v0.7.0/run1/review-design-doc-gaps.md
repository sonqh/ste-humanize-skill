# Design doc: invoice export

Status: draft, 2026-11-15.

## Problem

Customers cannot get all their invoices in one file. Support got 40 tickets with the tag "export" in October 2026. Today a customer can only page through the API, 100 invoices per page. The largest accounts have 120,000 invoices.

## Goals

- A customer exports all invoices as one CSV file.
- The export works for an account with 120,000 invoices.

## Non-goals

- TBD (owner unknown, date unknown). The draft names no non-goal.

## Proposed design

The customer clicks Export. A background job builds the CSV and puts it in S3. We will email a link to the file. The link expires after 24 hours.

The job runs on the existing worker pool. It reads invoices in pages of 1,000 and writes each page to the file.

Not known yet: whether the worker pool can run a job for an account with 120,000 invoices. TBD (owner unknown, date unknown).

## Options

| Option | Result | Why it loses or wins |
|---|---|---|
| Do nothing | Customers keep paging through the API, 100 invoices per page. | TBD (owner unknown). The draft gives no score. |
| A sync download button | It is fast for small accounts. It times out for large ones. | It fails the second goal, an account with 120,000 invoices. |
| Background job and emailed link | The design above. | TBD (owner unknown). The draft gives no score. |

The draft names no criteria for the options. TBD (owner unknown, date unknown).

## Cost

The S3 storage and the email cost about $4,000 a month. This is an estimate. Who made it, and from what, is TBD (owner unknown).

## How we know it works

The measure of success is TBD (owner unknown, date unknown). The draft gives no target and no way to measure it.

## Rollout

We will release the feature to all customers on 2026-12-15. The flag or switch, the phases, and the way back are TBD (owner unknown, date unknown).

## Open questions

- Does every invoice have a tax ID? Finance wants a column for it. TBD (owner unknown, date unknown).
- Can the worker pool run the job for 120,000 invoices? TBD (owner unknown, date unknown).
- Which non-goals, criteria, success target, and way back apply? TBD (owner unknown, date unknown).
