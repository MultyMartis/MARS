# I-SEO Report Hub — Report Export Template Metadata DB-09 Validation Plan v0.1

**Status:** PLAN ONLY — no apply; no validation execution against mutated schema in this charter  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export Template Metadata DB-09 Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md)

---

## 1. Baseline validation (before Apply)

Confirm read-only:

| Check | Expected |
|-------|----------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| schema_migrations | **7** |
| tables | **15** |
| report_exports | **4** |
| html / pdf | **2** / **2** |
| ids / keys | 1 `snapshot-1-html-v1`; 2 `snapshot-1-pdf-v1`; 3 `snapshot-1-html-v2`; 4 `snapshot-1-pdf-v2` |
| checksums | match Visual QA / Export Version Apply baseline |
| Artifacts on disk | v1/v2 HTML/PDF present; sizes/checksums match |
| No new columns yet | `template_id` etc. absent |

Charter wave may perform this baseline only (done for charter: DB + artifacts PASS).

---

## 2. Migration schema validation (after Apply)

| Check | Expected |
|-------|----------|
| schema_migrations | **8** |
| tables | **15** |
| New columns present | all seven nullable metadata columns |
| Indexes | `idx_report_exports_template`, `idx_report_exports_source_html` |
| FK | `source_html_export_id` → `report_exports(id)` ON DELETE SET NULL |
| Existing CHECKs | format/status unchanged |
| No dropped columns | yes |

---

## 3. Row count validation

| Check | Expected |
|-------|----------|
| report_exports | still **4** |
| html / pdf | still **2** / **2** |
| report_snapshots | **1** |
| monthly_report_contents | **1** |
| report_blocks | **6** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| No new export ids | max id still **4** |

---

## 4. Backfill validation

If backfill included:

| id | Assert |
|----|--------|
| 1 | `template_id` IS NULL; `template_version` IS NULL; `source_html_export_id` IS NULL |
| 2 | same NULL template/lineage |
| 3 | `template_id='iseo_default_v1'`; `template_version='1'`; `render_target='html_export'`; `render_engine='php_template_renderer'`; `source_html_export_id` IS NULL |
| 4 | `template_id='iseo_default_v1'`; `template_version='1'`; `render_target='pdf_export'`; `render_engine='edge_headless_pdf'`; `source_html_export_id=3` |

Also:

- storage_path / filename / file_size_bytes / checksum_sha256 unchanged for all four;
- idempotent re-backfill leaves same values;
- no row claims v1 = `iseo_default_v1`.

If backfill deferred: all new columns NULL for 1–4 is acceptable interim, documented in Apply result.

---

## 5. Artifact checksum validation

| File | size | sha256 |
|------|------|--------|
| `monthly-1-v1.html` | 5360 | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` |
| `monthly-1-v1.pdf` | 133005 | `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` |
| `monthly-1-v2.html` | 8562 | `27a6eee6f6729f5a081865a24aa1e4ca1f94554ff38d4a1278682f16f95f6ffe` |
| `monthly-1-v2.pdf` | 117055 | `a8c4d61c6216e8d70b193115faeab345c0c61ed25ee97a96b740f5f041a56b6b` |

FAIL if any artifact regenerated or checksum drifts during Apply.

---

## 6. UI / repository compatibility validation

After Apply (and before or during UI wave):

| Check | Expected |
|-------|----------|
| Export list/detail routes load | HTTP 200 for auth session (smoke) |
| No fatal SQL on missing column | repository SELECT includes new columns or uses compatible queries |
| UI without metadata | still shows legacy/fallback labels |
| UI with metadata (after UI wave) | prefers DB over filename inference |
| Create path (UI wave) | writes metadata for **new** exports |

DB-09 Apply wave: smoke that existing export pages still work is enough; full template-label rewrite can wait for UI Implementation 01.

---

## 7. No export mutation

Validate:

- no POST create of new HTML/PDF during Apply unless explicitly out of scope (default: **no create**);
- no overwrite of v1/v2 files;
- no public/share route enablement;
- no package install;
- no production deploy.

---

## 8. No public route

Confirm:

- no new public/token routes;
- downloads remain auth-gated;
- no client portal work in DB-09.

---

## 9. STOP conditions

STOP Apply / declare FAIL if:

- schema apply against wrong DB;
- row counts change unexpectedly;
- v1 backfilled as `iseo_default_v1`;
- artifact checksums change;
- new export rows appear without charter;
- public route introduced;
- credentials printed into docs.

Token:

`STOP — I-SEO REPORT HUB REPORT EXPORT TEMPLATE METADATA DB-09 VALIDATION FAILED`
