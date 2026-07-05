# FP-0002 V9-06D9F Next Step Recommendation v1

**Date:** 2026-07-05

## Selected action

**CREATE_V9_06D9G_MICRO_VISUAL_REPAIR_TASK**

## Rationale

D9-F read-only QA confirms D9-D/D9-E success for Home main structure (19/19), footer transplant, slider/vendor/pagination parity, assets, and secondary routes (ALL_200). Single remaining Home visual defect: FAQ section transplant typo in `template-parts/home/faq.php`.

## Deferred actions

| Action | When |
|--------|------|
| CREATE_V9_06D9G_ACF_ADMIN_EDITABILITY_WIRING_TASK | After FAQ micro repair + quick re-QA |
| CREATE_V9_06D9B2_HEADER_MEGA_MENU_REPAIR_TASK | Unchanged deferral from D9-B |
| OPERATOR_DECISION_REQUIRED | Only if operator chooses ACF-before-micro-repair |

## Micro repair task outline

- Scope: `faq.php` only (+ bounded runtime delivery 1 file)
- No DB/ACF/options/menu writes
- Verify: `faq-heading` unique; heading text matches static V9
- Re-check: Home FAQ screenshot + duplicate-id scan
