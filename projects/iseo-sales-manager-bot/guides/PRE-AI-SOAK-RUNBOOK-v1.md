
## Phase 3H.7.3.1 (2026-08-10)
- Verdict baseline: acceptance-card canonicalization + authoritative instance v1.1
- Root cause: callback status sync used reduced `buildFinalCard`; fixed to full canonical body
- Contract: `iseo-authoritative-card-instance-v1.1`
- Soak: new final 48h restarted (does not reuse 3H.7.3 T+0); Phase 3I.1 blocked; AI OFF
- Evidence: `evidence/phase3h731/`
<!-- Phase 3H.7.3 operator resurface production-parity repair 2026-08-10 -->
## Phase 3H.7.3 (current)

| Field | Value |
|-------|-------|
| **Phase** | 3H.7.3 — Operator resurface production-parity, contact error fix, multi-card sync hardening |
| **Verdict** | `COMPLETE — RESURFACE PARITY REPAIRED; OPERATOR ACCEPTANCE PENDING` |
| **Repairs** | Canonical renderer for resurface · formula-error contact filter · authoritative card registry · semantic ack ≠ sync warning |
| **Acceptance leads** | REAL_REOPEN_A/B/C pending · 12 parity cards · no new LEADS rows |
| **Runtime** | Ops **45** active · Admin **87** active · v2 inactive · AI **OFF** · reminders recipients=4 |
| **Soak** | 3H.7.2 interrupted · Fresh T+0 **2026-08-10 12:44 Europe/Moscow** · earliest T+48 **2026-08-12 12:44 Europe/Moscow** |
| **Evidence** | [evidence/phase3h73/](evidence/phase3h73/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3h73-resurface-production-parity-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h73-resurface-production-parity-v1.md) |
| **Gate** | Phase 3I.1 blocked until soak PASS + operator acceptance |

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

## Phase 3H.6 four-recipient soak

Attempt 3 invalidated (operator-approved baseline change 3→4). New T+0 **2026-08-06 20:28 Europe/Moscow**. Pass criteria require stable four-recipient fanout and reminder selection. STOP criteria unchanged except four-recipient expectation replaces three.


### Phase 3H.7

See evidence/phase3h7 and architecture/LEAD-REOPEN-CONTRACT-v1.md. Soak interrupted pending Gmail reauth + missed-lead recovery. Reopen: processed|spam -> pending via sm:r:.



## Phase 3H.7.1 note
Gmail OAuth recovery closed; original terminal cards now expose `↩️ Вернуть в обработку`; MISSED_PROD_LEAD_1 resolved without replay (no absent genuine form lead); soak restarted; Phase 3I.1 blocked.

## Phase 3H.7.2 note
Callback acknowledgement contract `iseo-lead-callback-ack-v1.0` deployed. Reopen ack is «Лид возвращён в обработку.». Aggregate no longer maps pending applied→processed. Operator-approved resurface of three genuine leads completed for acceptance; global reopen still does not fan out. Soak restarted; Phase 3I.1 blocked. See `evidence/phase3h72/`.

