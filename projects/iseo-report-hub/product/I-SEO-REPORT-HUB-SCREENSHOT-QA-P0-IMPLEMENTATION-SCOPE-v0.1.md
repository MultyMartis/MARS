# i-SEO Report Hub — Screenshot QA P0 Implementation Scope v0.1

**Next wave name:** `I-SEO Report Hub — Screenshot QA P0 Fix Implementation 01`  
**Charter basis:** Screenshot QA Fix Charter 01  
**Type:** scoped app-source implementation (views / helpers / CSS) + exact runtime sync if Model A requires it  
**Not in next wave:** DB mutation, export/share/PDF mutation, route architecture rewrite

---

## Objectives (P0 only)

1. Hide/sanitize fixture markers (`LOCAL_FIXTURE_ONLY`, `MARS_FIXTURE`, related fragments) in normal UI.
2. Replace bad demo/test bodies in client-facing render with calm empty states or safe demo text (render-layer).
3. Fix empty-looking action buttons on reporting periods (readable labels).
4. Make router 404 page Russian and non-technical.

---

## Allowed work

| Allowed | Notes |
|---------|-------|
| View / helper / render-layer updates | Yes |
| Shared sanitizer support class | Yes |
| CSS fixes for button contrast / labels | Yes |
| Friendly 404 view | Yes |
| Exact `app-source` → runtime sync for changed files | Only if implementation wave charter authorizes Model A sync |
| Login GET/session for validation screenshots | Optional; no password printing |

## Forbidden work

| Forbidden | Notes |
|-----------|-------|
| DB UPDATE/INSERT/DELETE | Including report_blocks, monthly_report_contents, work entries, exports, shares |
| PDF regeneration | Deferred |
| HTML export regeneration / new export row | Deferred |
| Export 4 artifact edits | Frozen |
| Share create/revoke/token changes | Frozen |
| POST apply / finalize / reopen | Forbidden |
| Production / WordPress / i-seo.su | Forbidden |
| Broad git / foreign WIP | Forbidden |

---

## Likely files / areas

Planning-only inventory (implementation may adjust within scope):

| Area | Candidate paths under `projects/iseo-report-hub/app-source/` |
|------|--------------------------------------------------------------|
| Sanitizer | `app/Support/UiTextSanitizer.php` **or** extend `app/Support/ClientReportDocument.php` |
| Client preview mapper / body | `app/Support/ClientReportDocument.php`, `app/Views/partials/client-report/document.php` |
| Reporting periods | `app/Views/pages/reporting-periods/index.php` (+ CSS) |
| Monthly report views | monthly report show / related partials |
| Work entry form header | `app/Views/pages/monthly-report-work-entries/form.php` (+ partials) |
| Assembly preview | `app/Views/pages/monthly-reports/assembly-preview.php` if markers leak |
| 404 | `app/Views/pages/not-found.php` |
| CSS | `public/assets/css/app.css`, `public/assets/css/client-report.css` if needed |
| Bootstrap require | `app/bootstrap.php` only if new support class must be loaded |

Do **not** edit Storage screenshot evidence or export artifacts.

---

## Validation (after implementation)

### Re-capture / re-check pages

At least:

- `/reporting-periods`
- `/monthly-reports/1`
- work entry create + edit
- `/monthly-reports/1/assembly-preview`
- `/monthly-reports/1/preview` (+ print optional)
- `/monthly-reports/5/preview`
- router 404 (`/__mars_visual_qa_404__` or equivalent)

Prefer new evidence under Storage incoming with a new run folder; do not overwrite Capture 01 folder unless operator asks.

### Pass criteria

- No `LOCAL_FIXTURE_ONLY` / `MARS_FIXTURE` in **normal visible** HTML for those pages (collapsed tech details may still mention markers if product keeps them).
- No `Updated body` / `Risks body` / numeric-only junk as visible client section bodies.
- Reporting periods primary action shows readable label (e.g. `Открыть`).
- 404: Russian friendly copy; CTA `На главную`; no Phase 1A router lecture in normal view.
- DB row counts unchanged vs pre-impl baseline (document counts in impl closeout).
- Export 4 / shares / PDF artifacts unchanged (checksums or attested non-touch).

### Smoke safety

- GET-only validation preferred.
- No public share token URL capture.
- No secrets / tokens in reports.

---

## Suggested implementation order

1. Shared sanitizer + wire into list/detail/form headers.
2. ClientReportDocument junk/empty fallbacks.
3. CSS fix for `.data-table .actions` button text.
4. `not-found.php` Russian friendly copy.
5. Validation screenshots + closeout.

---

## Exit

Implementation closeout must reference this scope doc and [I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-SAFETY-ACCEPTANCE-v0.1.md](I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-SAFETY-ACCEPTANCE-v0.1.md).
