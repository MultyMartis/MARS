# FP-0002 V9-06E26 About Page Architecture Audit v1

## Цель

Зафиксировать архитектурное состояние и delivery-контракт для страницы `"/o-centre/"` и связанных дочерних страниц в рамках волны E26A.

## Источники валидации

- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/about-page-architecture-audit.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/field-model-proposal.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/future-wave-acceptance-criteria.json`

## Текущее состояние

- Целевая страница: `"/o-centre/"`.
- WP page ID: `11`.
- Шаблон: `institutional.php`.
- Реализовано: hero.
- Недостает: **12 обязательных V9 секций** на hub-странице.

## Дочерние страницы и связанный контур

- IDs `12-16` существуют как дочерние страницы раздела.
- Фактический контент на текущий момент placeholder.
- По V9 ожидается унифицированный контур `plain-page-content` для дочерних страниц.

## ACF-покрытие

| Группа | Статус | Что уже есть | Что требуется |
|---|---|---|---|
| `group_fp02_page_institutional` | exists | hero, repeaters | детерминированная схема 12 секций |
| `group_fp02_blog_post_article_meta` | exists | blog meta fields | используется в E26B/C, не в E26A |

Отдельное требование: поле `hero_cta_label` (контракт E24) не должно регрессировать при расширении институционального шаблона.

## Архитектурные риски для `/o-centre/`

1. Частичная реализация (`hero-only`) и визуальный разрыв относительно static V9.
2. Недоопределенная repeater-модель усложняет стабильный рендер секций.
3. Риск смешения hub и child шаблонов без явного контракта.

## Delivery contract для E26A

1. Реализовать все 12 отсутствующих V9 секций на `"/o-centre/"`.
2. Сохранить последовательность секций и контентную иерархию V9.
3. Подключить рендер строго через ACF-модель (без placeholder).
4. Проверить совместимость с дочерними страницами `12-16` и `plain-page-content`.
5. Не закрывать E26A без evidence parity по hub-странице.

## Зависимости

- Готовность шаблонной архитектуры (`institutional.php` + partials).
- Актуальная ACF-схема repeaters для секций.
- Наличие тестовых данных для визуальной и контентной проверки.

## Вывод

`/o-centre/` является главным функциональным блокером E26: именно его завершение создает безопасную базу для последующих волн блога и закрытия non-service гэпов.
