# ORCA Operator Scope Consumer v1

**Consumer ID:** `orca-operator-scope-consumer-v1`  
**Primary contract:** Project business scope boundary (not demand proof)

---

## Input paths

| Contract | Path (pilot: Corvonero example) |
|----------|--------------------------------|
| Service scope registry | `projects/corvonero-direct-v2-clean-room/authority/` (pilot) |
| Business intake | Project `intake/*-BUSINESS-INTAKE-v1.md` |
| ADR component matrix | `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-COMPONENT-RESPONSIBILITY-MATRIX-v1.md` |

## Supported versions

Per-project scope version in intake JSON (`scope_version`).

## Required fields consumed

- Permitted service IDs
- Prohibited intents / strata for project
- Geographic and vertical boundaries
- **Not** used as proof of user demand (P0-C rule)

## Output

- `service_candidate.mapping_status` = `NOT_STARTED` or `CANDIDATE_ONLY` at admission
- Scope prohibition flags on REJECT paths
- `scope_version` in `versioning`

## Blocking conditions

- ACCEPT for service outside operator scope → `SI-SCOPE-001`
- ACCEPT inferred solely from scope catalogue presence → `SI-SCOPE-002` (with invariant 1)
- Missing scope_version → `SI-SCOPE-003`

## Error behavior

BLOCKING for out-of-scope ACCEPT; REJECT with `OUT_OF_OPERATOR_SCOPE` reason when clear.

## Audit trace

`audit.operator_scope`: `{scope_version, source_path, prohibitions_checked[]}`.

## Fallback behavior

If scope file missing in pilot → FATAL `BLOCKED — REQUIRED SEMANTIC CONTRACT NOT LOADED` for project-bound runs. Generic integration fixtures may use `fixtures/operator-scope-pilot-v1.json` (to be created at implementation).
