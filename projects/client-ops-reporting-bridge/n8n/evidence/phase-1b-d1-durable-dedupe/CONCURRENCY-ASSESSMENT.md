# Concurrency Assessment — D1

**Classification:** DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN

- No unique DB constraint on event_id
- Claim path is check-then-insert (race possible under parallel webhooks)
- Sequential single-producer proven by D1 tests
- Concurrent producers FORBIDDEN until atomicity proven
- Scheduler FORBIDDEN
- Parallel retries FORBIDDEN
