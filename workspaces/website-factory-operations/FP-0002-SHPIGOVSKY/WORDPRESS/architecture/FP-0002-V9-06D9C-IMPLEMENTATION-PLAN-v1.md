# FP-0002 V9-06D9-C — Home Hero Parity Implementation Plan

**Date:** 2026-07-05  
**Task:** V9-06D9-C Home Hero Parity Repair  
**Strategy:** Theme asset fallback (preferred over DB seed)

## Problem

Runtime Home hero renders panel/CTA on empty background because `home_hero_slides[0].image` is empty and theme asset was not delivered. Static V9 uses `/assets/img/hero/hero-main.png`.

## Root cause

`ACF_IMAGE_NOT_SEEDED + ASSET_NOT_DELIVERED` (confirmed D9-A).

## Approved repair

1. Copy `hero-main.png` from static V9 into `theme/shpigovsky/assets/img/hero/`.
2. Add `shpigovsky_get_home_hero_image_fallback()` in `inc/home-helpers.php`.
3. Update `template-parts/home/hero.php` to use fallback when ACF image URL is empty.
4. Bounded runtime delivery of exact changed files only.
5. No DB/ACF write — ACF image wins when later seeded.

## Out of scope

Other Home sections, Services Hub, Contacts, options, menus, rewrite flush, media uploads to WP library.

## Validation

- `hero__media` present in runtime DOM
- Hero image HTTP 200 from theme URL
- Route smoke ALL_200
- No other Home section changes

**Evidence:** `validation/v9-06d9c-home-hero-parity-repair/implementation-plan.json`
