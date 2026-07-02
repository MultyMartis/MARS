# Shpigovsky Core — V9-06B Skeleton

**Status:** `V9-06B SKELETON` / `NO CONTENT MODEL REGISTERED`  
**Version:** `0.2.0-skeleton`

## Purpose

Canonical project plugin skeleton for FP-0002. Establishes namespace/autoload boundary, module contracts, and future module locations — without registering CPT, permalinks, ACF fields, forms, or migrations at runtime.

## Module map

| Module | Path | Enabled in V9-06B |
|--------|------|:-----------------:|
| Service CPT | `src/ContentTypes/Service.php` | no |
| Service permalinks | `src/Permalinks/ServicePermalinks.php` | no |
| ACF integration | `src/Fields/AcfIntegration.php` | no |
| Repeater validation | `src/Fields/RepeaterValidation.php` | no |
| Site settings | `src/Settings/SiteSettings.php` | no |
| Migrations | `src/Migrations/MigrationRunner.php` | no |
| Consultation form | `src/Forms/ConsultationHandler.php` | no |
| Options pages | `src/Admin/OptionsPage.php` | no |
| Editor restrictions | `src/Admin/EditorRestrictions.php` | no |
| Taxonomies | `src/Taxonomies/` | rejected (empty) |

## Skeleton mode

`SHPIGOVSKY_CORE_SKELETON` is `true`. All modules implement `ModuleInterface::is_enabled()` and remain inert until V9-06C authorization.

## Architecture reference

- `WORDPRESS/architecture/FP-0002-THEME-PLUGIN-SKELETON-PLAN-v1.md`
- `WORDPRESS/architecture/FP-0002-WORDPRESS-ARCHITECTURE-v1.md`
