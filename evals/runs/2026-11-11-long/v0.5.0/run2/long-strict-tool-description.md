`search_orders` searches the orders that customers placed and returns them as a list. It returns only orders from the last 90 days.

Give `customer_id`, `created_after`, or both. If you give neither, the call fails with error code `ORD-400`, because a search with no filter would scan the whole table. `status` alone is not sufficient and also fails with `ORD-400`. This rule is important and easy to miss.

The tool is read-only. A call changes nothing, so you can call the tool as many times as necessary, within the rate limit below.

## Parameters

The tool has four search parameters.

| Parameter | Meaning | Rules |
|---|---|---|
| `customer_id` | The id of the customer whose orders you want. | String. |
| `status` | The order status to return. | Optional. One of `open`, `shipped`, `cancelled`, `refunded`. If you omit it, the tool returns orders of every status. |
| `created_after` | The tool returns only orders created after this moment. | Timestamp in ISO 8601 format, in UTC. Example: `2026-01-31T00:00:00Z`. |
| `limit` | The number of orders to return. | Default 20. Maximum 100. The tool does not reject a value above 100. It silently reduces the value to 100. This has confused callers before. |

## Results

- The tool sorts the results by creation time, newest first.
- Each order has the fields `id`, `customer_id`, `status`, `total`, `currency`, and `created_at`.
- `total` is in minor units. A `total` of 1999 with `currency` USD means 19.99 dollars. This is a common source of mistakes.
- The results do not include line items. Call `get_order` to get them.

## Pages

- When there are more results than `limit`, the response includes the field `next_cursor`.
- To get the next page, make the same call again with the `cursor` parameter set to that value.
- Keep all other parameters the same. If you change them between pages, the results may be inconsistent.
- When `next_cursor` is absent, there are no more pages.

## Orders older than 90 days

- The system moves orders older than 90 days to the archive. `search_orders` does not return them.
- This is true even when `created_after` is an earlier date. The result for that period is empty, and the tool raises no error.
- Call `search_archive` for those orders.

## Freshness

- The search index updates asynchronously. A new order or a status change can take up to 5 minutes to appear in the results.
- If you do not find an order that was just created, the index possibly does not contain it yet. This does not necessarily mean that the order does not exist.
- In that situation, call `get_order` with the order id. `get_order` reads from the primary database.

## Rate limit

- The tool permits 60 calls per minute per agent.
- When you exceed the limit, the call fails with HTTP 429. The response includes a `retry_after` value in seconds.
- Wait that number of seconds before you call again. Do not retry immediately.

Cut candidates: the "easy to miss" sentence, the "confused callers" sentence, the "common source of mistakes" sentence, the table-scan reason for `ORD-400`.
Reader: an agent that decides when and how to call `search_orders`.
