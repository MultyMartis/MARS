# FP-0002 V9-06D9G Next Step Recommendation v1

**Date:** 2026-07-05

## Selected action

**CREATE_V9_06D9H_ACF_ADMIN_EDITABILITY_WIRING_TASK**

## Rationale

D9-G repaired the only D9-F blocking Home visual defect (FAQ heading/id/aria transplant typo). Post-repair validation: FAQ parity PASS, duplicate `comfort-heading` resolved, comfort section intact, hero CTA / specialists / sliders / footer unchanged, secondary routes ALL_200. No-scope-drift PASS. ACF/admin editability wiring is the next planned wave per D9-0 charter.

## Deferred actions

| Action | When |
|--------|------|
| CREATE_V9_06D9H_FULL_VISUAL_PARITY_QA_TASK | Optional post-ACF wiring confirmation |
| CREATE_V9_06D9B2_HEADER_MEGA_MENU_REPAIR_TASK | Unchanged deferral from D9-B |
| OPERATOR_DECISION_REQUIRED | Only if operator defers ACF wiring |

## D9-H wiring task outline

- Wire Home FAQ / comfort / specialists headings to ACF where field groups exist
- Preserve D9-G heading contracts (`faq-heading`, `comfort-heading`, `specialists-heading`)
- No unscoped DB writes; follow D8 seed safety protocol
- Re-QA Home FAQ heading after wiring
