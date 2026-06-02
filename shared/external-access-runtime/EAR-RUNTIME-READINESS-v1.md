# EAR Runtime Readiness v1

**Purpose:** Define what must exist **before EAR runtime implementation may begin** — readiness criteria only, not a runtime design.  
**Status:** gate checklist — **no** implementation claimed.  
**Phase:** 2D (criteria) → assessed in **Phase 3 — Runtime Readiness Assessment**

---

## Readiness stance

Runtime implementation is **forbidden** until explicit human charter approves Phase 3+ work **and** readiness criteria below are satisfied or explicitly waived with documented risk acceptance.

Phase 2D completes **architecture** for Mode 2 connectors. Phase 3 **assesses** gap between architecture and implementable runtime — it does not imply implementation by default.

---

## Prerequisites (documentation)

| Prerequisite | Document | Phase | Status at 2D freeze |
|--------------|----------|-------|---------------------|
| EAR foundation | [EAR-ARCHITECTURE-v1.md](EAR-ARCHITECTURE-v1.md), [EAR-CHARTER-v1.md](EAR-CHARTER-v1.md) | 1 | **DONE** |
| Snapshot contract | [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md), [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md) | 2A | **DONE** |
| Acquisition workflow | [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md), lifecycle, publishing | 2B | **DONE** |
| OpenCart acquisition design | [EAR-OPENCART-ACQUISITION-DESIGN-v1.md](EAR-OPENCART-ACQUISITION-DESIGN-v1.md) + siblings | 2C | **DONE** |
| Connector architecture | [EAR-CONNECTOR-ARCHITECTURE-v1.md](EAR-CONNECTOR-ARCHITECTURE-v1.md) + Phase 2D siblings | 2D | **DONE** |
| Connector contract | [EAR-CONNECTOR-CONTRACT-v1.md](EAR-CONNECTOR-CONTRACT-v1.md) | 2D | **DONE** |
| Credential boundaries | [EAR-CREDENTIAL-BOUNDARY-v1.md](EAR-CREDENTIAL-BOUNDARY-v1.md) | 2D | **DONE** |
| Evidence package model | [EAR-EVIDENCE-PACKAGE-v1.md](EAR-EVIDENCE-PACKAGE-v1.md) | 2D | **DONE** |
| Snapshot mapping | [EAR-SNAPSHOT-MAPPING-v1.md](EAR-SNAPSHOT-MAPPING-v1.md) | 2D | **DONE** |
| Connector failure model | [EAR-CONNECTOR-FAILURES-v1.md](EAR-CONNECTOR-FAILURES-v1.md) | 2D | **DONE** |
| Workflow failure model | [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md) | 2B | **DONE** |
| Storage model | [EAR-STORAGE-MODEL-v1.md](EAR-STORAGE-MODEL-v1.md) | 2B | **DONE** (conceptual) |
| Security model | [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md) | 1 | **DONE** |
| Readiness gates | [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) | 2B | **DONE** |

---

## Readiness criteria (must be true to start runtime)

### Architecture completeness

| Criterion | Verification |
|-----------|--------------|
| Connector purpose, lifecycle, and non-responsibilities defined | Phase 2D architecture doc |
| All v1 connector classes cataloged with limits | [EAR-CONNECTOR-TYPES-v1.md](EAR-CONNECTOR-TYPES-v1.md) |
| Evidence vs Snapshot vs Consumer output distinguished | [EAR-EVIDENCE-PACKAGE-v1.md](EAR-EVIDENCE-PACKAGE-v1.md) |
| OpenCart reference flow documented | [EAR-MODE-2-OPENCART-REFERENCE-v1.md](EAR-MODE-2-OPENCART-REFERENCE-v1.md) |

### Validation model

| Criterion | Verification |
|-----------|--------------|
| Validate stage owns quality level and `safe-unknown` | Workflow + mapping docs |
| Redaction rules before publish | Credential boundary + OpenCart spec |
| Partial acquisition publish rules | Connector failures + publishing doc |

### Human authority

| Criterion | Verification |
|-----------|--------------|
| HITL before Mode 2 Acquire | [EAR-MODES-v1.md](EAR-MODES-v1.md), security model |
| Operator publish approval | [EAR-SNAPSHOT-PUBLISHING-v1.md](EAR-SNAPSHOT-PUBLISHING-v1.md) |
| Mode 3 forbidden in v1 | [EAR-MODES-v1.md](EAR-MODES-v1.md) |

### Risk acceptance

| Criterion | Verification |
|-----------|--------------|
| Per-connector risks documented | Phase 2C risk model + connector types |
| SITE-specific options documented as example only | SITE-001 docs |
| Explicit charter for first runtime pilot (site, channel, level) | **Required at Phase 3** — not satisfied by docs alone |

---

## Known gaps (block or waive at Phase 3)

| Gap | Blocks runtime? | Notes |
|-----|-----------------|-------|
| Formal schema / serializer for snapshot | Soft block | May implement with human validation first |
| Formal schema for Evidence Package | Soft block | Contract is conceptual |
| External quarantine path standardization | Medium | [EAR-STORAGE-MODEL-v1.md](EAR-STORAGE-MODEL-v1.md) conceptual only |
| Credential store product | Medium | Operator external secrets |
| Connector registry and versioning | Medium | Phase 3 assessment |
| Automated validation tooling | Soft | Manual Validate acceptable for pilot |
| Virus scan on ZIP | Soft | Policy **SAFE UNKNOWN** |
| FTPS-only decision | Soft | Charter |

---

## Phase 3 assessment outputs (expected)

Phase 3 **does not** implement runtime by default. Expected deliverables:

| Output | Purpose |
|--------|---------|
| Gap matrix | Architecture vs implementable MVP |
| Pilot charter template | First connector (likely SFTP or ZIP Intake) |
| Waived risks register | Explicit human acceptance |
| Go / no-go for implementation sub-charter | Separate from Phase 3 assessment |

---

## Minimum runtime MVP (future — not authorized here)

When charter approves implementation, smallest slice likely:

1. One connector class (ZIP Intake or SFTP).
2. Manual Validate (operator checklist).
3. OpenCart L1 snapshot publish to external bulk.
4. OCPilot intake test on published package.

Order and scope — **Phase 3 assessment**, not Phase 2D.

---

## SAFE UNKNOWN

- Programming language, packaging (CLI vs service), and repo location for runtime code.
- Whether runtime lives in MARS repo or consumer repo — charter decision.

---

## Non-goals

- Declaring runtime ready at Phase 2D freeze.
- Implementing connectors in Phase 2D.
