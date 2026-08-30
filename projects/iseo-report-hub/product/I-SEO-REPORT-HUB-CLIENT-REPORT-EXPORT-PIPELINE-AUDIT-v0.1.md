# I-SEO Report Hub — Client Report Export Pipeline Audit v0.1

**Status:** CHARTER / AUDIT — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-20  
**Wave:** Client Report Export HTML Alignment Charter 01

No app-source / runtime / DB / artifact mutation in this wave.

---

## 1. HTML export generation

| Step | Current reality |
|------|-----------------|
| Entry (HTTP) | `ReportExportController` POST create HTML / styled HTML for snapshot |
| Service | `ReportExportService::createHtmlForSnapshot` / `createStyledHtmlVersionForSnapshot` |
| Dry-render (non-writing) | `ReportExportService::dryRenderHtmlForSnapshot` → same HTML builder |
| Renderer | `Iseo\Support\ReportTemplateRenderer::render` |
| Template identity | Code-first `iseo_default_v1` via `ReportTemplate` / `ReportTemplateService` |
| Views | **None** — HTML is string-built in PHP (not Blade/partial) |
| CSS | **Embedded** `<style>` from `ReportTemplateRenderer::embeddedCss($tokens)` |
| Data source | **Snapshot only** — `report_snapshots.payload_json` decoded; **not** live `report_blocks` |
| Content shape | Internal export document: period/client/project/site meta, weekly sources, flat fields, blocks with `block_key` / type / sort, checksum diagnostics |
| Client preview alignment | **Not aligned** — preview uses `ClientReportDocument` + layout/partial; export still uses legacy internal HTML |

Key wiring (`app/routes.php`): `ReportTemplateRenderer` injected into `ReportExportService`.

---

## 2. PDF generation

| Step | Current reality |
|------|-----------------|
| Entry | `ReportExportService::createPdfForSnapshot` / `createStyledPdfVersionForSnapshot` |
| Source HTML | **Existing ready HTML export artifact on disk** (validated), not live preview |
| Engine | Microsoft Edge headless preferred; Chrome fallback (`--print-to-pdf=…`, `file://` URL) |
| Separate PDF template | **No** — PDF is print of the HTML file |
| CSS | Whatever is **inside** the HTML artifact (embedded today) |
| Temp profiles | Under Storage incoming temp roots (not public webroot) |
| Dedicated `ReportPdfService` | **Does not exist** in app-source |

Implication: future client-styled PDF **requires** a client-styled HTML artifact first (or an explicit alternate HTML source). Linked CSS that depends on HTTP `/assets/…` is unsafe for `file://` browser print.

---

## 3. Export file storage

| Concern | Current reality |
|---------|-----------------|
| Relative root | `storage/exports/reports/` (outside `public/`) |
| Path pattern | `storage/exports/reports/monthly-{monthlyId}/snapshot-{snapshotId}/monthly-{monthlyId}-v{N}.{html\|pdf}` |
| DB table | `report_exports` (+ DB-09 template metadata columns on styled rows) |
| Checksum | `checksum_sha256` of file; also `source_snapshot_checksum_sha256` |
| Status | `ready` for downloadable artifacts |
| Semantics | Treat as **immutable once ready** — create new version / new id; do not rewrite bytes of issued rows |
| Known frozen | Export **4** PDF v2 — checksum prefix `a8c4d61c6216e8d70b19`, size `117055` |

Idempotency: ready export for same snapshot checksum (or styled version finder) returns existing row without rewrite when validation passes.

---

## 4. Route `/report-exports/{id}`

| Concern | Current reality |
|---------|-----------------|
| Controller | `ReportExportController::show` |
| Nature | **Internal authenticated metadata / handoff UI** |
| Renders artifact? | **No** — does not re-render HTML template |
| Download | Separate `GET /report-exports/{id}/download` streams validated file |
| Shares UI | `GET /report-exports/{id}/shares` via `ReportExportShareController` |

Changing preview CSS/views does **not** change this page’s file bytes. Changing renderer without creating a new export also does **not** change export **4**.

---

## 5. Public share

| Concern | Current reality |
|---------|-----------------|
| Route | `GET /share/report/{64-hex-token}` |
| Controller | `PublicReportShareController::download` |
| Behavior | Resolves token → validates eligible PDF export → streams **static PDF** as `Content-Disposition: attachment` |
| Dynamic HTML public view | **Does not exist** |
| Safety | Token must never be printed in docs/logs; 404/410 deny pages are generic |

Active share remains tied to the PDF file referenced by that share row (today: export **4** context). Preview/template changes cannot alter share bytes until a **new** PDF is issued **and** a new share cutover is approved.

---

## 6. Preview vs export (gap)

| Surface | Mapper / template | Data | CSS | Affects share? |
|---------|-------------------|------|-----|----------------|
| `/monthly-reports/{id}/preview` | `ClientReportDocument` + `layout-client-report` + document partial | Live assemble() | Linked `client-report.css` | No |
| `/preview/print` | Same | Live assemble() | Same (+ print CSS) | No |
| HTML export create | `ReportTemplateRenderer` | Snapshot payload | Embedded tokens CSS | Only after new artifact |
| Public share | N/A (file stream) | Issued PDF file | N/A | Current PDF only |

---

## 7. Audit conclusion

Export HTML/PDF pipeline is **snapshot → ReportTemplateRenderer HTML → disk → optional Edge PDF → DB row**. Client preview template is a **parallel** document system. Alignment charter next step must introduce an **export-safe client document render path** without mutating issued artifacts **1–4** or public share behavior.
