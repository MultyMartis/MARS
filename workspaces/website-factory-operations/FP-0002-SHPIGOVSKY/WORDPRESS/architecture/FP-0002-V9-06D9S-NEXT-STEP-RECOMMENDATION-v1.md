# FP-0002 V9-06D9-S Next Step Recommendation

**Phase:** V9-06D9-S  
**Date:** 2026-07-06  
**Verdict:** PARTIAL PASS

## Situation

Reviews options are seeded in the database (10 rows, populated `author_label`/`text`). Frontend still resolves via **FALLBACK** because:

1. ACF field key `field_fp02_reviews_items` is shared between `group_fp02_page_reviews` and `group_fp02_site_options_reviews`.
2. Runtime subfields resolve to legacy names (`author_label`, `text`).
3. D9-R helper reads only `review_author` / `review_text`.

Visual output remains equivalent (10 slides, same copy) but source mode is not OPTIONS.

## Recommended next action

**OPERATOR_DECISION_REQUIRED**

Authorize a D9-T repair wave:

1. Assign unique ACF field keys for options reviews repeater (e.g. `field_fp02_options_reviews_items`).
2. Update `reviews-helpers.php` to normalize both D9-R and legacy subfield names (or options-only canonical names after key fix).
3. Re-seed or migrate existing 10 option rows if subfield names change.
4. Admin visual QA (screenshots deferred from D9-S).

Do **not** re-run D9-S seed alone — OPTIONS mode will not activate without schema/helper alignment.
