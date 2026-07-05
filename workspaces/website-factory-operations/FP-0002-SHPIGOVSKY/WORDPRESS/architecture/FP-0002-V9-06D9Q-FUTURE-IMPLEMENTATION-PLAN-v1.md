# FP-0002 V9-06D9Q Future Implementation Plan v1

**Date:** 2026-07-06

Evidence: `validation/v9-06d9q-reviews-include-planning/future-implementation-plan.json`

**Not authorized for execution in D9-Q.**

---

## Phase overview

| Phase | Name | Writes | Checkpoint |
|-------|------|--------|------------|
| **D9-R** | Shared include + schema | Theme, ACF JSON, runtime delivery | YES before sync |
| **D9-S** | Controlled seed / fallback wiring | Options values only | YES before seed |
| **D9-T** | Admin UX + visual regression QA | Evidence only | NO |
| **D9-U** | Legal/native content review (optional) | None | N/A |

---

## D9-R — Shared include source/schema

### Scope

- Add `group_fp02_site_options_reviews.json`
- Add `inc/reviews-helpers.php`, `template-parts/shared/reviews-slider.php`
- Refactor Home + reviews page partials
- Remove `home_reviews_teaser` from Home group
- Update plugin FieldGroups/RepeaterValidation if needed
- Bounded runtime delivery

### ACF JSON changes

**YES**

### Validation

- PHP lint
- Routes: `/`, `/kontakty/`, `/otzyvy/`, service 74
- Home reviews section with static fallback
- Home admin without reviews teaser field
- Site settings shows Reviews group

---

## D9-S — Seed or fallback

- Operator-chartered seed of V9 static cards into options **OR** explicit keep-static decision
- Set `reviews_enabled`, `visible`, `featured` flags
- Verify options-driven render path

### ACF JSON changes

**NO**

### DB checkpoint

**YES** before any `update_field(..., 'option')`

---

## D9-T — QA

- Home admin UX (no teaser)
- Site settings reviews usability
- Frontend 19/19 sections
- Swiper/pagination smoke
- `/otzyvy/` visual vs V9

Read-only; evidence JSON + screenshots.

---

## D9-U — Optional legal review

Testimonial authenticity and production content approval. May gate production migration of review text.

---

## Recommended next phase

**D9-R** — `CREATE_V9_06D9R_REVIEWS_SHARED_INCLUDE_IMPLEMENTATION_TASK`
