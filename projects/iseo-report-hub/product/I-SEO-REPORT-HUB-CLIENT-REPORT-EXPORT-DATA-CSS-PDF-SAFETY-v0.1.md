# I-SEO Report Hub — Client Report Export Data / CSS / PDF Safety v0.1

**Status:** CHARTER / SAFETY — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-20  
**Wave:** Client Report Export HTML Alignment Charter 01

---

## 1. Reusing `ClientReportDocument`

| Mode | Input | `local_demo` | Notes |
|------|-------|--------------|-------|
| Preview | `ReportPreviewService::assemble()` | `app.env === local` | Current live behavior |
| Export-safe | Snapshot `payload_json` (+ snapshot row meta as needed) | **`false` for client-bound artifacts** | Even on local hosts when rendering export evidence destined to prove client PDF look |

Required adapter work:

- Map snapshot payload fields (`period`, `client`, `project`, `site`, `monthly_report`, `blocks`, flat fields) into the DTO keys already consumed by `document.php`.
- Preserve IA order via `ClientReportDocument::SECTION_ORDER`.
- Keep strip/empty/manual/risk behavior identical to preview.

Do **not** put into DTO: ids, snapshot keys, checksums, weekly source lists, template diagnostics, apply flags.

---

## 2. CSS inclusion

| Surface | Method | Why |
|---------|--------|-----|
| Auth preview | Linked `/assets/css/client-report.css` | Fine for HTTP |
| Export HTML / future PDF source | **Embed full CSS** into `<style>` | Edge/Chrome `file://` print does not reliably load app HTTP assets |
| Evidence HTML (Impl 01) | Embed | Matches future PDF path |

Implementation notes:

- Read CSS from source file path at render time (app-source `public/assets/css/client-report.css`) and embed; fail closed if missing.
- Keep `@page` and `@media print` rules from client-report.css.
- Do not introduce CDN fonts for export HTML in Impl 01.
- Linked CSS-only export HTML is **not** PDF-ready.

---

## 3. PDF limitations (honest)

- Impl 01 **must not** claim PDF readiness unless an Edge/Chrome print was run (that is a later wave).
- PDF engine prints the **HTML file bytes**; it does not use preview routes.
- If embedded CSS omits a rule, PDF will miss it — Visual QA belongs to PDF Proof wave.
- `ReportTemplateRenderer` embedded token CSS remains the engine for historical v1/v2 artifacts.

---

## 4. Labels and markers

| Concern | Export-safe rule |
|---------|------------------|
| `LOCAL_FIXTURE_ONLY` / `MARS_FIXTURE` | Strip via existing `stripFixtureMarkers` |
| Local demo banner (“Локальная демо-среда”) | **Off** for export-safe / client artifact mode |
| Draft note | Allowed for non-finalized; finalized → “Итоговый отчёт” |
| Technical meta (`block_key`, checksum, template id comments) | **Forbidden** in client export HTML |
| Fake KPI / invented metrics | **Forbidden** — empty sections use empty messages |
| Empty sections | Keep honest empty copy; do not invent content |

---

## 5. Empty states

Reuse preview empty messages. Do not hide empty sections from the six-section IA unless a later product decision changes Target IA. Risk section keeps attention styling without “critical” alarmism.

---

## 6. Print twin vs export

`/preview/print` remains an **auth live** twin. It may guide visual expectations but is **not** the immutable export source. Exports stay snapshot-based so reopening/editing live blocks cannot silently change issued files.
