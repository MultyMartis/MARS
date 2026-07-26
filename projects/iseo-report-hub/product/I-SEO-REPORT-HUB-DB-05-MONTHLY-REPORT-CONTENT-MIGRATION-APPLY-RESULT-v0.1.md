# I-SEO Report Hub — DB-05 Monthly Report Content Migration Apply Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Monthly Report Content DB-05 Migration Apply 01  
**Related:** [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md), [REPORT-iseo-report-hub-db05-monthly-report-content-migration-apply-01.md](../reports/REPORT-iseo-report-hub-db05-monthly-report-content-migration-apply-01.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Wave status | **complete** |
| Migration applied | **yes** |
| Demo monthly row created | **yes** (1 row for period `2026-07`) |
| Real client data | **none** |
| Credentials in docs/Git | **none** |

Target DB: `iseo_report_hub_dev` @ `127.0.0.1` only.

---

## 2. Migration

| Field | Value |
|-------|-------|
| Filename | `2026_07_26_000004_create_monthly_report_contents_table.sql` |
| Source path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_26_000004_create_monthly_report_contents_table.sql` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_26_000004_create_monthly_report_contents_table.sql` |
| Checksum (SHA-256) | `91f367cdf73d1a4b1fcfa3175f190c0470cda86e5cd5706749e2d566c82430b8` |
| Batch | **4** |
| Ledger | `schema_migrations` row present; `checksum_ok` |
| Seed in migration | **none** |

---

## 3. Table

| Field | Value |
|-------|-------|
| Table | `monthly_report_contents` |
| Engine / charset / collation | InnoDB / utf8mb4 / `utf8mb4_0900_ai_ci` |
| Columns (21) | `id`, `reporting_period_id`, `status` (default `draft`), `title`, `executive_summary`, `work_completed`, `results_summary`, `key_findings`, `risks_and_blockers`, `next_month_plan`, `client_notes`, `internal_notes`, `source_weekly_checkpoint_ids` (JSON), `owner_user_id`, `reviewer_user_id`, `created_by`, `updated_by`, `reviewed_at`, `finalized_at`, `created_at`, `updated_at` |
| PK | `id` |
| Unique | `uniq_monthly_report_contents_period` (`reporting_period_id`) |
| Indexes | `idx_monthly_report_contents_status`, `owner_user_id`, `reviewer_user_id`, `created_by`, `updated_by` |
| FK | `fk_monthly_report_contents_reporting_period_id` → `reporting_periods(id)` **RESTRICT**; four user FKs → `users(id)` **SET NULL** |
| CHECK | `chk_monthly_report_contents_status` — status allowlist |
| JSON field policy | MySQL `JSON` column type enforces valid JSON for non-null values; **no** extra portable JSON CHECK added (matches existing migration style; documented decision) |

Constraint names follow DB-03/DB-04 style (`fk_*` / `chk_*` / `uniq_*` / `idx_*`), not the alternate charter token `monthly_report_contents_reporting_period_fk`.

---

## 4. DB Counts

| Metric | Before | After |
|--------|--------|-------|
| Migrations | **3** | **4** |
| Tables | **11** | **12** |
| reporting_periods | **2** | **2** (unchanged) |
| weekly_checkpoints | **4** | **4** (unchanged) |
| monthly_report_contents | **0** (absent) | **1** |

Baseline org counts unchanged: users **1**; roles **6**; clients/projects/sites **1/1/1**.

---

## 5. Demo Row

Linked to reporting period `2026-07` (id **1**, status `draft`). Owner/created_by/updated_by = local admin id **1**.

| Field | Value |
|-------|-------|
| Id | **1** |
| Status | `draft` |
| Title | `Demo Monthly Report — July 2026 — LOCAL_FIXTURE_ONLY` |
| Text fields | all `LOCAL_FIXTURE_ONLY` |
| `source_weekly_checkpoint_ids` | `[1, 2, 3, 7]` resolved from keys `2026-07-W1`…`W4` |

---

## 6. Validation

| Check | Result |
|-------|--------|
| Structure (columns / indexes / FK / CHECK / JSON type) | **pass** |
| Join to `reporting_periods` | **pass** (demo row → `2026-07`) |
| Invalid `reporting_period_id` FK | **fail expected** SQLSTATE `23000` errno 1452 (rolled back) |
| Duplicate `reporting_period_id` unique | **fail expected** SQLSTATE `23000` errno 1062 (rolled back) |
| Invalid status CHECK | **fail expected** errno 3819 (rolled back) |
| Invalid JSON | **fail expected** SQLSTATE `22032` errno 3140 (rolled back) |
| Valid JSON temp insert | **pass** then rolled back; count remains **1** |
| Idempotent second apply | `Nothing to apply. All migrations already applied.` |
| App regression GET | `/health` 200; `/login` 200; `/not-existing` 404; unauth `/reporting-periods` → `/login`; auth list/detail/weekly list/W4 detail **200** |
| Final row counts | monthly_report_contents **1**; reporting_periods **2**; weekly_checkpoints **4** unchanged |

---

## 7. Restrictions

- No production / remote DB
- No real client data
- No CRUD UI / app code / auth / health / fixture-tool edits
- No `reporting_periods` row mutation
- No `weekly_checkpoints` row mutation
- No DROP / TRUNCATE / DELETE
- No secrets / passwords / hashes / session ids in Git or this result
- No push

---

## 8. What Still Does Not Exist

- Monthly report CRUD
- Monthly report UI / editor
- Report blocks
- PDF / export
- Topvisor imports
- Client portal

---

## 9. Next Phase

**Recommended:** `Monthly Report Content CRUD Charter 01`

**Why:** DB-05 table + local demo monthly row exist under fixture period `2026-07`. Next product step is internal CRUD over this table (not report blocks DB-06 yet).

---

## 10. SAFE UNKNOWN

- Whether Apache `mod_php` session cookie domain/path defaults differ across future Laragon profile changes (auth smoke used file-based session injection matching prior waves).
- Exact HealthController expected table-count wording vs live table count **12** — health not updated this wave (no health code edits).
