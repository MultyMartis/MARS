# EAR — Operational Index



**Subsystem:** External Access Runtime (EAR) v1  

**Lane:** B — Shared Infrastructure (External Systems)  

**Status:** documented navigation only; **not** automated router or service registry



**Domain root:** [README.md](README.md)



---



## Programs (authoritative)



| Program | Status | Next |
|---------|--------|------|
| **EAR Architecture Program** | **COMPLETE** (frozen 2026-06-01) | Amendments only via explicit Architecture Amendment Charter |
| **EAR Runtime Program** | **STARTED** | R1.3 Connection Layer Skeleton — [projects/ear-runtime/](../../projects/ear-runtime/OPERATIONAL-INDEX.md) · state: [EAR-RUNTIME-STATE.md](../../projects/ear-runtime/EAR-RUNTIME-STATE.md) |



**Freeze package:** [freeze/EAR-RUNTIME-TRANSITION-v1/](freeze/EAR-RUNTIME-TRANSITION-v1/) · **Runtime project:** [projects/ear-runtime/](../../projects/ear-runtime/) · **Backlog:** [EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md) (authoritative) · **Boundary:** [EAR-RUNTIME-BOUNDARY-v1.md](EAR-RUNTIME-BOUNDARY-v1.md) · **Closeout:** [EAR-PHASE-CLOSEOUT-v1.md](EAR-PHASE-CLOSEOUT-v1.md) · **Exclusions:** [EAR-DEFAULT-EXCLUSIONS-v1.md](EAR-DEFAULT-EXCLUSIONS-v1.md)



---



## Canonical reading order



| Step | Document | Why |

|------|----------|-----|

| 1 | [README.md](README.md) | Scope and truth statement |

| 2 | [EAR-CHARTER-v1.md](EAR-CHARTER-v1.md) | Mission and boundaries |

| 3 | [EAR-ARCHITECTURE-v1.md](EAR-ARCHITECTURE-v1.md) | Operator → EAR → Snapshot → Consumer |

| 4 | [EAR-MODES-v1.md](EAR-MODES-v1.md) | Mode 0–3; v1 target Mode 2 |

| 5 | [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md) | Consumer input package |

| 6 | [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md) | Secrets, HITL, read-only default |

| 7 | [EAR-CONNECTION-TYPES-v1.md](EAR-CONNECTION-TYPES-v1.md) | Connector families (future) |

| 8 | [EAR-SCOPE-v1.md](EAR-SCOPE-v1.md) / [EAR-NON-GOALS-v1.md](EAR-NON-GOALS-v1.md) | In/out |

| 9 | [EAR-ROADMAP-v1.md](EAR-ROADMAP-v1.md) | Phases — no promises |

| 10 | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md) | OpenCart package structure (Phase 2A) |

| 11 | [EAR-SNAPSHOT-LIFECYCLE-v1.md](EAR-SNAPSHOT-LIFECYCLE-v1.md) | Acquire → Archive (Phase 2A) |

| 12 | [EAR-OPENCART-CONSUMER-GUIDE-v1.md](EAR-OPENCART-CONSUMER-GUIDE-v1.md) | OCPilot intake rules |

| 13 | [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md) | **Canonical** Request → Archive workflow (Phase 2B) |

| 14 | [EAR-ACQUISITION-MODES-v1.md](EAR-ACQUISITION-MODES-v1.md) | Manual / Guided / Connected modes (Phase 2B) |

| 15 | [EAR-SNAPSHOT-PUBLISHING-v1.md](EAR-SNAPSHOT-PUBLISHING-v1.md) | Publish gate and consumer visibility |

| 16 | [EAR-STORAGE-MODEL-v1.md](EAR-STORAGE-MODEL-v1.md) | Repository / external / archive roles |

| 17 | [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md) | Failure taxonomy and EAR behavior |

| 18 | [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) | Stage advancement gates |

| 19 | [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) | SITE-001 walkthrough (example only) |

| 20 | [EAR-OPENCART-ACQUISITION-DESIGN-v1.md](EAR-OPENCART-ACQUISITION-DESIGN-v1.md) | **Canonical** OpenCart acquisition design — channels + matrix (Phase 2C) |

| 21 | [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md) | Channel paths → Snapshot Levels 0–3 (Phase 2C) |

| 22 | [EAR-OPENCART-RISK-MODEL-v1.md](EAR-OPENCART-RISK-MODEL-v1.md) | Per-channel risks + EAR behavior (Phase 2C) |

| 23 | [EAR-OPENCART-QUALITY-MAPPING-v1.md](EAR-OPENCART-QUALITY-MAPPING-v1.md) | Level 0–3 minimum evidence (Phase 2C) |

| 24 | [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) | SITE-001 theoretical options (example only) |

| 25 | [EAR-OPENCART-READINESS-CHECKLIST-v1.md](EAR-OPENCART-READINESS-CHECKLIST-v1.md) | Pre-acquisition checklist (Phase 2C) |

| 26 | [EAR-OPENCART-DESIGN-DECISIONS-v1.md](EAR-OPENCART-DESIGN-DECISIONS-v1.md) | Phase 2C design decisions |

| 27 | [EAR-CONNECTOR-ARCHITECTURE-v1.md](EAR-CONNECTOR-ARCHITECTURE-v1.md) | **Canonical** Mode 2 connector model (Phase 2D) |

| 28 | [EAR-CONNECTOR-TYPES-v1.md](EAR-CONNECTOR-TYPES-v1.md) | Connector classes + max snapshot quality (Phase 2D) |

| 29 | [EAR-CONNECTOR-CONTRACT-v1.md](EAR-CONNECTOR-CONTRACT-v1.md) | Connector input/output/status contract (Phase 2D) |

| 30 | [EAR-CREDENTIAL-BOUNDARY-v1.md](EAR-CREDENTIAL-BOUNDARY-v1.md) | Credential separation of concerns (Phase 2D) |

| 31 | [EAR-EVIDENCE-PACKAGE-v1.md](EAR-EVIDENCE-PACKAGE-v1.md) | Evidence vs Snapshot vs consumer output (Phase 2D) |

| 32 | [EAR-SNAPSHOT-MAPPING-v1.md](EAR-SNAPSHOT-MAPPING-v1.md) | Connector → snapshot section mapping (Phase 2D) |

| 33 | [EAR-CONNECTOR-FAILURES-v1.md](EAR-CONNECTOR-FAILURES-v1.md) | Connector failure taxonomy (Phase 2D) |

| 34 | [EAR-MODE-2-OPENCART-REFERENCE-v1.md](EAR-MODE-2-OPENCART-REFERENCE-v1.md) | OpenCart Mode 2 reference flow (Phase 2D) |

| 35 | [EAR-RUNTIME-READINESS-v1.md](EAR-RUNTIME-READINESS-v1.md) | Pre-runtime readiness criteria (Phase 2D) |

| 36 | [EAR-PHASE-2D-DESIGN-DECISIONS-v1.md](EAR-PHASE-2D-DESIGN-DECISIONS-v1.md) | Phase 2D design decisions |

| 37 | [EAR-ACQUISITION-TRACKS-v1.md](EAR-ACQUISITION-TRACKS-v1.md) | **Canonical** Offline + Connected two-track model (Phase 2E) |

| 38 | [EAR-OFFLINE-ACQUISITION-v1.md](EAR-OFFLINE-ACQUISITION-v1.md) | Offline track — Archive First (Phase 2E) |

| 39 | [EAR-CONNECTED-ACQUISITION-v1.md](EAR-CONNECTED-ACQUISITION-v1.md) | Connected track — Managed Project (Phase 2E) |

| 40 | [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](EAR-ACQUISITION-SELECTION-GUIDE-v1.md) | Track selection decision guide (Phase 2E) |

| 41 | [EAR-OFFLINE-PATHS-v1.md](EAR-OFFLINE-PATHS-v1.md) | Canonical offline paths → snapshot levels (Phase 2E) |

| 42 | [EAR-CONNECTED-PATHS-v1.md](EAR-CONNECTED-PATHS-v1.md) | Canonical connected paths → snapshot levels (Phase 2E) |

| 43 | [EAR-OCPILOT-INTEGRATION-v1.md](EAR-OCPILOT-INTEGRATION-v1.md) | OCPilot × EAR by track — audit vs operations (Phase 2E) |

| 44 | [EAR-FUTURE-CONSUMERS-v1.md](EAR-FUTURE-CONSUMERS-v1.md) | Expected consumers and track preferences (Phase 2E) |

| 45 | [EAR-PHASE-2E-DESIGN-DECISIONS-v1.md](EAR-PHASE-2E-DESIGN-DECISIONS-v1.md) | Phase 2E design decisions |

| 46 | [EAR-RUNTIME-READINESS-ASSESSMENT-v1.md](EAR-RUNTIME-READINESS-ASSESSMENT-v1.md) | Phase 3 readiness audit — charter go/no-go |

| 47 | [EAR-PHASE-3-DECISION-v1.md](EAR-PHASE-3-DECISION-v1.md) | Phase 3 decision record |

| 48 | [PILOT-GOVERNANCE-v1.md](PILOT-GOVERNANCE-v1.md) | Pilot vs runtime / production boundaries (Phase 4) |

| 49 | [pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md) | First Connected Acquisition pilot charter |

| 50 | [PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md](PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md) | PILOT-001 assessment plan (no execution) |

| 51 | [pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-READINESS-REVIEW-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-READINESS-REVIEW-v1.md) | Phase 5 implementation readiness assessment |

| 52 | [pilots/PILOT-001-SITE-001-SFTP-READONLY/PHASE-5-DECISION-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/PHASE-5-DECISION-v1.md) | Phase 5 decision record |

| 53 | [pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md) | Sub-charter requirements (CONDITIONAL GO) |

| 54 | [pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-v1.md) | PILOT-001 Implementation Sub-Charter (boundaries; no execution) |

| 55 | [pilots/PILOT-001-SITE-001-SFTP-READONLY/EXECUTION-PREPARATION-PLAN-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/EXECUTION-PREPARATION-PLAN-v1.md) | Execution preparation stages (planning only) |

| 56 | [pilots/PILOT-001-SITE-001-SFTP-READONLY/PHASE-6-DECISION-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/PHASE-6-DECISION-v1.md) | Phase 6 decision record |

| 57 | [freeze/EAR-RUNTIME-TRANSITION-v1/](freeze/EAR-RUNTIME-TRANSITION-v1/) | **Architecture freeze** — transition to Runtime v1 |

| 58 | [EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md) | Runtime engineering backlog (R1–R5) |

| 59 | [EAR-RUNTIME-BOUNDARY-v1.md](EAR-RUNTIME-BOUNDARY-v1.md) | Architecture vs runtime layer boundary |

| 60 | [EAR-DEFAULT-EXCLUSIONS-v1.md](EAR-DEFAULT-EXCLUSIONS-v1.md) | Default acquisition exclusion policy |

| 61 | [EAR-PHASE-CLOSEOUT-v1.md](EAR-PHASE-CLOSEOUT-v1.md) | Phases 1–6 one-page closeout |



**Terms:** [EAR-GLOSSARY-v1.md](EAR-GLOSSARY-v1.md)



---



## Phase status



| Phase | Name | Status | Next |

|-------|------|--------|------|

| **1** | Architecture foundation | **DONE** | — |

| **2A** | OpenCart Snapshot Specification | **DONE** | — |

| **2B** | Read-Only Acquisition Workflow | **DONE** | — |

| **2C** | OpenCart Read-Only Acquisition Design | **DONE** | — |

| **2D** | Mode 2 Read-Only Connector Architecture | **DONE** | — |

| **2E** | Acquisition Tracks Architecture | **DONE** | — |

| **3** | Runtime Readiness Assessment | **DONE** | — |

| **4** | Connected Acquisition Pilot Charter | **DONE** | — |

| **5** | Implementation Readiness Review | **DONE** | — |

| **6** | Implementation Sub-Charter | **DONE** | — (architecture program frozen) |

| **—** | **Architecture freeze** | **DONE** | Runtime Program — Engineering Charter |

| **—** | **EAR Runtime Program** | **STARTED** | [projects/ear-runtime/](../../projects/ear-runtime/EAR-RUNTIME-STATE.md) · R1.3 next · [EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md) |



**Architecture program:** Phases 1–6 + [freeze/EAR-RUNTIME-TRANSITION-v1/](freeze/EAR-RUNTIME-TRANSITION-v1/) = **COMPLETE**. Further normative architecture requires **Architecture Amendment Charter**. PILOT-001 operator track (Phase 7 Execution Preparation Review, approvals) continues under [PILOT-GOVERNANCE-v1.md](PILOT-GOVERNANCE-v1.md) — **not** architecture expansion.



**Phase 2A deliverables:** [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md), [EAR-SNAPSHOT-LIFECYCLE-v1.md](EAR-SNAPSHOT-LIFECYCLE-v1.md), [EAR-OPENCART-CONSUMER-GUIDE-v1.md](EAR-OPENCART-CONSUMER-GUIDE-v1.md). **No** code, connectors, or runtime.



**Phase 2B deliverables:** [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md), [EAR-ACQUISITION-MODES-v1.md](EAR-ACQUISITION-MODES-v1.md), [EAR-SNAPSHOT-PUBLISHING-v1.md](EAR-SNAPSHOT-PUBLISHING-v1.md), [EAR-STORAGE-MODEL-v1.md](EAR-STORAGE-MODEL-v1.md), [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md), [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md), [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md). **No** code, connectors, scripts, automation, SSH, or FTP implementation.



**Phase 2C deliverables:** [EAR-OPENCART-ACQUISITION-DESIGN-v1.md](EAR-OPENCART-ACQUISITION-DESIGN-v1.md), [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md), [EAR-OPENCART-RISK-MODEL-v1.md](EAR-OPENCART-RISK-MODEL-v1.md), [EAR-OPENCART-QUALITY-MAPPING-v1.md](EAR-OPENCART-QUALITY-MAPPING-v1.md), [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](EAR-SITE-001-ACQUISITION-OPTIONS-v1.md), [EAR-OPENCART-READINESS-CHECKLIST-v1.md](EAR-OPENCART-READINESS-CHECKLIST-v1.md), [EAR-OPENCART-DESIGN-DECISIONS-v1.md](EAR-OPENCART-DESIGN-DECISIONS-v1.md). **No** code, connectors, scripts, automation, SSH/FTP implementation, or access execution.

**Phase 2D deliverables:** [EAR-CONNECTOR-ARCHITECTURE-v1.md](EAR-CONNECTOR-ARCHITECTURE-v1.md), [EAR-CONNECTOR-TYPES-v1.md](EAR-CONNECTOR-TYPES-v1.md), [EAR-CONNECTOR-CONTRACT-v1.md](EAR-CONNECTOR-CONTRACT-v1.md), [EAR-CREDENTIAL-BOUNDARY-v1.md](EAR-CREDENTIAL-BOUNDARY-v1.md), [EAR-EVIDENCE-PACKAGE-v1.md](EAR-EVIDENCE-PACKAGE-v1.md), [EAR-SNAPSHOT-MAPPING-v1.md](EAR-SNAPSHOT-MAPPING-v1.md), [EAR-CONNECTOR-FAILURES-v1.md](EAR-CONNECTOR-FAILURES-v1.md), [EAR-MODE-2-OPENCART-REFERENCE-v1.md](EAR-MODE-2-OPENCART-REFERENCE-v1.md), [EAR-RUNTIME-READINESS-v1.md](EAR-RUNTIME-READINESS-v1.md), [EAR-PHASE-2D-DESIGN-DECISIONS-v1.md](EAR-PHASE-2D-DESIGN-DECISIONS-v1.md). **No** code, runtime, connectors, scripts, schemas, automation, SSH, FTP, or access execution.

**Phase 2E deliverables:** [EAR-ACQUISITION-TRACKS-v1.md](EAR-ACQUISITION-TRACKS-v1.md), [EAR-OFFLINE-ACQUISITION-v1.md](EAR-OFFLINE-ACQUISITION-v1.md), [EAR-CONNECTED-ACQUISITION-v1.md](EAR-CONNECTED-ACQUISITION-v1.md), [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](EAR-ACQUISITION-SELECTION-GUIDE-v1.md), [EAR-OFFLINE-PATHS-v1.md](EAR-OFFLINE-PATHS-v1.md), [EAR-CONNECTED-PATHS-v1.md](EAR-CONNECTED-PATHS-v1.md), [EAR-OCPILOT-INTEGRATION-v1.md](EAR-OCPILOT-INTEGRATION-v1.md), [EAR-FUTURE-CONSUMERS-v1.md](EAR-FUTURE-CONSUMERS-v1.md), [EAR-PHASE-2E-DESIGN-DECISIONS-v1.md](EAR-PHASE-2E-DESIGN-DECISIONS-v1.md). **No** code, runtime, connectors, scripts, automation, or access execution.

**Phase 3 deliverables:** [EAR-RUNTIME-READINESS-ASSESSMENT-v1.md](EAR-RUNTIME-READINESS-ASSESSMENT-v1.md), [EAR-PHASE-3-DECISION-v1.md](EAR-PHASE-3-DECISION-v1.md). **Decision:** **CONDITIONAL GO** for first Connector Pilot Charter authorization. **No** code, runtime, connectors, scripts, automation, or live access execution.

**Phase 4 deliverables:** [pilots/PILOT-001-SITE-001-SFTP-READONLY/](pilots/PILOT-001-SITE-001-SFTP-READONLY/) (charter, success criteria, stop conditions, risk register, status, lessons-learned placeholder), [PILOT-GOVERNANCE-v1.md](PILOT-GOVERNANCE-v1.md), [PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md](PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md). **First authorized EAR pilot:** `PILOT-001` — SITE-001, SFTP Read-Only, Connected Acquisition, Mode 2, TEST, Level 1 target, OCPilot consumer. **No** code, runtime, connectors, scripts, SFTP logic, or access execution.

**Phase 5 deliverables:** [pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-READINESS-REVIEW-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-READINESS-REVIEW-v1.md), [pilots/PILOT-001-SITE-001-SFTP-READONLY/PHASE-5-DECISION-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/PHASE-5-DECISION-v1.md), [pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md). **Decision:** **CONDITIONAL GO** for PILOT-001 Implementation Sub-Charter authorization (drafting + human sign-off after Approval). **No** code, runtime, connectors, scripts, SFTP logic, or access execution.

**Phase 6 deliverables:** [pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-v1.md), [pilots/PILOT-001-SITE-001-SFTP-READONLY/EXECUTION-PREPARATION-PLAN-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/EXECUTION-PREPARATION-PLAN-v1.md), [pilots/PILOT-001-SITE-001-SFTP-READONLY/PHASE-6-DECISION-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/PHASE-6-DECISION-v1.md). **Outcome:** Implementation Sub-Charter **drafted**; operational paths **SAFE UNKNOWN**; **Execution NOT AUTHORIZED**. **No** code, runtime, connectors, scripts, SFTP logic, or access execution.

**Next (runtime program):** Authorize **EAR Runtime v1 Engineering Charter** — implement [EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md) per [EAR-RUNTIME-BOUNDARY-v1.md](EAR-RUNTIME-BOUNDARY-v1.md) under [projects/ear-runtime/](../../projects/ear-runtime/). Handoff: [freeze/EAR-RUNTIME-TRANSITION-v1/EAR-RUNTIME-HANDOFF-v1.md](freeze/EAR-RUNTIME-TRANSITION-v1/EAR-RUNTIME-HANDOFF-v1.md). Placement: [projects/ear-runtime/DECISION-EAR-RUNTIME-PLACEMENT-v1.md](../../projects/ear-runtime/DECISION-EAR-RUNTIME-PLACEMENT-v1.md).

**Next (operator / PILOT-001):** Phase 7 **Execution Preparation Review** — record **Approval** in STATUS if charter accepted → resolve §4 bindings → human **Implementation Authorization** on sub-charter §10 → separate **Execution Authorization** if live access desired. **Execution remains NOT AUTHORIZED** at architecture freeze.

Roadmap note: [EAR-ROADMAP-v1.md](EAR-ROADMAP-v1.md) phase numbering may differ — OPERATIONAL-INDEX is authoritative for EAR operational phases.



---



## Consumers (documentation references only)



| Consumer | Platform | EAR use (planned) |

|----------|----------|-------------------|

| OCPilot | OpenCart / ocStore | SITE-001 Run 5 — snapshot for read-only audit |

| WPilot | WordPress | Future read-only acquisition |

| Website Factory | Multi-site production | **SAFE UNKNOWN** — future |

| Landing Pilot | Landing / static | **SAFE UNKNOWN** — future |



No consumer implementation claimed in EAR v1 foundation.



---



## Operational triggers



| Trigger | Action |

|---------|--------|

| New external site audit chartered | Start at **Request** — [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md); mode 0–2 only |

| Operator provides files manually | Mode 0 — validate gates before Publish |

| EAR issues artifact checklist | Mode 1 — [EAR-ACQUISITION-MODES-v1.md](EAR-ACQUISITION-MODES-v1.md) |

| Missing artifacts block consumer | [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md); `safe-unknown`; no publish at inflated quality |

| Ready to hand off to OCPilot | [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) G4 + [EAR-SNAPSHOT-PUBLISHING-v1.md](EAR-SNAPSHOT-PUBLISHING-v1.md) |

| OpenCart snapshot shape / quality level | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |

| OCPilot intake or Run 5 resume | [EAR-OPENCART-CONSUMER-GUIDE-v1.md](EAR-OPENCART-CONSUMER-GUIDE-v1.md) |

| Where snapshots live (conceptual) | [EAR-STORAGE-MODEL-v1.md](EAR-STORAGE-MODEL-v1.md) |

| SITE-001 example path | [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) |

| OpenCart acquisition channels / paths | [EAR-OPENCART-ACQUISITION-DESIGN-v1.md](EAR-OPENCART-ACQUISITION-DESIGN-v1.md), [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md) |

| Pre-acquisition checklist | [EAR-OPENCART-READINESS-CHECKLIST-v1.md](EAR-OPENCART-READINESS-CHECKLIST-v1.md) |

| SITE-001 channel options (theoretical) | [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) |

| Snapshot publish vs archive | [EAR-SNAPSHOT-LIFECYCLE-v1.md](EAR-SNAPSHOT-LIFECYCLE-v1.md) + Phase 2B Publish stage |

| Connector model / contract / types | [EAR-CONNECTOR-ARCHITECTURE-v1.md](EAR-CONNECTOR-ARCHITECTURE-v1.md), [EAR-CONNECTOR-CONTRACT-v1.md](EAR-CONNECTOR-CONTRACT-v1.md), [EAR-CONNECTOR-TYPES-v1.md](EAR-CONNECTOR-TYPES-v1.md) |

| Evidence vs snapshot | [EAR-EVIDENCE-PACKAGE-v1.md](EAR-EVIDENCE-PACKAGE-v1.md) |

| Credential boundaries | [EAR-CREDENTIAL-BOUNDARY-v1.md](EAR-CREDENTIAL-BOUNDARY-v1.md) |

| Connector → section mapping | [EAR-SNAPSHOT-MAPPING-v1.md](EAR-SNAPSHOT-MAPPING-v1.md) |

| Connector failures | [EAR-CONNECTOR-FAILURES-v1.md](EAR-CONNECTOR-FAILURES-v1.md) |

| OpenCart Mode 2 reference | [EAR-MODE-2-OPENCART-REFERENCE-v1.md](EAR-MODE-2-OPENCART-REFERENCE-v1.md) |

| Pre-runtime readiness | [EAR-RUNTIME-READINESS-v1.md](EAR-RUNTIME-READINESS-v1.md) |

| Write access requested | **Stop** — Mode 3 not in v1; separate future charter |

| Choose Offline vs Connected vs Hybrid | [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](EAR-ACQUISITION-SELECTION-GUIDE-v1.md) |

| Two-track model overview | [EAR-ACQUISITION-TRACKS-v1.md](EAR-ACQUISITION-TRACKS-v1.md) |

| Archive-first / client package acquisition | [EAR-OFFLINE-ACQUISITION-v1.md](EAR-OFFLINE-ACQUISITION-v1.md), [EAR-OFFLINE-PATHS-v1.md](EAR-OFFLINE-PATHS-v1.md) |

| Managed project / recurring connected acquisition | [EAR-CONNECTED-ACQUISITION-v1.md](EAR-CONNECTED-ACQUISITION-v1.md), [EAR-CONNECTED-PATHS-v1.md](EAR-CONNECTED-PATHS-v1.md) |

| OCPilot track-specific workflows | [EAR-OCPILOT-INTEGRATION-v1.md](EAR-OCPILOT-INTEGRATION-v1.md) |

| Future consumer track preferences | [EAR-FUTURE-CONSUMERS-v1.md](EAR-FUTURE-CONSUMERS-v1.md) |

| Phase 2E decisions | [EAR-PHASE-2E-DESIGN-DECISIONS-v1.md](EAR-PHASE-2E-DESIGN-DECISIONS-v1.md) |

| Phase 3 readiness / decision | [EAR-RUNTIME-READINESS-ASSESSMENT-v1.md](EAR-RUNTIME-READINESS-ASSESSMENT-v1.md), [EAR-PHASE-3-DECISION-v1.md](EAR-PHASE-3-DECISION-v1.md) |

| First Connected Acquisition pilot | [pilots/PILOT-001-SITE-001-SFTP-READONLY/](pilots/PILOT-001-SITE-001-SFTP-READONLY/) |

| Pilot governance / assessment | [PILOT-GOVERNANCE-v1.md](PILOT-GOVERNANCE-v1.md), [PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md](PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md) |

| Architecture freeze / runtime transition | [freeze/EAR-RUNTIME-TRANSITION-v1/](freeze/EAR-RUNTIME-TRANSITION-v1/) |

| Runtime backlog / boundary / exclusions | [EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md), [EAR-RUNTIME-BOUNDARY-v1.md](EAR-RUNTIME-BOUNDARY-v1.md), [EAR-DEFAULT-EXCLUSIONS-v1.md](EAR-DEFAULT-EXCLUSIONS-v1.md) |



---



## Cross-references



| Source | Use |

|--------|-----|

| [shared/external-access-patterns/](../external-access-patterns/README.md) | Per-channel human gates |

| [projects/ocpilot/freeze/site-001-pre-runtime-bridge/](../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/) | Lessons and blockers |

| [projects/ocpilot/OPERATIONAL-INDEX.md](../../projects/ocpilot/OPERATIONAL-INDEX.md) | OCPilot Run 5 pause note |

| [projects/ear-runtime/](../../projects/ear-runtime/OPERATIONAL-INDEX.md) | EAR Runtime Program — engineering home, state, roadmap |
| [AGENTS.md](../../AGENTS.md) | HITL, REPORT, SAFE UNKNOWN |



---



## Reports



Operational work that touches external systems ends with `# REPORT — …` per MARS discipline. EAR foundation task report: operator chat / task closeout — not stored in this folder by default.

