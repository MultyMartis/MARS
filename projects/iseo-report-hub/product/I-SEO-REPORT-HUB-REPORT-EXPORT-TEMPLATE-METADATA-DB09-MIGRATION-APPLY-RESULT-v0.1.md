# I-SEO Report Hub — Report Export Template Metadata DB-09 Migration Apply Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export Template Metadata DB-09 Migration Apply 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md)
- [REPORT-iseo-report-hub-report-export-template-metadata-db09-migration-apply-01.md](../reports/REPORT-iseo-report-hub-report-export-template-metadata-db09-migration-apply-01.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Wave status | **complete** |
| Migration applied | **yes** |
| Backfill applied | **yes** (ids **3–4** only) |
| Final `schema_migrations` count | **8** |
| `report_exports` count unchanged | **yes** (still **4**) |
| Artifact checksums unchanged | **yes** |
| No public/share | **yes** |
| No package install | **yes** |
| DB target | `iseo_report_hub_dev` @ `127.0.0.1` only |
| App / repository / UI code | **none** this wave |
| Credentials in docs/Git | **none** |

---

## 2. Migration

| Field | Value |
|-------|-------|
| Filename | `2026_07_27_000008_add_template_metadata_to_report_exports_table.sql` |
| Checksum (SHA-256) | `75202829747e4a15138e2a89760fc68995e5e2cc56f1b20b80664f7a08eb37d0` |
| Batch | **8** |
| Ledger | `schema_migrations` row present; `checksum_ok` |
| `schema_migrations` before → after | **7 → 8** |
| Tables before → after | **15 → 15** |

### Columns added (nullable)

| Column | Type |
|--------|------|
| `template_id` | `VARCHAR(100)` NULL |
| `template_version` | `VARCHAR(50)` NULL |
| `render_target` | `VARCHAR(50)` NULL |
| `render_engine` | `VARCHAR(100)` NULL |
| `render_options_json` | `JSON` NULL |
| `source_html_export_id` | `BIGINT UNSIGNED` NULL |
| `metadata_json` | `JSON` NULL |

Column placement: after `source_snapshot_checksum_sha256`, before `created_by` (MySQL `AFTER` chain).

### Indexes

| Name | Columns |
|------|---------|
| `idx_report_exports_template` | (`template_id`, `template_version`) |
| `idx_report_exports_source_html` | (`source_html_export_id`) |

### Foreign key

| Constraint | Column | References | ON DELETE |
|------------|--------|------------|-----------|
| `fk_report_exports_source_html_export` | `source_html_export_id` | `report_exports(id)` | **SET NULL** |

No CHECK on template fields. No `report_templates` table. No sidecar table.

---

## 3. Runtime Sync

| Field | Value |
|-------|-------|
| Source migration path | `projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000008_add_template_metadata_to_report_exports_table.sql` |
| Runtime migration path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_27_000008_add_template_metadata_to_report_exports_table.sql` |
| Sync method | exact-file copy only |
| Source/runtime checksum match | **yes** |
| `.env.local` | **untouched** (exists; not printed; not committed) |
| Broad sync / app code copy | **no** |

---

## 4. Backfill

| id | Policy / result |
|----|-----------------|
| **1** | leave metadata **NULL** / legacy not recorded — **unchanged** |
| **2** | leave metadata **NULL** / legacy not recorded — **unchanged** |
| **3** | `template_id=iseo_default_v1`, `template_version=1`, `render_target=html_export`, `render_engine=php_template_renderer`, `source_html_export_id=NULL` + safe JSON options/metadata |
| **4** | `template_id=iseo_default_v1`, `template_version=1`, `render_target=pdf_export`, `render_engine=edge_headless_pdf`, `source_html_export_id=3` + safe JSON options/metadata |

### Gates (all required)

- id **3**: `export_key=snapshot-1-html-v2`, `format=html`, `status=ready`, checksum `27a6eee6…f95f6ffe`
- id **4**: `export_key=snapshot-1-pdf-v2`, `format=pdf`, `status=ready`, checksum `a8c4d61c…41a56b6b`
- id **3** verified present before id **4** update

### Affected rows

| Step | id 3 | id 4 |
|------|------|------|
| First successful gated apply path | updated **1** (then MySQL 1093 blocked id 4 on an EXISTS self-join; script fixed) | — |
| Resume after script fix | already matched | updated **1** |
| Idempotent re-run | already matched (0) | already matched (0) |

Temp backfill script (not in Git): `X:\AI MARS STORAGE\incoming\iseo-report-hub\db09-metadata-apply-01\backfill-db09.php`.

---

## 5. DB Validation

| Metric | Before | After |
|--------|--------|-------|
| schema_migrations | **7** | **8** |
| tables | **15** | **15** |
| report_exports | **4** | **4** |
| html / pdf rows | **2** / **2** | **2** / **2** |
| report_snapshots | **1** | **1** |
| monthly_report_contents | **1** | **1** |
| report_blocks | **6** | **6** |
| reporting_periods | **2** | **2** |
| weekly_checkpoints | **4** | **4** |
| clients / projects / sites | **1** / **1** / **1** | unchanged |
| users / roles | **1** / **6** | unchanged |

### Row metadata matrix

| id | template_id | template_version | render_target | render_engine | source_html_export_id |
|----|-------------|------------------|---------------|---------------|-----------------------|
| 1 | NULL | NULL | NULL | NULL | NULL |
| 2 | NULL | NULL | NULL | NULL | NULL |
| 3 | `iseo_default_v1` | `1` | `html_export` | `php_template_renderer` | NULL |
| 4 | `iseo_default_v1` | `1` | `pdf_export` | `edge_headless_pdf` | **3** |

JSON columns on ids 3–4: valid JSON. No DELETE/DROP/TRUNCATE. No export row insert/delete.

---

## 6. Artifact Validation

| Artifact | Checksum | Unchanged |
|----------|----------|-----------|
| `monthly-1-v1.html` | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` | **yes** |
| `monthly-1-v1.pdf` | `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` | **yes** (`%PDF`) |
| `monthly-1-v2.html` | `27a6eee6f6729f5a081865a24aa1e4ca1f94554ff38d4a1278682f16f95f6ffe` | **yes** |
| `monthly-1-v2.pdf` | `a8c4d61c6216e8d70b193115faeab345c0c61ed25ee97a96b740f5f041a56b6b` | **yes** (`%PDF`) |

No new artifacts. Storage remains under runtime `storage/exports/reports/` — outside `public/` and outside Git.

---

## 7. HTTP / Regression

Temporary PHP built-in server `127.0.0.1:8092` (docroot `public/`). Session inject for local admin (no password printed).

| Check | Result |
|-------|--------|
| `GET /health` | **200** |
| auth `GET /report-snapshots/1/exports` | **200** |
| auth `GET /report-exports/{1..4}` | **200** each |
| auth downloads 1–4 | **200** (HTML/PDF Content-Type) |
| `GET /share` | **404** |
| Summary | **12/12 PASS** |

No public share route. No app code changed this wave; smoke confirms existing routes still work after schema/backfill.

---

## 8. Restrictions

- no production / remote DB
- no real client data beyond existing `LOCAL_FIXTURE_ONLY` fixture exports
- no app code / auth / health / fixture tool edits
- no schema beyond DB-09 migration file
- no DELETE/DROP/TRUNCATE
- no new export rows; no artifact regeneration/overwrite
- no public share / token / public webroot writes
- no package install/download
- no secrets / credentials / password / hash / session in Git or reports
- no `.env` / source `.env.local`; runtime `.env.local` untouched and uncommitted

---

## 9. What Still Does Not Exist

- UI reads durable DB metadata (still may infer from key/content)
- repository/service writes metadata for future exports
- DB-backed template registry (`report_templates`)
- client branding DB assignment
- public share / client portal
- production deployment

---

## 10. Next Phase

**I-SEO Report Hub — Report Export Template Metadata UI Implementation 01**

---

## 11. SAFE UNKNOWN

- Whether Laragon Apache on port 80 was listening during this wave (smoke used temporary PHP `-S` on **8092**, consistent with prior waves).
- Exact operator retention policy for temp scripts under `X:\AI MARS STORAGE\incoming\iseo-report-hub\db09-metadata-apply-01\` (not in Git).
