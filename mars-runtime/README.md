# `mars-runtime`

**MARS — runtime entry (directory root)**

## Purpose

Reserved for the **DevOps / Runtime** concerns of MARS: process model, workers, schedulers, queues, deployment topology, environment wiring — as **planned** in the target architecture (see `web-gpt-sources/02_architecture.md`). This folder is the **structural** anchor for “where the running system would live” once implementation begins.

## Relation to MARS architecture

Maps to the **DevOps / Runtime** layer: runtime processes, jobs, and operational shell around the other layers. It does **not** by itself implement orchestration (that is **Control Plane**) or business agents (**Agent** layer); it hosts execution and ops.

## Status

**Planned** — no executable runtime, workers, or deployment assets exist in this repository in this phase. Only this placeholder layout.

## See also

- `architecture-map.md` — how repository folders align with documented MARS layers.
