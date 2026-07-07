# FP-0002 V9-06E22 Repair Plan

## 1. Admin IA repair

Remove `Герои` from **Настройки сайта** direct children and from `get_batch2_fielded_block_slugs()`.

Preserve under **Настройки сайта**:

- Общие настройки
- Повторяемые блоки
- Финальная форма
- Специалисты
- CTA-блоки
- Шапка
- Подвал
- Комфорт / преимущества

Top-level **Отзывы** unchanged.

## 2. ACF field group repair

- Remove `block_hero_fallbacks()` from `FieldGroups.php`
- Delete `acf-json/group_fp02_block_hero_fallbacks.json`
- Delete `group_fp02_block_hero_fallbacks` from runtime DB via `acf_delete_field_group`

Local hero groups untouched.

## 3. Frontend fallback repair

Remove:

- `shpigovsky_get_hero_fallbacks_block_context()`
- `shpigovsky_get_block_hero_fallback_image()`
- Block option read in `shpigovsky_get_hero_theme_fallback()`

Restored chain: **local/entity `hero_media` → theme asset registry → safe fallback**

## 4. Data preservation

- No local hero postmeta writes
- No page/service content writes
- Orphaned `options_fp02-block-hero-fallbacks_*` values may remain in DB (unused)

## 5. Runtime delivery

- `OptionsPage.php`, `FieldGroups.php`
- `hero-helpers.php`, `reusable-blocks-helpers.php`
- Delete runtime `group_fp02_block_hero_fallbacks.json`

## 6. Validation

- No `Герои` under Site Settings (source + ACF probe)
- Local hero groups present
- Frontend 9/9 routes HTTP 200
- E21 header/footer/comfort ACF groups active

Evidence: `validation/v9-06e22-remove-global-heroes-settings/repair-plan.json`
