# FP-0002 V9-06D9U — Canonical Options Meta Migration

## Migration

Migrated 10 rows from legacy `options_reviews_items_{n}_{author_label|text|metadata|source}` to canonical `review_*` subfields with matching `_options_reviews_items_*` ACF reference meta.

Defaults applied per D9-S seed plan: `review_rating=5`, `review_visible=1`, `review_featured=1`.

Legacy row keys deleted after canonical write (40 keys).

## Post-migration

- `get_field('reviews_items','option')` returns canonical keys.
- Admin first author: «Александр, Москва»; text length 344.
- Frontend source mode: OPTIONS (10 items).

## Result

PASS
