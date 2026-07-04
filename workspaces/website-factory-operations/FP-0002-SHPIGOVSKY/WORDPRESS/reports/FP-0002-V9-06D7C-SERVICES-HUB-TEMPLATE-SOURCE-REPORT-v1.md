# FP-0002 V9-06D7C Services Hub Template Source Report v1

**Date:** 2026-07-05  
**Task:** V9-06D7-C Services Hub Template Source  
**Preflight HEAD:** `3d42853a3035c26639cfd6d0f242e22eb82bf777`  
**Verdict:** PASS

## Summary

Source-only integration of V9 Services Hub layout into canonical WordPress theme `theme/shpigovsky/`. Replaced skeleton `services-hub.php` with V9-compatible hero, CPT-driven category hub groups, rehabilitation program, FAQ, and shared final-form. D7-A global shell and D7-B home source preserved. Runtime delivery **not performed**.

## Implementation

- New `inc/services-hub-helpers.php` — guarded ACF reads, hierarchical Service CPT queries, slug modifier map  
- `page-templates/services-hub.php` — `main.page-uslugi` orchestration  
- 6 services-hub template-parts + `service-card` component  
- Theme version `0.5.0-d7c-services-hub`

## Validation

| Check | Result |
|-------|--------|
| PHP lint (10 changed) | PASS |
| PHP lint (all theme PHP) | PASS |
| Source safety scan | PASS |
| No plugin/ACF JSON/V9 changes | PASS |
| No runtime writes | PASS |

Evidence: `validation/v9-06d7c-services-hub-template-source/final-verdict.json`

## Partial scope note

D7-C implements the D.6 Services Hub wave: hero, CPT category hubs, program block, FAQ, final-form. Deferred: founder-quote, comfort, genotyping hub, category galleries, hero background image.

## Recommended next action

**CREATE_V9_06D7C_RUNTIME_DELIVERY_TASK**

## Result

COMPLETE
