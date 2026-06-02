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
| **EAR Runtime Program** | **STARTED** | **This project** — [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) |

**Placement decision:** [DECISION-EAR-RUNTIME-PLACEMENT-v1.md](DECISION-EAR-RUNTIME-PLACEMENT-v1.md)  
**Foundation freeze:** [freeze/FOUNDATION-START-v1/](freeze/FOUNDATION-START-v1/)

---

## Current focus

| Field | Value |
|-------|-------|
| **Engineering Charter** | **DONE** — [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) |
| **Program** | **STARTED** |
| **Implementation** | **AUTHORIZED FOR R1 ONLY** (human approval pending) |
| **R1 Implementation Readiness Review** | **DONE** — [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md) (**CONDITIONAL GO**) |
| **R1 Implementation Charter** | **DONE** — [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md) |
| **R1.1 Runtime Skeleton** | **DONE** — [R1.1-FOUNDATION-STATE-v1.md](R1.1-FOUNDATION-STATE-v1.md) |
| **R1.2 Config Input Model** | **DONE** — [R1.2-CONFIG-INPUT-MODEL-v1.md](R1.2-CONFIG-INPUT-MODEL-v1.md) |
| **Current focus** | **R1.3 SFTP Connection Test Mode** — [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md) |
| **Next** | **R1.3 SFTP Connection Test Mode** |

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
| 15 | [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md) | Safe task breakdown R1.1–R1.10 |
| 16 | [R1-TEST-STRATEGY-v1.md](R1-TEST-STRATEGY-v1.md) | Non-production test plan |
| 17 | [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) | Human approval gate |
| 18 | [R1-PHASE-DECISION-v1.md](R1-PHASE-DECISION-v1.md) | R1 readiness phase decision record |
| 19 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Honest status |
| 20 | [STATE-TRANSITION-v1.md](STATE-TRANSITION-v1.md) | Engineering state transition record |

**Before any implementation:** read architecture freeze [shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/) and [EAR-RUNTIME-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BOUNDARY-v1.md).

---

## Folder map

| Path | Role |
|------|------|
| [runtime/](runtime/) | R1.2 — `cli.py`, `shared/config_loader.py`, `configs/`; connector code **NOT STARTED** |
| [docs/](docs/) | Runtime-specific engineering notes (not architecture amendments) |
| [pilots/](pilots/) | Runtime execution pilots and run artefacts (when chartered) |
| [freeze/](freeze/) | Runtime program freeze markers |

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

## Operational triggers

| Trigger | Action |
|---------|--------|
| Start Runtime Program engineering | **DONE** — [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) |
| R1 implementation readiness | **DONE** — [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md) (**CONDITIONAL GO**) |
| R1 Implementation Charter | **DONE** — [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md) |
| R1.1 Runtime Skeleton | **DONE** — [R1.1-FOUNDATION-STATE-v1.md](R1.1-FOUNDATION-STATE-v1.md) |
| R1.2 Config Input Model | **DONE** — [R1.2-CONFIG-INPUT-MODEL-v1.md](R1.2-CONFIG-INPUT-MODEL-v1.md); next: **R1.3** |
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
