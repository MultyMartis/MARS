# R2 — Architecture Consolidation Decision v1

**Type:** Program gate decision — **no** implementation  
**Date:** 2026-06-05  
**Review:** [R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md](R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md)  
**Subject:** R2 readiness before **R2.7 Evidence Package Generator**

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | Is the complete R2 architecture chain (R2 Charter through R2.6) **coherent, internally consistent, and ready** for R2.7 Evidence Package Generator work? |
| **Outcome** | **PASS WITH NOTES** |
| **R2 Architecture Consolidation** | **COMPLETE** |
| **R2 Ready For Generator** | **YES** |
| **Scope of pass** | Terminology, ownership, lifecycle, identity, storage, validation, model alignment across R2.1–R2.6; blind spots documented; no new architecture |
| **Explicitly not passed by this decision** | Generator implementation; validator code; quarantine persist; HandoffContract code; R3/R5 charters; live acquisition |

---

## Rationale

1. **Coherence** — Single evidence contract (`EvidencePackage`), sibling storage (`evidence/` vs `snapshots/`), explicit R2.6 handoff, and R2/R5 validation split form a closed architectural story from Acquire through Archive without contradiction across R2-CHARTER, R2-IMPLEMENTATION-CHARTER, and R2.1–R2.6.

2. **Internal consistency** — Cross-milestone invariant families (INV-*, ART-INV-*, VAL-INV-*, Q-INV-*, HO-INV-*) align without contradictory ownership. Minor terminology drift (T-01–T-07) is documented and **non-blocking**.

3. **Model alignment** — `evidence_package_models.py` matches R2.1 structure and R2.2–R2.6 implications; R2.3 taxonomy constants present; no proven contract gap requiring model change before R2.7.

4. **Prior gates consistent** — R2.2–R2.6 each **PASS WITH NOTES**; consolidation finds no regressions or new blockers relative to those decisions.

5. **Generator readiness** — R2.7 inputs (model, identity rules, artifact taxonomy, validation boundary catalog, quarantine layout, handoff inputs H-IN-01–H-IN-10) are **defined**. Remaining gaps (validator code, persist, dual R1.6 mock) are **expected R2.7 deliverables**, not architecture holes.

**PASS WITH NOTES** (not bare **PASS**): documented drift items (mock dual-model, `acquisition_id` unification, N-07 filenames, R2.4 validator not coded, SAFE UNKNOWN registry); no FAIL criteria met.

**FAIL** would apply if: contradictory ownership between R2/R3/R5; evidence/snapshot merge permitted; quality certification at evidence stage; consumer quarantine access chartered; or model contradicts R2.2–R2.6 invariants — **none apply**.

---

## Conditions satisfied

| ID | Condition | Status |
|----|-----------|--------|
| C-PASS-01 | Full R2 chain reviewed (Charter + Implementation Charter + R2.1–R2.6) | **SATISFIED** |
| C-PASS-02 | Terminology mismatches reported | **SATISFIED** — T-01–T-07 |
| C-PASS-03 | R2/R3/R4/R5/Operator/Consumer ownership verified | **SATISFIED** — no contradictions |
| C-PASS-04 | Lifecycle transitions traced Acquire → Archive | **SATISFIED** — no circular deps |
| C-PASS-05 | Identity trace (`acquisition_id`, `site_ref`, `connector_class`, `artifact_ref`, `snapshot_id`) | **SATISFIED** |
| C-PASS-06 | Storage layout consistent (`evidence/` vs `snapshots/`) | **SATISFIED** |
| C-PASS-07 | R2 vs R5 validation boundary consistent | **SATISFIED** |
| C-PASS-08 | Model alignment review without code change | **SATISFIED** |
| C-PASS-09 | Blind spots documented, not solved | **SATISFIED** — B-01–B-15 |
| C-PASS-10 | No implementation in consolidation milestone | **SATISFIED** |

---

## Notes (carry to R2.7)

| Note | Action | Owner |
|------|--------|-------|
| N-R2-CON-01 | Unify mock `acquisition_id` evidence vs persist | R2.7 |
| N-R2-CON-02 | Migrate mock CLI from R1.6 to R2.1 package | R2.7 |
| N-R2-CON-03 | Resolve N-07 `evidence/` index filename(s) at persist | R2.7 |
| N-R2-CON-04 | Implement R2-V-* validator alongside generator | R2.7 |
| N-R2-CON-05 | Use disambiguated Validate terminology in R2.7 docs | R2.7 |
| N-R2-CON-06 | Do not introduce `evidence_id` | Standing |
| N-R2-CON-07 | R3/R5 charters must reference R2.6 / R2.4 respectively | R3 / R5 planning |

---

## Gate transition

| Milestone | Before consolidation | After consolidation |
|-----------|---------------------|---------------------|
| R2.6 Evidence → Snapshot Handoff | **DONE** | **DONE** |
| R2 Architecture Consolidation | **NEXT** | **COMPLETE** |
| R2.7 Evidence Package Generator | **Blocked on consolidation** | **NEXT** — **READY** |

---

## Success criteria answers

| Criterion | Answer |
|-----------|--------|
| Is R2 architecture coherent? | **Yes** |
| Is R2 internally consistent? | **Yes, with documented minor drift (non-blocking)** |
| Is R2 ready for generator work? | **Yes** |
| Unresolved items | See [R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md](R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md) § Blind Spots — **none block R2.7** |

---

## Evidence index

| ID | Source |
|----|--------|
| D-R2-CON-01 | [R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md](R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md) |
| D-R2-CON-02 | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-DECISION-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-DECISION-v1.md) |
| D-R2-CON-03 | [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md) § Work Breakdown R2.7 |
