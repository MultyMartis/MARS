# EAR Runtime State

**Type:** Honest program status — update on charter or implementation milestones  
**Last updated:** 2026-06-02 (R1.2 Config Input Model — DONE)

---

## Summary

| Field | Value |
|-------|-------|
| **Program** | **STARTED** |
| **Implementation** | **AUTHORIZED FOR R1 ONLY** (pending human approval — [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md)) |
| **Runtime code** | **SKELETON ONLY** — [runtime/](runtime/) |
| **Runtime Skeleton** | **CREATED** (R1.1) |
| **R1.2 Config Input Model** | **DONE** |
| **Config loader** | **CREATED** |
| **Connector** | **NONE** |
| **Live access** | **FORBIDDEN** |
| **Implementation** | **FOUNDATION ONLY** |
| **Pilots executed** | **0** |
| **Architecture source** | [shared/external-access-runtime/](../../shared/external-access-runtime/) |
| **Runtime project** | [projects/ear-runtime/](.) |
| **Placement decision** | [DECISION-EAR-RUNTIME-PLACEMENT-v1.md](DECISION-EAR-RUNTIME-PLACEMENT-v1.md) |
| **Engineering Charter** | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) — **APPROVED** |

---

## Program gates

| Gate | Status | Notes |
|------|--------|-------|
| Architecture Program complete | **YES** | Frozen 2026-06-01 |
| Runtime Transition Freeze | **YES** | [freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/) |
| Runtime project foundation | **YES** | 2026-06-02 — this folder |
| **EAR Runtime v1 Engineering Charter** | **YES** | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) — 2026-06-02 |
| R1 Implementation Readiness Review | **YES** | [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md) — **CONDITIONAL GO** 2026-06-02 |
| R1 Implementation Charter | **YES** | [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md) — **IMPLEMENTATION CHARTERED** 2026-06-02; human approval pending |
| R1 Implementation human approval | **NO** | [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) |
| PILOT-001 Execution Authorization | **NO** | Architecture: Execution **NOT AUTHORIZED** |

**Program STARTED when:** human-approved Engineering Charter exists, references freeze, names ≥1 backlog item in scope, and this file is updated. **Satisfied 2026-06-02.**

---

## Backlog implementation state

| ID | Name | Status |
|----|------|--------|
| R1 | SFTP Read-Only Connector | **IMPLEMENTATION CHARTERED** — [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md); planning: [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) |
| R2 | Evidence Package Generator | **PLANNED** |
| R3 | Snapshot Builder | **PLANNED** |
| R4 | Snapshot Publisher | **PLANNED** |
| R5 | Validation Helpers | **PLANNED** |

**Implementation:** R1 **AUTHORIZED FOR R1 ONLY** — R1.1 skeleton **CREATED**; R1.2 config loader **CREATED**; connector code **NOT STARTED**. R2–R5: **NOT STARTED**.

---

## Pilots

| Pilot | Architecture package | Runtime execution |
|-------|---------------------|-------------------|
| PILOT-001 SITE-001 SFTP Read-Only | [shared/.../PILOT-001-SITE-001-SFTP-READONLY/](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/) | **NOT EXECUTED** |

Runtime pilot artefacts folder: [pilots/](pilots/) — empty at engineering charter approval.

---

## Folder readiness

| Path | Contents at engineering charter |
|------|----------------------------------|
| `runtime/` | **R1.2** — `cli.py` (skeleton + `--config`), `shared/config_loader.py`, `configs/` sample fixtures; see [R1.2-CONFIG-INPUT-MODEL-v1.md](R1.2-CONFIG-INPUT-MODEL-v1.md) |
| `docs/` | Empty (placeholder) |
| `pilots/` | Empty (`.gitkeep` only) |
| `freeze/FOUNDATION-START-v1/` | Foundation freeze marker |

---

## Engineering documents (charter run)

| Document | Status |
|----------|--------|
| [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) | **APPROVED** |
| [ENGINEERING-BOUNDARIES-v1.md](ENGINEERING-BOUNDARIES-v1.md) | Published |
| [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) | Published |
| [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) | Proposed |
| [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) | Planning only |
| [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md) | **DONE** — CONDITIONAL GO |
| [R1-IMPLEMENTATION-DECISIONS-v1.md](R1-IMPLEMENTATION-DECISIONS-v1.md) | Published |
| [R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md](R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md) | Published |
| [R1-PHASE-DECISION-v1.md](R1-PHASE-DECISION-v1.md) | Recorded |
| [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md) | **DONE** — IMPLEMENTATION CHARTERED |
| [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md) | Published |
| [R1-TEST-STRATEGY-v1.md](R1-TEST-STRATEGY-v1.md) | Published |
| [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) | **PENDING** human approval |
| [STATE-TRANSITION-v1.md](STATE-TRANSITION-v1.md) | Recorded |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-02 | Runtime project created; placement decision recorded; Program NOT STARTED |
| 2026-06-02 | EAR Runtime v1 Engineering Charter approved; Program **STARTED**; R1–R5 **PLANNED**; Implementation **NOT STARTED** |
| 2026-06-02 | R1 Implementation Readiness Review — **CONDITIONAL GO**; next gate R1 Implementation Charter |
| 2026-06-02 | R1 Implementation Charter — **IMPLEMENTATION CHARTERED**; Implementation **AUTHORIZED FOR R1 ONLY** (human approval pending); Runtime **NOT IMPLEMENTED** |
| 2026-06-02 | R1.1 Runtime Skeleton — **CREATED**; first runtime code (`cli.py` skeleton); Connector **NONE**; Implementation **FOUNDATION ONLY** |
| 2026-06-02 | R1.2 Config Input Model — **DONE**; config loader **CREATED**; sample config fixtures; Live access **FORBIDDEN**; Connector **NONE** |
