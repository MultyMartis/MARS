# ORCA Semantic Admission Integration Runtime v1

**Locus:** `projects/orca/semantic-intelligence/integration/runtime/`  
**Status:** `CORE IMPLEMENTATION APPROVED — READY FOR INTEGRATION PILOT`  
**Stack:** Node.js ESM (`.mjs`) — no additional dependencies

## Components

| ID | Module | Role |
|----|--------|------|
| I-01 | `src/contract-loader.mjs` | Load and verify contracts from runtime lock |
| I-02 | `src/record-generator.mjs` | Schema-conformant initial semantic records |
| I-03 | `src/admission-orchestrator.mjs` | Bounded admission pipeline orchestration |
| I-04 | `src/invariant-validator.mjs` | SI-INV-001–015 blocking validation |
| I-05 | `src/human-review-router.mjs` | Review queue routing |
| I-06 | `src/legacy-comparison-adapter.mjs` | Diagnostic legacy regex comparison |
| I-07 | `src/consumption-report.mjs` | Contract consumption evidence |

## CLI

**Search PPC (Wave 1.2):** `integration:run` without lifecycle gate is **LOCKED** unless `--diagnostic`. Production path: [orca-ppc-gate.mjs](cli/orca-ppc-gate.mjs).

```bash
cd projects/orca/semantic-intelligence/integration/runtime

node cli/orca-admission.mjs contracts:validate
node cli/orca-admission.mjs contracts:report
node cli/orca-admission.mjs record:validate <path-to-record.json>
node cli/orca-admission.mjs integration:run <path-to-fixture.json> --diagnostic
node tests/run-integration-fixtures.mjs
```

Exit codes: `0` success, `2` blocked/fail-closed, `1` usage error.

## Contract pinning

- **Authority manifest:** `../contracts/orca-semantic-contract-loading-manifest-v1.json`
- **Runtime lock:** `config/orca-semantic-contract-runtime-lock-v1.json`

Runtime lock pins checksums and fixture operator scope without altering canonical contracts.

## Boundaries

See [`ORCA-RUNTIME-BOUNDARY-v1.md`](ORCA-RUNTIME-BOUNDARY-v1.md).

**Not in scope:** real pilot execution, semantic accuracy proof, campaign production, Corvonero corpus processing.
