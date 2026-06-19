# WPilot Rollback v1

**Classification:** Policy layer — rollback semantics and expectations.
**Status:** Documented v1; policy model only.
**Related:** [WPILOT-MISSION-v1.md](WPILOT-MISSION-v1.md), [WPILOT-OPERATIONS-MANIFEST-v1.md](WPILOT-OPERATIONS-MANIFEST-v1.md), [WPILOT-RISK-CLASSES-v1.md](WPILOT-RISK-CLASSES-v1.md), [WPILOT-CHANGESET-v1.md](WPILOT-CHANGESET-v1.md), [WPILOT-TARGET-REGISTRY-v1.md](WPILOT-TARGET-REGISTRY-v1.md)

---

## Purpose

**Rollback** — механизм восстановления состояния после изменения.

Rollback отвечает на вопрос: *как вернуть цель или сайт к приемлемому состоянию, если apply, validation или операторское решение требуют отката*.

Rollback **не гарантирует** идеальное или полное восстановление. Он **уменьшает риск** изменений, предоставляя документированный, проверяемый путь восстановления.

Rollback является **частью change management** в WPilot: он не существует отдельно от [ChangeSet](WPILOT-CHANGESET-v1.md), [Operations Manifest](WPILOT-OPERATIONS-MANIFEST-v1.md) и [Risk Classes](WPILOT-RISK-CLASSES-v1.md).

Наличие Rollback Layer v1 **не означает** реализацию rollback automation, backup subsystem, API или runtime в плагине.

---

## Rollback Principles

### Backup First

Перед apply для write-like операций backup создаётся или подтверждается **до** мутации состояния. Rollback опирается на backup evidence; откат без подтверждённого источника считается неполным и требует operator review.

Согласование: Mission Charter (backup-first), ChangeSet стадия **Backup**, Risk Classes R2+.

### Validation After Rollback

Rollback **не считается успешным** только потому, что restore выполнен. После restore обязательна проверка: цель существует, ожидаемый контент на месте, страница рендерится, нет критических ошибок, ожидаемые markers восстановлены.

Согласование: Mission Charter (validation-first), операция `validate_change` (R0).

### Human Supervised

Rollback инициируется и подтверждается оператором. WPilot не выполняет автономный откат без human approval и operator confirmation.

Согласование: Mission Charter (human-supervised), Runtime Boundary.

### Evidence Driven

Каждый rollback по возможности фиксирует evidence: источник, timestamp, результат validation, operator confirmation, ссылку на backup. Evidence может храниться вне репозитория.

Согласование: Mission Charter (evidence-driven, audit-friendly), ChangeSet Evidence Expectations.

### Scope Aware

Rollback применяется к **явно определённой цели** или scope. Entity rollback, site rollback и environment rollback — разные уровни; не смешивать без явного operator charter.

Согласование: Operations Manifest Scope Rules, ChangeSet `target_type` / `target_id`.

### No Assumed Recovery

Оператор **не предполагает**, что restore «само всё исправит». Hosting backup, snapshot и plugin-created backup имеют разную полноту и latency. Если источник не verified — rollback остаётся в состоянии review, не closed.

---

## Relationship To ChangeSets

Rollback **связан с конкретным ChangeSet**. Он не является отдельной несвязанной операцией вне контекста изменения.

Каждый ChangeSet может иметь rollback-атрибуты:

| Field | Назначение |
|-------|------------|
| **rollback_available** | Доступен ли путь отката для данного run (yes / no). |
| **rollback_source** | Источник восстановления: backup path, snapshot id, verified export. |
| **rollback_status** | Состояние rollback в рамках ChangeSet: `not_needed`, `available`, `requested`, `in_progress`, `completed`, `failed`, `operator_review`. |

Связь с ChangeSet lifecycle:

- При успешном apply без отката: `rollback_available` = yes, `rollback_status` = `available` или `not_needed` (по risk class).
- При инициированном откате: ChangeSet переходит через стадию **Rollback** → статус `rolled_back` (см. [ChangeSet Status Model](WPILOT-CHANGESET-v1.md)).
- `rollback_source` обычно совпадает с `backup_path` или указывает на hosting / operator-verified source.

Recovery-операции из Manifest:

| operation_id | Роль в rollback |
|--------------|-----------------|
| `rollback_change` | Откат конкретного применённого изменения к состоянию до apply (R3). |
| `restore_backup` | Восстановление из подтверждённого backup; широкий scope → R4. |
| `validate_change` | Пост-rollback verification; read-only (R0). |

---

## Rollback Lifecycle

### Успешный путь

```
Rollback Requested
   ↓
Rollback Source Selected
   ↓
Restore Attempt
   ↓
Validation
   ↓
Rollback Closed
```

### Путь с неудачной validation

```
Rollback Requested
   ↓
Restore Attempt
   ↓
Validation Failed
   ↓
Operator Review
   ↓
Rollback Closed
```

| Стадия | Назначение |
|--------|------------|
| **Rollback Requested** | Оператор инициировал откат: после failed validation, регрессии или осознанного решения. |
| **Rollback Source Selected** | Выбран и зафиксирован `rollback_source` (ChangeSet backup, hosting backup, operator-verified export). |
| **Restore Attempt** | Выполнена попытка восстановления через `rollback_change` или `restore_backup`. |
| **Validation** | Пост-rollback проверка через `validate_change` или operator checklist. |
| **Operator Review** | При failed validation — эскалация: другой источник, ручной fix, закрытие с documented failure. |
| **Rollback Closed** | Rollback завершён; evidence зафиксирован; ChangeSet → `rolled_back` → `closed`. |

Rollback lifecycle **вложен** в ChangeSet lifecycle (стадия Rollback после Validate). Отдельный rollback-run без родительского ChangeSet не считается каноническим паттерном v1.

---

## Rollback Sources

Допустимые источники восстановления в v1:

### ChangeSet Backup

Backup, созданный или подтверждённый в рамках конкретного ChangeSet до apply.

Примеры:

- page backup
- shortcode backup
- widget backup
- footer zone export
- css_fragment snapshot

Предпочтительный источник для R2 scoped changes.

### Hosting Backup

Backup на уровне хостинга, вне plugin-created evidence.

Примеры:

- Beget backup
- hosting snapshot
- hosting restore point
- panel-level full-site backup

Используется при entity backup недостаточен или при environment rollback. Требует operator verification; может относиться к R4 scope.

### Operator Verified Source

Источник, явно проверенный и одобренный оператором до restore.

Примеры:

- verified export (JSON, HTML fragment, structured dump)
- manually approved restore source
- pre-run snapshot зафиксированный в change request / rollback plan

Если источник не verified — restore attempt не переходит в Validation без operator confirmation.

---

## Rollback Expectations By Risk Class

Сводная policy-таблица (не автоматическое enforcement):

| Risk Class | Rollback expectation |
|------------|----------------------|
| **R0** | Rollback не требуется |
| **R1** | Rollback не требуется |
| **R2** | Rollback **expected** — путь отката должен быть доступен (`rollback_available` = yes) |
| **R3** | Rollback **required** — обязателен план или path до/после apply |
| **R4** | **Rollback plan required before apply** — documented plan до execute; `restore_backup` и wide-scope recovery |
| **R5** | Rollback **не применяется** — операция запрещена |

Согласование с [Risk Classes Approval Expectations](WPILOT-RISK-CLASSES-v1.md):

- R2: «Должен быть возможен»
- R3: «Обязателен (plan или path)»
- R4: «План rollback до execute»

Операции recovery:

| operation_id | risk_class | Rollback layer note |
|--------------|------------|---------------------|
| `rollback_change` | R3 | Типичная операция entity/site rollback в рамках ChangeSet |
| `restore_backup` | R4 | Production-critical; plan required before apply unless scoped to single entity backup |

---

## Rollback Scope

Три уровня scope rollback в v1. Канонический источник target names и scope model — [Target Registry v1](WPILOT-TARGET-REGISTRY-v1.md).

### Entity Rollback

Откат **одной именованной сущности** (Entity Scope в Target Registry).

| target_id |
|-----------|
| page |
| post |
| shortcode |
| widget |
| menu |
| media |

Типичные операции: `rollback_change` с ChangeSet backup source. Соответствует R2–R3 в большинстве Triumph-паттернов.

### Site Rollback

Откат **структурных зон и конфигурации** (Site Scope в Target Registry).

| target_id |
|-----------|
| header |
| footer |
| css_fragment |
| theme_option |

Также: coordinated rollback нескольких entity targets в одном ChangeSet (scope в `description`). Требует явного scope и усиленного evidence. Часто R3; site-wide impact → R4.

### Environment Rollback

Откат на **уровне сайта или hosting/runtime layer** (Environment Scope в Target Registry).

| target_id |
|-----------|
| site |
| environment |

Примеры: hosting-level restore, snapshot-level restore, full backup restore (page + DB + files). Операция `restore_backup` (R4). Не заменяет disaster recovery procedures хостинга; требует operator confirmation и validation plan.

---

## Validation After Rollback

Rollback **не закрывается** без validation.

Минимальный checklist v1:

| Check | Описание |
|-------|----------|
| **target exists** | Цель (page, shortcode, zone) существует и адресуема |
| **expected content exists** | Контент соответствует pre-apply / backup reference |
| **page renders** | Страница или зона отображается без fatal errors |
| **no critical errors** | Нет регрессий layout, broken shortcodes, missing assets |
| **expected markers restored** | Контактные блоки, ссылки, footer/header markers на месте |

Validation выполняется через:

- `validate_change` (read-only, R0), или
- operator checklist с фиксацией в `validation_result`

При failed validation → **Operator Review** → повторный restore, смена source, или documented close с `failure_reason`.

---

## Rollback Evidence

Каждый rollback **по возможности** должен иметь:

| Evidence field | Описание |
|----------------|----------|
| **rollback_source** | Путь, id или описание источника восстановления |
| **rollback_timestamp** | ISO 8601 момент завершения restore attempt |
| **validation_result** | Итог пост-rollback проверки |
| **operator_confirmation** | Явное подтверждение оператора (who / when / scope acknowledged) |
| **backup_reference** | Ссылка на исходный backup, использованный как source |

Evidence **может храниться вне репозитория**:

```text
C:\AI MARS\backups\wpilot\
C:\AI MARS\local\runtime\
C:\AI MARS STORAGE\wpilot\evidence\
```

См. [local-storage-policy.md](local-storage-policy.md): backup и evidence paths — local-only, не commit targets.

Шаблон плана: [templates/rollback-plan-template.md](templates/rollback-plan-template.md).

---

## Rollback Example

Иллюстративный пример из реального WPilot-паттерна (Triumph DEV).

| Field | Value |
|-------|-------|
| **ChangeSet** | `apply_footer_change` |
| **Target** | `footer_contacts` |
| **Risk** | R2 |
| **Backup** | `footer_contacts.shortcoder.bak.html` |
| **Rollback Source** | backup file (ChangeSet Backup) |
| **Validation** | footer rendered correctly; contacts visible |
| **Status** | closed |

Расширенный evidence trail:

```
changeset_id:        cs-2026-06-19-footer-contacts-001
operation_id:        apply_footer_change
risk_class:          R2
rollback_available:  yes
rollback_source:     footer_contacts.shortcoder.bak.html
rollback_status:     completed
rollback_timestamp:  2026-06-19T15:10:00+03:00
validation_result:   validate_change: footer contacts visible, no layout regression
operator_confirmation: operator acknowledged restore from ChangeSet backup
status:              rolled_back → closed
```

---

## Non Goals

Rollback Layer v1 **не означает**:

| Non-goal | Пояснение |
|----------|-----------|
| **Time machine** | Полное восстановление произвольной точки времени без verified source |
| **Guaranteed recovery** | 100% восстановление состояния; зависит от качества backup и scope |
| **Autonomous repair** | Автоматический self-healing без оператора |
| **Hosting disaster recovery replacement** | Замена DR-процедур Beget или другого хостинга |

---

## Relationship To Mission

Rollback поддерживает принципы [Mission Charter](WPILOT-MISSION-v1.md):

| Mission principle | Rollback contribution |
|-------------------|----------------------|
| **backup-first** | ChangeSet Backup как предпочтительный rollback source |
| **validation-first** | Validation After Rollback обязательна |
| **human-supervised** | Operator initiation, confirmation, review |
| **audit-friendly** | Rollback Evidence trail |
| **rollback-capable** | Формализованный policy layer для recovery operations |

---

## Relationship To Other Layers

| Документ | Вопрос |
|----------|--------|
| **Operations Manifest** | «Какие recovery-операции существуют?» — `rollback_change`, `restore_backup`, `validate_change` |
| **Risk Classes** | «Когда rollback обязателен?» — R2 expected, R3 required, R4 plan before apply |
| **ChangeSet** | «Как rollback привязан к конкретному run?» — `rollback_available`, `rollback_source`, lifecycle, evidence |
| **Target Registry** | «Какие targets входят в entity / site / environment rollback scope?» — canonical `target_id` |
| **Rollback v1** | «Что считается rollback, какие источники допустимы, как проверять и закрывать?» |

Rollback **не заменяет** ChangeSet, Risk Classes или Manifest. Он **детализирует** rollback-семантику, которую эти слои уже предполагают.

Ранний operational документ [backup-rollback-rules.md](backup-rollback-rules.md) остаётся Phase 1 safety rules; **WPILOT-ROLLBACK-v1.md** — канонический policy layer для согласования с Mission, Manifest, Risk Classes и ChangeSet.

---

## Notes

Rollback Layer является **policy layer**.

Он **не требует**:

- БД
- API
- runtime
- plugin implementation
- automated rollback execution

Human-supervised model сохраняется: WPilot не получает автономного authority над восстановлением WordPress.

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v1 |
| Implements runtime | No |
| Replaces ChangeSet | No |
| Replaces Risk Classes | No |
| Replaces Mission Charter | No |
| Replaces backup-rollback-rules.md | No (complements; v1 is canonical policy layer) |
