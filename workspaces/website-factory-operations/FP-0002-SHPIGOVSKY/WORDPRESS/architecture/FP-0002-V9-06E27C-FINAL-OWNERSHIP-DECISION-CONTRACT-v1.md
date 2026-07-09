# FP-0002 V9-06E27C — Final Ownership Decision Contract

**Baseline:** `d6caab422bc9301caf3f90631558b43e1c9e3bfb`  
**Evidence:** `validation/v9-06e27c-page-service-ownership-decision/final-e27c-ownership-decision-contract.json`

## Conflict diagnosis

Legacy hub-child pages `#6/#7/#8` duplicate service CPT subdivision objects at identical paths. `ServicePermalinks` rewrite rules assign HTTP resolution to service CPT. Primary menu item `#301` still references page `#6`.

## Current state

| Surface | `/uslugi/zavisimosti/` | `/uslugi/psihicheskoe-zdorovie/` | `/uslugi/rasstroystva-pischevogo-povedeniya/` |
|---|---|---|---|
| Route owner | service `#73` | service `#77` | service `#84` |
| Menu owner | page `#6` (Primary only) | — | — |
| Shadow page | `#6` publish | `#7` publish | `#8` publish |

## Recommended canonical owner

Service CPT `#73`, `#77`, `#84` respectively.

## Operator decision required

Approve Option A and charter **V9-06E27D** implementation.

## E27D scope (upon approval)

1. DB checkpoint  
2. Menu retarget `#301`  
3. Trash `#6/#7/#8`  
4. Route validation  

## Risks

Menu retarget must precede page `#6` trash.

## Rollback

Trash restore + menu revert, or full DB checkpoint.

## Next task

`CREATE_V9_06E27D_PAGE_SERVICE_OWNERSHIP_IMPLEMENTATION_TASK`

## E27C result

**PASS** — read-only decision package complete; zero mutations.
