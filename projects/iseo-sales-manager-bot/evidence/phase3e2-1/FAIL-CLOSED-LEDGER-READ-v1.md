# FAIL-CLOSED LEDGER READ v1

## Required behavior (live Expand Delivery Recipients)

| Read outcome | Action |
|--------------|--------|
| Successful read + no row | Eligible to claim |
| Successful read + delivered | Skip send |
| Successful read + claimed / uncertain | **Reconcile** — do not blind-send |
| Successful read + failed_retryable | Retry only affected recipient under bound |
| Quota / error / unknown | **Fail closed** — send zero cards; safe error; retry ledger later |

## Explicit states

- `ledger_read_ok`
- `ledger_read_error`
- `reconciliation_required`

## Guard

Sheets error objects must **not** enter recipient expansion as empty ledger rows.

## Live confirmation (post-patch)

When claim upsert returned Sheets quota during Phase 3E.2.1 human fixtures:

- `sendOk = 0`
- no new Telegram storm from those claim failures

Harness: D01, D02 PASS.
