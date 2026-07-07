# FP-0002 V9-06E22 Global Heroes Removal

## Changes applied

| Item | Before | After |
|------|--------|-------|
| Site Settings menu `Герои` | present | removed |
| `fp02-block-hero-fallbacks` in fielded slugs | present | removed |
| `block_hero_fallbacks()` registration | active | removed |
| ACF JSON `group_fp02_block_hero_fallbacks.json` | present | deleted |
| DB field group metadata | present | deleted (1 write) |
| `shpigovsky_get_block_hero_fallback_image()` | active | removed |
| Local hero field groups | present | preserved |

## Files changed

**Plugin**

- `plugins/shpigovsky-core/src/Admin/OptionsPage.php`
- `plugins/shpigovsky-core/src/Fields/FieldGroups.php`

**Theme**

- `theme/shpigovsky/inc/hero-helpers.php`
- `theme/shpigovsky/inc/reusable-blocks-helpers.php`

**ACF JSON**

- Deleted `acf-json/group_fp02_block_hero_fallbacks.json`

Evidence: `validation/v9-06e22-remove-global-heroes-settings/global-heroes-removal-result.json`
