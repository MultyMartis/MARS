# I-SEO Report Hub — Report Export PDF Hardening Result v0.1

## 1. Status

- **complete**
- hardening implemented: **yes**
- no new PDF/export row: **yes** (PDF remains id **2**; `report_exports` count **2**)
- final DB state: `schema_migrations` **7**; tables **15**; `report_exports` **2** (html id 1 + pdf id 2); snapshot **1** active; monthly **1** finalized
- artifact unchanged: **yes** (PDF checksum `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320`; size **133005**; mtime unchanged on idempotent POST)
- no public/share: **yes**
- no package install: **yes**

## 2. Source Changes

- `app-source/app/Services/ReportExportService.php` — shared `validateReadyArtifact()`; absolute/traversal path rejection; MIME/format/extension/size/checksum/PDF-magic guards; download/idempotent/PDF-source paths use validator; safe MIME/filename helpers
- `app-source/app/Controllers/ReportExportController.php` — download uses safe MIME/filename; `nosniff` + `Cache-Control: private, no-store`
- `app-source/app/Views/pages/report-exports/index.php` — clearer HTML/PDF ready vs create vs re-check copy; no duplicate-create encouragement
- `app-source/app/Views/pages/report-exports/show.php` — validation hint for download
- `app-source/app/Views/pages/report-snapshots/show.php` — format/status badges; PDF ready note; re-check labels; Download HTML/PDF
- `app-source/public/assets/css/app.css` — ready-note / hint styles; PDF type badge outside table
- `app-source/README.md` — hardened export status; next stage styling charter

## 3. Runtime Changes

Exact sync (source → runtime):

- `app/Services/ReportExportService.php`
- `app/Controllers/ReportExportController.php`
- `app/Views/pages/report-exports/index.php`
- `app/Views/pages/report-exports/show.php`
- `app/Views/pages/report-snapshots/show.php`
- `public/assets/css/app.css`
- `README.md`

`.env.local` untouched. No broad sync. No artifact rewrite.

## 4. Validation Coverage

| Guard | Coverage |
|-------|----------|
| path validation | relative only; reject `..`, absolute/drive/UNC/`file:`; must stay under `storage/exports/reports`; reject public webroot |
| MIME validation | html → `text/html` (+ charset); pdf → `application/pdf`; unknown rejected |
| checksum validation | required; `hash_equals` vs file |
| size validation | DB `file_size_bytes` must match file size when > 0; empty rejected |
| PDF magic validation | `%PDF` on download + idempotent PDF + generation validation |
| idempotency validation | existing ready PDF validated then returned; audit `rewritten=false`; no file rewrite (mtime unchanged) |
| download validation | auth + ready + full artifact validation + safe headers; id-only route (path query ignored) |

## 5. Artifact State

- HTML relative: `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.html`
- HTML absolute (runtime only): `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.html`
- HTML size/checksum unchanged: **5360** / `c194c62b81c6…`
- PDF relative: `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf`
- PDF absolute (runtime only): `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.pdf`
- PDF size/checksum unchanged: **133005** / `707e72d65f253de1…`
- outside `public/`: **yes**
- not in Git: **yes**

## 6. DB State

| Metric | Before | After |
|--------|--------|-------|
| schema_migrations | 7 | 7 |
| tables | 15 | 15 |
| report_exports | 2 | 2 |
| html rows | 1 (id 1) | 1 (id 1) |
| pdf rows | 1 (id 2) | 1 (id 2) |
| report_snapshots | 1 | 1 |
| monthly_report_contents | 1 | 1 |
| report_blocks | 6 | 6 |
| reporting_periods | 2 | 2 |
| weekly_checkpoints | 4 | 4 |

Export rows unchanged. No business mutations. Optional audit: `report_export.pdf_idempotent_hit` on idempotent POST.

## 7. UI / UX

- export list: HTML + PDF formats, status ready, size, checksum short, download; PDF create only when HTML ready and no PDF; after PDF — ready note + re-check (idempotent)
- export detail: MIME/size/checksum; no public URL; validation hint
- snapshot cards: both exports with format/status; Download HTML/PDF; PDF ready note
- monthly: exports link retained; page 200
- duplicate create: not encouraged when PDF ready
- no public URL

## 8. Failure Modes

| Mode | Guarded behavior |
|------|------------------|
| missing file | validateReadyArtifact → user message; no absolute path leak |
| checksum mismatch | reject download / idempotent / PDF source |
| PDF magic invalid | reject PDF download / idempotent PDF |
| missing HTML source | PDF create fails with clear message |
| Edge missing | PDF create fails if Edge+Chrome absent (pre-existing) |
| traversal / absolute path / unknown format/MIME | rejected |
| client_viewer | list/view denied (role gate) |

Destructive simulation of real artifact delete was **not** performed; synthetic metadata mutations used in service smoke.

## 9. Smoke Tests

- PHP lint: PASS (changed PHP/views)
- Service validation suite: PASS (ready + rejection modes)
- HTTP smoke on `http://127.0.0.1:8091`: **67/67 PASS**
- Idempotent PDF POST → id **2**; checksum unchanged; mtime unchanged
- HTML/PDF download PASS; regression routes PASS
- no public/share routes (404)

## 10. Restrictions

- no production; no real client data; no schema edits; no DELETE/DROP/TRUNCATE
- no public share; no public webroot writes; no package install/download; no secrets in Git/docs

## 11. What Still Does Not Exist

- public share / client portal
- email delivery
- object storage
- export archive UI
- forced regeneration / repair UI
- multi-snapshot PDF batch
- production deployment

## 12. Next Phase

**Report Styling / Client Template Charter 01**

## 13. SAFE UNKNOWN

- Multi-role HTTP beyond `admin_owner` still deferred (same as prior PDF browser wave).
- Apache vhost listen state during this smoke: **SAFE UNKNOWN** (built-in PHP server used; not claimed as Apache proof).
