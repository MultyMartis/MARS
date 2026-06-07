# R3 — Implementation Decision v1

**Type:** Human gate decision record — engineering start for R3 Snapshot Assembly  
**Date:** 2026-06-05  
**Charter:** [R3-IMPLEMENTATION-CHARTER-v1.md](R3-IMPLEMENTATION-CHARTER-v1.md)  
**Prior decision:** [R3-DECISION-v1.md](R3-DECISION-v1.md) — **APPROVED WITH NOTES** (R3 program charter)

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | May **R3 engineering** (implementation charter scope) proceed and **R3.1+ code** begin after human sign-off? |
| **Outcome** | **APPROVED WITH NOTES** |
| **Scope of approval** | R3 mission, engineering scope, work packages R3.1–R3.7, Snapshot Package Model, identity continuity, safe-unknown strategy, R3/R5 validation boundary, implementation sequence, success/stop criteria per [R3-IMPLEMENTATION-CHARTER-v1.md](R3-IMPLEMENTATION-CHARTER-v1.md) |
| **Explicitly not approved by this decision** | R3 runtime code (until human sign-off below), Validate automation, Publish, OCPilot integration, live acquisition, SITE-001 / PILOT execution, Store redesign, normative JSON Schema |

---

## Rationale

1. **Charter gate satisfied** — [R3-CHARTER-v1.md](R3-CHARTER-v1.md) and [R3-DECISION-v1.md](R3-DECISION-v1.md) define R3 as Snapshot Assembly Layer; implementation charter maps gap matrix from R2 handoff without absorbing R5 Validate or R4 Publish scope.

2. **Architecture alignment** — [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md), [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md), [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md), and [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R3 match charter inputs, outputs, L1 candidate target, and acceptance criteria.

3. **R2 dependency chain** — R2 **COMPLETE WITH NOTES**; R2.6 handoff spec authoritative; R2.7 `--contract-evidence` provides traceable upstream input; HandoffContract code placement resolved at R3.5.

4. **Validation split** — R3 assembly eligibility vs R5 EAR Validate documented; candidate `package_quality_level: 0` default (N-R3-03); no quality inflation at assembly.

5. **Store boundary** — R1.9 frozen; R3 uses existing `{acquisition_id}/snapshots/{snapshot_id}/` layout; no evidence quarantine merge.

6. **Implementation sequence** — R3.1→R3.2→R3.3→R3.4→R3.5→R3.7 ordering minimizes rework; R3.6 boundary review parallel with model phase.

**APPROVED WITH NOTES** (not bare **APPROVED**): human sign-off required before first R3 code merge per N-R3-10 and R1/R2 gate pattern; quarantine persist, production `snapshot_id` algorithm, and physical encoding remain **SAFE UNKNOWN** until implementation resolves.

**REJECTED** would apply if implementation charter chartered Validate or Publish as R3, omitted R3/R5 boundary, merged evidence into snapshot tree, or set assembly default quality ≥ 1 — **none apply**.

---

## Notes (implementation)

| Note | Action |
|------|--------|
| N-01 | First engineering milestone: **R3.1 Snapshot Package Model** |
| N-02 | Do not implement R5 Validate or publish gates in R3 |
| N-03 | Candidate `package_quality_level: 0` until R5 certifies possession |
| N-04 | Retain R1.6 and `--contract-evidence` until R3 chain wired |
| N-05 | Quarantine persist (D-R2-01) — R3-adjacent; mock logical refs minimum |
| N-06 | HandoffContract module — R3.5 deliverable (deferred from R2.6) |
| N-07 | Disambiguate R2 structural validation vs R5 EAR Validate in all R3 docs |
| N-08 | Human approver must record approval below before R3.1 code |
| N-09 | Level 2+ extension/ocmod population — **Future**; L1 placeholder safe-unknown at R3 |
| N-10 | Live acquisition, SFTP, SITE-001 — Execution Authorization only |

---

## Conditions for human code approval

| ID | Condition | Status |
|----|-----------|--------|
| AP-R3-01 | [R3-IMPLEMENTATION-CHARTER-v1.md](R3-IMPLEMENTATION-CHARTER-v1.md) reviewed and accepted | Pending |
| AP-R3-02 | R3/R5 boundary (candidate only, no quality certification) — accepted | Documented in charter |
| AP-R3-03 | R3/R4 boundary (no Publish) — accepted | Documented in charter |
| AP-R3-04 | R2.1 `EvidencePackage` authoritative input; R1.6 deprecated at boundary — accepted | Documented |
| AP-R3-05 | Mock-first generator; live path requires Execution Authorization — accepted | Documented |
| AP-R3-06 | External `output_root` only; no snapshot bulk in git — accepted | R1.8B + EAR-STORAGE-MODEL |
| AP-R3-07 | PILOT-001 / SITE-001 execution **not** implied | Acknowledged |

---

## Conditions that block live pilot (not R3 mock code)

| ID | Blocker | Owner |
|----|---------|-------|
| BL-R3-01 | PILOT-001 Execution Authorization | Pilot governance |
| BL-R3-02 | Operator `credential_ref` and output root bindings | Operator |
| BL-R3-03 | Live SFTP connected acquire | R1 connector + pilot charter |
| BL-R3-04 | R5 Validate pass on candidate | R5 — post R3 assembly |

R3 mock-path implementation may proceed after AP-R3-01–AP-R3-07 without BL-R3-01–BL-R3-03 resolved.

---

## Gate transition

| Gate | Before Implementation Charter | After Implementation Charter |
|------|------------------------------|------------------------------|
| R3 Charter | **COMPLETE** | **COMPLETE** |
| R3 Implementation Charter | **NEXT** | **COMPLETE** |
| R3 Status | AUTHORIZED FOR IMPLEMENTATION CHARTER | **AUTHORIZED FOR ENGINEERING** |
| R3 Implementation (code) | **NOT AUTHORIZED** | **NOT AUTHORIZED** until human sign-off AP-R3-08 |
| R3.1 Snapshot Package Model | **NOT STARTED** | **NEXT** |

---

## Sign-off record

| Role | Record |
|------|--------|
| Charter executor | Agent architecture charter 2026-06-05 |
| Human implementation approval | **PENDING** (AP-R3-08) |

---

## Evidence

| # | Evidence | Location |
|---|----------|----------|
| D-R3I-01 | R3 program charter | [R3-CHARTER-v1.md](R3-CHARTER-v1.md) |
| D-R3I-02 | R3 charter gate — APPROVED WITH NOTES | [R3-DECISION-v1.md](R3-DECISION-v1.md) |
| D-R3I-03 | Evidence → Snapshot handoff | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) |
| D-R3I-04 | R2 closure — READY FOR R3 WITH NOTES | [R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md) |
| D-R3I-05 | OpenCart snapshot spec | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| D-R3I-06 | Quality level mapping | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| D-R3I-07 | Storage roles | [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |
| D-R3I-08 | Backlog R3 definition | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) |
| D-R3I-09 | R3 Implementation Charter artifact | [R3-IMPLEMENTATION-CHARTER-v1.md](R3-IMPLEMENTATION-CHARTER-v1.md) |
