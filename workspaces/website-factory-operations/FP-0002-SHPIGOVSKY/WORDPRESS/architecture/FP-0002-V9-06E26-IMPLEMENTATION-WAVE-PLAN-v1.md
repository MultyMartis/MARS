# FP-0002 V9-06E26 Implementation Wave Plan v1

## Цель

Определить исполнимый порядок волн E26A-E26D с зависимостями, контрольными точками и ожидаемыми артефактами валидации.

## Источники валидации

- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/implementation-wave-plan.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/future-wave-acceptance-criteria.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/risk-and-dependency-map.json`

## План волн

| Wave | Название | Область | Статус |
|---|---|---|---|
| E26A | o-centre page implementation | `institutional.php`, 12 отсутствующих секций, ACF repeaters | planned |
| E26B | blog archive implementation | `home.php`, архив `/blog/`, empty-state и карточки | planned |
| E26C | blog single implementation | `single.php`, article meta, lower stack | planned |
| E26D | demo seed and verification | seed posts/categories, smoke, evidence pack | planned |

## Последовательность и зависимости

1. **E26A first**: закрывает крупнейший structural gap non-service страниц.
2. **Permalink policy lock** (`"/blog/%postname%/"`) обязателен до полноценного выполнения E26B/E26C.
3. **E26B и E26C** могут идти частично параллельно только после фикса route policy.
4. **E26D** стартует только когда archive/single production-complete и без placeholder.

## Deliverables по волнам

- E26A: parity-реализация `/o-centre/`, подтверждение 12 секций.
- E26B: рабочий архив `"/blog/"` на `page_for_posts=19`.
- E26C: рабочий single по паттерну `"/blog/%postname%/"`.
- E26D: набор demo-сущностей + доказательная валидация маршрутов и шаблонов.

## Контрольные гейты

| Gate | Проверка |
|---|---|
| G1 | `/o-centre/` содержит все 12 V9 секций |
| G2 | `permalink_structure` соответствует `"/blog/%postname%/"` |
| G3 | Archive/single не содержат placeholder-блоков |
| G4 | Seed данных достаточно для QA сценариев |
| G5 | `blog_public` переключается только после evidence gate |

## Explicit deferrals

- WPilot metadata fields: планируются на future wave, вне E26 acceptance.
- E27 obsolete cleanup (IDs `10`, `17`, `21`, `25`): отдельный backlog.
- Любые изменения модели контента вне `post`: вне E26 scope.

## Вывод

План волн E26 валиден: он закрывает критические architectural gaps по принципу сначала структура (`o-centre`), затем блоговые маршруты/шаблоны, затем seed и доказательства.
