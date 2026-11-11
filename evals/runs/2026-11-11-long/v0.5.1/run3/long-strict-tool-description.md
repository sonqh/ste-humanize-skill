`search_orders` searches the orders that customers placed and returns them as a list. It returns only orders from the last 90 days.

The tool is read-only. A call changes nothing, so you can call it as many times as necessary, within the rate limit below.

## When to use a different tool

- For orders older than 90 days, use `search_archive`.
- For the line items of an order, use `get_order`.
- For an order that was just created and is not in the results, use `get_order` with the order id.

## Parameters

| Parameter | Value | Effect |
|---|---|---|
| `customer_id` | A string. | The id of the customer whose orders you want. |
| `status` | Optional. One of `open`, `shipped`, `cancelled`, or `refunded`. | If you do not give it, the tool returns orders of every status. |
| `created_after` | A timestamp in ISO 8601 format in UTC, for example `2026-01-31T00:00:00Z`. | The tool returns only orders created after that moment. |
| `limit` | The number of orders to return. The default is 20 and the maximum is 100. | The tool does not reject a value above 100. It silently reduces the value to 100. This has confused people before. |
| `cursor` | The `next_cursor` value from the previous response. | The tool returns the next page. Refer to "Pages". |

## Required filter

This rule is important and easy to miss. Give at least one of `customer_id` or `created_after`.

- If you give neither, the call fails with the error code `ORD-400`. A search with no filter would scan the whole table.
- If you give only `status`, the call also fails with `ORD-400`.

## Results

The tool sorts the results by creation time, newest first.

Each order has the fields `id`, `customer_id`, `status`, `total`, `currency`, and `created_at`.

- `total` is in minor units. A `total` of 1999 with `currency` USD means 19.99 dollars. This is a common source of mistakes.
- The results do not include line items. Use `get_order` to get them.

## Pages

- If there are more results than `limit`, the response includes the field `next_cursor`.
- To get the next page, make the same call again with `cursor` set to that value. Keep all other parameters the same.
- If you change the other parameters between pages, the results may be inconsistent.
- If `next_cursor` is absent, there are no more pages.

## Limits

- Orders older than 90 days: the system moves these orders to the archive, and `search_orders` does not return them. This is true even if `created_after` is an earlier date. The result for that period is empty and the tool raises no error. Use `search_archive` for these orders.
- Freshness: the system updates the search index asynchronously. A new order or a status change may take up to 5 minutes to appear in the results. If the tool does not find an order that was just created, the index may not contain it yet. This does not necessarily mean that the order does not exist. In that situation, use `get_order` with the order id, because `get_order` reads from the primary database.
- Rate limit: the tool allows 60 calls per minute per agent. Above the limit, the call fails with HTTP 429, and the response includes a `retry_after` value in seconds. Wait that many seconds before you try again. Do not retry immediately.

Cut candidates: "This has confused people before" (limit), "important and easy to miss" (required filter), "This is a common source of mistakes" (total).
