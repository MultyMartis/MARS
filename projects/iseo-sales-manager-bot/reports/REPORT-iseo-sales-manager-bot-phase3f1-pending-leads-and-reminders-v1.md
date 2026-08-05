# REPORT — ISEO SALES MANAGER BOT PHASE 3F.1 PENDING LEADS COMMANDS AND DAILY REMINDERS V1

## 1. Verdict

`COMPLETE — COMMANDS AND REMINDER ENGINE READY; OPERATOR ACTIVATION PENDING`

Pending-lead visibility commands and a daily reminder engine were implemented on Admin.dev, offline harness passed 73/73, and live command acceptance covered admin/moderator/revoked paths. A controlled live reminder-schedule exercise reached the ACCESS_CONTROL step and correctly failed closed under a Sheets quota condition. Production reminders remain switched off pending an explicit operator activation decision.

## 2. Operator-approved scope

Phase 3F.1 is limited to `projects/iseo-sales-manager-bot/**`: pending-lead view commands, reminder engine implementation and CONFIG contract, evidence, architecture/implementation docs, status docs, and this report. No AI activation, no access change, no Operational.dev change, no new workflow, no client auto-message, and no reminder production activation was authorized.

## 3. Phase 3E.2 final closeout (entry condition)

The operator completed visual confirmation of the Phase 3E.2.3 final proof card. Verdict: `PHASE 3E.2 COMPLETE — HUMAN FIRST REPLY ENGINE READY`. Confirmed: operator visual proof, Human Reply Style, copy block, no known-data re-ask; one card to Андрей and one to Мопс with no repeats; Sheets amplification fix holds (empty-poll writes=0); Phase 3E.2.3 offline harness 83/83 PASS; AI OFF; client auto-messages=0; real leads lost=0. Detail: `evidence/phase3f1/PHASE3E2-FINAL-CLOSEOUT-v1.md`.

## 4. Admin.dev patch summary

Same workflow ID `wLrLp4WQHm1VJmxz`. Node count **59 → 79** (+20): pending-lead view nodes, reminder command nodes, and an internal reminder schedule branch. In-place patch, not a new workflow. Detail: `implementation/PENDING-COMMANDS-v1.md`, `implementation/REMINDER-CONFIG-COMMANDS-v1.md`.

## 5. Operational.dev state

Unchanged: 45 nodes, active, `minutesInterval=2`, AI OFF. No patch was applied to Operational.dev in this phase.

## 6. Pending source forensic

Authoritative rule: `manager_status` primary, `lifecycle_status` secondary, `close_reason` tertiary; legacy rows with none of these populated default to pending unless a close signal is present. Detail: `evidence/phase3f1/PENDING-SOURCE-FORENSIC-v1.md`.

## 7. Pending view contract

`buildPendingView()` excludes technical-retry rows, invalid/empty-shell rows, and probable-test rows (by default); deduplicates by business key; sorts oldest-first; buckets by age. Detail: `evidence/phase3f1/PENDING-VIEW-CONTRACT-v1.md`, `architecture/PENDING-LEADS-VIEW-v1.md`.

## 8. `/pending_count` command

Compact count + age-bucket summary; Admin-only diagnostic test-count addendum. Live-accepted for admin and moderator; denied for revoked. Detail: `evidence/phase3f1/PENDING-COUNT-ACCEPTANCE-v1.md`.

## 9. `/pending_leads` command

Paginated, HTML-escaped, oldest-first list; `/pending_leads_test` is the Admin-only test-inclusive variant. Message length stayed well under the Telegram 4096-character limit. Detail: `evidence/phase3f1/PENDING-LIST-ACCEPTANCE-v1.md`.

## 10. Pagination

Default page size 5, maximum 10; out-of-range pages clamp to the last valid page rather than erroring. Detail: `evidence/phase3f1/PAGINATION-ACCEPTANCE-v1.md`.

## 11. Command authorization matrix

Staff-read class (`/pending_count`, `/pending_leads`, `/reminder_status`) allows active Admin/moderator; admin-config class (`/pending_leads_test`, all `/reminder_*` mutators) is Admin-only. Revoked/pending/public denied first, before any command-class check. Detail: `evidence/phase3f1/COMMAND-AUTHORIZATION-v1.md`.

## 12. Reminder CONFIG contract

New CONFIG keys under `pending_reminder_version=sm-pending-reminder-v1.0`; `pending_reminders_enabled=false` default; `pending_reminder_time=10:00`; `pending_reminder_timezone=Europe/Moscow`. Time/timezone inputs are validated before any write. Detail: `evidence/phase3f1/REMINDER-CONFIG-CONTRACT-v1.md`.

## 13. Reminder schedule gate

`isReminderWindowDue()` fails closed at every branch: disabled, invalid config, outside window, already-completed window all resolve to zero sends. Detail: `evidence/phase3f1/REMINDER-SCHEDULE-GATE-v1.md`, `architecture/PENDING-REMINDER-v1.md`.

## 14. Reminder window key

`pending-reminder:<date>:<time>:<timezone>` — deterministic, PII-free, one key per calendar day at the configured time/timezone. Detail: `evidence/phase3f1/REMINDER-WINDOW-KEY-v1.md`.

## 15. Reminder recipient snapshot

Active Admin/moderator only, sourced from the same ACCESS_CONTROL registry as the rest of the product; revoked/public/pending/blocked always excluded. Detail: `evidence/phase3f1/REMINDER-RECIPIENT-SNAPSHOT-v1.md`.

## 16. `REMINDER_DELIVERIES` ledger

New additive Sheets tab; no existing tab schema changed; empty in production. Key: `<reminder_window>|<recipient_ref>`. Detail: `evidence/phase3f1/REMINDER-DELIVERY-LEDGER-v1.md`, `implementation/SHEETS-MIGRATION-SPEC-v1.md`.

## 17. Reminder idempotency

Two layers — window-level (CONFIG guard) and recipient-level (ledger claim-before-send) — prevent both whole-batch repetition across 15-minute checks and per-recipient resend on partial failure. Detail: `evidence/phase3f1/REMINDER-IDEMPOTENCY-v1.md`, `architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md`.

## 18. Reminder Sheets call budget

A non-due schedule tick costs one bounded CONFIG read; a due window is bounded to roughly 4 reads + 4 writes + 1 CONFIG update for 2 eligible recipients — not a per-poll amplifier. Detail: `evidence/phase3f1/REMINDER-SHEETS-CALL-BUDGET-v1.md`.

## 19. Controlled reminder live acceptance

The schedule path reached `Gate → CLEAN → ACCESS`; the ACCESS_CONTROL read hit a live Sheets quota condition and the engine correctly produced **zero sends** rather than a partial or fallback delivery. Production was left with `pending_reminders_enabled=false`, `pending_reminder_time=10:00`, `pending_reminder_timezone=Europe/Moscow`. Detail: `evidence/phase3f1/CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md`.

## 20. Post-lifecycle pending acceptance

A lead marked processed or spam via the existing callback path immediately disappears from the pending view; buttons, callback tokens, and actor attribution are unchanged. Detail: `evidence/phase3f1/POST-LIFECYCLE-PENDING-ACCEPTANCE-v1.md`.

## 21. Harness results

`node implementation/harness/phase3f1-harness.mjs` → **73/73 PASS** (63 required checks + 10 extra consistency checks). Detail: `evidence/phase3f1/HARNESS-RESULTS-v1.md`, `evidence/phase3f1/HARNESS-RESULTS-RAW.json`.

## 22. Live command acceptance matrix

| Actor | `/pending_count` | `/pending_leads` | `/reminder_status` | Config-class command |
|---|---|---|---|---|
| Admin (active) | PASS — showed live business pending count | PASS | PASS — extended form | PASS |
| Moderator (active) | PASS | PASS | PASS — short form, showed disabled | denied |
| Revoked | denied | denied | denied | denied |

An invalid `/reminder_time` value was rejected without a CONFIG write.

## 23. Example Telegram text — `/pending_count`

```
Необработанных заявок: 4
до 2 часов: 1 · 2–24 часа: 1 · старше суток: 2
```

## 24. Example Telegram text — `/pending_leads`

```
1. 3 д 2 ч · Легаси
Audit · legacy.ru
Старая запись без lifecycle
Черновик ответа: готов

2. 2 д 5 ч · Мария
Разработка сайта · shop-demo.ru
Нужен новый сайт каталога
Черновик ответа: нет

Страница 1 из 1 · всего 4
```

## 25. Example Telegram text — `/reminder_status` (moderator, short form)

```
⏰ Напоминания о заявках
Статус: выключены
Время: 10:00
Часовой пояс: Europe/Moscow
```

## 26. Example Telegram text — reminder message template

```
⏰ Напоминание о заявках

Необработанных заявок: 4
Старше суток: 2
Самая старая: 3 д 2 ч

Посмотреть список: /pending_leads

Сначала обратите внимание на самые старые заявки.
```

## 27. Example Telegram text — moderator denied config command

```
Недостаточно прав для этой команды.
```

(Exact deny wording follows the existing Admin deny convention; no configuration values or counts are leaked to a denied caller.)

## 28. Access state

Unchanged: Андрей — active admin; Мопс — active moderator; Оля and Никита remain revoked, not restored. Reminder eligible recipients: **2**.

## 29. Final workflow state

Admin.dev active, 79 nodes. Operational.dev active, unchanged, 45 nodes. Sales-Manager-v2 inactive. AI OFF. No new workflow. Detail: `evidence/phase3f1/FINAL-WORKFLOW-STATE-v1.md`.

## 30. Counters

| Counter | Value | Note |
|---|---:|---|
| Pending business leads in fixture snapshot | 4 | 2 fresh leads + 1 legacy-compatible + 1 missing-timestamp (harness fixtures). Live production had more historical pending items at various points — not re-measured as part of this offline fixture count; see `evidence/phase3f1/PENDING-COUNT-ACCEPTANCE-v1.md` |
| Test leads excluded (harness) | 1 | |
| Processed control excluded (harness) | 1 | |
| Reminder eligible recipients | 2 | Андрей (admin), Мопс (moderator) |
| Controlled reminder sends | 0 | Sheets quota fail-closed on ACCESS_CONTROL; engine ready |
| Revoked reminder sends | 0 | |
| Reminder duplicate sends | 0 | |
| Later schedule-check sends | 0 | |
| Production reminders enabled | false | |
| AI provider calls | 0 | |
| Automatic client messages | 0 | |
| Workflows created | 0 | |
| Access changes | 0 | |
| Operational.dev changes | 0 | |
| Destructive migrations | 0 | |

## 31. Fail-closed preservation

Every reminder-engine failure branch (disabled, invalid config, outside window, already-completed, ledger read error, claim failure, stamp uncertainty, ACCESS_CONTROL quota) resolves to zero-send or reconciliation-required — never a default-to-send or blind resend.

## 32. Lifecycle regression

Buttons, callback payloads, actor attribution, archive behavior, and AI OFF contracts remain unchanged (harness #43–#54; contract checks documented explicitly as contract vs. proven-live where applicable).

## 33. Admin compatibility

`/my_status`, `/moderator_pending`, `/moderators`, `/leads`, and both callback outcomes were exercised as regression stubs and remain unaffected by the Admin.dev patch.

## 34. Sheets migration

One new additive tab, `REMINDER_DELIVERIES`; no existing tab schema (`CONFIG`, `lead_clean_v2`, `LEAD_DELIVERIES`, `LEAD_EVENTS`, `ACCESS_CONTROL`, `ACCESS_EVENTS`) was altered. Detail: `implementation/SHEETS-MIGRATION-SPEC-v1.md` §Phase 3F.1.

## 35. Documentation set

19 new evidence files under `evidence/phase3f1/`; 3 new architecture docs; 2 new implementation docs; 12 existing docs updated surgically with additive Phase 3F.1 sections; 1 draft spec annotated as implemented; this report.

## 36. Safety counters

| Counter | Value |
|---|---:|
| offline harness pass rate | 73/73 |
| live command acceptance failures | 0 |
| reminder sends in controlled window | 0 |
| AI provider calls | 0 |
| automatic client messages | 0 |
| workflows created | 0 |
| access changes | 0 |
| Operational.dev changes | 0 |
| destructive Git operations | 0 |
| new Sheets tabs (additive) | 1 |
| existing Sheets tab schemas altered | 0 |

## 37. Files created

Under `projects/iseo-sales-manager-bot/`:

- `evidence/phase3f1/PHASE3E2-FINAL-CLOSEOUT-v1.md`
- `evidence/phase3f1/PENDING-SOURCE-FORENSIC-v1.md`
- `evidence/phase3f1/PENDING-VIEW-CONTRACT-v1.md`
- `evidence/phase3f1/PENDING-COUNT-ACCEPTANCE-v1.md`
- `evidence/phase3f1/PENDING-LIST-ACCEPTANCE-v1.md`
- `evidence/phase3f1/PAGINATION-ACCEPTANCE-v1.md`
- `evidence/phase3f1/REMINDER-CONFIG-CONTRACT-v1.md`
- `evidence/phase3f1/REMINDER-SCHEDULE-GATE-v1.md`
- `evidence/phase3f1/REMINDER-WINDOW-KEY-v1.md`
- `evidence/phase3f1/REMINDER-RECIPIENT-SNAPSHOT-v1.md`
- `evidence/phase3f1/REMINDER-DELIVERY-LEDGER-v1.md`
- `evidence/phase3f1/REMINDER-IDEMPOTENCY-v1.md`
- `evidence/phase3f1/REMINDER-SHEETS-CALL-BUDGET-v1.md`
- `evidence/phase3f1/COMMAND-AUTHORIZATION-v1.md`
- `evidence/phase3f1/CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md`
- `evidence/phase3f1/POST-LIFECYCLE-PENDING-ACCEPTANCE-v1.md`
- `evidence/phase3f1/FINAL-WORKFLOW-STATE-v1.md`
- `evidence/phase3f1/PHASE3F1-ACCEPTANCE-RECEIPT-v1.md`
- `architecture/PENDING-LEADS-VIEW-v1.md`
- `architecture/PENDING-REMINDER-v1.md`
- `architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md`
- `implementation/PENDING-COMMANDS-v1.md`
- `implementation/REMINDER-CONFIG-COMMANDS-v1.md`
- this report: `reports/REPORT-iseo-sales-manager-bot-phase3f1-pending-leads-and-reminders-v1.md`

Pre-existing (created earlier in this task window, kept unchanged): `evidence/phase3f1/HARNESS-RESULTS-v1.md`, `evidence/phase3f1/HARNESS-RESULTS-RAW.json`, `implementation/harness/phase3f1-harness.mjs`, `implementation/runtime-libs/pending-leads-lib.mjs`.

## 38. Files changed

`README.md`, `OPERATIONAL-INDEX.md`, `product/CURRENT-PRODUCTION-BASELINE-v1.md`, `product/PRODUCT-ARCHITECTURE-v1.md`, `product/KNOWN-LIMITATIONS-v1.md`, `product/PRODUCT-ROADMAP-v1.md`, `product/PENDING-LEAD-REMINDER-SPEC-v1-DRAFT.md`, `architecture/TELEGRAM-UX-CONTRACT-v1.md`, `architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md`, `implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md`, `implementation/SHEETS-MIGRATION-SPEC-v1.md`, `implementation/TEST-HARNESS-SPEC-v1.md`, `guides/OLYA-LEAD-WORK-GUIDE-v1.md`, `guides/OPERATOR-RUNBOOK-v1.md`.

## 39. Security validation

No secrets, Telegram/chat identifiers, workbook identifiers, phone numbers, email addresses, real domains, credential hashes, or raw workflow exports were copied into committed-scope evidence. Access-state descriptions use role labels only (admin/moderator/revoked), never raw IDs.

## 40. Commit

**PENDING_PUSH — parent agent.**

Expected primary message:

`feat(iseo-sales-manager-bot): add pending-lead commands and daily reminder engine`

Optional second message if the parent splits documentation from implementation evidence:

`docs(iseo-sales-manager-bot): record phase 3f1 pending leads and reminder acceptance`

Canonical tip base for this worktree: `56c3d9ed`.

## 41. Push

**PENDING_PUSH — parent agent.** No push was performed as part of this task.

## 42. Risks

- Google Sheets still lacks atomic CAS; the reminder ledger inherits the same best-effort-sequential limitation as lead delivery.
- The controlled live window only proved the fail-closed path under quota, not a full successful dual-recipient send.
- A 15-minute schedule checker inspecting a 20-minute due window means up to ~2 checks can observe "due" before the window-key guard is written — window-key idempotency is the load-bearing control here, not the schedule interval itself.
- `REMINDER_DELIVERIES` is a new tab; any future manual edit to it outside the documented lifecycle could desynchronize idempotency state.

## 43. SAFE UNKNOWN

- Exact appearance of the reminder message in the operator's/moderator's live Telegram client (pending operator visual check).
- Whether a full non-quota dual-recipient reminder send will complete without incident on the next attempt — not yet observed.
- Live production pending-count history prior to this phase (only the fixture snapshot count is reported honestly here).

## 44. Operator visual acceptance packet

Example texts are reproduced in §23–§27 above (pending_count, pending_leads, reminder_status, reminder message template, moderator denied config). Please confirm the following points (charter AF.1–AF.10):

1. `/pending_count` text is clear and matches what you expect to see for the current queue.
2. `/pending_leads` list formatting (age, name, service, site, summary, draft status) is readable and useful.
3. `/reminder_status` moderator (short) form is accurate and contains no confusing internal terms.
4. `/reminder_status` Admin (extended) form is accurate and useful for diagnosis.
5. The reminder message template tone and content are acceptable for a daily nudge.
6. The moderator-denied wording for a config-class command is acceptable and does not leak configuration.
7. Leaving reminders **OFF** with default `10:00` `Europe/Moscow` is acceptable for now.
8. No PII, lead IDs, or Telegram identifiers appear in any of the texts above.
9. The pending-business-count wording and age buckets match what Оля/Андрей would find useful day-to-day.
10. You are not requesting immediate reminder activation as part of this closeout — activation remains a separate, explicit future decision.

Reminders stay **OFF** until you explicitly authorize activation.

## 45. Remaining operator actions

1. Review the example texts and confirm the 10 points in §44.
2. Decide whether/when to authorize `pending_reminders_enabled=true` in production — this report does not request that activation.
3. After confirmation, the parent agent may perform selective commit/push per the approved git wave.
4. Do not enable AI, restore revoked access, or activate the rollback workflow as part of this closeout.

## 46. Non-goals confirmed unchanged

First Reply Engine v2.1, Human Reply Style v1, card format `sm-msg-v2.4`, delivery fail-closed reconciliation for lead cards, Operational.dev topology, and access state are all unchanged by Phase 3F.1.

## 47. Stop condition

Stop at:

`COMPLETE — COMMANDS AND REMINDER ENGINE READY; OPERATOR ACTIVATION PENDING`

Do not activate production reminders and do not claim a live non-quota dual-send proof beyond what is recorded in `evidence/phase3f1/CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md` until the operator explicitly authorizes the next step.
