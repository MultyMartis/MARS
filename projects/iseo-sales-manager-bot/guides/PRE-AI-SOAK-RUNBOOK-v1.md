# PRE-AI SOAK RUNBOOK v1

## Start

- Attempt 1: 06.08.2026 14:20 МСК — **INTERRUPTED BY OBSERVABILITY REPAIR**
- Attempt 2: 06.08.2026 19:15 МСК — **INTERRUPTED BY LAST-PROCESSED STATUS READBACK REPAIR**
- **Final T+0:** 2026-08-06 16:20 Europe/Moscow
- **Earliest PASS time:** 2026-08-08 16:20 Europe/Moscow

## T+0 observation checkpoint (executed)

- Executed: **2026-08-06 19:52 Europe/Moscow** (~3h 32m elapsed)
- Verdict: `SOAK T+0 STOP — PRODUCTION INVARIANT VIOLATION`
- STOP: MOD_C_REVOKED identity reactivated after T+0 and received a lead card (4-recipient fanout)
- Next calendar mark: T+6 @ 06.08.2026 22:20 Europe/Moscow (not a PASS claim)
- Phase 3I.1: **blocked**
- Evidence: `evidence/pre-ai-soak/FINAL-SOAK-CHECKPOINT-T0-v1.md`

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

Checkpoint notes under `evidence/pre-ai-soak/` only after real elapsed times. T+0 STOP evidence recorded 06.08.2026 19:52 МСК.
