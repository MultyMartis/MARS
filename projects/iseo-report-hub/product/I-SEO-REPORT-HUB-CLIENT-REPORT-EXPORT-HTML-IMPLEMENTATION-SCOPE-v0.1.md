# I-SEO Report Hub — Client Report Export HTML Implementation Scope v0.1

**Status:** CHARTER / SCOPE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-20  
**Wave:** Client Report Export HTML Alignment Charter 01

Next implementation name:

**`I-SEO Report Hub — Client Report Export HTML Alignment Implementation 01`**

---

## 1. Goal

Prove that **client report document style HTML** can be generated from **snapshot payload** (same data contract family as exports) **without**:

- creating export rows;
- writing under `storage/exports/reports/`;
- regenerating PDF;
- mutating DB content / shares;
- changing public share behavior;
- overwriting export **4**.

---

## 2. In scope

| Item | Detail |
|------|--------|
| Snapshot→DTO adapter | Extend `ClientReportDocument` (e.g. `fromSnapshotPayload`) or add thin mapper that maps snapshot payload → same DTO as `fromAssemble` |
| Export-safe HTML renderer | New support/service that renders document layout/partial **as a full HTML string** with **embedded** `client-report.css` |
| Reuse | `ClientReportDocument`, `partials/client-report/document.php` (via View partial or equivalent), visual IA/CSS |
| Non-mutating smoke | Service method and/or CLI tool that dry-renders HTML |
| Evidence | Write HTML evidence **only** under Storage (see §5) |
| Docs | Implementation result + closeout report + OPERATIONAL-INDEX |

---

## 3. Out of scope

- `POST` HTML/PDF/styled create routes invocation for product exports;
- new `report_exports` row;
- any write under runtime/app `storage/exports/`;
- PDF Edge/Chrome run (belongs to PDF Regeneration Proof 01);
- share create/revoke/cutover;
- public HTML share view;
- mutating `ReportTemplateRenderer` behavior for existing create paths;
- changing `/report-exports/4` UI beyond incidental zero-touch;
- metrics / fake KPI;
- production / WordPress / package installs;
- runtime sync **unless** implementation charter explicitly allowlists exact source→runtime files for the new renderer/tool only.

---

## 4. Recommended shape

### A. Service method (required)

Example conceptual API (names flexible):

- `ClientReportHtmlRenderer::renderFromSnapshot(array $snapshot, array $payload, array $options): string`
- Options: `embed_css=true`, `local_demo=false` for export-safe mode, `strip_markers=true`

May be wrapped by `ReportExportService::dryRenderClientHtmlForSnapshot(int $snapshotId)` that **reads** snapshot only and returns HTML — **no file/DB write**.

### B. CLI / tools script (optional but useful)

`tools/render-client-report-html-preview.php` (or under `projects/iseo-report-hub/tools/`):

- local-dev guarded;
- reads snapshot id (default active snapshot for monthly 1);
- writes evidence to Storage path below;
- refuses to write under `storage/exports/`;
- prints **no** share tokens / secrets.

If tool adds operational risk or bootstrap complexity, **service method + one-off agent script under Storage incoming is enough** — prefer simplest non-mutating proof.

### C. Routes

**No new public/internal HTML export route required** for Impl 01.  
Do **not** use `/preview/print` as the product export HTML source.

---

## 5. Evidence strategy

Allowed evidence root:

`X:\AI MARS STORAGE\incoming\iseo-report-hub\client-report-export-html-alignment-implementation-01\`

Rules:

- evidence HTML is **not** a product export;
- not registered in `report_exports`;
- not shareable via `/share/report/{token}`;
- not committed to git;
- may include a short `RECEIPT.md` (status codes, checksum of evidence file, “DB unchanged” checklist) — **no tokens**.

---

## 6. Acceptance pointer

See `I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-ACCEPTANCE-v0.1.md`.

---

## 7. Follow-on (explicitly later)

1. PDF Regeneration Proof 01 — new export id from client HTML; never overwrite 4.  
2. Share Handoff Update 01 — only after operator accepts new PDF.  
3. Optionally wire styled create paths to client renderer for **new** versions only.
