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

