# WPilot Risk Classes v1

**Classification:** Policy layer — risk taxonomy for typed operations.
**Status:** Documented v1; policy model only.
**Related:** [WPILOT-MISSION-v1.md](WPILOT-MISSION-v1.md), [WPILOT-OPERATIONS-MANIFEST-v1.md](WPILOT-OPERATIONS-MANIFEST-v1.md), [WPILOT-TARGET-REGISTRY-v1.md](WPILOT-TARGET-REGISTRY-v1.md)

---

## Purpose

[Operations Manifest](WPILOT-OPERATIONS-MANIFEST-v1.md) определяет **какие** операции существуют в модели WPilot: `operation_id`, категории, scope, lifecycle.

**Risk Classes** определяют **насколько опасна** каждая операция — уровень риска для политики, а не для реализации.

Risk Classes **не определяют**:

- реализацию в плагине, REST API или runtime;
- конкретные endpoint'ы;
- автоматическое enforcement;
- наличие approval engine, backup subsystem или rollback automation.

Risk Classes **используются для**:

- **approval rules** — какой уровень человеческого контроля ожидается;
- **validation requirements** — когда обязательна пост-проверка или dry-run;
- **rollback expectations** — когда откат или backup evidence обязателен;
- **operational decisions** — эскалация, отказ, выбор workflow.

Наличие risk class в этом документе **не означает**, что соответствующие guardrails уже реализованы.

---

## Risk Model Overview

| Risk Class | Name | Description |
|------------|------|-------------|
| **R0** | Read Only | Операции, не изменяющие состояние сайта. Только инспекция и чтение. |
| **R1** | Draft Only | Создание предложений изменений без применения к live-состоянию. |
| **R2** | Scoped Content Change | Локальные изменения ограниченного контента в явно заданном scope. |
| **R3** | Site Configuration Change | Изменения конфигурации сайта, навигации, восстановления или отката на уровне, затрагивающем структуру сайта. |
| **R4** | Production Critical | Операции, способные затронуть весь сайт, домен или бизнес-функции; требуют максимального контроля. |
| **R5** | Forbidden | Операции вне разрешённой модели WPilot; не должны выполняться. |

Шкала **монотонна по воздействию**: R0 < R1 < R2 < R3 < R4. Класс R5 — вне допустимой модели, не «следующий уровень» после R4.

---

## R0 — Read Only

### Описание

Операции, **не изменяющие** состояние WordPress: контент, настройки, файлы, БД, плагины, темы.

Типичные стадии lifecycle: **Inspect** (и опционально **Validate** для сверки с ожиданием без мутации).

### Примеры (из Manifest v1)

- `inspect_page`
- `inspect_shortcode`
- `inspect_widget`
- `inspect_menu`
- `inspect_environment`
- `inspect_site`, `inspect_post`, `inspect_theme_option`, `inspect_plugin`, `inspect_media`, `inspect_footer`, `inspect_header`, `inspect_css`
- `validate_change` — read-only recovery/verification: не изменяет состояние сайта

### validate_change (R0)

`validate_change` does not modify site state.

It validates post-apply state, rendered output, expected markers, links, or health checks.

It may be part of a higher-risk workflow, but the validation operation itself is read-only.

### Требования

| Требование | Ожидание |
|------------|----------|
| Backup | Не требуется |
| Rollback | Не требуется |
| Validation | Опционально (сверка фактов) |
| Approval | Может быть **упрощённым** — аутентификация и доступ оператора достаточны; явное pre-apply approval не применяется, т.к. apply отсутствует |

Human-supervised модель сохраняется: оператор инициирует и несёт ответственность за доступ, но операция сама по себе не создаёт write-risk.

---

## R1 — Draft Only

### Описание

Создание **предложений** изменений: diff, dry-run, план, черновик — **без применения** к live-состоянию.

Ничего не коммитится в production-контент до отдельной Apply-операции с соответствующим risk class и approval.

### Примеры (из Manifest v1)

- `draft_page_change`
- `draft_footer_change`
- `draft_css_change`
- `draft_shortcode_change`, `draft_menu_change`, `draft_widget_change`, `draft_content_change`

### Требования

| Требование | Ожидание |
|------------|----------|
| Изменение состояния | **Ничего не изменяется** на сайте |
| Backup | Не требуется |
| Rollback | Не требуется |
| Validation | Рекомендуется для качества плана (dry-run integrity) |
| Approval | Оператор **инициирует** draft; отдельное pre-draft approval не обязательно, но результат draft требует review перед Apply |

---

## R2 — Scoped Content Change

### Описание

**Локальные** изменения **ограниченного** контента: одна именованная цель или явно ограниченный фрагмент в допустимом scope Manifest v1.

Не затрагивает глобальную конфигурацию сайта (menus site-wide, theme options, domain settings).

### Примеры (из Manifest v1)

- `apply_shortcode_change`
- `apply_content_change`
- `apply_footer_change`
- `apply_css_change` (scoped `css_fragment` only — см. ниже)

### apply_css_change (scope escalation)

`apply_css_change` is **R2** only when scoped to an isolated CSS fragment or page-local raw HTML/CSS.

Site-wide child theme CSS change escalates to **R3** or **R4** depending on environment and impact.

### Требования

| Требование | Ожидание |
|------------|----------|
| Backup | **Обязателен** перед apply |
| Validation | **Обязательна** после apply (или как отдельная `validate_change`) |
| Rollback | **Должен быть возможен** (plugin-created backup или operator-verified path) |
| Approval | **Обязателен** до Apply (Mission Charter: human-supervised write-like actions) |
| Scope | Одна именованная цель; массовые или неограниченные цели **не допускаются** |

### Типичные цели (targets)

Канонические `target_id` — [Target Registry v1](WPILOT-TARGET-REGISTRY-v1.md).

- `page` / `post` (field-level content)
- `shortcode`
- `widget` (при появлении соответствующей apply-операции в будущих версиях Manifest)
- `footer` (footer zone)
- `css_fragment` (child theme / scoped patch)

---

## R3 — Site Configuration Change

### Описание

Изменения **конфигурации сайта** или **recovery-операций**, затрагивающих структуру, навигацию или восстановление состояния шире одного контентного фрагмента.

### Примеры (из Manifest v1 и policy)

- `apply_menu_change` — изменение меню навигации
- `rollback_change` — откат конкретного применённого изменения к состоянию до apply
- `apply_css_change` — когда scope выходит за isolated fragment (site-wide child theme CSS)

### Примеры (концептуальные, вне Manifest v1)

- изменение `theme_option` (write)
- изменение widgets (глобальная конфигурация)
- изменение site settings

### Требования

| Требование | Ожидание |
|------------|----------|
| Backup | **Обязателен** |
| Approval | **Обязателен** (явное человеческое одобрение) |
| Validation | **Обязательна** |
| Rollback | **Обязателен** — план отката или подтверждённый backup path до выполнения |

---

## R4 — Production Critical

### Описание

Операции, способные затронуть **весь сайт**, **домен** или **бизнес-функции** — независимо от того, входят ли они в Manifest v1.

### Примеры (из Manifest v1)

- `restore_backup` — восстановление из подтверждённого backup

### restore_backup (R4)

`restore_backup` can affect wide site state and must be treated as production-critical unless explicitly scoped to a single entity backup.

### Примеры (концептуальные)

- production-wide configuration
- domain-level settings
- deployment-related actions
- live publish без DEV-only gate
- SEO/indexing toggles на production (вне DEV isolation helper)
- `apply_css_change` — site-wide child theme CSS (environment-dependent escalation)

### Требования

| Требование | Ожидание |
|------------|----------|
| Explicit approval | **Обязателен** — отдельное подтверждение оператора с фиксацией scope |
| Rollback plan | **Обязателен** до выполнения |
| Validation plan | **Обязателен** — что и как проверяется после действия |
| Operator confirmation | **Обязателен** — production environment explicitly acknowledged |

### Важно

**R4 не означает запрет.**

R4 означает **повышенный контроль**: больше evidence, явный rollback plan, нет автономного выполнения. Операция может быть разрешена после human charter для конкретного run.

---

## R5 — Forbidden

### Описание

Операции, **не входящие** в разрешённую модель WPilot. Не получают валидный `operation_id` в Manifest v1.

### Примеры

| Forbidden pattern | Причина |
|-------------------|---------|
| `execute_arbitrary_sql` | Произвольный SQL; вне safety boundary |
| `execute_arbitrary_php` | Code execution |
| `delete_random_files` | Неограниченное удаление; нет scoped target |
| `unapproved_production_change` | Изменение без approval и backup evidence |
| `mass_content_rewrite` | Массовая перезапись; вне scoped replacement |
| `autonomous_update_operations` | plugin/theme/core auto-update; противоречит Mission non-goals |
| `plugin_auto_update`, `theme_auto_update`, `core_auto_update` | Как в Forbidden Operations Manifest v1 |

### Требование

**Операции R5 не должны выполняться WPilot.**

При запросе на подобное действие ожидается **refusal** (отказ), эскалация оператору, без расширения Manifest «по умолчанию».

---

## Operation Mapping v1

Привязка `operation_id` из [Operations Manifest v1](WPILOT-OPERATIONS-MANIFEST-v1.md) к risk class.

Поле **default risk** в Manifest (low / medium / high) — ориентировочная метка до Risk Classes; **risk class** ниже — каноническая policy-привязка v1.

### Inspection → R0

| operation_id | risk_class | Notes |
|--------------|------------|-------|
| `inspect_site` | R0 | |
| `inspect_page` | R0 | |
| `inspect_post` | R0 | |
| `inspect_shortcode` | R0 | |
| `inspect_widget` | R0 | |
| `inspect_menu` | R0 | |
| `inspect_theme_option` | R0 | Read-only |
| `inspect_plugin` | R0 | |
| `inspect_media` | R0 | |
| `inspect_footer` | R0 | |
| `inspect_header` | R0 | |
| `inspect_css` | R0 | Read-only |
| `inspect_environment` | R0 | |
| `validate_change` | R0 | Read-only post-apply verification |

### Draft → R1

| operation_id | risk_class | Notes |
|--------------|------------|-------|
| `draft_page_change` | R1 | |
| `draft_shortcode_change` | R1 | |
| `draft_footer_change` | R1 | |
| `draft_menu_change` | R1 | |
| `draft_widget_change` | R1 | |
| `draft_css_change` | R1 | |
| `draft_content_change` | R1 | |

### Apply

| operation_id | risk_class | Notes |
|--------------|------------|-------|
| `apply_content_change` | R2 | Scoped page/post field |
| `apply_shortcode_change` | R2 | Scoped shortcode fragment |
| `apply_footer_change` | R2 | Scoped footer zone |
| `apply_css_change` | R2 | Scoped css fragment only; site-wide child theme CSS → R3/R4 |
| `apply_menu_change` | R3 | Site navigation configuration |
| `apply_change` | SAFE UNKNOWN | Umbrella operation; blocked unless subtype resolved (см. Notes) |

### Recovery

| operation_id | risk_class | Notes |
|--------------|------------|-------|
| `validate_change` | R0 | Read-only post-apply verification; does not modify site state |
| `rollback_change` | R3 | Recovery / structural rollback path |
| `restore_backup` | R4 | Production-critical unless scoped to single entity backup |

### Forbidden → R5

Действия из раздела **Forbidden Operations** Manifest v1 не имеют `operation_id` и относятся к **R5**:

| Forbidden action | risk_class |
|------------------|------------|
| `execute_arbitrary_sql` | R5 |
| `execute_arbitrary_php` | R5 |
| `delete_random_files` | R5 |
| `mass_content_rewrite` | R5 |
| `plugin_auto_update` | R5 |
| `theme_auto_update` | R5 |
| `core_auto_update` | R5 |
| `unapproved_production_change` | R5 |

---

## Approval Expectations

Сводная матрица ожиданий по классам (policy layer; не автоматическое enforcement):

| Risk Class | Approval posture | Backup | Validation | Rollback |
|------------|------------------|--------|------------|----------|
| **R0** | Минимальный контроль: auth + operator initiation | Нет | Опционально | Нет |
| **R1** | Оператор инициирует; review перед Apply | Нет | Рекомендуется для плана | Нет |
| **R2** | Human approval **до Apply** | **Обязателен** | **Обязательна** | Должен быть **возможен** |
| **R3** | **Явный approval** | **Обязателен** | **Обязательна** | **Обязателен** (plan или path) |
| **R4** | **Explicit approval** + operator confirmation + documented plans | **Обязателен** | **План validation** | **План rollback** до execute |
| **R5** | **Prohibited** — выполнение не допускается | — | — | — |

Согласование с [Mission Charter](WPILOT-MISSION-v1.md): «All actions require human approval» интерпретируется как отсутствие **автономного authority** у WPilot. R0 допускает упрощённый контроль (нет pre-mutation approval), но не автономное выполнение без оператора.

---

## Relationship To Manifest

| Документ | Вопрос |
|----------|--------|
| **Operations Manifest** | «Что можно делать?» — каталог `operation_id`, категории, scope, lifecycle, forbidden list |
| **Risk Classes** | «Насколько это опасно?» — уровень риска, approval/backup/validation/rollback expectations |

Risk Classes **расширяют** Manifest, не заменяют его:

- Manifest без Risk Classes описывает операции без формальной шкалы риска.
- Risk Classes без Manifest не определяют допустимые операции.
- Изменение risk class **не должно** менять семантику `operation_id` без отдельного charter review.

Manifest v1 уже ссылается на отдельный документ Risk Classes; данный файл закрывает этот слой для v1.

---

## Notes

- Risk Classes описывают **policy layer** для human-operated WPilot workflows и будущих bindings (plugin, Cursor, dashboards).
- Они **не означают** наличие реализации approval engine, automated risk scoring или runtime enforcement.
- **`apply_change` → SAFE UNKNOWN (umbrella):** `apply_change` is an umbrella operation. It must not be executed directly without resolving to a specific subtype:
  - `apply_content_change`
  - `apply_shortcode_change`
  - `apply_footer_change`
  - `apply_menu_change`
  - `apply_css_change`
  If subtype cannot be resolved, operation is blocked.
- **`validate_change` → R0:** read-only verification; may follow a higher-risk apply workflow, but the validation operation itself does not mutate site state.
- **`restore_backup` → R4:** wide site state impact; production-critical unless explicitly scoped to a single entity backup.
- **`apply_css_change` scope rule:** R2 for isolated CSS fragment or page-local raw HTML/CSS; site-wide child theme CSS escalates to R3 or R4 depending on environment and impact.

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v1 |
| Implements runtime | No |
| Replaces Manifest | No |
| Replaces Mission Charter | No |
