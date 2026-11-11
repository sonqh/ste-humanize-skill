# Stop sync retries after 5 attempts

Sync now stops after 5 failed attempts and shows "Sync paused" in the status bar. Before this change, sync retried without a limit when the server returned 503, and the retries flooded the API. One customer, Acme, saw 40,000 requests in one hour (SUP-2211).

The cause was the retry loop in `sync/retry.ts`. It had no maximum.

## What changes

- Sync makes 5 attempts at most. The wait between attempts starts at 1 second and doubles each time.
- After the last attempt fails, sync stops and the status bar shows "Sync paused".
- Sync does not retry a 401. It retried a 401 before, and that retry had no use.

## How to verify

1. Run `npm test -- retry`.
2. Set `SYNC_FAKE_503=1`. Make sure that sync stops after 5 attempts.

## Risk

Users with unstable networks will see "Sync paused" more often.

## Not in this PR

A retry budget for each account. I will add it later.
