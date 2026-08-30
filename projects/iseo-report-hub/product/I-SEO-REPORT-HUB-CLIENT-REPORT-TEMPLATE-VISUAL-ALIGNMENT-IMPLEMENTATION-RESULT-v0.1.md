# I-SEO Report Hub — Client Report Template Visual Alignment Implementation Result v0.1

**Status:** IMPLEMENTED (preview document only; no DB / export / PDF write)  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Client Report Template Visual Alignment Implementation 01  
**Verdict:** `CLIENT REPORT PREVIEW TEMPLATE PASS`

Live internal preview `GET /monthly-reports/{id}/preview` now renders a dedicated client SEO-report document instead of the admin/debug preview shell. Export HTML/PDF, public share, and `ReportTemplateRenderer` are unchanged. Issued export **4** remains frozen.

---

## 1. Route result

| Surface | Result |
|---------|--------|
| `GET /monthly-reports/{id}/preview` | Client document layout; no admin sidebar |
| `GET /monthly-reports/{id}/preview/print` | Same document; print CSS |
| Assembly / export detail / shares | Unchanged |
| Public `/share/report/{token}` | Unchanged PDF stream of export **4** |

Routes were not added or renamed.

---

## 2. Client document

Option B: dedicated reusable template.

| Part | Path |
|------|------|
| Layout | `app-source/app/Views/layouts/layout-client-report.php` |
| Partial | `app-source/app/Views/partials/client-report/document.php` |
| Preview page | `app-source/app/Views/pages/report-preview/show.php` |
| CSS | `app-source/public/assets/css/client-report.css` |
| Mapper | `app-source/app/Support/ClientReportDocument.php` |
| Controller | `app-source/app/Controllers/ReportPreviewController.php` — preview-only DTO + client layout |

IA order: cover → Краткое резюме → Результаты → Что сделали → Ключевые выводы → Риски и блокеры → План на следующий месяц → footer.

Hidden from the document: admin chrome, edit/apply/source controls, ids/keys/checksums, weekly dumps, raw `LOCAL_FIXTURE_ONLY`, `Internal report export`.

Empty states are calm notes. No invented KPI.

Visual: paper on `#f5f6f8`, ink `#18181B`, accent `#facc15`, A4 `@page` / `@media print`. Operator back link is `.no-print`.

---

## 3. Safety

| Item | Changed |
|------|---------|
| DB | **no** |
| Report 1 / 5 | **no** |
| `report_blocks` / work entries | **no** |
| Exports / shares / PDF | **no** |
| Export 4 checksum prefix | `a8c4d61c6216e8d70b19` unchanged |
| Export 4 size | 117055 unchanged |
| `ReportTemplateRenderer` | **untouched** |

---

## 4. Validation

PHP lint OK. Authenticated GET smoke **61/61 PASS**. Preview assertions PASS (no admin chrome; six RU sections in IA order; print CSS present). DB counts unchanged.

---

## 5. Remaining debt

- Client Report Export HTML Alignment 01 (reuse this document in future HTML export; do not overwrite ids 3/4)
- Client Report PDF Regeneration Proof 01 (new export id)
- Metrics model for `results_summary`
- Screenshot QA of all pages when the operator sends shots

---

## 6. SAFE UNKNOWN

- Whether a later wave will add a public HTML share view (today share is PDF-only).
- Pixel match of issued PDF 4 against the new preview (expected mismatch until regeneration proof).
