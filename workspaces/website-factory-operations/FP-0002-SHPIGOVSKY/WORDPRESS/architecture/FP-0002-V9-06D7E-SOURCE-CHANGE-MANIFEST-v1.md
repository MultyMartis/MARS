# FP-0002 V9-06D7E Source Change Manifest v1

**Date:** 2026-07-05  
**Task:** V9-06D7-E Contacts Template Source  
**Preflight HEAD:** `0672ed2b03ce58a5a35b3a969d9c68f5280b835b`  
**Theme version:** `0.7.0-d7e-contacts-template`

## Added

| Path | Purpose |
|------|---------|
| `theme/shpigovsky/inc/contacts-helpers.php` | Read-only ACF/options helpers, body class, static fallbacks |
| `theme/shpigovsky/template-parts/contacts/location-card.php` | Reusable location article partial |

## Updated

| Path | Change |
|------|--------|
| `theme/shpigovsky/functions.php` | Require contacts-helpers; bump version |
| `theme/shpigovsky/page-templates/contacts.php` | V9 main wrapper and section orchestration |
| `theme/shpigovsky/template-parts/contacts/map-body.php` | Full V9 contacts-body markup |
| `theme/shpigovsky/template-parts/contacts/rehabilitation-steps.php` | Full V9 steps + CTA + support |

## Preserved

- D7-A global shell/assets
- D7-B home source
- D7-C services hub source
- D7-D service templates source

## Not changed

- Plugin source
- ACF JSON
- V9 src/dist
- Runtime files

**Result:** PASS
