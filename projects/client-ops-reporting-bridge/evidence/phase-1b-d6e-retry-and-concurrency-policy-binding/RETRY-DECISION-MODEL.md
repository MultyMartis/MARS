# RETRY-DECISION-MODEL

**Token:** `D6E_RETRY_DECISION_MODEL_DEFINED`

Four mutually exclusive top-level states:

| Decision | Meaning |
|----------|---------|
| `SAFE_TO_RETRY` | Positive evidence that no server-side intake/claim/customer-delivery side effect occurred; same `event_id` replay may be safe **only** under a new explicit charter. D6E never auto-executes. |
| `UNSAFE_TO_RETRY` | Positive evidence that replay could cause unsafe/duplicate/contradictory side effect or violates an invariant. |
| `RECONCILE_BEFORE_RETRY` | Outcome ambiguous; durable state must be queried before any replay decision. Default for ambiguity. |
| `FINAL_FAILURE` | Terminal for current charter/event unless a separate recovery/reconciliation charter is created. |

Always: `automatic_retry=false`, `max_automatic_retries=0`, `max_safe_concurrency=1`.
