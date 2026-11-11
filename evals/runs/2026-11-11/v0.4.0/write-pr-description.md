# Stop sync retries after 5 attempts

Sync now stops after 5 attempts. Before this change, it retried without a limit when the server returned 503. One customer saw 40,000 requests in an hour (SUP-2211). The retry loop in `sync/retry.ts` had no maximum.

## What changes

- Sync makes 5 attempts at most. The wait between attempts starts at 1 second and doubles each time.
- After the last attempt, sync stops and the status bar shows "Sync paused".
- Sync does not retry a 401. It retried a 401 before, and that retry could not succeed.

## How to verify

Run the retry tests:

```
npm test -- retry
```

Then do a manual test. Set `SYNC_FAKE_503=1`. Make sure that sync stops after 5 attempts.

## Risk

Users with unstable networks will see "Sync paused" more often.

## Not in this PR

A retry budget for each account. I will do that in a later PR.
