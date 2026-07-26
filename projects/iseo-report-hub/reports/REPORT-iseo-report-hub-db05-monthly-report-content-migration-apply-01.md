# REPORT — I-SEO REPORT HUB DB-05 MONTHLY REPORT CONTENT MIGRATION APPLY 01

**project_id:** `iseo-report-hub`  
**Date:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Monthly Report Content DB-05 Migration Apply 01

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `ab51fbd0c23872709b53b334a0d38edbfd238c75` |
| Staged/index before | **empty** |
| i-SEO WIP before | **clean** (no modified/untracked under `projects/iseo-report-hub/`) |
| Foreign WIP | **preserved** (untouched) |
| Write scope | allowlisted migration SQL + result/closeout docs + OPERATIONAL-INDEX; one runtime migration file copy |

---

## 2. Preflight

| Check | Result |
|-------|--------|
| PHP executable | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` — present |
| MySQL executable | `X:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\bin\mysql.exe` — present (DB checks via PHP PDO) |
| DB target | `iseo_report_hub_dev` |
| DB host | `127.0.0.1` |
| Migration count before | **3** |
| Table count before | **11** |
| Baseline counts | users **1**; roles **6**; clients/projects/sites **1/1/1**; reporting_periods **2**; weekly_checkpoints **4** |
| Period `2026-07` | id **1**, `draft` |
| Weekly keys | W1 id1 `completed`; W2 id2 `reviewed`; W3 id3 `draft`; W4 id7 `skipped` |
| `monthly_report_contents` before | **absent** |
| Runtime `.env.local` | **present** (not printed; not edited; not committed) |

---

## 3. Migration Source

| Field | Value |
|-------|-------|
| Filename | `2026_07_26_000004_create_monthly_report_contents_table.sql` |
| Source path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_26_000004_create_monthly_report_contents_table.sql` |
| SQL design | InnoDB utf8mb4 table `monthly_report_contents`; unique period; status CHECK; period FK RESTRICT; user FKs SET NULL; JSON soft source-id list |
| JSON field policy | rely on MySQL `JSON` type; **no** extra JSON CHECK (portable style alignment with prior migrations) |
| Seed in migration | **none** |

---

## 4. Runtime Sync

| Check | Result |
|-------|--------|
| File copied | yes — only `_000004` migration |
| Hash match | yes — SHA-256 `91f367cdf73d1a4b1fcfa3175f190c0470cda86e5cd5706749e2d566c82430b8` |
| `.env.local` untouched | yes |
| Broad sync | **no** |

---

## 5. Migration Apply

| Step | Result |
|------|--------|
| First run | Applied `2026_07_26_000004_create_monthly_report_contents_table.sql` — OK |
| Second run (idempotency) | `Nothing to apply. All migrations already applied.` |
| Migrations before/after | **3 → 4** |
| Tables before/after | **11 → 12** |
| Batch | **4** |
| Checksum | `91f367cdf73d1a4b1fcfa3175f190c0470cda86e5cd5706749e2d566c82430b8` |

---

## 6. Demo Monthly Report Content

| Field | Value |
|-------|-------|
| Action | **inserted** (was absent) |
| Id | **1** |
| Status | `draft` |
| Title | `Demo Monthly Report — July 2026 — LOCAL_FIXTURE_ONLY` |
| Text markers | all content TEXT fields = `LOCAL_FIXTURE_ONLY` |
| Linked period | id **1** / `2026-07` |
| `source_weekly_checkpoint_ids` | `[1, 2, 3, 7]` from keys W1–W4 |
| Owner / created_by / updated_by | admin id **1** |

---

## 7. DB Validation

| Check | Result |
|-------|--------|
| Columns | **21** present |
| FK invalid period | expected fail SQLSTATE `23000` / 1452 (rolled back) |
| Unique duplicate period | expected fail SQLSTATE `23000` / 1062 (rolled back) |
| CHECK invalid status | expected fail errno **3819** (rolled back) |
| JSON invalid | expected fail SQLSTATE `22032` / 3140 (rolled back) |
| Row counts | monthly **1**; reporting_periods **2** unchanged; weekly_checkpoints **4** unchanged; W1–W4 statuses unchanged |

---

## 8. App Regression Smoke

HTTP GET only (no POST CRUD):

| Request | Result |
|---------|--------|
| `GET /health` | **200** |
| `GET /login` | **200** |
| `GET /not-existing` | **404** |
| `GET /reporting-periods` unauth | **302** → `/login` |
| `GET /reporting-periods` auth | **200**; contains `2026-07` |
| `GET /reporting-periods/1` auth | **200**; weekly section present; contains W4 |
| `GET /reporting-periods/1/weekly-checkpoints` auth | **200**; W1–W4 present |
| `GET /weekly-checkpoints/7` auth | **200** |
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

| Doc | Path |
|-----|------|
| Result | `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-MIGRATION-APPLY-RESULT-v0.1.md` |
| OPERATIONAL-INDEX | updated — DB-05 apply status + next stage |

---

## 11. Commit

| Field | Value |
|-------|-------|
| Staging | exact-path `git add` only (4 allowlisted paths) |
| Staged list | migration SQL; migration-apply result; this report; OPERATIONAL-INDEX |
| Commit message | `feat(iseo-report-hub): add monthly report content migration` |
| Commit hash | **PENDING_PRIMARY_COMMIT** |
| Hash-record follow-up | if needed — `docs(iseo-report-hub): record monthly report content migration commit hash` |
| Push | **no** |

---

## 12. SAFE UNKNOWN

- Whether Apache `mod_php` session cookie domain/path defaults differ across future Laragon profile changes.
- Exact HealthController expected table-count wording vs live table count **12** (health code not edited this wave).

---

## 13. Recommended Next Action

**I-SEO Report Hub — Monthly Report Content CRUD Charter 01**

---

## 14. Files Changed

### Git (Active Brain)

- `projects/iseo-report-hub/app-source/database/migrations/2026_07_26_000004_create_monthly_report_contents_table.sql` (created)
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-MIGRATION-APPLY-RESULT-v0.1.md` (created)
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-db05-monthly-report-content-migration-apply-01.md` (created)
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md` (updated)

### Runtime (not Git)

- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_26_000004_create_monthly_report_contents_table.sql` (copied; hash-matched)

### DB (`iseo_report_hub_dev` @ `127.0.0.1`)

- created table `monthly_report_contents`
- ledger row batch **4**
- inserted 1 local fixture monthly report content row (id **1**)
- validation attempts rolled back only

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
