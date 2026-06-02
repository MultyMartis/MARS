# EAR Runtime Structure v1

**Type:** Proposed folder structure — responsibilities only  
**Date:** 2026-06-02  
**Charter:** [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md)  
**Status:** **PROPOSED** — no implementation

---

## Purpose

Define the proposed layout under `projects/ear-runtime/runtime/` for future implementation. This document describes **responsibilities only** — no code, no modules, no library choices.

---

## Top-level project layout

| Path | Role |
|------|------|
| `runtime/` | Future implementation root (connectors, builders, validators, publishers, shared) |
| `docs/` | Runtime-specific engineering notes — not architecture amendments |
| `pilots/` | Runtime execution pilots and run artefacts (when Execution authorized) |
| `freeze/` | Runtime program freeze markers |
| Project root `*.md` | Charters, state, roadmaps, operational index |

Architecture remains in `shared/external-access-runtime/`.

---

## Proposed `runtime/` structure

```
runtime/
├── connectors/       # R1 — connector execution
├── builders/         # R2, R3 — evidence and snapshot assembly
├── validators/       # R5 — validation helpers
├── publishers/       # R4 — snapshot publishing
└── shared/           # Cross-cutting utilities (logging, config binding, common types)
```

**At foundation:** `runtime/` contains only `.gitkeep` — structure is **not materialized** as subdirectories until implementation readiness review.

---

## Folder responsibilities

### `runtime/connectors/`

| Aspect | Responsibility |
|--------|----------------|
| **Owns** | Connector execution implementations per connector contract |
| **First item** | R1 — SFTP Read-Only Connector |
| **Inputs** | Connector Input per [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md) — operator-supplied, external credential resolution |
| **Outputs** | Raw acquisition artefacts, connector status, errors, warnings — input for builders |
| **Does not own** | Evidence Package assembly, snapshot build, publish, consumer logic |

### `runtime/builders/`

| Aspect | Responsibility |
|--------|----------------|
| **Owns** | Evidence Package generation (R2); candidate Snapshot assembly (R3) |
| **Inputs** | Connector output + acquisition metadata; validated evidence for snapshot build |
| **Outputs** | Evidence Package structure; candidate unpublished snapshot workspace |
| **Does not own** | Connector transport; publish gate; autonomous validation certification |

Sub-responsibility split (when implemented):

| Sub-area | Backlog |
|----------|---------|
| Evidence assembly | R2 |
| Snapshot assembly | R3 |

### `runtime/validators/`

| Aspect | Responsibility |
|--------|----------------|
| **Owns** | Human-operated Validate assistants (R5) |
| **Inputs** | Evidence Package and/or candidate snapshot |
| **Outputs** | Validate reports, gate checklist status, publish blockers |
| **Does not own** | Autonomous gate enforcement product; human Validate sign-off replacement |

### `runtime/publishers/`

| Aspect | Responsibility |
|--------|----------------|
| **Owns** | Snapshot publishing helpers (R4) |
| **Inputs** | Candidate snapshot + human Publish approval |
| **Outputs** | Published immutable snapshot reference; publish log |
| **Does not own** | OCPilot intake execution; consumer deployment |

### `runtime/shared/`

| Aspect | Responsibility |
|--------|----------------|
| **Owns** | Cross-cutting utilities used by multiple runtime areas |
| **Examples (future)** | Structured logging helpers, config binding interfaces, common metadata types, CLI entrypoint patterns |
| **Does not own** | Business logic belonging to a single backlog item; architecture contract definitions |

**Constraint:** `shared/` must not become a dumping ground — utilities require justification and minimal surface area.

---

## Dependency flow (logical)

```
connectors/  →  builders/ (evidence)  →  validators/  →  builders/ (snapshot)  →  validators/  →  publishers/
                     ↑                          ↑                                    ↑
                 shared/                    shared/                              shared/
```

R5 (validators) may run against evidence and/or candidate snapshot per architecture lifecycle.

---

## Explicit non-goals (structure)

| Not in structure | Reason |
|------------------|--------|
| `tests/` layout | Deferred to implementation readiness review |
| `scripts/` at project root | No scripts at charter approval |
| Credential vault module | Out of scope — external to runtime |
| Consumer adapters | Belongs to OCPilot/WPilot/Factory |
| Architecture docs mirror | Architecture stays in `shared/` |

---

## Truth statement

Proposed structure is a **planning artefact**. Subdirectories under `runtime/` do not exist except placeholder `.gitkeep`. No modules, packages, or entrypoints are defined.
