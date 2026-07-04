# FP-0002 V9-06D7E Contacts Template Source Report v1

**Date:** 2026-07-05  
**Task:** V9-06D7-E Contacts Template Source  
**Preflight HEAD:** `0672ed2b03ce58a5a35b3a969d9c68f5280b835b`  
**Verdict:** PASS

## Summary

Source-only integration of V9 Contacts layout into canonical WordPress theme `theme/shpigovsky/`. Implemented `contacts-map-body` and `contacts-rehabilitation-steps` sections with ACF page field and site option bindings, guarded fallbacks, and shared `program-cta-band` CTA. D7-A through D7-D source preserved. Runtime delivery **not performed**.

## Implementation

- New `inc/contacts-helpers.php` — guarded reads, location resolution, map embed allowlist, body class
- Updated `page-templates/contacts.php` — V9 `page-kontakty__main` orchestration
- Updated `template-parts/contacts/map-body.php` — full contacts-body section
- Updated `template-parts/contacts/rehabilitation-steps.php` — steps, CTA, support
- New `template-parts/contacts/location-card.php` — location article partial
- Theme version `0.7.0-d7e-contacts-template`

## Validation

| Check | Result |
|-------|--------|
| PHP lint (6 changed) | PASS |
| PHP lint (all theme PHP) | PASS |
| Source safety scan | PASS |
| No plugin/ACF JSON/V9 changes | PASS |
| No runtime writes | PASS |

Evidence: `validation/v9-06d7e-contacts-template-source/final-verdict.json`

## Deferred

- Map PNG assets and rehabilitation interior photo (content migration media)
- Options page seed values
- Live form endpoint (modal-only CTA preserved)

## Recommended next action

**CREATE_V9_06D7E_RUNTIME_DELIVERY_TASK**

## Result

COMPLETE
