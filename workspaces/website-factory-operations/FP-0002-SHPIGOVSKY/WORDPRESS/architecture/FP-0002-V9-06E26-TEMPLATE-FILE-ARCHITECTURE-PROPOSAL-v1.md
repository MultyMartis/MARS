# FP-0002 V9-06E26 Template File Architecture Proposal v1

## Цель

Определить целевую файловую топологию шаблонов для `"/o-centre/"` и блогового контура `"/blog/"` в рамках E26.

## Источники валидации

- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/template-file-architecture-proposal.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/current-wp-route-and-data-inventory.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/final-e26-architecture-contract.json`

## Целевая топология шаблонов

### Institutional контур

- `institutional.php`
- `partials/institutional/hero.php`
- `partials/institutional/section-*`

### Blog archive контур

- `home.php`
- `partials/blog/archive-loop.php`
- `partials/blog/archive-empty.php`

### Blog single контур

- `single.php`
- `partials/article-content.php`
- `partials/lower-stack.php`

## Правила архитектуры шаблонов

1. `"/blog/"` должен резолвиться через archive-контекст `home.php` (при `page_for_posts=19`).
2. `single.php` обязан формировать рендер для `"/blog/%postname%/"`.
3. Article meta рендер централизуется, чтобы исключить дубли между archive teaser и single.
4. Любые placeholder partials подлежат замене на production-реализацию в E26B/E26C.

## Обязательные изменения

- Замена placeholder-контента в `article-content`, `article-lower-stack`, `blog-archive-card`.
- Расширение `institutional.php` с hero-only до полного секционного стека.
- Явная поддержка archive empty-state и non-empty state в blog loop.

## Ограничения

- Без Article CPT.
- Без aliasing маршрутов на `"/articles/"`.
- Без включения WPilot metadata в acceptance E26.

## Проверяемые инварианты

| Инвариант | Ожидание |
|---|---|
| Route namespace | Только `"/blog/"` |
| Post type | Только стандартный `post` |
| Template readiness | Нет skeleton/placeholder в финальном контуре |
| ACF rendering | Детерминированный, тестируемый |

## Вывод

Предложенная топология минимально достаточна для полного E26-покрытия и не нарушает существующие ограничения проекта: стандартный WP post, канонический `/blog/` namespace, phased delivery по E26A-E26D.
