# I-SEO Report Hub — DB-03 Reporting Periods Migration Apply Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub DB-03 Reporting Periods Migration Apply 01  
**Related:** [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md), [REPORT-iseo-report-hub-db03-reporting-periods-migration-apply-01.md](../reports/REPORT-iseo-report-hub-db03-reporting-periods-migration-apply-01.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Wave status | **complete** |
| Migration applied | **yes** |
| Migration count before / after | **1 → 2** |
| Table count before / after | **9 → 10** |
| Real client data | **none** |
| Credentials in docs/Git | **none** |

Target DB: `iseo_report_hub_dev` @ `127.0.0.1` only.

---

## 2. Migration File

| Field | Value |
|-------|-------|
| Source path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_25_000002_create_reporting_periods_table.sql` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_25_000002_create_reporting_periods_table.sql` |
| Checksum (SHA-256) | `5bc50e53ab20a347c8a278d1726be6c71d835b572f369a14d2256e3e986e3be9` |
| Batch | **2** |
| Ledger status | Row present; `checksum_ok` on `db-migrate.php status` |

---

## 3. Table Created

| Field | Value |
|-------|-------|
| Table | `reporting_periods` |
| Engine / charset / collation | InnoDB / utf8mb4 / `utf8mb4_0900_ai_ci` |
| Columns | `id`, `project_id`, `period_key`, `period_start`, `period_end`, `status` (default `draft`), `title`, `summary`, `owner_user_id`, `reviewer_user_id`, `created_by`, `updated_by`, `finalized_at`, `created_at`, `updated_at` |
| Status set | `draft`, `active`, `weekly_review`, `monthly_review`, `finalized`, `archived` |
| FK policy | `project_id` → `projects(id)` **RESTRICT**; user refs → `users(id)` **SET NULL** |
| Unique | `uniq_reporting_periods_project_period` on `(project_id, period_key)` |
| Indexes | `idx_reporting_periods_project_id`, `period_key`, `status`, `owner_user_id`, `reviewer_user_id`, `finalized_at`, `created_at` (+ PK + unique) |

---

## 4. DB Validation

| Check | Result |
|-------|--------|
| Table exists | **yes** |
| Columns / nullability / defaults | **match migration** |
| Indexes | **all required present** |
| Foreign keys | **5 FKs present** (project RESTRICT; four user SET NULL) |
| CHECK constraints | `chk_reporting_periods_dates`, `chk_reporting_periods_status` **present** |
| `period_key` shape CHECK | **omitted** — app-level validation preferred |
| Row counts | users **1**; roles **6**; clients **0**; projects **0**; reporting_periods **0** |
| Unique/FK insert smoke | **structural only** — no project fixture; no period row insert |

---

## 5. Idempotency

| Check | Result |
|-------|--------|
| Second `db-migrate.php apply` | `Nothing to apply. All migrations already applied.` |
| Checksum behavior | Match; no mismatch; no duplicate ledger/table error |

---

## 6. Health / App Smoke

| Endpoint | Result |
|----------|--------|
| `GET /health` | **HTTP 200**; DB connection **pass**; migration count **2**; latest migration = `2026_07_25_000002_create_reporting_periods_table.sql` |
| Health table count wording | Still reports `9 / 9` expected baseline — **expected limitation**; HealthController not updated this wave |
| `GET /login` | **HTTP 200** |
| `GET /not-existing` | **HTTP 404** |
| Auth baseline | **not modified** (no auth/app code edits) |

---

## 7. Restrictions

- No production / remote DB
- No real client data
- No fixture client/project/period rows
- No app / auth / CRUD UI code edits
- No schema beyond DB-03 `reporting_periods`
- No secrets / passwords / hashes in Git or this result

---

## 8. What Still Does Not Exist

- Reporting period CRUD
- Project/client fixture
- Weekly checkpoints tables
- Monthly report content tables
- UI forms for periods
- Client portal

---

## 9. Next Phase

**Recommended:** `Project/Client Local Fixture Charter 01`

**Why:** `clients`/`projects` remain **0/0**. Period insert, unique-key smoke, and meaningful Reporting Period CRUD validation all require at least one safe local project FK. Fixture-first unblocks CRUD without inventing real client data.

(Alternate later: `Reporting Period CRUD Charter 01` after a safe local fixture exists.)

---

## 10. SAFE UNKNOWN

- Whether HealthController expected-table list will be updated in a later charter (not in this wave).
- Exact operator preference between fixture-first vs CRUD-first if product wants UI shell before any rows.
