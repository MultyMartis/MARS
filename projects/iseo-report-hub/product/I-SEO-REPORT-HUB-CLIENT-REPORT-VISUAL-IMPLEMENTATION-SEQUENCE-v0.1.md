# I-SEO Report Hub — Client Report Visual Implementation Sequence v0.1

**Status:** CHARTER / SEQUENCE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Client Report Template Visual Alignment Charter 01

---

## 1. Next wave (recommended)

**`I-SEO Report Hub — Client Report Template Visual Alignment Implementation 01`**

Scope:

- Option B document partial + client layout + client DTO mapping;
- apply to `GET /monthly-reports/{id}/preview` and print twin;
- preserve routes;
- i-SEO visual tokens; Target IA order; hide technical metadata;
- **no** PDF regeneration;
- **no** new/updated export rows;
- **no** share mutation;
- **no** DB content mutation;
- **no** assembly-preview restyle;
- **no** screenshot QA of all admin pages.

Success = report 1 preview looks like a client SEO document while export **4** / active share stay frozen.

---

## 2. Later waves

| Order | Wave | Intent |
|-------|------|--------|
| 2 | Client Report Public Share Alignment 01 | Only if a **dynamic** HTML share view is added. Today share is PDF stream → **skip unless product changes delivery**. Visual smoke of PDF bytes is not a template task. |
| 3 | Client Report Export HTML Alignment 01 | Point **future** HTML export renderer at the same document. No new row unless the wave explicitly creates a **new** version. Do not overwrite id **3**. |
| 4 | Client Report PDF Regeneration Proof 01 | New PDF from new HTML; evidence; **new** export id; checksum changes only for the new artifact; keep id **4** + current share. |
| Optional | Metrics / results_summary model | Separate; do not fake KPI in visual waves. |
| Optional | Screenshot QA all pages | When operator sends shots; not a gate for Impl 01. |
| Parallel | Production Environment Operator Decision 01 | Environment track; not this UX track. |

---

## 3. Implementation 01 suggested steps

1. Preflight (volume/branch/WIP) + clean worktree if foreign index present.  
2. Add `ClientReportViewService` (or equivalent mapper) — render-time only.  
3. Add `layout-client-report.php` + `partials/client-report/document.php` + CSS.  
4. Switch `ReportPreviewController` to the document layout.  
5. Thin `no-print` back link only.  
6. Keep `print` route on the same document.  
7. GET smoke + DOM/CSS assertions (no sidebar, no `block_key`, six headings in IA order).  
8. Confirm DB/export/share/PDF unchanged.  
9. Docs result + OPERATIONAL-INDEX.  
10. Exact-path commit; **no push**. Runtime sync only if that implementation charter explicitly allows source→runtime copy of the new views/css.

---

## 4. Explicit non-goals for Impl 01

- Regenerating PDF 4.  
- Restyling `assembly-preview`.  
- Public HTML report page.  
- WordPress / i-seo.su.  
- Package installs / font CDN for export.  
- Changing `sort_order` in DB to match IA (render-time order is enough).
