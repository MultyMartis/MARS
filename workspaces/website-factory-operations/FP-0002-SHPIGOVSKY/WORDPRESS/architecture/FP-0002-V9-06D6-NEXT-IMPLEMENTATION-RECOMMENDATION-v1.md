# FP-0002 V9-06D.6 Next Implementation Recommendation v1

**Date:** 2026-07-04

## Recommended action

**CREATE_V9_06D7_GLOBAL_SHELL_ASSET_INTEGRATION_SOURCE_TASK**

## Rationale

1. D.5 confirmed all first-wave routes HTTP 200 with skeleton baseline.
2. Theme chrome is unstyled and V9 CSS/JS are not enqueued — every route integration would still look like skeleton without D7-A.
3. Home/service/contacts template work depends on shared header/footer/assets.
4. ACF field gaps exist but do not block starting shell/asset integration with omit-empty fallbacks.
5. Service template work should follow after chrome and assets exist.

## Not recommended now

| Action | Why not |
|---|---|
| CREATE_V9_06D7_HOME_TEMPLATE_INTEGRATION_SOURCE_TASK | Premature without global CSS/chrome |
| CREATE_V9_06D7_SERVICE_TEMPLATE_INTEGRATION_SOURCE_TASK | Premature without global CSS/chrome and layout wiring context |
| CREATE_V9_06D7_ACF_FIELD_GAP_REPAIR_TASK | Gaps documented; not blocking D7-A |
| OPERATOR_DECISION_REQUIRED | Clear next micro-task exists |

## Authorization status

V9-06D.7: **READY FOR OPERATOR REVIEW** — not authorized by this planning task.
