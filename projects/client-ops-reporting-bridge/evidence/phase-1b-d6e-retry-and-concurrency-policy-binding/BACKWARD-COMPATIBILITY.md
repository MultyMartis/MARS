# BACKWARD-COMPATIBILITY

**Token:** `D6E_BACKWARD_COMPATIBILITY_MODEL_DEFINED`

- Workstream A ledger states PENDING/SENT/FAILED unchanged.
- Workstream B `source_status` / `delivery_eligibility` / threshold semantics unchanged.
- Workstream C activation lifecycle / lock / budgets unchanged.
- Producer historical `retry_decision` strings map into D6E vocabulary without enabling auto-retry.
- Legacy `RETRY_FUTURE_ELIGIBLE` maps to `RECONCILE_BEFORE_RETRY` (not auto-safe).
