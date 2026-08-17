> **Phase 3H.9.2 (2026-08-17):** ACCESS live drifted to 3 after an incomplete 2026-08-16 `/moderator_remove`/`/moderator_add` cycle left MOD_A revoked. Classified `UNAUTHORIZED_STATE_DRIFT`. Restored MOD_A via existing `/moderator_add` (same profile_no 3). Live ACCESS=4 · CONFIG=4 · Operational resolver=4 · reminder resolver=4. Next natural 10:00: **2026-08-18 Europe/Moscow**. Soak not restarted. Phase 3I.1 blocked. AI OFF. No four-recipient test sends.

> **Phase 3H.9 (2026-08-17):** False «Недостаточно прав» on raw lead was ACCESS/CONFIG Google Sheets `invalid_grant` mislabeled as a permission deny. Reminder 10:00 windows 15–17 Aug failed at CONFIG read with the same credential error before evaluation; 429 retry path was not applicable. Admin deny text + Sheets error classifier patched. Live Sheets OAuth reconnect by operator is still required before ADMIN_A raw retest and the next natural 4-recipient 10:00. Soak not restarted. Phase 3I.1 blocked. AI OFF.

> **Phase 3H.8.2.2 (2026-08-14):** Reminder pending eligibility uses `iseo-reminder-current-state-selector-v1.0` — unique `lead_id` → authoritative current status → eligibility. First CLEAN pending row no longer wins. Production Reminder Build Claims adds no per-lead Sheets calls. Duplicate CLEAN row source forensic is deferred. Real 10:00 acceptance still pending.

<!-- Phase 3H.9.2 addendum 2026-08-17 -->
## Phase 3H.9.2 addendum

Live ACCESS is again the approved four-recipient set (ADMIN_A, MOD_A, MOD_B, MOD_C). Do not treat the 2026-08-16 incomplete restore as a three-recipient baseline. Next natural reminder window: **2026-08-18 10:00 Europe/Moscow**. Soak not restarted.

<!-- Phase 3H.8.2 addendum 2026-08-14 -->
## Phase 3H.8.2 addendum

- Contract: `iseo-sheets-429-retry-v1.0` on reminder-critical Sheets reads (Admin.dev only).
- ACCESS_CONTROL 429: explicit Wait 5s/15s/30s loop (max 4 attempts); fail closed `ERROR_SHEETS_429_ACCESS`; no stale ACCESS send fallback.
- `/reminder_status` exposes ERROR + stage + quota reason + retry count.
- Soak remains: **INTERRUPTED — REAL REMINDER WINDOW FAILED ON SHEETS 429** (not restarted).
- Next live acceptance: **2026-08-15 10:00 Europe/Moscow** with `REMINDER_ACCEPTANCE_LEAD_2` left pending.
- Do not claim REMINDER LIVE PASS until that scheduled window succeeds.
- Phase 3I.1 blocked; AI OFF; Admin **92** nodes; Ops **45**; v2 inactive.
- Evidence: [evidence/phase3h82/](evidence/phase3h82/) · Report: [reports/REPORT-iseo-sales-manager-bot-phase3h82-reminder-sheets429-resilience-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h82-reminder-sheets429-resilience-v1.md)

<!-- Phase 3H.8 addendum 2026-08-13 -->
## Phase 3H.8 addendum

- Reminder/pending CLEAN source of truth: `lead_clean_v2` (not obsolete `LEADS`).
- Observability contract: `iseo-reminder-observability-v1.1`.
- Soak: **INTERRUPTED — REAL PENDING LEAD MISSED DAILY REMINDER WINDOW**.
- Next live acceptance window: **2026-08-14 10:00 Europe/Moscow** with `REMINDER_PROD_LEAD_A` left pending.
- Phase 3I.1 blocked; AI OFF; do not artificially invoke production reminder.

---

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

# PRODUCTION BASELINE — PRE-AI SOAK FOUR RECIPIENT v1

| Field | Value |
|---|---|
| Timestamp | 2026-08-06 20:28 Europe/Moscow |
| Operational.dev | xSnXPy8cEHoZw6xG · active · 45 |
| Admin.dev | wLrLp4WQHm1VJmxz · active · 85 |
| Sales-Manager-v2 | inactive |
| Parser | sm-parser-v3.3 |
| Heartbeat | iseo-gmail-poll-heartbeat-v1.0 |
| Templates | approved deterministic INTLSEO |
| Personalization | iseo-recipient-name-v1.1 |
| Resolver | iseo-reply-profile-resolver-v1.0 |
| Profiles | 1 Андрей · 2 Оля · 3 Михаил · 4 Никита |
| Card recipients | 4 |
| Reminder recipients | 4 |
| Reminder | ON · 10:00 · Europe/Moscow |
| Reporting | manual |
| AI | OFF |
| Customer auto-send | OFF |
| Production LEADS (clean) | 1 processed · pending 0 |
| Backup | private Storage git-sync phase3h6 post-change |
| Canonical tip at charter | origin/mars/canonical-post-recovery @ aee4d4b5+phase3h6 commits |


## Phase 3H.7 interruption

Status: `INTERRUPTED — MISSED PRODUCTION LEAD INVESTIGATION AND REOPEN WORKFLOW CHANGE`.
New T+0 not started until Gmail reauth + missed-lead recovery gate.


## Phase 3H.7.1 note
Gmail OAuth recovery closed; original terminal cards now expose `↩️ Вернуть в обработку`; MISSED_PROD_LEAD_1 resolved without replay (no absent genuine form lead); soak restarted; Phase 3I.1 blocked.

## Phase 3H.7.2 note
Callback acknowledgement contract `iseo-lead-callback-ack-v1.0` deployed. Reopen ack is «Лид возвращён в обработку.». Aggregate no longer maps pending applied→processed. Operator-approved resurface of three genuine leads completed for acceptance; global reopen still does not fan out. Soak restarted; Phase 3I.1 blocked. See `evidence/phase3h72/`.

