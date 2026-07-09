# FP-0002 V9-06E26A-POLISH Baseline Decor Item Audit v1

**Task:** V9-06E26A-POLISH  
**Date:** 2026-07-09  
**Verdict:** PASS

## Static V9 target

- Parent: `comfort__gallery` inside infrastructure narrative g5 (static includes `comfort-gallery.html` with `fancyboxGroup: o-centre-infrastructure-g5`).
- First child: `comfort__gallery-item comfort__gallery-item_decor` (`comfort-gallery-decor.html`).
- Logo: `assets/img/branding/logo.svg`, decorative (`alt=""`), `width="auto"` `height="auto"`, no fancybox link.

## Current WP before fix

- Partial: `template-parts/institutional/infrastructure-narrative.php`.
- g5 group rendered six fancybox `<a>` items only; decor div missing.
- First child was `comfort__gallery-item--wide` (infrastructure-13.webp).

## Decision

Add hardcoded decor markup before g5 foreach loop; reuse `shpigovsky_asset_uri( 'img/branding/logo.svg' )`. No ACF/DB changes.

## Evidence

`validation/v9-06e26a-polish-infrastructure-g5-decor-logo/baseline-decor-item-audit.json`
