# FP-0002 V9-06D9-T Next Step Recommendation

**Phase:** V9-06D9-T  
**Date:** 2026-07-06

## Recommended next action

**CREATE_V9_06D9U_ADMIN_VISUAL_QA_TASK**

## Rationale

- Frontend source mode is **OPTIONS** with 10 preserved reviews.
- ACF key collision resolved; helper normalization supports legacy D9-S row keys in DB.
- Row-level option meta still uses legacy keys (`author_label`, `text`) — admin edit fields may show empty until optional canonical meta migration in a future controlled task.
- Operator visual QA should confirm admin Site Settings reviews UI and frontend parity with captured screenshots.

## Not recommended yet

- Reviews content rewrite (seed preserved as-is)
- Legal/native content review (separate lane)
