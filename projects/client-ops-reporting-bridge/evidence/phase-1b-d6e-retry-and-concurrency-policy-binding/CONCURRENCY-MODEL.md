# CONCURRENCY-MODEL

**Tokens:** `D6E_CONCURRENCY_MODEL_DEFINED` · `D6E_SAME_EVENT_CONCURRENCY_FORBIDDEN` · `D6E_DIFFERENT_EVENT_CONCURRENCY_REMAINS_ONE` · `D6E_CONCURRENCY_REMAINS_ONE`

| Field | Value |
|-------|-------|
| `max_safe_concurrency` | 1 |
| `max_automatic_retries` | 0 |
| same-event concurrency | FORBIDDEN |
| different-event concurrency | FORBIDDEN_UNTIL_ATOMICITY_PROVEN |
| D1 historical | `DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN` |
| overturned_by_abc | false |
| verdict | `D6E_CONCURRENCY_REMAINS_ONE` |

Layers: source_producer_invocation · lifecycle_orchestration · workflow_activation · webhook_request · data_table_first_seen_claim · telegram_delivery · delivery_finalization.
