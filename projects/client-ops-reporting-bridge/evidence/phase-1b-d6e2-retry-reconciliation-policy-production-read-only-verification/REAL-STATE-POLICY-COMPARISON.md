# REAL-STATE-POLICY-COMPARISON

**Token:** `D6E2_REAL_STATE_POLICY_COMPARISON_COMPLETE`

## Historical PENDING + Telegram success

- event_id: c84e29bf-79b1-5aea-98c4-9dc8d651fc96
- delivery_state: PENDING (not durably finalized)
- decision: UNSAFE_TO_RETRY
- reason_code: HISTORICAL_PENDING_BLIND_RETRY_PROHIBITED
- retry_authorized: false
- no_send_guard: true
- requires_reconciliation: true
- action: reconciliation / operator review only; row untouched; no resend

## SENT (D6A2 synthetic)

- event_id: d6a2a001-27d6-4a2e-bd6a-000000000001
- delivery_state: SENT (terminal successful)
- decision: UNSAFE_TO_RETRY
- reason_code: HTTP_202_SENT_TERMINAL
- retry_authorized: false
- terminal_success: true
- requires_reconciliation: false
- action: no resend; no reconciliation required for delivery authorization; row untouched
