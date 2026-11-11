`search_orders` searches the orders that customers placed in the last 90 days and returns them as a list.

The tool is read-only. A call changes nothing, so you can call it as many times as necessary, within the rate limit.

## Parameters

Give `customer_id` or `created_after`, or both. If you give neither, the call fails with error code `ORD-400`, because a search with no filter would scan the whole table. `status` alone is not sufficient and also fails with `ORD-400`.

| Parameter | Type | Meaning |
|---|---|---|
| `customer_id` | string | The id of the customer whose orders you want. |
| `status` | optional, one of `open`, `shipped`, `cancelled`, `refunded` | Returns only orders with this status. If you omit it, the tool returns orders of every status. |
| `created_after` | timestamp, ISO 8601 format in UTC, for example `2026-01-31T00:00:00Z` | Returns only orders created after that moment. |
| `limit` | default 20, maximum 100 | The number of orders to return. The tool does not reject a value above 100. It silently reduces the value to 100. This behavior confused callers before. |
| `cursor` | value of `next_cursor` from the previous response | Gets the next page of results. |

## Results

The tool sorts the results by creation time, newest first. Each order has the fields `id`, `customer_id`, `status`, `total`, `currency`, and `created_at`.

- `total` is in minor units. A `total` of 1999 with `currency` USD means 19.99 dollars. This is a common source of mistakes.
- The results do not include line items. Use `get_order` to get them.

## Pages

When there are more results than `limit`, the response includes the field `next_cursor`.

- To get the next page, make the same call again with `cursor` set to the value of `next_cursor`.
- Keep all other parameters the same. If you change them between pages, the results may be inconsistent.
- When `next_cursor` is absent, there are no more pages.

## Limits

- Orders older than 90 days are in the archive. `search_orders` does not return them, even if `created_after` is an earlier date. The result for that period is empty and the tool raises no error. Use `search_archive` for those orders.
- The search index updates asynchronously. A new order or a status change may take up to 5 minutes to appear in the results. If the tool does not find an order that was just created, the order may not be indexed yet. This does not necessarily mean that the order does not exist. In that situation, use `get_order` with the order id, because `get_order` reads from the primary database.
- The tool allows 60 calls per minute per agent. Above that limit, the call fails with HTTP 429 and the response includes a `retry_after` value in seconds. Wait that number of seconds before you try again. Do not retry immediately.

Cut candidates: the table-scan reason for `ORD-400`, the note that the `limit` reduction confused callers, the note that minor units cause mistakes.
