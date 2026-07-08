# FP-0002 V9-06E26 Risk And Dependency Map v1

## Цель

Сконцентрировать ключевые риски E26 и зафиксировать зависимости, критичные для безопасного исполнения волн E26A-E26D.

## Источники валидации

- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/risk-and-dependency-map.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/final-verdict.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/no-scope-drift-validation.json`

## Карта рисков

| ID | Риск | Влияние | Вероятность | Митигирующая мера |
|---|---|---|---|---|
| R1 | Permalink mismatch (`/%postname%/` vs `"/blog/%postname%/"`) | High | High | Принудительное выравнивание permalink до launch |
| R2 | Skeleton-шаблоны дают неполный/неверный рендер | High | High | Закрыть шаблонные гэпы в E26A-C |
| R3 | Несоответствие draft 746 (E25A vs E26 probe) | Medium | Medium | Зафиксировать mismatch, повторно проверить в E26D |
| R4 | Obsolete страницы мешают будущей route-cleanup | Medium | Medium | Отдельный E27 backlog по IDs `10/17/21/25` |

## Карта зависимостей

1. Стабильность ACF-групп между окружениями (`group_fp02_page_institutional`, `group_fp02_blog_post_article_meta`).
2. Seed-контент (posts/categories) для QA archive/single.
3. Управляемое переключение `blog_public` только после evidence gate.
4. Сохранение канонического namespace `"/blog/"` во всех маршрутных слоях.

## Риски вне E26 acceptance

- WPilot metadata deployment (future-only область).
- Массовая очистка obsolete pages (E27).
- Пересмотр модели контента (CPT-интродукция).

## Dependency-to-wave matrix

| Dependency | E26A | E26B | E26C | E26D |
|---|---|---|---|---|
| Institutional ACF schema | Required | Optional | Optional | Verified |
| Permalink lock (`/blog/%postname%/`) | Optional | Required | Required | Verified |
| Blog templates readiness | Optional | Required | Required | Verified |
| Seed data | Optional | Optional | Optional | Required |
| Evidence bundle | Optional | Optional | Optional | Required |

## Вывод

Критический риск-профиль E26 сосредоточен в route policy и template completeness. При соблюдении wave sequencing и gating-механики риски остаются управляемыми.
