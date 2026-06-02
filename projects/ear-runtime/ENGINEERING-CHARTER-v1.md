# EAR Runtime v1 Engineering Charter

**Type:** Human-approved engineering program charter — **authorizes planning**, **not** implementation  
**Date:** 2026-06-02  
**Program:** EAR Runtime Program v1  
**Status:** **APPROVED** — Runtime Engineering **STARTED**

---

## Purpose

This document is the **official start** of the EAR Runtime Engineering Program. It authorizes runtime engineering discipline, backlog planning, and structure definition under `projects/ear-runtime/`.

**This charter does NOT authorize:**

- Connector implementation
- Runtime code or scripts
- Library or framework selection
- Live SFTP or connected access
- PILOT-001 Execution Authorization

Implementation requires separate readiness review and charter per backlog item.

---

## Prerequisites (satisfied)

| Prerequisite | Status | Reference |
|--------------|--------|-----------|
| EAR Architecture Program | **COMPLETE** (frozen 2026-06-01) | [shared/external-access-runtime/](../../shared/external-access-runtime/) |
| Runtime Transition Freeze | **YES** | [freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/) |
| Runtime project foundation | **YES** | [DECISION-EAR-RUNTIME-PLACEMENT-v1.md](DECISION-EAR-RUNTIME-PLACEMENT-v1.md) |
| Placement decision | **APPROVED** | `projects/ear-runtime/` |

---

## Runtime Mission

EAR Runtime executes **approved acquisition workflows** defined by frozen EAR Architecture. The runtime layer turns normative contracts into human-operated helpers that produce inspectable artefacts for downstream consumers.

| Mission area | Description |
|--------------|-------------|
| **Execute approved acquisition workflows** | Mode 2 Connected Read-Only paths per architecture — starting with CON-L1-A / SFTP |
| **Generate evidence packages** | Assemble Evidence Packages from connector output — distinct from consumer snapshots |
| **Generate snapshots** | Build candidate Snapshot Level 1 packages from validated evidence |
| **Validate outputs** | Provide human-operated Validate assistants — checklists, structural checks, gate reminders |
| **Publish snapshots** | Apply Publish gate under HITL; produce consumer-visible immutable snapshot references |
| **Support EAR consumers** | Deliver published snapshots compatible with OCPilot intake (v1 reference consumer) |

**Constraint:** Runtime **must not exceed** approved EAR architecture. Normative behavior changes require **Architecture Amendment Charter** — not runtime engineering.

**First pilot target (planning only):** PILOT-001 — SITE-001 (Автосалон СИБКАР) — Connected Acquisition, Mode 2, SFTP Read-Only, Snapshot Level 1.

---

## Runtime Stack

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| **Primary language** | **Python** | SFTP, SSH, filesystem inventory, hashing, manifest generation, JSON, snapshot assembly, and CLI tooling align naturally with Python ecosystem |
| **Runtime style** | **CLI-first** | Human-operated helpers invoked explicitly by operator; no hidden services |
| **Execution model** | **Human-operated** | Every acquisition session requires operator initiation and HITL gates per architecture |
| **Mode** | **Read-only first** | Mode 2 read-only SFTP is v1 scope; write connectors and Mode 3 are forbidden without architecture amendment |

### Why Python (approved)

Python is selected because the v1 backlog centers on:

- SFTP and SSH client operations
- Filesystem traversal and inventory
- Content hashing and integrity checks
- JSON manifest and metadata generation
- Snapshot directory assembly
- Operator-facing CLI tooling

**No blocking contradiction** exists in repository evidence at charter approval.

### Explicit non-decisions (this charter)

| Not decided | Deferred to |
|-------------|-------------|
| Frameworks | Implementation readiness review per backlog item |
| Libraries (e.g. SFTP client) | R1 Implementation Readiness Review |
| Package layout details | [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) — responsibilities only |
| CI/CD or deployment | Future ops charter |

---

## In-scope backlog (planning authorized)

| ID | Name | Engineering status |
|----|------|-------------------|
| **R1** | SFTP Read-Only Connector | **PLANNED** — [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) |
| **R2** | Evidence Package Generator | **PLANNED** |
| **R3** | Snapshot Builder | **PLANNED** |
| **R4** | Snapshot Publisher | **PLANNED** |
| **R5** | Validation Helpers | **PLANNED** |

Authoritative acceptance criteria: [shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md)

---

## Engineering documents (this charter run)

| Document | Role |
|----------|------|
| [ENGINEERING-BOUNDARIES-v1.md](ENGINEERING-BOUNDARIES-v1.md) | What runtime owns and does not own |
| [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) | Operational principles for all runtime work |
| [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) | Proposed folder responsibilities |
| [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) | R1 planning charter |
| [STATE-TRANSITION-v1.md](STATE-TRANSITION-v1.md) | Engineering state transition record |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Honest program status |

---

## Relationship to foundation charter

[EAR-RUNTIME-CHARTER-v1.md](EAR-RUNTIME-CHARTER-v1.md) defines mission, consumers, and architecture relationships at **project foundation**. This **Engineering Charter** satisfies the gate named in [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) and marks the Runtime Program as **STARTED**.

---

## Approval

| Field | Value |
|-------|-------|
| **Charter** | EAR Runtime v1 Engineering Charter |
| **Approved** | 2026-06-02 |
| **Authorizes** | Runtime engineering program start; R1–R5 planning |
| **Does not authorize** | Implementation, live access, pilot execution |

---

## Truth statement

**No** runtime code, connector, library selection, or live access session exists at engineering charter approval. Program **STARTED** ≠ Implementation **STARTED**.
