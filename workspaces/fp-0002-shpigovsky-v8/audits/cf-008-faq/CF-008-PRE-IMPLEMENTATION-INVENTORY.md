# CF-008 Pre-Implementation Inventory

**Family:** `home-faq` → target `faq`
**HEAD:** `4fe928f2512af77413d61a5263aa685aae667123`
**Date:** 2026-06-28

## Consumer table

| Page | Include path | Root class | Items | Trigger hook | Panel hook | IDs/ARIA | Default state | Page scope |
|---|---|---:|---|---|---|---|---|
| index.html | partials/sections/home-faq.html | home-faq | 10 | data-accordion-button | data-accordion-panel | headingId=home-faq-heading; triggers 1–10; panels 1–10 | item 1 open | shared partial |
| uslugi.html | partials/sections/home-faq.html | home-faq | 10 | data-accordion-button | data-accordion-panel | headingId=home-faq-heading | item 1 open | shared partial |
| uslugi-v2.html | partials/sections/home-faq.html | home-faq | 10 | data-accordion-button | data-accordion-panel | headingId=home-faq-heading | item 1 open | shared partial |
| usluga-podrazdel-v1.html | partials/sections/home-faq.html | home-faq | 10 | data-accordion-button | data-accordion-panel | sectionId=service-subdivision-faq | item 1 open | page section/heading ids |
| usluga-konechnaya-v1.html | partials/sections/home-faq.html | home-faq | 10 | data-accordion-button | data-accordion-panel | sectionId=service-leaf-faq | item 1 open | page section/heading ids |

## Summary

- **Consumers:** 5
- **Inline copies:** 0
- **Duplicate partials:** 0
- **CSS copies:** 0 (single `.home-faq__*` block in `style.scss`)
- **JS initializations:** 1 global `[data-accordion]` handler in `main.js` (not name-scoped)
- **Content variants:** 0 (same hardcoded Q/A on all pages)
- **Structure variants:** 0
- **Default-state variants:** 0 (first item open everywhere)

## Boundary

| Related family | Partial | Pages | Structural relationship | Included in CF-008 |
|---|---|---:|---|---:|
| home-faq | home-faq.html | 5 | FAQ accordion H2 + list | YES |
| home-treatment-prevention | home-treatment-prevention.html | 1 | Different layout/content | NO |
| home-why-us | home-why-us.html | 1 | Uses data-accordion-panel only | NO |
| legal/service accordions | — | 0 | Not present | NO |

**Boundary decision:** CONFIRMED — only `home-faq` family in scope.

## Component identity

**Classification:** SHARED_BUT_PAGE_NAMED
**Result:** CONFIRMED — identical HTML structure, CSS, JS behavior, default state across all consumers.
