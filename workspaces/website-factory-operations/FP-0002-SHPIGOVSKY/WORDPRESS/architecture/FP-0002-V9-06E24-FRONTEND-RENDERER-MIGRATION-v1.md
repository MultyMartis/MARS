# FP-0002 V9-06E24 Frontend Renderer Migration

## Helper

`shpigovsky_get_local_hero_cta_label( $post_id, $route_fallback = '' )` in `inc/hero-helpers.php`

## Fallback chain

1. Local `hero_cta_label` on page/service
2. Route-specific fallback (e.g. alcohol leaf)
3. `default_button_label` site option via `shpigovsky_get_hero_default_cta_label()`
4. Static V9 `Записаться на консультацию`

## Files updated

| Renderer | Change |
|---|---|
| `template-parts/home/hero.php` | local front-page `hero_cta_label` |
| `template-parts/services-hub/hero.php` | local hub `hero_cta_label` |
| `template-parts/service/inner-hero.php` | `shpigovsky_get_local_hero_cta_label()` |
| `inc/institutional-helpers.php` | `shpigovsky_get_local_hero_cta_label()` |

No global `Герои` / block hero reads reintroduced.

Evidence: `validation/v9-06e24-hero-cta-button-text-per-entity/frontend-renderer-migration-result.json`
