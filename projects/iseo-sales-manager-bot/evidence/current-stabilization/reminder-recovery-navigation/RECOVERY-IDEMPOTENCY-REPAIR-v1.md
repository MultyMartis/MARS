# RECOVERY IDEMPOTENCY REPAIR

## Changes (Admin.dev, 104 nodes)

1. **Collapse ACCESS For Reminder Ledger** — single item before ledger read.
2. **Reminder Post Deliver Window** — after Telegram `delivered`, when all intended recipients delivered → `Reminder Mark Window Complete` → stamp `last_window`.
3. **Build Claims** — skip only `delivered`/`sent` (`ALREADY_DELIVERED`); nonempty ledger row filter; digest v1.1 group buttons.
4. Group navigation namespace `sm:g:` + handlers.

## Invariant

`UNIQUE(business_window, recipient_ref)` successful digest ≤ 1.

Harness: `implementation/harness/reminder-recovery-idempotency-v1.mjs` → **PASS**, duplicate_sends_after_repair = **0**.
