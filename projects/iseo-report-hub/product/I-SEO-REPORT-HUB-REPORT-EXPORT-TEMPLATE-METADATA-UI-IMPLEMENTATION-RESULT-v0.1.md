# I-SEO Report Hub — Report Export Template Metadata UI Implementation Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export Template Metadata UI Implementation 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-APPLY-RESULT-v0.1.md)
- [REPORT-iseo-report-hub-report-export-template-metadata-ui-implementation-01.md](../reports/REPORT-iseo-report-hub-report-export-template-metadata-ui-implementation-01.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Status | **complete** |
| DB metadata read | **yes** |
| UI metadata display | **yes** |
| Future export metadata write support | **yes** (styled HTML/PDF create paths; not invoked this wave) |
| DB unchanged | **yes** |
| Artifacts unchanged | **yes** |
| Smoke result | **27/27 PASS** (read-only HTTP) |

---

## 2. Source Changes

| Path | Change |
|------|--------|
| `app-source/app/Support/ReportTemplate.php` | `ID`/`VERSION` aliases; PDF render target + engine constants |
| `app-source/app/Services/ReportTemplateService.php` | Legacy label → `not recorded / legacy` |
| `app-source/app/Repositories/ReportExportRepository.php` | SELECT join source HTML; insert DB-09 columns; `findByIdWithSourceHtml` |
| `app-source/app/Services/ReportExportService.php` | DB-first label helpers; enrich display; styled create writes metadata |
| `app-source/app/Controllers/ReportExportController.php` | Pass render/source/legacy flags to detail view |
| `app-source/app/Controllers/ReportSnapshotController.php` | Enrich export cards with display metadata |
| `app-source/app/Views/pages/report-exports/index.php` | Template / render / source HTML columns |
| `app-source/app/Views/pages/report-exports/show.php` | Template, render target/engine, source HTML |
| `app-source/app/Views/pages/report-snapshots/show.php` | DB-first labels + PDF lineage |
| `app-source/app/Views/pages/monthly-reports/show.php` | Metadata note |
| `app-source/public/assets/css/app.css` | Legacy badge / source lineage / muted meta |
| `app-source/README.md` | DB-09 UI status + next stage |

No migration / tools / auth / health edits.

---

## 3. Runtime Sync

Exact-path copy of allowlisted changed files to:

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`

`.env.local` **untouched**. No broad sync. No artifact sync.

---

## 4. Metadata Read Model

| Field | Handling |
|-------|----------|
| `template_id`, `template_version` | Primary for template label |
| `render_target`, `render_engine` | Mapped to human labels |
| `source_html_export_id` | Lineage for PDF; join/`findById` fallback |
| `render_options_json`, `metadata_json` | Stored/written as safe JSON; not shown raw in default UI |
| Fallback | NULL → `not recorded / legacy` / `not recorded`; never invent `iseo_default_v1` for v1 |

---

## 5. Metadata Display

| Surface | Behavior |
|---------|----------|
| Export list | Template + render + source HTML columns |
| Export detail | Full template/render/source facts |
| Snapshot cards | Latest styled/legacy labels from DB |
| Monthly page | Note that labels prefer DB-09 |

### ids 1–4 display matrix

| id | key | Template | Render target | Render engine | Source HTML |
|----|-----|----------|---------------|---------------|-------------|
| 1 | `snapshot-1-html-v1` | not recorded / legacy | not recorded | not recorded | — |
| 2 | `snapshot-1-pdf-v1` | not recorded / legacy | not recorded | not recorded | not recorded |
| 3 | `snapshot-1-html-v2` | `iseo_default_v1 v1` | HTML export | PHP template renderer | — |
| 4 | `snapshot-1-pdf-v2` | `iseo_default_v1 v1` | PDF export | Edge headless PDF | `#3 snapshot-1-html-v2` |

---

## 6. Future Write Support

| Path | Fields written |
|------|----------------|
| Styled HTML create | `template_id=iseo_default_v1`, `template_version=1`, `render_target=html_export`, `render_engine=php_template_renderer`, safe JSON options/metadata |
| Styled PDF create | same template + `render_target=pdf_export`, `render_engine=edge_headless_pdf`, `source_html_export_id` = source HTML id |
| Legacy HTML/PDF create | metadata columns remain NULL (no inventing styled identity) |
| This wave | **create flow not invoked** |

---

## 7. DB / Artifact Validation

| Check | Before | After |
|-------|--------|-------|
| schema_migrations | 8 | 8 |
| tables | 15 | 15 |
| report_exports | 4 | 4 |
| html / pdf | 2 / 2 | 2 / 2 |
| snapshots / monthly / blocks / periods / weekly | 1 / 1 / 6 / 2 / 4 | unchanged |
| id 1–2 metadata | NULL | NULL |
| id 3–4 metadata | filled | filled unchanged |
| Artifact checksums | expected SHA-256 | MATCH unchanged |

No DELETE/DROP/TRUNCATE. No new export rows.

---

## 8. HTTP Smoke

Temporary PHP built-in `127.0.0.1:8092`, docroot runtime `public/`.

| Assertion | Result |
|-----------|--------|
| `/health` 200 | PASS |
| `/login` expected | PASS |
| `/not-existing` 404 | PASS |
| auth exports list — 4 keys + legacy + styled + source `#3` | PASS |
| details 1–4 labels | PASS |
| downloads 1–4; PDF magic `%PDF` | PASS |
| snapshot + monthly GET | PASS |
| `/share` 404 | PASS |
| **Total** | **27/27 PASS** |

No create POST. No cookies/passwords printed.

---

## 9. Restrictions

- no DB mutation; no schema edits; no new export rows; no artifact writes
- no package install; no secrets in Git/report
- no public/share; no `.env.local` commit
- no auth/health/fixture tool edits

---

## 10. What Still Does Not Exist

- DB-backed template registry
- client branding DB
- public share / client portal
- repair / regeneration UI
- production deployment

---

## 11. Next Phase

**Report Delivery / Public Share Charter 01**

---

## 12. SAFE UNKNOWN

- Whether Laragon Apache was listening on port 80 during this smoke (PHP `-S` used intentionally).
- Exact operator schedule for Public Share charter.
