# WPilot Target Registry v1

**Classification:** Policy layer — canonical target taxonomy for WPilot operations.
**Status:** Documented v1; policy model only.
**Related:** [WPILOT-MISSION-v1.md](WPILOT-MISSION-v1.md), [WPILOT-OPERATIONS-MANIFEST-v1.md](WPILOT-OPERATIONS-MANIFEST-v1.md), [WPILOT-RISK-CLASSES-v1.md](WPILOT-RISK-CLASSES-v1.md), [WPILOT-CHANGESET-v1.md](WPILOT-CHANGESET-v1.md), [WPILOT-ROLLBACK-v1.md](WPILOT-ROLLBACK-v1.md)

---

## Purpose

**Target Registry** определяет канонический список целей (targets), на которые WPilot может воздействовать в рамках типизированных операций.

Target Registry отвечает на вопрос: **«На какие сущности может воздействовать WPilot?»**

Target Registry используется для:

- **Operations Manifest** — scope rules и привязка `operation_id` к допустимым целям
- **Risk Classes** — классификация воздействия по типу и scope цели
- **ChangeSets** — поля `target_type` и `target_id`
- **Rollback** — entity / site / environment rollback scope
- **будущих bindings** — Cursor workflow, dashboards, operator templates
- **будущих plugin endpoints** — mapping REST surface → canonical targets

Target Registry **не определяет реализацию**. Наличие target в реестре **не означает**, что соответствующий endpoint, API, БД или runtime уже существует.

---

## Design Principles

| Principle | Описание |
|-----------|----------|
| **Stable identifiers** | Каждая цель имеет стабильный `target_id` в snake_case. Идентификатор не меняется между версиями документации без явного charter review. |
| **Human-readable names** | Каждая цель имеет понятное имя для оператора, change request и audit trail. |
| **CMS-oriented targets** | Цели отражают WordPress/CMS-сущности и зоны сайта, а не произвольные технические артефакты. |
| **Scope-aware hierarchy** | Цели группируются по уровню воздействия: entity → site → environment. |
| **No runtime assumptions** | Реестр описывает policy layer. Он не предполагает plugin, REST API, database schema или automated enforcement. |

---

## Target Categories

Верхнеуровневые категории целей WPilot v1:

### Content Targets

Контентные сущности WordPress: страницы, записи, shortcode-фрагменты в контенте.

### Structure Targets

Структурные элементы сайта: виджеты, меню, header/footer-зоны.

### Configuration Targets

Настройки и scoped-патчи: CSS-фрагменты, theme options.

### Asset Targets

Медиа и вложения WordPress.

### Environment Targets

Сайт как целое и окружение (hosting/runtime layer).

---

## Canonical Targets

Канонический реестр целей v1:

| target_id | name | category | description |
|-----------|------|----------|-------------|
| **page** | Page | Content | WordPress page: метаданные, контент, slug, ID. |
| **post** | Post | Content | WordPress post (любой public post type, кроме page): метаданные, контент, тип, статус. |
| **shortcode** | Shortcode | Content | Именованный shortcode-фрагмент в контенте (в т.ч. WPBakery block / shortcoder entry). |
| **widget** | Widget | Structure | Виджет и его конфигурация в sidebar / widget area. |
| **menu** | Menu | Structure | Меню навигации и его пункты. |
| **header** | Header | Structure | Header-зона сайта: шаблон, контент, меню, виджеты в зоне header. |
| **footer** | Footer | Structure | Footer-зона сайта: шаблон, контент, виджеты, контактные блоки в зоне footer. |
| **css_fragment** | CSS Fragment | Configuration | Scoped CSS-патч: child theme fragment, page-local CSS, isolated stylesheet block. |
| **theme_option** | Theme Option | Configuration | Настройка темы (theme mod / theme option), без произвольных wp_options. |
| **media** | Media | Asset | Вложение медиатеки: файл, метаданные, alt, привязки. |
| **site** | Site | Environment | WordPress instance как целое: сводная инспекция, plugins list, theme state, общий статус. |
| **environment** | Environment | Environment | Hosting/runtime layer: WP version, PHP, indexing, DEV/prod hints, server-level signals. |

**Формат `target_id`:** snake_case, lowercase, без пробелов. Это канонический идентификатор для ChangeSet, scope rules и будущих bindings.

---

## Content Targets

### page

WordPress **page** — статическая страница с собственным slug, ID, title, content, meta.

Типичные операции: `inspect_page`, `draft_page_change`, `apply_content_change`.

Примеры `target_id`: `contacts`, `page_id:42`, `about-us`.

### post

WordPress **post** (и другие content post types, кроме page) — запись блога, новость, custom post type entry.

Типичные операции: `inspect_post`, `draft_content_change`, `apply_content_change`.

Примеры `target_id`: `news-item-slug`, `post_id:17`.

### shortcode

**Shortcode-фрагмент** — именованный блок внутри контента: WPBakery element, shortcoder entry, inline shortcode region.

Типичные операции: `inspect_shortcode`, `draft_shortcode_change`, `apply_shortcode_change`.

Примеры `target_id`: `footer_contacts`, `hero_block_1`, `vc_row:contacts-section`.

**Примечание:** shortcode — entity-level content target. Footer/header **zones** — structure targets (см. ниже). Операция может быть scoped к shortcode внутри footer, не смешивая уровни без явного `description`.

---

## Structure Targets

### widget

**Widget** — конфигурация виджета в конкретной widget area.

Типичные операции: `inspect_widget`, `draft_widget_change`.

Примеры `target_id`: `sidebar-1:text-3`, `footer-col-2:custom_html-1`.

Apply-операции для widget в Manifest v1 ограничены; write path — future extension.

### menu

**Menu** — WordPress navigation menu и его items.

Типичные операции: `inspect_menu`, `draft_menu_change`, `apply_menu_change`.

Примеры `target_id`: `primary`, `footer-nav`, `menu_id:3`.

### header

**Header zone** — зона header сайта как структурная единица: шаблон header, меню в header, виджеты, layout markers.

Типичные операции: `inspect_header`, `draft_header_change` (future), zone-specific draft/apply.

Примеры `target_id`: `site-header`, `header-main`, `the7-header-layout`.

Header — **site-scoped structure target**. Изменения в header часто затрагивают navigation и layout; risk class может эскалировать (R2 → R3).

### footer

**Footer zone** — зона footer сайта как структурная единица: шаблон footer, контактные блоки, виджеты, layout markers.

Типичные операции: `inspect_footer`, `draft_footer_change`, `apply_footer_change`.

Примеры `target_id`: `site-footer`, `footer-contacts-zone`, `footer-main`.

**Согласование с ChangeSet-примером:** операция `apply_footer_change` может менять footer **zone**, но конкретный механизм изменения (shortcode entry, widget, theme fragment) фиксируется в `description` и evidence. `target_type` для zone-level операций — `footer`; для точечного shortcode — `shortcode`.

---

## Configuration Targets

### css_fragment

**CSS Fragment** — изолированный CSS-патч, не site-wide stylesheet без явного scope.

Типичные операции: `inspect_css`, `draft_css_change`, `apply_css_change`.

Примеры `target_id`: `child-theme:footer-patch`, `page-local:contacts`, `scoped:header-spacing-fix`.

Scope rule (из Risk Classes): isolated fragment → R2; site-wide child theme CSS → R3/R4.

### theme_option

**Theme Option** — настройка активной темы (theme mod, theme-specific option).

Типичные операции: `inspect_theme_option` (read-only в Manifest v1).

Примеры `target_id`: `the7_footer_layout`, `logo_url`, `theme_mod:footer_columns`.

Write-операции для theme_option вне Manifest v1; future extension.

---

## Asset Targets

### media

**Media** — вложение WordPress Media Library.

Типичные операции: `inspect_media`.

Примеры `target_id`: `attachment_id:128`, `media:hero-banner.webp`, `logo-attachment`.

Write/apply для media вне Manifest v1; future extension.

---

## Environment Targets

### site

**Site** — WordPress instance как целое: активная тема, список плагинов, общий operational status, site passport reference.

Типичные операции: `inspect_site`.

Примеры `target_id`: `site-dev`, `site_passport:triumph-dev`, `primary`.

Site — не отдельная content entity; это aggregate inspection target для сводной read-only инспекции.

### environment

**Environment** — hosting/runtime layer вокруг WordPress instance.

Типичные операции: `inspect_environment`.

Примеры `target_id`: `wp_version`, `indexing`, `dev_prod_hint`, `php_runtime`.

#### Различие: site vs environment

| Аспект | **site** | **environment** |
|--------|----------|-------------------|
| **Уровень** | WordPress instance | Hosting / runtime layer |
| **Примеры** | active theme, plugins, site status | WP version, PHP, indexing, DEV/prod, server signals |
| **Типичный scope** | Site Scope (aggregate) | Environment Scope |
| **Write в v1** | Нет прямых apply | Нет прямых apply |

`site` отвечает на вопрос «что происходит **внутри** WordPress?». `environment` — «в каком **окружении** работает этот instance?».

---

## Scope Model

Три уровня scope для целей WPilot v1:

### Entity Scope

Отдельная именованная сущность или фрагмент. Минимальный blast radius.

| target_id |
|-----------|
| page |
| post |
| shortcode |
| widget |
| menu |
| media |

Entity scope соответствует R2 scoped changes в большинстве Triumph-паттернов.

### Site Scope

Структурные зоны и конфигурация, затрагивающие layout/navigation сайта шире одного content fragment.

| target_id |
|-----------|
| header |
| footer |
| theme_option |
| css_fragment |

Site scope часто соответствует R2 (isolated css_fragment) или R3 (menus, site-wide css, header/footer layout).

### Environment Scope

Сайт как целое или hosting/runtime layer.

| target_id |
|-----------|
| site |
| environment |

Environment scope соответствует aggregate inspection (R0) и wide-scope recovery (`restore_backup` → R4).

---

## Relationship To Operations

Target Registry является источником допустимых значений для scope rules в [Operations Manifest](WPILOT-OPERATIONS-MANIFEST-v1.md).

Примеры привязки `operation_id` → canonical target:

| operation_id | primary target_id | notes |
|--------------|-------------------|-------|
| `inspect_page` | page | Read-only entity inspection |
| `inspect_post` | post | Read-only entity inspection |
| `inspect_shortcode` | shortcode | Read-only fragment inspection |
| `inspect_widget` | widget | Read-only structure inspection |
| `inspect_menu` | menu | Read-only structure inspection |
| `inspect_header` | header | Read-only zone inspection |
| `inspect_footer` | footer | Read-only zone inspection |
| `inspect_css` | css_fragment | Read-only configuration inspection |
| `inspect_theme_option` | theme_option | Read-only; write outside v1 |
| `inspect_media` | media | Read-only asset inspection |
| `inspect_site` | site | Aggregate site inspection |
| `inspect_environment` | environment | Runtime/hosting inspection |
| `draft_page_change` | page | Draft without apply |
| `draft_shortcode_change` | shortcode | Draft without apply |
| `draft_footer_change` | footer | Zone-level draft |
| `draft_menu_change` | menu | Draft without apply |
| `draft_widget_change` | widget | Draft without apply |
| `draft_css_change` | css_fragment | Draft without apply |
| `draft_content_change` | page **or** post | Polymorphic; `target_type` обязателен |
| `apply_content_change` | page **or** post | Scoped field-level apply |
| `apply_shortcode_change` | shortcode | Scoped fragment apply |
| `apply_footer_change` | footer | Zone-level apply |
| `apply_menu_change` | menu | Site navigation apply |
| `apply_css_change` | css_fragment | Scoped CSS apply |
| `rollback_change` | **varies** | Follows parent ChangeSet `target_type` |
| `restore_backup` | **varies** | Entity / site / environment by scope |
| `validate_change` | **varies** | Inherits target from parent ChangeSet |

Операции без фиксированного target до runtime resolution:

- **`apply_change`** — umbrella operation; blocked until subtype resolves to concrete target
- **`restore_backup`** — target определяется scope backup (entity → page/shortcode/…; wide → site/environment)
- **`rollback_change`** — target наследуется от ChangeSet, который откатывается

---

## Relationship To ChangeSets

Каждый ChangeSet использует:

| Field | Source |
|-------|--------|
| **target_type** | Canonical `target_id` из Target Registry |
| **target_id** | Operator-defined identifier: slug, ID, zone name, fragment key |

Target Registry является **источником допустимых значений** для `target_type`.

Правила v1:

- `target_type` **должен** быть одним из canonical `target_id` из таблицы Canonical Targets.
- `target_id` **должен** однозначно идентифицировать цель до стадии Apply.
- Одна apply-операция в одном ChangeSet — **одна именованная цель** (или явно ограниченный набор в `description`).
- Массовые или неограниченные цели **не входят** в v1.

Согласование с [ChangeSet Target Types](WPILOT-CHANGESET-v1.md): ChangeSet v1 enum синхронизирован с Target Registry v1; реестр остаётся **каноническим источником** для `target_type`.

---

## Relationship To Rollback

[Rollback Scope](WPILOT-ROLLBACK-v1.md) определяется через Target Registry и Scope Model.

| Rollback level | Targets | Typical operations |
|----------------|---------|-------------------|
| **Entity Rollback** | page, post, shortcode, widget, menu, media, css_fragment | `rollback_change` with ChangeSet backup |
| **Site Rollback** | header, footer, menu, theme_option, css_fragment (site-wide), multiple entities | `rollback_change`; coordinated scope in `description` |
| **Environment Rollback** | site, environment | `restore_backup`; hosting snapshot |

Rollback source selection зависит от `target_type`:

- Entity scope → ChangeSet backup preferred
- Site scope → ChangeSet backup or operator-verified export
- Environment scope → hosting backup, full snapshot (R4)

---

## Future Extensions

Возможны новые targets в будущих версиях реестра:

| Future target_id | Category | Notes |
|------------------|----------|-------|
| **taxonomy** | Content | Categories, tags, custom taxonomies |
| **comment** | Content | Comments and moderation |
| **user** | Configuration | WordPress users and roles |
| **form** | Structure | Contact forms, CF7, form plugins |
| **seo_object** | Configuration | SEO metadata objects (Yoast, RankMath) |
| **plugin** | Environment | Plugin-level inspection/write (currently `inspect_plugin` without dedicated target) |

Эти targets **не входят в v1**. Добавление требует charter review и обновления Manifest, Risk Classes, ChangeSet.

---

## Notes

Target Registry является **policy/documentation layer**.

Он **не требует**:

- plugin implementation
- API
- database
- runtime
- automated target validation

Human-supervised model из [Mission Charter](WPILOT-MISSION-v1.md) сохраняется: наличие target в реестре не даёт WPilot автономного authority над WordPress.

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v1 |
| Implements runtime | No |
| Replaces Operations Manifest | No |
| Replaces ChangeSet | No |
| Replaces Rollback | No |
| Canonical source for `target_type` | Yes |
