# FP-0002 V9-06E26 Future Wave Acceptance Criteria v1

## Назначение

Документ фиксирует формальные критерии приемки по каждой волне E26 и единые правила закрытия архитектурного контракта.

## Источники валидации

- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/future-wave-acceptance-criteria.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/final-e26-architecture-contract.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/final-verdict.json`

## Acceptance criteria по волнам

### E26A — About / Institutional

- `"/o-centre/"` содержит все 12 обязательных V9 секций.
- ACF-контент отрисовывается без placeholder.
- Template-структура соответствует утвержденной архитектуре institutional.

### E26B — Blog Archive

- `"/blog/"` корректно работает как archive (через `page_for_posts=19`).
- Архив поддерживает empty/non-empty state.
- Каноникал и breadcrumbs строго в namespace `"/blog/"`.

### E26C — Blog Single

- Single-маршрут соответствует `"/blog/%postname%/"`.
- Article meta отрисовывается из ACF с fallback.
- Lower-stack блоки функциональны и не placeholder.

### E26D — Seed + Verification

- Seed включает репрезентативные посты и категории.
- Smoke-тесты archive/single проходят без деградаций.
- Evidence bundle фиксирует parity и открытые гэпы.

## Горизонтальные критерии (для всех волн)

1. Канонический блоговый маршрут: `"/blog/"`; `"/articles/"` не используется как целевой.
2. Тип статьи: стандартный `post`, без article CPT.
3. WPilot metadata не входит в acceptance gate E26.
4. Scope drift не допускается (ориентир: no-scope-drift validation).

## Критерии блокировки closeout

- Неисправленный permalink mismatch.
- Сохранение skeleton/placeholder в обязательных шаблонах.
- Отсутствие seed-данных к моменту финальной верификации.
- Неподтвержденная parity по `/o-centre/`.

## Вывод

Критерии приемки E26 прозрачны и измеримы: они позволяют закрывать каждую волну по наблюдаемым признакам и исключают формальное закрытие без реальной функциональной готовности.
