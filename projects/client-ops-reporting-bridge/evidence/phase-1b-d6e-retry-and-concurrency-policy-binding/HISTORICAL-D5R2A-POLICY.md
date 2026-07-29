# HISTORICAL-D5R2A-POLICY

**Token:** `D6E_HISTORICAL_PENDING_POLICY_CLASSIFIED`

Historical event `c84e29bf-79b1-5aea-98c4-9dc8d651fc96`:

- `intake_state=FIRST_SEEN`
- `event_status=ATTENTION`
- `delivery_state=PENDING`

Policy: blind retry **prohibited** when historical Telegram success evidence exists (`HISTORICAL_PENDING_BLIND_RETRY_PROHIBITED` → `UNSAFE_TO_RETRY` + no-send guard).

`HISTORICAL_D5R2A_ROW_RECONCILIATION_AUTHORIZED=NO` — D6E does not mutate or reconcile this row in production.
