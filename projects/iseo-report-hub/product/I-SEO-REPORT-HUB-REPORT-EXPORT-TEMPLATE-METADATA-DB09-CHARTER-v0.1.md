# I-SEO Report Hub — Report Export Template Metadata DB-09 Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation; no SQL/migration file; no artifact regeneration  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export Template Metadata DB-09 Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-STYLING-VISUAL-QA-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-VISUAL-QA-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-STYLING-EXPORT-VERSION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-EXPORT-VERSION-APPLY-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-STYLING-DEFAULT-TEMPLATE-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-DEFAULT-TEMPLATE-IMPLEMENTATION-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-DB-08-REPORT-EXPORTS-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-DB-08-REPORT-EXPORTS-MIGRATION-APPLY-RESULT-v0.1.md)

---

## 1. Purpose

Зафиксировать **docs/policy слой DB-09** для durable template / render metadata на export rows.

Цель charter:

1. Спроектировать DB-09 migration charter для durable template/render metadata in `report_exports` / export rendering metadata.
2. Сравнить варианты (columns / sidecar / registry / combined) и выбрать MVP.
3. Зафиксировать compatibility / backfill policy для существующих rows 1–4.
4. Зафиксировать `source_html_export_id` policy для PDF rows.
5. Зафиксировать migration / implementation / validation plans для следующей волны.
6. Не менять app-source / runtime / DB / artifacts в этой волне.

Эта волна — **documentation / policy only**. Migration SQL, schema apply, backfill и UI **не** выполняются здесь.

---

## 2. Current Baseline

### Report Styling Visual QA 01

| Item | Value |
|------|-------|
| Primary | `1d1d3c0d4af462698dc8fef84c03d3d1673bdcab` |
| Hash-record | `cc488020818a88316f6f3bbf32650661aaa976a7` |
| Tip HEAD (at charter start) | `00982547c434c9c497716a69a1031a277bc8d030` |
| Verdict | **PASS_WITH_MINOR_ISSUES** |
| Push | **no** |
| Styled HTML/PDF v2 | visually accepted for MVP |
| DB / artifacts | **unchanged** during QA |

### Report Styling Export Version Apply 01

| Item | Value |
|------|-------|
| Primary | `31ff2a734c894ab50ba3532e3b96b68391b002ae` |
| Hash-record | `c7ce6b8649c364102cb32b8d8fc2f5240bf1a527` |
| Status | **COMPLETE** |
| `report_exports` | **4** total (html **2**, pdf **2**) |
| Schema change | **none** |

### Export rows (ids 1–4)

| id | key | format | role | template knowledge today |
|----|-----|--------|------|--------------------------|
| 1 | `snapshot-1-html-v1` | html | historical v1 | not recorded (key/content inference only) |
| 2 | `snapshot-1-pdf-v1` | pdf | historical v1 | not recorded; source HTML lineage not durable |
| 3 | `snapshot-1-html-v2` | html | styled v2 | `iseo_default_v1` v1 in artifact content / UI inference |
| 4 | `snapshot-1-pdf-v2` | pdf | styled v2 | same template by process evidence; source HTML export id **3** by process, not DB FK |

### Styled artifacts (runtime storage; not Git)

| Artifact | size | checksum (sha256) |
|----------|------|-------------------|
| `monthly-1-v2.html` | 8562 | `27a6eee6f6729f5a081865a24aa1e4ca1f94554ff38d4a1278682f16f95f6ffe` |
| `monthly-1-v2.pdf` | 117055 | `a8c4d61c6216e8d70b193115faeab345c0c61ed25ee97a96b740f5f041a56b6b` |

### Report Styling Default Template Implementation 01

| Item | Value |
|------|-------|
| Primary | `4ad0f5818780b67a02a62b9c03e8d867c4ce4aba` |
| Hash-record | `8ed05c77d3e8775cddd866220f54c7ad676c4550` |
| Template | `iseo_default_v1` version **1** |
| Dry-render | **17/17 PASS** |

### DB baseline (read-only check this charter)

| Metric | Value |
|--------|-------|
| Target | `iseo_report_hub_dev` @ `127.0.0.1` |
| schema_migrations | **7** |
| tables | **15** |
| report_exports | **4** (html **2**, pdf **2**) |
| report_snapshots | **1** |
| monthly_report_contents | **1** |
| report_blocks | **6** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |

### Current limitation

- template metadata exists in rendered v2 artifact content and UI inference only;
- DB `report_exports` has **no** durable columns for `template_id`, `template_version`, `render_target`, `render_engine`, `render_options_json`, `source_html_export_id`, parent/export lineage;
- v1/v2 labels are inferred from key/content/code conventions;
- future delivery / share / client portal must not rely on filename inference.

---

## 3. Problem

DB cannot currently answer, without inference:

- which template generated this export;
- which template version;
- which render target / engine / options;
- which HTML export was used to generate a PDF export;
- which exports are legacy / unrecorded;
- how UI can show template state without filename/content inference.

Without DB-09, delivery/share workflows and future multi-template work will keep fragile conventions.

---

## 4. Scope

### In scope

- DB-09 design;
- columns / sidecar / registry comparison;
- recommended MVP decision;
- migration / backfill plan (policy only);
- validation plan (policy only);
- OPERATIONAL-INDEX update;
- closeout REPORT.

### Out of scope (this charter)

- DB mutation;
- migration SQL creation/edit;
- schema file creation;
- app-source changes;
- runtime changes;
- artifact changes / regeneration;
- report_exports / snapshots / blocks / monthly / weekly / period row changes;
- backfill execution;
- public delivery / share / client portal;
- production deployment.

---

## 5. Recommended Decision

**Option A — add nullable columns to `report_exports`.**

MVP:

- nullable render metadata columns on `report_exports`;
- defer `report_templates` registry;
- defer client branding assignment;
- defer forced backfill repair UI;
- exact controlled backfill plan for ids **3–4** only (executed in Migration Apply wave, not here);
- legacy v1 rows **1–2** remain `template_id` / `template_version` **NULL** (not recorded) — do **not** invent `iseo_default_v1` for v1;
- PDF id **4** planned `source_html_export_id = 3`; PDF id **2** remains NULL.

See Design doc for columns, indexes, FK, and backfill matrix.

---

## 6. Safety Boundary

- Local DB target only: `iseo_report_hub_dev` @ `127.0.0.1`.
- No production DB.
- No silent overwrite of historical v1 artifacts or rows.
- No absolute Windows paths / credentials in `render_options_json`.
- Foreign WIP preserved; exact-path docs commits only.
- This charter does **not** apply migration, backfill, or UI.

---

## 7. Next Wave

Recommended next action (one only):

**I-SEO Report Hub — Report Export Template Metadata DB-09 Migration Apply 01**

Then (separate, recommended):

**I-SEO Report Hub — Report Export Template Metadata UI Implementation 01**

Alternative: combine migration + repository/UI only if operator explicitly approves. Default = **split migration first**.
