# i-SEO Report Hub — Screenshot QA P0 Fix Strategy v0.1

**Wave:** Screenshot QA Fix Charter 01  
**Next implementation:** `I-SEO Report Hub — Screenshot QA P0 Fix Implementation 01`  
**Policy:** render-layer first; **no** DB mutation in P0 implementation; PDF/export/share frozen

---

## Goal

Eliminate four P0 visual defects from Automated Screenshot Capture 01 without mutating local DB rows, export 4, shares, or PDF artifacts.

---

## Fix 1 — Render-layer sanitizer

### Intent

Hide technical fixture markers from **normal** UI surfaces while leaving DB values unchanged.

### Markers to strip / neutralize (display)

- `LOCAL_FIXTURE_ONLY`
- `MARS_FIXTURE`
- Obvious fixture suffixes in titles (e.g. trailing `— LOCAL_FIXTURE_ONLY`, spaced marker fragments)
- Related marker fragments already handled partially by `ClientReportDocument::stripFixtureMarkers()`

### Apply to

- Report / period titles in lists and headers
- Reporting periods table «Название»
- Monthly report detail summaries (default visible fields)
- Parent report banner on work entry create/edit
- Summary assembly preview labels where markers leak
- Client preview / print document title and section bodies

### May remain

- Collapsed `<details>` technical / debug sections (if product keeps them)
- Manager shell banners that intentionally say «тестовая среда» / fixture badge **as environment honesty** (distinct from raw `LOCAL_FIXTURE_ONLY` in content) — do not invent new EN debug strings

### Implementation shape

- Prefer shared helper, e.g. `app/Support/UiTextSanitizer.php`, **or** extend existing support (`ClientReportDocument::stripFixtureMarkers` + call sites).
- Views/controllers call sanitizer at **render** time only.
- **Must not** UPDATE MySQL.

### Existing baseline

`ClientReportDocument::stripFixtureMarkers()` already strips `LOCAL_FIXTURE_ONLY` / `MARS_FIXTURE` for client document body formatting — **not** consistently applied to manager list/detail titles. P0 must close that gap.

---

## Fix 2 — Demo content cleanup strategy (render-first)

### Decision for P0

**Prefer render-layer fallbacks / empty states. No DB mutation.**

### Obvious test strings (display)

Treat as non-showable when they are the **entire** body (or dominate):

- `Updated body`
- `Risks body`
- Numeric-only bodies like `78678`, `786786`, `6786`, `786`
- Other trivial junk patterns of the same class (short English placeholder bodies)

### Client preview behavior

When a section body is junk / empty after sanitize:

- Show calm Russian empty state (reuse existing copy where present, e.g. «Раздел будет заполнен после ручной редакции.» or equivalent calm empty), **or**
- Optional short neutral SEO-demo placeholder text (product-safe, no fake metrics)

Do **not** regenerate PDF/HTML export from cleaned preview.

### Later (separate wave only)

If operator wants real DB content replacement:

- Dedicated **local-only DB cleanup / proof** charter
- Backup before write
- Explicit allowlisted IDs / fields
- No silent mutation inside P0 Fix Implementation 01

---

## Fix 3 — Reporting periods action button labels

### Evidence

`03_reporting_periods.png`: yellow primary action pills look empty; «Изменить» readable.

### Source read (planning)

`app/Views/pages/reporting-periods/index.php` already outputs label `Открыть` on `.btn.btn-primary.btn-sm`.

CSS conflict:

```css
.data-table .actions a {
  color: var(--color-accent); /* #facc15 */
}
```

overrides `.btn-primary` text color (`--brand-accent-text` / dark) → **yellow text on yellow background**.

### Fix

- Restore readable button text color for `.btn` / `.btn-primary` inside `.data-table .actions` (higher specificity or exclude `.btn` from link color rule).
- Keep action links as **safe GET** (`Открыть` → period show; `Изменить` → edit).
- **No POST.**

Optional: scan other data tables with the same pattern if screenshots show empty yellow pills.

---

## Fix 4 — Friendly Russian 404

### Target

`app/Views/pages/not-found.php` (rendered by `HealthController::notFound()` for unmatched paths).

### Expected copy

- Heading: `Страница не найдена`
- Body: `Такой страницы нет или ссылка устарела.`
- CTA: `На главную` → `/`

### Rules

- Update **error view only** (and CSS if needed).
- **No** route-matching rewrite.
- Hide exact path / «Phase 1A…» from normal view; optional collapsed technical details if useful for local debug.
- Keep HTTP status **404**.

Out of P0: other inline English 404 HTML strings in various controllers (resource-not-found). May be noted for later localization pack; primary capture was router 404 page.

---

## Explicitly not in P0 strategy

- PDF regeneration / export HTML alignment
- Export 4 overwrite
- Share create/revoke/token changes
- Report finalize / reopen / apply POST
- Broad monthly-report UX collapse (P1)
- Mobile responsive QA (P2)
- Production ops
