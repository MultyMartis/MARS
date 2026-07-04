# FP-0002 V9-06D7D Service Template Source Report v1

**Date:** 2026-07-05  
**Task:** V9-06D7-D Service Template Source  
**Preflight HEAD:** `131da3c66f4fd49208dfb5aea7122a5b15d3c391`  
**Verdict:** PASS

## Summary

Source-only integration of V9 service parent/detail layouts into canonical WordPress theme `theme/shpigovsky/`. Wired `service_layout_variant` ACF routing with hierarchy/slug fallback; implemented hero, subnav, children, intro, signs, program, stages, FAQ, CTA bands, and final-form across subdivision/leaf/alcohol stacks. D7-A shell, D7-B home, and D7-C services hub preserved. Runtime delivery **not performed**.

## Implementation

- New `inc/service-helpers.php` — guarded ACF reads, CPT child queries, layout resolution, breadcrumbs/subnav  
- Updated `inc/service-template-loader.php` — ACF + hierarchy variant routing  
- Updated `single-service.php` — V9 main class per variant  
- 14 service template-parts + 2 shared components activated  
- Theme version `0.6.0-d7d-service-templates`

## Validation

| Check | Result |
|-------|--------|
| PHP lint (21 changed) | PASS |
| PHP lint (all theme PHP) | PASS |
| Source safety scan | PASS |
| No plugin/ACF JSON/V9 changes | PASS |
| No runtime writes | PASS |

Evidence: `validation/v9-06d7d-service-template-source/final-verdict.json`

## Partial scope note

D7-D implements the D.6 service wave core: hero, navigation, CPT children, structured sections with ACF/fallback, FAQ, CTA, final-form. Deferred: nature, team-stats, landscape, specialists, founder-quote, comfort, reviews, corridor — require shared block integration or content migration.

## Recommended next action

**CREATE_V9_06D7D_RUNTIME_DELIVERY_TASK**

## Result

COMPLETE
