# V9-06E56 Task I — Comfort admin menu split

## Approach

1. **Storage unchanged:** all comfort / gallery / rehab ACF values remain under options post_id `fp02-block-comfort` (`fp02-block-comfort_*` in `fp02_options`). Frontend `get_field(..., 'fp02-block-comfort')` is untouched.
2. **New admin menus** (same `post_id`):
   - `fp02-block-comfort-intro` — Комфорт — вводный блок
   - `fp02-block-comfort-gallery` — Комфорт — галерея
   - `fp02-block-comfort-requirements` — Комфорт — требования
3. **Field groups split** (field keys preserved; each key in exactly one group):
   - `group_fp02_block_comfort_intro`
   - `group_fp02_block_comfort_gallery`
   - `group_fp02_block_comfort_requirements`
4. **Legacy page** `fp02-block-comfort`: still registered for bookmark safety, **removed from submenu**, **admin_init redirect** → intro.
5. **E55 styling:** new slugs match `fp02-block-*` → `fp02-site-settings-admin` body class still applies.
6. **Zero content mutation:** pre-split evidence dump in `comfort-options-pre-split-evidence.json`.

## Operator note

Old monolithic ACF JSON archived to `group_fp02_block_comfort.pre-split.json.bak`. If a DB-synced copy of `group_fp02_block_comfort` existed, it was set to `acf-disabled`.
