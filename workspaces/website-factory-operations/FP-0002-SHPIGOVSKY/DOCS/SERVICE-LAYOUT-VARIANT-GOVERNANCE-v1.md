# FP-0002 — Service Layout Variant Governance v1

**Status:** Placeholder layout mode restored (local) — **V9-06E51** (builds on E45-FIX03 depth UI)  
**Date:** 2026-07-15  
**Field (technical):** `service_layout_variant` / `field_fp02_service_layout_variant`  
**Field (editor):** `service_editor_role` / `field_fp02_service_editor_role` (UI label: **Макет страницы услуги**)  
**Field (override):** `service_layout_override_enabled` / `field_fp02_service_layout_override_enabled` (**hidden** from normal admin UI)  
**Child block:** `service_child_services_enabled`, `service_child_services_heading`  
**ACF group:** `group_fp02_service_layout_hero`  
**Page stub field (generic templates):** `page_layout_mode` / `group_fp02_page_layout_mode`  
**Depth helper:** `shpigovsky_get_service_depth()` / `ServiceLayoutGovernance::get_service_depth()`

This document governs the service CPT layout selection for editors and developers.  
It is **not** a production claim and **not** a broad service-page redesign.

---

## 1. Operator model (E51)

### Depth rules

| Depth | Meaning | Admin UI | Effective layout |
|------:|---------|----------|------------------|
| 1 | First-level service (`post_parent = 0`) | Selector: **Раздел** / **Услуга** / **Заглушка** | `section`→`subdivision`, `service`→`service_general`, `placeholder`→`placeholder` |
| 2+ | Nested under another service | Selector: **Услуга** / **Заглушка** (no Раздел) | `service`→`service_general`, `placeholder`→`placeholder` |

**Confirmed first-level sections:** `#73` Зависимости, `#77` Психическое здоровье, `#84` РПП.  
Placeholder option is available on sections but **not** enabled by default.

### Заглушка behavior

When `service_editor_role=placeholder` (synced to `service_layout_variant=placeholder`):

- Frontend returns HTTP 200 with **header / navigation / H1 / footer only**.
- Stack partial: `template-parts/service/placeholder-stack.php`.
- ACF content (hero, service_general_*, section_*, repeaters) is **not deleted**.
- Switch back to Услуга/Раздел restores full rendering.

Test page (E51): `#78` Депрессия.

### Technical values (internal)

| Value | Role |
|-------|------|
| `subdivision` | Frontend stack for **Раздел** |
| `service_general` | Frontend stack for **Услуга** |
| `placeholder` | Frontend stub stack for **Заглушка** |
| `standard` / `extended` | Legacy → leaf |
| `alcohol_special` | Deprecated alias of `service_general` |

**Save sync (E51):**

- Nested + role `placeholder` → keep placeholder / layout `placeholder`
- Nested + other → `service` + `service_general`
- First-level → sync layout from selected role; override forced off

---

## 2. Effective frontend resolution

Authority: `shpigovsky_resolve_service_layout_variant()` in theme `inc/service-helpers.php`.

1. Role or layout `placeholder` → `placeholder` (**including nested**)
2. Depth ≥ 2 non-placeholder → `service-general`
3. Legacy override **on** (stale meta only) → map technical layout
4. Role `section` → `subdivision`
5. Role `service` → `service-general`
6. Else legacy layout / known roots / default `service-general`

ACF→theme map:

- `service_general` → `service-general`
- `alcohol_special` → `service-general` (legacy alias)
- `placeholder` → `placeholder`
- `standard` / `extended` → `leaf`
- `subdivision` → `subdivision`

Alcohol **static V9 copy** remains gated to known alcohol page `#74` / slug `lechenie-alkogolnoy-zavisimosti` — **not** by layout name.

---

## 3. Child services tile block

Unchanged from FIX01/FIX02 except: child-services CSS is **not** enqueued on placeholder pages.

---

## 4. Page generic stub mode

Pages using `page-templates/generic.php` may set ACF `page_layout_mode`:

- `full` (default) — generic content shell from ACF SoT (`group_fp02_page_generic_content`, V9-06E52)
- `placeholder` — H1 only

Dedicated templates (Home, `/uslugi/`, contacts, reviews, legal, institutional hub) are **out of this field** by design.

See also: `DOCS/GENERIC-PAGES-ADMIN-PARITY-MODEL-v1.md`.

---

## 5. History

- **E44:** audit + Option B recommendation
- **E45:** Option B with three editor types including placeholder
- **E45-FIX01:** two-type model; placeholder demoted from primary UI
- **E45-FIX02:** rename technical `alcohol_special` → `service_general`
- **E45-FIX03:** depth-based one-block selector; nested auto service
- **E51:** restore **Заглушка** as first-class layout mode + true stub frontend; `#78` test enable
- **E52:** generic pages ACF content SoT + empty-safe + placeholder for `generic.php`

---

## 6. Out of scope

Home freeze, `/uslugi/` hub redesign, hosting preview, Git persistence, foreign MARS projects, mass enabling placeholder on all demo pages.
