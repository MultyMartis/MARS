# FP-0002 V9-06E26 Current WP Route And Data Inventory v1

## Назначение

Документ описывает фактическое состояние маршрутов, данных и шаблонов в WordPress на момент V9-06E26. Это operational baseline для планирования волн E26A-E26D.

## Источники валидации

- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/current-wp-route-and-data-inventory.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/static-v9-route-inventory.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/no-scope-drift-validation.json`

## Snapshot WP probe (2026-07-08)

| Параметр | Значение | Оценка |
|---|---|---|
| `page_for_posts` | `19` | Корректно назначена страница архива |
| `permalink_structure` | `/%postname%/` | GAP относительно `"/blog/%postname%/"` |
| `blog_public` | `0` | Crawl закрыт до завершения E26 |
| `posts_count` | `0` | Нет материала для QA archive/single |
| `categories_count` | `1` (empty) | Таксономия без контента |

## Инвентарь маршрутов и сущностей

- Канонический маршрут блога по контракту: `"/blog/"` (не `"/articles/"`).
- Тип контента для статей: стандартный `post`.
- Article CPT отсутствует и не должен вводиться в E26.
- Статус портирования:
  - Уже портировано: homepage, services tree, contacts, reviews, legal shells.
  - Незавершено: `/o-centre/`, `/blog/`, `/blog/<postname>/`.

## Текущее состояние шаблонов

| Шаблон/блок | Текущее состояние | Риск |
|---|---|---|
| `home.php` | skeleton | Архив блога без production-паритета |
| `single.php` | skeleton | Single без production-паритета |
| `article-content` | placeholder | Контентная часть статьи не реализована |
| `article-lower-stack` | placeholder | Нижний стек статьи не реализован |
| `blog-archive-card` | placeholder | Карточки архива не production-ready |
| `institutional.php` | hero-only | `/o-centre/` неполный по V9 |

## О-центре и дочерние страницы

- Hub `"/o-centre/"`: страница ID `11`, шаблон `institutional.php`, hero работает, но **12 V9 секций отсутствуют**.
- Дочерние страницы (IDs `12-16`): сейчас placeholder-содержимое; в V9 ожидается контур `plain-page-content`.

## ACF и модель данных

- `group_fp02_page_institutional`: существует, покрывает hero и repeaters; покрытие частичное.
- `group_fp02_blog_post_article_meta`: существует, пригоден для article meta.
- `hero_cta_label` в контексте E24 уже зафиксирован и должен быть сохранен.

## Зафиксированные mismatches

1. Draft `746`: в E25A документирован, в E26 probe `get_post(746)=null`.
2. Obsolete страницы для E27 cleanup backlog: IDs `10`, `17`, `21`, `25`.
3. WPilot metadata: только future plan, не текущая реализация.

## Вывод

WP находится в состоянии **conditional-execution-ready** для E26: архитектурная рамка подтверждена, но запуск производственной волны требует устранения permalink mismatch, завершения skeleton-шаблонов и seed-контента для QA.
