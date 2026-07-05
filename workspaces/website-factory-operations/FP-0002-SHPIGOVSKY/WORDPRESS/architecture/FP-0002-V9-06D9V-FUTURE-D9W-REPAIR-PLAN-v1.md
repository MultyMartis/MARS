# FP-0002 V9-06D9V — Future D9-W Repair Plan

**Phase:** V9-06D9-V planning output (no repair performed)  
**Date:** 2026-07-06  
**Recommended charter:** `CREATE_V9_06D9W_REVIEWS_ADMIN_AND_LAYOUT_REPAIR_TASK`

## Wave 1 — Admin duplicate cleanup

- DB checkpoint
- List runtime `acf-field-group` posts for `group_fp02_site_options_reviews`
- Deactivate/trash stale copy on `fp02-site-settings`
- Verify **Настройки сайта** has no reviews module

## Wave 2 — Admin storage context fix

- Migrate canonical review meta to `fp02-reviews` ACF post_id
- Update `inc/reviews-helpers.php` to read/write `'fp02-reviews'`
- Confirm 10 editable rows in **Отзывы** admin
- Confirm frontend source mode **OPTIONS**

## Wave 3 — `/otzyvy/` layout transplant

- Implement `template-parts/reviews/archive-list.php` from static V9:
  - `reviews-archive-list.html`
  - `review-archive-card.html`
- Update `page-templates/reviews.php`:
  - Remove `reviews-section` slider include
  - Add `page-otzyvy` body class / `page-otzyvy__main`
  - Wire `reviews-rehabilitation-requirements` partial
- **Preserve** Home slider via `home/reviews.php` only

## Wave 4 — Validation

- Admin: Site Settings, Отзывы, Home #4 save
- Frontend: Home slider; `/otzyvy/` card list spacing vs static V9 src
- Screenshots where tooling available

## Safety boundaries (D9-W)

- No production migration
- No menu mutation
- No rewrite flush unless separately gated
- Plugin edits only if separately chartered

## Evidence

`validation/v9-06d9v-reviews-admin-static-layout-reconciliation-audit/future-d9w-repair-plan.json`
