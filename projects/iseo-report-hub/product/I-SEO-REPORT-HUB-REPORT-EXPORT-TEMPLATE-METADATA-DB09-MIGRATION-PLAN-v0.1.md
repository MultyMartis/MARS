# I-SEO Report Hub — Report Export Template Metadata DB-09 Migration Plan v0.1

**Status:** PLAN ONLY — no migration file created; no DB apply; no backfill executed  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export Template Metadata DB-09 Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md)

---

## 1. Recommended next wave

**I-SEO Report Hub — Report Export Template Metadata DB-09 Migration Apply 01**

Scope of that wave (not this charter):

1. Add migration SQL under `app-source/database/migrations/`.
2. Sync migration file to Localhost runtime (Model A source → runtime).
3. Apply to local DB `iseo_report_hub_dev` @ `127.0.0.1` only.
4. Optionally execute controlled backfill for rows **3–4** only.
5. Minimal repository read support only if required for compatibility — **no** full UI rewrite in Apply wave (UI = separate wave).
6. No new exports / artifacts / public routes.

Then:

**I-SEO Report Hub — Report Export Template Metadata UI Implementation 01**

---

## 2. Preflight (Apply wave)

Before any write/apply:

| Check | Expected |
|-------|----------|
| Repo root | `X:\AI MARS` |
| Volume | `X:` label `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| DB host / name | `127.0.0.1` / `iseo_report_hub_dev` |
| schema_migrations | **7** (before apply) |
| tables | **15** |
| report_exports | **4** |
| html / pdf rows | **2** / **2** |
| export ids | **1–4** present with known keys/checksums |
| Artifacts | v1/v2 HTML/PDF exist; checksums match baseline |
| i-SEO WIP | clean or charter-allowlisted only |
| Foreign WIP | preserved |
| Staged index | no unexpected `projects/iseo-report-hub/` paths |

STOP if target/host mismatch, wrong counts, missing rows 1–4, or foreign i-SEO staged conflict.

---

## 3. Expected migration filename

Suggested:

`projects/iseo-report-hub/app-source/database/migrations/2026_07_27_000008_add_template_metadata_to_report_exports_table.sql`

**Apply prompt must verify** exact next sequence against existing migration list (currently `000001`…`000007`). If date/order differs, rename to next free batch number — do not invent out-of-order files.

Ledger: `tools/db-migrate.php` inserts `schema_migrations` after successful apply (same pattern as DB-08).

---

## 4. Schema changes (conceptual)

`ALTER TABLE report_exports` add nullable columns:

- `template_id` VARCHAR(100) NULL
- `template_version` VARCHAR(50) NULL
- `render_target` VARCHAR(50) NULL
- `render_engine` VARCHAR(100) NULL
- `render_options_json` JSON NULL
- `source_html_export_id` BIGINT UNSIGNED NULL
- `metadata_json` JSON NULL

Indexes:

- `idx_report_exports_template` (`template_id`, `template_version`)
- `idx_report_exports_source_html` (`source_html_export_id`)

FK:

- `fk_report_exports_source_html` → `report_exports(id)` **ON DELETE SET NULL**

No new tables in DB-09. No DROP. No rewrite of existing non-null columns. No CHECK on template_id.

Expected after apply:

| Metric | After |
|--------|-------|
| schema_migrations | **8** |
| tables | **15** (unchanged count) |
| report_exports row count | **4** (unchanged) |

---

## 5. Controlled backfill plan

Optional but **recommended** for local fixture evidence in Apply wave.

### Gates (all required)

1. `id = 3` AND `export_key = 'snapshot-1-html-v2'` AND checksum matches `27a6eee6…f95f6ffe`
2. `id = 4` AND `export_key = 'snapshot-1-pdf-v2'` AND checksum matches `a8c4d61c…41a56b6b`
3. `id = 1` / `2` **must not** receive `iseo_default_v1`

### Planned updates

| id | Updates |
|----|---------|
| 3 | `template_id='iseo_default_v1'`, `template_version='1'`, `render_target='html_export'`, `render_engine='php_template_renderer'`, `source_html_export_id=NULL` |
| 4 | `template_id='iseo_default_v1'`, `template_version='1'`, `render_target='pdf_export'`, `render_engine='edge_headless_pdf'`, `source_html_export_id=3` |
| 1–2 | leave template fields NULL (no invent) |

Idempotency: UPDATE … WHERE id/key/checksum gates; re-apply leaves same values.

**Not executed in this charter.**

---

## 6. No v1 overwrite / no artifact mutation

Apply wave MUST:

- not change storage_path / filename / size / checksum for any row;
- not regenerate HTML/PDF files;
- not create export ids 5+;
- not mutate report_snapshots / monthly / blocks / periods / weekly;
- not touch `.env` / admin passwords;
- not enable public/share routes.

---

## 7. Sync / apply plan

1. Author migration SQL in `app-source` only (Model A SoT).
2. Exact-path sync migration file → runtime `database/migrations/`.
3. Run existing migrate tool against `iseo_report_hub_dev` only.
4. Verify ledger batch / checksum_ok.
5. Run controlled backfill SQL (if operator includes it) with exact gates.
6. Run validation plan checks.
7. Docs result + REPORT; scoped commit; **no push** unless operator asks.

---

## 8. Rollback / failure boundaries

| Failure | Response |
|---------|----------|
| Preflight count mismatch | STOP; no ALTER |
| Migration apply fails mid-way | STOP; do not invent manual DROP without charter; capture error; operator decides restore |
| Backfill gate miss | STOP backfill; leave NULLs; report |
| Artifact checksum drift | STOP; do not “fix” by regenerating |
| Wrong DB host/name | STOP immediately |

Preferred rollback for unused new columns: reverse migration charter (DROP columns) only with explicit destructive/schema charter — not ad-hoc.

---

## 9. STOP conditions (Apply wave)

STOP if:

- not `iseo_report_hub_dev` @ `127.0.0.1`;
- migrations ≠ 7 before apply;
- report_exports ≠ 4 or ids 1–4 missing;
- i-SEO foreign staged conflict;
- attempt to backfill v1 as `iseo_default_v1`;
- attempt to mutate artifacts;
- production / remote DB target.

Token:

`STOP — I-SEO REPORT HUB REPORT EXPORT TEMPLATE METADATA DB-09 MIGRATION APPLY SAFETY CONDITION FAILED`
