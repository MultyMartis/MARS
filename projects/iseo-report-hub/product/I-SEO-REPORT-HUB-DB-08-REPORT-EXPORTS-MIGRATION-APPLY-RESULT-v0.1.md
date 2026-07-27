# I-SEO Report Hub — DB-08 Report Exports Migration Apply Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export DB-08 Migration Apply 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md), [REPORT-iseo-report-hub-db08-report-exports-migration-apply-01.md](../reports/REPORT-iseo-report-hub-db08-report-exports-migration-apply-01.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Wave status | **complete** |
| Migration file | `2026_07_27_000007_create_report_exports_table.sql` |
| Applied | **yes** |
| DB target | `iseo_report_hub_dev` @ `127.0.0.1` only |
| Table created | **yes** — `report_exports` |
| Row count | **0** |
| No export rows | **yes** |
| No export files | **yes** |
| Existing business rows mutated | **no** |
| App / service / routes / UI | **none** this wave |
| Credentials in docs/Git | **none** |

---

## 2. Migration

| Field | Value |
|-------|-------|
| Filename | `2026_07_27_000007_create_report_exports_table.sql` |
| Source path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000007_create_report_exports_table.sql` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000007_create_report_exports_table.sql` |
| Checksum (SHA-256) | `130e1b2f0a58a5661f0be99aa254e628186c1df6e6252acabbdf97ffe5877baa` |
| Batch | **7** |
| Ledger | `schema_migrations` row present; `checksum_ok` |
| Seed / export INSERT | **none** |

### Columns (16)

`id`, `report_snapshot_id`, `monthly_report_content_id`, `export_key`, `format`, `status` (default `ready`), `storage_disk` (default `local`), `storage_path`, `filename`, `mime_type`, `file_size_bytes`, `checksum_sha256`, `source_snapshot_checksum_sha256`, `created_by`, `created_at`, `archived_at`

### Indexes

| Name | Columns | Unique |
|------|---------|--------|
| PRIMARY | `id` | yes |
| `uq_report_exports_export_key` | `export_key` | yes |
| `idx_report_exports_snapshot_format_status` | (`report_snapshot_id`, `format`, `status`) | no |
| `idx_report_exports_monthly_format_status` | (`monthly_report_content_id`, `format`, `status`) | no |
| (FK index) `fk_report_exports_created_by` | `created_by` | no |

### Foreign keys

| Constraint | Column | References | ON DELETE |
|------------|--------|------------|-----------|
| `fk_report_exports_snapshot` | `report_snapshot_id` | `report_snapshots(id)` | RESTRICT |
| `fk_report_exports_monthly` | `monthly_report_content_id` | `monthly_report_contents(id)` | RESTRICT |
| `fk_report_exports_created_by` | `created_by` | `users(id)` | SET NULL |

### CHECK constraints

| Constraint | Rule |
|------------|------|
| `chk_report_exports_format` | `format IN ('html','pdf')` |
| `chk_report_exports_status` | `status IN ('ready','failed','archived')` |

Engine / charset / collation: InnoDB / utf8mb4 / `utf8mb4_0900_ai_ci`.

---

## 3. DB Before / After

| Metric | Before | After |
|--------|--------|-------|
| schema_migrations | **6** | **7** |
| Tables | **14** | **15** |
| report_exports | absent | exists, **0** rows |
| reporting_periods | **2** | **2** (unchanged) |
| weekly_checkpoints | **4** | **4** (unchanged) |
| monthly_report_contents | **1** | **1** (unchanged) |
| report_blocks | **6** | **6** (unchanged) |
| report_snapshots | **1** | **1** (unchanged) |
| users / roles / clients / projects / sites | 1 / 6 / 1 / 1 / 1 | unchanged |

Monthly report content id **1**:

| Field | Before / after |
|-------|----------------|
| status | `finalized` (unchanged) |
| finalized_at | non-null (unchanged) |
| title | `Demo Monthly Report — July 2026 — LOCAL_FIXTURE_ONLY` |
| reporting_period_id | **1** |

Report snapshot id **1**:

| Field | Before / after |
|-------|----------------|
| snapshot_key | `monthly-1-v1` (unchanged) |
| version | **1** (unchanged) |
| status | `active` (unchanged) |
| checksum_sha256 | `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38` (unchanged) |
| render_mode | `blocks_primary` (unchanged) |

Report blocks (all **reviewed**, unchanged):

| block_key | sort_order | status |
|-----------|------------|--------|
| executive_summary | 15 | reviewed |
| work_completed | 20 | reviewed |
| results_summary | 30 | reviewed |
| risks_and_blockers | 35 | reviewed |
| key_findings | 40 | reviewed |
| next_month_plan | 50 | reviewed |

---

## 4. Validation

| Check | Result |
|-------|--------|
| Schema columns (16) | **pass** |
| Indexes (unique + composite status indexes) | **pass** |
| FKs (snapshot / monthly / created_by) | **pass** |
| CHECK format + status | **pass** (visible in `information_schema`) |
| Row count 0 | **pass** |
| Migration ledger row + checksum | **pass** |
| Unrelated business counts | **pass** (unchanged) |
| Snapshot checksum / monthly finalized | **pass** (unchanged) |
| No storage export files/dirs created | **pass** |

Procedure: `php tools/db-migrate.php apply` from Localhost runtime (env from runtime `.env.local`; password not printed).

---

## 5. Runtime Sync

| Item | Result |
|------|--------|
| Migration file copied source → runtime | **yes** (exact path only) |
| README sync (migrations line) | **yes** (exact path only) |
| `.env.local` | **untouched** |
| Broad sync | **no** |
| App code / tools sync | **no** |

---

## 6. Restrictions

Confirmed this wave:

- no production / remote DB;
- no real client data;
- no export rows inserted;
- no export files created;
- no mutation of reporting_periods / weekly_checkpoints / monthly_report_contents / report_blocks / report_snapshots rows;
- no app-source `app/**` / auth / health / tools edits;
- no DELETE / DROP / TRUNCATE;
- no secrets / credentials / password / hash in Git or this doc;
- no `.env` / source `.env.local`;
- no push / fetch / pull / reset / clean / stash / broad git add;
- no Composer / npm / WordPress / vhost / hosts / service restart;
- no demo workspace / registry changes.

---

## 7. Next Phase

**I-SEO Report Hub — Report Export HTML Artifact Implementation 01**

---

## 8. SAFE UNKNOWN

- Whether HTML Implementation 01 will create the first `report_exports` row for snapshot id 1 in the same wave as artifact file write, or split metadata vs file smoke — not decided in this apply wave.
- PDF export timing (post-HTML vs separate charter) — deferred per Export/PDF charter.
