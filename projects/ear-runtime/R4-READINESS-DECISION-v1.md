# R4 — Readiness Decision v1

**Type:** Program gate decision — **no** Publish Engine implementation, **no** live pilot  
**Date:** 2026-06-07  
**Review:** [R4-READINESS-REVIEW-v1.md](R4-READINESS-REVIEW-v1.md)  
**Subject:** R4 architecture closure and R4 implementation code authorization

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | Is R4 architecturally complete enough to close the R4 design phase and authorize future R4 **implementation** work? |
| **Outcome** | **READY FOR R4 IMPLEMENTATION WITH NOTES** |
| **R4 Status** | **COMPLETE WITH NOTES** (architecture and contracts) |
| **R4 implementation code** | **AUTHORIZED** (subject to human implementation gate) |
| **Scope of pass** | R4 Charter + R4 Implementation Charter closed; R4.1–R4.8 milestones complete; IAC-R4-01–09 satisfied; IAC-R4-10 satisfied with notes; R4.8 boundary PASS WITH NOTES; mock-path R3 candidate verified; no critical ownership conflicts; EAR publish architecture closed at design layer |
| **Explicitly not passed by this decision** | Publish Engine code; `publish_result_models.py`; `--publish-snapshot` CLI; Store publish-metadata persist adapter; live SITE-001/SFTP Publish; post-implementation charter IAC (operator can execute Publish); OCPilot integration |

---

## Architecture verdict

| Verdict | **R4 COMPLETE WITH NOTES** |
|---------|----------------------------|

**Why COMPLETE WITH NOTES:**

1. All R4.1–R4.8 milestone gate artefacts exist with **PASS WITH NOTES** decisions.
2. Contract chain is coherent: Published Snapshot (R4.1) → publish state (R4.2) + visibility (R4.3) + metadata (R4.4) → PublishResult (R4.5) + flow (R4.6) → engine architecture (R4.7) → boundary audit (R4.8).
3. R4.8 confirms no critical R2/R3/R5/Consumer absorption; VB-R4-01–18 defined.
4. Upstream R2, R3, R5 **COMPLETE WITH NOTES** — documented debt does not block R4 architecture or mock-path Publish engineering.
5. Deferred items (engine, result dataclass module, CLI, Store adapter, consumer registry encoding) are explicitly scoped to post-R4.9 implementation — not hidden gaps.

**Why not bare COMPLETE:** no Publish Engine or CLI yet; R4.5 contract-only (no Python module); inherited R2/R3/R5 debt for live paths; SAFE UNKNOWN on Store metadata encoding and consumer registry pointer; human implementation gate still required per program pattern.

**FAIL** would apply if: R4 absorbed Validate, assembly, or evidence generation; quality certification assigned to R4; critical boundary violation; missing R4.1–R4.8 artefacts; or contradictory ownership — **none apply**.

---

## Rationale

1. **All required milestones have gate artefacts** — R4.1 through R4.8 each have model/contract/review documents with **PASS WITH NOTES** decisions; R4 Charter and R4 Implementation Charter are **COMPLETE**.

2. **Contract chain coherent** — `PublishedSnapshot` (R4.1) → publish lifecycle (R4.2) → consumer visibility (R4.3) + publish metadata (R4.4) → `PublishResult` (R4.5) + HITL flow (R4.6) → Publish Engine architecture (R4.7) → boundary audit (R4.8). R4.7 seven stages map to upstream contracts without contradiction.

3. **Ownership boundary clean** — R4.8 confirms R4 does not absorb R2 evidence, R3 assembly, or R5 Validate. VB-R4-01–18 defined. Medium drifts (DRIFT-R4-01–08) are implementation-time guidance, not architecture blockers.

4. **Upstream dependencies satisfied** — R2, R3, and R5 **COMPLETE WITH NOTES** with documented debt that does not block R4 architecture or mock-path Publish implementation. `--contract-snapshot` produces valid R3 candidate; mock R5 bundle acceptable per A-R4-10.

5. **R4 model layer exists without premature engine** — R4.1–R4.4 dataclass modules in `runtime/shared/` contain contracts only; no `ear_publish_engine.py`, no Publish logic in R2/R3 validators — aligned with charter intent.

6. **EAR publish architecture closed** — R4 design phase complete; no further R4 architecture milestones required before implementation authorization.

---

## Mandatory answers (decision record)

| # | Question | Answer |
|---|----------|--------|
| 1 | Is R4 architecturally complete? | **Yes, with notes** |
| 2 | Is R4 internally coherent? | **Yes** |
| 3 | Can implementation begin later? | **Yes** — authorized subject to human gate |
| 4 | Can R4 publish validated snapshots? | **Yes, architecturally** — runtime not yet implemented |
| 5 | Can R4 support future SITE-001 publish flow? | **Yes, architecturally** — live path gated by Execution Authorization + upstream debt |
| 6 | Can R4 support future OCPilot consumers? | **Yes** — visibility grant + `consumer_target`; intake is consumer-owned |
| 7 | What remains outside R4? | R5 Validate; R3 assembly; R2 evidence; consumer execution; live acquisition |
| 8 | What debt remains? | Engine, result models, CLI, Store adapter, inherited R2/R3/R5 live-path debt — see review § Outstanding Debt |

---

## Conditions satisfied

| ID | Condition | Status |
|----|-----------|--------|
| C-R4R-PASS-01 | R4 Charter + Implementation Charter complete | **SATISFIED** |
| C-R4R-PASS-02 | R4.1–R4.8 milestone decisions exist | **SATISFIED** |
| C-R4R-PASS-03 | IAC-R4-01–IAC-R4-09 satisfied | **SATISFIED** |
| C-R4R-PASS-04 | R4.8 boundary review PASS WITH NOTES | **SATISFIED** |
| C-R4R-PASS-05 | R2/R3/R5 dependencies COMPLETE WITH NOTES | **SATISFIED** |
| C-R4R-PASS-06 | R3 candidate available on `--contract-snapshot` | **SATISFIED** |
| C-R4R-PASS-07 | No R4 Publish logic in R2/R3 runtime code | **SATISFIED** |
| C-R4R-PASS-08 | VB-R4-01–18 invariants defined | **SATISFIED** |
| C-R4R-PASS-09 | No critical ownership conflict | **SATISFIED** |
| C-R4R-PASS-10 | No implementation changes in this review | **SATISFIED** |

---

## Conditions partially satisfied (notes — not blockers)

| ID | Condition | Status | Carry-forward |
|----|-----------|--------|---------------|
| C-R4R-NOTE-01 | IAC-R4-10 ready for implementation phase | **SATISFIED WITH NOTES** | Human gate before first engine PR |
| C-R4R-NOTE-02 | Post-implementation charter IAC (operator can execute Publish) | **NOT SATISFIED** | Expected — code not yet implemented |
| C-R4R-NOTE-03 | `publish_result_models.py` | **NOT SATISFIED** | First R4.7+ implementation slice |
| C-R4R-NOTE-04 | Consumer registry pointer encoding | **PARTIALLY SPECIFIED** | N-R4.8-07 — resolve in first adapter PR |
| C-R4R-NOTE-05 | Store publish metadata write scope | **PARTIALLY SPECIFIED** | N-R4.8-03 — metadata only |

---

## Conditions not satisfied (debt — does not block architecture closure)

| ID | Condition | Status | Carry-forward |
|----|-----------|--------|---------------|
| C-R4R-DEBT-01 | Publish Engine code | **NOT SATISFIED** | Post-decision implementation |
| C-R4R-DEBT-02 | `--publish-snapshot` CLI | **NOT SATISFIED** | R4.7 implementation |
| C-R4R-DEBT-03 | Store publish metadata adapter | **NOT SATISFIED** | R1.8 + R4 adapter |
| C-R4R-DEBT-04 | R5 Validate Engine (real bundle) | **NOT SATISFIED** | R5 implementation — mock acceptable for R4 engineering |
| C-R4R-DEBT-05 | Contract-path Store persist (R3) | **NOT SATISFIED** | R3-adjacent |
| C-R4R-DEBT-06 | Live SITE-001 / SFTP Publish | **NOT SATISFIED** | Execution Authorization |

---

## Implementation authorization recommendation

| Field | Value |
|-------|-------|
| **Recommendation** | **AUTHORIZE R4 IMPLEMENTATION** |
| **First implementation slice** | `publish_result_models.py` (R4.5) + `ear_publish_engine.py` skeleton (R4.7) + mock R5 bundle fixture |
| **Human gate** | **Required** before first Publish Engine PR — per R4-IMPLEMENTATION-DECISION-v1 pattern |
| **Parallel work** | R5 Validate Engine implementation may proceed independently; runtime order Validate → Publish preserved |
| **Live execution** | **NOT AUTHORIZED** — requires Execution Authorization + D-LIVE-* debt resolution |

---

## Notes (carry to implementation)

| Note | Action | Owner |
|------|--------|-------|
| N-R4R-01 | First implementation slice: `ear_publish_engine.py` skeleton + `publish_result_models.py` | R4 implementation |
| N-R4R-02 | Disambiguate CLI/log labels: "promotion assembly" vs "snapshot assembly"; "gate verification" vs "EAR Validate" | R4 implementation |
| N-R4R-03 | Stage 2 implementation must be gate-read only — no category assessors or possession logic | R4 implementation |
| N-R4R-04 | Store publish metadata write = adapter side effect — metadata only, not section tree | Store adapter |
| N-R4R-05 | Combined Store+Publish workflow must enforce Validate HITL at Stage 1 precondition | R4.6 / engine |
| N-R4R-06 | Production default: require Store placement confirmation — in-memory path pilot-only | R4 implementation |
| N-R4R-07 | Import VB-R4-01–18 into engine PR review checklist | R4 implementation |
| N-R4R-08 | Resolve consumer registry pointer ownership in first adapter PR | R4 implementation |
| N-R4R-09 | Mock R5 bundle acceptable until R5 engine exists — do not block R4 engineering | Standing |
| N-R4R-10 | Human HITL mandatory: Validate sign-off + Publish approval — engine must not bypass | Standing |

---

## Gate transition

| Milestone | Before review | After review |
|-----------|---------------|--------------|
| **R4 program (architecture)** | IN PROGRESS — R4.8 DONE | **COMPLETE WITH NOTES** |
| **R4.9 Readiness Review** | Current gate | **DONE** |
| **R4 implementation code** | NOT AUTHORIZED | **AUTHORIZED** (human gate before first PR) |
| **EAR publish architecture (design)** | Open through R4.8 | **CLOSED** |
| **R5 Validate Engine implementation** | AUTHORIZED | **Continues** (parallel) |
| **Live Publish / SITE-001** | NOT AUTHORIZED | **NOT AUTHORIZED** |

---

## Human approver

| Field | Value |
|-------|-------|
| **Decision type** | Program readiness gate |
| **Human approver** | **Pending** — operator confirmation |
| **Automated review** | R4.9 readiness review complete 2026-06-07 |
| **Prior human gate** | R4.8 Publish Boundary Review — **PASSED** |

---

## Cross-references

| Document | Use |
|----------|-----|
| [R4-READINESS-REVIEW-v1.md](R4-READINESS-REVIEW-v1.md) | Full review evidence |
| [R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md](R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md) | Boundary authority |
| [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) | Upstream dependency pattern |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Updated program status |
