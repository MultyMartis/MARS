# I-SEO Report Hub — DB-06 Report Blocks Migration Apply Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Report Blocks DB-06 Migration Apply 01  
**Related:** [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md), [REPORT-iseo-report-hub-db06-report-blocks-migration-apply-01.md](../reports/REPORT-iseo-report-hub-db06-report-blocks-migration-apply-01.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Wave status | **complete** |
| Migration applied | **yes** |
| Fixture report blocks created | **yes** (5 rows for monthly report content id **1** / period `2026-07`) |
| Real client data | **none** |
| Credentials in docs/Git | **none** |
| CRUD UI/code changes | **none** |

Target DB: `iseo_report_hub_dev` @ `127.0.0.1` only.

---

## 2. Migration

| Field | Value |
|-------|-------|
| Filename | `2026_07_26_000005_create_report_blocks_table.sql` |
| Source path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_26_000005_create_report_blocks_table.sql` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_26_000005_create_report_blocks_table.sql` |
| Checksum (SHA-256) | `951bc88826a6155a624377b43851f1d6f7eadb8fdf7d229cb5bffe952eee3236` |
| Batch | **5** |
| Ledger | `schema_migrations` row present; `checksum_ok` |
| Seed in migration | **none** |

---

## 3. Table

| Field | Value |
|-------|-------|
| Table | `report_blocks` |
| Engine / charset / collation | InnoDB / utf8mb4 / `utf8mb4_0900_ai_ci` |
| Columns (20) | `id`, `monthly_report_content_id`, `block_key`, `block_type`, `sort_order` (default `0`), `status` (default `draft`), `title`, `body`, `summary`, `data_json`, `source_weekly_checkpoint_ids`, `source_metric_refs`, `owner_user_id`, `reviewer_user_id`, `created_by`, `updated_by`, `reviewed_at`, `approved_at`, `created_at`, `updated_at` |
| PK | `id` |
| Unique | `uniq_report_blocks_parent_key` (`monthly_report_content_id`, `block_key`) |
| Ordering index | `idx_report_blocks_parent_sort` (`monthly_report_content_id`, `sort_order`) — **non-unique** |
| Other indexes | `idx_report_blocks_parent_type`, `idx_report_blocks_status`, `owner_user_id`, `reviewer_user_id`, `created_by`, `updated_by` |
| FK | `fk_report_blocks_monthly_report_content_id` → `monthly_report_contents(id)` **RESTRICT**; four user FKs → `users(id)` **SET NULL** |
| CHECK | `chk_report_blocks_status` (status allowlist); `chk_report_blocks_block_type` (block_type allowlist) — both applied |
| JSON field policy | MySQL `JSON` type for `data_json`, `source_weekly_checkpoint_ids`, `source_metric_refs`; **no** extra portable JSON CHECK |

Constraint names follow DB-03/DB-04/DB-05 style (`fk_*` / `chk_*` / `uniq_*` / `idx_*`), not the alternate charter token `report_blocks_monthly_report_content_fk`.

---

## 4. DB Counts

| Metric | Before | After |
|--------|--------|-------|
| Migrations | **4** | **5** |
| Tables | **12** | **13** |
| reporting_periods | **2** | **2** (unchanged) |
| weekly_checkpoints | **4** | **4** (unchanged) |
| monthly_report_contents | **1** | **1** (unchanged; id **1** status remains `in_progress`) |
| report_blocks | **0** (absent) | **5** |

Baseline org counts unchanged: users **1**; roles **6**; clients/projects/sites **1/1/1**.

---

## 5. Fixture Blocks

Parent: monthly report content id **1** / reporting period `2026-07` (id **1**). Owner/created_by/updated_by = local admin id **1**.

| block_key / block_type | sort_order | status |
|------------------------|------------|--------|
| `executive_summary` | 10 | `draft` |
| `work_completed` | 20 | `draft` |
| `results_summary` | 30 | `draft` |
| `key_findings` | 40 | `draft` |
| `next_month_plan` | 50 | `draft` |

All titles/bodies/summaries/JSON markers: `LOCAL_FIXTURE_ONLY`.  
`source_weekly_checkpoint_ids` = `[1, 2, 3, 7]` resolved from keys `2026-07-W1`…`W4`.  
`data_json` = `{"marker":"LOCAL_FIXTURE_ONLY"}`; `source_metric_refs` = `{"marker":"LOCAL_FIXTURE_ONLY","refs":[]}`.

---

## 6. Validation

| Check | Result |
|-------|--------|
| Structure (columns / indexes / FK / CHECK / JSON type) | **pass** |
| Invalid `monthly_report_content_id` FK | **fail expected** SQLSTATE `23000` errno 1452 (rolled back) |
| Duplicate `(parent, block_key)` unique | **fail expected** SQLSTATE `23000` errno 1062 (rolled back) |
| Invalid status CHECK | **fail expected** errno 3819 / SQLSTATE `HY000` (rolled back) |
| Invalid block_type CHECK | **fail expected** errno 3819 / SQLSTATE `HY000` (rolled back) |
| Invalid JSON | **fail expected** SQLSTATE `22032` errno 3140 (rolled back) |
| Valid JSON temp insert | **pass** then rolled back; count remains **5** |
| Parent linkage | **pass** (all 5 → monthly id 1 → period `2026-07`; weekly ids resolve W1–W4) |
| Idempotent second apply | `Nothing to apply. All migrations already applied.` |
| App regression GET | `/health` 200; `/login` 200; `/not-existing` 404; unauth `/reporting-periods` → `/login`; auth list/detail/weekly list/W4/monthly show+edit **200** |
| Final row counts | report_blocks **5**; monthly_report_contents **1**; reporting_periods **2**; weekly_checkpoints **4** unchanged |

---

## 7. Restrictions

- No production / remote DB
- No real client data
- No CRUD UI / app code / auth / health / fixture-tool edits
- No `reporting_periods` row mutation
- No `weekly_checkpoints` row mutation
- No `monthly_report_contents` row mutation
- No DROP / TRUNCATE / DELETE
- No secrets / passwords / hashes / session ids in Git or this result
- No push

---

## 8. What Still Does Not Exist

- Report block CRUD / editor
- Drag / drop reorder product
- PDF / export
- Topvisor imports / metric tables
- Client portal / public share
- Evidence / uploads
- Hard FK from JSON weekly/metric refs

---

## 9. Next Phase

**Recommended:** `Report Blocks CRUD Charter 01`

**Why:** DB-06 table + local fixture blocks exist under monthly content id **1** / period `2026-07`. Next product step is internal CRUD over `report_blocks` (not further DB hardening).

---

## 10. SAFE UNKNOWN

- Whether Apache `mod_php` session cookie domain/path defaults differ across future Laragon profile changes (auth smoke used file-based session injection matching prior waves).
- Exact HealthController expected table-count wording vs live table count **13** — health not updated this wave (no health code edits).
