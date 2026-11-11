`search_orders` searches the orders that customers placed in the last 90 days and returns them as a list.

The tool is read-only. A call changes nothing, so you can call it as many times as necessary without side effects. The rate limit below still applies.

Use a different tool in these cases:

- You need orders older than 90 days. Use `search_archive`.
- You need the line items of an order. Use `get_order`.
- The search does not find an order that was just created. Use `get_order` with the order id.

## Parameters

Give at least one of `customer_id` or `created_after`. If you give neither, the call fails with error code `ORD-400`, because a search with no filter would scan the whole table. `status` alone is not sufficient. That call also fails with `ORD-400`.

- `customer_id` (string): the id of the customer whose orders you want.
- `status` (optional): one of `open`, `shipped`, `cancelled`, or `refunded`. If you do not give it, the tool returns orders of every status.
- `created_after` (timestamp): ISO 8601 format in UTC, for example `2026-01-31T00:00:00Z`. The tool returns only orders created after that moment.
- `limit`: the number of orders to return. The default is 20 and the maximum is 100. The tool does not reject a value above 100. It silently reduces the value to 100. This confused people before.

## Results

The tool sorts the results by creation time, newest first. Each order has these fields: `id`, `customer_id`, `status`, `total`, `currency`, and `created_at`.

`total` is in minor units. For example, 1999 with currency USD means 19.99 dollars. This is a common source of mistakes.

The results do not include line items.

## Pages

When there are more results than `limit`, the response includes a `next_cursor` field. To get the next page, make the same call again with the `cursor` parameter set to that value. Keep all other parameters the same. If you change them between pages, the results may be inconsistent. When `next_cursor` is absent, there are no more pages.

## Limits

- Age. Orders older than 90 days are moved to the archive, and `search_orders` does not return them. This is also true when `created_after` is an earlier date. The result is empty for that period, and the tool raises no error.
- Freshness. The search index updates asynchronously. A new order or a status change may take up to 5 minutes to appear in the results. If the search does not find a new order, the index possibly does not contain it yet. The order can still exist. `get_order` reads from the primary database, so it can find that order.
- Rate. The tool permits 60 calls per minute per agent. Above that limit, the call fails with HTTP 429, and the response includes a `retry_after` value in seconds. Wait that number of seconds before you call again. Do not retry immediately.

Kept as-is: "are moved to the archive" stays passive because the source does not name the actor.
Cut candidates: "This confused people before", "This is a common source of mistakes", the table-scan reason for `ORD-400`.
