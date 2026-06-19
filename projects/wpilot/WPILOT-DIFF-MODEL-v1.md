# WPilot Diff Model v1

**Classification:** Change layer — canonical comparison and delta description model.
**Status:** Documented v1; logical model only.
**Related:** [WPILOT-MISSION-v1.md](WPILOT-MISSION-v1.md), [WPILOT-SITE-SNAPSHOT-MODEL-v1.md](WPILOT-SITE-SNAPSHOT-MODEL-v1.md), [WPILOT-CHANGESET-v1.md](WPILOT-CHANGESET-v1.md), [WPILOT-ROLLBACK-v1.md](WPILOT-ROLLBACK-v1.md), [WPILOT-OPERATIONS-MANIFEST-v1.md](WPILOT-OPERATIONS-MANIFEST-v1.md), [WPILOT-TARGET-REGISTRY-v1.md](WPILOT-TARGET-REGISTRY-v1.md), [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md)

---

## Purpose

**Diff** — каноническое, структурированное описание **различий** между двумя состояниями WordPress-сайта (или его scoped части).

Diff фиксирует **что изменилось**, **между чем** и **насколько это значимо** — а не **полное состояние** сайта и не **как восстановить** состояние.

WPilot использует Diff Model как change layer для:

- inspection — понимание отличий между baseline и текущим наблюдением;
- validation — подтверждение, что apply привёл к ожидаемым изменениям и не затронул лишнее;
- drift detection — обнаружение незапланированных отклонений live state от snapshot или approved baseline;
- change planning — подготовка draft, dry-run и ChangeSet на основе осознанного delta;
- rollback planning — оценка, что именно нужно вернуть и какой scope rollback покрывает;
- capability verification — evidence, что операция произвела предсказуемый, ограниченный delta.

### Diff ≠ Backup

| Аспект | Diff | Backup |
|--------|------|--------|
| **Назначение** | Описание различий между состояниями | Восстановление состояния |
| **Форма** | Логическая модель delta-записей | Артефакт restore (файл, export, hosting bundle) |
| **Направление** | Compare / describe change | Write-back / restore |
| **Полнота** | Scoped к сравниваемым объектам | Должен покрывать restore scope или явно помечать gaps |
| **Policy layer** | Change description | Recovery source (см. [Rollback v1](WPILOT-ROLLBACK-v1.md)) |

Diff **может ссылаться** на backup-derived state как на одну из сторон сравнения, но **не выполняет** restore и **не заменяет** backup.

### Diff ≠ Snapshot

| Аспект | Diff | Site Snapshot |
|--------|------|---------------|
| **Назначение** | Что **изменилось** между A и B | Что **есть** в момент capture |
| **Вход** | Два (или более) state refs | Один момент времени / один capture |
| **Объекты** | Delta records (`change_type`, severity) | Snapshot objects (observed state) |
| **Слой** | Change layer | State layer |
| **Типичный вопрос** | «Чем отличается contacts page от baseline?» | «Как выглядит contacts page сейчас?» |

Snapshot описывает **состояние**. Diff описывает **переход или расхождение** между состояниями. Diff **потребляет** snapshot (или snapshot-equivalent state) как input; snapshot **не подразумевает** сравнение.

Наличие Diff Model v1 **не означает** runtime, API, plugin diff engine, automated compare pipeline или persisted diff store.

---

## Diff Sources

Diff всегда строится между **двумя сторонами сравнения** (`source_a`, `source_b`). Каждая сторона — ссылка на состояние, не обязательно полный Site Snapshot.

### Snapshot → Snapshot

Сравнение двух зафиксированных snapshot bundles (или partial snapshots).

| Типичный сценарий | Пример |
|-------------------|--------|
| Pre-apply vs post-apply | Baseline snapshot до ChangeSet Apply vs partial snapshot после Validate |
| Periodic drift review | Snapshot недельной давности vs свежий inspection snapshot |
| Cross-environment compare | DEV snapshot vs staging snapshot (operator-initiated, scoped) |

**Правила:**

- Обе стороны **должны** явно указывать `scope`; diff partial↔full без маркировки — `SAFE UNKNOWN` coverage.
- `source_a` обычно = baseline / older; `source_b` = candidate / newer — convention, не enforcement.

### Snapshot → Live State

Сравнение зафиксированного snapshot с текущим live observation (REST read, HTML capture, operator re-inspect).

| Типичный сценарий | Пример |
|-------------------|--------|
| Drift detection | Pre-apply snapshot vs live page после внешнего редактирования |
| Stale baseline check | Snapshot перед dry-run vs live content at execute time |
| Validation assist | Expected post-apply snapshot vs live render check |

**Правила:**

- Live state **не является** snapshot до структурирования; diff может помечать live-side objects как `inferred` или `partial`.
- Checksum / content mismatch между snapshot и live — типичный вход для `modified` или `unknown` diff records и refusal paths в plugin dry-run (см. plugin-mvp contracts; не часть Diff Model runtime).

### Backup → Snapshot

Сравнение backup-derived state (export fragment, `content_before`, plugin backup record) со snapshot или snapshot object.

| Типичный сценарий | Пример |
|-------------------|--------|
| Rollback planning | Pre-apply backup content vs current snapshot object for target |
| Backup coverage check | Backup export vs partial snapshot — есть ли gaps |
| Post-rollback validation | Restored backup state vs expected snapshot after rollback |

**Правила:**

- Backup остаётся **recovery source**; diff только **описывает** delta, не restore.
- Backup binary / full DB dump **не обязан** полностью map в snapshot objects; gaps → `SAFE UNKNOWN` diff severity или missing diff records.

### Operator Verified Source → Snapshot

Сравнение human-confirmed fact (admin panel, hosting panel, manual check) со snapshot или snapshot object.

| Типичный сценарий | Пример |
|-------------------|--------|
| Gap fill | Operator confirms plugin version; snapshot had `SAFE UNKNOWN` |
| Conflict resolution | Operator says footer menu changed; snapshot still shows old state |
| Evidence override | Operator verified source wins for planning when REST evidence stale |

**Правила:**

- Operator verified source — highest trust для **planning**, но diff record **должен** помечать provenance (`source_b` or notes).
- Diff не **автоматически** применяет operator override к snapshot; re-capture snapshot recommended.

### Source reference fields (recommended)

| Field | Description |
|-------|-------------|
| **source_kind** | `snapshot` \| `live_state` \| `backup` \| `operator_verified` \| `dry_run_preview` |
| **source_ref** | `snapshot_id`, backup path, evidence ref, operator note id |
| **captured_at** | ISO 8601 или `SAFE UNKNOWN` |
| **scope** | `full_site` \| `entity` \| `zone` \| `fragment` |

---

## Diff Levels

Уровни diff задают **гранулярность и домен** сравнения. Aligned с [Snapshot Levels](WPILOT-SITE-SNAPSHOT-MODEL-v1.md) (L0–L4), но описывают **изменения**, не capture depth.

```
Identity Diff
   ↓
Structure Diff
   ↓
Content Diff
   ↓
Configuration Diff
   ↓
Environment Diff
```

| Level | Name | Что сравнивается | Типичные diff objects |
|-------|------|------------------|----------------------|
| **Identity** | Site Identity Diff | Label, URL/domain (sanitized), environment class, owner context | `site` identity fields |
| **Structure** | Structure Diff | Menus, header/footer zones, navigation, structural refs | `menu`, `header`, `footer`, structural relationships |
| **Content** | Content Diff | Pages, posts, shortcodes, media refs in content | `page`, `post`, `shortcode`, `media` |
| **Configuration** | Configuration Diff | Theme, plugins, scoped CSS, theme_option-visible state | `active_theme`, `active_plugins`, `css_fragment`, `theme_option` |
| **Environment** | Environment Diff | WP/PHP/hosting signals, indexing, DEV/prod markers | `environment` |

### Level rules

- Diff bundle **может** включать только subset levels (например, Content diff для одной page).
- Diff level **не равен** risk class; severity оценивается отдельно (см. Diff Severity).
- Structure diff с content impact **может** порождать записи на нескольких levels (relationship change + content change).
- Environment diff **не заменяет** hosting-level rollback scope; см. [Rollback v1](WPILOT-ROLLBACK-v1.md).

---

## Diff Objects

Каждое зафиксированное различие представляется как **diff object** (delta record).

### Canonical object fields

| Field | Required | Description |
|-------|----------|-------------|
| **diff_id** | yes | Уникальный идентификатор записи diff в bundle (stable within bundle) |
| **source_a** | yes | Ссылка на состояние «до» / baseline (source ref + kind) |
| **source_b** | yes | Ссылка на состояние «после» / candidate (source ref + kind) |
| **target_type** | yes | Тип затронутой сущности; aligned с [Target Registry](WPILOT-TARGET-REGISTRY-v1.md) `target_type` |
| **target_id** | yes | Идентификатор цели: slug, numeric ID, zone name, fragment key |
| **change_type** | yes | `added` \| `removed` \| `modified` \| `moved` \| `unknown` |
| **description** | yes | Человекочитаемое описание delta; audit-friendly, без secrets |

### Recommended optional fields

| Field | Description |
|-------|-------------|
| **diff_level** | Identity \| Structure \| Content \| Configuration \| Environment |
| **severity** | Informational \| Minor \| Moderate \| Major \| Critical \| SAFE UNKNOWN |
| **field_path** | Конкретное поле или path внутри объекта (например, `post_content`, `menu_item:3:title`) |
| **relationship** | Если `moved`: from → to ref |
| **evidence_refs** | HTML, REST, export refs supporting this delta |
| **notes** | Operator notes, inference markers, coverage limits |

### Example diff object

```
diff_id:       diff-001
source_a:      snapshot:sn-pre-apply-contacts-2026-06-19
source_b:      live_state:rest-read-page-69-2026-06-19T15:00
target_type:   shortcode
target_id:     footer_contacts
change_type:   modified
description:   Contact phone text differs between pre-apply snapshot and live REST read.
severity:      Moderate
diff_level:    Content
```

---

## Change Types

Канонические значения `change_type` v1:

| change_type | Meaning | Typical source_a → source_b |
|-------------|---------|---------------------------|
| **added** | Объект или фрагмент присутствует в B, отсутствует в A | Snapshot without shortcode → snapshot with shortcode |
| **removed** | Объект или фрагмент присутствует в A, отсутствует в B | Page in baseline → page deleted or unpublished in candidate |
| **modified** | Объект существует в обеих сторонах, но наблюдаемые поля различаются | Same `target_id`, different content, title, CSS, or config |
| **moved** | Объект или фрагмент сменил structural position без semantic delete+add | Shortcode relocated within page; menu item reordered |
| **unknown** | Delta detected but classification uncertain; incomplete evidence or partial scope | Backup vs live with unreadable encoding; fuzzy HTML diff without operator confirm |

### Change type rules

- Prefer **modified** over removed+added when stable `target_id` persists.
- **moved** requires structural position change evidence, not mere content edit.
- **unknown** **не блокирует** diff bundle; it signals operator review before apply or rollback decisions.
- Dry-run «expected after» vs «before» в plugin context maps к **modified** (or **added**/**removed** for span-level) at Content level — logical alignment only; plugin contracts remain separate.

---

## Diff Severity

Severity оценивает **операционную значимость** delta для operator и workflow — не заменяет [Risk Classes](WPILOT-RISK-CLASSES-v1.md) R0–R5.

| Severity | Meaning | Typical operator response |
|----------|---------|---------------------------|
| **Informational** | Ожидаемое или нейтральное отличие; не влияет на apply/rollback decision | Log, optional review |
| **Minor** | Незначительное отличие в scoped fragment; low blast radius | Review; may proceed if expected |
| **Moderate** | Заметное content or structure change in named target | Explicit review before apply or after drift detect |
| **Major** | Широкий scope, multiple targets, or critical zone touched | Approval reconsideration; narrow scope or abort |
| **Critical** | Data loss signal, security-relevant change, production-impacting drift, forbidden zone mutation | Stop; rollback or refusal path; no silent continue |
| **SAFE UNKNOWN** | Severity cannot be determined from available evidence or scope | Treat as elevated caution; re-inspect; do not auto-downgrade |

### Severity vs Risk Class

| Layer | Question |
|-------|----------|
| **Risk Class (R0–R5)** | Насколько опасна **запланированная операция**? |
| **Diff Severity** | Насколько значимо **обнаруженное отличие** между состояниями? |

Diff severity **может информировать** risk review (например, unexpected Critical drift before apply), но **не заменяет** `risk_class` в ChangeSet.

---

## Diff Relationships

Diff Model **связан** с другими слоями WPilot; diff bundle — описание delta, не execution.

### Diff → Snapshot

| Relationship | Meaning |
|--------------|---------|
| **consumes** | Diff строится из snapshot (или snapshot-equivalent) inputs |
| **validates_capture** | Post-apply diff подтверждает или опровергает snapshot accuracy |
| **scopes_to** | Diff bundle может быть scoped к subset snapshot objects |

Snapshot Model ссылается на diff в validation usage («diff against pre-apply snapshot»); Diff Model **формализует** эту операцию.

### Diff → ChangeSet

| Relationship | Meaning |
|--------------|---------|
| **informs_draft** | Draft-stage diff поддерживает `description` и target selection |
| **pre_apply_baseline** | `source_a` часто = pre-apply snapshot ref в ChangeSet evidence |
| **post_apply_validation** | Post-apply diff — validation input; unexpected deltas → rollback consideration |
| **references** | ChangeSet optional field `diff_ref` or validation attachment (future operator convention) |

ChangeSet **выполняет** изменение; Diff **описывает** ожидаемое или фактическое delta вокруг run.

### Diff → Validation

| Relationship | Meaning |
|--------------|---------|
| **expected_delta** | Approved plan defines acceptable diff set (scope + severity ceiling) |
| **actual_delta** | Post-apply diff compared to expected |
| **validation_fail** | Critical/Major unexpected diff → validation fail → rollback path |

Согласование: `validate_change` operation (R0), Mission validation-first.

### Diff → Rollback

| Relationship | Meaning |
|--------------|---------|
| **rollback_scope** | Diff показывает, какие targets changed → what rollback must cover |
| **pre_post_compare** | Backup→live or backup→snapshot diff оценивает restore completeness |
| **post_rollback_check** | Snapshot→live diff after rollback confirms restoration |

Rollback **восстанавливает**; Diff **не восстанавливает**, только помогает выбрать scope и проверить результат.

---

## Diff Usage

### Inspection

- Compare two inspection captures to understand site evolution.
- Scoped diff (single page + shortcodes) reduces noise vs full-site compare.

### Validation

- Post-apply: expected diff (from draft/dry-run) vs actual diff (snapshot or live).
- Validation pass: actual delta ⊆ expected scope and severity within approved ceiling.

### Drift Detection

- Snapshot→Live State diff on schedule or before execute.
- Unexpected drift → execute refusal, re-inspect, or new ChangeSet — operator decision.

### Change Planning

- Snapshot baseline + intended change → predicted diff for draft ChangeSet.
- Operations Manifest **Draft** category (`draft_page_change`, etc.) produces plan/diff without apply.

### Rollback Planning

- Identify which `target_type` / `target_id` records changed since backup.
- Assess whether entity rollback sufficient or broader `restore_backup` needed.

### Capability Verification

- [Proven Capabilities](WPILOT-PROVEN-CAPABILITIES-v1.md) evidence may include diff summary («apply produced single shortcode modified, Moderate, as planned»).
- Diff alone **не доказывает** capability; requires completed operation + validation trail.

---

## Non Goals

Diff Model v1 **не является**:

| Non-goal | Clarification |
|----------|---------------|
| **Backup** | Не создаёт restore artifacts |
| **Restore** | Не выполняет write-back или hosting restore |
| **Runtime** | Не plugin process, не Cursor agent, не automated compare job |
| **Execution engine** | Не orchestrates apply, validate, rollback, or dry-run execute |
| **API contract** | Не REST endpoint map; plugin-mvp dry-run contracts отдельны |
| **Database schema** | Не таблицы persistence для diff store |
| **Full binary diff** | Не обязан byte-level diff всего сайта, БД или filesystem |
| **AI rewrite / suggestion** | Не генерирует изменения; только описывает observed deltas |

---

## Relationship To Core Model

Diff Model — **change layer**. Он **потребляет** state layer (Snapshot) и **информирует** change management layers.

| Layer | Relationship to Diff Model |
|-------|---------------------------|
| **Mission** | Supports evidence-driven, validation-first, inspection-before-change; diff makes change visible |
| **Operations Manifest** | Draft operations produce planned diff; validation operations consume actual diff |
| **Risk Classes** | Diff severity informs review; does not replace R0–R5 |
| **Targets** | `target_type` / `target_id` on diff objects aligned with Target Registry |
| **Bindings** | Allowed operation→target pairs scope which diffs are in-policy |
| **ChangeSet** | Pre/post apply diff supports lifecycle and evidence |
| **Rollback** | Diff scopes rollback; rollback source remains backup/snapshot artifact |
| **Proven Capabilities** | Evidence may reference diff summaries from proven runs |
| **Site Snapshot** | Primary state input for compare; Snapshot = state, Diff = delta |

Suggested logical placement (documentation only):

```
Mission
   ↓
Site Snapshot Model     ← state / observation layer
   ↓
Diff Model              ← change / comparison layer
   ↓
Operations Manifest → Risk → Bindings → ChangeSet → Rollback
   ↓
Target Registry (taxonomy shared with diff objects)
   ↓
Proven Capabilities (evidence register; may reference diffs)
```

---

## Notes

- **Diff Model = change layer.** Описывает *что изменилось между состояниями*, не *полное состояние* и не *как восстановить*.
- **Snapshot Model = state layer.** Snapshot фиксирует *что есть*; Diff сравнивает *два «что есть»* или *snapshot с live*.
- Diff bundles могут получать stable id (`diff_bundle_id`) в operator workflow; v1 не задаёт format persistence.
- Partial diff — **норма**; full-site diff — aspirational and expensive, not default.
- При конфликте diff evidence и operator observation — **operator verified source** wins for planning; re-capture recommended.
- Plugin dry-run checksum mismatch is an **implementation signal** aligned with Snapshot→Live diff at Content level; see [dry-run-model-v0.md](plugin-mvp/dry-run-model-v0.md) for execute gate semantics.

---

## Differentiation From Related Documents

| Document | Role | How Diff Model differs |
|----------|------|------------------------|
| [WPILOT-SITE-SNAPSHOT-MODEL-v1.md](WPILOT-SITE-SNAPSHOT-MODEL-v1.md) | State layer — what site **is** at capture | Snapshot = state; Diff = **comparison** between states |
| [WPILOT-CHANGESET-v1.md](WPILOT-CHANGESET-v1.md) | Change execution unit with lifecycle | ChangeSet = **run container**; Diff = **description of delta** around run |
| [WPILOT-ROLLBACK-v1.md](WPILOT-ROLLBACK-v1.md) | Rollback policy and sources | Rollback = **restore**; Diff = **what changed**, informs scope |
| [plugin-mvp/dry-run-model-v0.md](plugin-mvp/dry-run-model-v0.md) | Plugin no-mutation preview before execute | Dry-run = **planned** single-target replacement preview; Diff Model = **general** logical compare layer |
| [backup-rollback-rules.md](backup-rollback-rules.md) | Operational backup discipline | Backup rules = when/how to backup; Diff may compare backup state but does not create backup |
| [metacode-wpilot-plugin-concept.md](metacode-wpilot-plugin-concept.md) | Plugin concept mentions «diff preview» | Concept = product direction; Diff Model v1 = **canonical policy structure** for deltas |

No duplicate Diff Model document existed before v1. Terminology overlap («diff» in dry-run, draft operations, checksum preview) refers to **operational or plugin-local preview**, not this canonical change layer unless explicitly linked.

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v1 |
| Implements runtime | No |
| Replaces Site Snapshot Model | No |
| Replaces ChangeSet | No |
| Replaces Rollback | No |
| Replaces plugin dry-run contract | No |
