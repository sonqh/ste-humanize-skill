# Answer a ticket about webhooks that stopped

The customer can re-enable a disabled endpoint in Settings > Webhooks and replay the missed events from the last 7 days. Events older than 7 days are gone, so answer these tickets quickly.

You need the delivery log of the customer's endpoint.

## What the system does when a delivery fails

- The system retries a failed delivery 5 times in 2 hours. The wait between retries increases.
- If all 5 retries fail, the system marks the endpoint as `failing`.
- If the endpoint stays `failing` for 3 days, the system disables it and sends an email to the account owner.

## Steps

1. Open the delivery log of the endpoint.
2. Find the failed deliveries. If they show HTTP 401 with error code `WH-401`, the signature check failed on the customer's side.
3. For `WH-401`, tell the customer to correct the signature check on their side.
4. Find the state of the endpoint: `failing` or disabled.
5. If the endpoint is `failing`, tell the customer that the system disables it after 3 days in this state.
6. If the endpoint is disabled, tell the customer that the account owner received an email about it.
7. Tell the customer to re-enable the disabled endpoint in Settings > Webhooks.
8. Tell the customer to use the Replay button to replay the missed events. Replay includes events from the last 7 days only.
9. If the webhooks stopped more than 7 days ago, tell the customer that the older events are gone. Replay cannot recover them.
