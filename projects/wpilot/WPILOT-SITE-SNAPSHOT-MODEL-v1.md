# WPilot Site Snapshot Model v1

**Classification:** State layer — canonical site state description model.
**Status:** Documented v1; logical model only.
**Related:** [WPILOT-MISSION-v1.md](WPILOT-MISSION-v1.md), [WPILOT-OPERATIONS-MANIFEST-v1.md](WPILOT-OPERATIONS-MANIFEST-v1.md), [WPILOT-TARGET-REGISTRY-v1.md](WPILOT-TARGET-REGISTRY-v1.md), [WPILOT-CHANGESET-v1.md](WPILOT-CHANGESET-v1.md), [WPILOT-ROLLBACK-v1.md](WPILOT-ROLLBACK-v1.md), [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md)

---

## Purpose

**Site Snapshot** — каноническое, структурированное описание состояния WordPress-сайта в конкретный момент времени.

Snapshot фиксирует **что есть на сайте сейчас** (или на момент acquisition), а не **что должно быть изменено** и не **как выполнить изменение**.

WPilot использует Site Snapshot как общий state layer для:

- inspection — понимание текущего состояния перед операцией;
- validation — сравнение фактического состояния с ожидаемым после apply;
- change planning — выбор целей, scope и риска на основе реального состояния;
- rollback planning — определение восстановимых точек и gaps в coverage;
- capability proof — привязка evidence к конкретному состоянию сайта.

### Snapshot ≠ Backup

| Аспект | Site Snapshot | Backup |
|--------|---------------|--------|
| **Назначение** | Описание и структурирование состояния | Восстановление состояния |
| **Форма** | Логическая модель объектов, связей, evidence refs | Артефакт restore (файл, export, hosting bundle) |
| **Полнота** | Может быть partial, scoped, level-specific | Должен покрывать restore scope или явно помечать gaps |
| **Использование** | Read, compare, plan, validate | Write-back, restore, rollback apply |
| **Policy layer** | State description | Recovery source (см. [Rollback v1](WPILOT-ROLLBACK-v1.md)) |

Snapshot **может ссылаться** на backup artifacts как evidence, но **не заменяет** backup и **не выполняет** restore.

Snapshot = **структурированное описание состояния сайта**, а не копия файлов, не дамп БД и не hosting-level bundle.

Наличие Site Snapshot Model v1 **не означает** runtime, API, plugin storage schema, automated acquisition pipeline или persisted snapshot store.

---

## Snapshot Scope

Snapshot описывает области сайта, которые WPilot может inspect, validate, plan или rollback-scope.

Минимальный канонический scope v1:

| Scope area | Описание | Типичный snapshot level |
|------------|----------|-------------------------|
| **site identity** | Label, URL/domain (sanitized), environment class (test/prod/SAFE UNKNOWN), owner context | L0 |
| **environment** | WP version signals, PHP/hosting hints, indexing, DEV/prod markers | L4 |
| **pages** | Список и атрибуты страниц: ID, slug, title, status, content refs | L2 |
| **posts** | Записи и public custom post types (кроме page) | L2 |
| **shortcodes** | Именованные shortcode-регионы в контенте (в т.ч. builder blocks) | L2 |
| **menus** | Меню навигации, пункты, привязки | L1 |
| **header** | Header-зона: template refs, embedded shortcodes, menu/widget refs | L1 |
| **footer** | Footer-зона: template refs, embedded shortcodes, contact blocks | L1 |
| **css fragments** | Scoped CSS: child theme patches, page-local CSS, isolated blocks | L3 |
| **active theme** | Активная тема, child theme presence, theme signals (The7 и др.) | L3 |
| **active plugins** | Список активных плагинов и версий (visibility-dependent) | L3 |
| **media references** | Ссылки на медиа: attachment IDs, URLs (sanitized), alt, usage refs | L2 / L3 |

Snapshot **может быть partial**: оператор или workflow фиксирует только scope, нужный для конкретной операции (например, одна page + связанные shortcodes). Partial snapshot **обязан** явно указывать `scope` и не притворяться full-site capture.

Области вне минимального scope (widgets, theme_option, database, filesystem, credentials) могут входить в snapshot по charter, но **не обязаны** присутствовать в каждом snapshot.

Согласование с [Target Registry v1](WPILOT-TARGET-REGISTRY-v1.md): scope areas map к `target_type`, но snapshot описывает **состояние**, а Target Registry — **допустимые цели операций**.

---

## Snapshot Levels

Уровни snapshot задают **глубину и granularity** описания, не risk class и не operation category.

```
L0 — Site Identity
   ↓
L1 — Structure
   ↓
L2 — Content
   ↓
L3 — Configuration
   ↓
L4 — Environment
```

| Level | Name | Что фиксирует | Типичные объекты |
|-------|------|---------------|------------------|
| **L0** | Site Identity | Кто/где/какой сайт; sanitized identity без secrets | `site`, identity record |
| **L1** | Structure | Структурные зоны и навигация | `menu`, `header`, `footer`, structural refs |
| **L2** | Content | Контентные сущности и встроенные фрагменты | `page`, `post`, `shortcode`, media refs in content |
| **L3** | Configuration | Theme, plugins, scoped CSS и config-visible state | `active_theme`, `active_plugins`, `css_fragment`, `theme_option` |
| **L4** | Environment | Hosting/runtime/context signals | `environment`, WP/PHP visibility, indexing |

### Level rules

- Snapshot **может** останавливаться на любом level (например, L0+L2 для page-scoped inspection).
- Более высокий level **не подразумевает** автоматическое наличие всех объектов нижних levels — только явно captured objects.
- ChangeSet и Rollback **могут ссылаться** на snapshot level как на baseline для validation и rollback planning.
- L4 **не заменяет** hosting backup или environment rollback; см. [Rollback v1](WPILOT-ROLLBACK-v1.md) environment scope.

---

## Snapshot Objects

Каждый зафиксированный элемент состояния представляется как **snapshot object**.

### Canonical object fields

| Field | Required | Description |
|-------|----------|-------------|
| **object_type** | yes | Тип объекта; канонически aligned с `target_type` из Target Registry где применимо |
| **object_id** | yes | Стабильный идентификатор: slug, numeric ID, zone name, fragment key |
| **source** | yes | Откуда получено описание (см. Evidence) |
| **scope** | yes | `full_site` \| `entity` \| `zone` \| `fragment` — granularity capture |
| **notes** | no | Operator notes, SAFE UNKNOWN markers, capture limitations |

### Object catalog v1

| object_type | object_id examples | Typical scope | notes |
|-------------|-------------------|---------------|-------|
| **site** | `dev.gktriumph.ru`, `site_label:gktriumph-dev` | full_site | L0 anchor; sanitized URL only |
| **environment** | `env:dev`, `hosting:beget` | full_site | L4; visibility may be partial |
| **page** | `page_id:69`, `contacts` | entity | L2; content may be ref-only or inline per evidence |
| **post** | `post_id:17`, `news-slug` | entity | L2 |
| **shortcode** | `footer_contacts`, `vc_row:hero` | fragment | L2; often nested in page/footer/header |
| **menu** | `primary`, `menu_id:3` | zone | L1 |
| **header** | `header:main` | zone | L1; may reference menus/shortcodes |
| **footer** | `footer:main` | zone | L1 |
| **css_fragment** | `child-theme:custom.css`, `page:69:inline` | fragment | L3 |
| **active_theme** | `the7`, `the7-child` | full_site | L3 |
| **active_plugins** | `plugins:active_list` | full_site | L3; list object, not per-plugin mutation target by default |
| **media** | `attachment_id:102`, `media:logo-header` | entity / fragment | L2–L3; refs preferred over binary inline |
| **plugin** | `metacode-wpilot` | entity | L3; single plugin entry when disambiguation needed |

**object_type** использует snake_case и по возможности совпадает с [Target Registry](WPILOT-TARGET-REGISTRY-v1.md) `target_id`. Snapshot object описывает **наблюдаемое состояние**; target описывает **допустимую цель операции**.

---

## Snapshot Relationships

Snapshot objects связаны directed relationships для navigation, impact analysis и rollback scope reasoning.

### Canonical relationship types

| Relationship | From → To | Meaning |
|--------------|-----------|---------|
| **contains** | site → pages | Site includes page objects |
| **contains** | site → menus | Site includes menu objects |
| **contains** | site → active_theme | Site uses theme state |
| **contains** | site → active_plugins | Site runs plugin set |
| **hosts** | page → shortcode | Page content contains shortcode fragment |
| **hosts** | footer → shortcode | Footer zone contains shortcode fragment |
| **hosts** | header → shortcode | Header zone contains shortcode fragment |
| **references** | page → media | Page content references media attachment |
| **uses** | header → menu | Header zone uses menu |
| **uses** | footer → menu | Footer zone may use menu |
| **depends_on** | css_fragment → active_theme | CSS patch scoped to theme context |
| **scoped_to** | shortcode → page | Shortcode located within page (when not global) |
| **scoped_to** | css_fragment → page | Page-local CSS |

### Example relationship graph (illustrative)

```
site
 ├── pages (page:contacts, page:cargo-taxi, …)
 ├── menus (menu:primary)
 ├── active_theme (the7-child)
 ├── active_plugins (plugins:active_list)
 └── environment (env:dev)

page:contacts
 └── shortcode:footer_contacts

footer:main
 └── shortcode:footer_contacts

page:cargo-taxi
 ├── shortcode:hero_block
 └── media:attachment_id:102
```

Relationships **не выполняют** cascade restore. Они помогают оператору и workflow понять **что затронет изменение** и **какой evidence нужен для validation**.

---

## Snapshot Evidence

Snapshot object или snapshot bundle **опирается на evidence** — наблюдаемый источник, из которого состояние было получено или подтверждено.

### Evidence types v1

| Evidence type | Description | Typical use |
|---------------|-------------|-------------|
| **HTML** | Rendered page HTML, zone HTML, sanitized capture | Visual/structure validation, shortcode presence |
| **REST** | WordPress REST response (pages, posts, site info, plugins where exposed) | Structured inspection, plugin MVP read path |
| **WP content** | `post_content`, raw storage, builder-encoded content | Pre/post apply compare, shortcode inspection |
| **Export** | Sanitized export fragment (JSON, text, scoped file) | Offline review, rollback source ref |
| **Operator verified source** | Human-confirmed fact from admin, hosting panel, or manual check | Fills SAFE UNKNOWN; highest trust for gaps |

### Evidence rules

- Каждый snapshot object **должен** иметь хотя бы один evidence ref или явный `SAFE UNKNOWN` в `notes`.
- Evidence **не коммитится** в git, если содержит secrets, PII или full credentials — см. [local-storage-policy.md](local-storage-policy.md).
- HTML snapshot как evidence **≠** Site Snapshot Model: HTML — **источник**; Site Snapshot — **структурированная интерпретация** состояния.
- Pre-apply backup (`content_before`, backup path) — evidence для rollback, может **feed** snapshot object state at capture time, но остаётся recovery artifact по [Rollback v1](WPILOT-ROLLBACK-v1.md).

### Evidence quality markers (optional in notes)

| Marker | Meaning |
|--------|---------|
| `verified` | Operator or validation confirmed match |
| `stale` | Capture older than current run; re-inspect recommended |
| `partial` | Only subset of object captured |
| `inferred` | Derived from related object, not direct read |

---

## Snapshot Usage

### Inspection

- Baseline перед `inspect_*` operations: какие объекты уже известны, какие — SAFE UNKNOWN.
- Scoped snapshot (например, L2 page + shortcodes) снижает повторные read и фиксирует inspection context.

### Validation

- Post-apply: новый partial snapshot или diff against pre-apply snapshot.
- Validation evidence привязывается к snapshot objects (page renders, shortcode present, CSS applied).

### ChangeSet planning

- ChangeSet `target_type` / `target_id` **выбираются** с учётом snapshot: объект существует, scope понятен, relationships известны.
- `description` ChangeSet может ссылаться на `snapshot_id` или capture timestamp как baseline ref.

### Rollback planning

- Pre-apply snapshot (или backup-derived state) определяет **ожидаемое состояние после rollback**.
- Relationship graph показывает, нужен ли entity-only rollback или broader scope.

### Capability proof

- [Proven Capabilities v1](WPILOT-PROVEN-CAPABILITIES-v1.md) может ссылаться на snapshot capture как контекст evidence («inspection proven on page 69 with REST + HTML evidence»).
- Snapshot **не доказывает** capability сам по себе; proof требует completed operation + validation + evidence trail.

---

## Relationship To Existing Layers

Site Snapshot Model — **state layer**. Он не заменяет policy layers ниже; он **питает** их фактическим контекстом.

| Layer | Relationship to Site Snapshot |
|-------|------------------------------|
| **Mission** | Snapshot поддерживает evidence-driven, validation-first, inspection-before-change principles |
| **Operations Manifest** | Inspection/apply operations **consume** snapshot scope; snapshot не добавляет новых `operation_id` |
| **Risk Classes** | Snapshot depth не меняет R0–R5; incomplete snapshot may increase operator caution, not auto-elevate risk |
| **Target Registry** | `object_type` aligned с `target_type`; snapshot = observed state, registry = operable targets |
| **Operation Bindings** | Bindings определяют допустимые operation→target pairs; snapshot подтверждает target existence |
| **ChangeSet** | Pre-apply snapshot / baseline ref для planning; post-apply snapshot для validation closeout |
| **Rollback** | Snapshot describes expected post-rollback state; backup remains rollback **source** |
| **Proven Capabilities** | Evidence may reference snapshot captures; proven status still requires executed operation proof |

Suggested logical placement in WPilot model (documentation only):

```
Mission
   ↓
Site Snapshot Model  ← state / observation layer
   ↓
Operations Manifest → Risk → Bindings → ChangeSet → Rollback
   ↓
Target Registry (taxonomy shared with snapshot objects)
   ↓
Proven Capabilities (evidence register; may reference snapshots)
```

---

## Non Goals

Site Snapshot Model v1 **не является**:

| Non-goal | Clarification |
|----------|---------------|
| **Backup** | Не создаёт restore artifacts; см. Rollback, backup-rollback-rules |
| **Restore** | Не выполняет write-back или hosting restore |
| **Runtime** | Не plugin process, не Cursor agent, не automated job |
| **Execution engine** | Не orchestrates apply, validate, or rollback |
| **API contract** | Не REST endpoint map; plugin-mvp contracts отдельны |
| **Database schema** | Не таблицы `{prefix}wpilot_*`; см. plugin-mvp/storage-model-v0 |
| **Site passport** | Не operator template; см. templates/site-passport-template.md |
| **Full-site mirror** | Не обязан capture every file, option, or DB row |

---

## Notes

- **Snapshot Model = state layer.** Описывает *что зафиксировано о сайте*, не *как это изменить* и не *как восстановить*.
- Snapshot bundles могут получать stable id (`snapshot_id`) в operator workflow; v1 не задаёт format persistence.
- Partial snapshots — **норма** для MVP и human-supervised runs; full-site snapshot — aspirational, not default.
- При конфликте между snapshot evidence и operator live observation — **operator verified source** wins для planning; re-capture recommended.
- Factory-native sites (Mode A) могут в будущем поставлять structured snapshot payloads from Website Factory; legacy sites (Mode B) rely on inspection-acquired partial snapshots.

---

## Differentiation From Related Documents

| Document | Role | How Site Snapshot Model differs |
|----------|------|--------------------------------|
| [templates/site-passport-template.md](templates/site-passport-template.md) | Operator checklist for sanitized site facts | Passport = manual fact sheet; Snapshot Model = canonical object/relationship/evidence structure |
| [plugin-mvp/storage-model-v0.md](plugin-mvp/storage-model-v0.md) | Planned plugin DB tables for backups/audit | Storage model = implementation persistence; Snapshot Model = logical state description |
| [backup-rollback-rules.md](backup-rollback-rules.md) | Operational backup/rollback discipline | Backup rules = when/how to backup; Snapshot = describe state, not store restore bundle |
| [local-storage-policy.md](local-storage-policy.md) | Local-only artifact paths | Policy for where HTML/JSON backups live; Snapshot may reference those paths as evidence |
| [WPILOT-ROLLBACK-v1.md](WPILOT-ROLLBACK-v1.md) | Rollback policy and sources | Rollback uses backup/snapshot **artifacts** as sources; Site Snapshot describes **expected state** after restore |
| [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md) | Evidence register of proven ops | Proven Capabilities = what was **done**; Site Snapshot = what the site **was/is** at capture time |

No duplicate document exists. Terminology overlap («snapshot» in backup/HTML context) is **operational artifact naming**, not this state model.
