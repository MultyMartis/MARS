# FP-0002 V9-06D9A Visual Parity Repair Plan v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9a-visual-parity-audit/visual-parity-repair-plan.json`

## Sequenced repair waves

| Task | Objective | Files suspected | Mutation | DB | Runtime delivery | Risk | Acceptance |
|------|-----------|-----------------|----------|---:|-----------------|------|------------|
| **D9-C** | Restore photo hero | hero.php, ACF home_hero_slides, media | ACF + MEDIA | yes | yes | LOW-MED | hero__media visible; screenshot parity |
| **D9-B** | Fix Inter font 404s | v9-style.css, assets.php | CSS path rewrite | no | yes | MED | All woff2 HTTP 200 |
| **D9-D** | Port 12 missing sections | front-page.php, new partials, ACF seed | TEMPLATE + ACF | yes | yes | HIGH | ≥18 sections rendered |
| **D9-E** | Density/spacing/vendor | assets.php, section partials | CSS + enqueue | partial | yes | MED | Full-page density ↑ |
| **D9-F** | Secondary pages | hub/service/contacts partials | AUDIT+repair | TBD | yes | MED | Hub/service screenshots |
| D8-F (optional) | Admin UX labels | acf-json | source only | no | yes | LOW | After visual parity |

## Operator priority alignment

1. **D9-C** — addresses “hero looks empty/light” (CRITICAL)
2. **D9-B** — addresses “text thinner/paler” (font synthesis from 404)
3. **D9-D** — addresses “sections missing” (14 section gap)

## No repair performed in D9-A

This document is planning only. Zero mutations authorized during audit.

## Recommended first task

**CREATE_V9_06D9C_HOME_HERO_PARITY_REPAIR_TASK**
