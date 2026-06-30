# Search PPC Regression Corpus v1

**Status:** IMPLEMENTED  
**Machine-readable:** `tools/commander-transport/contracts/search-ppc-regression-corpus-v1.json`

## Purpose

Failure-prevention fixtures from Triumph and Corvonero historical failures. **Not** automatic semantic authority for future clients.

## Categories

1. **Template contamination** — ремонт/запчасти/эвакуатор in stale E9
2. **Metadata transport** — explicit clear / preserve / set semantics
3. **Semantic reject/keep** — Corvonero 1C programmer examples
4. **Geo routing** — Новосибирск LOCAL_ONLY, Саратов REMOTE_ONLY, Минск REJECT
5. **Service routing** — CA-01..CA-05 examples
6. **Group architecture** — forbidden generic ad text
7. **Negative policy** — quoted pseudo-safe values; separate TXT policy
8. **Differential hotfix** — V2.6 → V2.6.1 allowed changes

## Test coverage

- `metadata-operation-model.test.mjs`
- `template-sanitizer.test.mjs`
- `artifact-xlsx-validator.test.mjs`
- `differential-validator.test.mjs`
- `release-gate.test.mjs`
