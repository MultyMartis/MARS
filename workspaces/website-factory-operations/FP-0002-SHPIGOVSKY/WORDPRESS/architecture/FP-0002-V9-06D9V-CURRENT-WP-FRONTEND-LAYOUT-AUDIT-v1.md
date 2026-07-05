# FP-0002 V9-06D9V — Current WP Frontend Layout Audit

**Phase:** V9-06D9-V (read-only)  
**Date:** 2026-07-06  
**Runtime:** http://shpigovsky.test/

## Home `/`

| Check | Result |
|---|---|
| HTTP | 200 |
| Markup | `reviews__slider swiper` + 10 `reviews__slide` |
| Template | `home/reviews.php` → `shared/reviews-slider.php` |
| Static V9 parity | **MATCH** (slider expected on Home) |

Operator note "still looks like old slider" is **expected for Home** per static V9 authority.

## Reviews `/otzyvy/`

| Check | Result |
|---|---|
| HTTP | 200 |
| Main class | `shpigovsky-skeleton shpigovsky-skeleton--reviews` (not `page-otzyvy__main`) |
| Markup found | Shared slider (10 slides) + skeleton archive-list comment |
| Markup missing | `reviews-archive`, `review-archive-card`, pagination, rehabilitation section |
| Static V9 parity | **MISMATCH** |

## Root cause

`page-templates/reviews.php` includes:

1. `reviews-section.php` → shared Home slider (**wrong for archive page**)
2. `archive-list.php` → inert skeleton placeholder only

Theme CSS (`v9-style.css`) already contains `.reviews-archive` / `.page-otzyvy` rules but markup does not trigger them.

## Screenshots

Not captured — PHP/Playwright unavailable; dist/ not built. HTML curl probes used instead.

## Evidence

`validation/v9-06d9v-reviews-admin-static-layout-reconciliation-audit/current-wp-frontend-layout-audit.json`
