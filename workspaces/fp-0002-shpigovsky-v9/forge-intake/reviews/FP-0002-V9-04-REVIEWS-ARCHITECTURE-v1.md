# FP-0002 V9-04 Reviews Architecture v1

**Date:** 2026-07-02

## Decision: page repeater (default)

| Approach | Verdict |
|----------|---------|
| CPT `review` | Deferred — not required for V9 scope |
| Repeater on Reviews page | **SELECTED** |
| Options-stored reviews | Rejected — not page-owned |
| Posts category | Rejected — mixes blog editorial |

## Rationale

- V9 has archive `/otzyvy/` only — no published single-review routes.
- V8 note "отдельная страница отзыва — на всякий случай" preserved as **future extensibility** in Open Decisions.

## Fields per review (repeater)

- author display name
- date text or date field
- rating (if shown)
- body text
- optional thumbnail

## Ordering

Manual repeater order = display order.

## Migration

Demo review cards from `reviews-archive-list.html` → initial repeater rows.
