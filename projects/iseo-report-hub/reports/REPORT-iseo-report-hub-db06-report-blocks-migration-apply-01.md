# REPORT — I-SEO REPORT HUB DB-06 REPORT BLOCKS MIGRATION APPLY 01

**project_id:** `iseo-report-hub`  
**Date:** 2026-07-26  
**Wave:** Report Blocks DB-06 Migration Apply 01  
**Result:** COMPLETE

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `f6cae2e8111617420f3395ebe2459be0783e7eaa` |
| Staged/index before | **empty** |
| i-SEO WIP before | **clean** |
| Foreign WIP | **preserved** (untouched) |
| Write scope | migration SQL + result/closeout docs + OPERATIONAL-INDEX; one runtime migration copy; local DB table + fixture inserts only |

---

## 2. Preflight

| Item | Result |
|------|--------|
| PHP executable | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` — present |
| MySQL executable | `X:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\bin\mysql.exe` — present (DB checks via PHP PDO) |
| DB target | `iseo_report_hub_dev` |
| DB host | `127.0.0.1` |
| Migration count before | **4** |
| Table count before | **12** |
| Baseline counts | users **1**; roles **6**; clients/projects/sites **1/1/1**; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1** |
| `report_blocks` before | **absent** |
| Monthly parent | id **1**, period `2026-07`, status `in_progress`, `LOCAL_FIXTURE_ONLY` |
| W1–W4 | ids **1/2/3/7** present by checkpoint_key |
| Runtime `.env.local` | **present** (not printed; not edited; not committed) |

---

## 3. Migration Source

| Field | Value |
|-------|-------|
| Filename | `2026_07_26_000005_create_report_blocks_table.sql` |
| Source path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_26_000005_create_report_blocks_table.sql` |
| SQL design | InnoDB / utf8mb4; parent FK RESTRICT; user FKs SET NULL; unique `(monthly_report_content_id, block_key)`; non-unique parent+sort index; JSON columns |
| block_type CHECK policy | **applied** — `chk_report_blocks_block_type` allowlist (stable on MySQL 8.4.3) |
| status CHECK policy | **applied** — `chk_report_blocks_status` |
| JSON field policy | MySQL `JSON` type only; no extra JSON CHECK |
| Seed in migration | **none** |

Constraint names use DB-05 style (`fk_report_blocks_*`, `chk_report_blocks_*`, `uniq_report_blocks_parent_key`).

---

## 4. Runtime Sync

| Check | Result |
|-------|--------|
| File copied | yes — only `_000005_create_report_blocks_table.sql` |
| Hash match | yes — SHA-256 `951bc88826a6155a624377b43851f1d6f7eadb8fdf7d229cb5bffe952eee3236` |
| `.env.local` untouched | yes |
| Broad sync | **no** |

---

## 5. Migration Apply

| Step | Result |
|------|--------|
| First run | Applied `2026_07_26_000005_create_report_blocks_table.sql` OK |
| Second run (idempotency) | `Nothing to apply. All migrations already applied.` |
| Migration count | **4 → 5** |
| Table count | **12 → 13** |
| Batch | **5** |
| Checksum | `951bc88826a6155a624377b43851f1d6f7eadb8fdf7d229cb5bffe952eee3236` |

---

## 6. Fixture Report Blocks

| Field | Value |
|-------|-------|
| Rows | **inserted** (5); none pre-existing |
| Parent monthly report id | **1** |
| Period key | `2026-07` |
| Block keys | `executive_summary`, `work_completed`, `results_summary`, `key_findings`, `next_month_plan` |
| Sort orders | 10 / 20 / 30 / 40 / 50 |
| Statuses | all `draft` |
| Markers | titles/bodies/summaries/JSON = `LOCAL_FIXTURE_ONLY` |
| Source weekly checkpoint ids | `[1, 2, 3, 7]` (W1–W4) |

---

## 7. DB Validation

| Check | Result |
|-------|--------|
| Columns | **20** present; JSON cols `data_json`, `source_weekly_checkpoint_ids`, `source_metric_refs` |
| FK | invalid parent → errno **1452** (rolled back) |
| Unique | duplicate parent+key → errno **1062** (rolled back) |
| CHECK status | invalid → errno **3819** (rolled back) |
| CHECK block_type | invalid → errno **3819** (rolled back) |
| JSON | invalid → errno **3140**; valid temp insert rolled back |
| Parent linkage | all 5 → monthly id 1 → `2026-07`; weekly ids resolve W1–W4 |
| Row counts | report_blocks **5**; reporting_periods **2** unchanged; weekly_checkpoints **4** unchanged; monthly_report_contents **1** unchanged (`in_progress`) |

---

## 8. App Regression Smoke

| Route | Result |
|-------|--------|
| `GET /health` | **200** |
| `GET /login` | **200** |
| `GET /not-existing` | **404** |
| `GET /reporting-periods` unauth | **302** → `/login` |
| `GET /reporting-periods` auth | **200** (shows `2026-07`) |
| `GET /reporting-periods/1` | **200** (weekly + monthly sections; demo monthly; `in_progress`) |
| `GET /reporting-periods/1/weekly-checkpoints` | **200** (W1–W4) |
| `GET /weekly-checkpoints/7` | **200** (W4) |
| `GET /reporting-periods/1/monthly-report` | **200** |
| `GET /monthly-reports/1` | **200** |
| `GET /monthly-reports/1/edit` | **200** |
| POST CRUD smoke | **not run** (out of scope) |

Auth smoke used session injection; no password / session id printed in this report.

---

## 9. Restrictions Confirmed

- no production DB
- no real client data
- no credentials in Git/report
- no password/hash/session in report
- no `.env` committed
- no source `.env.local`
- no CRUD UI/code edits
- no auth/health edits
- no fixture tool changes
- no reporting_period row mutation
- no weekly_checkpoint row mutation
- no monthly_report_contents mutation
- no DROP/TRUNCATE/DELETE
- no DB dump
- no WordPress
- no Composer/npm
- no vhost/hosts/service restart
- no demo/registry changes
- no push/fetch/pull/reset/clean/stash
- no broad git add

---

## 10. Documentation

| Artifact | Path |
|----------|------|
| Result doc | `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-MIGRATION-APPLY-RESULT-v0.1.md` |
| Closeout | `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db06-report-blocks-migration-apply-01.md` |
| OPERATIONAL-INDEX | updated — DB-06 migration apply status + next stage |

---

## 11. Commit

| Field | Value |
|-------|-------|
| Message | `feat(iseo-report-hub): add report blocks migration` |
| Exact-path git add | migration SQL + result doc + closeout report + OPERATIONAL-INDEX |
| Staged list | allowlisted i-SEO paths only (4 paths) |
| Commit hash | `1b71a0213c61844258a87afb68f9b796bd35443f` |
| Hash-record follow-up | `7393d7c1d287bb8d180e41be26d37f738e330821` — `docs(iseo-report-hub): record report blocks migration commit hash` (this report only) |
| HEAD after wave | `7393d7c1d287bb8d180e41be26d37f738e330821` |
| Push | **no** |

---

## 12. SAFE UNKNOWN

- Whether Apache `mod_php` session cookie domain/path defaults differ across future Laragon profile changes.
- Exact HealthController expected table-count wording vs live table count **13** — health not updated this wave.

---

## 13. Recommended Next Action

**I-SEO Report Hub — Report Blocks CRUD Charter 01**

---

## 14. Files Changed

### Git (Active Brain)

- `projects/iseo-report-hub/app-source/database/migrations/2026_07_26_000005_create_report_blocks_table.sql` (created)
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-MIGRATION-APPLY-RESULT-v0.1.md` (created)
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db06-report-blocks-migration-apply-01.md` (created)
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md` (updated)

### Runtime (not in Git)

- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_26_000005_create_report_blocks_table.sql` (copied)

### DB (`iseo_report_hub_dev` @ `127.0.0.1`)

- Created table `report_blocks`
- Inserted 5 local fixture report block rows for monthly report content id 1 / period `2026-07`
- Validation insert attempts rolled back
- Ledger: migration batch **5**

---

## 15. Git Actions

| Action | Done? |
|--------|-------|
| exact-path git add | **yes** (allowlisted only) |
| commit | **yes** (primary + optional hash-record) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout | **no** |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
