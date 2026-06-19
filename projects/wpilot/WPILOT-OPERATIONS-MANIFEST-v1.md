# WPilot Operations Manifest v1

**Classification:** Operations layer — typed operation model.
**Status:** Documented v1; logical model only.
**Related:** [WPILOT-MISSION-v1.md](WPILOT-MISSION-v1.md), [WPILOT-RISK-CLASSES-v1.md](WPILOT-RISK-CLASSES-v1.md), [WPILOT-TARGET-REGISTRY-v1.md](WPILOT-TARGET-REGISTRY-v1.md)

---

## Purpose

В WPilot **Operation** (операция) — это типизированное действие с фиксированной семантикой, а не произвольное «сделать что-нибудь на сайте».

Каждая операция описывается набором обязательных атрибутов:

| Атрибут | Назначение |
|---------|------------|
| **operation_id** | Стабильный идентификатор операции (kebab-case, без пробелов). |
| **description** | Что делает операция и на какой результат нацелена. |
| **risk_class** | Класс риска по [Risk Classes v1](WPILOT-RISK-CLASSES-v1.md); в таблицах ниже — ориентировочный default risk (low / medium / high). |
| **approval requirement** | Требуется ли явное человеческое одобрение перед выполнением или применением. |
| **rollback expectation** | Ожидается ли путь отката после операции (да/нет). |
| **scope** | Допустимые типы целей (page, post, menu и т.д.). |

Manifest v1 фиксирует **какие** операции допустимы в модели WPilot. Наличие операции в Manifest **не означает**, что она уже реализована в плагине, workflow или runtime.

---

## Operation Lifecycle

Операции в WPilot проходят через общую модель жизненного цикла:

```
Inspect
   ↓
Draft
   ↓
Approval
   ↓
Apply
   ↓
Validate
   ↓
Rollback (if required)
```

**Не каждая операция проходит все стадии.**

| Стадия | Когда применяется |
|--------|-------------------|
| **Inspect** | Перед любым изменением; для read-only операций — единственная или основная стадия. |
| **Draft** | Когда нужно подготовить изменение без применения (diff, dry-run, план). |
| **Approval** | Для операций с риском изменения состояния; обязательна по [Mission Charter](WPILOT-MISSION-v1.md) для write-like действий. |
| **Apply** | Когда подготовленное и одобренное изменение применяется к цели. |
| **Validate** | После apply — проверка факта, целостности, видимости на сайте. |
| **Rollback** | При сбое, регрессии или отказе оператора — восстановление из backup или откат изменения. |

Типичные сокращённые пути:

- **Inspection Operations:** Inspect → (опционально Validate для сверки с ожиданием).
- **Draft Operations:** Inspect → Draft → (далее Apply только после Approval).
- **Apply Operations:** Inspect → Draft → Approval → Apply → Validate → (Rollback при необходимости).
- **Recovery Operations:** могут начинаться с Validate или сразу выполнять Rollback / Restore.

---

## Operation Categories

### Inspection Operations

Read-only. Не изменяют состояние WordPress.

- Требуют аутентификации и доступа, но не изменяют контент, настройки, файлы или БД.
- Стадии Approval и Rollback обычно не применяются.

### Draft Operations

Подготовка изменений без применения.

- Формируют план, diff, dry-run или черновик.
- Не коммитят изменения в live-состояние до отдельной Apply-операции с Approval.

### Apply Operations

Применение изменений к определённой цели в scope.

- Требуют human approval до Apply (см. Mission Charter).
- Ожидают backup-first и rollback path для write-like операций.

### Recovery Operations

Rollback, восстановление и пост-apply проверка.

- Используются после неудачного apply, по решению оператора или по плану отката.
- `validate_change` — read-only recovery/verification operation: проверяет уже применённое изменение, не изменяя состояние сайта.
- `restore_backup` — при восстановлении полной страницы, сайта или БД может относиться к risk class R4 (см. [Risk Classes](WPILOT-RISK-CLASSES-v1.md)).

---

## Approved Operations v1

### Inspection

| operation_id | category | description | default risk | rollback expected |
|--------------|----------|-------------|--------------|-------------------|
| inspect_site | Inspection | Сводная read-only инспекция сайта: окружение, активная тема, плагины, общий статус. | low | no |
| inspect_page | Inspection | Read-only чтение страницы: метаданные, контент, структура. | low | no |
| inspect_post | Inspection | Read-only чтение записи (post): метаданные, контент, тип, статус. | low | no |
| inspect_shortcode | Inspection | Read-only разбор shortcode-фрагментов в контенте (в т.ч. WPBakery). | low | no |
| inspect_widget | Inspection | Read-only инспекция виджетов и их конфигурации. | low | no |
| inspect_menu | Inspection | Read-only инспекция меню навигации и пунктов. | low | no |
| inspect_theme_option | Inspection | Read-only чтение theme options / настроек темы (без записи). | low | no |
| inspect_plugin | Inspection | Read-only список и статус плагинов. **Target gap:** в Target Registry v1 нет canonical target для `inspect_plugin`; операция остаётся approved, future target candidate: `plugin` (см. Scope Rules). | low | no |
| inspect_media | Inspection | Read-only инспекция медиатеки: вложения, метаданные, привязки. | low | no |
| inspect_footer | Inspection | Read-only инспекция footer-зоны: контент, виджеты, шаблоны. | low | no |
| inspect_header | Inspection | Read-only инспекция header-зоны: контент, меню, шаблоны. | low | no |
| inspect_css | Inspection | Read-only инспекция CSS (child theme, кастомные фрагменты) без записи. | low | no |
| inspect_environment | Inspection | Read-only инспекция окружения: WP version, PHP, indexing, DEV/prod hints. | low | no |

### Draft

| operation_id | category | description | default risk | rollback expected |
|--------------|----------|-------------|--------------|-------------------|
| draft_page_change | Draft | Подготовка изменения страницы: diff, dry-run, план без apply. | medium | no |
| draft_shortcode_change | Draft | Подготовка точечного изменения shortcode-фрагмента без apply. | medium | no |
| draft_footer_change | Draft | Подготовка изменения footer без apply. | medium | no |
| draft_menu_change | Draft | Подготовка изменения меню без apply. | medium | no |
| draft_widget_change | Draft | Подготовка изменения виджета без apply. | medium | no |
| draft_css_change | Draft | Подготовка CSS-патча (child theme / scoped fragment) без apply. | medium | no |
| draft_content_change | Draft | Подготовка общего контентного изменения в scope без apply. | medium | no |

### Apply

| operation_id | category | description | default risk | rollback expected |
|--------------|----------|-------------|--------------|-------------------|
| apply_change | Apply | Abstract umbrella operation: применение одобренного scoped-изменения к именованной цели. **Cannot execute directly** without resolving to concrete subtype (`apply_content_change`, `apply_shortcode_change`, `apply_footer_change`, `apply_menu_change`, `apply_css_change`). If subtype cannot be resolved, operation is blocked. | high | yes |
| apply_content_change | Apply | Применение одобренного контентного изменения (page/post field). | high | yes |
| apply_shortcode_change | Apply | Применение одобренного точечного изменения shortcode. | high | yes |
| apply_footer_change | Apply | Применение одобренного изменения footer. | high | yes |
| apply_menu_change | Apply | Применение одобренного изменения меню. | high | yes |
| apply_css_change | Apply | Применение одобренного CSS-патча. | high | yes |

### Recovery

| operation_id | category | description | default risk | rollback expected |
|--------------|----------|-------------|--------------|-------------------|
| rollback_change | Recovery | Откат конкретного применённого изменения к состоянию до apply. | medium | yes |
| restore_backup | Recovery | Восстановление из подтверждённого backup (plugin-created или operator-verified). May be **R4** when it affects full page/site/database state (см. [Risk Classes](WPILOT-RISK-CLASSES-v1.md)). | high | yes |
| validate_change | Recovery | Read-only recovery/verification: пост-apply проверка факта изменения, целостности, видимости, регрессий. Does not modify site state. | low | no |

---

## Scope Rules

Operations operate on **defined targets only**. Операция без явной цели в допустимом scope не считается валидной.

Канонический источник target names — [Target Registry v1](WPILOT-TARGET-REGISTRY-v1.md). Допустимые `target_id` в v1:

| target_id | Примеры применения |
|-----------|-------------------|
| **page** | `inspect_page`, `draft_page_change`, `apply_content_change` |
| **post** | `inspect_post`, `draft_content_change`, `apply_content_change` |
| **shortcode** | `inspect_shortcode`, `draft_shortcode_change`, `apply_shortcode_change` |
| **widget** | `inspect_widget`, `draft_widget_change` |
| **menu** | `inspect_menu`, `draft_menu_change`, `apply_menu_change` |
| **header** | `inspect_header`, zone-specific draft/apply (future) |
| **footer** | `inspect_footer`, `draft_footer_change`, `apply_footer_change` |
| **css_fragment** | `inspect_css`, `draft_css_change`, `apply_css_change` |
| **theme_option** | `inspect_theme_option` (read-only в v1) |
| **media** | `inspect_media` |
| **site** | `inspect_site` |
| **environment** | `inspect_environment` |

### inspect_plugin (target gap)

`inspect_plugin` currently has **no canonical target** in [Target Registry v1](WPILOT-TARGET-REGISTRY-v1.md). Операция остаётся **approved** в Manifest v1 с зафиксированным target gap. Future target candidate: **`plugin`** — добавление только через обновление Target Registry (не в v1).

Правила scope:

- Одна операция apply привязана к **одной именованной цели** (или явно ограниченному набору, если оператор зафиксировал scope в change request).
- Массовые или неограниченные цели **не входят** в Manifest v1.
- Цель должна быть идентифицируема до стадии Draft (ID, slug, zone name, fragment key).
- Новые targets — только через обновление Target Registry.

---

## Forbidden Operations

Следующие действия **не входят** в Approved Operations v1 и не считаются типизированными операциями WPilot:

| Forbidden action | Причина исключения |
|------------------|------------------|
| execute_arbitrary_sql | Произвольный SQL; противоречит safety boundary плагина и MVP. |
| execute_arbitrary_php | Выполнение произвольного PHP / code execution. |
| delete_random_files | Неограниченное удаление файлов; нет scoped target. |
| mass_content_rewrite | Массовая перезапись контента; вне scoped replacement. |
| plugin_auto_update | Автообновление плагинов; вне MVP и Mission non-goals. |
| theme_auto_update | Автообновление тем; вне MVP. |
| core_auto_update | Автообновление WordPress core; вне MVP. |
| unapproved_production_change | Изменение production без явного approval и backup evidence. |

Запрещённые действия не получают `operation_id` в Manifest v1. Если подобное действие необходимо в будущем, требуется отдельный charter, risk review и новая версия Manifest — не расширение v1 по умолчанию.

---

## Relationship To Risk Classes

Manifest v1 определяет **каталог операций** и их категории.

**Risk Classes** уже определены в [WPILOT-RISK-CLASSES-v1.md](WPILOT-RISK-CLASSES-v1.md): формальная таксономия риска (R0–R5), матрица approval, backup, validation и rollback expectations.

В таблицах Manifest v1 поле **default risk** — ориентировочная метка (low / medium / high). Каноническая привязка `operation_id` → `risk_class` — в Risk Classes v1. Изменение risk class не должно менять семантику операций без отдельного charter review.

---

## Notes

- Manifest v1 описывает **логическую модель** типизированных операций WPilot.
- Наличие операции в таблице **не означает** реализацию в плагине, REST API, Cursor workflow или любом runtime.
- Human-supervised model из Mission Charter сохраняется: Apply-операции предполагают approval; WPilot не получает автономного authority над WordPress.
- `apply_change` — abstract umbrella operation; cannot execute without concrete subtype resolution.
- `validate_change` — read-only recovery/verification; risk class R0 (см. [Risk Classes](WPILOT-RISK-CLASSES-v1.md)).
- `restore_backup` — may escalate to R4 when affecting full page/site/database state.

### Current documentation stack

Policy-слои WPilot v1 (документированы):

1. [Mission](WPILOT-MISSION-v1.md)
2. [Operations Manifest](WPILOT-OPERATIONS-MANIFEST-v1.md) (этот документ)
3. [Risk Classes](WPILOT-RISK-CLASSES-v1.md)
4. [ChangeSet](WPILOT-CHANGESET-v1.md)
5. [Rollback](WPILOT-ROLLBACK-v1.md)
6. [Target Registry](WPILOT-TARGET-REGISTRY-v1.md)

Следующие слои (вне scope v1): operation-to-endpoint mapping, Cursor workflow bindings, dashboards — отдельные документы.
