# FP-0002 V9-06E26 Final Architecture Contract v1

## Статус контракта

**PASS (conditional-execution-ready)** — архитектурная рамка подтверждена, при явных известных гэпах перед implementation closeout.

## Источники валидации

- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/final-e26-architecture-contract.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/final-verdict.json`
- `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/no-scope-drift-validation.json`

## Contract invariants

1. Task identifier для артефактов: `V9-06E26`.
2. Канонический archive route: `"/blog/"`.
3. Канонический single route pattern: `"/blog/%postname%/"`.
4. Тип статьи: только стандартный WP `post`.
5. WPilot future fields: вне implementation scope E26.

## Required artifact bundle

- Route inventory и WP data inventory.
- Архитектурные аудиты (blog + about).
- План волн, карта рисков/зависимостей, acceptance criteria.
- Документы no-scope-drift и final verdict.

## Execution guardrails

- Запрет fallback/alias на `"/articles/"`.
- Запрет closeout на skeleton-шаблонах.
- Запрет приемки без seed-базированной верификации.
- Запрет CPT-эскалации в рамках E26.

## Известные blocking gaps

| GAP | Текущее состояние | Требуемое действие |
|---|---|---|
| Permalink structure | `/%postname%/` | Перевести на `"/blog/%postname%/"` |
| Blog templates | skeleton/placeholder | Production implementation (E26B/E26C) |
| About hub `/o-centre/` | missing 12 sections | Полное покрытие (E26A) |
| Content dataset | `posts_count=0` | Seed в E26D |

## Зафиксированные mismatch/legacy элементы

- Draft `746`: документирован в E25A, отсутствует по E26 probe (`get_post(746)=null`).
- Obsolete страницы для E27 cleanup: `10`, `17`, `21`, `25`.

## Вне контракта E26

- Реализация WPilot metadata (future only).
- E27 cleanup obsolete pages.
- Любые изменения beyond архитектурного и контентного плана E26.

## Recommended next action

`CREATE_V9_06E26A_ABOUT_PAGE_WORDPRESS_ACF_PORT_TASK`

## Заключение

Контракт E26 валиден и пригоден к исполнению: route-модель, field-модель и wave sequencing согласованы, при обязательном соблюдении blocking conditions и guardrails.
