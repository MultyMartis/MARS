# Triumph / Corvonero Systemic Reconciliation v1

**Date:** 2026-06-30  
**Status:** DOCUMENTATION + EXECUTABLE GENERALIZATION COMPLETE

## Triumph lessons classification

| Lesson | Status |
|--------|--------|
| Commander ZIP patch via exporter-cli | **EXECUTABLE** — reused in `commander-patcher-adapter.mjs` |
| Header map / column positions | **EXECUTABLE** — `commander-header-map-v0.json` |
| Bid ladder Triumph v1.3 | **EXECUTABLE** — `bid-ladder.mjs` |
| Callout `||` delimiter | **EXECUTABLE** — `callout-serializer.mjs` |
| Clean URL / no UTM in ad URL | **EXECUTABLE** — `url-policy.mjs` |
| Template SHA identity check | **EXECUTABLE** — `template-validator.mjs` |
| E9 campaign negatives clear on blank policy | **EXECUTABLE** (V2.6.1) — now in metadata model + sanitizer |
| Organization blank policy | **EXECUTABLE** — adapter + contract |
| Survivability validation rules (docs) | **DOCUMENTED** — `triumph-manipulator/validation/` |
| Semantic campaign generation prompts | **PROJECT-SPECIFIC** — Triumph ORCA prompts |
| Triumph promotion URL in template | **CONTAMINATION** — must sanitize E11 |
| Stale E9 negatives (ремонт/запчасти/эвакуатор) | **CONTAMINATION** — regression corpus + sanitizer |
| Shared neutral template | **MISSING** — current template IS Triumph production template |
| Release gate / artifact-first validation | **MISSING** (was) → **IMPLEMENTED** (this task) |
| Operator approval receipt | **MISSING** (was) → **IMPLEMENTED** |
| Release state model | **MISSING** (was) → **IMPLEMENTED** |

## What was generalized in this task

- Template contract (machine-readable)
- Metadata operation model (clear/preserve/set)
- Template sanitization layer
- Artifact-first XLSX validator
- Authority-artifact reconciler
- Differential validator (hotfix mode)
- Release gate runner
- Regression corpus fixtures

## What remains project-specific

- Corvonero phrase authority, group plan, ad copy
- Corvonero bid policy `CORVONERO_BALANCED_CYCLIC_10_RUB_V1`
- Corvonero campaign generators under `pilots/corvonero/tools/`
- Triumph S-tier draft JSON instances (not used for Corvonero)

## Corvonero reconciliation

- **V2.6:** semantic authority baseline — unchanged
- **V2.6.1:** generation hotfix — E9 clear in actual XLSX
- **No V2.7** created
- **OPERATOR_SEMANTIC_APPROVED:** no retroactive invention — see release state file

## Template reality

The shared Commander template at `triumph-manipulator-commander-template-v1.xlsx` contains Triumph client data. Sanitization is **mandatory** before any new project uses it.
