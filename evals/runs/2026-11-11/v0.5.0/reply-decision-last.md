I think we should delete the 6 orphan rows first and then run the migration again. If finance still needs those rows for the 2023 audit, we may have to archive them instead.

The migration adds a NOT NULL column to the orders table, and 6 rows in production have no customer_id. That is why the constraint fails.

I looked at two other fixes:

- Backfill the rows. The customers were deleted in 2023, so there is no data to backfill from.
- Make the column nullable. That defeats the purpose of the change.

Cut candidates: the sentence that says what the migration adds (the reviewer may already know it).
