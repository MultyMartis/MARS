# EAR Architecture Complete v1

**Type:** Final architecture inventory at freeze  
**Date:** 2026-06-01  
**Scope:** Phases 1, 2A–2E, 3, 4, 5, 6 (documentation program)

---

## What “COMPLETE” means

**COMPLETE** = architecture, contracts, workflows, and pilot governance are **documented**, **cross-linked**, and **sufficient** to authorize **EAR Runtime v1 Engineering** without further architecture waves as the default.

**COMPLETE does not mean:** runtime exists, connectors run, snapshots were acquired, or PILOT-001 executed.

---

## Snapshot Contract — COMPLETE

| Element | Evidence | Notes |
|---------|----------|-------|
| Logical consumer package | [EAR-SNAPSHOT-CONTRACT-v1.md](../../EAR-SNAPSHOT-CONTRACT-v1.md) | Platform-agnostic contract |
| OpenCart package shape | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../EAR-OPENCART-SNAPSHOT-SPEC-v1.md) | Sections, metadata, manifest rules |
| Quality levels 0–3 | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../EAR-OPENCART-QUALITY-MAPPING-v1.md) | Minimum evidence per level |
| Publishing rules | [EAR-SNAPSHOT-PUBLISHING-v1.md](../../EAR-SNAPSHOT-PUBLISHING-v1.md) | No credential leakage to consumers |
| Exclusions in metadata | Spec + [EAR-DEFAULT-EXCLUSIONS-v1.md](../../EAR-DEFAULT-EXCLUSIONS-v1.md) | Policy frozen at transition |

**Deferred:** Formal `ear-snapshot-v1` JSON Schema file; automated schema validation product.

---

## Workflow — COMPLETE

| Element | Evidence |
|---------|----------|
| Canonical stages | [EAR-ACQUISITION-WORKFLOW-v1.md](../../EAR-ACQUISITION-WORKFLOW-v1.md) — Request → Acquire → Validate → Publish → Archive |
| Acquisition modes 0–2 | [EAR-ACQUISITION-MODES-v1.md](../../EAR-ACQUISITION-MODES-v1.md) |
| Mode 3 | **Forbidden** in v1 — [EAR-NON-GOALS-v1.md](../../EAR-NON-GOALS-v1.md) |
| SITE-001 walkthrough (example) | [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](../../EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) |

**Deferred:** Automated workflow engine; CI gates.

---

## Lifecycle — COMPLETE

| Element | Evidence |
|---------|----------|
| Snapshot lifecycle | [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../EAR-SNAPSHOT-LIFECYCLE-v1.md) |
| Readiness gates G1–G4 | [EAR-READINESS-GATES-v1.md](../../EAR-READINESS-GATES-v1.md) |
| Failure taxonomy | [EAR-FAILURE-MODELS-v1.md](../../EAR-FAILURE-MODELS-v1.md) |
| Storage roles | [EAR-STORAGE-MODEL-v1.md](../../EAR-STORAGE-MODEL-v1.md) — repository / external / archive |

**Deferred:** Standardized org-wide quarantine path strings (operator binds per pilot).

---

## Acquisition Tracks — COMPLETE

| Track | Evidence |
|-------|----------|
| Two-track model | [EAR-ACQUISITION-TRACKS-v1.md](../../EAR-ACQUISITION-TRACKS-v1.md) |
| Offline — Archive First | [EAR-OFFLINE-ACQUISITION-v1.md](../../EAR-OFFLINE-ACQUISITION-v1.md), [EAR-OFFLINE-PATHS-v1.md](../../EAR-OFFLINE-PATHS-v1.md) |
| Connected — Managed Project | [EAR-CONNECTED-ACQUISITION-v1.md](../../EAR-CONNECTED-ACQUISITION-v1.md), [EAR-CONNECTED-PATHS-v1.md](../../EAR-CONNECTED-PATHS-v1.md) |
| Selection guide | [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](../../EAR-ACQUISITION-SELECTION-GUIDE-v1.md) |
| OpenCart channel design | [EAR-OPENCART-ACQUISITION-DESIGN-v1.md](../../EAR-OPENCART-ACQUISITION-DESIGN-v1.md), [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](../../EAR-OPENCART-SNAPSHOT-PATHS-v1.md) |
| Phase 2E decisions | [EAR-PHASE-2E-DESIGN-DECISIONS-v1.md](../../EAR-PHASE-2E-DESIGN-DECISIONS-v1.md) |

**Deferred:** Hybrid coordinator pilot; additional connector-class pilots beyond PILOT-001 scope.

---

## Connector Architecture — COMPLETE (design)

| Element | Evidence |
|---------|----------|
| Layer model | [EAR-CONNECTOR-ARCHITECTURE-v1.md](../../EAR-CONNECTOR-ARCHITECTURE-v1.md) |
| Connector classes | [EAR-CONNECTOR-TYPES-v1.md](../../EAR-CONNECTOR-TYPES-v1.md) |
| I/O contract | [EAR-CONNECTOR-CONTRACT-v1.md](../../EAR-CONNECTOR-CONTRACT-v1.md) |
| Evidence vs snapshot | [EAR-EVIDENCE-PACKAGE-v1.md](../../EAR-EVIDENCE-PACKAGE-v1.md) |
| Section mapping | [EAR-SNAPSHOT-MAPPING-v1.md](../../EAR-SNAPSHOT-MAPPING-v1.md) |
| Failures | [EAR-CONNECTOR-FAILURES-v1.md](../../EAR-CONNECTOR-FAILURES-v1.md) |
| OpenCart Mode 2 reference | [EAR-MODE-2-OPENCART-REFERENCE-v1.md](../../EAR-MODE-2-OPENCART-REFERENCE-v1.md) |
| Connection catalog | [EAR-CONNECTION-TYPES-v1.md](../../EAR-CONNECTION-TYPES-v1.md) |

**Deferred:** Any executable connector; SFTP client library choice; registry database.

---

## Pilot System — COMPLETE (governance)

| Element | Evidence |
|---------|----------|
| Pilot vs runtime vs production | [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) |
| First pilot charter | [pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md](../../pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md) |
| Success / stop / risks | SUCCESS-CRITERIA, STOP-CONDITIONS, RISK-REGISTER in pilot folder |
| Implementation readiness | Phase 5 review + **CONDITIONAL GO** |
| Sub-charter | [IMPLEMENTATION-SUBCHARTER-v1.md](../../pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-v1.md) — drafted |
| Phase 3 / 5 / 6 decisions | EAR-PHASE-3-DECISION, PHASE-5-DECISION, PHASE-6-DECISION |

**Deferred:** Operator Approval, Implementation Authorization sign-off, Execution Authorization, live acquisition.

---

## Governance — COMPLETE

| Element | Evidence |
|---------|----------|
| Charter and scope | [EAR-CHARTER-v1.md](../../EAR-CHARTER-v1.md), [EAR-SCOPE-v1.md](../../EAR-SCOPE-v1.md) |
| Security / HITL | [EAR-SECURITY-MODEL-v1.md](../../EAR-SECURITY-MODEL-v1.md) |
| Credential boundary | [EAR-CREDENTIAL-BOUNDARY-v1.md](../../EAR-CREDENTIAL-BOUNDARY-v1.md) |
| Modes | [EAR-MODES-v1.md](../../EAR-MODES-v1.md) — v1 target Mode 2 |
| OpenCart risks | [EAR-OPENCART-RISK-MODEL-v1.md](../../EAR-OPENCART-RISK-MODEL-v1.md) |
| Consumer separation | [EAR-OPENCART-CONSUMER-GUIDE-v1.md](../../EAR-OPENCART-CONSUMER-GUIDE-v1.md), [EAR-OCPILOT-INTEGRATION-v1.md](../../EAR-OCPILOT-INTEGRATION-v1.md) |
| Pre-runtime readiness criteria | [EAR-RUNTIME-READINESS-v1.md](../../EAR-RUNTIME-READINESS-v1.md) |

---

## Readiness — COMPLETE (assessment artifact)

| Element | Evidence | Outcome |
|---------|----------|---------|
| Formal audit | [EAR-RUNTIME-READINESS-ASSESSMENT-v1.md](../../EAR-RUNTIME-READINESS-ASSESSMENT-v1.md) | 15 READY, 3 PARTIAL, 0 NOT READY |
| Decision record | [EAR-PHASE-3-DECISION-v1.md](../../EAR-PHASE-3-DECISION-v1.md) | **CONDITIONAL GO** for pilot charter |

**PARTIAL (accepted):** Storage path standardization; operational Request template; roadmap vs OPERATIONAL-INDEX phase numbering.

---

## Architecture freeze boundary

New work that belongs in **Runtime Engineering** (not architecture) is defined in [EAR-RUNTIME-BOUNDARY-v1.md](../../EAR-RUNTIME-BOUNDARY-v1.md).

Amendments to frozen architecture require explicit human **Architecture Amendment Charter** — not implied by runtime tasks.
