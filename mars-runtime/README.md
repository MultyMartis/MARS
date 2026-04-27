# `mars-runtime`

**MARS — runtime entry (directory root)**

## Purpose

Reserved for the **DevOps / Runtime** concerns of MARS: process model, workers, schedulers, queues, deployment topology, environment wiring — as **planned** in the target architecture (see `web-gpt-sources/02_architecture.md`). This folder is the **structural** anchor for “where the running system would live” once implementation begins.

## Relation to MARS architecture

Maps to the **DevOps / Runtime** layer: runtime processes, jobs, and operational shell around the other layers. It does **not** by itself implement orchestration (that is **Control Plane**) or business agents (**Agent** layer); it hosts execution and ops.

## Contracts vs implementation

- **Documentation** **contract:** [`execution-bridge-v0.md`](execution-bridge-v0.md) (**Execution** **Bridge** v0) is a **documented** contract in this folder (normative for **how** a bridge is described; **not** a claim of code). See also `architecture-map.md` for how repository paths map to documented MARS layers.
- **Runtime** **implementation:** **No** executable **runtime**, workers, deployment assets, or bridge **code** in this repository in **Phase 1** — per `AGENTS.md` and the master build map **planned-implementation** stance.

## See also

- `architecture-map.md` — how repository folders align with documented MARS layers.
- `execution-bridge-v0.md` — Execution Bridge contract v0 (documentation only).
