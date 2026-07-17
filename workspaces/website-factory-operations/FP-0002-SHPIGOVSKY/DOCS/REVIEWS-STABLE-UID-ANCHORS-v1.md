# Reviews Data Model — Stable UID Anchors (E62C)

**Model:** ACF Options repeater `reviews_items` on `fp02-reviews` (not a Review CPT).

## Public identity

| Surface | Value |
|---------|-------|
| Field | `review_uid` |
| Format | `review-xxxxxxxx` |
| Archive card | `id="{review_uid}"` |
| Slider link | `/otzyvy[/page/N]/#{review_uid}` |

Page number is derived from **current** row position ÷ `reviews_per_page`.  
UID does **not** change on reorder; page number may.

## Lifecycle

- Existing rows: migrated once via `shpigovsky_ensure_review_uids()` (idempotent).
- New / empty / duplicate UIDs: assigned on Reviews options save.
- Admin field is readonly; operators should not hand-edit.

## Legacy

Index-based anchors (`#review-1`) from E62B are superseded and no longer rendered as element IDs.
