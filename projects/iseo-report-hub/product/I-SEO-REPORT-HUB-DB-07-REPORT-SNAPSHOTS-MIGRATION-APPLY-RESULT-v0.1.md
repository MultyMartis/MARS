# I-SEO Report Hub — DB-07 Report Snapshots Migration Apply Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Snapshot DB-07 Migration Apply 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md), [REPORT-iseo-report-hub-db07-report-snapshots-migration-apply-01.md](../reports/REPORT-iseo-report-hub-db07-report-snapshots-migration-apply-01.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Wave status | **complete** |
| Migration file | `2026_07_27_000006_create_report_snapshots_table.sql` |
| Applied | **yes** |
| DB target | `iseo_report_hub_dev` @ `127.0.0.1` only |
| Table created | **yes** — `report_snapshots` |
| Row count | **0** |
| No snapshot rows | **yes** |
| Existing business rows mutated | **no** |
| App / service / routes / UI | **none** this wave |
| Credentials in docs/Git | **none** |

---

## 2. Migration

| Field | Value |
|-------|-------|
| Filename | `2026_07_27_000006_create_report_snapshots_table.sql` |
| Source path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000006_create_report_snapshots_table.sql` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000006_create_report_snapshots_table.sql` |
| Checksum (SHA-256) | `8f1890f6595f5f9fedb3f1366a5207fad9eca55f94dbcc549406313d192c6ab0` |
| Batch | **6** |
| Ledger | `schema_migrations` row present; `checksum_ok` |
| Seed / snapshot INSERT | **none** |

### Columns (17)

`id`, `monthly_report_content_id`, `reporting_period_id`, `snapshot_key`, `version` (default `1`), `status` (default `active`), `title`, `render_mode`, `payload_json`, `rendered_text`, `rendered_html`, `checksum_sha256`, `source_block_ids`, `source_weekly_checkpoint_ids`, `created_by`, `created_at`, `archived_at`

### Indexes

| Name | Columns | Unique |
|------|---------|--------|
| PRIMARY | `id` | yes |
| `uq_report_snapshots_monthly_version` | (`monthly_report_content_id`, `version`) | yes |
| `uq_report_snapshots_snapshot_key` | `snapshot_key` | yes |
| `idx_report_snapshots_monthly_status` | (`monthly_report_content_id`, `status`) | no |
| `idx_report_snapshots_period_status` | (`reporting_period_id`, `status`) | no |
| (FK index) `fk_report_snapshots_created_by` | `created_by` | no |

### Foreign keys

| Constraint | Column | References | ON DELETE |
|------------|--------|------------|-----------|
| `fk_report_snapshots_monthly` | `monthly_report_content_id` | `monthly_report_contents(id)` | RESTRICT |
| `fk_report_snapshots_period` | `reporting_period_id` | `reporting_periods(id)` | RESTRICT |
| `fk_report_snapshots_created_by` | `created_by` | `users(id)` | SET NULL |

### CHECK constraints

| Constraint | Rule |
|------------|------|
| `chk_report_snapshots_status` | `status IN ('active','superseded','archived')` |
| `chk_report_snapshots_version` | `version >= 1` |

Engine / charset / collation: InnoDB / utf8mb4 / `utf8mb4_0900_ai_ci`.

---

## 3. DB Before / After

| Metric | Before | After |
|--------|--------|-------|
| schema_migrations | **5** | **6** |
| Tables | **13** | **14** |
| report_snapshots | absent | exists, **0** rows |
| reporting_periods | **2** | **2** (unchanged) |
| weekly_checkpoints | **4** | **4** (unchanged) |
| monthly_report_contents | **1** | **1** (unchanged) |
| report_blocks | **6** | **6** (unchanged) |
| users / roles / clients / projects / sites | 1 / 6 / 1 / 1 / 1 | unchanged |

Monthly report content id **1**:

| Field | Before / after |
|-------|----------------|
| status | `finalized` (unchanged) |
| finalized_at | non-null (unchanged) |
| title | `Demo Monthly Report — July 2026 — LOCAL_FIXTURE_ONLY` |
| reporting_period_id | **1** |
| Fingerprint SHA-256 | `fed3ce67ec4f16c783c07c4c453047c3a4e5b7bb32ebe01d7b0d4e0a40622253` (unchanged) |

Report blocks (all **reviewed**, fingerprint unchanged `5edaad3bc3adb58f301e32616750bfdc0776f7167097ed25fe73d7deede4b00b`):

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
| Schema columns (17) | **pass** |
| Indexes (unique + status indexes) | **pass** |
| FKs (monthly / period / created_by) | **pass** |
| CHECK status + version | **pass** (visible in `information_schema.CHECK_CONSTRAINTS`) |
| Row count 0 | **pass** |
| Migration ledger row + checksum | **pass** |
| Unrelated business counts | **pass** (unchanged) |
| Monthly / blocks fingerprints | **pass** (unchanged) |

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
- no snapshot rows inserted;
- no mutation of reporting_periods / weekly_checkpoints / monthly_report_contents / report_blocks rows;
- no app-source `app/**` / auth / health / tools edits;
- no DELETE / DROP / TRUNCATE;
- no secrets / credentials / password / hash in Git or this doc;
- no `.env` / source `.env.local`;
- no push / fetch / pull / reset / clean / stash / broad git add;
- no Composer / npm / WordPress / vhost / hosts / service restart;
- no demo workspace / registry changes.

---

## 7. Next Phase

**I-SEO Report Hub — Report Snapshot Implementation 01**

---

## 8. SAFE UNKNOWN

- Whether Implementation 01 will create the first active snapshot for monthly id 1 in the same wave as service/routes, or split create-smoke separately — not decided in this apply wave.
- Multi-role HTTP create/view smoke may remain deferred if only admin_owner session injection exists (same pattern as finalization).
