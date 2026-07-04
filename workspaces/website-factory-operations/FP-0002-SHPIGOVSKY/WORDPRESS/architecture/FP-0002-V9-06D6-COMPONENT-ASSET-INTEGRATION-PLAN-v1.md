# FP-0002 V9-06D.6 Component / Asset Integration Plan v1

**Date:** 2026-07-04

## Global chrome (Wave D7-A)

- Port V9 header/footer/nav markup into existing skeleton partials
- Desktop nav from WP menus; mobile offcanvas JS classified safe_static
- Modal markup only; submit deferred (forms module disabled)
- Breadcrumbs hierarchy-derived

## CSS

- Package compiled V9 CSS into `theme/shpigovsky/assets/css/` from V9 `dist` (or approved build artifact)
- Do not edit V9 `src/`/`dist/`
- Enqueue via `inc/assets.php` / `shpigovsky_enqueue_theme_assets`
- Version with theme version or filemtime
- No new design tokens

## JS

| Class | Behaviors |
|---|---|
| safe_static | reveal, offcanvas, scroll-to-top |
| requires_wp_adaptation | Swiper, Fancybox, Inputmask |
| deferred | modal/form submit |
| not first wave | blog-specific |

## Images/media

- Theme assets: logo, icons, shared chrome, first-wave decorative/service images needed for shell/home/service chrome
- Media library later for CMS-managed fields
- Empty media → omit block

## Fallbacks

Empty ACF/options must not fatal; omit sections or show `post_title` only.

## Result

COMPLETE
