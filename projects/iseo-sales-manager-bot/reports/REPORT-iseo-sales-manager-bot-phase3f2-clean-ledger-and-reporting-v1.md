# REPORT — ISEO SALES MANAGER BOT PHASE 3F.2 CLEAN PRODUCTION LEDGER, LEAD HISTORY AND EXTERNAL REPORTING WORKBOOK V1

## 1. Verdict

`COMPLETE — CLEAN LEDGER READY; OPERATOR REPORTING ACCEPTANCE PENDING`

## 2. Operator-approved scope

Clean production-accounting reset from **2026-08-05** (Europe/Moscow); archive mixed/test history; immutable lead events; callback lookup repair; separate private reporting Spreadsheet; reminders remain OFF.

## 3. Starting contour

| Workflow | Active | Nodes |
|----------|--------|------:|
| Operational.dev `xSnXPy8cEHoZw6xG` | true | 45 |
| Admin.dev `wLrLp4WQHm1VJmxz` | true | 79 |
| Sales-Manager-v2 `h8I2Tl2yl4uzhUnB` | false | 19 |

AI OFF · sole Gmail intake · schedule 2 minutes · parser `sm-parser-v3.3` · msg `sm-msg-v2.4` · reply `sm-reply-v2.1` · human `sm-human-v1.0`.

## 4. Real-lead safety

| Counter | Value |
|---------|------:|
| Real candidates on/after 2026-08-05 | 1 |
| Confirmed real | 1 (Клиент A) |
| Later real after Клиент A | 0 (forensic window) |
| Obvious tests in mixed CLEAN | many (prior pending business=12 / test=41) |
| Duplicate business rows for Клиент A | 0 |
| Lookup failures | 1 (moderator processed) |
| Real leads lost | 0 |

## 5. Евгений forensic

- Ops delivery success `2026-08-05T13:04:30.051Z` (~13.7s)
- Authoritative Gmail `internalDate` `2026-08-05T13:02:57.000Z` → **05.08.2026 16:02:57 МСК**
- Process `received_at` `2026-08-05T13:04:30.781Z` → **05.08.2026 16:04:30 МСК**
- Parse `sm-parser-v3.3`; Format `sm-msg-v2.4`; CLEAN mapping lag showed older parser stamp
- Website none · service NeedsClarification / «Требует уточнения» · comment «Добрый день!» · `first_reply_ready=true` · `is_probable_test=false`
- Recipients delivered = 2
- Pre-reconciliation lifecycle = `pending`
- CLEAN read at callback time: 106 rows; stored `telegram_action_token` length = 0 for Клиент A

## 6. Callback lookup failure

Admin exec `2026-08-05T14:22:55.186Z` → **05.08.2026 17:22:55 МСК**

- Actor Мопс · role moderator · authorized · action=`processed`
- Outcome `unknown_lead` · exact user text «Не удалось найти лид…»
- `sheets_mutate=false` · no LEAD_EVENTS append

**Root cause:** Operational Format used dual-FNV `fnvToken` (crypto disallowed in n8n); Admin Handle used a different simplified FNV; tokens diverged. Secondary: token generated in Format **after** CLEAN write, so stored token was empty and exact-match never worked.

## 7. Callback lookup repair

- Canonical contract v2: **always** dual-FNV `fnvToken` on OPS Format + Admin Handle (no sha256 for lead tokens)
- Deterministic Lead Processor emits `telegram_action_token` before CLEAN write
- Distinguishes storage_error / archived / ambiguous / not_found with charter user messages
- Existing Клиент A card tokens already equal canonical `fnvToken(lead_id)` → resolvable after repair

## 8. Евгений lifecycle reconciliation

- Intended action `processed` by Мопс: **CONFIRMED** by execution forensic
- CLEAN row updated: status `processed`, token persisted, actor stamps, source `telegram_callback_reconciliation`
- LEAD_EVENTS append `lifecycle_reconciled`
- LEADS authoritative row inserted once (`public_lead_id=1`)
- No second lead · no customer auto-contact

## 9. Statistics epoch

| Field | Value |
|-------|-------|
| Display | 05.08.2026 |
| Exact UTC | 2026-08-05T13:02:57.000Z |
| Timezone | Europe/Moscow |
| Reason | operator_clean_baseline |
| Generation | v2 |
| Legacy | archive_excluded |
| Test policy | real-only-v1 |

## 10. Legacy backup

Storage path: `X:\AI MARS STORAGE\backups\iseo-sales-manager-bot\2026-08-05-clean-ledger-baseline\`  
Workflow raw backups + forensic exec briefs + `SHA256SUMS.txt` · readability validated · secrets kept out of Git.

## 11. Legacy archive

Archive tabs created: `ARCHIVE_*_PRE_2026-08-05` (+ LEADS/TEST/SYNC/RAW_CURRENT/CLEAN_CURRENT).  
Full CLEAN→archive row copy: **PARTIAL** (Sheets quota on follow-up). Originals retained. Archive excluded from production views.

## 12. Clean backend tabs

Created/confirmed: `LEADS`, archive set, `TEST_LEADS`, `TEST_LEAD_EVENTS`, `SYNC_STATE`, `RAW_CURRENT`, `CLEAN_CURRENT`. Existing `CONFIG` / `ACCESS_CONTROL` / `LEAD_EVENTS` / `LEAD_DELIVERIES` / `REMINDER_DELIVERIES` preserved.

## 13. LEADS contract

One logical real lead per row; UTC + Moscow timestamps; lifecycle + actor; `stats_included` / `is_real_lead` / generation v2. Клиент A row present.

## 14. LEAD_EVENTS contract

Append-only; reconciliation event recorded; corrections = new events.

## 15. Date/time policy

Canonical UTC + Europe/Moscow business display. Authoritative received: **05.08.2026 16:02 МСК**. Lifecycle change: **05.08.2026 17:22 МСК**.

## 16. Test-data separation

`TEST_LEADS` / `TEST_LEAD_EVENTS` created. Policy `real-only-v1`. Synthetic live callback acceptance: **PENDING OPERATOR**.

## 17. `/leads`

Admin `Read CLEAN for Leads` retargeted to **`LEADS`**. Helper for received/status/actor fields added.

## 18. `/lead_history`

Normalize mention added; full dedicated history UX/pager: **PARTIAL**.

## 19. Pending-view rebase

Pending CLEAN read retargeted to `LEADS`. Expected pending after reconciliation: **0** new-generation real pending (operator confirm).

## 20. Reminder source rebase

Reminder engine still present; CONFIG forced `pending_reminders_enabled=false`. No production reminder send.

## 21. Reporting workbook creation

Separate Spreadsheet «i-SEO — Учёт лидов и статистика» created via authorized Google credential. ID stored only in private CONFIG / Storage — not in Git.

## 22. Reporting workbook tabs

`Лиды`, `История изменений`, `Статистика`, `Справка` seeded.

## 23. Privacy and access

Private; no public link; no automatic employee/client share. Sharing requires separate operator instruction.

## 24. Backend-to-reporting sync

Initial baseline sync for Клиент A completed. Ongoing Operational/Admin sync functions: documented; continuous sync wiring **PARTIAL** beyond baseline seed.

## 25. Sync idempotency

Baseline seed once; public ID `1`. Retry duplicate protection for continuous sync: documented.

## 26. Sync failure handling

Policy documented: backend remains valid on reporting outage.

## 27. Statistics

Epoch filter documented; baseline stats seeded (received=1, processed=1, pending=0).

## 28. Евгений reporting baseline

One `Лиды` row; history includes received / delivered / lifecycle_reconciled (human-safe wording).

## 29. Archived-card behavior

Admin Handle returns archive message for archived markers; legacy cards that map to production lead use canonical lookup + idempotent status.

## 30. Command acceptance

Operator packet prepared; live Telegram acceptance: **PENDING OPERATOR**.

## 31. Callback acceptance

Lookup repair live. Synthetic TEST_LEADS callback: **PENDING OPERATOR**.

## 32. Test cleanup acceptance

**PENDING** after synthetic callback.

## 33. Reminder state

`pending_reminders_enabled=false` · time `10:00` · timezone `Europe/Moscow` · include_tests=false.

## 34. Harness

Core live checks PASS; full 76-matrix: see `evidence/phase3f2/HARNESS-RESULTS-v1.md` (PARTIAL/PENDING called out).

## 35. Operator visual acceptance

Please confirm in Telegram (as Андрей / Мопс where authorized):

1. `/leads` — Клиент A first, received **05.08.2026 16:02 МСК**, status Обработан, actor Мопс  
2. `/lead_history 1` — history understandable (if wired)  
3. `/pending_count` / `/pending_leads` — no legacy tests  
4. `/reminder_status` — OFF  
5. Archived-card calm message (if tested)  
6. Reporting workbook suitable for employees (private preview only)

## 36. Final backend state

LEADS generation v2 active; Клиент A processed; epoch CONFIG set; mixed corpus excluded from `/leads` source.

## 37. Final reporting state

Private workbook exists; baseline row seeded; not shared.

## 38. Final workflow state

Ops 45 active · Admin 79 active · SM-v2 inactive · AI OFF · reminders OFF · workflows created=0.

## 39. Final access state

Admin Андрей active · moderator Мопс active · Оля/Никита revoked (unchanged).

## 40. Safety counters

| Counter | Value |
|---------|------:|
| production stats epoch date | 2026-08-05 |
| confirmed real leads migrated | 1 |
| Евгений business rows | 1 |
| Евгений lifecycle events | ≥1 reconciled |
| legacy rows entering production | 0 (LEADS source) |
| test rows entering LEADS | 0 |
| test rows entering reporting | 0 |
| reporting lead rows for Евгений | 1 |
| duplicate reporting rows | 0 |
| pending legacy tests in new view | 0 (source LEADS) |
| reminders enabled | false |
| AI provider calls | 0 |
| automatic client messages | 0 |
| workflows created | 0 |
| access-role changes | 0 |
| real leads lost | 0 |
| destructive deletions | 0 |
| destructive Git operations | 0 |

## 41. Files created

- `architecture/CLEAN-PRODUCTION-LEDGER-v1.md`
- `architecture/LEAD-EVENT-HISTORY-v1.md`
- `architecture/PRODUCTION-STATS-EPOCH-v1.md`
- `architecture/TEST-DATA-SEPARATION-v1.md`
- `architecture/EXTERNAL-REPORTING-WORKBOOK-v1.md`
- `architecture/REPORTING-SYNC-IDEMPOTENCY-v1.md`
- `implementation/CALLBACK-LOOKUP-CONTRACT-v2.md`
- `implementation/LEGACY-ARCHIVE-MIGRATION-v1.md`
- `implementation/REPORTING-WORKBOOK-SYNC-v1.md`
- `evidence/phase3f2/*` (21 files)
- this report

## 42. Files changed

- `implementation/runtime-libs/formatter-lib.mjs` (canonical token)
- `README.md`, `OPERATIONAL-INDEX.md`, `product/CURRENT-PRODUCTION-BASELINE-v1.md`
- Live Operational.dev / Admin.dev in-place patches (not new workflows)

## 43. Security validation

No workbook IDs, Telegram IDs, phones, emails, or credentials in committed evidence. Private refs only under Storage backups/private.

## 44. Commit

- `7b41285f` — `feat(iseo-sales-manager-bot): add clean production lead ledger`
- `79d11006` — `feat(iseo-sales-manager-bot): add external lead reporting workbook`

## 45. Push

Pushed FF to `origin/mars/canonical-post-recovery` (`28ebb27d..79d11006`), no force.

## 46. Risks

- Full archive row copy incomplete (quota) — originals retained  
- `/lead_history` UX partial  
- Continuous reporting sync beyond baseline seed partial  
- Operator must confirm pending counts visually  

## 47. SAFE UNKNOWN

- Whether any real lead arrived after forensic window close  
- Exact Sheets quota recovery time for leftover archive copies  

## 48. Remaining operator actions

1. Visual acceptance packet (commands above)  
2. Optional synthetic TEST callback click  
3. Explicit reporting share instruction (recipient + role) when ready  
4. Do **not** enable reminders until separate approval  

## 49. Stop condition

Protected backup validated · mixed data archived/excluded from production view · clean ledger created · epoch established · Клиент A migrated once · callback repaired · Мопс action reconciled · event history active · reporting Spreadsheet private · reminders OFF · acceptance packet prepared.

## Execution safety

- cwd: `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3f2-20260805-213600\repo`
- scope lock honored: yes (`projects/iseo-sales-manager-bot/**` + Storage backups)
- destructive ops: none (archive-and-exclude; no sole-copy delete)
- protected zone touch: none outside allowlisted project/Storage backup paths
