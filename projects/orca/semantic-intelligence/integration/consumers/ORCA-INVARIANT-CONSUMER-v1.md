# ORCA Invariant Consumer v1

**Consumer ID:** `orca-invariant-consumer-v1`  
**Primary contract:** P0-B semantic record invariants

---

## Input paths

| Contract | Path |
|----------|------|
| Invariants registry | `semantic-intelligence/contracts/orca-semantic-record-invariants-v1.json` |
| Human-readable | `semantic-intelligence/contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md` |

## Supported versions

`v1`

## Required fields consumed

All 20 invariants from registry; P0-I minimum blocking set (15 rules) enforced at validator.

## Output

- Invariant validation result per record
- `blocking_violations[]` with codes

## Blocking conditions

Any P0-I minimum invariant fail → record blocked. See [`../validators/ORCA-SEMANTIC-ADMISSION-INVARIANT-VALIDATOR-v1.md`](../validators/ORCA-SEMANTIC-ADMISSION-INVARIANT-VALIDATOR-v1.md).

## Error behavior

BLOCKING — violated invariant downgrades illegal ACCEPT to blocked state; pipeline marks record `INTEGRATION_BLOCKED`.

## Audit trace

`audit.invariants_checked[]`: `{invariant_id, pass, code}`.

## Fallback behavior

**None.** No waiver without human override audit entry (integration pilot may simulate; production requires operator policy).
