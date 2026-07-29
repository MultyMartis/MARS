# OFFLINE-IMPLEMENTATION

**Tokens:** `D6E_POLICY_ENGINE_DEFINED` · `D6E_RECONCILIATION_PLANNER_DEFINED` · `D6E_DETERMINISTIC_CLOCK_TESTS`

| File | Role |
|------|------|
| `n8n/runners/lib/client-ops-retry-policy.mjs` | Policy evaluator (B0–B7, four decisions) |
| `n8n/runners/lib/client-ops-retry-reason-codes.mjs` | Stable reason codes |
| `n8n/runners/lib/client-ops-reconciliation-planner.mjs` | GET-only reconcile plan |
| `n8n/runners/lib/client-ops-retry-charter.mjs` | Explicit charter validator/template |
| `n8n/runners/lib/client-ops-concurrency-policy.mjs` | Concurrency=1 gates |
| `n8n/harness/d6e-retry-concurrency-policy-harness.mjs` | E1–E40 + EC1–EC10 offline harness |
| `src/client_ops_reporting_bridge/retry_policy_binding.py` | Producer binding (no auto-retry) |
| `tests/test_retry_policy_d6e.py` | Python binding unit tests |

No network. No production mutation. Deterministic clock (no sleep).
