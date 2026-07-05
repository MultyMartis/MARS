# FP-0002 V9-06D9U — Home Blocker Removal

## Actions

1. Added `inc/admin-options.php` — `acf/prepare_field` returns false for `field_fp02_home_reviews_teaser`.
2. Added `acf/validate_save_post` priority 1 — unset `$_POST['acf']['field_fp02_home_reviews_teaser']` before `RepeaterValidation` runs.

## Preserved

- Orphan meta on Home #4 (`home_reviews_teaser`, `home_reviews_teaser_0_*`) untouched.

## Result

PASS — field not visible in admin; save validation no longer blocked.
