# FP-0002 V9-06D7C Runtime Delivery Gate v1

**Date:** 2026-07-05  
**Task:** V9-06D7-C Services Hub Template Source

## Gate status

| Check | Status |
|-------|--------|
| Source integration complete | YES (core wave) |
| PHP lint (source) | PASS |
| Source safety scan | PASS |
| Runtime delivery performed in D7-C | **NO** (forbidden) |
| Runtime delivery authorized | **NO** — separate operator task required |

## Required before runtime delivery

1. Operator authorization: `CREATE_V9_06D7C_RUNTIME_DELIVERY_TASK`  
2. Preflight HEAD sync (same discipline as D7-B)  
3. PHP lint on theme source  
4. Dry-run delivery plan + hash baseline  
5. Bounded theme-files-only copy to `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\themes\shpigovsky\`  
6. Post-delivery route smoke (`/uslugi/` + service routes)  
7. Services Hub section render smoke (hero, CPT groups, FAQ if seeded)  
8. Rollback: restore prior theme hash from checkpoint  

## Expected runtime target

`X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\themes\shpigovsky\`

## Blockers for delivery

- None in source layer after D7-C PASS  
- Visual parity for deferred sections (founder-quote, comfort, genotyping, galleries) remains post-migration  

## Result

READY FOR OPERATOR REVIEW — runtime delivery **NOT_PERFORMED**
