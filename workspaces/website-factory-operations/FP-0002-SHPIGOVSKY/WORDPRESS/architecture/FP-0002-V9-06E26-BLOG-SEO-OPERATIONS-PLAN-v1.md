# FP-0002 V9-06E26 Blog SEO Operations Plan v1

## Цель

Описать безопасный SEO-план включения блогового контура после завершения архитектурной и шаблонной части E26.

## Источники валидации

- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/blog-seo-operations-plan.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/current-wp-route-and-data-inventory.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/final-verdict.json`

## SEO control points (обязательные)

1. Переключить permalink на `"/blog/%postname%/"`.
2. Включать индексирование только после production-ready archive/single.
3. Заполнить taxonomy (категории) для исключения пустой архивации.
4. Проверить canonical URL исключительно в namespace `"/blog/"`.

## Prelaunch checks

| Проверка | Критерий PASS |
|---|---|
| `blog_public` | До E26D завершения остается `0` |
| Маршруты | `"/blog/"` и `"/blog/<postname>/"` возвращают HTTP 200 |
| Контент | Нет thin placeholder-страниц |
| Шаблоны | `home.php` / `single.php` production-ready |
| Каноникал | Нет ссылок/каноникалов на `"/articles/"` |

## Пострелизные операции

- Регенерация sitemap с включением блоговых маршрутов.
- Мониторинг первичной индексации и crawl anomalies.
- Контроль качества блока `related_posts` после первой редакторской публикации.

## Синхронизация с E26 волнами

- E26A: prerequisite для non-service parity.
- E26B/C: подготовка SEO-ready archive/single слоя.
- E26D: seed + smoke + evidence; только после этого возможен переход к `blog_public=1` (операторское решение).

## Scope boundaries

- WPilot metadata: future only, не блокирует SEO launch gate E26.
- E27 obsolete page cleanup (`10, 17, 21, 25`): отдельный поток.
- Миграции контент-модели вне standard `post`: вне данного плана.

## Вывод

SEO-включение блога должно быть строго по gate-модели: сначала маршруты и шаблоны, затем данные и проверки, и только после доказательств E26D допускается включение crawl/index.
