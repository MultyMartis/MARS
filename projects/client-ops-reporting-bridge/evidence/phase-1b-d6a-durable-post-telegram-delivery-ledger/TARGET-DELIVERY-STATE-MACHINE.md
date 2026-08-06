# TARGET-DELIVERY-STATE-MACHINE

**Token:** `D6A_DELIVERY_STATE_MACHINE_DEFINED`

## States (primary)

| State | Meaning |
|-------|---------|
| PENDING | Claimed / unresolved delivery |
| SENT | Positively proven Telegram delivery |
| FAILED | Positively proven terminal Telegram delivery failure |

No extra primary states in D6A (`FAILED_RETRYABLE` deferred to workstream E).

## Transitions

| From | To | Trigger | Durable write | Idempotency | Invalid / notes |
|------|----|---------|---------------|-------------|-----------------|
| PENDING | SENT | Telegram SUCCESS authority | Update `delivery_state=SENT` where event_id + PENDING | Second finalize → NOOP | — |
| PENDING | FAILED | Telegram DEFINITE_FAILURE | Update `delivery_state=FAILED` where event_id + PENDING | Second finalize → NOOP | — |
| SENT | SENT | Replay finalize | No mutation | Idempotent observation | — |
| FAILED | FAILED | Replay finalize | No mutation | Idempotent observation | — |
| SENT | FAILED | Any automatic path | Reject | Fail-closed | Prohibited |
| FAILED | SENT | Casual / automatic | Reject | — | Requires future recovery charter |
| PENDING | PENDING | Ambiguous Telegram / interrupted / ledger write fail after success | No automatic resend | Safe unresolved | Operator reconcile |

## Invariants

- `intake_state` unchanged by finalize
- `event_status` unchanged by finalize
- Duplicate intake never attempts Telegram (any delivery_state)
- HTTP 202 = intake accepted, not delivery completed
