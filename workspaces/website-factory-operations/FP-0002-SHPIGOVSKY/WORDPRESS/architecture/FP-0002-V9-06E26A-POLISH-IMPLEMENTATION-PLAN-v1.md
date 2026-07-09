# FP-0002 V9-06E26A-POLISH Implementation Plan v1

**Task:** V9-06E26A-POLISH  
**Date:** 2026-07-09

## Scope

Single-file theme polish: add missing g5 decor logo item on `/o-centre/`.

## Edit

| Component | Plan | Safety |
|---|---|---|
| `infrastructure-narrative.php` | Insert decor `<div>` before g5 image loop | Theme-only; matches home `comfort.php` decor pattern |
| Asset | `shpigovsky_asset_uri( 'img/branding/logo.svg' )` | Existing theme asset |
| ACF | No change | 0 JSON writes |
| DB | No change | 0 writes |

## Validation

- Route: `/o-centre/` HTTP 200
- Markers: `comfort__gallery-item_decor` first in g5; logo.svg HTTP 200
- Regression: `/`, `/blog/`, `/uslugi/`, `/kontakty/`

## Evidence

`validation/v9-06e26a-polish-infrastructure-g5-decor-logo/implementation-plan.json`
