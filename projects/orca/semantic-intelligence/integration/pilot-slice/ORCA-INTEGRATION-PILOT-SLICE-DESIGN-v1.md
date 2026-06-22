# ORCA Integration Pilot Slice Design v1

**Design ID:** `orca-integration-pilot-slice-v1`  
**Target size:** ~200 phrases  
**Status:** `DESIGN ONLY — NOT EXECUTED`

---

## Purpose

Verify P0-I integration and enforcement on a bounded slice **before** B0 benchmark, gold labels, or Corvonero rerun.

### Verifies

- Contracts actually loaded (not manifest-only)
- Schema-valid semantic record output
- ACCEPT / REJECT / ABSTAIN emission
- Blocking invariants fire on known failure patterns
- Human review routing
- Legacy regex comparison without legacy authority

### Is not

- B0 benchmark qualification
- Gold dataset
- Production semantic core
- Corvonero restart
- Classifier accuracy proof (D3 thresholds out of scope)

---

## Phrase source categories (design only — no selection in this task)

| Category | Source | Count (target) | Label status |
|----------|--------|----------------|--------------|
| Generic fixtures | `semantic-intelligence/fixtures/` | ~40 | Shape tests only |
| Corvonero diagnostic | Freshly selected from MIG corpus | ~50 | **NOT GOLD** |
| Triumph-derived examples | Scenario-first commercial patterns | ~30 | **NOT GOLD** |
| Hard negatives | Career/edu/DIY/navigational | ~40 | **NOT GOLD** |
| Ambiguity stress | Short-head, problem-query | ~40 | **NOT GOLD** |

**Total:** ~200

Old Corvonero `ELIGIBLE COMMERCIAL` labels **must not** be used as truth.

---

## Execution prerequisites

1. P0-I charter operator approval
2. Implementation backlog I-01–I-08 complete
3. Contract loading manifest checksums pinned
4. Operator approves phrase selection list (separate task)

---

## Success artifacts (post-implementation)

| Artifact | Owner |
|----------|-------|
| Pilot run log | I-08 |
| Contract-consumption report | I-07 |
| Legacy comparison report | I-06 |
| Invariant violation summary | I-04 |
| Review routing sample | I-05 |

---

## Stop boundary

Pilot output must not feed clustering, negatives, campaign production, or export.
