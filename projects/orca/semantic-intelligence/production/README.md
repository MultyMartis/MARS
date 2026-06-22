# ORCA Full-Corpus Production Semantic Intelligence

**Wave:** 3  
**Status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED` (uncommitted)  
**Locus:** `projects/orca/semantic-intelligence/production/`

## Placement decision

Wave 3 extends the existing ORCA Semantic Intelligence system under `projects/orca/semantic-intelligence/`. It does **not** duplicate semantic logic inside `projects/mars-search-ppc-production/`.

| Layer | Path | Role |
|-------|------|------|
| Architecture / contracts (P0-A–C) | `../architecture/`, `../taxonomy/`, `../contracts/` | Authority — reused |
| Integration enforcement core (P0-I) | `../integration/runtime/` | Contract loader, invariants — imported |
| **Production pipeline (Wave 3)** | `./` | Full-corpus runner, assessor, tiers, ownership, clustering, negatives |

Lifecycle gating uses `projects/mars-search-ppc-production/runtime/src/lifecycle-gate.mjs` via `runtime/production-gate.mjs`.

## Pipeline stages (SPPC-05–09)

```text
Full Canonical Registry + Business Scope + Service Registry
  → Commercial Admission (assessor + hard rules + invariants)
  → Automated Reassessment (risk candidates)
  → Adjudication (FINAL ACCEPT / REJECT / ABSTAIN)
  → T1–T5 Demand Segmentation (ACCEPT only)
  → Service Ownership
  → Semantic Clustering + Cluster QA
  → Negative Intelligence + Conflict Validation
  → Bounded Review Queue + Semantic Output Pack
```

## Model boundary

Live LLM/model execution is **NOT VALIDATED**. Production uses `deterministic-assessor.mjs` (fixture/diagnostic) via assessor contract. See `contracts/MODEL-RUNTIME-BOUNDARY-v1.md`.

## Entry points

```bash
node runtime/cli/orca-semantic-production.mjs run --manifest <path> --out <dir>
node tests/run-production-test-matrix.mjs
node tests/run-wave3-bypass-audit.mjs
node tests/run-scale-test.mjs
node tests/run-p0i-comparison.mjs
```
