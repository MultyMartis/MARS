# FP-0002 V9-06D9Q Recommended Reviews Architecture v1

**Date:** 2026-07-06

Evidence: `validation/v9-06d9q-reviews-include-planning/recommended-reviews-architecture.json`

---

## Architecture name

**FP-0002 Shared Reviews Include (Hybrid E / Options primary)**

---

## Source-of-truth

| Layer | Role |
|-------|------|
| **Primary** | ACF Options repeater `reviews_items` on `fp02-site-settings` |
| **Demo fallback** | Static V9 card set in `shpigovsky_reviews_static_fallback_items()` |
| **Future** | Reviews CPT (not D9-R) |
| **Legacy** | `group_fp02_page_reviews` — defer; optional page override later |

---

## Admin location

- **Options page:** `fp02-site-settings` («Настройки сайта»)
- **New group:** `group_fp02_site_options_reviews` — «Site Options — Reviews»

### Fields

| Field | Type | Notes |
|-------|------|-------|
| `reviews_enabled` | true_false | Master section toggle |
| `reviews_section_heading` | text | Default «Отзывы» |
| `reviews_all_link_label` | text | Default «Смотреть отзывы» |
| `reviews_all_link_url` | url | Default `/otzyvy/` |
| `reviews_items` | repeater max 50 | See sub-fields |

**Repeater sub-fields:** `author_label`, `text`, `metadata`, `source`, `rating` (1–5, default 5), `visible`, `featured`.

All sub-fields **optional** (`required: 0`).

---

## Fallback precedence

1. `reviews_enabled === false` → hide section everywhere.
2. Visible `reviews_items` rows exist → render from options.
3. Else → static V9 demo fallback (current hardcoded cards).
4. (Future) CPT published reviews insert between options and static when implemented.

---

## Frontend structure

| Path | Role |
|------|------|
| `inc/reviews-helpers.php` | Query/normalize/fallback logic |
| `template-parts/shared/reviews-slider.php` | Shared Swiper markup |
| `template-parts/home/reviews.php` | Thin wrapper: `context=home`, `limit=10`, `featured_only=true` |
| `template-parts/reviews/reviews-section.php` | Reviews page hero/slider |
| `template-parts/reviews/archive-list.php` | Full list, no limit |

Heading precedence: `reviews_section_heading` option → `home_reviews_heading` (until migrated) → static «Отзывы».

---

## `home_reviews_teaser` disposition

| Action | Timing |
|--------|--------|
| Remove from Home ACF group JSON | D9-R |
| Never wire to frontend | Permanent |
| Orphan DB meta | Leave; no destructive cleanup |
| `home_reviews_heading` | Migrate to options in D9-R (preferred) or keep temporarily |

---

## Content policy

- **Static fallback:** DEMO_ONLY — not production-approved testimonials.
- **Options seed (D9-S):** Operator-chartered; documented payload.
- **Production:** D9-U legal/native review optional before go-live.

---

## Migration

1. D9-R: commit ACF JSON + theme helpers; bounded runtime delivery.
2. D9-S: DB checkpoint; seed options from V9 static if operator approves.
3. Export options via ACF/tools for production push.

---

## Answers to D9-Q charter questions

| # | Question | Answer |
|---|----------|--------|
| 1 | Where should reviews live? | ACF Options `reviews_items` on `fp02-site-settings` |
| 2 | Shared globally? | **Yes** — one helper, multiple template contexts |
| 3 | How should Home consume? | Shared include with limit/featured filter |
| 4 | CPT vs Options vs hybrid? | **Hybrid E** — Options now, CPT later if needed |
| 5 | Safest for FP-0002 stage? | Options + shared include + static fallback |
| 6 | What to do with `home_reviews_teaser`? | Deprecate; remove from Home admin in D9-R |
| 7 | Next implementation task? | **D9-R** shared include + schema |
