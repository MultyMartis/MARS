# I-SEO Report Hub — Report Styling Export Version Apply Result v0.1

## 1. Status

- **complete**
- styled HTML v2 created: **yes** (export id **3**)
- styled PDF v2 created: **yes** (export id **4**)
- template id/version: `iseo_default_v1` / **1**
- idempotency: **yes** (repeat create returns same ids; checksums stable; `report_exports` stays **4**)
- old artifacts unchanged: **yes**
- final DB state: migrations **7**; tables **15**; `report_exports` **4** (html **2**, pdf **2**)
- no public/share: **yes**
- no package install: **yes**

## 2. Source Changes

- `projects/iseo-report-hub/app-source/app/routes.php`
- `projects/iseo-report-hub/app-source/app/Controllers/ReportExportController.php`
- `projects/iseo-report-hub/app-source/app/Controllers/ReportSnapshotController.php`
- `projects/iseo-report-hub/app-source/app/Services/ReportExportService.php`
- `projects/iseo-report-hub/app-source/app/Repositories/ReportExportRepository.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/report-exports/index.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/report-exports/show.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/report-snapshots/show.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/monthly-reports/show.php`
- `projects/iseo-report-hub/app-source/public/assets/css/app.css`
- `projects/iseo-report-hub/app-source/README.md`

Unchanged (already sufficient): `ReportTemplateService.php`, `ReportTemplate.php`, `ReportTemplateRenderer.php`, `bootstrap.php`, `app.js`.

## 3. Runtime Changes

Exact allowlist sync to `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`:

- mirrors of the source files listed above (except Active Brain docs)

`.env.local` untouched.

## 4. Export Versioning

- v1 historical: `snapshot-1-html-v1` / `snapshot-1-pdf-v1` (ids 1/2) preserved
- v2 styled: `snapshot-1-html-v2` / `snapshot-1-pdf-v2` (ids 3/4)
- version rule: next = max existing version for snapshot+format + 1; styled create returns existing ready v≥2 (no v3)
- idempotency: service + HTTP POST re-check return ids 3/4
- no v3 produced

## 5. Styled HTML v2

- export id: **3**
- key: `snapshot-1-html-v2`
- relative path: `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v2.html`
- absolute path: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v2.html`
- file size: **8562**
- checksum: `27a6eee6f6729f5a081865a24aa1e4ca1f94554ff38d4a1278682f16f95f6ffe`
- template metadata (in HTML / UI inference): `iseo_default_v1` v1
- validation: contains template id, snapshot key `monthly-1-v1`, period `2026-07`, embedded CSS, `@page`; no `<script`; no external asset tags; fixture text may include `https://demo.example.test` (content, not CDN asset)

## 6. Styled PDF v2

- export id: **4**
- key: `snapshot-1-pdf-v2`
- relative path: `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v2.pdf`
- absolute path: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v2.pdf`
- file size: **117055**
- checksum: `a8c4d61c6216e8d70b193115faeab345c0c61ed25ee97a96b740f5f041a56b6b`
- `%PDF` magic: **yes**
- engine: Edge headless (`msedge.exe` **150.0.4078.99**)
- source HTML v2 export id: **3**

## 7. DB State

| Metric | Before | After |
|--------|--------|-------|
| schema_migrations | 7 | 7 |
| tables | 15 | 15 |
| report_exports | 2 | 4 |
| html rows | 1 | 2 |
| pdf rows | 1 | 2 |
| report_snapshots | 1 | 1 |
| monthly_report_contents | 1 | 1 |
| report_blocks | 6 | 6 |
| reporting_periods | 2 | 2 |
| weekly_checkpoints | 4 | 4 |

- rows inserted: id **3** HTML v2, id **4** PDF v2
- v1 rows id 1/2 unchanged (keys, sizes, checksums)
- snapshot/monthly/blocks unchanged
- audit: `report_export.html_created` (3), `report_export.pdf_created` (4), `report_export.html_idempotent_hit` / `report_export.pdf_idempotent_hit`

## 8. Artifact State

- v1 HTML/PDF unchanged (checksums match baseline)
- v2 HTML/PDF created under runtime export storage only
- outside `public/` and outside Git tree
- no unexpected duplicate v3 files

## 9. UI / Export Integration

- export list shows four rows with template labels (v1 legacy / v2 `iseo_default_v1 v1`)
- export detail distinguishes Historical v1 vs Styled export
- snapshot card prefers latest styled HTML/PDF when present; link to all versions
- monthly page notes styled default available as separate version
- no public link; no destructive controls

## 10. Smoke Tests

- PHP lint: **0** errors on changed PHP/views
- service create + idempotency + FS/DB checks: **33/34** core assertions (CDN URL assertion refined — fixture URL only; **no** external asset refs)
- HTTP / regression via temporary `127.0.0.1:8091`: **55/55 PASS**
- downloads 1–4 auth 200; PDF magic for 2 and 4

## 11. Restrictions

- no production / remote DB
- no real client data beyond LOCAL_FIXTURE_ONLY
- no schema edits / db-migrate
- no DELETE/DROP/TRUNCATE
- no public share / public webroot writes
- no package install/download
- no secrets in Git/report

## 12. What Still Does Not Exist

- DB-backed template registry
- durable template metadata columns
- client branding DB / logo upload
- public share / client portal
- repair/regeneration UI
- production deployment

## 13. Next Phase

**Report Styling Visual QA 01**

## 14. SAFE UNKNOWN

- Laragon Apache on port 80 was not listening during this wave; HTTP smoke used temporary PHP built-in on `127.0.0.1:8091` (same pattern as prior i-SEO export waves). Domain `iseo-report-hub.test` resolves to 127.0.0.1 but was not used as the smoke base URL in this run.
