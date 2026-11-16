# Design doc: export all invoices as one CSV file

Status: draft, 2026-11-15. The backend team must agree on this design before the work starts.

## Problem

Customers ask support for all their invoices in one file. Support got 40 tickets with the tag "export" in October 2026.

Today a customer can only page through the API, 100 invoices per page. The largest accounts have 120,000 invoices.

## Goals and non-goals

Goals:

- A customer exports all invoices as one CSV file.
- The export works for an account with 120,000 invoices.

Non-goals: TBD (owner unknown).

## Proposed design

The customer clicks Export. A background job builds the CSV and puts it in S3. We email a link to the file. The link expires after 24 hours.

The job runs on the existing worker pool. It reads invoices in pages of 1,000 and writes each page to the file.

## Options

- Do nothing. Customers keep paging the API, 100 invoices per page.
- A sync download button. It is fast for small accounts. It times out for large ones, so it fails the second goal.
- A background job with an emailed link. This is the proposed design.

## What we do not know yet

- We have no test of the job on an account with 120,000 invoices on the existing worker pool. Test: TBD (owner unknown).
- The cost is an estimate: about $4,000 a month for the S3 storage and the email. The author and the basis of the estimate are TBD (owner unknown).

## How we know it works

Measure of success: TBD (owner unknown).

## Rollout

We will release the feature to all customers on 2026-12-15. The flag and the way back are TBD (owner unknown).

## Open questions

- Does every invoice have a tax ID? Finance wants a column for it. Answer: TBD (owner unknown).
- What are the non-goals? TBD (owner unknown).
- What is the measure of success? TBD (owner unknown).
- What is the way back if the release fails? TBD (owner unknown).
- Who made the cost estimate, and from what? TBD (owner unknown).
