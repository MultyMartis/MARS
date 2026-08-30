# I-SEO Report Hub — DB-04 Weekly Checkpoints Migration Apply Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Weekly Checkpoints DB-04 Migration Apply 01  
**Related:** [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md), [REPORT-iseo-report-hub-db04-weekly-checkpoints-migration-apply-01.md](../reports/REPORT-iseo-report-hub-db04-weekly-checkpoints-migration-apply-01.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Wave status | **complete** |
| Migration applied | **yes** |
| Demo weekly checkpoints created | **yes** (W1–W3) |
| Real client data | **none** |
| Credentials in docs/Git | **none** |

Target DB: `iseo_report_hub_dev` @ `127.0.0.1` only.

---

## 2. Migration

| Field | Value |
|-------|-------|
| Filename | `2026_07_26_000003_create_weekly_checkpoints_table.sql` |
| Source path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_26_000003_create_weekly_checkpoints_table.sql` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_26_000003_create_weekly_checkpoints_table.sql` |
| Checksum (SHA-256) | `8ab9c0e84a262ab9c8662cd502ab18943810dc6a034d2cd25a89935e2ddaacd3` |
| Batch | **3** |
| Ledger | `schema_migrations` row present; `checksum_ok` |
| Seed in migration | **none** |

---

## 3. Table

| Field | Value |
|-------|-------|
| Table | `weekly_checkpoints` |
| Engine / charset / collation | InnoDB / utf8mb4 / `utf8mb4_0900_ai_ci` |
| Columns (21) | `id`, `reporting_period_id`, `week_index`, `checkpoint_key`, `checkpoint_start`, `checkpoint_end`, `status` (default `draft`), `title`, `summary`, `work_done`, `findings`, `next_steps`, `risks`, `owner_user_id`, `reviewer_user_id`, `created_by`, `updated_by`, `reviewed_at`, `completed_at`, `created_at`, `updated_at` |
| PK | `id` |
| Unique | `uniq_weekly_checkpoints_period_week` (`reporting_period_id`, `week_index`); `uniq_weekly_checkpoints_period_key` (`reporting_period_id`, `checkpoint_key`) |
| Indexes | `idx_weekly_checkpoints_reporting_period_id`, `status`, `owner_user_id`, `reviewer_user_id`, `created_by`, `updated_by` |
| FK | `fk_weekly_checkpoints_reporting_period_id` → `reporting_periods(id)` **RESTRICT**; four user FKs → `users(id)` **SET NULL** |
| CHECK | `chk_weekly_checkpoints_week_index` (1–6); `chk_weekly_checkpoints_dates`; `chk_weekly_checkpoints_status` |

Constraint names follow DB-03 style (`fk_*` / `chk_*` / `uniq_*` / `idx_*`), not the alternate charter token `weekly_checkpoints_reporting_period_fk`.

---

## 4. DB Counts

| Metric | Before | After |
|--------|--------|-------|
| Migrations | **2** | **3** |
| Tables | **10** | **11** |
| reporting_periods | **2** | **2** (unchanged) |
| weekly_checkpoints | **0** (absent) | **3** |

Baseline org counts unchanged: users **1**; roles **6**; clients/projects/sites **1/1/1**.

---

## 5. Demo Rows

All linked to reporting period `2026-07` (id **1**, status `draft`). Owner/created_by/updated_by = local admin id **1**.

| Id | Week | Key | Status | Title / text markers |
|----|------|-----|--------|----------------------|
| 1 | 1 | `2026-07-W1` | `completed` | `Demo Week 1 — LOCAL_FIXTURE_ONLY`; text fields `LOCAL_FIXTURE_ONLY`; `completed_at` set |
| 2 | 2 | `2026-07-W2` | `reviewed` | `Demo Week 2 — LOCAL_FIXTURE_ONLY`; text fields `LOCAL_FIXTURE_ONLY`; `reviewed_at` set |
| 3 | 3 | `2026-07-W3` | `draft` | `Demo Week 3 — LOCAL_FIXTURE_ONLY`; text fields `LOCAL_FIXTURE_ONLY` |

---

## 6. Validation

| Check | Result |
|-------|--------|
| Structure (columns / indexes / FK / CHECK) | **pass** |
| Join to `reporting_periods` | **3** rows join for `2026-07` |
| Invalid `reporting_period_id` FK | **fail expected** SQLSTATE `23000` (rolled back) |
| Duplicate `(period, week_index)` | **fail expected** SQLSTATE `23000` (rolled back) |
| Duplicate `(period, checkpoint_key)` | **fail expected** SQLSTATE `23000` (rolled back) |
| `week_index` 0 / 7 CHECK | **fail expected** error 3819 (rolled back) |
| Date order CHECK | **fail expected** error 3819 (rolled back) |
| Invalid status CHECK | **fail expected** error 3819 (rolled back) |
| Idempotent second apply | `Nothing to apply. All migrations already applied.` |
| App regression GET | `/health` 200; `/login` 200; `/not-existing` 404; unauth `/reporting-periods` → `/login`; auth list/detail **200** with `2026-07` |
| Final row counts | weekly_checkpoints **3**; reporting_periods **2** unchanged |

---

## 7. Restrictions

- No production / remote DB
- No real client data
- No CRUD UI / app code / auth / health / fixture-tool edits
- No `reporting_periods` row mutation
- No DROP / TRUNCATE / DELETE
- No secrets / passwords / hashes / session ids in Git or this result
- No push

---

## 8. What Still Does Not Exist

- Weekly checkpoint CRUD
- Weekly checkpoint UI
- Monthly report editor
- Report blocks
- Topvisor imports
- Client portal

---

## 9. Next Phase

**Recommended:** `Weekly Checkpoints CRUD Charter 01`

**Why:** DB-04 table + local W1–W3 smoke rows exist under fixture period `2026-07`. Next product step is internal CRUD over this table (not monthly content DB-05 yet).

---

## 10. SAFE UNKNOWN

- Whether Apache `mod_php` session cookie domain/path defaults differ across future Laragon profile changes (auth smoke used file-based session injection matching prior CRUD wave).
- Exact HealthController expected table-count wording vs live table count **11** — health still may report older baseline wording; **not** updated this wave (no health code edits).
