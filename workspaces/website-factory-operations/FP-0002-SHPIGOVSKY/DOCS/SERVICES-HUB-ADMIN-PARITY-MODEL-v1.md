# FP-0002 — Services Hub Admin Parity Model v1

**Status:** ACCEPTED / FROZEN (local) — V9-06E44  
**Date:** 2026-07-14  
**Task:** V9-06E43 + V9-06E43-FIX01; freeze V9-06E44  
**Local URL:** http://shpigovsky.test/uslugi/  
**Services hub page ID:** `#5`  
**Template:** `page-templates/services-hub.php`  
**Canonical ACF group:** `group_fp02_page_services_hub` (DB publish `#1628`)

This document describes the Services hub admin/frontend architecture after E43 / E43-FIX01.  
Services hub is **frozen** as of V9-06E44 (`REPORTS/FREEZE-FP-0002-V9-06E44-SERVICES-HUB-ACCEPTED.md`).  
Next scope after freeze: service CPT layout-variant governance (`DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`) — **not** hub product redesign.  
It follows the Home model (`DOCS/HOME-PAGE-ADMIN-PARITY-MODEL-v1.md`) but is **page-specific**.  
It is **not** a production or hosting claim.

---

## Architecture summary

### Frontend is canon

- Render order is defined by `page-templates/services-hub.php` → partials.
- Admin ACF field order follows that sequence.
- Visual design for hero remains `services-inner-hero-v2` (not Home `.hero--home`).

### Direct-edit vs automated blocks

| Class | Meaning | Services hub admin role |
|-------|---------|-------------------------|
| **Direct editable** | Values on page #5 ACF | Slides, program copy, FAQ, secondary CTA |
| **Automated / external** | CPT or reusable blocks | Visibility toggle + notices |
| **Partial** | Intro/settings on hub; cards from elsewhere | Mix |
| **Legacy** | Pre-E43 hero scalars | Hidden (`fp02-acf-legacy-retired`); fallback only |

### Hero slider

- Repeater: `services_hero_slides` (eyebrow, title, lead, image, cta_label, item_enabled).
- Settings: `services_hero_autoplay_*`, `services_hero_arrows_enabled`, `services_hero_dots_enabled`.
- Swiper local vendor; init `[data-services-hero-slider]`.
- One slide: no Swiper attrs/nav (appearance preserved).
- Multi-slide: keep shell `min-height: 320px` (avoid Home-style height collapse).

### Toggles (default ON)

- `services_hub_nav_visible`
- `services_hub_catalog_visible`
- `services_hub_category_gallery_dots_enabled`
- `services_hub_program_visible`
- `services_hub_founder_quote_visible`
- `services_hub_comfort_visible`
- `services_hub_secondary_cta_visible`
- `services_hub_faq_visible`
- `services_hub_final_form_visible`

### Localization

- RU labels via `__()` / text domain `shpigovsky-core` (plugin FieldGroups) and `shpigovsky` (theme).
- Admin section titles: `.fp02-acf-section-title` (~20px) via `admin-home-acf.css` on Services hub edit screen.

### Source / runtime

1. Backup first.
2. Patch source under `WORDPRESS/`; deliver matching PHP/JS/admin CSS to runtime.
3. Operator `v9-style.css`: additive E43 rules only (do not overwrite operator deltas).
4. Persist selectively only under explicit charter.

### Generated category sections (E43-FIX01)

Root/higher-level service CPT objects (not taxonomy terms) drive `.services-category-section-v2` blocks.

| Frontend class | Admin field | Object | Notes |
|----------------|-------------|--------|-------|
| `__intro` | `service_short_description` (Мини-описание) | root service (`subdivision`) | Same field as leaf cards; for roots also category intro |
| `__lead` | `service_category_section_lead` | root service (`subdivision` only in admin) | New textarea; V9 static fallback if empty |

Resolve helpers (theme): `shpigovsky_resolve_services_hub_category_intro()`, `shpigovsky_resolve_services_hub_category_lead()`.

Current roots: `#73` Зависимости, `#77` Психическое здоровье, `#84` Расстройства пищевого поведения.

### Explicitly out of this model

- Full service category page admin parity (beyond hub intro/lead)
- Service leaf page admin parity
- Home product changes (frozen E42)
- Unfreezing `/uslugi/` without an explicit charter (frozen E44)
- Replacing `service_layout_variant` technical enum without Option B implementation task
