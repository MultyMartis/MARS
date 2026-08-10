
## Phase 3H.7.3.2 (2026-08-10)
- Verdict: `PHASE 3H.7.3.2 TECHNICAL REPAIR COMPLETE — OPERATOR LIVE CARD-EDIT ACCEPTANCE REQUIRED`
- Root cause: Expand scoring double-counted `operator_resurface_parity` via `includes('operator_resurface')`, selecting stale MSG over operator-visible acceptance_canonical card
- Contract: `iseo-authoritative-card-instance-v1.2` (exclusive scoring + callback initiator preference + archive exclusion)
- Soak: NOT restarted; prior soak timing invalidated; Phase 3I.1 blocked; AI OFF
- Evidence: `evidence/phase3h732/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3h732-live-telegram-card-edit-v1.md`

## Phase 3H.7.3.1 (2026-08-10)
- Verdict baseline: acceptance-card canonicalization + authoritative instance v1.1
- Root cause: callback status sync used reduced `buildFinalCard`; fixed to full canonical body
- Contract: `iseo-authoritative-card-instance-v1.1`
- Soak: interrupted by 3H.7.3.2 card-edit targeting defect
- Evidence: `evidence/phase3h731/`
<!-- Phase 3H.7.3 operator resurface production-parity repair 2026-08-10 -->
## Phase 3H.7.3 (superseded soak by 3H.7.3.2)

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

# CURRENT PRODUCTION BASELINE v1

**Срез:** Phase 3H.7 missed-lead forensic + reopen · 2026-08-10 11:29 Europe/Moscow
**Статус:** AI OFF; reminders ON 10:00 Europe/Moscow; reporting manual; poll heartbeat v1.0; **active recipients=4** (Андрей, Оля, Михаил, Никита). Workflows Ops 45 / Admin 85 / v2 inactive.

| Контур | Workflow ID | Active | Nodes | Роль |
|---|---|---:|---:|---|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 | rollback; не активировать |
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | Parser 3.3; multi-recipient; AI OFF; sole Gmail fetch |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 85 | profiles; callbacks; reminders ON; live ACCESS reminder count |

## CONFIG (post-3H.6)

`ai_enabled=false` · `parser_version=sm-parser-v3.3` · `pending_reminders_enabled=true` · `pending_reminder_time=10:00` · `pending_reminder_timezone=Europe/Moscow` · `pending_reminder_min_count=1` · tests/archive excluded · `pending_reminder_active_recipients_count=4` · `reporting_sync_mode=manual` · `/reminder_status` prefers live ACCESS

## Profiles

1. Андрей — admin — active — cards — personalization ON  
2. Оля — moderator — active — cards — personalization ON  
3. Михаил — moderator — active — cards — personalization ON  
4. Никита — moderator — active — cards — personalization ON  

## Prior soak note

Attempt 3 / prior T+0 STOP reclassified via erratum: operator-approved baseline change 3→4 (not a security incident). See Phase 3H.6 report.

## Immutable soak baseline

See `product/PRODUCTION-BASELINE-PRE-AI-SOAK-FOUR-RECIPIENT-v1.md`.


## Phase 3H.7.1 note
Gmail OAuth recovery closed; original terminal cards now expose `↩️ Вернуть в обработку`; MISSED_PROD_LEAD_1 resolved without replay (no absent genuine form lead); soak restarted; Phase 3I.1 blocked.

## Phase 3H.7.2 note
Callback acknowledgement contract `iseo-lead-callback-ack-v1.0` deployed. Reopen ack is «Лид возвращён в обработку.». Aggregate no longer maps pending applied→processed. Operator-approved resurface of three genuine leads completed for acceptance; global reopen still does not fan out. Soak restarted; Phase 3I.1 blocked. See `evidence/phase3h72/`.

