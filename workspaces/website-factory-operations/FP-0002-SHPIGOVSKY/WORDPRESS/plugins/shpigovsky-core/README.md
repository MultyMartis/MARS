# Shpigovsky Core — V9-06C.1 Content Model Source

**Status:** `V9-06C.1 SOURCE ACTIVATION GATE RESOLVED` / `NO RUNTIME DELIVERY PERFORMED`
**Version:** `0.3.1-v9-06c1-source`

## Purpose

Canonical project plugin source for FP-0002. Establishes namespace/autoload boundary, module contracts, and V9-06C source implementations for CPT, permalinks, ACF field groups, options page, admin UX, and validation hooks. V9-06C.1 resolves the coarse skeleton gate in source by using a phase-aware activation registry.

## Module map

| Module | Path | V9-06C.1 source state |
|--------|------|:-----------------:|
| Service CPT | `src/ContentTypes/Service.php` | enabled in `content_model` |
| Service permalinks | `src/Permalinks/ServicePermalinks.php` | enabled in `content_model` |
| ACF integration | `src/Fields/AcfIntegration.php` | enabled in `content_model` when ACF exists |
| ACF field groups | `src/Fields/FieldGroups.php` | enabled in `content_model` when ACF PRO exists |
| Repeater validation | `src/Fields/RepeaterValidation.php` | enabled in `content_model` when ACF PRO exists |
| Site settings | `src/Settings/SiteSettings.php` | enabled in `content_model` when ACF PRO exists |
| Migrations | `src/Migrations/MigrationRunner.php` | disabled until V9-06D2 or later |
| Consultation form | `src/Forms/ConsultationHandler.php` | disabled until later phase |
| Options pages | `src/Admin/OptionsPage.php` | enabled in `content_model` when ACF PRO exists |
| Editor restrictions | `src/Admin/EditorRestrictions.php` | enabled in `content_model` |
| Taxonomies | `src/Taxonomies/` | rejected (empty) |

## Source mode

`SHPIGOVSKY_CORE_MODE` defaults to `content_model`. `SHPIGOVSKY_CORE_SKELETON` remains only as a derived compatibility constant and is false unless mode is explicitly `skeleton`.

V9-06C.1 is source-only. It does not deliver runtime files, create WordPress objects, run migrations, flush rewrites, update options, or use ACF Extended PRO APIs.

## Architecture reference

- `WORDPRESS/architecture/FP-0002-THEME-PLUGIN-SKELETON-PLAN-v1.md`
- `WORDPRESS/architecture/FP-0002-WORDPRESS-ARCHITECTURE-v1.md`
