# CONCURRENCY-POLICY-PROOF

**Token:** `D6E2_AUTOMATIC_RETRIES_DISABLED_VERIFIED`

**Token:** `D6E2_CONCURRENCY_ONE_VERIFIED`

AUTOMATIC_RETRIES_ENABLED=NO
MAX_AUTOMATIC_RETRIES=0
MAX_SAFE_CONCURRENCY=1

```json
{
  "D6E_RETRY_DEFAULTS": {
    "automatic_retry_budget": 0,
    "manual_bounded_retry_budget": 1,
    "max_safe_concurrency": 1,
    "max_automatic_retries": 0,
    "automatic_retries_enabled": false
  },
  "D6E_MAX_SAFE_CONCURRENCY": 1,
  "pending_automatic_retry": false,
  "sent_automatic_retry": false,
  "pending_max_automatic_retries": 0,
  "sent_max_safe_concurrency": 1
}
```

No parallel production requests issued by D6E2.
