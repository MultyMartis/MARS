# CORVONERO Commander — Current Authority Validation v1

**Validated at:** 2026-06-29T18:25:30Z  
**Tool:** `projects/mars-search-ppc-production/tools/commander-transport/`  
**Mode:** `validate` only  
**Status:** **FAIL** (expected)

## Stop code

`STOP — CAMPAIGN ARCHITECTURE EXCEEDS COMMANDER GROUP LIMIT`

## Primary blockers (phrase limits)

| Group | Campaign | Phrases | Limit |
|-------|----------|---------|-------|
| `ca-01-specialist-search` | CA-01 | **384** | 200 |
| `ca-05-direct-service-order` | CA-05 | **201** | 200 |

## Additional violations

| Code | Detail |
|------|--------|
| `INVALID_REGION_CAMPAIGN_SETTINGS` | Geography in campaign settings is `Новосибирск + Новосибирская область` — transport requires `Новосибирская область` per row |
| `MISSING_GROUP_NEGATIVES` | No approved group-level negatives authority loaded |

## Warnings

| Code | Detail |
|------|--------|
| `CROSS_CAMPAIGN_NOT_APPLIED` | Cross-campaign negatives not deployed — policy preserved |

## Not performed

- XLSX generation
- Commander import
- `build-payload`
- Authority modification

## Verdict

Current frozen Corvonero authority is **BLOCKED BY ARCHITECTURE VALIDATION**. CA-01 V2 regrouping (CT-4) remains required before transport generation.
