# R2 — Implementation Decision v1

**Type:** Human gate decision record — engineering start for R2 Evidence Package Generator  
**Date:** 2026-06-04  
**Charter:** [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md)  
**Prior decision:** [R2-DECISION-v1.md](R2-DECISION-v1.md) — **APPROVED WITH NOTES** (R2 program charter)

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | May **R2 engineering** (implementation charter scope) proceed and **R2.1+ code** begin after human sign-off? |
| **Outcome** | **APPROVED WITH NOTES** |
| **Scope of approval** | R2 mission, engineering scope, work breakdown R2.1–R2.7, inputs/outputs, identity model, validation boundary, Evidence → Snapshot boundary, success/stop criteria per [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md) |
| **Explicitly not approved by this decision** | Live acquisition, SFTP execution, SITE-001 / PILOT execution, OpenCart snapshot sections, Publish, OCPilot integration, persistence redesign, normative JSON Schema |

---

## Rationale

1. **Charter gate satisfied** — [R2-CHARTER-v1.md](R2-CHARTER-v1.md) and [R2-DECISION-v1.md](R2-DECISION-v1.md) define R2 as Evidence Package Generator; implementation charter maps gap matrix from [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) without absorbing R3 scope.
2. **Architecture alignment** — [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md), [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md), [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md), and [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R2 match charter inputs, outputs, and acceptance.
3. **R1 dependency chain** — R1 **COMPLETE**; R1.6 skeleton, R1.8C evidence path, and R1-CONTRACT-MAPPING provide traceable upstream inputs; evidence persist deferral resolved at engineering scope (R2.5).
4. **Validation split** — R2 vs R5 boundary documented; no `package_quality_level` at evidence stage (N-03).
5. **Store boundary** — R1.9 frozen; R2 adds `evidence/` only; mock snapshot Store remains Level 0 honest.

**APPROVED WITH NOTES** (not bare **APPROVED**): human sign-off required before first R2 code merge per N-06 and [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) gate pattern; `evidence/` index filenames and checksum registry remain **SAFE UNKNOWN** until implementation resolves or architecture amends.

**NOT APPROVED** would apply if implementation charter chartered OpenCart sections as R2, omitted evidence/snapshot handoff, or authorized live pilot without Execution Authorization — none apply.

---

## Notes (implementation)

| Note | Action |
|------|--------|
| N-01 | First engineering milestone: **R2.1 Evidence Package Model** |
| N-02 | Do not implement `file-manifest/` section population in R2 |
| N-03 | Do not set `package_quality_level` ≥ 1 on evidence or mock snapshot persist |
| N-04 | Publish remains R4 |
| N-05 | Live connector generator path optional; mock path is minimum |
| N-06 | Human approver must record approval below before R2.1 code |
| N-07 | Resolve exact `evidence/` index file names at R2.5 — not blocking charter approval |
| N-08 | `evidence_id` as package root — **SAFE UNKNOWN**; use `acquisition_id` per architecture |

---

## Conditions for human code approval

| ID | Condition | Status |
|----|-----------|--------|
| AP-R2-01 | [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md) reviewed and accepted | Pending |
| AP-R2-02 | R2/R3 boundary (HandoffContract, no OpenCart sections in R2) — accepted | Documented in charter |
| AP-R2-03 | R2/R5 boundary (no quality level on evidence) — accepted | Documented in charter |
| AP-R2-04 | Mock-first generator; live path requires Execution Authorization — accepted | Documented |
| AP-R2-05 | External `output_root` only; no evidence bulk in git — accepted | R1.8C + EAR-STORAGE-MODEL |
| AP-R2-06 | PILOT-001 / SITE-001 execution **not** implied | Acknowledged |

---

## Conditions that block live pilot (not R2 mock code)

| ID | Blocker | Owner |
|----|---------|-------|
| BL-R2-01 | PILOT-001 Execution Authorization | Pilot governance |
| BL-R2-02 | Operator `credential_ref` and output root bindings | Operator |
| BL-R2-03 | Live SFTP connected acquire | R1 connector + pilot charter |

R2 mock-path implementation may proceed after AP-R2-01–AP-R2-06 without BL-R2-01–BL-R2-03 resolved.

---

## Gate transition

| Gate | Before Implementation Charter | After Implementation Charter |
|------|------------------------------|------------------------------|
| R2 Charter | **COMPLETE** | **COMPLETE** |
| R2 Implementation Charter | **READY** | **COMPLETE** |
| R2 Status | AUTHORIZED FOR IMPLEMENTATION CHARTER | **AUTHORIZED FOR ENGINEERING** |
| R2 Implementation (code) | **NOT AUTHORIZED** | **NOT AUTHORIZED** until human AP-R2-01 sign-off |
| Next milestone | — | **R2.1 Evidence Package Model** |

---

## Evidence

| # | Evidence | Location |
|---|----------|----------|
| D-R2I-01 | R2 program charter | [R2-CHARTER-v1.md](R2-CHARTER-v1.md) |
| D-R2I-02 | R2 charter gate | [R2-DECISION-v1.md](R2-DECISION-v1.md) |
| D-R2I-03 | Planning gap matrix | [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) |
| D-R2I-04 | Evidence package semantics | [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) |
| D-R2I-05 | Lifecycle Validate boundary | [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md) |
| D-R2I-06 | Quarantine storage roles | [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |
| D-R2I-07 | Evidence path PC-08 | [R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md](R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md) |
| D-R2I-08 | R1.6 skeleton gap | [R1.6-EVIDENCE-PACKAGE-MODEL-v1.md](R1.6-EVIDENCE-PACKAGE-MODEL-v1.md) |
| D-R2I-09 | Backlog R2 definition | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) |
| D-R2I-10 | R2 Implementation Charter | [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md) |

---

## Sign-off record

| Role | Record |
|------|--------|
| Charter executor | Agent implementation charter 2026-06-04 |
| Human implementation approval | **PENDING** — record below when AP-R2-01 satisfied |

### Approvals

| Role | Name | Date | Decision |
|------|------|------|----------|
| Charter authority (human) | _Pending_ | — | _Pending_ |
| Technical review | Documented 2026-06-04 | 2026-06-04 | Implementation charter drafted; **APPROVED WITH NOTES** for engineering scope |
