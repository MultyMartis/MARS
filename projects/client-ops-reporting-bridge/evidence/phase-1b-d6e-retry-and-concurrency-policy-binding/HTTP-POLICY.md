# HTTP-POLICY

**Tokens:** `D6E_HTTP202_POLICY_DEFINED` · `D6E_HTTP200_DUPLICATE_POLICY_DEFINED` · `D6E_HTTP409_POLICY_DEFINED` · `D6E_HTTP4XX_POLICY_DEFINED` · `D6E_HTTP5XX_POLICY_DEFINED` · `D6E_AMBIGUOUS_TRANSPORT_REQUIRES_RECONCILIATION` · `D6E_NO_ROW_RECONCILIATION_POLICY_DEFINED`

| Observation | Decision tendency |
|-------------|-------------------|
| Ambiguous transport / response lost + unknown claim | `RECONCILE_BEFORE_RETRY` |
| 202 + SENT | `UNSAFE_TO_RETRY` (terminal success) |
| 202 + PENDING | `RECONCILE_BEFORE_RETRY` |
| 202 + FAILED | `FINAL_FAILURE` |
| 200 duplicate + SENT | `UNSAFE_TO_RETRY` |
| 200 duplicate + PENDING | `RECONCILE_BEFORE_RETRY` |
| 200 duplicate + FAILED | `FINAL_FAILURE` |
| 409 conflict | `FINAL_FAILURE` |
| 401/403 auth | `FINAL_FAILURE` |
| 400/422 validation | `FINAL_FAILURE` |
| 404 / inactive before POST | `FINAL_FAILURE` |
| 5xx claim unknown | `RECONCILE_BEFORE_RETRY` |
| No row + non-authoritative | `RECONCILE_BEFORE_RETRY` |
| No row + authoritative no-intake | `SAFE_TO_RETRY` class (charter required; no auto-exec) |
