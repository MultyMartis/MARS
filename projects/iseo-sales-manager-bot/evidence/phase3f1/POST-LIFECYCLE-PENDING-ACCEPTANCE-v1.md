# POST-LIFECYCLE PENDING ACCEPTANCE v1

**Question:** does adding the pending view + reminder engine change existing lifecycle behavior (buttons, callbacks, attribution, archive)?

## Answer: no

Phase 3F.1 is a read-only view layer plus a new scheduled notification path. It does not touch `Update CLEAN Lifecycle`, `Handle Callback Action`, the button/callback contract (`sm:p:<token12>` / `sm:s:<token12>`), or actor attribution.

## Proven behavior

| Check | Result |
|---|---|
| A lead marked `processed` via the existing callback immediately disappears from the pending view (harness #43) | PASS |
| A lead marked `spam` via the existing callback immediately disappears from the pending view (harness #44) | PASS |
| Repeated callback on an already-settled lead remains idempotent (contract, #45) | PASS |
| Actor attribution on final cards is unchanged (contract, #46) | PASS |
| Original inline action buttons (`✅ Обработано` / `🚫 Спам`) are unchanged (contract, #47) | PASS |
| Archive (`/leads`) cards remain non-actionable / buttonless (contract, #48) | PASS |
| `/my_status`, `/moderator_pending`, `/moderators`, `/leads`, callback-processed, callback-spam regression stubs | PASS (#49–54) |

## Why this matters operationally

Because the pending view recomputes from live CLEAN data on every command/reminder invocation (no separate cached "pending list" that could drift), a manager clicking **✅ Обработано** on a card immediately removes that lead from both `/pending_count` and the next reminder — there is no separate state to keep in sync.

*Related: [PENDING-VIEW-CONTRACT-v1.md](PENDING-VIEW-CONTRACT-v1.md), `architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md`.*
