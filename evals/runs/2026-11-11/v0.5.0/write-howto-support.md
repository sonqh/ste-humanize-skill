# Answer a ticket about webhooks that stopped

The customer can enable the endpoint again in Settings > Webhooks and replay the missed events from the last 7 days. Events older than 7 days are gone, and we cannot recover them.

Before you start, you need two things:

- The delivery log of the customer's endpoint.
- The date when the deliveries stopped.

## How an endpoint stops

- We try each delivery 5 times over 2 hours. The wait between tries becomes longer each time.
- If all 5 tries fail, we mark the endpoint as `failing`.
- After 3 days as `failing`, we disable the endpoint automatically. We also send an email to the account owner.

## Steps

1. Find the state of the endpoint: `failing` or disabled.
2. If the endpoint is disabled, tell the customer that the account owner received an email about it.
3. Look in the delivery log for HTTP 401 with the error code `WH-401`. This entry means that the signature check failed on the customer's side.
4. If you find `WH-401`, tell the customer to correct the signature check on their endpoint.
5. Tell the customer to enable the endpoint again in Settings > Webhooks.
6. Tell the customer to click the Replay button. It sends the missed events from the last 7 days again.
7. Compare the date when the deliveries stopped with the 7-day limit. If some events are older than 7 days, tell the customer that those events are gone.
