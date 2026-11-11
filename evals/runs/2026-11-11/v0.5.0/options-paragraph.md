We could handle the rate limit in four ways, and each has trade-offs.

- Retry with exponential backoff. This is simple, but it can take up to 30 seconds on a bad day.
- Queue the requests in Redis. This keeps the UI fast, but it needs a new worker. We lose the queue if Redis restarts without persistence.
- Ask the vendor for a higher limit. This costs nothing to build, but it takes about two weeks and the vendor may refuse.
- Cache responses for 5 minutes. This removes most calls, but it works only for read requests, so writes would still hit the limit.
