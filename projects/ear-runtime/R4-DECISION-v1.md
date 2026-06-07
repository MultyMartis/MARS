# R4 Decision v1

**Type:** Charter gate decision — R4 EAR Publish Layer  
**Date:** 2026-06-07  
**Charter:** [R4-CHARTER-v1.md](R4-CHARTER-v1.md)  
**Prior decision:** [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) — **READY FOR R5 IMPLEMENTATION WITH NOTES**; R5.9 architecture **APPROVED**

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | May **R4 Charter** close and **R4 Implementation Charter** phase proceed? |
| **Outcome** | **APPROVED WITH NOTES** |
| **Scope of approval** | R4 mission, scope, non-goals, inputs, outputs, publish lifecycle, Published Snapshot definition, ownership matrix, consumer boundary, R5→R4 boundary, success/stop criteria per [R4-CHARTER-v1.md](R4-CHARTER-v1.md) |
| **Explicitly not approved by this decision** | R4 runtime code, Publish engine implementation, Validate execution, Store redesign, snapshot assembly, evidence generation, OCPilot integration, live acquisition, SITE-001 / PILOT execution |

---

## Rationale

1. **R5 readiness gate satisfied** — [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) authorizes R4 planning; R5.1–R5.9 complete; R5.6 defines advisory `PublishEligibilityRecommendation` consumed by R4; R5.8 confirms R4 Publish ownership not absorbed by R5.

2. **Authoritative mission aligned** — [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R4 defines Snapshot Publisher as Publish gate + consumer-visible reference; charter correctly positions R4 as promotion layer after R5 Validate and Store.

3. **Pipeline contract explicit** — `R2 Evidence → R3 Candidate → R5 Validate → Store → R4 Publish → Consume` documented; Publish cannot bypass Validate; R4 never validates or certifies quality.

4. **Boundary preservation** — R4 does not redesign R1/R2/R3/R5, does not assemble sections (R3), does not generate evidence (R2), does not execute Validate (R5). Matches R5.8 ownership matrix and R3.6 complementary checks.

5. **Store vs Publish distinction explicit** — [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) G-09 resolved; R4 inherits frozen layout; consumer access begins only after R4 per [EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md).

6. **Mandatory questions answered** — Charter explicitly addresses: why Validate does not Publish; why Publish does not Validate; why consumer access begins only after R4; why R4 does not own quality.

7. **R5/R3 debt acknowledged** — In-memory validated path, Store persist adapter, Validate Engine not implemented — not blockers for R4 charter per R5 readiness decision.

**APPROVED WITH NOTES** (not bare **APPROVED**): Implementation charter must carry R5 readiness notes, R3 Store persist debt, and R5 Validate Engine not yet implemented; **R4 code implementation remains NOT AUTHORIZED** until R4 Implementation Charter and human gate per R1/R2/R3/R5 pattern.

**FAIL** would apply if charter contradicted backlog (e.g. chartered Validate as R4), omitted R5→R4 boundary, assigned quality certification to R4, allowed Publish without Validate, or merged Publish with assembly — **none apply**.

---

## Notes (carried to R4 Implementation Charter)

| Note | Action |
|------|--------|
| N-R4-01 | Title implementation work **R4 — EAR Publish Layer** / Snapshot Publisher — not Validate or Snapshot Assembly |
| N-R4-02 | First implementation consumes R5 bundle: `ValidationResult`, optional `ValidateReport`, `PublishEligibilityRecommendation` — not R3 assembly result alone |
| N-R4-03 | Emit distinct artefact: `PublishResult` — never reuse `ValidationResult` as Publish outcome |
| N-R4-04 | R5 Validate pass + ELIGIBLE recommendation are preconditions — separate Publish HITL mandatory |
| N-R4-05 | Human HITL mandatory for pilot — Publish helpers assist, do not replace operator Publish sign-off |
| N-R4-06 | Fail closed on NOT_ELIGIBLE per R5.6 — default block until re-Validate or audited override |
| N-R4-07 | Disambiguate R5 Validate / R4 Publish / consumer intake in all R4 docs |
| N-R4-08 | Published snapshot is read-only promotion — no section mutation at Publish |
| N-R4-09 | Consumer registry pointer location — resolve at Implementation Charter (**SAFE UNKNOWN** at R4 Charter) |
| N-R4-10 | Human implementation approval gate — R4 Implementation Charter does not bypass prior gate pattern |
| N-R4-11 | R5 Validate Engine may not exist when R4 implementation starts — R4 may use mock R5 bundle for engineering |
| N-R4-12 | Contract-path Store persist (R3 debt) — R4 Publish design must support stored and in-memory validated inputs |

---

## Evidence

| # | Evidence | Location |
|---|----------|----------|
| D-R4-01 | R5 readiness review — R4 planning authorized | [R5-READINESS-REVIEW-v1.md](R5-READINESS-REVIEW-v1.md) |
| D-R4-02 | R5 closure — architecture complete with notes | [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) |
| D-R4-03 | R5→R4 publish boundary | [R5-CHARTER-v1.md](R5-CHARTER-v1.md) § Publish Boundary |
| D-R4-04 | Publish Eligibility advisory contract | [R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md](R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md) |
| D-R4-05 | R5/R3/R4 boundary audit | [R5.8-VALIDATION-BOUNDARY-DECISION-v1.md](R5.8-VALIDATION-BOUNDARY-DECISION-v1.md) |
| D-R4-06 | Store vs Publish distinction | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) § Task 5 |
| D-R4-07 | Publishing architecture | [EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md) |
| D-R4-08 | Readiness gates G3–G4 | [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md) |
| D-R4-09 | Backlog R4 definition | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R4 |
| D-R4-10 | R4 Charter artifact | [R4-CHARTER-v1.md](R4-CHARTER-v1.md) |

---

## Gate transition

| Gate | Before R4 Charter | After R4 Charter |
|------|-------------------|------------------|
| R5 Readiness Review | **COMPLETE** | **COMPLETE** |
| R4 Charter | **AUTHORIZED** | **COMPLETE** |
| R4 Implementation Charter | **NOT STARTED** | **NEXT** — authorized to draft |
| R4 Implementation (code) | **NOT AUTHORIZED** | **NOT AUTHORIZED** until Implementation Charter + human decision |
| R5 Validate Engine code | **AUTHORIZED** (human gate) | **AUTHORIZED** — parallel track |

---

## Sign-off record

| Role | Record |
|------|--------|
| Charter executor | Agent architecture charter 2026-06-07 |
| Human implementation approval | **PENDING** (R4 Implementation Charter) |
