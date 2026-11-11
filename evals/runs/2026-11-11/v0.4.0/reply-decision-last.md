I think we should delete the 6 orphan rows first, then run the migration again. If finance still needs those rows for the 2023 audit, we may have to archive them instead.

The constraint fails because 6 rows in production have no customer_id. The migration adds a NOT NULL column to the orders table. We cannot backfill those rows: the customers were deleted in 2023, so there is no data to backfill from. I also considered a nullable column, but that defeats the purpose of the change.

Cut candidates: the sentence that says what the migration adds, if the reviewer already knows the change.
