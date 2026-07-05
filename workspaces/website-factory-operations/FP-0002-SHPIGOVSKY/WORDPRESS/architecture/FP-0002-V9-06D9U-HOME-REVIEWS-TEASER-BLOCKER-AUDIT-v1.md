# FP-0002 V9-06D9U — Home Reviews Teaser Blocker Audit

## Summary

Home admin blocker traced to **PHP-local** `home_reviews_teaser` field still registered in `shpigovsky-core` `FieldGroups.php` (`field_fp02_home_reviews_teaser`, max 6 rows via `RepeaterValidation.php`). Canonical JSON and DB field group no longer contain the field; orphan post meta on page #4 preserved.

## Repair approach

Theme `inc/admin-options.php` suppresses admin visibility (`acf/prepare_field`) and strips POST payload before core validation (`acf/validate_save_post` priority 1). No plugin edits.

## Result

PASS — blocker removed from Home admin UX without deleting orphan meta.
