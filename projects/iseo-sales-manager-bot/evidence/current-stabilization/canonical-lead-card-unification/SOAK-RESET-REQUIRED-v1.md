# SOAK-RESET-REQUIRED-v1

## Status

**SOAK RESET REQUIRED** — do **not** start a new soak window on top of this maintenance.

## Rationale

- Admin.dev graph patched (Handle Callback Action, Recent Leads)
- Partial acceptance (`all_pass: false`) — status_callbacks and reminder_group not closed in harness
- MOD_B isolation cycle completed and restored
- Operator halted further live test traffic

## Before next soak

1. Confirm MOD_B active (forensic: done @ 11:38:55Z)
2. Optional: re-run acceptance sections status_callbacks + reminder_group in dedicated window
3. Reset soak baseline counters / ledger expectations per project soak charter
4. Do not treat this task as full charter PASS for soak continuity
