# ROLLBACK — Specialists Hub 01

Operator full Beget backup existed before this wave.

## Bounded restore

1. Page `#1030`
   - `_wp_page_template` → `page-templates/generic.php`
   - optional: restore `generic_page_body` / `post_content` from `03-mutate.json` → `before` (placeholder only)
2. Files: restore from `layer-b-pre-deploy/` / remove new hub template parts:
   - `wp-content/themes/shpigovsky/page-templates/specialists-hub.php` (remove)
   - `wp-content/themes/shpigovsky/template-parts/specialist/hub-content.php` (remove)
   - `wp-content/themes/shpigovsky/template-parts/specialist/hub-list.php` (remove)
   - restore prior `fancybox-vendors.php`, `FieldGroups.php`, `shpigovsky-core.php`, `acf-json/group_fp02_page_generic_content.json`

Do not use full theme overwrite or full DB restore for this wave.
