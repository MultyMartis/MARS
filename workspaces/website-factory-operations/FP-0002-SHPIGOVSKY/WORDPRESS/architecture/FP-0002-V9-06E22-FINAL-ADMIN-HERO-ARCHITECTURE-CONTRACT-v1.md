# FP-0002 V9-06E22 Final Admin / Hero Architecture Contract

## Site Settings menu (final)

Direct children under **Настройки сайта**:

1. Общие настройки
2. Повторяемые блоки
3. Финальная форма
4. Специалисты
5. CTA-блоки
6. Шапка
7. Подвал
8. Комфорт / преимущества

**Forbidden:** `Герои` under Site Settings.

## Hero architecture authority

Hero blocks are **local/entity-owned**, not global reusable blocks.

| Context | Admin location | Primary field |
|---------|----------------|---------------|
| Home | Front page edit | `hero_media`, `home_hero_slides` |
| Services hub | Page `uslugi` | `hero_media` |
| Service subdivision/leaf | Service post | `hero_media`, hero text fields |
| Institutional pages | Page edit | `hero_media` |

## Fallback chain (post-E22)

```
local/entity hero_media
  → theme asset registry (shpigovsky_get_hero_context_registry)
  → safe empty fallback
```

No global hero option layer.

## E21 preserved

- Шапка (`group_fp02_block_header`)
- Подвал (`group_fp02_block_footer`)
- Комфорт / преимущества (`group_fp02_block_comfort`)

## Batch 1 preserved

- Финальная форма, Специалисты, CTA-блоки

## Reviews

- Top-level **Отзывы** (`fp02-reviews`) preserved
- No reviews alias under Site Settings

## Deferred

- Batch 3 reusable blocks
- Service duplicate feature
- Obsolete page cleanup

Evidence: `validation/v9-06e22-remove-global-heroes-settings/final-e22-admin-hero-architecture-contract.json`
