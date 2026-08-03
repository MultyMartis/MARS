# REAL TELEGRAM ACCEPTANCE v1

**Status:** PASS — Андрей live sequence complete  
**Acceptance window:** post repair-3 (after 2026-08-03T18:28:36Z); operator confirmation recorded 2026-08-04 ~01:45–01:50 +07

## Андрей sequence (operator-attested)

| Command | Result | Notes |
|---|---|---|
| `/start` | PASS | Admin start message |
| `/help` | PASS | Canonical underscores preserved (`/last_error`, `/ai_status`, …) |
| `/config` | PASS | Admins 1 · Moderators 1 · Lead-action 2 · ACCESS_CONTROL |
| `/moderators` | PASS | Olya listed active |
| `/moderator_info 54C479` | PASS | Opaque code only (no raw Telegram ID in operator transcript) |
| `/moderator_add 54C479` (active) | PASS | Idempotent |
| `/moderator_remove 54C479` | PASS | Registry updated |
| `/moderators` (after remove) | PASS | 0 active moderators |
| `/moderator_pending` | PASS | Honest pending/none |
| `/moderator_add 54C479` (re-add) | PASS | Olya restored |
| `/moderators` (after re-add) | PASS | Olya active |
| `/health` | PASS | |
| repeated `/start` | PASS | No silence after registry write path |

## Proof summary

- Telegram updates received; Admin.dev executions created (see `REAL-ACCEPTANCE-EXEC-MATRIX.json`).
- One Telegram response per tested command; no duplicate operator reports.
- No raw Telegram IDs / tokens / webhook URLs in this evidence pack.
- ACCESS_CONTROL is effective authorization source.
- Moderator add/remove mutates live registry without workflow edits.
- Olya restored as active moderator at close of acceptance.

## Olya interactive

Operator closed Андрей matrix with Olya restored active. Separate Olya `/start`/`/help` interactive session may remain optional follow-up; registry + Admin path proven.
