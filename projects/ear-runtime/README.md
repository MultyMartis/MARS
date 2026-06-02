# EAR Runtime — Engineering Project

**Status:** **documented** project placement and charter — **R1 foundation skeleton + config loader only**; connector **not started**.  
**Lane:** B — External Systems / Acquisition Engineering  
**Program:** EAR Runtime Program v1 — **STARTED** (see [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md))  
**Registry:** `ear-runtime` — [registry/project-registry.md](../../registry/project-registry.md)

---

## What this project is

**EAR Runtime** is the **engineering home** for Mode 2 acquisition helpers: connectors, evidence assembly, snapshot build/publish tooling, and validation assistants. It is a **separate MARS project** from the frozen EAR Architecture tree.

| Layer | Location | Role |
|-------|----------|------|
| **EAR Architecture Program** | [shared/external-access-runtime/](../../shared/external-access-runtime/) | Normative contracts, workflows, pilot governance — **COMPLETE** (frozen) |
| **EAR Runtime Program** | **This folder** (`projects/ear-runtime/`) | Implementation backlog, engineering state, runtime pilots, future code |
| **Consumers** | e.g. [projects/ocpilot/](../ocpilot/) | Analysis and operations — **not** EAR Runtime |

---

## Program transition

```
EAR Architecture Program (COMPLETE)
        │
        │  freeze: EAR-RUNTIME-TRANSITION-v1
        ▼
EAR Runtime Program (NOT STARTED → chartered engineering)
        │
        │  when authorized: implements R1–R5
        ▼
Published Snapshots → OCPilot / future WPilot / others
```

**Architecture freeze:** [shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/)  
**Placement decision:** [DECISION-EAR-RUNTIME-PLACEMENT-v1.md](DECISION-EAR-RUNTIME-PLACEMENT-v1.md)

---

## Ownership boundaries

| Owner | Owns |
|-------|------|
| **EAR Architecture** (`shared/external-access-runtime/`) | What the system **must** do — contracts, gates, tracks, connector **design**, pilot charters at architecture level |
| **EAR Runtime** (this project) | **How** chartered helpers implement those contracts — code, CLIs, run logs, runtime pilot execution artefacts |
| **OCPilot / WPilot / Factory** | Consumer analysis, site-specific workflows, deployment — **not** acquisition mechanics |
| **Operator / human** | Credentials, Execution Authorization, Publish sign-off, charter approval |

Runtime **must conform** to architecture; it **must not** silently amend normative design in README or code comments.

---

## Start here

| Document | Purpose |
|----------|---------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation hub for Runtime Program |
| [EAR-RUNTIME-CHARTER-v1.md](EAR-RUNTIME-CHARTER-v1.md) | Mission, consumers, relationships |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Current program status (honest) |
| [EAR-RUNTIME-ROADMAP-v1.md](EAR-RUNTIME-ROADMAP-v1.md) | R1–R5 sequencing |
| [EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md) | Index to authoritative backlog |

---

## Truth statement

- **No** SFTP connector, evidence generator, snapshot builder, publisher, or validation helper **production implementation** is claimed until explicitly recorded in [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) with charter reference. R1.1 skeleton and R1.2 config loader are **foundation-only** — not live acquisition.
- Backlog items **R1–R5** describe engineering **targets**; existence of markdown ≠ runtime exists.
- PILOT-001 architecture package remains under [shared/external-access-runtime/pilots/](../../shared/external-access-runtime/pilots/); runtime execution pilots may be mirrored or extended under `projects/ear-runtime/pilots/` when chartered.

---

## Cross-references

| Source | Use |
|--------|-----|
| [shared/external-access-runtime/OPERATIONAL-INDEX.md](../../shared/external-access-runtime/OPERATIONAL-INDEX.md) | Architecture navigation |
| [shared/external-access-runtime/EAR-RUNTIME-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BOUNDARY-v1.md) | Architecture vs runtime layer |
| [AGENTS.md](../../AGENTS.md) | MARS agent discipline, SAFE UNKNOWN, REPORT |
