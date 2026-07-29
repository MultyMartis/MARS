# NO-ROW-POLICY-PROOF

**Token:** `D6E2_NO_ROW_POLICY_FAILS_CLOSED`

Offline fixture: ambiguous transport + no row (no production event created).

```json
{
  "decision": "RECONCILE_BEFORE_RETRY",
  "reason_code": "NO_ROW_AMBIGUOUS",
  "retry_authorized": false,
  "automatic_retry": false,
  "requires_reconciliation": true,
  "requires_new_charter": false,
  "freshness_recheck_required": true,
  "controlled_lifecycle_required": true,
  "operator_action_required": true,
  "no_send_guard": false,
  "max_automatic_retries": 0,
  "max_safe_concurrency": 1,
  "event_id": "d6e2-offline-no-row-fixture-0001",
  "event_identity_preserved": true,
  "automatic_retries_enabled": false,
  "reconciliation_plan": {
    "decision": "RECONCILE_BEFORE_RETRY",
    "reason_code": "NO_ROW_AMBIGUOUS",
    "actions": [
      "READ_DATA_TABLE_EVENT",
      "READ_N8N_EXECUTIONS",
      "VERIFY_WORKFLOW_CONTAINMENT",
      "RECOMPUTE_FRESHNESS",
      "OPERATOR_REVIEW_REQUIRED"
    ],
    "executable": false,
    "production_mutation_authorized": false,
    "live_reconciliation_executed": false
  },
  "workstream_a_unchanged": true,
  "workstream_b_unchanged": true,
  "workstream_c_unchanged": true,
  "unattended_mode_enabled": false
}
```

decision=RECONCILE_BEFORE_RETRY
reason_code=NO_ROW_AMBIGUOUS
retry_authorized=false

SAFE_TO_RETRY requires authoritative no-intake proof under a future explicit charter — not mere absence of a row.
No live retry executed.
