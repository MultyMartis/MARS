# P0-I Real Integration Pilot — p0-i-real-slice-v1

**Status:** `P0-I REAL INTEGRATION PILOT — AUTHORIZED`  
**Purpose:** Bounded integration/enforcement proof on ~200 real Corvonero phrases.

## This is NOT

- a benchmark
- a gold dataset
- a Semantic Core production run
- a Corvonero restart
- campaign production

## Structure

| Path | Role |
|------|------|
| `selection/` | Source inventory, policy, manifest, selection script |
| `input/` | Frozen pilot input |
| `config/` | Pinned runtime, contracts, scope |
| `runs/` | Assessor and pilot runner |
| `output/` | Semantic records (isolated) |
| `review/` | Human review queues |
| `diagnostics/` | Legacy diagnostic comparison |
| `validation/` | Pre/post run validation |
| `decisions/` | Pilot-specific decisions |
| `reports/` | Integration report |

## Execution order

1. `node selection/select-pilot-phrases-v1.mjs`
2. `node runs/freeze-pilot-input-v1.mjs`
3. `node validation/pre-run-validation-v1.mjs`
4. `node runs/run-p0-i-pilot-v1.mjs`

**Git:** Pilot package is intentionally uncommitted for operator inspection.
