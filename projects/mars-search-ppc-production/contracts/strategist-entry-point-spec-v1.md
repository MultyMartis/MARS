# AI PPC Strategist — Entry Boundary Specification v1

**Status:** `MISSING RUNTIME — CONTRACT ONLY`  
**Lifecycle stage:** SPPC-13  
**Wave:** 1.1

---

## Finding

No executable AI PPC Strategist consumer exists in-repo. Strategy generation today occurs only through human/Web-GPT/Cursor workflows without a dedicated strategist CLI or output schema validator.

## Required entry contract (when implemented)

| Field | Requirement |
|-------|-------------|
| Manifest | Required — `project-ppc-state-manifest-v2` |
| SPPC-12 | `dated_analytical_pack` must be complete and approved |
| Paid SERP | `paid_serp_business_hours_evidence` or approved degradation |
| Output | `ppc_strategy_decision_record` only |
| Forbidden | campaign registry, Commander, semantic admission artifacts |

## Gate invocation

```bash
node projects/mars-search-ppc-production/runtime/cli/search-ppc-gate.mjs \
  --manifest <path> --stage SPPC-13 --action strategy
```

## Interim enforcement

- Lifecycle gate blocks `ppc_strategy_decision_record` before SPPC-12 complete.
- Ad hoc project scripts attempting strategy without manifest must be classified **QUARANTINED**.
- Cursor tasks requesting strategy must pass `validate-cursor-ppc-task.mjs`.

## Classification

`NOT TESTABLE — COMPONENT MISSING` for strategist-specific bypass tests until runtime exists.
