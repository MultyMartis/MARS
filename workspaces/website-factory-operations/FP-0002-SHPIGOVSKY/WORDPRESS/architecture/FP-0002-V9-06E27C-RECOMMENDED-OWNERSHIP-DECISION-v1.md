# FP-0002 V9-06E27C — Recommended Ownership Decision

**Evidence:** `validation/v9-06e27c-page-service-ownership-decision/recommended-ownership-decision.json`  
**Status:** Recommendation only — **not executed**

## Recommendation summary

`RECOMMENDED_KEEP_SERVICE_CPT` (Option A)

## Per-route decisions

| Route | Canonical owner | Page action | Service action | Menu | Redirect later |
|---|---|---|---|---|---|
| `/uslugi/zavisimosti/` | service `#73` | trash `#6` later | **KEEP** | retarget `#301` → `#73` | NO |
| `/uslugi/psihicheskoe-zdorovie/` | service `#77` | trash `#7` later | **KEEP** | none | NO |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | service `#84` | trash `#8` later | **KEEP** | none | NO |

## MUST_NOT_TOUCH

- Pages `#3`, `#4`, `#5`, `#19`
- Post `#750`
- Service `#74` (alcohol leaf), `#75`, and full `#73` child tree
- Permalink structure, rewrite rules, redirects

## Operator gate

Evidence supports Option A without architectural ambiguity. Operator approval required **only to authorize E27D execution** (DB writes).
