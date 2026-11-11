`search_orders` searches the orders that customers placed in the last 90 days. It returns them as a list, newest first.

The tool is read-only. A call changes nothing, so you can call it as many times as necessary, within the rate limit below.

## Parameters

The search has four parameters.

| Parameter | Value |
|---|---|
| `customer_id` | String. The id of the customer whose orders you want. |
| `status` | Optional. One of `open`, `shipped`, `cancelled`, or `refunded`. If you omit it, the tool returns orders of every status. |
| `created_after` | Timestamp in ISO 8601 format in UTC, for example `2026-01-31T00:00:00Z`. The tool returns only orders created after that moment. |
| `limit` | The number of orders to return. The default is 20 and the maximum is 100. The tool does not reject a value above 100. It silently reduces the value to 100. This reduction has confused callers before. |

Give at least one of `customer_id` or `created_after`. If you give neither, the call fails with error code `ORD-400`, because a search with no filter would scan the whole table. `status` alone is not sufficient and also fails with `ORD-400`.

## Results

Each order has the fields `id`, `customer_id`, `status`, `total`, `currency`, and `created_at`.

- `total` is in minor units. A `total` of 1999 with `currency` USD means 19.99 dollars. This is a common source of mistakes.
- The results do not include line items. Use `get_order` to get them.
- The tool sorts the results by creation time, newest first.

## Pages

- When there are more results than `limit`, the response includes the field `next_cursor`.
- To get the next page, make the same call again with the `cursor` parameter set to that value. Keep all other parameters the same. If you change them between pages, the results may be inconsistent.
- When `next_cursor` is absent, there are no more pages.

## Limits

- Orders older than 90 days are in the archive, and `search_orders` does not return them. A `created_after` date earlier than that does not change this. The result for that period is empty, and the tool raises no error. Use `search_archive` for those orders.
- The search index updates asynchronously. A new order or a status change may take up to 5 minutes to show in the results.
- If the tool does not find an order that was just created, the index may not contain it yet. This does not necessarily mean that the order does not exist. Call `get_order` with the order id, because `get_order` reads from the primary database.
- The rate limit is 60 calls per minute per agent. Above the limit, the call fails with HTTP 429, and the response includes a `retry_after` value in seconds. Wait that many seconds before you try again. Do not retry immediately.

Cut candidates: the remark that the `limit` reduction has confused callers, the remark that minor units are a common source of mistakes.
