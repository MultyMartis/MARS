# FP-0002 V9-06E20 Repair Plan

**Wave:** V9-06E20 Remove Reviews Alias From Site Settings  
**Operator authority:** Remove `Отзывы` from **Настройки сайта**; preserve top-level **Отзывы**.

## 1. Admin menu repair

Remove `fp02-block-reviews` from `OptionsPage::get_reusable_block_subpages()` and `get_batch1_fielded_block_slugs()`. Remove alias admin notice block.

**Keep under Настройки сайта:**

- Общие настройки
- Повторяемые блоки
- Финальная форма
- Специалисты
- CTA-блоки

## 2. Reviews preservation

- Keep theme `admin-options.php` top-level `fp02-reviews` (no theme edit).
- Keep storage `post_id=fp02-reviews`.
- Zero reviews option value writes.

## 3. Field group location repair

- ACF JSON: remove `fp02-block-reviews` location rule.
- Runtime DB: `acf_update_field_group` to single `fp02-reviews` location (1 metadata write).

## 4. Runtime delivery

- `plugins/shpigovsky-core/src/Admin/OptionsPage.php`
- `acf-json/group_fp02_site_options_reviews.json`

## 5. Validation

- Admin: alias absent; top-level present; Batch 1 siblings intact.
- Data: 10 rows, sample Андрей preserved.
- Frontend: 7 routes HTTP 200, no fatals.
