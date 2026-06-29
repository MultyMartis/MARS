# WPilot ChangeSet v1

**Classification:** Change management layer — unit of change execution.
**Status:** Documented v1; logical model only.
**Related:** [WPILOT-MISSION-v1.md](WPILOT-MISSION-v1.md), [WPILOT-OPERATIONS-MANIFEST-v1.md](WPILOT-OPERATIONS-MANIFEST-v1.md), [WPILOT-RISK-CLASSES-v1.md](WPILOT-RISK-CLASSES-v1.md), [WPILOT-TARGET-REGISTRY-v1.md](WPILOT-TARGET-REGISTRY-v1.md)

---

## Purpose

В WPilot **ChangeSet** — основная единица изменения.

Операции из [Operations Manifest](WPILOT-OPERATIONS-MANIFEST-v1.md) **не выполняются напрямую** как произвольное действие на сайте. Конкретное изменение оформляется и проходит жизненный цикл **через ChangeSet**.

ChangeSet является **контейнером изменения**. Он описывает:

| Аспект | Что фиксирует ChangeSet |
|--------|-------------------------|
| **Что меняется** | `target_type`, `target_id`, привязка к `operation_id` |
| **Почему меняется** | `description`, контекст запроса оператора |
| **Какой риск** | `risk_class` (из [Risk Classes](WPILOT-RISK-CLASSES-v1.md)) |
| **Какой backup** | `backup_required`, evidence backup path |
| **Какая проверка** | `validation_required`, evidence validation result |
| **Какой rollback** | `rollback_available`, evidence rollback source |

**ChangeSet не равен реализации.**

Наличие ChangeSet в модели v1 **не означает**, что существует БД, API, runtime, плагин или автоматизированный workflow. ChangeSet — логическая запись о том, **как конкретное изменение должно быть подготовлено, одобрено, выполнено, проверено и закрыто** в human-supervised модели WPilot.

---

## ChangeSet Lifecycle

Типичный успешный путь:

```
Draft
   ↓
Approval
   ↓
Backup
   ↓
Apply
   ↓
Validate
   ↓
Close
```

Путь с откатом после неудачной валидации или по решению оператора:

```
Draft
   ↓
Approval
   ↓
Backup
   ↓
Apply
   ↓
Validate
   ↓
Rollback
   ↓
Close
```

| Стадия | Назначение |
|--------|------------|
| **Draft** | ChangeSet создан; зафиксированы цель, операция, риск и намерение изменения. Состояние сайта ещё не меняется. |
| **Approval** | Оператор (или назначенный approval owner) явно одобрил выполнение с учётом `risk_class`. |
| **Backup** | Создан или подтверждён backup до apply, если `backup_required` = yes. |
| **Apply** | Одобренное изменение применено к цели через соответствующую `operation_id`. |
| **Validate** | Пост-apply проверка: факт изменения, целостность, видимость, отсутствие регрессий. |
| **Rollback** | Восстановление к состоянию до apply при сбое, регрессии или отказе оператора. |
| **Close** | ChangeSet завершён; evidence зафиксирован; дальнейшие стадии не требуются. |

**Не каждый ChangeSet проходит все стадии.**

- Read-only или inspection-only сценарии могут не порождать apply-ChangeSet.
- Draft-only операции (R1) могут завершаться на Draft без Apply до появления отдельного apply-ChangeSet.
- Rollback применяется только когда `rollback_available` = yes и оператор инициирует откат.

Согласование с Mission Charter: human-supervised, backup-first, validation-first, rollback-capable, evidence-driven.

---

## Required Fields

Канонический минимальный набор полей ChangeSet v1:

| Field | Type / format | Required | Description |
|-------|---------------|----------|-------------|
| **changeset_id** | string (stable id) | yes | Уникальный идентификатор ChangeSet (kebab-case или UUID; без пробелов). |
| **created_at** | ISO 8601 datetime | yes | Момент создания ChangeSet. |
| **status** | enum (см. Status Model) | yes | Текущая стадия жизненного цикла. |
| **operation_id** | string | yes | Ссылка на операцию из Operations Manifest v1. Должна быть конкретной; umbrella `apply_change` без subtype **не допускается**. |
| **risk_class** | R0 \| R1 \| R2 \| R3 \| R4 \| R5 | yes | Класс риска по Risk Classes v1 для данного run. |
| **target_type** | enum (см. Target Types) | yes | Тип цели изменения. |
| **target_id** | string | yes | Идентификатор цели: slug, ID, zone name, fragment key и т.д. |
| **description** | string | yes | Что и зачем меняется; контекст для оператора и audit trail. |
| **approval_required** | yes \| no | yes | Требуется ли явное одобрение до Apply (по risk class и policy). |
| **backup_required** | yes \| no | yes | Требуется ли backup до Apply. |
| **rollback_available** | yes \| no | yes | Доступен ли путь отката после Apply. |
| **validation_required** | yes \| no | yes | Обязательна ли пост-apply проверка. |

### Recommended optional fields

| Field | Description |
|-------|-------------|
| **site_id** | Идентификатор сайта / site passport reference. |
| **environment** | DEV / staging / production hint; production требует явного operator confirmation для R4. |
| **approved_at** | Timestamp одобрения. |
| **approved_by** | Оператор или approval owner (без секретов). |
| **backup_path** | Ссылка на backup evidence (может быть вне репозитория). |
| **validation_result** | Ссылка или краткий итог validation. |
| **rollback_source** | Источник для отката (backup id, snapshot path, pre-apply state ref). |
| **closed_at** | Timestamp закрытия ChangeSet. |
| **failure_reason** | При `status` = failed — причина отказа или сбоя. |
| **parent_changeset_id** | Связь draft-ChangeSet → apply-ChangeSet, если разделены. |

---

## Target Types

Канонический источник допустимых значений `target_type` — [Target Registry v1](WPILOT-TARGET-REGISTRY-v1.md). ChangeSet v1 использует полный enum из реестра.

Минимальный набор `target_type` в v1 (синхронизирован с Target Registry):

| target_type | Примеры `target_id` | Типичные операции |
|-------------|---------------------|-------------------|
| **page** | `contacts`, `page_id:42` | `inspect_page`, `draft_page_change`, `apply_content_change` |
| **post** | `news-item-slug`, `post_id:17` | `inspect_post`, `draft_content_change`, `apply_content_change` |
| **shortcode** | `footer_contacts`, `hero_block_1` | `inspect_shortcode`, `draft_shortcode_change`, `apply_shortcode_change` |
| **widget** | `sidebar-1:text-3` | `inspect_widget`, `draft_widget_change` |
| **menu** | `primary`, `footer-nav` | `inspect_menu`, `draft_menu_change`, `apply_menu_change` |
| **header** | `site-header`, `header-main` | `inspect_header`, `draft_header_change` (future) |
| **footer** | `site-footer`, `footer-contacts-zone` | `inspect_footer`, `draft_footer_change`, `apply_footer_change` |
| **css_fragment** | `child-theme:footer-patch`, `page-local:contacts` | `inspect_css`, `draft_css_change`, `apply_css_change` |
| **theme_option** | `the7_footer_layout` | `inspect_theme_option` (read-only в Manifest v1) |
| **media** | `attachment_id:128`, `media:hero-banner.webp` | `inspect_media` |
| **site** | `site-dev`, `site_passport:triumph-dev` | `inspect_site` |
| **environment** | `wp_version`, `indexing`, `dev_prod_hint` | `inspect_environment` |

Правила:

- `target_type` **должен** быть одним из canonical `target_id` из [Target Registry v1](WPILOT-TARGET-REGISTRY-v1.md).
- Одна apply-операция в одном ChangeSet привязана к **одной именованной цели** (или явно ограниченному набору, зафиксированному в `description`).
- Цель должна быть идентифицируема до стадии Apply.
- Массовые или неограниченные цели **не входят** в ChangeSet v1.
- Новые `target_type` вне этого enum — только через обновление Target Registry (charter review); ChangeSet не расширяет реестр самостоятельно.

---

## Status Model

Канонические значения `status`:

| status | Meaning |
|--------|---------|
| **draft** | ChangeSet создан; изменение описано, но не одобрено и не применено. |
| **approved** | Явное одобрение получено; можно переходить к backup (если требуется) или apply. |
| **backup_completed** | Backup создан или подтверждён; готовность к apply. |
| **applied** | Изменение применено к цели. |
| **validated** | Пост-apply проверка успешно завершена. |
| **rolled_back** | Откат выполнен после apply. |
| **closed** | ChangeSet завершён (успех, откат или осознанное закрытие без apply). |
| **failed** | Выполнение прервано: отказ, ошибка, невыполненные требования policy (нет backup, нет approval, blocked operation). |

Типичные переходы:

```
draft → approved → backup_completed → applied → validated → closed
draft → approved → backup_completed → applied → validated → rolled_back → closed
draft → failed
approved → failed
backup_completed → failed
applied → failed
validated → rolled_back → closed
```

Статус `validated` может предшествовать `closed` без промежуточного `rolled_back` при успешном завершении.

---

## ChangeSet Example

### Footer Menu Change

Иллюстративный пример apply-ChangeSet.

```
changeset_id:       cs-2026-06-19-footer-menu-001
created_at:         2026-06-19T14:30:00+03:00
operation_id:       apply_footer_change
risk_class:         R2
target_type:        shortcode
target_id:          footer_contacts
description:        Обновить контактный блок в footer без изменения остальной структуры.
approval_required:  yes
backup_required:    yes
rollback_available: yes
validation_required: yes
status:             validated
```

Рекомендуемые evidence fields для полного run:

| Field | Example value |
|-------|---------------|
| **backup_path** | `X:\AI MARS\backups\wpilot\site-dev\2026-06-19-footer-contacts-pre-apply.json` |
| **validation_result** | `validate_change: footer contacts visible, no layout regression` |
| **rollback_source** | тот же `backup_path` |

---

## Relationship To Operations Manifest

| Слой | Вопрос |
|------|--------|
| **Operations Manifest** | **Что делать?** — каталог `operation_id`, категории (Inspection / Draft / Apply / Recovery), scope, forbidden list. |
| **ChangeSet** | **Как конкретно выполняется изменение?** — экземпляр run: цель, риск, approval, backup, apply, validate, rollback, evidence, статус. |

Связь:

- `operation_id` в ChangeSet **должен** ссылаться на операцию из Approved Operations v1.
- ChangeSet **не добавляет** новых операций; новые `operation_id` появляются только через обновление Manifest.
- Inspection-only операции (R0) обычно **не требуют** полного apply-ChangeSet; результат inspect может породить отдельный draft- или apply-ChangeSet.
- `apply_change` (umbrella) **не может** быть `operation_id` ChangeSet без разрешения в конкретный subtype.

Operations Manifest описывает **тип** действия. ChangeSet описывает **конкретный экземпляр** этого действия на именованной цели с полным operational trail.

---

## Relationship To Risk Classes

[Risk Classes v1](WPILOT-RISK-CLASSES-v1.md) определяют **policy expectations** по классу риска:

| Risk Class | Approval | Backup | Validation | Rollback |
|------------|----------|--------|------------|----------|
| **R0** | Упрощённый контроль | Нет | Опционально | Нет |
| **R1** | Review перед Apply | Нет | Рекомендуется | Нет |
| **R2** | Обязателен до Apply | Обязателен | Обязательна | Должен быть возможен |
| **R3** | Явный approval | Обязателен | Обязательна | Обязателен |
| **R4** | Explicit approval + confirmation | Обязателен | План validation | План rollback до execute |
| **R5** | Prohibited | — | — | — |

ChangeSet **хранит результат выполнения** этих требований для конкретного run:

- `risk_class` — привязка к policy;
- `approval_required`, `backup_required`, `rollback_available`, `validation_required` — ожидаемые флаги (обычно выводимые из risk class, но фиксируемые явно);
- `status` и evidence fields — фактическое состояние выполнения.

ChangeSet с `risk_class` = R5 или с forbidden `operation_id` считается **невалидным** и должен перейти в `failed` без Apply.

---

## Evidence Expectations

Каждый ChangeSet **должен по возможности** иметь ссылки на evidence:

| Evidence type | Typical field | Description |
|---------------|---------------|-------------|
| **Backup** | `backup_path` | Путь к snapshot, export или plugin-created backup до apply. |
| **Validation** | `validation_result` | Итог `validate_change` или operator checklist; ссылка на отчёт. |
| **Rollback** | `rollback_source` | Источник для `rollback_change` или `restore_backup`. |

Evidence **может храниться вне репозитория**.

Примеры допустимых расположений (operator machine, не commit targets):

```text
X:\AI MARS\backups\wpilot\
X:\AI MARS\local\runtime\
X:\AI MARS STORAGE\wpilot\evidence\
```

См. также [local-storage-policy.md](local-storage-policy.md): `/backups/` и `/local/` исключены из git.

Evidence-driven принцип из Mission Charter: audit-friendly trail без хранения секретов, credentials или `wp-config.php` в репозитории.

---

## Notes

- ChangeSet v1 описывает **логическую модель** единицы изменения WPilot.
- **Не требует** существования БД, API, runtime, approval engine или automated enforcement.
- Human-supervised model сохраняется: WPilot не получает автономного authority над WordPress.
- ChangeSet **не заменяет** Operations Manifest, Risk Classes или Mission Charter.
- Шаблон [change-request-template.md](templates/change-request-template.md) может использоваться оператором **до** формализации ChangeSet; ChangeSet — каноническая структура для execution trail.
- Следующие слои (вне scope v1): bindings к plugin REST, Cursor workflow, dashboards — отдельные документы.

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v1 |
| Implements runtime | No |
| Replaces Operations Manifest | No |
| Replaces Risk Classes | No |
| Replaces Mission Charter | No |
