# FP-0002 V9-06E17 — Site Settings IA Skeleton

**Evidence:** `validation/v9-06e17-site-settings-ia-skeleton/site-settings-ia-skeleton-result.json`

## Implemented

| Component | Status |
|-----------|--------|
| Parent `fp02-site-settings` | ACTIVE, redirect=true |
| `Общие настройки` | ACTIVE with contacts + modal/CTA groups |
| `Повторяемые блоки` | ACTIVE redirect parent |
| 12 block subpages | SKELETON with admin info notice |
| Top-level `Отзывы` | UNCHANGED |
| `fp02-block-reviews` | SKELETON placeholder |

## Source changes

- `plugins/shpigovsky-core/src/Admin/OptionsPage.php` — full IA registration
- `plugins/shpigovsky-core/src/Fields/FieldGroups.php` — location → general subpage
- `acf-json/group_fp02_site_options_contacts.json` — location sync
- `acf-json/group_fp02_site_options_modal_cta.json` — location sync

## Storage

`post_id=option` on general subpage preserves all `options_*` values. Zero DB writes in E17.
