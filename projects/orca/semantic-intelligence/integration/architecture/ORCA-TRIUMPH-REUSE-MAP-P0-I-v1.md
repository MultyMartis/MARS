# ORCA Triumph Reuse Map — P0-I Context v1

**Map ID:** `orca-triumph-reuse-map-p0-i-v1`  
**Date:** 2026-06-22

---

## Classification key

| Action | Meaning |
|--------|---------|
| **REUSE DIRECTLY** | Use in P0-I admission path without modification |
| **ADAPT** | Use with integration wrapper or scope change |
| **DOWNSTREAM ONLY** | After admission PASS — not in P0-I scope |
| **NOT IN ADMISSION** | Do not use for semantic admission decisions |

---

## Triumph assets

| Asset | Action | Rationale |
|-------|--------|-----------|
| Export validators (`validate-export*.mjs`, 345 rules) | **DOWNSTREAM ONLY** | Export parity — not admission |
| Artifact parity tools | **ADAPT** | Hook as I-09 external artifact parity — post-admission |
| Curated JSON SoT patterns (`intent-groups`, seeds) | **ADAPT** | Inform authority design and protected seed policy — not auto-ACCEPT |
| Scenario-first commercial doctrine | **ADAPT** | Inform annotation examples and operator intake — not regex substitute |
| `is_primary` seed protection pattern | **ADAPT** | Integrate in operator-scope / seed consumer (post-P0-I) |
| Triumph 64-phrase curated set | **NOT IN ADMISSION** | Project-specific — diagnostic examples only (I7) |
| Demand evidence trace workflow | **ADAPT** | Human review and provenance model |
| SE blocklists (employment, edu) | **ADAPT** | Merge into annotation policy consumer — avoid third duplicate |
| Validation CLI 345 export rules | **NOT IN ADMISSION** | Do not replace P0-I invariant validator |
| Commander export pipeline | **DOWNSTREAM ONLY** | Blocked until semantic core approval |
| Triumph per-phrase operator review UX | **ADAPT** | Human review router pattern |

---

## Corvonero assets

| Asset | Action | Rationale |
|-------|--------|-----------|
| `run-clean-room-semantic-pipeline-v1.mjs` regex | **ADAPT** | Diagnostic baseline only (I5) |
| MIG Wordstat corpus | **ADAPT** | Pilot phrase source — labels not truth |
| Service scope registry | **ADAPT** | Operator-scope consumer input |
| Clean-room reports | **REUSE DIRECTLY** | Failure analysis evidence |
| v7 contract audit at export | **DOWNSTREAM ONLY** | Proves export gate — missed admission |

---

## ORCA P0 documents

| Document | Action |
|----------|--------|
| P0-A ADR | **REUSE DIRECTLY** |
| P0-B taxonomy/schema/invariants | **REUSE DIRECTLY** via consumers |
| P0-C annotation guideline | **REUSE DIRECTLY** via policy consumer |
| P0-D benchmark charter | **DOWNSTREAM ONLY** — hold until P0-I PASS |
