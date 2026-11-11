search_orders searches the orders that customers placed in the last 90 days and returns them as a list. The tool is read-only. A call changes nothing, so you can call it as many times as necessary without side effects, within the rate limit below.

## Required filter

Give customer_id, created_after, or both. If you give neither, the call fails with error code ORD-400. status alone is not sufficient and also fails with ORD-400. A search with no filter would scan the whole table.

## Parameters

- customer_id (string): the id of the customer whose orders you want.
- status (optional): one of open, shipped, cancelled, or refunded. If you do not give it, the tool returns orders of every status.
- created_after: a timestamp in ISO 8601 format in UTC, for example 2026-01-31T00:00:00Z. The tool returns only orders created after that moment.
- limit: the number of orders to return. The default is 20 and the maximum is 100. The tool does not reject a value above 100. It silently reduces the value to 100. This confused people before.
- cursor: the next_cursor value from the previous response. Use it only to get the next page.

## Results

The tool sorts the results by creation time, newest first. Each order has these fields:

- id
- customer_id
- status
- total
- currency
- created_at

total is in minor units. A total of 1999 with currency USD means 19.99 dollars. This is a common source of mistakes.

The results do not include line items. Call get_order to get them.

## Pages

When there are more results than the limit, the response includes a field named next_cursor. To get the next page, make the same call again with cursor set to that value. Keep all other parameters the same. If you change the other parameters between pages, the results may be inconsistent. When next_cursor is absent, there are no more pages.

## Orders older than 90 days

search_orders does not return orders older than 90 days. The system moves them to the archive. This is true even if created_after is an earlier date. The result is then empty for that period, and the tool gives no error. Use the search_archive tool for those orders.

## Freshness

The system updates the search index asynchronously. A new order or a status change may take up to 5 minutes to appear in the results. If the tool does not find an order that was just created, the index possibly does not contain it yet. An empty result does not necessarily mean that the order does not exist. In that situation, call get_order with the order id. get_order reads from the primary database.

## Rate limit

The tool permits 60 calls per minute per agent. Above the limit, the call fails with HTTP 429. The response includes a retry_after value in seconds. Wait that number of seconds before you call again. Do not retry immediately.

Cut candidates: the reason for ORD-400 ("would scan the whole table"), "This confused people before", "This is a common source of mistakes".
