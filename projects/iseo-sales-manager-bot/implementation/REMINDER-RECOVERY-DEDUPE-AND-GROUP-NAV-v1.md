# REMINDER RECOVERY DEDUPE + GROUP NAV v1

## Live defect

2026-08-21 primary `36699` delivered ADMIN_A digest (msg 1060); recovery `36708` re-sent same window (msg 1061).

## Repair

- Post-deliver → Mark Window Complete (stamp `last_window`)
- Collapse ACCESS before ledger read
- Skip only delivered/sent recipients
- Digest filter buttons + `sm:g:` group navigation

## Evidence

`evidence/current-stabilization/reminder-recovery-navigation/`

## Harness

`implementation/harness/reminder-recovery-idempotency-v1.mjs`
