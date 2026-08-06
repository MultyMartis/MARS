# CONTAINMENT-POLICY

**Tokens:** `D6E_CONTAINMENT_FAILURE_BLOCKS_RETRY` · `D6E_CONTAINMENT_AND_DELIVERY_OUTCOMES_SEPARATED`

| Containment | Delivery | Decision |
|-------------|----------|----------|
| `CONTAINMENT_FAILED` | any | `FINAL_FAILURE` (blocks retry) |
| `RECONTAINED_WITH_ANOMALY` | SENT | `UNSAFE_TO_RETRY` |
| `RECONTAINED_WITH_ANOMALY` | PENDING | `RECONCILE_BEFORE_RETRY` |

Containment outcome is separate from Telegram/ledger delivery outcome. Delivery success does not waive containment failure.
