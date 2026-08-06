# REMINDER COUNT THREE ROOT CAUSE — Phase 3H.6

## Root cause

**Stale CONFIG cache** `pending_reminder_active_recipients_count=3` left from Phase 3H.4 three-recipient backfill, not refreshed after operator restored MOD_C.

## Not

- Not a hardcoded builder fallback-only defect (fallback unused when key present)
- Not display-only in the sense of inventing a number without a source — source existed but was stale
- Not ACCESS selector failure (send path already dynamic)

## Repair

1. CONFIG cache updated 3 → **4**  
2. `Reminder Commands` patched (Phase 3H.6) to prefer live `$('Read ACCESS_CONTROL')` count using the same staff predicate as Reminder Build Claims, with CONFIG as fallback only
