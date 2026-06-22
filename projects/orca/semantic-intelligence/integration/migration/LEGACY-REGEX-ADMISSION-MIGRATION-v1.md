# Legacy Regex Admission Migration v1

**Migration ID:** `legacy-regex-admission-migration-v1`  
**Date:** 2026-06-22  
**Script under review:** `projects/orca/projects/corvonero-direct-v2-clean-room/tools/run-clean-room-semantic-pipeline-v1.mjs`

---

## Current state (forensic)

| Function | Role today | Authority |
|----------|------------|-----------|
| `classifyIntent()` | Regex arrays (CAREER, EDU, DIY, PRODUCT_CFG, etc.) | **LEGACY AUTHORITY** (defect) |
| `commercialEligibility()` | Maps intent class → `ELIGIBLE COMMERCIAL` / `NOT ELIGIBLE — *` | **LEGACY AUTHORITY** (defect) |
| `mapService()` | SERVICE_PATTERNS regex | Downstream — must not run before admission PASS |
| `clusterKey()` / `discoverNegatives()` | Post-admission | Correctly ordered but fed broken input |

**Finding:** 1892 `ELIGIBLE COMMERCIAL` from topic≈intent failure. No contract load. No ABSTAIN terminal.

---

## Migration states

| State | Definition | Target for regex |
|-------|------------|------------------|
| `LEGACY AUTHORITY` | Produces final commercial eligibility | **Exit** |
| `DIAGNOSTIC BASELINE` | Emits comparison fields only | **Target** |
| `SIGNAL GENERATOR ONLY` | Contributes candidate signals to annotation consumer | **Target** |
| `DEPRECATED` | Marked no authority; scheduled removal | Transitional |
| `REMOVED` | Deleted from admission path | Future (not this task) |

**Required target:** `DIAGNOSTIC BASELINE / SIGNAL GENERATOR ONLY`

---

## Comparison report schema

Per phrase during pilot (I-06):

| Field | Description |
|-------|-------------|
| `phrase` | Raw query |
| `legacy_decision` | e.g. `ELIGIBLE COMMERCIAL` |
| `legacy_intent_class` | e.g. `COMMERCIAL SERVICE` |
| `new_decision` | `ACCEPT` / `REJECT` / `ABSTAIN` |
| `disagreement` | boolean |
| `violated_invariant` | SI-INV code if legacy ACCEPT illegal |
| `review_route` | Router output if triggered |

Output path (implementation): `integration/pilot-slice/reports/legacy-comparison-v1.json`

---

## Migration steps (implementation backlog)

1. **I-06** — Wrap `classifyIntent` / `commercialEligibility` in diagnostic adapter; write only to `diagnostic_comparison.*`
2. Insert P0-I orchestrator as sole authority for `commercial_eligibility.decision`
3. Disable `mapService` until invariant PASS on record
4. Pilot comparison report — measure disagreement rate (informational, not D3)
5. Mark script header `LEGACY — NOT SEMANTIC AUTHORITY`
6. **Do not delete** legacy script in this charter task

---

## Regex signal reuse (allowed)

Legacy patterns may feed **candidate signals** with source tag `legacy_regex_signal` — subject to annotation policy consumer override.

Example: `career_pattern` match → `opposing_evidence` for commercial ACCEPT, not automatic REJECT unless policy confirms.
