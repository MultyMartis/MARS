# Shpigovsky Core — V9-06C Content Model Source

**Status:** `V9-06C SOURCE IMPLEMENTED` / `NO RUNTIME CONTENT MODEL REGISTERED`
**Version:** `0.3.0-v9-06c-source`

## Purpose

Canonical project plugin source for FP-0002. Establishes namespace/autoload boundary, module contracts, and V9-06C source implementations for CPT, permalinks, ACF field groups, options page, admin UX, and validation hooks — without registering them in runtime while skeleton mode is enabled.

## Module map

| Module | Path | Enabled in V9-06B |
|--------|------|:-----------------:|
| Service CPT | `src/ContentTypes/Service.php` | source implemented, runtime gated |
| Service permalinks | `src/Permalinks/ServicePermalinks.php` | source implemented, runtime gated |
| ACF integration | `src/Fields/AcfIntegration.php` | source implemented, runtime gated |
| ACF field groups | `src/Fields/FieldGroups.php` | source implemented, runtime gated |
| Repeater validation | `src/Fields/RepeaterValidation.php` | source implemented, runtime gated |
| Site settings | `src/Settings/SiteSettings.php` | source implemented, runtime gated |
| Migrations | `src/Migrations/MigrationRunner.php` | no |
| Consultation form | `src/Forms/ConsultationHandler.php` | no |
| Options pages | `src/Admin/OptionsPage.php` | source implemented, runtime gated |
| Editor restrictions | `src/Admin/EditorRestrictions.php` | source implemented, runtime gated |
| Taxonomies | `src/Taxonomies/` | rejected (empty) |

## Skeleton mode

`SHPIGOVSKY_CORE_SKELETON` is `true`. Source modules implement `ModuleInterface::is_enabled()` and remain inert until a later runtime delivery phase explicitly disables the gate.

## Architecture reference

- `WORDPRESS/architecture/FP-0002-THEME-PLUGIN-SKELETON-PLAN-v1.md`
- `WORDPRESS/architecture/FP-0002-WORDPRESS-ARCHITECTURE-v1.md`
