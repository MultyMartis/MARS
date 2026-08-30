# i-SEO Report Hub — Screenshot QA P0 Fix Implementation Result v0.1

**Wave:** Screenshot QA P0 Fix Implementation 01  
**Date:** 2026-08-21  
**Verdict:** `SCREENSHOT QA P0 FIX PASS_WITH_MINOR_ISSUES`

---

## P0 fixes applied

| ID | Fix | Approach |
|----|-----|----------|
| P0-1 | Fixture markers | Render-layer `UiTextSanitizer` + wired into manager/client views |
| P0-2 | Demo junk bodies | Line-aware junk filter + section fallbacks in `ClientReportDocument` / assembly |
| P0-3 | Empty yellow buttons | CSS specificity for `.data-table .actions a.btn-primary` |
| P0-4 | Technical EN 404 | Russian friendly `not-found.php` + optional local collapsed tech details |

**No DB mutation. No export/share/PDF mutation. Export 4 untouched.**

---

## Files changed (app-source)

- `app/Support/UiTextSanitizer.php` **(new)**
- `app/Support/ClientReportDocument.php`
- `app/Support/UiLabels.php`
- `app/Support/helpers.php`
- `app/bootstrap.php`
- `app/Views/pages/not-found.php`
- `app/Views/pages/reporting-periods/index.php`
- `app/Views/pages/reporting-periods/show.php`
- `app/Views/pages/monthly-reports/show.php`
- `app/Views/pages/monthly-reports/assembly-preview.php`
- `app/Views/pages/monthly-report-work-entries/form.php`
- `app/Views/partials/monthly-work-entries.php`
- `public/assets/css/app.css`

---

## Runtime sync (exact)

Synced Model A → `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`:

- `app/Support/UiTextSanitizer.php`
- `app/Support/ClientReportDocument.php`
- `app/Support/UiLabels.php`
- `app/Support/helpers.php`
- `app/bootstrap.php`
- `app/Views/pages/not-found.php`
- `app/Views/pages/reporting-periods/index.php`
- `app/Views/pages/reporting-periods/show.php`
- `app/Views/pages/monthly-reports/show.php`
- `app/Views/pages/monthly-reports/assembly-preview.php`
- `app/Views/pages/monthly-report-work-entries/form.php`
- `app/Views/partials/monthly-work-entries.php`
- `public/assets/css/app.css`

**Not synced:** `.env.local`, storage, exports, logs, DB, vendor, PDFs, WordPress/i-seo.su, OVERSEO assets.

---

## Evidence

| Role | Path |
|------|------|
| Before | `X:\AI MARS STORAGE\incoming\iseo-report-hub\automated-screenshot-capture-01\20260821-010501` |
| After | `X:\AI MARS STORAGE\incoming\iseo-report-hub\screenshot-qa-p0-fix-implementation-01\20260821-023143` |
| After index | `...\20260821-023143\P0-FIX-SCREENSHOT-INDEX.md` |
| After assertions | `...\20260821-023143\P0-FIX-ASSERTIONS.md` |

Screenshots are Storage evidence only — **not** committed.

---

## Validation summary

- PHP lint: all synced PHP files OK
- HTTP GET: health/login + required authenticated routes OK; 404 status preserved
- Normal-visible forbidden strings: absent on P0 assert pages (textarea / tech-details excluded)
- DB before/after identical (periods=2, monthly=2, report1 blocks=6 entries=7, exports=4, shares=7, export4 size=117055, checksum prefix `a8c4d61c6216`)

### Minor residual (accepted by charter)

- Work-entry **edit** form may still show `LOCAL_FIXTURE_ONLY` inside editable `internal_note` / `evidence_note` textareas (no DB write; intentional).
- Assembly preview may keep raw markers only inside collapsed **Технические детали**.

---

## Remaining P1/P2

See triage result: P1 monthly-detail UX collapse; P1/P2 report-5 deeper content; PDF/export alignment **parked**; mobile deferred.

---

## Next

Operator review of P0 after screenshots.
