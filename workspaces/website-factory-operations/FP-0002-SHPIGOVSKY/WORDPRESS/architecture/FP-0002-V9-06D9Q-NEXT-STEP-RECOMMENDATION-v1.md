# FP-0002 V9-06D9Q Next Step Recommendation v1

**Date:** 2026-07-06

---

## Verdict

D9-Q planning **COMPLETE**. Implementation **not** authorized in this wave.

---

## Recommended architecture

**Hybrid E** — ACF Options shared reviews (`fp02-site-settings`) + shared theme include + static V9 fallback. Deprecate `home_reviews_teaser` on Home admin.

---

## Recommended next action

**CREATE_V9_06D9R_REVIEWS_SHARED_INCLUDE_IMPLEMENTATION_TASK**

Single selected action. Do not parallelize D9-R with legal review unless operator explicitly splits charter.

---

## Not recommended now

| Action | Reason |
|--------|--------|
| CREATE_V9_06D9R_LEGAL_NATIVE_CONTENT_REVIEW_TASK | Premature before shared include exists; schedule as D9-U after D9-S |
| CREATE_V9_06D9R_OPERATOR_DECISION_TASK | Operator already decided: shared include, not Home ACF |
| Keep `home_reviews_teaser` | Rejected ownership model |

---

## Operator confirmations still useful (non-blocking)

1. Approve static demo fallback until D9-S seed.
2. Confirm heading migration from `home_reviews_heading` to options in D9-R.
3. Live Home save confirmation (carried from D9-P).

---

## HEAD note

D9-Q executed at synced tip `c188cd2e` (+1 after corrective `fae4cd07`). Branch 0/0 with remote. Planning scope unaffected.
