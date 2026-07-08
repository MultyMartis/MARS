# FP-0002 V9-06E26 Field Model Proposal v1

## Цель

Предложить устойчивую field-модель для E26, используя существующие ACF-группы без изменения базовой контентной типизации WordPress.

## Источники валидации

- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/field-model-proposal.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/about-page-architecture-audit.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/blog-strategic-architecture-audit.json`

## Доступные группы (as-is)

### 1) `group_fp02_page_institutional`

- Статус: существует.
- Подтвержденные блоки: hero + repeaters.
- Роль в E26: primary data model для `/o-centre/` и секционного наполнения.

### 2) `group_fp02_blog_post_article_meta`

- Статус: существует.
- Подтвержденные поля: `source_label`, `reading_time`, `disclaimer`, `author_flag`, `date_flag`, `related_posts`.
- Роль в E26: metadata contract для стандартного post single.

## Предлагаемые расширения (без scope drift)

1. Для institutional: зафиксировать детерминированную структуру repeaters на 12 V9 секций.
2. Для blog post meta: определить fallback-правила для пустых редакторских значений.
3. Добавить формальные правила валидации:
   - `reading_time`: предсказуемый формат (например, `N мин`).
   - `source_label`: ограничение формата и длины.
   - `related_posts`: фильтр только на publish-сущности.

## Поля вне текущего acceptance gate

- WPilot metadata fields:
  - planned: `true`
  - implemented_now: `false`
  - В E26 не используются как блокирующий критерий приемки.

## Контрактная модель рендера

- Тип статьи: стандартный `post`.
- Meta слой single-страницы: берется из `group_fp02_blog_post_article_meta`.
- Institutional-страница: секции рендерятся через repeaters `group_fp02_page_institutional`.
- Запрещено: ввод article CPT в E26.

## Риски и меры

| Риск | Влияние | Мера |
|---|---|---|
| Неопределенные repeaters для 12 секций | Высокое | Зафиксировать схему до E26A implementation |
| Пустые article meta поля | Среднее | Ввести fallback-механику и editorial guide |
| Потенциальная регрессия E24 `hero_cta_label` | Среднее | Включить в regression checklist E26A |

## Вывод

Существующих ACF-групп достаточно для E26 при условии формализации repeater-схемы institutional и единых fallback/validation правил для article meta.
