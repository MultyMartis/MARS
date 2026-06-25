# AG-WP-001 — FW-07B Contract Validation Report v1

**Document type:** Validation report  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24  
**Validator:** [tools/validate-ag-wp-001-operation-contracts.mjs](../tools/validate-ag-wp-001-operation-contracts.mjs)

---

## Run summary

| Check | Result |
|-------|--------|
| Schema self-validation | PASS |
| Operation registry validation | PASS |
| Duplicate operation IDs | 0 |
| Tool reference validation | PASS |
| Failure code registry load | PASS |
| Production scope prohibition | PASS |
| R5 authorization check | PASS (none authorized) |
| Fixture positive tests | 3/3 PASS |
| Fixture negative tests | 4/4 PASS (correctly rejected) |

---

## Counts

| Metric | Value |
|--------|-------|
| Operations discovered | 42 |
| Operations valid | 42 |
| Operations invalid | 0 |
| Bindings defined | 10 |
| Bindings proven | 0 |
| Bindings unimplemented | 10 |
| Failure codes | 36 |
| Fixtures passed | 7 |
| Fixtures failed | 0 |

---

## Commands executed

```text
node tools/validate-ag-wp-001-operation-contracts.mjs
node tools/validate-ag-wp-001-operation-contracts.mjs --fixtures
```

**Exit code:** 0

---

## Honesty

- No WordPress operations were executed
- No runtime mutations performed
- `BOUND_NOT_IMPLEMENTED` bindings are **not** counted as proven

---

*FW-07B validation report v1.*
