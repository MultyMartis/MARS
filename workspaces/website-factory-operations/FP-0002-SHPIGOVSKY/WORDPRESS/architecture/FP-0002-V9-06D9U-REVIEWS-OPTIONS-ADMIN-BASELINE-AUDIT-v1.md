# FP-0002 V9-06D9U — Reviews Options Admin Baseline Audit

## Baseline (pre-repair)

| Item | State |
|---|---|
| Admin location | `fp02-site-settings` only |
| Top-level menu | Absent |
| Rows | 10 seeded |
| Stored subfields | Legacy `author_label`, `text`, `metadata`, `source` under `options_*` keys |
| Canonical subfields in admin | Empty (key mismatch) |
| Frontend source mode | OPTIONS (helper compatibility) |

## Root cause

D9-S seed wrote legacy subfield names into `options_reviews_items_*` option meta. D9-T fixed schema keys and helper mapping but not row-level canonical storage.

## Result

PASS — baseline documented; migration target confirmed.
