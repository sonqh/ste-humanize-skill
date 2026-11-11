We have four options to handle the rate limit. Each one has trade-offs.

- Retry with exponential backoff. This is simple, but it can take up to 30 seconds on a bad day.
- Queue the requests in Redis. The UI stays fast, but this option needs a new worker. If Redis restarts without persistence, we lose the queue.
- Ask the vendor for a higher limit. This costs nothing to build, but it takes about two weeks and the vendor may refuse.
- Cache responses for 5 minutes. This removes most calls, but it only works for read requests. Writes would still hit the limit.
