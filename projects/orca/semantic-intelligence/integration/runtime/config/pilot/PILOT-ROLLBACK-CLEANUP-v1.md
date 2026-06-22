# P0-I Pilot Rollback and Cleanup

**Status:** `I-08 — READY FOR PHRASE-SELECTION GATE`

## Allowed cleanup (pilot runs only)

1. Delete `runtime/output/pilot-runs/<run_id>/`
2. Delete `runtime/reports/pilot-*` generated for a specific run
3. Clear `runtime/output/integration-*.json` test artifacts if needed

## Forbidden cleanup

- Canonical contracts under `semantic-intelligence/taxonomy/`, `schemas/`, `contracts/`
- Committed charter and approval records
- Corvonero corpus or MIG sources
- Campaign or Commander artifacts

## Rollback procedure

1. Stop any in-progress pilot runner process
2. Remove pilot run output directory for the run ID
3. Verify no canonical source files were modified (`git status` scoped to `runtime/output/`)
4. Record rollback in operator log — no automatic persistence in this core
