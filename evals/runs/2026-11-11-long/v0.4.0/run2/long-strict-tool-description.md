`search_orders` searches the orders that customers placed and returns them as a list. It returns only orders from the last 90 days. For older orders, use `search_archive`.

The tool is read-only. A call changes nothing, so you can call it as many times as necessary. The rate limit below applies.

## Parameters

- `customer_id` (string): the id of the customer whose orders you want.
- `status` (optional): one of `open`, `shipped`, `cancelled`, or `refunded`. If you do not give `status`, the tool returns orders of every status.
- `created_after` (timestamp): ISO 8601 format in UTC, for example `2026-01-31T00:00:00Z`. The tool returns only orders created after that moment.
- `limit`: the number of orders to return. The default is 20. The maximum is 100. The tool does not reject a value above 100. It silently reduces the value to 100. This confused callers before.

You must give at least one of `customer_id` or `created_after`. If you give neither, the call fails with error code `ORD-400`, because a search with no filter would scan the whole table. `status` alone is not sufficient. That call also fails with `ORD-400`.

## Results

The tool sorts the results by creation time, newest first. Each order has the fields `id`, `customer_id`, `status`, `total`, `currency`, and `created_at`.

- `total` is in minor units. A `total` of 1999 with `currency` USD means 19.99 dollars. This is a common source of mistakes.
- The results do not include line items. Use `get_order` to get them.

## Pages

When there are more results than `limit`, the response includes a `next_cursor` field. To get the next page, make the same call again with the `cursor` parameter set to that value. Keep all other parameters the same. If you change them between pages, the results may be inconsistent. When the response has no `next_cursor`, there are no more pages.

## Limits

- The system moves orders older than 90 days to the archive. `search_orders` does not return them, even if `created_after` is an earlier date. The result for that period is empty, and the tool raises no error. Use `search_archive` for those orders.
- The search index updates asynchronously. A new order or a status change may take up to 5 minutes to appear in the results. If the tool does not find an order that was just created, the index may not contain it yet. An empty result does not necessarily mean that the order does not exist. In that situation, call `get_order` with the order id. `get_order` reads from the primary database.
- The tool allows 60 calls per minute per agent. Above that limit, the call fails with HTTP 429. The response includes a `retry_after` value in seconds. Wait that number of seconds before you call again. Do not retry immediately.

Cut candidates: "This confused callers before", "This is a common source of mistakes", the reason for `ORD-400` (a full table scan).
