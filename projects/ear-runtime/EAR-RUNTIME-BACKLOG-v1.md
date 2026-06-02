# EAR Runtime Backlog v1 — Project Index

**Type:** Runtime project backlog index — **references** authoritative definitions  
**Date:** 2026-06-02  
**Program:** EAR Runtime Program v1 — **NOT STARTED**

---

## Ownership (do not duplicate)

| Role | Location |
|------|----------|
| **Authoritative backlog definitions** | [shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) |
| **Architecture boundary** | [shared/external-access-runtime/EAR-RUNTIME-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BOUNDARY-v1.md) |
| **Transition freeze** | [shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/) |
| **Engineering tracking & state** | **This project** — [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md), [EAR-RUNTIME-ROADMAP-v1.md](EAR-RUNTIME-ROADMAP-v1.md) |

**Rule:** Amend acceptance criteria, dependencies, and normative "what to build" in the **architecture backlog** only. This file tracks **runtime program status** and links — not a second source of truth.

---

## Dependency overview

Same as architecture backlog (reference):

```
R1 (SFTP Read-Only Connector)
    ↓
R2 (Evidence Package Generator)
    ↓
R3 (Snapshot Builder) ──→ R4 (Snapshot Publisher)
    ↓
R5 (Validation Helpers) — may overlap R3/R4
```

Full dependency notes: [architecture backlog § Dependency overview](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md#dependency-overview)

---

## Items (index)

| ID | Name | Authoritative section |
|----|------|------------------------|
| **R1** | First SFTP Read-Only Connector | [§ R1](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md#r1--first-sftp-read-only-connector) |
| **R2** | Evidence Package Generator | [§ R2](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md#r2--evidence-package-generator) |
| **R3** | Snapshot Builder | [§ R3](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md#r3--snapshot-builder) |
| **R4** | Snapshot Publisher | [§ R4](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md#r4--snapshot-publisher) |
| **R5** | Validation Helpers | [§ R5](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md#r5--validation-helpers) |

---

## Runtime project status columns (engineering)

Update these in [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) when charter/implementation progresses:

| ID | Runtime status (foundation) | Implementation location |
|----|----------------------------|-------------------------|
| R1 | **NOT STARTED** | `runtime/` (future) |
| R2 | **NOT STARTED** | `runtime/` (future) |
| R3 | **NOT STARTED** | `runtime/` (future) |
| R4 | **NOT STARTED** | `runtime/` (future) |
| R5 | **NOT STARTED** | `runtime/` (future) |

---

## Backlog governance (inherited)

| Rule | Source |
|------|--------|
| Charter required before implementation | [architecture backlog § Backlog governance](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md#backlog-governance) |
| Architecture amendments out of backlog | Architecture Amendment Charter |
| Pilot execution | [PILOT-GOVERNANCE-v1.md](../../shared/external-access-runtime/PILOT-GOVERNANCE-v1.md) |
| Status honesty | Backlog existence ≠ runtime exists |

---

## Traceability

Architecture traceability table: [architecture backlog § Traceability](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md#traceability)

When R1+ implementation exists, add a **runtime traceability** subsection to [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) linking modules → contracts (not duplicated here).

---

## Truth statement

This index was created at **Runtime project foundation**. **No** backlog item is implemented.
