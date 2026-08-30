# I-SEO Report Hub — Client Report Export Alignment Options v0.1

**Status:** CHARTER / OPTIONS — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-20  
**Wave:** Client Report Export HTML Alignment Charter 01

---

## Option A — Modify `ReportTemplateRenderer` to use `ClientReportDocument`

Replace or heavily rewrite the existing string-built export HTML so it consumes the client document DTO / partials.

| Pros | Cons |
|------|------|
| Single future SoT for preview/export/PDF | High blast radius on any future `createHtml*` / styled create path |
| Less dual-path long term | May surprise operators if any create runs before PDF proof is ready |
| | Existing dry-render expectations / Visual QA baselines for `iseo_default_v1` internal HTML shift |

**Not recommended for Implementation 01.**

---

## Option B — Dedicated export HTML renderer variant (keep old renderer)

Add a **new** export-safe path that reuses:

- `ClientReportDocument` (extend with snapshot adapter if needed);
- `layout-client-report` / `partials/client-report/document` composition (or an export twin that embeds CSS);
- `client-report.css` content (embedded for PDF safety).

Leave `ReportTemplateRenderer` intact so historical recreate/idempotent paths and mental model of v1/v2 internal exports stay stable. Existing artifacts **1–4** remain untouched because they are already on disk.

| Pros | Cons |
|------|------|
| Safest code alignment toward client look | Temporary dual path |
| No existing artifact change | Need snapshot→DTO adapter |
| Future exports can opt into client document mode | Must explicitly wire create paths later |
| Supports non-mutating smoke/evidence first | |

**Recommended.**

---

## Option C — Docs/manual only until PDF regeneration wave

Defer all code until a combined HTML+PDF proof.

| Pros | Cons |
|------|------|
| Zero code risk now | No proof that client document can render export-safe HTML |
| | PDF wave would carry both template and engine risk |

**Defer as sole strategy** — too little progress after preview pass.

---

## Recommendation

**Option B.**

### Implementation 01 shape (within Option B)

| Decision | Choice |
|----------|--------|
| Modify old renderer? | **No** |
| Add new service/renderer? | **Yes** — e.g. `ClientReportHtmlRenderer` / `ClientReportExportRenderService` |
| Wire into `createHtml*` / styled create? | **No** in Impl 01 (dormant / explicit method only) |
| New export DB row? | **Forbidden** |
| PDF regeneration? | **Forbidden** |
| HTTP route for export preview? | **Optional — prefer no**; use CLI/tool or service method smoke |
| Use `/preview/print` as HTML source for future PDF? | **Not as product export source** — print is auth live assemble; exports must stay **snapshot-based**. Print may remain a **visual reference** only |
| CSS for export evidence | **Embed** CSS text for PDF-readiness; do not claim PDF proof until Edge run on that HTML |

### Dual-path exit criteria (later)

After PDF Regeneration Proof + operator acceptance, either:

1. make client document renderer the default for **new** export versions; or  
2. retire internal `ReportTemplateRenderer` for new creates while keeping it for forensic/legacy understanding.

Do **not** delete old renderer while exports **1–4** and their Visual QA history still matter.
