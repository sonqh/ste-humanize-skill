`search_orders` searches the orders that customers placed and returns them as a list. Use it for orders from the last 90 days. You must give `customer_id`, `created_after`, or both.

The tool is read-only. A call changes nothing, so you can call the tool as many times as necessary, within the rate limit below.

Parameters:

- `customer_id`: a string. It is the id of the customer whose orders you want.
- `status`: optional. It is one of `open`, `shipped`, `cancelled`, or `refunded`. If you do not give it, the tool returns orders of every status.
- `created_after`: a timestamp in ISO 8601 format in UTC, for example `2026-01-31T00:00:00Z`. The tool returns only orders created after that moment.
- `limit`: the number of orders to return. The default is 20 and the maximum is 100. The tool does not reject a value above 100. It silently reduces the value to 100. This has confused callers before.
- `cursor`: the `next_cursor` value from the previous page. Refer to "Pages" below.

Required filter:

- Give at least one of `customer_id` or `created_after`. This rule is easy to miss.
- If you give neither, the call fails with error code `ORD-400`. A search with no filter would scan the whole table.
- `status` alone is not sufficient. That call also fails with `ORD-400`.

Results:

- The tool sorts the results by creation time, with the newest order first.
- Each order has the fields `id`, `customer_id`, `status`, `total`, `currency`, and `created_at`.
- `total` is in minor units. A `total` of 1999 with `currency` USD means 19.99 dollars. This is a common source of mistakes.
- The results do not include line items. Use `get_order` to get them.

Pages:

- When there are more results than `limit`, the response includes the field `next_cursor`.
- To get the next page, make the same call again with `cursor` set to that value. Keep all other parameters the same.
- If you change the other parameters between pages, the results may be inconsistent.
- When `next_cursor` is absent, there are no more pages.

Orders older than 90 days:

- The system moves orders older than 90 days to the archive. `search_orders` does not return them.
- This is true even when `created_after` is an earlier date. The result is empty for that period, and the tool raises no error.
- Use `search_archive` for those orders.

Freshness:

- The search index updates asynchronously. A new order or a status change may take up to 5 minutes to appear in the results.
- If the tool does not find an order that was just created, the index may not contain the order yet. The order may still exist.
- In that situation, use `get_order` with the order id. `get_order` reads from the primary database.

Rate limit:

- The tool permits 60 calls per minute per agent.
- Above that limit, the call fails with HTTP 429. The response includes a `retry_after` value in seconds.
- Wait that number of seconds, then try again. Do not retry immediately.

Cut candidates: "This has confused callers before", "This rule is easy to miss", "This is a common source of mistakes".
