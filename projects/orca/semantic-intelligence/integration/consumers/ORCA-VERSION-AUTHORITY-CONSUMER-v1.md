# ORCA Version Authority Consumer v1

**Consumer ID:** `orca-version-authority-consumer-v1`  
**Primary contract:** P0-A authority model and ADR versioning rules

---

## Input paths

| Contract | Path |
|----------|------|
| Authority model | `architecture/semantic-intelligence/orca-semantic-intelligence-authority-model-v1.json` |
| ADR manifest | `architecture/semantic-intelligence/orca-semantic-intelligence-adr-v1.json` |
| Contract loading manifest | `integration/contracts/orca-semantic-contract-loading-manifest-v1.json` |

## Supported versions

Per-contract `version` field in loading manifest; global admission bundle `p0-i-bundle-v1`.

## Required fields consumed

- Expected version per contract
- Checksum SHA-256
- Load order
- Compatibility matrix

## Output

- `versioning.*` block on every semantic record
- `assessor_versions` (ruleset, orchestrator, validator)
- Run-level `contract_bundle_version`

## Blocking conditions

- Checksum mismatch → `BLOCKED — SEMANTIC CONTRACT VERSION MISMATCH`
- Unsupported version → `SI-VER-002`
- Missing `versioning` on output record → `SI-VER-003`

## Error behavior

FATAL at load time for required contracts.

## Audit trace

`audit.contract_bundle`: `{bundle_version, contracts[], all_required_loaded}`.

## Fallback behavior

**None.** Partial bundle load forbidden for required contracts.
