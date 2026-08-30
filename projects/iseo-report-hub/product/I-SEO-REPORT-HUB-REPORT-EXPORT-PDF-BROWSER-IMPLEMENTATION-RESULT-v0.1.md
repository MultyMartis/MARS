# I-SEO Report Hub — Report Export PDF Browser Implementation Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Browser Implementation 01  
**Related:** PDF Engine Probe 01, HTML Artifact Implementation 01, DB-08 Apply

---

## 1. Status

| Field | Value |
|-------|-------|
| Outcome | **complete** |
| PDF service implemented | **yes** |
| PDF route implemented | **yes** — `POST /report-snapshots/{id}/exports/pdf` |
| PDF artifact created | **yes** |
| Metadata row created | **yes** — `report_exports.id=2` |
| Idempotency | **yes** — second create returns same id; checksum stable |
| Final DB state | migrations **7**; tables **15**; `report_exports` **2** (html **1** + pdf **1**) |
| No public/share | **yes** |
| No package install | **yes** |

---

## 2. Source Changes

- `app-source/app/routes.php`
- `app-source/app/Controllers/ReportExportController.php`
- `app-source/app/Controllers/ReportSnapshotController.php`
- `app-source/app/Services/ReportExportService.php`
- `app-source/app/Repositories/ReportExportRepository.php`
- `app-source/app/Views/pages/report-exports/index.php`
- `app-source/app/Views/pages/report-exports/show.php`
- `app-source/app/Views/pages/report-snapshots/show.php`
- `app-source/app/Views/pages/monthly-reports/show.php`
- `app-source/public/assets/css/app.css`
- `app-source/README.md`

Not changed: `bootstrap.php`, `app.js`, Auth/DB/CSRF/Health, migrations, tools.

---

## 3. Runtime Changes

Exact allowlist sync of the changed source files above to:

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`

`.env.local` untouched. No broad sync.

---

## 4. PDF Artifact

| Field | Value |
|-------|-------|
| Relative path | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf` |
| Absolute runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.pdf` |
| File size | **133005** bytes |
| Checksum SHA-256 | `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` |
| `%PDF` magic | **validated** |
| Outside public | **yes** |
| Not in Git | **yes** |

---

## 5. Engine

| Field | Value |
|-------|-------|
| Engine used | **Microsoft Edge** |
| Executable | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` |
| Version | **150.0.4078.99** |
| Flags summary | `--headless --disable-gpu --no-first-run --disable-extensions --disable-background-networking --disable-sync --no-default-browser-check --user-data-dir=… --print-to-pdf=… file:///…` |
| Temp profile root | `X:\AI MARS STORAGE\incoming\iseo-report-hub\pdf-browser-temp\` (per-run unique profile; cleaned after run) |
| Fallback used | **no** (Edge succeeded) |
| Input | Existing HTML artifact via `file://` URL (not live HTTP) |

---

## 6. Routes

| Method | Path | Notes |
|--------|------|-------|
| POST | `/report-snapshots/{id}/exports/pdf` | Create / idempotent return |
| GET | `/report-snapshots/{id}/exports` | Lists HTML + PDF |
| GET | `/report-exports/{id}` | Detail supports `format=pdf` |
| GET | `/report-exports/{id}/download` | Auth download; MIME `application/pdf` |

No public/token/share/DELETE/GET-mutation routes.

---

## 7. Export Rules

- **Source of truth for PDF:** existing ready HTML export artifact (not live `report_blocks` / monthly rows).
- **HTML source gate:** ready HTML row + file exists + checksum match + active snapshot + valid payload.
- **PDF generation:** Edge headless print-to-PDF; Chrome allowlisted fallback only if Edge fails.
- **Metadata:** insert `report_exports` with relative path, MIME, size, file checksum, source snapshot checksum.
- **Idempotency:** ready PDF for same snapshot checksum + matching file → return existing row.
- **Download policy:** auth-only attachment stream; no public webroot URL.

---

## 8. Access / Auth

- Auth required for create/view/download.
- Create roles: `admin_owner`, `seo_lead_reviewer`.
- View/download roles: admin_owner, seo_lead_reviewer, seo_specialist, account_client_manager, internal_viewer.
- `client_viewer`: no access.
- CSRF required on POST.
- Smoke used `admin_owner` session injection; multi-role HTTP deferred.

---

## 9. DB Actions

| Metric | Before | After |
|--------|--------|-------|
| schema_migrations | 7 | 7 |
| tables | 15 | 15 |
| report_exports | 1 | 2 |
| pdf report_exports | 0 | 1 |
| html report_exports | 1 | 1 (unchanged id **1**) |
| report_snapshots | 1 | 1 |
| monthly_report_contents | 1 | 1 |
| report_blocks | 6 | 6 |
| reporting_periods | 2 | 2 |
| weekly_checkpoints | 4 | 4 |

PDF row: id **2**, key `snapshot-1-pdf-v1`, format `pdf`, status `ready`.  
Audit: `report_export.pdf_created` (1), `report_export.pdf_idempotent_hit` (≥1).  
No snapshot/monthly/block/period/weekly mutation. No schema change.

---

## 10. UI / Export Integration

- Export index shows HTML + PDF rows; Create PDF when HTML ready and PDF missing.
- Export detail supports PDF MIME and Download PDF.
- Snapshot detail has PDF export card.
- Monthly report links to Exports.

---

## 11. Smoke Tests

- PHP lint on changed PHP/views: **PASS**
- Service create + idempotent: **PASS**
- HTTP unauth POST denied: **PASS**
- Auth list/detail/download PDF: **PASS**
- HTTP idempotent POST: **PASS**
- Snapshot PDF card: **PASS**
- No public/share routes: **PASS**
- Regression suite (health/login/periods/weekly/monthly/preview/snapshot/exports/blocks): **PASS**
- HTTP smoke summary: **39/39 PASS** (`127.0.0.1:8088`)

---

## 12. Restrictions

Confirmed: no production/remote DB; no real client data; no schema edits; no DELETE/DROP/TRUNCATE; no public share; no public webroot writes; no package/binary install; no Composer/npm; no secrets in Git/docs.

---

## 13. What Still Does Not Exist

- Public share / client portal
- Email delivery
- Object storage
- Export archive UI
- Forced regeneration flow
- Multi-snapshot PDF batch
- Production deployment

---

## 14. Next Phase

**Report Export PDF Hardening 01**

---

## 15. SAFE UNKNOWN

- Apache vhost (`iseo-report-hub.test:80`) not listening this session — HTTP smoke used PHP built-in `127.0.0.1:8088`.
- Multi-role HTTP smoke beyond `admin_owner` deferred.
- Exact Edge stderr noise on successful print (task_manager fallback messages) is environmental; PDF magic/size/checksum validated.
