# FP-0002 V9-06E26 Blog Strategic Architecture Audit v1

## Цель

Определить целевую стратегическую архитектуру блога в WP в рамках E26 и зафиксировать обязательные технические решения без scope drift.

## Источники валидации

- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/blog-strategic-architecture-audit.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/current-wp-route-and-data-inventory.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/final-e26-architecture-contract.json`

## Стратегические решения (утвержденные)

1. Используется стандартный тип `post` как каноническая статья.
2. Article CPT в E26 **не вводится**.
3. Архив блога привязан к `page_for_posts=19` с каноническим маршрутом `"/blog/"`.
4. Метаданные статьи рендерятся через `group_fp02_blog_post_article_meta`.

## Канонический маршрутный контракт

- Archive: `"/blog/"`
- Single: `"/blog/%postname%/"`
- Legacy route `"/articles/"`: нецелевой и должен быть исключен из SEO/каноникал/внутренних ссылок.

## Архитектурные гэпы на текущем состоянии

- `permalink_structure` не соответствует целевому (`/%postname%/` вместо `"/blog/%postname%/"`).
- `home.php` и `single.php` находятся на уровне skeleton.
- `article-content` и `article-lower-stack` являются placeholder-блоками.
- Нет seeded-постов и категорий для верификации полноты archive/single.
- `blog_public=0` блокирует индексирование до закрытия delivery-гейта.

## Обязательные remediation-шаги

| Приоритет | Действие | Ожидаемый эффект |
|---|---|---|
| P0 | Переключить permalink на `"/blog/%postname%/"` | Маршрутная консистентность V9/WP |
| P0 | Довести archive/single шаблоны до production parity | Рендер без placeholder |
| P1 | Ввести seed-датасет постов и категорий | QA на реальных данных |
| P1 | Проверить canonical/meta breadcrumbs в namespace `"/blog/"` | SEO-корректность |
| P2 | Подготовить evidence bundle E26D | Управляемый closeout |

## Non-goals E26

- Внедрение WPilot metadata (только future planning).
- Миграция/очистка obsolete pages E27 (`10, 17, 21, 25`) в рамках E26.
- Введение новой модели контента вне standard `post`.

## Вывод аудита

Стратегическая архитектура блога согласована и непротиворечива, но исполнение остается условным до устранения маршрутного mismatch и заполнения данных для полноценных archive/single проверок.
