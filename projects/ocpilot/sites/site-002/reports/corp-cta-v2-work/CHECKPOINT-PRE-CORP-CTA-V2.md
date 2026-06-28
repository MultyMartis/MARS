# CHECKPOINT — SITE-002 Universal Corporate CTA v2 (pre-implementation)

**Task:** SITE-002 — UNIVERSAL CORPORATE CTA v2 (M9.14–M9.18 CTA system replacement)  
**Branch:** `mars/canonical-post-recovery`  
**Timestamp:** 2026-06-29  
**Authority:** SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01, SITE-002-STABLE-LIVE-LOCAL-FONTS-01, SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02

## Scope

Replace **last CTA block only** on six corporate pages with unified `zpm-corp-cta` component.

## Out of scope (frozen)

Home, catalog, PDP, PLP, Commercial Trust catalog block, About layout/content, navigation, header, footer, forms JS, controllers, main.js.

## Pre-change remote targets

- `assets/css/style.css`
- `catalog/view/theme/default/template/information/about.twig`
- `catalog/view/theme/default/template/information/delivery.twig`
- `catalog/view/theme/default/template/information/payment.twig`
- `catalog/view/theme/default/template/information/guarantee.twig`
- `catalog/view/theme/default/template/information/dealers.twig`
- `catalog/view/theme/default/template/information/custom_equipment.twig`
- `catalog/view/theme/default/template/sections/blockcorporatecta.twig` (new)
- `catalog/view/theme/default/template/sections/corpcta-*.twig` (new)
- `catalog/view/theme/default/template/sections/corpcta-form-*.twig` (new)

## Rollback

Restore `.pre-site-002-corp-cta-v2.bak` backups from `projects/ocpilot/sites/site-002/backups/` and clear Twig cache.
