# Demo Content Cleanup Backlog (FP-0002)

**Status:** OPEN — operator decision required before production  
**Created:** 2026-07-17 (V9-06E62C)  
**Do not execute cleanup in E62C.**

## Inventory

### Demo Blog posts (10)

| ID | Slug | Purpose |
|----|------|---------|
| 1745–1754 | `demo-pagination-article-01` … `10` | Blog archive pagination + featured image demos (E61/E62B) |

### Demo Reviews (20 of 30 ACF options rows)

- Stored in ACF Options repeater `reviews_items` on `fp02-reviews` (not a Review CPT).
- Marked in evidence matrix (`is_demo` / E62B source markers).
- Stable public anchors use `review_uid` (E62C), not row index.

See: `REPORTS/evidence/v9-06e62c-ocentre-service-admin-review-anchor-final-regression/demo-content-inventory.json`.

## Future cleanup procedure

1. Explicit operator production-cleanup charter.
2. Pre-change DB backup of `mars_wp_fp0002`.
3. Trash/delete demo Blog posts `#1745–1754` (or current ID list).
4. Remove demo `reviews_items` rows from Reviews options; keep real operator reviews.
5. Re-verify `/blog/` and `/otzyvy/` page counts + slider link targets.
6. Re-run `shpigovsky_ensure_review_uids()` if any empty UIDs remain.
7. Record write log + screenshots.

## Policy

Local demo content must not ship to production without operator approval.
