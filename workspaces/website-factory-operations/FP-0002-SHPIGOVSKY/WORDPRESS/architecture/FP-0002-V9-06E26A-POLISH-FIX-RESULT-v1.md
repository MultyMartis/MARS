# FP-0002 V9-06E26A-POLISH Fix Result v1

**Task:** V9-06E26A-POLISH  
**Date:** 2026-07-09  
**Verdict:** PASS

## Changed file

`WORDPRESS/theme/shpigovsky/template-parts/institutional/infrastructure-narrative.php`

## Before → After

| Marker | Before | After |
|---|---|---|
| g5 first child | `a.comfort__gallery-item--wide` | `div.comfort__gallery-item_decor` |
| `comfort__gallery-item_decor` in g5 | absent | present |
| Logo asset | n/a | `img/branding/logo.svg` |

Six existing g5 gallery links unchanged; wide indexes (0, 5) unchanged relative to image loop.

## Evidence

`validation/v9-06e26a-polish-infrastructure-g5-decor-logo/polish-fix-result.json`
