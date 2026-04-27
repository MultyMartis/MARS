# `mars-runtime`

**MARS — runtime entry (directory root)**

## Purpose

Reserved for the **DevOps / Runtime** concerns of MARS: process model, workers, schedulers, queues, deployment topology, environment wiring — as **planned** in the target architecture (see `web-gpt-sources/02_architecture.md`). This folder is the **structural** anchor for “where the running system would live” once implementation begins.

## Relation to MARS architecture

Maps to the **DevOps / Runtime** layer: runtime processes, jobs, and operational shell around the other layers. It does **not** by itself implement orchestration (that is **Control Plane**) or business agents (**Agent** layer); it hosts execution and ops.

## Contracts vs implementation

- **Documentation** **contracts:** this folder now contains the Stage 8.5 and Stage 13 runtime-facing contract set (see links below). These files are **normative documentation**, not runtime code.
- **Runtime** **implementation:** **No** executable **runtime**, workers, deployment assets, queue/orchestrator services, or bridge **code** in this repository in **Phase 1** — per `AGENTS.md` and the master build map **planned-implementation** stance.

## Contract files in `mars-runtime/` (v0)

- `execution-bridge-v0.md` — Execution Bridge contract v0 (documentation only).
- `execution-queue-v0.md` — Execution Queue / Job System contract v0 (documentation only).
- `execution-orchestrator-v0.md` — Execution Orchestrator contract v0 (documentation only).
- `execution-context-v0.md` — Execution Context Model contract v0 (documentation only).
- `run-lifecycle-v0.md` — Run Lifecycle Model contract v0 (documentation only).
- `resource-quota-v0.md` — Resource / Concurrency Model contract v0 (documentation only).
- `architecture-map.md` — repository-folder mapping to documented MARS layers.

## Status note

- This folder is **documentation only** in Phase 1.
- No runtime implementation is claimed by the presence of these contracts.
