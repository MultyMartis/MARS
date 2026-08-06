# REPORT — ISEO SALES MANAGER BOT PHASE 3H.4.1 LAST PRODUCTION PROCESSED STATUS READBACK REPAIR

## 1. Verdict

`PHASE 3H.4.1 COMPLETE — STATUS READBACK REPAIRED; FINAL 48-HOUR SOAK RESTARTED`

## 2. Operator approval

Operator approved a narrow repair of the `/status` last-production-processed timestamp. Production lead ledger must not be rewritten. No Phase 3I.1, AI, reminder, profile, or reporting changes.

## 3. Starting operator evidence

`/stats` processed=1 · `/pending_count`=0 · `/leads` shows PROD_LEAD_1 processed @ 17:22 МСК · `/status` showed `нет данных`. See `evidence/phase3h4-1/STARTING-OPERATOR-EVIDENCE-v1.md`.

## 4. Starting contour

Ops `xSnXPy8cEHoZw6xG` 45 active · Admin `wLrLp4WQHm1VJmxz` 85 active · v2 inactive · AI OFF · reminders ON · recipients 3 · Никита revoked.

## 5. Pre-repair backup

Private backups under `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3h41-*/runtime/backups/pre-repair/`. Sanitized manifest: `evidence/phase3h4-1/PRE-REPAIR-BACKUP-MANIFEST-v1.md`. Status sha before: `2138ecea…e596ad`.

## 6. Production lead truth

One production lead (PROD_LEAD_1): processed; received ~16:02 МСК; lifecycle_changed_at `2026-08-05T14:22:55.186Z` (= 17:22 МСК); actor MOD_A; pending=0; spam=0. **No lead row mutation.**

## 7. `/status` execution forensic

Path: Telegram → Normalize → Read CONFIG → Collapse `config_map` → Authorize → Route → Status → Telegram. Pre-repair CONFIG keys `last_production_processed_*` present with **empty values**; synthetic `last_lead_success_at` still 22:23 source.

## 8. Readback root cause

Phase 3H.4 Status correctly stopped using synthetic 22:23. Phase 3H.4 CONFIG backfill wrote **empty** `value` cells (webhook body nesting: `processed_at` not on top-level json). Status fail-closed to `нет данных`. Not missing production data.

## 9. Source precedence

Contract `iseo-last-production-processed-v1.0`: LEAD_EVENTS → LEADS → CONFIG cache → `нет данных`.

## 10. CONFIG mapping

Post-repair: `last_production_processed_at=2026-08-05T14:22:55.186Z` (len 24) · lead id cache set · aligned `last_processed_*`. Legacy `last_lead_success_at` retained but unused for production line.

## 11. LEADS verification

prod leads=1 · processed=1 · pending=0 · spam=0 · lifecycle_changed_at matches 17:22 МСК.

## 12. LEAD_EVENTS verification

No production event appended this phase. Display does not require a new event when LEADS + CONFIG cache agree.

## 13. Synthetic timestamp exclusion

22:23 synthetic stamp excluded from `/status` production line. Acceptance `has_2223=false`.

## 14. Repair

Admin.dev Status Code patched (same ID, 85 nodes). CONFIG cache rewritten from LEADS via self-contained Prep (no empty webhook body). Operational.dev not modified.

## 15. Timestamp parser

Accepts ISO UTC strings and Date objects; rejects invalid/empty.

## 16. Europe/Moscow formatting

`05.08.2026 17:22 МСК`.

## 17. Dynamic future behavior

Later valid production processed timestamps replace earlier ones; exclusions keep tests/synth/spam/pending/delivery/reminder/pre-epoch out. No hardcoded date/lead id in Status code.

## 18. `/status` live result

`Последний обработанный лид: 05.08.2026 17:22 МСК`

## 19. `/stats` consistency

received=1; pending=0; processed=1; spam=0

## 20. `/pending_count` consistency

0

## 21. `/leads` consistency

Same processed lead @ 17:22 МСК

## 22. Health regression

`/health` acceptance reply delivered; AI OFF; contour active.

## 23. Reminder-status regression

Reminders ON · 10:00 Europe/Moscow · recipients 3.

## 24. No-silent regression

Recognized read-only commands returned visible replies.

## 25. Production invariants

AI OFF · OpenRouter=0 · auto-send=0 · Ops unchanged · Admin active 85 · v2 inactive · workflows created=0 · access changes=0 · profile wipes=0 · leads lost/duplicated=0 · drafts modified=0.

## 26. Harness

`phase3h41-harness.mjs` **23/23 PASS**.

## 27. Post-repair backup

`runtime/backups/post-repair/` + `evidence/phase3h4-1/POST-REPAIR-BACKUP-MANIFEST-v1.md`. Status sha after: `422130ee…e7a642`.

## 28. Soak Attempt 1

`SOAK ATTEMPT 1 — INTERRUPTED BY OBSERVABILITY REPAIR` (preserved).

## 29. Soak Attempt 2

`SOAK ATTEMPT 2 — INTERRUPTED BY LAST-PROCESSED STATUS READBACK REPAIR`.

## 30. Final soak start

**2026-08-06 16:20 Europe/Moscow**

## 31. Earliest valid completion

**2026-08-08 16:20 Europe/Moscow**

## 32. Final workflow state

Ops 45 active · Admin 85 active · v2 inactive · workflows created=0.

## 33. Final profile state

Андрей / Оля / Михаил active+enabled cards; Никита revoked+disabled.

## 34. Final reminder state

Enabled · 10:00 Europe/Moscow · min pending 1 · tests/archives excluded · recipients 3.

## 35. Final reporting state

manual / только вручную

## 36. Final AI state

OFF

## 37. Production statistics

received=1 · pending=0 · processed=1 · spam=0

## 38. Safety counters

production leads inspected=1 · processed=1 · pending=0 · lead rows modified=0 · events appended=0 · inconsistent status fields remaining=0 · OpenRouter=0 · customer auto-messages=0 · Operational changes=0 · Admin ID unchanged · workflows created=0 · access changes=0 · profile wipes=0 · leads lost=0 · leads duplicated=0 · historical drafts modified=0 · Phase 3I.1 started=false

## 39. Files created

- `architecture/LAST-PRODUCTION-PROCESSED-CONTRACT-v1.md`
- `implementation/LAST-PROCESSED-STATUS-READBACK-REPAIR-v1.md`
- `evidence/phase3h4-1/*` (21+ receipts)
- `reports/REPORT-iseo-sales-manager-bot-phase3h4-1-last-processed-status-repair-v1.md`

## 40. Files changed

README.md · OPERATIONAL-INDEX.md · product baselines/limitations/roadmap · architecture status/ledger contracts · implementation status/admin/text specs · guides operator + pre-AI soak runbooks.

## 41. Security validation

No Telegram IDs, phones, emails, customer names/domains, workbook IDs, raw executions, or unsanitized workflow exports committed. Aliases PROD_LEAD_1 / ADMIN_A / MOD_A / MOD_B / MOD_C_REVOKED only.

## 42. Commit

- fix: `7dda2d43799edaefc4703a957f33a51244a9bee5` — restore last production processed status
- docs: `b8dd6494025e3c4c3684e55cba88328ac1a8c1e7` — restart final pre-ai soak


## 43. Push

Pending push to `origin/mars/canonical-post-recovery` (no force).


## 44. Risks

CONFIG cache can drift if a future writer persists empty values again; Operational delivery success still writes synthetic-capable `last_lead_success_at` (must stay unused for production line). Callback path does not yet stamp production cache on every processed transition (documented follow-up; not in this narrow charter).

## 45. SAFE UNKNOWN

Whether every historical LEAD_EVENTS row uses a single canonical `event_type` string for processed — LEADS lifecycle_changed_at remains authoritative for this lead. Exact wall-clock of operator’s original Telegram `/status` screenshot not re-fetched (defect reproduced via live CONFIG probe).

## 46. Remaining operator actions

1. Confirm `/status` in Telegram as ADMIN_A shows 17:22 МСК.
2. Run soak checkpoints per `guides/PRE-AI-SOAK-RUNBOOK-v1.md`.
3. Do not start Phase 3I.1 until soak PASS.

## 47. Phase 3I.1 gate

**Blocked.** Soak PASS not claimed.

## 48. Stop condition

Stop after production truth verified, `/status`=17:22, stats/leads/status agree, no production mutation, observability intact, reminders unchanged, post-repair backup done, final soak restarted, Phase 3I.1 blocked. **Met.**

