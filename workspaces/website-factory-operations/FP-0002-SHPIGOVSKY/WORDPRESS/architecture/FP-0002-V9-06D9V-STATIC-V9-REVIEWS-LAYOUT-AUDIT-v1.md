# FP-0002 V9-06D9V — Static V9 Reviews Layout Audit

**Phase:** V9-06D9-V (read-only)  
**Date:** 2026-07-06  
**Authority:** `workspaces/fp-0002-shpigovsky-v9/src/` (dist/ not built at audit time)

## Home (`src/pages/index.html`)

- Includes `partials/sections/reviews.html`
- **Layout:** Swiper slider (`.reviews` → `.reviews__slider` → `.reviews__slide`)
- **Slides:** 10 static cards
- **Spacing:** `.reviews__heading { margin-bottom: var(--pad-gap) }`; card padding `var(--pad-gap)`

## Reviews page (`src/pages/otzyvy.html`)

- **Body:** `page-otzyvy`
- **Main:** `page-otzyvy__main`
- **Sections (top → bottom):**
  1. `reviews-page__breadcrumbs`
  2. `reviews-archive-list.html` — **vertical card list**, not slider
  3. `reviews-rehabilitation-requirements.html`

### Archive list structure

```
section.reviews-archive
  .container.reviews-archive__container
    h1.reviews-archive__heading
    p.reviews-archive__intro
    .reviews-archive__list[data-reveal-group]
      article.review-archive-card (×6 static)
    nav.reviews-archive-pagination
```

### Key spacing CSS (`src/scss/style.scss`)

- `.reviews-archive__list { flex-direction: column; gap: var(--pad-gap); }`
- `.review-archive-card { gap: var(--pad-gap-line); padding: var(--pad-gap); }`

## Conclusion

- **Home:** shared slider is correct authority.
- **`/otzyvy/`:** must use archive card list — **not** Home slider.

## Evidence

`validation/v9-06d9v-reviews-admin-static-layout-reconciliation-audit/static-v9-reviews-layout-audit.json`
