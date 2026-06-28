# CF-007 Pre-Implementation Inventory — Reviews (`home-reviews`)

**Wave:** FP-0002 V8 CF-007
**HEAD at inventory:** 4737b020c93dcbdfd2b309b3abe9a564a9a8ca79
**Classification:** SHARED_BUT_PAGE_NAMED

## Consumer table

| Page | Include path | Root class | Slides | Slider hook | Navigation | Pagination | IDs/ARIA | Page scope |
|---|---|---:|---|---|---|---|---|
| `index.html` | `partials/sections/home-reviews.html` | `.home-reviews` | 10 | `data-reviews-slider` | none (Swiper `navigation: false`) | `data-reviews-pagination` | `aria-label="Отзывы"` on section; rating `aria-label` per card | Home |
| `usluga-podrazdel-v1.html` | `partials/sections/home-reviews.html` | `.home-reviews` | 10 | `data-reviews-slider` | none | `data-reviews-pagination` | same | Service subdivision |
| `usluga-konechnaya-v1.html` | `partials/sections/home-reviews.html` | `.home-reviews` | 10 | `data-reviews-pagination` | none | `data-reviews-pagination` | `id="service-leaf-reviews"` on section | Service leaf |

## Summary

- **Consumers:** 3 (`index.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`)
- **Inline copies:** 0
- **Duplicate partials:** 0
- **Duplicate CSS blocks:** 0 (single block in `style.scss` lines 1683–1826)
- **Duplicate JS initializations:** 0 (`initHomeReviews` in `main.js`, one path)
- **Page-specific wrappers:** 0
- **Visual variants:** 0
- **Content variants:** 0 (same hardcoded content on all pages)
- **Slide-count variants:** 0 (10 slides everywhere)
- **Unresolved dependencies:** none

## Boundary decision

| Related family | Partial | Pages | Visual relationship | Included in CF-007 |
|---|---|---:|---|---:|
| `home-reviews` | `home-reviews.html` | 3 | target family | yes |
| `founder-quote` | `founder-quote.html` | 4 | text quote block, different structure | no |
| standalone testimonials | — | 0 | none in V8 | no |
| review page/cards | — | 0 | none | no |

**Boundary decision:** Only the Swiper testimonial carousel family currently named `home-reviews` is in scope.

**Result:** CONFIRMED

## JS hooks

- `[data-reviews-slider]` — Swiper root (already neutral)
- `[data-reviews-pagination]` — pagination element (already neutral)
- `initHomeReviews()` — IIFE name (page-specific prefix; rename to `initReviews`)

## CSS selectors (active)

Root `.home-reviews` and children: `__heading`, `__title`, `__all-link`, `__all-text`, `__all-icon`, `__slider`, `__wrapper`, `__slide`, `__card`, `__rating`, `__star`, `__quote`, `__text`, `__author`, `__author-name`, `__read-all`, `__pagination` (grouped with gallery/specialists pagination).

## Neutral name target

- Partial: `src/partials/sections/reviews.html`
- Root class: `.reviews`
- Conflict check: no existing `.reviews` family in active V8 source
