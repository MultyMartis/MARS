# FP-0002 V9-06E7B — Hero Final State v1

**Date:** 2026-07-06

## Theme hero system

- **Registry:** `inc/hero-helpers.php` — `shpigovsky_get_hero_context_registry()`
- **Shared partial:** `template-parts/shared/services-inner-hero-v2.php`
- **Layouts:** home (`hero--home`), services inner v2 (`services-inner-hero-v2`), institutional
- **Resolution:** ACF `hero_media` → theme asset fallback per context key

## Admin editability

Hero image fields registered in project plugin `FieldGroups.php` for:

- Front page (home)
- Services hub page template
- Service post type
- Institutional page template

## Runtime seed state

Four hero contexts seeded with Media Library attachments (IDs 302–305). Alcohol corrected to service ID 74.

## Frontend

All core hero routes return HTTP 200 with hero markup and image (admin field or theme fallback). Institutional `/o-centre/` uses theme fallback (not in seed scope).

Authority: `validation/v9-06e7b-hero-system-finalization-scope-reconciliation/frontend-hero-validation.json`
