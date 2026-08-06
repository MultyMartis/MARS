# PRE-AI SOAK RUNBOOK v1

## Start

- Attempt 1: 06.08.2026 14:20 МСК — **INTERRUPTED BY OBSERVABILITY REPAIR**
- Attempt 2: 06.08.2026 19:15 МСК — **INTERRUPTED BY LAST-PROCESSED STATUS READBACK REPAIR**
- **Final T+0:** 2026-08-06 16:20 Europe/Moscow
- **Earliest PASS time:** 2026-08-08 16:20 Europe/Moscow

## Rules

- No feature work · AI stays OFF · no OpenRouter · no customer auto-send
- No reminder schedule changes · no role changes except emergency revoke
- No Phase 3I.1

## Commands

/status /health /stats /pending_count /delivery_status /delivery_users /last_error /reminder_status /reply_profiles /config /leads

## Phase 3H.4.1 checks (T+0)

- ADMIN_A `/status` — last production processed **05.08.2026 17:22 МСК** (not `нет данных`, not 22:23)
- `/stats` processed=1 · `/pending_count`=0 · `/leads` agrees
- `/reminder_status` visible · `/health` OK

## Evidence to return

Checkpoint notes under `evidence/pre-ai-soak/` and `evidence/phase3h4-1/FINAL-SOAK-CHECKPOINT-T0-v1.md` only after real elapsed times.
