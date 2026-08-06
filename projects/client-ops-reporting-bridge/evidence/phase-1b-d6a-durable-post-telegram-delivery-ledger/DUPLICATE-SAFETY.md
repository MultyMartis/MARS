# DUPLICATE-SAFETY

**Token:** `D6A_DUPLICATE_SUPPRESSION_PRESERVED`

## Rule

Intake classification remains authoritative for Telegram side effect:

- `FIRST_SEEN` → may Telegram (once) then finalize
- `DUPLICATE` / `EVENT_ID_CONFLICT` → **never** Telegram, regardless of `delivery_state`

## Matrix

| Existing delivery_state | Duplicate intake | Telegram | State change |
|-------------------------|------------------|----------|--------------|
| PENDING | suppressed | 0 | remains PENDING (reconcile later) |
| SENT | suppressed | 0 | remains SENT |
| FAILED | suppressed | 0 | remains FAILED (no auto retry in D6A) |

Terminal-state logic must not re-open Telegram from finalizer or duplicate path.
