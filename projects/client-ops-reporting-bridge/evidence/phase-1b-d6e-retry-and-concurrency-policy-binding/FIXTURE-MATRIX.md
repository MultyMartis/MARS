# FIXTURE-MATRIX (E1–E40)

Harness `n8n/harness/d6e-retry-concurrency-policy-harness.mjs` → **40/40 PASS**.

| Id | Scenario | Expected decision | Notes |
|----|----------|-------------------|-------|
| E1 | Pre-tx semantic failure | `FINAL_FAILURE` | PRE_TRANSMISSION_SEMANTIC* |
| E2 | Pre-tx transient no side effect | `SAFE_TO_RETRY` | charter still required / rejected if absent |
| E3 | Ambiguous transport | `RECONCILE_BEFORE_RETRY` | AMBIGUOUS* |
| E4 | Ambiguous transport (alt) | `RECONCILE_BEFORE_RETRY` | ambiguity default |
| E5 | HTTP 202 + SENT | `UNSAFE_TO_RETRY` | terminal success |
| E6 | HTTP 202 + PENDING | `RECONCILE_BEFORE_RETRY` | HTTP_202_PENDING* |
| E7 | HTTP 202 + FAILED | `FINAL_FAILURE` | FAILED |
| E8 | HTTP 200 + SENT | `UNSAFE_TO_RETRY` | SENT |
| E9 | HTTP 200 + PENDING | `RECONCILE_BEFORE_RETRY` | DUPLICATE_PENDING |
| E10 | HTTP 200 + FAILED | `FINAL_FAILURE` | FAILED |
| E11 | HTTP 409 | `FINAL_FAILURE` | CONFLICT |
| E12 | HTTP 401/403 | `FINAL_FAILURE` | AUTH |
| E13 | HTTP 404 inactive | `FINAL_FAILURE` | WORKFLOW_INACTIVE |
| E14 | HTTP 400/422 | `FINAL_FAILURE` | VALIDATION |
| E15 | HTTP 500 | `RECONCILE_BEFORE_RETRY` | 5XX |
| E16 | No row ambiguous | `RECONCILE_BEFORE_RETRY` | NO_ROW_AMBIGUOUS |
| E17 | No row authoritative no-intake | `SAFE_TO_RETRY` | charter required |
| E18 | PENDING ledger | `RECONCILE_BEFORE_RETRY` | PENDING_NEVER_AUTO_RETRY |
| E19 | SENT ledger | `UNSAFE_TO_RETRY` | ALREADY_SENT |
| E20 | FAILED ledger | `FINAL_FAILURE` | DELIVERY_FAILED_TERMINAL |
| E21 | Telegram SUCCESS + PENDING | `UNSAFE_TO_RETRY` | no-send guard |
| E22 | Telegram UNKNOWN + PENDING | `RECONCILE_BEFORE_RETRY` | TELEGRAM_UNKNOWN |
| E23 | Telegram FAILED + FAILED ledger | `FINAL_FAILURE` | TELEGRAM_FAILED |
| E24 | Containment failed | `FINAL_FAILURE` | CONTAINMENT_FAILED |
| E25 | Recontain anomaly + SENT | `UNSAFE_TO_RETRY` | ANOMALY_SENT |
| E26 | Recontain anomaly + PENDING | `RECONCILE_BEFORE_RETRY` | ANOMALY_PENDING |
| E27 | Stale eligibility | `FINAL_FAILURE` | freshness blocks |
| E28 | NOT_SAFE_TO_SEND | `FINAL_FAILURE` | NOT_ELIGIBLE |
| E29 | Same-event parallel | `UNSAFE_TO_RETRY` | SAME_EVENT |
| E30 | Different-event parallel | `UNSAFE_TO_RETRY` | GLOBAL_CONCURRENCY |
| E31 | SAFE class without charter | `SAFE_TO_RETRY` | charter rejected REQUIRED |
| E32 | Charter event mismatch | `SAFE_TO_RETRY` | EVENT_MISMATCH reject |
| E33 | Charter source mismatch | `SAFE_TO_RETRY` | SOURCE_MISMATCH reject |
| E34 | Retry budget exhausted | `SAFE_TO_RETRY` | BUDGET_EXHAUSTED reject |
| E35 | New source run | `FINAL_FAILURE` | NEW_SOURCE_RUN_NOT_RETRY |
| E36 | Historical PENDING blind retry | `UNSAFE_TO_RETRY` | HISTORICAL_PENDING* |
| E37 | Response lost + SENT | `UNSAFE_TO_RETRY` | SENT |
| E38 | Response lost + FAILED | `FINAL_FAILURE` | FAILED |
| E39 | Response lost + PENDING | `RECONCILE_BEFORE_RETRY` | PENDING |
| E40 | Evidence sanitization | `UNSAFE_TO_RETRY (SENT path) + sanitize` | secrets stripped |

All cases assert `automatic_retry=false`, `max_automatic_retries=0`, `max_safe_concurrency=1`, and `retry_authorized=false` (no execution).
