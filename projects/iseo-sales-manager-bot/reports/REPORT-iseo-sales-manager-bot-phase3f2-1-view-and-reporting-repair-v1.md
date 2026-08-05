# REPORT — ISEO SALES MANAGER BOT PHASE 3F.2.1 TELEGRAM ARCHIVE, HISTORY COMMAND AND REPORTING MAPPING REPAIR

## 1. Verdict

**COMPLETE — VIEW AND REPORTING REPAIR READY; OPERATOR ACCEPTANCE PENDING**

## 2. Operator-approved scope

Repair Phase 3F.2 acceptance defects without redesigning clean-ledger architecture: `/leads` mapping, `/lead_history` route, reporting keyed mapper + CLIENT_A resync, human source display.

## 3. Starting contour

Operational.dev active (45), Admin.dev active (79→82), Sales-Manager-v2 inactive, AI OFF, reminders OFF, sole Gmail intake, LEADS=1 CLIENT_A processed/Мопс.

## 4. Live acceptance defects

See `evidence/phase3f2-1/LIVE-ACCEPTANCE-DEFECTS-v1.md`.

## 5. `/leads` root cause

Unused Phase 3F.2 helper; formatter still bound to legacy CLEAN field names (`manager_status`/`service`/`summary`). Details: `LEADS-MAPPING-ROOT-CAUSE-v1.md`.

## 6. Canonical lead-view adapter

Implemented (`phase3f21_canonical_lead_view` + shared private lib). Precedence per charter.

## 7. `/leads` repair

Archive card shows processed, service, comment, timestamps, actor, source display, first reply; no action buttons.

## 8. `/lead_history` router defect

Documented mention only; absent from Route Command → «Команда не найдена».

## 9. `/lead_history` repair

New history read/handler nodes; route aligned before Switch fallback; staff auth for moderators.

## 10. History UX

Human Russian labels; list-number resolution; invalid guidance; no internal IDs.

## 11. Reporting mapping root cause

Positional seed + header `indexOf`/row metadata leakage class. See `REPORTING-27-ROOT-CAUSE-v1.md`.

## 12. Erroneous numeric values

Live post-resync `27` remaining = **0**.

## 13. Keyed reporting mapper

Explicit ordered schema; additive readiness column; reply text column stores text only.

## 14. Source display mapping

`source_channel=gmail_form` retained; `source_display=Сайт i-seo.su` on CLIENT_A + future Ops emission.

## 15. First-reply column

`Готовый первый ответ` = actual text; `Черновик ответа готов` = Да/Нет.

## 16. Human event labels

Mapper covers received/delivered/reconciled/synced codes → Russian.

## 17. CLIENT_A targeted resync

One row updated; no duplicate; lifecycle untouched.

## 18. Reporting `Лиды`

PASS sanitized acceptance (source/status/actor/reply/human last event).

## 19. Reporting `История изменений`

Human-readable events; actor Мопс on reconciliation.

## 20. Reporting `Статистика`

received=1 / processed=1 / pending=0 / spam=0 / tests=0 / epoch 05.08.2026 / Europe/Moscow / avg 80 мин.

## 21. Reporting `Справка`

Epoch + source explanation + privacy/schema present.

## 22. Backend/Telegram/reporting consistency

PASS for listed invariants (operator Telegram visual still pending).

## 23. Callback regression

Canonical token contract preserved; harness token identity PASS; no CLIENT_A re-press.

## 24. Pending regression

Expected zero pending for clean generation (operator reconfirm).

## 25. Reminder state

enabled=false; 10:00; Europe/Moscow; include_tests=false — kept OFF.

## 26. Harness

82/82 PASS.

## 27. Live command acceptance

Workflow wiring verified. Operator must re-run Telegram commands for visual packet confirmation.

## 28. Operator visual acceptance

**PENDING** — packet below.

### Operator acceptance packet (expected)

`/leads`: archive card CLIENT_A, ✅ Обработан, received 05.08.2026 16:02 МСК, changed ~17:22 МСК, Кем: Мопс, Интерес Требует уточнения, comment Добрый день!, Источник Сайт i-seo.su, first reply block, archive notice, no buttons.

`/lead_history 1`: recognized; human events; no internal IDs.

`/pending_count` / `/pending_leads`: zero (unless later real pending).

`/reminder_status`: OFF / 10:00 / Europe/Moscow.

`/help`: includes `/leads`, `/lead_history`, pending, reminder_status.

Reporting sanitized: source Сайт i-seo.su; reply text; no `27`; stats 1/1/0/0.

## 29. Final backend state

LEADS rows=1; lifecycle=processed; actor=Мопс; source_display set.

## 30. Final reporting state

Лиды rows=1; history humanized; stats clean; справка updated.

## 31. Final workflow state

Admin 82 nodes active; Ops 45 active; SM-v2 inactive.

## 32. Final access state

Андрей admin/active; Мопс moderator/active; Оля/Никита revoked — **unchanged**.

## 33. Safety counters

| Counter | Value |
|---|---|
| backend CLIENT_A rows | 1 |
| reporting CLIENT_A rows | 1 |
| duplicate reporting rows | 0 |
| erroneous 27 remaining | 0 |
| /leads lifecycle mismatches | 0 |
| /leads missing service | 0 |
| /leads missing request | 0 |
| /lead_history recognized | 1 |
| human-facing machine event codes | 0 |
| source display | Сайт i-seo.su |
| reporting received/processed/pending/spam | 1/1/0/0 |
| reminders enabled | false |
| AI provider calls | 0 |
| automatic client messages | 0 |
| workflows created | 0 |
| access-role changes | 0 |
| real leads lost/duplicated | 0/0 |
| destructive deletions | 0 |
| destructive Git operations | 0 |

## 34. Files created

`evidence/phase3f2-1/*`, `architecture/HUMAN-FACING-SOURCE-MAPPING-v1.md`, `implementation/LEAD-VIEW-ADAPTER-v1.md`, `implementation/REPORTING-KEYED-MAPPER-v1.md`, `implementation/LEAD-HISTORY-COMMAND-v1.md`, this report.

## 35. Files changed

README, OPERATIONAL-INDEX, product baselines/limitations, architecture ledger/event/reporting docs, implementation specs, guides.

## 36. Security validation

No PII/IDs/workbook URLs/tokens committed. Private raw workflow JSON remains under STORAGE only.

## 37. Commit

See git log after staging allowlisted `projects/iseo-sales-manager-bot/**`.

## 38. Push

To `origin/mars/canonical-post-recovery` (no force).

## 39. Risks

- Operator has not yet visually confirmed Telegram output in this wave.
- Continuous new-lead reporting sync still partial (known limitation).
- CLEAN vs LEADS dual-write unification deferred (not redesigned here).

## 40. SAFE UNKNOWN

- Exact historical cell that first introduced operator-observed `27` in an exported XLSX snapshot (class proven; live count now 0).
- Full LEAD_EVENTS schema column aliases for every legacy row (history filters by lead_id/public id).

## 41. Remaining operator actions

1. Run acceptance commands as Андрей and Мопс.
2. Confirm reporting workbook visuals.
3. Confirm reminders remain OFF.
4. Confirm no duplicate CLIENT_A.

## 42. Stop condition

Repair deployed + harness PASS + evidence/report committed. **Stop for operator visual acceptance.** Do not enable reminders/AI/SM-v2; do not create workflows; do not contact CLIENT_A.
