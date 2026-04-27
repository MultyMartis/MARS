# MARS — Execution Orchestrator v0

**Status:** documented — contract only. This document describes coordination responsibilities and boundaries. **No orchestrator implementation exists in-repo.**

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Role

The Execution Orchestrator is the coordination layer that aligns agents, workflows, tools, and model decisions across a run, without directly performing tool calls or serving as durable memory storage.

---

## 2. Responsibilities

| Responsibility | Description |
|----------------|-------------|
| Task dispatch | Dispatches execution-ready units through [execution-bridge-v0.md](execution-bridge-v0.md). |
| Job scheduling | Schedules and sequences jobs through [execution-queue-v0.md](execution-queue-v0.md). |
| State tracking | Tracks run/task progression via [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md). |
| Signal propagation | Preserves and propagates canonical signals across orchestration transitions. |

---

## 3. Boundaries (normative v0)

- The orchestrator **does not execute tools directly**.
- The orchestrator **does not store memory**.
- The orchestrator coordinates; execution and persistence are delegated to dedicated contract surfaces.

---

## 4. Relation to system layers

| Layer / artefact | Relation |
|------------------|----------|
| `control-plane` | Receives orchestration intent and policy/routing hooks from control-plane contracts. |
| [../workflows/workflow-v0.md](../workflows/workflow-v0.md) | Aligns run progression with documented workflow states and transitions. |
| [execution-bridge-v0.md](execution-bridge-v0.md) | Uses bridge as dispatch boundary to concrete executors. |
| Tool layer (`../tools/`) | Coordinates tool-related steps via contracts; does not invoke tools itself. |
| Model routing (`../models/model-routing-v0.md`) | Consumes model-routing outcomes as orchestration inputs. |

---

## 5. Explicit non-claims

- No executable orchestrator process, scheduler service, or runtime router is present in this repository for v0.
- No claim is made that orchestration behavior is currently enforced at runtime.

---

## 6. SAFE UNKNOWN

- Internal orchestration algorithm, queue fairness strategy, and scaling topology are unspecified.
- Deployment mode (single-process, distributed, serverless, etc.) is not fixed.
- Failover semantics and election/leadership behavior are not specified in v0.

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-28 | Execution Orchestrator v0 authored (documentation-only contract, no implementation claim). |

---

*End of Execution Orchestrator v0.*
