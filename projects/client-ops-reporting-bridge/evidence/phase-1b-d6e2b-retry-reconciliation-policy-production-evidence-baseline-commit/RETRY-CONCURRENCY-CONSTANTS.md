# RETRY-CONCURRENCY-CONSTANTS

AUTOMATIC_RETRIES_ENABLED=NO
MAX_AUTOMATIC_RETRIES=0
MAX_SAFE_CONCURRENCY=1

Historical limitation remains load-bearing: `DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN`
Same-event parallel retry: forbidden
Different-event concurrent lifecycle on same workflow: forbidden
No concurrency increase was proven.
