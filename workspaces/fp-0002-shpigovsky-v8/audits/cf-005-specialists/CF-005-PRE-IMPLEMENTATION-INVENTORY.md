# CF-005 Pre-Implementation Inventory — Specialists

**Date:** 2026-06-28
**Classification:** SHARED_BUT_PAGE_NAMED
**HEAD:** pre-implementation snapshot

---

## Consumer table

| Page | Include path | Root class | Slider hook | Navigation hooks | IDs/ARIA | Page scope dependency |
|---|---|---|---|---|---|---|
| `index.html` | `partials/sections/home-specialists.html` | `.home-specialists` | `data-specialists-slider` | pagination `data-specialists-pagination` | `headingId`: `home-specialists-heading`; `aria-labelledby` on section | Home-prefixed root class and heading id |
| `usluga-podrazdel-v1.html` | `partials/sections/home-specialists.html` | `.home-specialists` | `data-specialists-slider` | pagination `data-specialists-pagination` | `sectionId`: `service-subdivision-specialists`; `headingId`: `service-subdivision-specialists-heading` | Page-specific section/heading ids only |
| `usluga-konechnaya-v1.html` | `partials/sections/home-specialists.html` | `.home-specialists` | `data-specialists-slider` | pagination `data-specialists-pagination` | `sectionId`: `service-leaf-specialists`; `headingId`: `service-leaf-specialists-heading` | Page-specific section/heading ids only |

---

## Summary

| Metric | Value |
|---|---:|
| Total consumers | 3 |
| Inline copies | 0 |
| Duplicate partials | 0 |
| Duplicate CSS blocks | 0 (shared selectors in `style.scss`) |
| Duplicate JS initializations | 0 (`initHomeSpecialists` — single `[data-specialists-slider]` loop) |
| Page-specific wrappers | 0 |
| Visual variants | 0 |
| Content variants | 0 (same hardcoded cards on all pages) |
| Unresolved dependencies | 0 |

---

## CSS selectors (active source)

- `.home-specialists__pagination` (+ bullet rules shared with reviews/gallery)
- `.home-specialists__head`, `__heading`, `__all-link`, `__all-icon`
- `.home-specialists__slider`, `__wrapper`, `__card`, `__photo`, `__name`, `__role`
- Media query: `.home-specialists__head` at ≤1024px

No standalone `.home-specialists` root block in SCSS (child-only family).

---

## JS

- File: `src/js/main.js`
- Init: `initHomeSpecialists()` — `querySelectorAll('[data-specialists-slider]')`
- Pagination: `[data-specialists-pagination]`
- Swiper config: slidesPerView 3.5 / breakpoints 320, 768, 1025; loop false; navigation false

---

## Component identity

All three consumers use identical partial markup, card order (5 slides), images under `assets/img/content/home-specialists/`, and shared CSS/JS. **SHARED_BUT_PAGE_NAMED — safe to universalize.**
