# R4 — Implementation Decision v1

**Type:** Human gate decision record — engineering start for R4 EAR Publish Layer  
**Date:** 2026-06-07  
**Charter:** [R4-IMPLEMENTATION-CHARTER-v1.md](R4-IMPLEMENTATION-CHARTER-v1.md)  
**Prior decision:** [R4-DECISION-v1.md](R4-DECISION-v1.md) — **APPROVED WITH NOTES** (R4 program charter)

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | May **R4 engineering** (implementation charter scope) proceed and **R4.1+ contract work** begin after human sign-off? |
| **Outcome** | **APPROVED WITH NOTES** |
| **Scope of approval** | R4 mission, engineering scope, work packages R4.1–R4.9, Published Snapshot model, publish state model, consumer visibility model, publish metadata model, Publish Result contract, Publish Flow contract, Publish Engine architecture scope, publish boundary review, readiness review gate, success/stop criteria per [R4-IMPLEMENTATION-CHARTER-v1.md](R4-IMPLEMENTATION-CHARTER-v1.md) |
| **Explicitly not approved by this decision** | R4 runtime code, Publish engine implementation, Validate execution, quality certification, snapshot assembly, evidence generation, quarantine mutation, OCPilot integration, live acquisition, SITE-001 / PILOT execution, Store redesign |

---

## Rationale

1. **R4 charter gate satisfied** — [R4-DECISION-v1.md](R4-DECISION-v1.md) authorizes Implementation Charter; R4 mission, scope, publish lifecycle, and R5→R4 boundary documented in [R4-CHARTER-v1.md](R4-CHARTER-v1.md).

2. **R5 readiness supports R4 planning** — [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) authorizes R4 planning in parallel; R5.6 defines advisory `PublishEligibilityRecommendation` consumed by R4; R5.8 confirms R4 Publish ownership not absorbed by R5.

3. **Architecture alignment** — Implementation charter maps [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R4 Snapshot Publisher to contract models without absorbing R3 assembly, R5 Validate, or R2 evidence generation.

4. **Store vs Publish explicit** — [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) § Task 5 G-09 resolved; R4 inherits frozen layout; consumer access begins only after R4 per [EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md).

5. **Boundary preservation** — R4 does not validate, certify quality, assemble sections, generate evidence, or mutate quarantine. Distinct `PublishResult` mandated (N-R4-03). Dual HITL documented (N-R4-04, N-R4-05).

6. **Mandatory questions answered** — Implementation charter explicitly addresses: what makes a snapshot published; what does not; why Store ≠ Publish; why Publish does not create quality; why consumer visibility begins only after Publish.

7. **Upstream debt acknowledged** — Validate Engine not implemented, contract-path Store persist, mock R5 bundle path — not blockers for implementation charter per R4-DECISION notes N-R4-11, N-R4-12.

**APPROVED WITH NOTES** (not bare **APPROVED**): human sign-off required before first R4 code merge per N-R4-10 and R1/R2/R3/R5 gate pattern; publish state encoding, consumer registry pointer, and PublishResult serialization remain **SAFE UNKNOWN** until R4.1+ implementation resolves.

**FAIL** would apply if implementation charter chartered Validate as R4, omitted R5→R4 boundary, assigned quality certification to R4, merged Publish with assembly, allowed Publish without Validate, or proposed runtime code in charter phase — **none apply**.

---

## Notes (implementation)

| Note | Action |
|------|--------|
| N-R4I-01 | First engineering milestone: **R4.1 Published Snapshot Model** |
| N-R4I-02 | Do not implement Validate, assembly, or evidence generation in R4 |
| N-R4I-03 | Emit distinct artefact: `PublishResult` — never reuse `ValidationResult` |
| N-R4I-04 | R5 bundle is Publish entry precondition — implement at engine entry gate |
| N-R4I-05 | Human HITL mandatory for pilot — dual gate: Validate sign-off + Publish approval |
| N-R4I-06 | NOT_ELIGIBLE → BLOCKED PublishResult — fail closed |
| N-R4I-07 | Disambiguate R5 Validate / R4 Publish / consumer intake in all R4 docs |
| N-R4I-08 | Published snapshot read-only promotion — no section mutation |
| N-R4I-09 | Mock R5 bundle acceptable until Validate Engine exists |
| N-R4I-10 | Human approver must record approval below before R4.1 code |
| N-R4I-11 | Consumer registry pointer — resolve at R4.3/R4.7 |
| N-R4I-12 | Support stored and in-memory validated snapshot inputs |

---

## Conditions for human code approval

| ID | Condition | Status |
|----|-----------|--------|
| AP-R4-01 | [R4-IMPLEMENTATION-CHARTER-v1.md](R4-IMPLEMENTATION-CHARTER-v1.md) reviewed and accepted | Pending |
| AP-R4-02 | R4/R5 boundary (promotion only, no Validate) — accepted | Documented in charter |
| AP-R4-03 | R4/R3 boundary (read-only, no section population) — accepted | Documented in charter |
| AP-R4-04 | Store vs Publish distinction — accepted | Documented in charter |
| AP-R4-05 | Dual HITL mandatory for pilot — accepted | Documented in charter |
| AP-R4-06 | External `output_root` only; no Publish bulk in git — accepted | R1.8B + EAR-STORAGE-MODEL |
| AP-R4-07 | PILOT-001 / SITE-001 execution **not** implied | Acknowledged |
| AP-R4-08 | Mock-first Publish; live path requires Execution Authorization — accepted | Documented |

---

## Conditions that block live pilot (not R4 mock contract work)

| ID | Blocker | Owner |
|----|---------|-------|
| BL-R4-01 | PILOT-001 Execution Authorization | Pilot governance |
| BL-R4-02 | Operator `credential_ref` and output root bindings | Operator |
| BL-R4-03 | Live SFTP connected acquire | R1 connector + pilot charter |
| BL-R4-04 | R5 Validate Engine implementation (live bundle) | R5 — parallel track |
| BL-R4-05 | Contract-path Store persist for validated snapshots | R3 debt |
| BL-R4-06 | Consumer program intake wiring (OCPilot) | Consumer programs |

R4 contract-model work (R4.1–R4.6) may proceed after AP-R4-01–AP-R4-08 without BL-R4-01–BL-R4-06 resolved. Publish **code** (R4.7+) requires R4.9 Readiness Review pass.

---

## Gate transition

| Gate | Before Implementation Charter | After Implementation Charter |
|------|------------------------------|------------------------------|
| R4 Charter | **COMPLETE** | **COMPLETE** |
| R4 Implementation Charter | **NEXT** | **COMPLETE** |
| R4 Status | CHARTERED | **AUTHORIZED FOR R4.1** |
| R4 Implementation (code) | **NOT AUTHORIZED** | **NOT AUTHORIZED** until R4.9 + human sign-off AP-R4-10 |
| R4.1 Published Snapshot Model | **NOT STARTED** | **NEXT** |
| R5 Validate Engine code | **AUTHORIZED** (human gate) | **AUTHORIZED** — parallel track |

---

## Sign-off record

| Role | Record |
|------|--------|
| Charter executor | Agent architecture charter 2026-06-07 |
| Human implementation approval | **PENDING** (AP-R4-10) |

---

## Evidence

| # | Evidence | Location |
|---|----------|----------|
| D-R4I-01 | R4 program charter | [R4-CHARTER-v1.md](R4-CHARTER-v1.md) |
| D-R4I-02 | R4 charter gate — APPROVED WITH NOTES | [R4-DECISION-v1.md](R4-DECISION-v1.md) |
| D-R4I-03 | R5 readiness — R4 planning authorized | [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) |
| D-R4I-04 | R5→R4 publish boundary | [R5-CHARTER-v1.md](R5-CHARTER-v1.md) § Publish Boundary |
| D-R4I-05 | Publish Eligibility advisory contract | [R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md](R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md) |
| D-R4I-06 | R5/R3/R4 boundary audit | [R5.8-VALIDATION-BOUNDARY-DECISION-v1.md](R5.8-VALIDATION-BOUNDARY-DECISION-v1.md) |
| D-R4I-07 | Store vs Publish distinction | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) § Task 5 |
| D-R4I-08 | Publishing architecture | [EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md) |
| D-R4I-09 | Readiness gates G3–G4 | [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md) |
| D-R4I-10 | Backlog R4 definition | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R4 |
| D-R4I-11 | R4 Implementation Charter artifact | [R4-IMPLEMENTATION-CHARTER-v1.md](R4-IMPLEMENTATION-CHARTER-v1.md) |
