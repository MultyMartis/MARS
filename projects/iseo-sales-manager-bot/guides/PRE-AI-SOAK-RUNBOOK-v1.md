# PRE-AI SOAK RUNBOOK v1

## Start

- Attempt 1: 06.08.2026 14:20 МСК — **INVALIDATED** (Phase 3H.4 observability repair)
- **Restart T+0:** 2026-08-06 19:15 Europe/Moscow
- **Earliest PASS time:** 2026-08-08 19:15 Europe/Moscow

## Rules

- No feature work · AI stays OFF · no OpenRouter · no customer auto-send
- No reminder schedule changes · no role changes except emergency revoke
- No Phase 3I.1

## Commands

/status /health /stats /pending_count /delivery_status /delivery_users /last_error /reminder_status /reply_profiles /config

## Phase 3H.4 observability checks (T+0)

- ADMIN_A `/reminder_status` — visible reply (not silent)
- ADMIN_A `/status` — poll time advances; last production lead **05.08.2026 17:22 МСК** (`lead_19fd2052066e18b7`)
- `/health` Gmail OK does not substitute for poll heartbeat in `/status`

## Evidence to return

Checkpoint notes under `evidence/pre-ai-soak/` and `evidence/phase3h4/SOAK-CHECKPOINT-T0-v2.md` only after real elapsed times.
