# FP-0002 V9-06E18 — Batch 1 Option Seed

Evidence: `validation/v9-06e18-reusable-blocks-batch-1-fields/batch-1-option-seed-result.json`

## Rules applied

- Preserve existing operator values (skip non-empty).
- Specialists seeded from `shpigovsky_get_v9_specialists_cards()` via `specialist_photo_asset` paths.
- Reviews data not rewritten (`fp02-reviews` preserved).
- Images: theme asset paths only — `MEDIA_ATTACHMENT_DEFERRED`.

## Contexts

| Context | Purpose |
|---------|---------|
| `fp02-block-final-form` | Final form copy |
| `fp02-block-specialists` | Specialists repeater |
| `fp02-block-cta-bands` | Global CTA defaults |
| `fp02-reviews` | Unchanged canonical reviews storage |
