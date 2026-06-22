# ORCA Semantic Enforcement Model v1

**Model ID:** `orca-semantic-enforcement-model-v1`  
**Date:** 2026-06-22

---

## Enforcement layers

| Layer | Mechanism | When |
|-------|-----------|------|
| L0 Load | Contract loader version + checksum | Pipeline start |
| L1 Schema | JSON Schema validation | Per record post-generation |
| L2 Policy | Annotation consumer decision rules | Pre-invariant |
| L3 Invariant | SI-INV blocking validator | Post-decision |
| L4 Router | Human review mandatory routes | Post-validation |
| L5 Integration QA | Contract-consumption report | Run end |

---

## Blocking vs diagnostic

| Channel | Authority | Enforcement |
|---------|-----------|-------------|
| P0-I admission orchestrator | **YES** | BLOCKING |
| Invariant validator | **YES** | BLOCKING |
| Legacy regex adapter | **NO** | Diagnostic only |
| Manifest registration | **NO** | FAIL if not consumed |

---

## Evidence requirements

Every blocked record must emit:

- `violation.code`
- `violation.severity`
- `contract_versions` at time of decision
- `audit.lineage[]`

Run-level FATAL halts entire pilot — no partial authority fallback.
