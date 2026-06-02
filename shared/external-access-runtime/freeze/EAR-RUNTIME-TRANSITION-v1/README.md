# EAR Runtime Transition Freeze v1

**Type:** Architecture program closeout — transition planning only  
**Date:** 2026-06-01  
**Status:** **FROZEN** — EAR Architecture Program **COMPLETE**

---

## Purpose

This folder records the **EAR Runtime Transition Freeze**: the point at which EAR architectural development stops and **EAR Runtime v1 Engineering** becomes the primary program.

**This folder does not contain:** runtime code, connectors, scripts, SFTP logic, execution plans with commands, or live access procedures.

---

## Freeze declaration

| Program | Status | Primary objective |
|---------|--------|-------------------|
| **EAR Architecture Program** | **COMPLETE** | Document acquisition layer, snapshot contract, connectors (design), tracks, pilot governance |
| **EAR Runtime Program** | **NOT STARTED** | Engineering home: [projects/ear-runtime/](../../../../projects/ear-runtime/) — implement Mode 2 helpers per engineering charter — **no** implementation in this freeze |

Further **architecture expansion** is **not** the default next step. Changes to frozen architecture require an explicit **Architecture Amendment Charter** (human).

---

## Package contents

| Document | Role |
|----------|------|
| [EAR-STATE-SUMMARY-v1.md](EAR-STATE-SUMMARY-v1.md) | One-page current state — readiness, pilot, deferred items |
| [EAR-ARCHITECTURE-COMPLETE-v1.md](EAR-ARCHITECTURE-COMPLETE-v1.md) | Final architecture inventory — complete vs deferred |
| [EAR-LESSONS-LEARNED-v1.md](EAR-LESSONS-LEARNED-v1.md) | Architecture-phase lessons (no execution lessons) |
| [EAR-RUNTIME-HANDOFF-v1.md](EAR-RUNTIME-HANDOFF-v1.md) | What Runtime v1 receives — inputs and boundaries |
| [EAR-NEXT-STAGE-v1.md](EAR-NEXT-STAGE-v1.md) | Recommended entry into Runtime Engineering |

---

## Related artifacts (outside this folder)

| Artifact | Location |
|----------|----------|
| Runtime engineering backlog | [../../EAR-RUNTIME-BACKLOG-v1.md](../../EAR-RUNTIME-BACKLOG-v1.md) |
| Default acquisition exclusions | [../../EAR-DEFAULT-EXCLUSIONS-v1.md](../../EAR-DEFAULT-EXCLUSIONS-v1.md) |
| Architecture vs runtime boundary | [../../EAR-RUNTIME-BOUNDARY-v1.md](../../EAR-RUNTIME-BOUNDARY-v1.md) |
| Phase closeout (Phases 1–6) | [../../EAR-PHASE-CLOSEOUT-v1.md](../../EAR-PHASE-CLOSEOUT-v1.md) |
| Operational navigation | [../../OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) |
| **EAR Runtime engineering project** | [../../../../projects/ear-runtime/](../../../../projects/ear-runtime/) · [DECISION-EAR-RUNTIME-PLACEMENT-v1.md](../../../../projects/ear-runtime/DECISION-EAR-RUNTIME-PLACEMENT-v1.md) · [FOUNDATION-START-v1](../../../../projects/ear-runtime/freeze/FOUNDATION-START-v1/) |
| PILOT-001 package | [../../pilots/PILOT-001-SITE-001-SFTP-READONLY/](../../pilots/PILOT-001-SITE-001-SFTP-READONLY/) |

---

## Truth statement

- EAR architecture is **documented** and considered **mature** for Mode 2 Connected Read-Only v1.
- **No** EAR runtime, connector implementation, or SFTP session exists in the MARS repository as of this freeze.
- PILOT-001 is **authorized** at charter level; **Execution is NOT AUTHORIZED**.
- Runtime Readiness assessment: **CONDITIONAL GO** (documentation) — see [EAR-RUNTIME-READINESS-ASSESSMENT-v1.md](../../EAR-RUNTIME-READINESS-ASSESSMENT-v1.md).
