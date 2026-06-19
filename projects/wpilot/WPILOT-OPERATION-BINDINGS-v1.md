# WPilot Operation Bindings v1

**Classification:** Policy layer — official bindings between operations, targets, and risk policy.
**Status:** Documented v1; policy model only.
**Related:** [WPILOT-MISSION-v1.md](WPILOT-MISSION-v1.md), [WPILOT-OPERATIONS-MANIFEST-v1.md](WPILOT-OPERATIONS-MANIFEST-v1.md), [WPILOT-RISK-CLASSES-v1.md](WPILOT-RISK-CLASSES-v1.md), [WPILOT-TARGET-REGISTRY-v1.md](WPILOT-TARGET-REGISTRY-v1.md), [WPILOT-CHANGESET-v1.md](WPILOT-CHANGESET-v1.md), [WPILOT-ROLLBACK-v1.md](WPILOT-ROLLBACK-v1.md)

---

## Purpose

**Operation Bindings** определяет официальную связь между слоями WPilot Core Model:

- [Operations Manifest](WPILOT-OPERATIONS-MANIFEST-v1.md) — каталог `operation_id`
- [Target Registry](WPILOT-TARGET-REGISTRY-v1.md) — допустимые `target_id`
- [Risk Classes](WPILOT-RISK-CLASSES-v1.md) — `risk_class` и policy expectations
- [ChangeSet](WPILOT-CHANGESET-v1.md) — единица выполнения run
- [Rollback](WPILOT-ROLLBACK-v1.md) — ожидания и execution policy отката

Bindings отвечает на вопрос: **«Какая операция допустима для какой цели, с каким риском и какими требованиями approval / backup / validation / rollback?»**

Operation Bindings — это **policy layer**. Документ **не определяет**:

- реализацию в плагине, REST API или runtime;
- endpoint map или API contract;
- workflow engine или automated enforcement;
- execution authority.

Наличие binding в v1 **не означает**, что соответствующий guardrail уже реализован.

---

## Design Principles

| Principle | Описание |
|-----------|----------|
| **Explicit bindings** | Каждая approved операция Manifest v1 имеет явную запись binding. Неявные разрешения не допускаются. |
| **No implicit permissions** | Операция без binding или с blocked status не считается исполняемой. |
| **Target-aware operations** | `allowed_targets` ссылаются только на canonical `target_id` из Target Registry v1. |
| **Risk-aware execution** | `risk_class` берётся из Risk Classes v1; bindings не переопределяют risk policy. |
| **Human-supervised model** | Approval expectations согласованы с Mission Charter: нет автономного authority у WPilot. |
| **Policy before implementation** | Bindings фиксируют policy до любой plugin / API / runtime реализации. |

---

## Binding Structure

Каждая запись Operation Bindings v1 описывается полями:

| Field | Назначение |
|-------|------------|
| **operation_id** | Стабильный идентификатор из [Operations Manifest v1](WPILOT-OPERATIONS-MANIFEST-v1.md). |
| **allowed_targets** | Список canonical `target_id` из [Target Registry v1](WPILOT-TARGET-REGISTRY-v1.md), на которые операция может быть привязана. Значение `none` — target gap. Значение `inherits` — target наследуется от родительского ChangeSet. Значение `unresolved` — операция blocked до разрешения subtype. |
| **risk_class** | Канонический класс риска R0–R5 из [Risk Classes v1](WPILOT-RISK-CLASSES-v1.md). Может включать scope-эскалацию (см. `apply_css_change`). |
| **approval_required** | Требование человеческого контроля: `operator initiated`, `no apply authority`, `required`, `explicit required`, `blocked`. |
| **backup_required** | `no`, `required`, `existing verified source`. |
| **validation_required** | `no`, `optional`, `required`, `plan required`. |
| **rollback_expectation** | `none`, `expected`, `required`, `plan required`, `operation itself`. |

Дополнительные статусы binding (не отдельные поля, но фиксируются в записях):

- **binding_status:** `fully_bound` | `partially_bound` | `target_gap` | `blocked`
- **notes:** scope escalation, inheritance rules, subtype resolution

---

## Inspection Bindings

Read-only операции. Общий policy-профиль: **R0**, backup не требуется, validation не обязательна, rollback не ожидается.

### inspect_page

| Field | Value |
|-------|-------|
| allowed_targets | `page` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_post

| Field | Value |
|-------|-------|
| allowed_targets | `post` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_shortcode

| Field | Value |
|-------|-------|
| allowed_targets | `shortcode` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_widget

| Field | Value |
|-------|-------|
| allowed_targets | `widget` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_menu

| Field | Value |
|-------|-------|
| allowed_targets | `menu` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_header

| Field | Value |
|-------|-------|
| allowed_targets | `header` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_footer

| Field | Value |
|-------|-------|
| allowed_targets | `footer` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_media

| Field | Value |
|-------|-------|
| allowed_targets | `media` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_css

| Field | Value |
|-------|-------|
| allowed_targets | `css_fragment` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_theme_option

| Field | Value |
|-------|-------|
| allowed_targets | `theme_option` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_environment

| Field | Value |
|-------|-------|
| allowed_targets | `environment` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_site

| Field | Value |
|-------|-------|
| allowed_targets | `site` |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | fully_bound |

### inspect_plugin (target gap)

| Field | Value |
|-------|-------|
| allowed_targets | **none** (target gap) |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no |
| rollback_expectation | none |
| binding_status | **target_gap** |

**Отдельная отметка:** `inspect_plugin` — approved operation в Manifest v1, но в Target Registry v1 **нет** canonical target `plugin`. Операция остаётся в bindings с зафиксированным gap; gap **не устраняется** в v1. Future target candidate: `plugin` — только через charter review и обновление Target Registry.

---

## Draft Bindings

Draft-операции не применяют изменения к live-состоянию. Общий policy-профиль: **R1**, нет apply authority, backup не требуется, validation optional, rollback none.

### draft_page_change

| Field | Value |
|-------|-------|
| allowed_targets | `page` |
| risk_class | R1 |
| approval_required | no apply authority |
| backup_required | no |
| validation_required | optional |
| rollback_expectation | none |
| binding_status | fully_bound |

### draft_shortcode_change

| Field | Value |
|-------|-------|
| allowed_targets | `shortcode` |
| risk_class | R1 |
| approval_required | no apply authority |
| backup_required | no |
| validation_required | optional |
| rollback_expectation | none |
| binding_status | fully_bound |

### draft_footer_change

| Field | Value |
|-------|-------|
| allowed_targets | `footer` |
| risk_class | R1 |
| approval_required | no apply authority |
| backup_required | no |
| validation_required | optional |
| rollback_expectation | none |
| binding_status | fully_bound |

### draft_menu_change

| Field | Value |
|-------|-------|
| allowed_targets | `menu` |
| risk_class | R1 |
| approval_required | no apply authority |
| backup_required | no |
| validation_required | optional |
| rollback_expectation | none |
| binding_status | fully_bound |

### draft_widget_change

| Field | Value |
|-------|-------|
| allowed_targets | `widget` |
| risk_class | R1 |
| approval_required | no apply authority |
| backup_required | no |
| validation_required | optional |
| rollback_expectation | none |
| binding_status | fully_bound |

### draft_css_change

| Field | Value |
|-------|-------|
| allowed_targets | `css_fragment` |
| risk_class | R1 |
| approval_required | no apply authority |
| backup_required | no |
| validation_required | optional |
| rollback_expectation | none |
| binding_status | fully_bound |

### draft_content_change

| Field | Value |
|-------|-------|
| allowed_targets | `page`, `post` |
| risk_class | R1 |
| approval_required | no apply authority |
| backup_required | no |
| validation_required | optional |
| rollback_expectation | none |
| binding_status | partially_bound |

**notes:** polymorphic target; оператор обязан указать `target_type` (`page` или `post`) до apply-path.

---

## Apply Bindings

Apply-операции изменяют live-состояние. Требуют human approval, backup и validation по Risk Classes; rollback expected или required.

### apply_content_change

| Field | Value |
|-------|-------|
| allowed_targets | `page`, `post` |
| risk_class | R2 |
| approval_required | required |
| backup_required | required |
| validation_required | required |
| rollback_expectation | expected |
| binding_status | partially_bound |

**notes:** polymorphic target; одна именованная цель на ChangeSet.

### apply_shortcode_change

| Field | Value |
|-------|-------|
| allowed_targets | `shortcode` |
| risk_class | R2 |
| approval_required | required |
| backup_required | required |
| validation_required | required |
| rollback_expectation | expected |
| binding_status | fully_bound |

### apply_footer_change

| Field | Value |
|-------|-------|
| allowed_targets | `footer` |
| risk_class | R2 |
| approval_required | required |
| backup_required | required |
| validation_required | required |
| rollback_expectation | expected |
| binding_status | fully_bound |

### apply_menu_change

| Field | Value |
|-------|-------|
| allowed_targets | `menu` |
| risk_class | R3 |
| approval_required | required |
| backup_required | required |
| validation_required | required |
| rollback_expectation | required |
| binding_status | fully_bound |

### apply_css_change

| Field | Value |
|-------|-------|
| allowed_targets | `css_fragment` |
| risk_class | **R2** (default: isolated fragment / page-local CSS) |
| approval_required | required |
| backup_required | required |
| validation_required | required |
| rollback_expectation | expected (R2) / required (R3/R4 escalation) |
| binding_status | partially_bound |

**Scope escalation (не меняет target, меняет risk_class):**

| Scope | risk_class | rollback_expectation |
|-------|------------|----------------------|
| isolated `css_fragment`, page-local patch | R2 | expected |
| site-wide child theme CSS | R3 or R4 | required |

Эскалация зависит от environment и blast radius; фиксируется в ChangeSet `risk_class` и evidence.

### apply_change (blocked)

| Field | Value |
|-------|-------|
| allowed_targets | **unresolved** |
| risk_class | unresolved until subtype |
| approval_required | blocked |
| backup_required | blocked |
| validation_required | blocked |
| rollback_expectation | blocked |
| binding_status | **blocked** |

**status:** umbrella operation; **cannot execute** until resolved to concrete subtype:

- `apply_content_change`
- `apply_shortcode_change`
- `apply_footer_change`
- `apply_menu_change`
- `apply_css_change`

If subtype cannot be resolved, operation remains **blocked**.

---

## Recovery Bindings

### validate_change

| Field | Value |
|-------|-------|
| allowed_targets | **inherits** (from parent ChangeSet `target_type`) |
| risk_class | R0 |
| approval_required | operator initiated |
| backup_required | no |
| validation_required | no (operation itself is validation) |
| rollback_expectation | none |
| binding_status | partially_bound |

**notes:** read-only post-apply verification; не изменяет состояние сайта. Target наследуется от ChangeSet, который проверяется.

### rollback_change

| Field | Value |
|-------|-------|
| allowed_targets | **inherits** (from parent ChangeSet `target_type`) |
| risk_class | R3 |
| approval_required | required |
| backup_required | required |
| validation_required | required |
| rollback_expectation | operation itself |
| binding_status | partially_bound |

**notes:** откат конкретного применённого изменения; target и scope следуют родительскому ChangeSet. Допустимые inherited targets — любой canonical `target_id` из Registry v1, использованный в parent apply.

### restore_backup

| Field | Value |
|-------|-------|
| allowed_targets | **inherits** / varies by backup scope (`page`, `post`, `shortcode`, `footer`, `menu`, `css_fragment`, `site`, `environment`, …) |
| risk_class | R4 (default; may de-escalate only when explicitly scoped to single entity backup — operator charter) |
| approval_required | explicit required |
| backup_required | existing verified source |
| validation_required | required |
| rollback_expectation | plan required |
| binding_status | partially_bound |

**notes:** production-critical wide-scope recovery; rollback plan обязателен до execute.

---

## Binding Matrix

Сводная таблица для всех approved операций Manifest v1 (29 операций).

| operation | target | risk | approval | backup | validation | rollback | status |
|-----------|--------|------|----------|--------|------------|----------|--------|
| inspect_site | site | R0 | operator initiated | no | no | none | fully_bound |
| inspect_page | page | R0 | operator initiated | no | no | none | fully_bound |
| inspect_post | post | R0 | operator initiated | no | no | none | fully_bound |
| inspect_shortcode | shortcode | R0 | operator initiated | no | no | none | fully_bound |
| inspect_widget | widget | R0 | operator initiated | no | no | none | fully_bound |
| inspect_menu | menu | R0 | operator initiated | no | no | none | fully_bound |
| inspect_theme_option | theme_option | R0 | operator initiated | no | no | none | fully_bound |
| inspect_plugin | **none (gap)** | R0 | operator initiated | no | no | none | target_gap |
| inspect_media | media | R0 | operator initiated | no | no | none | fully_bound |
| inspect_footer | footer | R0 | operator initiated | no | no | none | fully_bound |
| inspect_header | header | R0 | operator initiated | no | no | none | fully_bound |
| inspect_css | css_fragment | R0 | operator initiated | no | no | none | fully_bound |
| inspect_environment | environment | R0 | operator initiated | no | no | none | fully_bound |
| draft_page_change | page | R1 | no apply authority | no | optional | none | fully_bound |
| draft_shortcode_change | shortcode | R1 | no apply authority | no | optional | none | fully_bound |
| draft_footer_change | footer | R1 | no apply authority | no | optional | none | fully_bound |
| draft_menu_change | menu | R1 | no apply authority | no | optional | none | fully_bound |
| draft_widget_change | widget | R1 | no apply authority | no | optional | none | fully_bound |
| draft_css_change | css_fragment | R1 | no apply authority | no | optional | none | fully_bound |
| draft_content_change | page, post | R1 | no apply authority | no | optional | none | partially_bound |
| apply_change | **unresolved** | unresolved | blocked | blocked | blocked | blocked | blocked |
| apply_content_change | page, post | R2 | required | required | required | expected | partially_bound |
| apply_shortcode_change | shortcode | R2 | required | required | required | expected | fully_bound |
| apply_footer_change | footer | R2 | required | required | required | expected | fully_bound |
| apply_menu_change | menu | R3 | required | required | required | required | fully_bound |
| apply_css_change | css_fragment | R2 / R3 / R4 | required | required | required | expected / required | partially_bound |
| validate_change | inherits | R0 | operator initiated | no | no | none | partially_bound |
| rollback_change | inherits | R3 | required | required | required | operation itself | partially_bound |
| restore_backup | varies / inherits | R4 | explicit required | existing verified source | required | plan required | partially_bound |

**Проверка покрытия:** все 29 `operation_id` из Manifest v1 присутствуют в матрице. Новые `target_id` не введены.

---

## Binding Classification Summary

### Fully bound (20)

Операции с фиксированным `allowed_targets` (один target) и стабильным `risk_class` без обязательного subtype/inheritance resolution:

`inspect_site`, `inspect_page`, `inspect_post`, `inspect_shortcode`, `inspect_widget`, `inspect_menu`, `inspect_theme_option`, `inspect_media`, `inspect_footer`, `inspect_header`, `inspect_css`, `inspect_environment`, `draft_page_change`, `draft_shortcode_change`, `draft_footer_change`, `draft_menu_change`, `draft_widget_change`, `draft_css_change`, `apply_shortcode_change`, `apply_footer_change`, `apply_menu_change`

### Partially bound (7)

Операции, где target, risk или execution status зависит от контекста:

| operation | Причина partial binding |
|-----------|-------------------------|
| `draft_content_change` | polymorphic target: `page` \| `post` |
| `apply_content_change` | polymorphic target: `page` \| `post` |
| `apply_css_change` | scope escalation R2 → R3/R4 |
| `validate_change` | target inherits from parent ChangeSet |
| `rollback_change` | target inherits from parent ChangeSet |
| `restore_backup` | target varies by backup scope |
| `apply_change` | **blocked** until subtype resolved (также classified blocked) |

### Target gap (1)

| operation | Причина |
|-----------|---------|
| `inspect_plugin` | нет canonical target `plugin` в Target Registry v1 |

### Blocked (1)

| operation | Причина |
|-----------|---------|
| `apply_change` | umbrella operation; unresolved until concrete apply subtype |

---

## Relationship To Target Registry

[Target Registry v1](WPILOT-TARGET-REGISTRY-v1.md) является **единственным источником** допустимых `target_id` для bindings.

Правила v1:

- Bindings **не создают** новые targets.
- `allowed_targets` в bindings — только подмножество canonical targets Registry v1 или специальные policy-маркеры (`none`, `inherits`, `unresolved`).
- `inspect_plugin` фиксирует **target gap**, не новый target.
- Polymorphic bindings (`page`, `post`) используют **существующие** registry targets, не composite target.

---

## Relationship To Risk Classes

Bindings **используют** [Risk Classes v1](WPILOT-RISK-CLASSES-v1.md); bindings **не изменяют** risk policy.

- Канонический `risk_class` для операции определён в Risk Classes.
- Bindings добавляют operational context: approval / backup / validation / rollback expectations в форме binding record.
- Scope escalation (`apply_css_change`) — уже описана в Risk Classes; bindings лишь связывают её с target `css_fragment`.
- Forbidden operations (R5) **не имеют** bindings — они вне approved Manifest v1.

---

## Relationship To ChangeSets

Каждый ChangeSet **обязан** ссылаться на binding (явно или через resolvable `operation_id` + `target_type`).

Правила v1:

| ChangeSet field | Binding source |
|-----------------|----------------|
| `operation_id` | Должен быть approved в Manifest и иметь binding |
| `target_type` | Должен входить в `allowed_targets` binding (или inherit path для recovery) |
| `risk_class` | Должен соответствовать binding; эскалация только по documented rules |
| `backup_required` | Следует из binding / risk class |
| `validation_required` | Следует из binding / risk class |
| `rollback_available` | Следует из `rollback_expectation` binding |

ChangeSet с `apply_change` без resolved subtype — **invalid / blocked**.

ChangeSet с `inspect_plugin` — допустим как policy record, но `target_type` не может быть заполнен canonical value до появления `plugin` в Registry.

---

## Relationship To Rollback

Bindings определяют **rollback expectations** (что ожидается от операции).

[Rollback Layer v1](WPILOT-ROLLBACK-v1.md) определяет **rollback execution policy** (как откатывать, источники, validation after rollback, evidence).

| rollback_expectation (binding) | Rollback layer responsibility |
|-------------------------------|------------------------------|
| none | Rollback не применяется |
| expected | Rollback path должен быть возможен; детали — Rollback policy |
| required | Rollback plan/path обязателен до или после apply |
| plan required | Explicit rollback plan до execute (`restore_backup`) |
| operation itself | Операция является act of rollback (`rollback_change`) |

Bindings не заменяют Rollback Layer и не описывают automation.

---

## Known Gaps

### inspect_plugin

| Aspect | Value |
|--------|-------|
| operation_id | `inspect_plugin` |
| Manifest status | approved |
| Registry target | **none** — нет `plugin` в Target Registry v1 |
| binding status | target_gap |
| risk_class | R0 (operation semantics read-only) |
| resolution | **не устраняется в v1** |

**Причина:** нет canonical plugin target в Registry v1.

**Статус:** approved operation · target gap · future review.

Future target candidate `plugin` добавляется только через обновление Target Registry (charter review), не через bindings v1.

---

## Future Extensions

Возможны будущие bindings для новых targets и операций. **Не входят в v1:**

| Future area | Notes |
|-------------|-------|
| **plugin** | закрывает gap для `inspect_plugin`; write paths — отдельный charter |
| **taxonomy** | categories, tags, custom taxonomies |
| **user** | WordPress users and roles |
| **comment** | comments and moderation |
| **seo_object** | SEO metadata objects (Yoast, RankMath и аналоги) |

Добавление требует обновления Target Registry, Manifest, Risk Classes, ChangeSet и bindings — не расширение bindings v1 по умолчанию.

---

## Notes

Operation Bindings v1:

- **не создаёт** runtime;
- **не создаёт** REST surface;
- **не создаёт** API contract;
- **не создаёт** execution authority;
- **не создаёт** workflow engine;
- **не создаёт** endpoint implementation.

Bindings — policy/documentation layer для human-operated WPilot workflows, ChangeSet authoring и будущих operator templates.

### Current documentation stack

Policy-слои WPilot v1 (документированы):

1. [Mission](WPILOT-MISSION-v1.md)
2. [Operations Manifest](WPILOT-OPERATIONS-MANIFEST-v1.md)
3. [Risk Classes](WPILOT-RISK-CLASSES-v1.md)
4. [ChangeSet](WPILOT-CHANGESET-v1.md)
5. [Rollback](WPILOT-ROLLBACK-v1.md)
6. [Target Registry](WPILOT-TARGET-REGISTRY-v1.md)
7. [Operation Bindings](WPILOT-OPERATION-BINDINGS-v1.md) (этот документ)

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v1 |
| Implements runtime | No |
| Creates API / endpoints | No |
| Creates new targets | No |
| Resolves inspect_plugin gap | No (gap documented only) |
| Canonical source for operation ↔ target ↔ risk binding | Yes |
