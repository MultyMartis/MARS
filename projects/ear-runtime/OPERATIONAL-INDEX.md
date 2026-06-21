# EAR Runtime — Operational Index

**Status:** **documented** navigation only — **not** a service registry or automated router.  
**Lane:** B — External Systems / Acquisition Engineering  
**Domain root:** [README.md](README.md)  
**Architecture source:** [shared/external-access-runtime/](../../shared/external-access-runtime/)

---

## Programs (authoritative split)

| Program | Status | Location |
|---------|--------|----------|
| **EAR Architecture Program** | **COMPLETE** (frozen 2026-06-01) | [shared/external-access-runtime/](../../shared/external-access-runtime/) |
| **EAR Runtime Program** | **STARTED** — baseline frozen 2026-06-07 | **This project** — [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) |

**Placement decision:** [DECISION-EAR-RUNTIME-PLACEMENT-v1.md](DECISION-EAR-RUNTIME-PLACEMENT-v1.md)  
**Foundation freeze:** [freeze/FOUNDATION-START-v1/](freeze/FOUNDATION-START-v1/)  
**Stable baseline (pre-live):** [EAR-STABLE-BASELINE-2026-06.md](EAR-STABLE-BASELINE-2026-06.md) — 2026-06-07

---

## Current focus

| Field | Value |
|-------|-------|
| **Engineering Charter** | **DONE** — [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) |
| **Program** | **STARTED** |
| **Implementation** | **FOUNDATION + CONNECTOR SKELETON + LISTING + MANIFEST + EVIDENCE + SNAPSHOT MODEL** — R1.1–R1.7 done; connector **SKELETON ONLY**; listing/manifest/evidence/snapshot **MOCK ONLY** |
| **R1 Implementation Readiness Review** | **DONE** — [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md) (**CONDITIONAL GO**) |
| **R1 Implementation Charter** | **DONE** — [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md) |
| **R1.1 Runtime Skeleton** | **DONE** — [R1.1-FOUNDATION-STATE-v1.md](R1.1-FOUNDATION-STATE-v1.md) |
| **R1.2 Config Input Model** | **DONE** — [R1.2-CONFIG-INPUT-MODEL-v1.md](R1.2-CONFIG-INPUT-MODEL-v1.md) |
| **R1.3 Connection Layer Skeleton** | **DONE** — [R1.3-CONNECTION-LAYER-SKELETON-v1.md](R1.3-CONNECTION-LAYER-SKELETON-v1.md) |
| **R1.4 Remote Listing Model** | **DONE** — [R1.4-REMOTE-LISTING-MODEL-v1.md](R1.4-REMOTE-LISTING-MODEL-v1.md) |
| **R1.5 Manifest Builder Skeleton** | **DONE** — [R1.5-MANIFEST-BUILDER-SKELETON-v1.md](R1.5-MANIFEST-BUILDER-SKELETON-v1.md) |
| **R1.6 Evidence Package Model** | **DONE** — [R1.6-EVIDENCE-PACKAGE-MODEL-v1.md](R1.6-EVIDENCE-PACKAGE-MODEL-v1.md) |
| **R1.7 Snapshot Package Model** | **DONE** — [R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md](R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md) |
| **R1.8A Persistence Design Review** | **DONE** — [R1.8A-PERSISTENCE-DESIGN-REVIEW-v1.md](R1.8A-PERSISTENCE-DESIGN-REVIEW-v1.md) (**CONDITIONAL GO**) |
| **R1.8B Snapshot Storage Contract** | **DONE** — [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) |
| **R1.8C Persistence Layout Charter** | **DONE** — [R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md](R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md) |
| **R1.8D Persistence Kickoff Charter** | **DONE** — [R1.8D-PERSISTENCE-KICKOFF-CHARTER-v1.md](R1.8D-PERSISTENCE-KICKOFF-CHARTER-v1.md) |
| **R1.8 Persistence Model** | **DONE** — [R1.8-PERSISTENCE-MODEL-v1.md](R1.8-PERSISTENCE-MODEL-v1.md) (mock Store only) |
| **R1.8E Persistence Verification Review** | **DONE** — [R1.8E-PERSISTENCE-VERIFICATION-REVIEW-v1.md](R1.8E-PERSISTENCE-VERIFICATION-REVIEW-v1.md) (**PASS WITH NOTES**) |
| **R1.9 Store Hardening** | **DONE** — [R1.9-HARDENING-REVIEW-v1.md](R1.9-HARDENING-REVIEW-v1.md) (**PASS WITH NOTES**) |
| **Persistence** | **IMPLEMENTED (mock Store)** — **VERIFIED** |
| **Store** | **VERIFIED** |
| **Publish** | **SKELETON ONLY** — `ear_publish_engine.py`; mock E2E in-memory |
| **R2 Planning Review** | **DONE** — [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) (**APPROVED WITH NOTES**) |
| **R2 Charter** | **DONE** — [R2-CHARTER-v1.md](R2-CHARTER-v1.md) ([R2-DECISION-v1.md](R2-DECISION-v1.md) **APPROVED WITH NOTES**) |
| **R2 Implementation Charter** | **DONE** — [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md) ([R2-IMPLEMENTATION-DECISION-v1.md](R2-IMPLEMENTATION-DECISION-v1.md) **APPROVED WITH NOTES**) |
| **R2.1 Evidence Package Model** | **DONE** — [R2.1-EVIDENCE-PACKAGE-MODEL-v1.md](R2.1-EVIDENCE-PACKAGE-MODEL-v1.md) |
| **R2.2 Evidence Identity Review** | **DONE** — [R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md](R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md) ([R2.2-EVIDENCE-IDENTITY-DECISION-v1.md](R2.2-EVIDENCE-IDENTITY-DECISION-v1.md) **PASS WITH NOTES**) |
| **R2.3 Evidence Artifact Index** | **DONE** — [R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md](R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md) ([R2.3-EVIDENCE-ARTIFACT-INDEX-DECISION-v1.md](R2.3-EVIDENCE-ARTIFACT-INDEX-DECISION-v1.md) **PASS WITH NOTES**) |
| **R2.4 Evidence Validation Boundary** | **DONE** — [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) ([R2.4-EVIDENCE-VALIDATION-DECISION-v1.md](R2.4-EVIDENCE-VALIDATION-DECISION-v1.md) **PASS WITH NOTES**) |
| **R2.5 Evidence Quarantine Layout** | **DONE** — [R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md](R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md) ([R2.5-EVIDENCE-QUARANTINE-DECISION-v1.md](R2.5-EVIDENCE-QUARANTINE-DECISION-v1.md) **PASS WITH NOTES**) |
| **R2.6 Evidence → Snapshot Handoff** | **DONE** — [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) ([R2.6-EVIDENCE-SNAPSHOT-HANDOFF-DECISION-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-DECISION-v1.md) **PASS WITH NOTES**) |
| **R2 Architecture Consolidation Review** | **DONE** — [R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md](R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md) ([R2-ARCHITECTURE-CONSOLIDATION-DECISION-v1.md](R2-ARCHITECTURE-CONSOLIDATION-DECISION-v1.md) **PASS WITH NOTES**) |
| **R2.7 Evidence Package Generator** | **DONE** — [R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md](R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md) ([R2.7-EVIDENCE-PACKAGE-GENERATOR-DECISION-v1.md](R2.7-EVIDENCE-PACKAGE-GENERATOR-DECISION-v1.md) **PASS WITH NOTES**) |
| **R2 Readiness Review** | **DONE** — [R2-READINESS-REVIEW-v1.md](R2-READINESS-REVIEW-v1.md) ([R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md) **READY FOR R3 WITH NOTES**) |
| **R2 Status** | **COMPLETE WITH NOTES** |
| **R3 Charter** | **DONE** — [R3-CHARTER-v1.md](R3-CHARTER-v1.md) ([R3-DECISION-v1.md](R3-DECISION-v1.md) **APPROVED WITH NOTES**) |
| **R3 Implementation Charter** | **DONE** — [R3-IMPLEMENTATION-CHARTER-v1.md](R3-IMPLEMENTATION-CHARTER-v1.md) ([R3-IMPLEMENTATION-DECISION-v1.md](R3-IMPLEMENTATION-DECISION-v1.md) **APPROVED WITH NOTES**) |
| **R3.1 Snapshot Package Model** | **DONE** — [R3.1-SNAPSHOT-PACKAGE-MODEL-v1.md](R3.1-SNAPSHOT-PACKAGE-MODEL-v1.md) ([R3.1-SNAPSHOT-PACKAGE-MODEL-DECISION-v1.md](R3.1-SNAPSHOT-PACKAGE-MODEL-DECISION-v1.md) **PASS WITH NOTES**) |
| **R3.2 Snapshot Identity Layer** | **DONE** — [R3.2-SNAPSHOT-IDENTITY-LAYER-v1.md](R3.2-SNAPSHOT-IDENTITY-LAYER-v1.md) ([R3.2-SNAPSHOT-IDENTITY-DECISION-v1.md](R3.2-SNAPSHOT-IDENTITY-DECISION-v1.md) **PASS WITH NOTES**) |
| **R3.3 Section Assembly Rules** | **DONE** — [R3.3-SECTION-ASSEMBLY-RULES-v1.md](R3.3-SECTION-ASSEMBLY-RULES-v1.md) ([R3.3-SECTION-ASSEMBLY-DECISION-v1.md](R3.3-SECTION-ASSEMBLY-DECISION-v1.md) **PASS WITH NOTES**) |
| **R3.4 Safe Unknown Propagation** | **DONE** — [R3.4-SAFE-UNKNOWN-PROPAGATION-v1.md](R3.4-SAFE-UNKNOWN-PROPAGATION-v1.md) ([R3.4-SAFE-UNKNOWN-DECISION-v1.md](R3.4-SAFE-UNKNOWN-DECISION-v1.md) **PASS WITH NOTES**) |
| **R3.5 Candidate Snapshot Generator** | **DONE** — [R3.5-CANDIDATE-SNAPSHOT-GENERATOR-v1.md](R3.5-CANDIDATE-SNAPSHOT-GENERATOR-v1.md) ([R3.5-CANDIDATE-SNAPSHOT-GENERATOR-DECISION-v1.md](R3.5-CANDIDATE-SNAPSHOT-GENERATOR-DECISION-v1.md) **PASS WITH NOTES**) |
| **R3.6 Validation Boundary Review** | **DONE** — [R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md](R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md) ([R3.6-VALIDATION-BOUNDARY-DECISION-v1.md](R3.6-VALIDATION-BOUNDARY-DECISION-v1.md) **PASS WITH NOTES**) |
| **R3 Readiness Review** | **DONE** — [R3-READINESS-REVIEW-v1.md](R3-READINESS-REVIEW-v1.md) ([R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) **READY FOR R5 WITH NOTES**) |
| **R3 Status** | **COMPLETE WITH NOTES** |
| **R5 Charter** | **DONE** — [R5-CHARTER-v1.md](R5-CHARTER-v1.md) ([R5-DECISION-v1.md](R5-DECISION-v1.md) **APPROVED WITH NOTES**) |
| **R5 Implementation Charter** | **DONE** — [R5-IMPLEMENTATION-CHARTER-v1.md](R5-IMPLEMENTATION-CHARTER-v1.md) ([R5-IMPLEMENTATION-DECISION-v1.md](R5-IMPLEMENTATION-DECISION-v1.md) **APPROVED WITH NOTES**) |
| **R5.1 Validation Result Model** | **DONE** — [R5.1-VALIDATION-RESULT-MODEL-v1.md](R5.1-VALIDATION-RESULT-MODEL-v1.md) ([R5.1-VALIDATION-RESULT-DECISION-v1.md](R5.1-VALIDATION-RESULT-DECISION-v1.md) **PASS WITH NOTES**) |
| **R5.2 Validation Category Model** | **DONE** — [R5.2-VALIDATION-CATEGORY-MODEL-v1.md](R5.2-VALIDATION-CATEGORY-MODEL-v1.md) ([R5.2-VALIDATION-CATEGORY-DECISION-v1.md](R5.2-VALIDATION-CATEGORY-DECISION-v1.md) **PASS WITH NOTES**) |
| **R5.3 Quality Possession Model** | **DONE** — [R5.3-QUALITY-POSSESSION-MODEL-v1.md](R5.3-QUALITY-POSSESSION-MODEL-v1.md) ([R5.3-QUALITY-POSSESSION-DECISION-v1.md](R5.3-QUALITY-POSSESSION-DECISION-v1.md) **PASS WITH NOTES**) |
| **R5.4 Redaction Review Model** | **DONE** — [R5.4-REDACTION-REVIEW-MODEL-v1.md](R5.4-REDACTION-REVIEW-MODEL-v1.md) ([R5.4-REDACTION-REVIEW-DECISION-v1.md](R5.4-REDACTION-REVIEW-DECISION-v1.md) **PASS WITH NOTES**) |
| **R5.5 Validate Report Contract** | **DONE** — [R5.5-VALIDATE-REPORT-CONTRACT-v1.md](R5.5-VALIDATE-REPORT-CONTRACT-v1.md) ([R5.5-VALIDATE-REPORT-DECISION-v1.md](R5.5-VALIDATE-REPORT-DECISION-v1.md) **PASS WITH NOTES**) |
| **R5.6 Publish Eligibility Contract** | **DONE** — [R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md](R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md) ([R5.6-PUBLISH-ELIGIBILITY-DECISION-v1.md](R5.6-PUBLISH-ELIGIBILITY-DECISION-v1.md) **PASS WITH NOTES**) |
| **R5.7 Validate Engine** | **DONE** — [R5.7-VALIDATE-ENGINE-v1.md](R5.7-VALIDATE-ENGINE-v1.md) ([R5.7-VALIDATE-ENGINE-DECISION-v1.md](R5.7-VALIDATE-ENGINE-DECISION-v1.md) **PASS WITH NOTES**) |
| **R5.8 Validation Boundary Review** | **DONE** — [R5.8-VALIDATION-BOUNDARY-REVIEW-v1.md](R5.8-VALIDATION-BOUNDARY-REVIEW-v1.md) ([R5.8-VALIDATION-BOUNDARY-DECISION-v1.md](R5.8-VALIDATION-BOUNDARY-DECISION-v1.md) **PASS WITH NOTES**) |
| **R5 Readiness Review** | **DONE** — [R5-READINESS-REVIEW-v1.md](R5-READINESS-REVIEW-v1.md) ([R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) **READY FOR R5 IMPLEMENTATION WITH NOTES**) |
| **R5 Status** | **COMPLETE WITH NOTES** |
| **R4 Charter** | **DONE** — [R4-CHARTER-v1.md](R4-CHARTER-v1.md) ([R4-DECISION-v1.md](R4-DECISION-v1.md) **APPROVED WITH NOTES**) |
| **R4 Implementation Charter** | **DONE** — [R4-IMPLEMENTATION-CHARTER-v1.md](R4-IMPLEMENTATION-CHARTER-v1.md) ([R4-IMPLEMENTATION-DECISION-v1.md](R4-IMPLEMENTATION-DECISION-v1.md) **APPROVED WITH NOTES**) |
| **R4.1 Published Snapshot Model** | **DONE** — [R4.1-PUBLISHED-SNAPSHOT-MODEL-v1.md](R4.1-PUBLISHED-SNAPSHOT-MODEL-v1.md) ([R4.1-PUBLISHED-SNAPSHOT-MODEL-DECISION-v1.md](R4.1-PUBLISHED-SNAPSHOT-MODEL-DECISION-v1.md) **PASS WITH NOTES**) |
| **R4.2 Publish State Model** | **DONE** — [R4.2-PUBLISH-STATE-MODEL-v1.md](R4.2-PUBLISH-STATE-MODEL-v1.md) ([R4.2-PUBLISH-STATE-MODEL-DECISION-v1.md](R4.2-PUBLISH-STATE-MODEL-DECISION-v1.md) **PASS WITH NOTES**) |
| **R4.3 Consumer Visibility Model** | **DONE** — [R4.3-CONSUMER-VISIBILITY-MODEL-v1.md](R4.3-CONSUMER-VISIBILITY-MODEL-v1.md) ([R4.3-CONSUMER-VISIBILITY-MODEL-DECISION-v1.md](R4.3-CONSUMER-VISIBILITY-MODEL-DECISION-v1.md) **PASS WITH NOTES**) |
| **R4.4 Publish Metadata Model** | **DONE** — [R4.4-PUBLISH-METADATA-MODEL-v1.md](R4.4-PUBLISH-METADATA-MODEL-v1.md) ([R4.4-PUBLISH-METADATA-MODEL-DECISION-v1.md](R4.4-PUBLISH-METADATA-MODEL-DECISION-v1.md) **PASS WITH NOTES**) |
| **R4.5 Publish Result Contract** | **DONE** — [R4.5-PUBLISH-RESULT-CONTRACT-v1.md](R4.5-PUBLISH-RESULT-CONTRACT-v1.md) ([R4.5-PUBLISH-RESULT-DECISION-v1.md](R4.5-PUBLISH-RESULT-DECISION-v1.md) **PASS WITH NOTES**) |
| **R4.6 Publish Flow Contract** | **DONE** — [R4.6-PUBLISH-FLOW-CONTRACT-v1.md](R4.6-PUBLISH-FLOW-CONTRACT-v1.md) ([R4.6-PUBLISH-FLOW-DECISION-v1.md](R4.6-PUBLISH-FLOW-DECISION-v1.md) **PASS WITH NOTES**) |
| **R4.7 Publish Engine Architecture** | **DONE** — [R4.7-PUBLISH-ENGINE-ARCHITECTURE-v1.md](R4.7-PUBLISH-ENGINE-ARCHITECTURE-v1.md) ([R4.7-PUBLISH-ENGINE-DECISION-v1.md](R4.7-PUBLISH-ENGINE-DECISION-v1.md) **PASS WITH NOTES**) |
| **R4.8 Publish Boundary Review** | **DONE** — [R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md](R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md) ([R4.8-PUBLISH-BOUNDARY-DECISION-v1.md](R4.8-PUBLISH-BOUNDARY-DECISION-v1.md) **PASS WITH NOTES**) |
| **R4 Readiness Review** | **DONE** — [R4-READINESS-REVIEW-v1.md](R4-READINESS-REVIEW-v1.md) ([R4-READINESS-DECISION-v1.md](R4-READINESS-DECISION-v1.md) **READY FOR R4 IMPLEMENTATION WITH NOTES**) |
| **R4 Status** | **COMPLETE WITH NOTES** |
| **Mock E2E Flow** | **IMPLEMENTED** — [EAR-MOCK-E2E-FLOW-v1.md](EAR-MOCK-E2E-FLOW-v1.md) |
| **Mock E2E Readiness Review** | **DONE** — [EAR-MOCK-E2E-READINESS-REVIEW-v1.md](EAR-MOCK-E2E-READINESS-REVIEW-v1.md) ([EAR-MOCK-E2E-READINESS-DECISION-v1.md](EAR-MOCK-E2E-READINESS-DECISION-v1.md) **READY FOR SITE-001 DRY-RUN PLANNING WITH NOTES**) |
| **EAR Stable Baseline 2026-06** | **FROZEN** — [EAR-STABLE-BASELINE-2026-06.md](EAR-STABLE-BASELINE-2026-06.md) — pre-live foundation freeze |
| **SITE-001 Dry Run Plan** | **DONE** — [SITE-001-DRY-RUN-PLAN-v1.md](SITE-001-DRY-RUN-PLAN-v1.md) — operator procedure; planning complete |
| **Execution Authorization Review** | **DONE** — [EXECUTION-AUTHORIZATION-REVIEW-v1.md](EXECUTION-AUTHORIZATION-REVIEW-v1.md) ([EXECUTION-AUTHORIZATION-DECISION-v1.md](EXECUTION-AUTHORIZATION-DECISION-v1.md) **AUTHORIZED WITH NOTES**) |
| **SITE-001 dry-run execution (HG-0)** | **AUTHORIZED WITH NOTES** — mock/in-memory path only; human sign-off pending |
| **SITE-001 dry-run executed** | **YES** — 1 run — [SITE-001-DRY-RUN-EXECUTION-v1.md](SITE-001-DRY-RUN-EXECUTION-v1.md) ([SITE-001-DRY-RUN-DECISION-v1.md](SITE-001-DRY-RUN-DECISION-v1.md) **PASS WITH NOTES**) |
| **Current focus** | HG-4 Execution Authorization Review input — dry-run record complete |
| **Next** | HG-4 live pilot input review; optional `--mock-e2e` CLI; real R5 assessors + R4 Store adapter (human gates); PILOT-001 Execution Authorization (explicit human YES required) |

---

## Canonical reading order (Runtime Program)

| Step | Document | Why |
|------|----------|-----|
| 1 | [README.md](README.md) | Project scope and ownership |
| 2 | [DECISION-EAR-RUNTIME-PLACEMENT-v1.md](DECISION-EAR-RUNTIME-PLACEMENT-v1.md) | Why runtime lives under `projects/` |
| 3 | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) | **Engineering program start** — mission, stack, backlog planning |
| 4 | [EAR-RUNTIME-CHARTER-v1.md](EAR-RUNTIME-CHARTER-v1.md) | Foundation mission and consumer relationships |
| 5 | [ENGINEERING-BOUNDARIES-v1.md](ENGINEERING-BOUNDARIES-v1.md) / [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) | Ownership and principles |
| 6 | [EAR-RUNTIME-SCOPE-v1.md](EAR-RUNTIME-SCOPE-v1.md) / [EAR-RUNTIME-NON-GOALS-v1.md](EAR-RUNTIME-NON-GOALS-v1.md) | In/out and anti-creep |
| 7 | [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) | Proposed `runtime/` layout |
| 8 | [EAR-RUNTIME-ROADMAP-v1.md](EAR-RUNTIME-ROADMAP-v1.md) | R1–R5 phases |
| 9 | [EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md) | Engineering targets (references architecture backlog) |
| 10 | [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) | R1 planning charter |
| 11 | [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md) | R1 implementation readiness (**CONDITIONAL GO**) |
| 12 | [R1-IMPLEMENTATION-DECISIONS-v1.md](R1-IMPLEMENTATION-DECISIONS-v1.md) | Evidence-backed runtime decisions |
| 13 | [R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md](R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md) | Preconditions before R1 code |
| 14 | [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md) | **R1 Implementation Charter** — scope, decisions, boundaries |
| 15 | [R1-AUTHORITATIVE-SEQUENCE-v1.md](R1-AUTHORITATIVE-SEQUENCE-v1.md) | **Authoritative** R1 execution order (PC-07) |
| 16 | [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md) | Legacy task catalog R1.1–R1.10 (reconciled via authoritative sequence) |
| 17 | [R1-TEST-STRATEGY-v1.md](R1-TEST-STRATEGY-v1.md) | Non-production test plan |
| 18 | [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) | Human approval gate |
| 19 | [R1-PHASE-DECISION-v1.md](R1-PHASE-DECISION-v1.md) | R1 readiness phase decision record |
| 20 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Honest status |
| 21 | [STATE-TRANSITION-v1.md](STATE-TRANSITION-v1.md) | Engineering state transition record |
| 22 | [R1-GATE-RECONCILIATION-v1.md](R1-GATE-RECONCILIATION-v1.md) | Gate integrity — R1.1/R1.2 vs decision gate |
| 23 | [R1-CONTRACT-MAPPING-v1.md](R1-CONTRACT-MAPPING-v1.md) | Config ↔ connector contract field mapping |
| 24 | [R1.3-READINESS-DECISION-v1.md](R1.3-READINESS-DECISION-v1.md) | R1.3 readiness (**GO**) |
| 25 | [R1.3-CONNECTION-LAYER-SKELETON-v1.md](R1.3-CONNECTION-LAYER-SKELETON-v1.md) | R1.3 connector skeleton (**DONE**) |
| 26 | [R1.4-REMOTE-LISTING-MODEL-v1.md](R1.4-REMOTE-LISTING-MODEL-v1.md) | R1.4 listing model (**DONE**, mock only) |
| 27 | [R1.5-MANIFEST-BUILDER-SKELETON-v1.md](R1.5-MANIFEST-BUILDER-SKELETON-v1.md) | R1.5 manifest builder (**DONE**, mock only) |
| 28 | [R1.6-EVIDENCE-PACKAGE-MODEL-v1.md](R1.6-EVIDENCE-PACKAGE-MODEL-v1.md) | R1.6 evidence package model (**DONE**, mock only) |
| 29 | [R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md](R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md) | R1.7 snapshot package model (**DONE**, mock only) |
| 30 | [R1.8A-PERSISTENCE-DESIGN-REVIEW-v1.md](R1.8A-PERSISTENCE-DESIGN-REVIEW-v1.md) | R1.8A persistence design review (**DONE**, no implementation) |
| 31 | [R1.8A-PERSISTENCE-READINESS-DECISION-v1.md](R1.8A-PERSISTENCE-READINESS-DECISION-v1.md) | R1.8A readiness (**CONDITIONAL GO** → carried **GO**) |
| 32 | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) | R1.8B storage contract (**DONE**, no implementation) |
| 33 | [R1.8B-STORAGE-CONTRACT-DECISION-v1.md](R1.8B-STORAGE-CONTRACT-DECISION-v1.md) | R1.8B readiness (**CONDITIONAL GO** → carried **GO**) |
| 34 | [R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md](R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md) | R1.8C layout charter (**DONE**, no implementation) |
| 35 | [R1.8C-PERSISTENCE-LAYOUT-DECISION-v1.md](R1.8C-PERSISTENCE-LAYOUT-DECISION-v1.md) | R1.8C readiness (**GO** carried) |
| 36 | [R1.8D-PERSISTENCE-KICKOFF-CHARTER-v1.md](R1.8D-PERSISTENCE-KICKOFF-CHARTER-v1.md) | R1.8D kickoff charter (**DONE**, no implementation) |
| 37 | [R1.8D-PERSISTENCE-KICKOFF-DECISION-v1.md](R1.8D-PERSISTENCE-KICKOFF-DECISION-v1.md) | R1.8 entry (**GO**) |
| 38 | [R1.8-PERSISTENCE-MODEL-v1.md](R1.8-PERSISTENCE-MODEL-v1.md) | R1.8 Persistence Model (**DONE**, mock Store) |
| 39 | [R1.8E-PERSISTENCE-VERIFICATION-REVIEW-v1.md](R1.8E-PERSISTENCE-VERIFICATION-REVIEW-v1.md) | R1.8E verification (**DONE**, **PASS WITH NOTES**) |
| 40 | [R1.8E-PERSISTENCE-DECISION-v1.md](R1.8E-PERSISTENCE-DECISION-v1.md) | R1.8E decision — R1.8 **VERIFIED** |
| 41 | [R1.9-HARDENING-CHECKLIST-v1.md](R1.9-HARDENING-CHECKLIST-v1.md) | R1.9 hardening checklist (**DONE**) |
| 42 | [R1.9-HARDENING-REVIEW-v1.md](R1.9-HARDENING-REVIEW-v1.md) | R1.9 Store hardening review (**DONE**) |
| 43 | [R1.9-HARDENING-DECISION-v1.md](R1.9-HARDENING-DECISION-v1.md) | R1.9 decision — Store **VERIFIED** |
| 44 | [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) | R2 planning review (**DONE**, no implementation) |
| 45 | [R2-PLANNING-DECISION-v1.md](R2-PLANNING-DECISION-v1.md) | R2 kickoff decision — **APPROVED WITH NOTES** |
| 46 | [R2-CHARTER-v1.md](R2-CHARTER-v1.md) | R2 Evidence Package Layer charter (**DONE**, no implementation) |
| 47 | [R2-DECISION-v1.md](R2-DECISION-v1.md) | R2 charter decision — **APPROVED WITH NOTES** |
| 48 | [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md) | R2 Implementation Charter (**DONE**, no implementation) |
| 49 | [R2-IMPLEMENTATION-DECISION-v1.md](R2-IMPLEMENTATION-DECISION-v1.md) | R2 engineering decision — **APPROVED WITH NOTES** |
| 50 | [R2.1-EVIDENCE-PACKAGE-MODEL-v1.md](R2.1-EVIDENCE-PACKAGE-MODEL-v1.md) | R2.1 contract evidence package model (**DONE**, dataclasses only) |
| 51 | [R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md](R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md) | R2.2 evidence identity review (**DONE**, no implementation) |
| 52 | [R2.2-EVIDENCE-IDENTITY-DECISION-v1.md](R2.2-EVIDENCE-IDENTITY-DECISION-v1.md) | R2.2 identity gate — **PASS WITH NOTES** |
| 53 | [R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md](R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md) | R2.3 artifact index review (**DONE**, no generator/validator) |
| 54 | [R2.3-EVIDENCE-ARTIFACT-INDEX-DECISION-v1.md](R2.3-EVIDENCE-ARTIFACT-INDEX-DECISION-v1.md) | R2.3 artifact index gate — **PASS WITH NOTES** |
| 55 | [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) | R2.4 validation boundary review (**DONE**, no validator) |
| 56 | [R2.4-EVIDENCE-VALIDATION-DECISION-v1.md](R2.4-EVIDENCE-VALIDATION-DECISION-v1.md) | R2.4 validation boundary gate — **PASS WITH NOTES** |
| 57 | [R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md](R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md) | R2.5 quarantine layout review (**DONE**, no persist) |
| 58 | [R2.5-EVIDENCE-QUARANTINE-DECISION-v1.md](R2.5-EVIDENCE-QUARANTINE-DECISION-v1.md) | R2.5 quarantine gate — **PASS WITH NOTES** |
| 59 | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) | R2.6 handoff review (**DONE**, no generator/snapshot builder) |
| 60 | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-DECISION-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-DECISION-v1.md) | R2.6 handoff gate — **PASS WITH NOTES** |
| 61 | [R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md](R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md) | R2 architecture consolidation review (**DONE**, no implementation) |
| 62 | [R2-ARCHITECTURE-CONSOLIDATION-DECISION-v1.md](R2-ARCHITECTURE-CONSOLIDATION-DECISION-v1.md) | R2 consolidation gate — **PASS WITH NOTES**; R2 ready for R2.7 |
| 63 | [R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md](R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md) | R2.7 contract generator (**DONE**, mock-first, in-memory) |
| 64 | [R2.7-EVIDENCE-PACKAGE-GENERATOR-DECISION-v1.md](R2.7-EVIDENCE-PACKAGE-GENERATOR-DECISION-v1.md) | R2.7 gate — **PASS WITH NOTES** |
| 65 | [R2-READINESS-REVIEW-v1.md](R2-READINESS-REVIEW-v1.md) | R2 readiness review (**DONE**, no implementation) |
| 66 | [R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md) | R2 closure gate — **READY FOR R3 WITH NOTES** |
| 67 | [R3-CHARTER-v1.md](R3-CHARTER-v1.md) | R3 Snapshot Assembly Layer charter (**DONE**, no implementation) |
| 68 | [R3-DECISION-v1.md](R3-DECISION-v1.md) | R3 charter decision — **APPROVED WITH NOTES** |
| 69 | [R3-IMPLEMENTATION-CHARTER-v1.md](R3-IMPLEMENTATION-CHARTER-v1.md) | R3 Implementation Charter (**DONE**, no implementation) |
| 70 | [R3-IMPLEMENTATION-DECISION-v1.md](R3-IMPLEMENTATION-DECISION-v1.md) | R3 engineering decision — **APPROVED WITH NOTES** |
| 71 | [R3.1-SNAPSHOT-PACKAGE-MODEL-v1.md](R3.1-SNAPSHOT-PACKAGE-MODEL-v1.md) | R3.1 OpenCart snapshot package model (**DONE**, dataclasses only) |
| 72 | [R3.1-SNAPSHOT-PACKAGE-MODEL-DECISION-v1.md](R3.1-SNAPSHOT-PACKAGE-MODEL-DECISION-v1.md) | R3.1 gate — **PASS WITH NOTES** |
| 73 | [R3.2-SNAPSHOT-IDENTITY-LAYER-v1.md](R3.2-SNAPSHOT-IDENTITY-LAYER-v1.md) | R3.2 snapshot identity contract (**DONE**, no code) |
| 74 | [R3.2-SNAPSHOT-IDENTITY-DECISION-v1.md](R3.2-SNAPSHOT-IDENTITY-DECISION-v1.md) | R3.2 gate — **PASS WITH NOTES** |
| 75 | [R3.3-SECTION-ASSEMBLY-RULES-v1.md](R3.3-SECTION-ASSEMBLY-RULES-v1.md) | R3.3 section assembly mapping contract (**DONE**, no code) |
| 76 | [R3.3-SECTION-ASSEMBLY-DECISION-v1.md](R3.3-SECTION-ASSEMBLY-DECISION-v1.md) | R3.3 gate — **PASS WITH NOTES** |
| 77 | [R3.4-SAFE-UNKNOWN-PROPAGATION-v1.md](R3.4-SAFE-UNKNOWN-PROPAGATION-v1.md) | R3.4 safe-unknown propagation contract (**DONE**, no code) |
| 78 | [R3.4-SAFE-UNKNOWN-DECISION-v1.md](R3.4-SAFE-UNKNOWN-DECISION-v1.md) | R3.4 gate — **PASS WITH NOTES** |
| 79 | [R3.5-CANDIDATE-SNAPSHOT-GENERATOR-v1.md](R3.5-CANDIDATE-SNAPSHOT-GENERATOR-v1.md) | R3.5 candidate generator (**DONE**, mock-first, in-memory) |
| 80 | [R3.5-CANDIDATE-SNAPSHOT-GENERATOR-DECISION-v1.md](R3.5-CANDIDATE-SNAPSHOT-GENERATOR-DECISION-v1.md) | R3.5 gate — **PASS WITH NOTES** |
| 81 | [R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md](R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md) | R3.6 validation boundary review (**DONE**, no R5/Publish) |
| 82 | [R3.6-VALIDATION-BOUNDARY-DECISION-v1.md](R3.6-VALIDATION-BOUNDARY-DECISION-v1.md) | R3.6 gate — **PASS WITH NOTES** |
| 83 | [R3-READINESS-REVIEW-v1.md](R3-READINESS-REVIEW-v1.md) | R3 readiness review (**DONE**, no R5/Publish) |
| 84 | [R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) | R3 closure gate — **READY FOR R5 WITH NOTES** |
| 85 | [R5-CHARTER-v1.md](R5-CHARTER-v1.md) | R5 EAR Validate Layer charter (**DONE**, no implementation) |
| 86 | [R5-DECISION-v1.md](R5-DECISION-v1.md) | R5 charter decision — **APPROVED WITH NOTES** |
| 87 | [R5-IMPLEMENTATION-CHARTER-v1.md](R5-IMPLEMENTATION-CHARTER-v1.md) | R5 Implementation Charter (**DONE**, no implementation) |
| 88 | [R5-IMPLEMENTATION-DECISION-v1.md](R5-IMPLEMENTATION-DECISION-v1.md) | R5 engineering decision — **APPROVED WITH NOTES** |
| 89 | [R5.1-VALIDATION-RESULT-MODEL-v1.md](R5.1-VALIDATION-RESULT-MODEL-v1.md) | R5.1 Validation Result model (**DONE**, dataclasses only) |
| 90 | [R5.1-VALIDATION-RESULT-DECISION-v1.md](R5.1-VALIDATION-RESULT-DECISION-v1.md) | R5.1 gate — **PASS WITH NOTES** |
| 91 | [R5.2-VALIDATION-CATEGORY-MODEL-v1.md](R5.2-VALIDATION-CATEGORY-MODEL-v1.md) | R5.2 Validation Category model (**DONE**, dataclasses only) |
| 92 | [R5.2-VALIDATION-CATEGORY-DECISION-v1.md](R5.2-VALIDATION-CATEGORY-DECISION-v1.md) | R5.2 gate — **PASS WITH NOTES** |
| 93 | [R5.3-QUALITY-POSSESSION-MODEL-v1.md](R5.3-QUALITY-POSSESSION-MODEL-v1.md) | R5.3 Quality Possession model (**DONE**, dataclasses only) |
| 94 | [R5.3-QUALITY-POSSESSION-DECISION-v1.md](R5.3-QUALITY-POSSESSION-DECISION-v1.md) | R5.3 gate — **PASS WITH NOTES** |
| 95 | [R5.4-REDACTION-REVIEW-MODEL-v1.md](R5.4-REDACTION-REVIEW-MODEL-v1.md) | R5.4 Redaction Review model (**DONE**, dataclasses only) |
| 96 | [R5.4-REDACTION-REVIEW-DECISION-v1.md](R5.4-REDACTION-REVIEW-DECISION-v1.md) | R5.4 gate — **PASS WITH NOTES** |
| 97 | [R5.5-VALIDATE-REPORT-CONTRACT-v1.md](R5.5-VALIDATE-REPORT-CONTRACT-v1.md) | R5.5 Validate Report contract (**DONE**, no implementation) |
| 98 | [R5.5-VALIDATE-REPORT-DECISION-v1.md](R5.5-VALIDATE-REPORT-DECISION-v1.md) | R5.5 gate — **PASS WITH NOTES** |
| 99 | [R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md](R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md) | R5.6 Publish Eligibility contract (**DONE**, no implementation) |
| 100 | [R5.6-PUBLISH-ELIGIBILITY-DECISION-v1.md](R5.6-PUBLISH-ELIGIBILITY-DECISION-v1.md) | R5.6 gate — **PASS WITH NOTES** |
| 101 | [R5.7-VALIDATE-ENGINE-v1.md](R5.7-VALIDATE-ENGINE-v1.md) | R5.7 Validate Engine architecture (**DONE**, no implementation) |
| 102 | [R5.7-VALIDATE-ENGINE-DECISION-v1.md](R5.7-VALIDATE-ENGINE-DECISION-v1.md) | R5.7 gate — **PASS WITH NOTES** |
| 103 | [R5.8-VALIDATION-BOUNDARY-REVIEW-v1.md](R5.8-VALIDATION-BOUNDARY-REVIEW-v1.md) | R5.8 validation boundary review (**DONE**, no implementation) |
| 104 | [R5.8-VALIDATION-BOUNDARY-DECISION-v1.md](R5.8-VALIDATION-BOUNDARY-DECISION-v1.md) | R5.8 gate — **PASS WITH NOTES** |
| 105 | [R5-READINESS-REVIEW-v1.md](R5-READINESS-REVIEW-v1.md) | R5 readiness review (**DONE**, no engine code) |
| 106 | [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) | R5 closure gate — **READY FOR R5 IMPLEMENTATION WITH NOTES** |
| 107 | [R4-CHARTER-v1.md](R4-CHARTER-v1.md) | R4 EAR Publish Layer charter (**DONE**, no implementation) |
| 108 | [R4-DECISION-v1.md](R4-DECISION-v1.md) | R4 charter decision — **APPROVED WITH NOTES** |
| 109 | [R4-IMPLEMENTATION-CHARTER-v1.md](R4-IMPLEMENTATION-CHARTER-v1.md) | R4 Implementation Charter (**DONE**, no implementation) |
| 110 | [R4-IMPLEMENTATION-DECISION-v1.md](R4-IMPLEMENTATION-DECISION-v1.md) | R4 engineering decision — **APPROVED WITH NOTES** |
| 111 | [R4.1-PUBLISHED-SNAPSHOT-MODEL-v1.md](R4.1-PUBLISHED-SNAPSHOT-MODEL-v1.md) | R4.1 Published Snapshot model (**DONE**, dataclasses only) |
| 112 | [R4.1-PUBLISHED-SNAPSHOT-MODEL-DECISION-v1.md](R4.1-PUBLISHED-SNAPSHOT-MODEL-DECISION-v1.md) | R4.1 gate — **PASS WITH NOTES** |
| 113 | [R4.2-PUBLISH-STATE-MODEL-v1.md](R4.2-PUBLISH-STATE-MODEL-v1.md) | R4.2 Publish State model (**DONE**, dataclasses only) |
| 114 | [R4.2-PUBLISH-STATE-MODEL-DECISION-v1.md](R4.2-PUBLISH-STATE-MODEL-DECISION-v1.md) | R4.2 gate — **PASS WITH NOTES** |
| 115 | [R4.3-CONSUMER-VISIBILITY-MODEL-v1.md](R4.3-CONSUMER-VISIBILITY-MODEL-v1.md) | R4.3 Consumer Visibility model (**DONE**, dataclasses only) |
| 116 | [R4.3-CONSUMER-VISIBILITY-MODEL-DECISION-v1.md](R4.3-CONSUMER-VISIBILITY-MODEL-DECISION-v1.md) | R4.3 gate — **PASS WITH NOTES** |
| 117 | [R4.4-PUBLISH-METADATA-MODEL-v1.md](R4.4-PUBLISH-METADATA-MODEL-v1.md) | R4.4 Publish Metadata model (**DONE**, dataclasses only) |
| 118 | [R4.4-PUBLISH-METADATA-MODEL-DECISION-v1.md](R4.4-PUBLISH-METADATA-MODEL-DECISION-v1.md) | R4.4 gate — **PASS WITH NOTES** |
| 119 | [R4.5-PUBLISH-RESULT-CONTRACT-v1.md](R4.5-PUBLISH-RESULT-CONTRACT-v1.md) | R4.5 Publish Result contract (**DONE**, no implementation) |
| 120 | [R4.5-PUBLISH-RESULT-DECISION-v1.md](R4.5-PUBLISH-RESULT-DECISION-v1.md) | R4.5 gate — **PASS WITH NOTES** |
| 121 | [R4.6-PUBLISH-FLOW-CONTRACT-v1.md](R4.6-PUBLISH-FLOW-CONTRACT-v1.md) | R4.6 Publish Flow contract (**DONE**, no implementation) |
| 122 | [R4.6-PUBLISH-FLOW-DECISION-v1.md](R4.6-PUBLISH-FLOW-DECISION-v1.md) | R4.6 gate — **PASS WITH NOTES** |
| 123 | [R4.7-PUBLISH-ENGINE-ARCHITECTURE-v1.md](R4.7-PUBLISH-ENGINE-ARCHITECTURE-v1.md) | R4.7 Publish Engine architecture (**DONE**, no implementation) |
| 124 | [R4.7-PUBLISH-ENGINE-DECISION-v1.md](R4.7-PUBLISH-ENGINE-DECISION-v1.md) | R4.7 gate — **PASS WITH NOTES** |
| 125 | [R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md](R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md) | R4.8 publish boundary review (**DONE**, no implementation) |
| 126 | [R4.8-PUBLISH-BOUNDARY-DECISION-v1.md](R4.8-PUBLISH-BOUNDARY-DECISION-v1.md) | R4.8 gate — **PASS WITH NOTES** |
| 127 | [R4-READINESS-REVIEW-v1.md](R4-READINESS-REVIEW-v1.md) | R4 readiness review (**DONE**, no engine code) |
| 128 | [R4-READINESS-DECISION-v1.md](R4-READINESS-DECISION-v1.md) | R4 closure gate — **READY FOR R4 IMPLEMENTATION WITH NOTES** |
| 129 | [EAR-MOCK-E2E-FLOW-v1.md](EAR-MOCK-E2E-FLOW-v1.md) | First mock E2E orchestration — Config → Publish in-memory (**DONE**) |
| 130 | [EAR-MOCK-E2E-READINESS-REVIEW-v1.md](EAR-MOCK-E2E-READINESS-REVIEW-v1.md) | Mock E2E readiness review (**DONE**, no implementation) |
| 131 | [EAR-MOCK-E2E-READINESS-DECISION-v1.md](EAR-MOCK-E2E-READINESS-DECISION-v1.md) | Mock E2E gate — **READY FOR SITE-001 DRY-RUN PLANNING WITH NOTES** |
| 132 | [EAR-STABLE-BASELINE-2026-06.md](EAR-STABLE-BASELINE-2026-06.md) | **Stable baseline freeze** — pre-live architecture + runtime foundation; Mock E2E PASS ≠ live readiness |
| 133 | [SITE-001-DRY-RUN-PLAN-v1.md](SITE-001-DRY-RUN-PLAN-v1.md) | **SITE-001 Dry Run Plan** — operator procedure; mock/in-memory only |
| 134 | [EXECUTION-AUTHORIZATION-REVIEW-v1.md](EXECUTION-AUTHORIZATION-REVIEW-v1.md) | Execution Authorization Review (**DONE**, no implementation) |
| 135 | [EXECUTION-AUTHORIZATION-DECISION-v1.md](EXECUTION-AUTHORIZATION-DECISION-v1.md) | HG-0 gate — **AUTHORIZED WITH NOTES** for dry-run execution |
| 136 | [SITE-001-DRY-RUN-EXECUTION-v1.md](SITE-001-DRY-RUN-EXECUTION-v1.md) | **SITE-001 Dry Run execution record** — mock/in-memory operator rehearsal (**DONE**) |
| 137 | [SITE-001-DRY-RUN-DECISION-v1.md](SITE-001-DRY-RUN-DECISION-v1.md) | Dry Run gate — **PASS WITH NOTES**; PILOT-001 **NOT AUTHORIZED** |

**Before any implementation:** read architecture freeze [shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/) and [EAR-RUNTIME-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BOUNDARY-v1.md).

**Before SITE-001 dry-run planning or live work:** read [EAR-STABLE-BASELINE-2026-06.md](EAR-STABLE-BASELINE-2026-06.md) for frozen scope, limitations, and authorization boundaries.

---

## Folder map

| Path | Role |
|------|------|
| [runtime/](runtime/) | R1–R5 skeleton + Mock E2E — `cli.py`, `engines/ear_validate_engine.py`, `engines/ear_publish_engine.py`, `engines/ear_mock_e2e_engine.py`, plus R1/R2/R3 modules |
| [docs/](docs/) | Runtime-specific engineering notes (not architecture amendments) |
| [pilots/](pilots/) | Runtime execution pilots and run artefacts (when chartered) |
| [freeze/](freeze/) | Runtime program freeze markers — includes [FOUNDATION-START-v1/](freeze/FOUNDATION-START-v1/); stable baseline at [EAR-STABLE-BASELINE-2026-06.md](EAR-STABLE-BASELINE-2026-06.md) |

---

## Engineering backlog (summary)

Authoritative item definitions: [shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md)  
Runtime project index: [EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md)

| ID | Name | Dependency |
|----|------|------------|
| **R1** | First SFTP Read-Only Connector | — |
| **R2** | Evidence Package Generator | R1 |
| **R3** | Snapshot Builder | R2 |
| **R4** | Snapshot Publisher | R3 |
| **R5** | Validation Helpers | R2 (may parallel R3/R4) |

---

## Audit remediation (2026-06-04)

| Item | Status |
|------|--------|
| OCPilot + EAR Consistency Audit remediation | **DONE** |
| Gate reconciliation | [R1-GATE-RECONCILIATION-v1.md](R1-GATE-RECONCILIATION-v1.md) |
| Contract mapping | [R1-CONTRACT-MAPPING-v1.md](R1-CONTRACT-MAPPING-v1.md) |
| R1.3 readiness | **DONE** — [R1.3-CONNECTION-LAYER-SKELETON-v1.md](R1.3-CONNECTION-LAYER-SKELETON-v1.md) |
| R1.4 Remote Listing Model | **DONE** — [R1.4-REMOTE-LISTING-MODEL-v1.md](R1.4-REMOTE-LISTING-MODEL-v1.md) |
| R1.5 Manifest Builder Skeleton | **DONE** — [R1.5-MANIFEST-BUILDER-SKELETON-v1.md](R1.5-MANIFEST-BUILDER-SKELETON-v1.md) |
| R1.6 Evidence Package Model | **DONE** — [R1.6-EVIDENCE-PACKAGE-MODEL-v1.md](R1.6-EVIDENCE-PACKAGE-MODEL-v1.md) |
| R1.7 Snapshot Package Model | **DONE** — [R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md](R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md) |
| R1.8A Persistence Design Review | **DONE** — [R1.8A-PERSISTENCE-DESIGN-REVIEW-v1.md](R1.8A-PERSISTENCE-DESIGN-REVIEW-v1.md) |
| R1.8B Snapshot Storage Contract | **DONE** — [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) |
| R1.8C Persistence Layout Charter | **DONE** — [R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md](R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md) |
| R1.8D Persistence Kickoff Charter | **DONE** — [R1.8D-PERSISTENCE-KICKOFF-CHARTER-v1.md](R1.8D-PERSISTENCE-KICKOFF-CHARTER-v1.md); PC-07/PC-09 **RESOLVED** |
| R1.8 Persistence Model | **DONE** — [R1.8-PERSISTENCE-MODEL-v1.md](R1.8-PERSISTENCE-MODEL-v1.md) |
| R1.8E Persistence Verification Review | **DONE** — [R1.8E-PERSISTENCE-VERIFICATION-REVIEW-v1.md](R1.8E-PERSISTENCE-VERIFICATION-REVIEW-v1.md) (**PASS WITH NOTES**) |
| R1.9 Store Hardening | **DONE** — [R1.9-HARDENING-REVIEW-v1.md](R1.9-HARDENING-REVIEW-v1.md) (**PASS WITH NOTES**) |
| **R2 Planning Review** | **DONE** — [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) |
| **R2 Charter** | **DONE** — [R2-CHARTER-v1.md](R2-CHARTER-v1.md) |
| **R2 Implementation Charter** | **DONE** — [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md) |
| **R2.1 Evidence Package Model** | **DONE** — [R2.1-EVIDENCE-PACKAGE-MODEL-v1.md](R2.1-EVIDENCE-PACKAGE-MODEL-v1.md) |
| **R2.2 Evidence Identity Review** | **DONE** — [R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md](R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md) |
| **R2.3 Evidence Artifact Index** | **DONE** — [R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md](R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md) |
| **R2.4 Evidence Validation Boundary** | **DONE** — [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) |
| **R2.5 Evidence Quarantine Layout** | **DONE** — [R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md](R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md) |
| **R2.6 Evidence → Snapshot Handoff** | **DONE** — [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) |
| **R2 Architecture Consolidation Review** | **DONE** — [R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md](R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md) |
| **R2.7 Evidence Package Generator** | **DONE** — [R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md](R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md) |
| **R2 Readiness Review** | **DONE** — [R2-READINESS-REVIEW-v1.md](R2-READINESS-REVIEW-v1.md) |
| **R3 Charter** | **DONE** — [R3-CHARTER-v1.md](R3-CHARTER-v1.md) |
| **R3 Implementation Charter** | **DONE** — [R3-IMPLEMENTATION-CHARTER-v1.md](R3-IMPLEMENTATION-CHARTER-v1.md) |
| **R3 Readiness Review** | **DONE** — [R3-READINESS-REVIEW-v1.md](R3-READINESS-REVIEW-v1.md) |
| **R5 Charter** | **DONE** — [R5-CHARTER-v1.md](R5-CHARTER-v1.md) |
| **R5 Implementation Charter** | **DONE** — [R5-IMPLEMENTATION-CHARTER-v1.md](R5-IMPLEMENTATION-CHARTER-v1.md) |
| **R5.2 Validation Category Model** | **DONE** — [R5.2-VALIDATION-CATEGORY-MODEL-v1.md](R5.2-VALIDATION-CATEGORY-MODEL-v1.md) |
| **R5.3 Quality Possession Model** | **DONE** — [R5.3-QUALITY-POSSESSION-MODEL-v1.md](R5.3-QUALITY-POSSESSION-MODEL-v1.md) |
| **R5.4 Redaction Review Model** | **DONE** — [R5.4-REDACTION-REVIEW-MODEL-v1.md](R5.4-REDACTION-REVIEW-MODEL-v1.md) |
| **R5.5 Validate Report Contract** | **DONE** — [R5.5-VALIDATE-REPORT-CONTRACT-v1.md](R5.5-VALIDATE-REPORT-CONTRACT-v1.md) |
| **R5.6 Publish Eligibility Contract** | **DONE** — [R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md](R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md) |
| **R5.7 Validate Engine** | **DONE** — [R5.7-VALIDATE-ENGINE-v1.md](R5.7-VALIDATE-ENGINE-v1.md) |
| **R5.8 Validation Boundary Review** | **DONE** — [R5.8-VALIDATION-BOUNDARY-REVIEW-v1.md](R5.8-VALIDATION-BOUNDARY-REVIEW-v1.md) |
| **R5 Readiness Review** | **DONE** — [R5-READINESS-REVIEW-v1.md](R5-READINESS-REVIEW-v1.md) |
| **R4 Charter** | **DONE** — [R4-CHARTER-v1.md](R4-CHARTER-v1.md) |
| **R4 Implementation Charter** | **DONE** — [R4-IMPLEMENTATION-CHARTER-v1.md](R4-IMPLEMENTATION-CHARTER-v1.md) |
| **R4.1 Published Snapshot Model** | **DONE** — [R4.1-PUBLISHED-SNAPSHOT-MODEL-v1.md](R4.1-PUBLISHED-SNAPSHOT-MODEL-v1.md) |
| **R4.2 Publish State Model** | **DONE** — [R4.2-PUBLISH-STATE-MODEL-v1.md](R4.2-PUBLISH-STATE-MODEL-v1.md) |
| **R4.3 Consumer Visibility Model** | **DONE** — [R4.3-CONSUMER-VISIBILITY-MODEL-v1.md](R4.3-CONSUMER-VISIBILITY-MODEL-v1.md) |
| **R4.4 Publish Metadata Model** | **DONE** — [R4.4-PUBLISH-METADATA-MODEL-v1.md](R4.4-PUBLISH-METADATA-MODEL-v1.md) |
| **R4.5 Publish Result Contract** | **DONE** — [R4.5-PUBLISH-RESULT-CONTRACT-v1.md](R4.5-PUBLISH-RESULT-CONTRACT-v1.md) |
| **R4.6 Publish Flow Contract** | **DONE** — [R4.6-PUBLISH-FLOW-CONTRACT-v1.md](R4.6-PUBLISH-FLOW-CONTRACT-v1.md) |
| **R4.7 Publish Engine Architecture** | **DONE** — [R4.7-PUBLISH-ENGINE-ARCHITECTURE-v1.md](R4.7-PUBLISH-ENGINE-ARCHITECTURE-v1.md) |
| **R4.8 Publish Boundary Review** | **DONE** — [R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md](R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md) |
| **R4 Readiness Review** | **DONE** — [R4-READINESS-REVIEW-v1.md](R4-READINESS-REVIEW-v1.md) |
| **Mock E2E Readiness Review** | **DONE** — [EAR-MOCK-E2E-READINESS-REVIEW-v1.md](EAR-MOCK-E2E-READINESS-REVIEW-v1.md) (**READY FOR SITE-001 DRY-RUN PLANNING WITH NOTES**) |
| **SITE-001 Dry Run Plan** | **DONE** — [SITE-001-DRY-RUN-PLAN-v1.md](SITE-001-DRY-RUN-PLAN-v1.md) |
| **Execution Authorization Review** | **DONE** — [EXECUTION-AUTHORIZATION-REVIEW-v1.md](EXECUTION-AUTHORIZATION-REVIEW-v1.md) (**AUTHORIZED WITH NOTES**) |
| **Next** | HG-4 Execution Authorization Review; PILOT-001 gate (explicit human YES); real R5 assessors + R4 Store adapter |

---

## Operational triggers

| Trigger | Action |
|---------|--------|
| Start Runtime Program engineering | **DONE** — [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) |
| R1 implementation readiness | **DONE** — [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md) (**CONDITIONAL GO**) |
| R1 Implementation Charter | **DONE** — [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md) |
| R1.1 Runtime Skeleton | **DONE** — [R1.1-FOUNDATION-STATE-v1.md](R1.1-FOUNDATION-STATE-v1.md) |
| R1.2 Config Input Model | **DONE** — [R1.2-CONFIG-INPUT-MODEL-v1.md](R1.2-CONFIG-INPUT-MODEL-v1.md) |
| R1.3 Connection Layer Skeleton | **DONE** — [R1.3-CONNECTION-LAYER-SKELETON-v1.md](R1.3-CONNECTION-LAYER-SKELETON-v1.md) |
| R1.4 Remote Listing Model | **DONE** — [R1.4-REMOTE-LISTING-MODEL-v1.md](R1.4-REMOTE-LISTING-MODEL-v1.md) |
| R1.5 Manifest Builder Skeleton | **DONE** — [R1.5-MANIFEST-BUILDER-SKELETON-v1.md](R1.5-MANIFEST-BUILDER-SKELETON-v1.md) |
| R1.9 Store Hardening | **DONE** |
| R2 Planning Review | **DONE** |
| R2 Charter | **DONE** |
| R2 Implementation Charter | **DONE** |
| R2.1 Evidence Package Model | **DONE** |
| R2.2 Evidence Identity Review | **DONE** |
| R2.3 Evidence Artifact Index | **DONE** |
| R2.4 Evidence Validation Boundary | **DONE** |
| R2.5 Evidence Quarantine Layout | **DONE** |
| R2 Readiness Review | **DONE** |
| R3.3 Section Assembly Rules | **DONE** |
| R3.4 Safe Unknown Propagation | **DONE** |
| R3 Readiness Review | **DONE** |
| R5 Charter | **DONE** — R5 **COMPLETE WITH NOTES**; R5 implementation **AUTHORIZED** (human gate) |
| R4 Charter | **DONE** — R4 **COMPLETE WITH NOTES**; R4 implementation **AUTHORIZED** (human gate) |
| Implement backlog item | Charter must name item; update [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) |
| Architecture contract change | **Architecture Amendment Charter** — not runtime README |
| Live SFTP / connected acquisition | PILOT Execution Authorization — [PILOT-GOVERNANCE-v1.md](../../shared/external-access-runtime/PILOT-GOVERNANCE-v1.md) |
| Hand off to OCPilot | Published snapshot per architecture — [EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md) |

---

## Cross-references

| Source | Use |
|--------|-----|
| [shared/external-access-runtime/OPERATIONAL-INDEX.md](../../shared/external-access-runtime/OPERATIONAL-INDEX.md) | Architecture program index |
| [shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/) | Transition freeze package |
| [projects/ocpilot/OPERATIONAL-INDEX.md](../ocpilot/OPERATIONAL-INDEX.md) | OCPilot consumer |
| [AGENTS.md](../../AGENTS.md) | REPORT, HITL, SAFE UNKNOWN |

---

## Reports

Runtime engineering work ends with `# REPORT — …` per MARS discipline when the operator requests task closeout.
