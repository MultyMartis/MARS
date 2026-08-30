# I-SEO Report Hub — Client Report Template Architecture v0.1

**Status:** CHARTER / ARCHITECTURE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Client Report Template Visual Alignment Charter 01

No code in this wave. Implementation 01 must follow this file.

---

## 1. Options

### Option A — Restyle existing preview/export templates in place

Change `report-preview/show.php` and `ReportTemplateRenderer` independently.

| Pros | Cons |
|------|------|
| Fast | Easy to leave admin chrome + diagnostics mixed into “client” view |
| | Preview (`app.css` + layout) and export (embedded CSS) drift |
| | Print still tied to admin layout |

**Not recommended** as the primary path.

### Option B — Dedicated reusable client report render

One document partial (or renderer) used by:

- internal preview (new document layout);
- future HTML export;
- future PDF (via that HTML);
- future HTML public view **if** product ever adds one (today public share is PDF-only).

Admin pages stay on `layout.php`.

| Pros | Cons |
|------|------|
| One composition / IA / hide-list | More files than a CSS-only tweak |
| Safe split from assembly/admin | Preview and issued PDF can temporarily differ (acceptable) |
| PDF-ready structure without regen now | |

**Recommended.**

### Option C — Separate PDF-only template and web-share template

| Pros | Cons |
|------|------|
| Tune PDF independently | Duplicate IA and hide-list |
| | Two visual sources of truth |

**Defer.** Use Option B; only split later if Edge print proves a real conflict.

---

## 2. Recommendation

**Option B.**

Implementation 01:

- add the dedicated client document render;
- switch **only** `/monthly-reports/{id}/preview` and `/preview/print` onto a **document layout** (no sidebar);
- do **not** regenerate export 3/4;
- do **not** change public share streaming;
- do **not** restyle assembly-preview or export detail as the client report.

`ReportTemplateRenderer` may stay as-is in Impl 01 (issued artifacts unchanged). A later export-alignment wave should **reuse the same document renderer** (or call the same PHP partial from the exporter) so future HTML/PDF match preview.

---

## 3. Target file structure (Implementation 01)

Proposed (names may be kebab-case equivalents; do not restructure unrelated folders):

| Path | Role |
|------|------|
| `app/Views/layout-client-report.php` | Document HTML shell: charset, title, CSS, no sidebar/topbar |
| `app/Views/partials/client-report/document.php` | Cover + IA sections + footer |
| `app/Views/pages/report-preview/show.php` | Thin page: optional `no-print` back strip + include document |
| `app/Views/pages/report-preview/print.php` | Keep as twin; same document |
| `public/assets/css/client-report.css` | Screen + `@media print` tokens (or a clearly scoped block if a new file is too heavy — **prefer dedicated file** so export can later embed it) |
| `app/Services/ClientReportViewService.php` (optional) | Maps assemble() payload → client DTO (order, hide, empty states, strip fixture markers) |
| `app/Support/ReportTemplateRenderer.php` | **Unchanged in Impl 01** unless a non-writing dry-render helper is added without touching artifacts |

Do not edit `dist`. Do not add frameworks. JS not required.

`View` already supports `$layout` and `renderPartial`. `BaseController::render(..., $layout)` can pass `layout-client-report`.

---

## 4. Data contract (client DTO)

Input: `ReportPreviewService::assemble()` (+ report row, optional active snapshot for **operator strip only**).

Output DTO (conceptual):

```
ClientReportDocument
  brand: "i-SEO"
  title: string (fixture markers stripped)
  document_type: "Ежемесячный SEO-отчёт"
  client_name, project_name, site_label_or_url
  period_label: human range
  status_label: "Итоговый отчёт" | "Черновик"
  report_date: finalized_at | preview generated_at
  local_demo: bool (true in local env)
  specialist_name?: optional display name
  sections: list of
    key: one of the six
    heading_ru: from UiLabels
    body_text: string (escaped; markers stripped)
    is_empty: bool
    is_manual: bool (executive_summary, results_summary, key_findings)
    tone: "default" | "attention"  (risks default attention, not critical)
```

Must **not** include: ids, keys, checksums, weekly sources, diagnostics, apply flags, snapshot keys.

Ordering: fixed IA list in Target IA §2, not DB `sort_order`.

---

## 5. Routes

| Route | Impl 01 |
|-------|---------|
| `GET /monthly-reports/{id}/preview` | Keep path; change layout/view |
| `GET /monthly-reports/{id}/preview/print` | Same document; print CSS |
| Assembly / export / share / snapshot | Unchanged |
| Public `/share/report/{token}` | Unchanged PDF stream |

No new public route. No `/preview/client` unless implementation hits a hard conflict (not expected).

---

## 6. PDF regeneration

**Not in Implementation 01.**

Changing renderer code without creating a new export row does not alter files on disk. Public share continues to stream export **4**.

When export HTML is later aligned, generate a **new** styled version (v3+), never overwrite ids 3/4.

---

## 7. Auth

Preview remains **internal-auth**. Client look ≠ public access. Public clients still receive the issued PDF via tokenized share.
