# `mars-runtime`

**MARS — runtime entry (directory root)**

## Purpose

Reserved for the **DevOps / Runtime** concerns of MARS: process model, workers, schedulers, queues, deployment topology, environment wiring — as **planned** in the target architecture (see `web-gpt-sources/02_architecture.md`). This folder is the **structural** anchor for “where the running system would live” at full maturity.

**Today**, `mars-runtime/` holds **both** the **v0 architecture contracts** (Stage 8.5 / Stage 13-facing markdown) **and** **minimal experimental R1** JavaScript (narrow demos under `adapters/`, `runtime/`). R1 entrypoints are **human-invoked** only (manual `node …`); adapters call **operator-configured external** URLs (e.g. your n8n webhook), not services defined or hosted by this repository. That R1 code does **not** constitute a shipped production runtime, **does not** implement the **control plane** or **autonomous orchestration**, and **does not** replace contract-only folders (`control-plane/`, `workflows/`, …) with executable equivalents; a complete queue/orchestrator-backed system remains **planned** (see **Contracts vs implementation** below). Folder→layer **narrative** (non-authoritative): `architecture-map.md`.

## Relation to MARS architecture

Maps to the **DevOps / Runtime** layer: at documented maturity, runtime processes, jobs, and operational shell around the other layers. It does **not** by itself implement orchestration (that is **Control Plane**) or business agents (**Agent** layer). **Today**, R1 does **not** provide a long-running host, scheduler, or service — only optional sketch scripts alongside the markdown contracts.

## Contracts vs implementation

- **Documentation contracts:** this folder contains the Stage 8.5 and Stage 13 runtime-facing contract set (see links below). These files are **normative documentation**, not executable product runtime.
- **Minimal R1 experimental code:** the same folder also holds **narrow** JavaScript experiments (e.g. under `adapters/`, `runtime/`) that exercise a **task → bridge → adapter → webhook** path. R1 is **limited**: it does **not** implement a full queue, orchestrator, concurrency manager, memory subsystem, or model routing layer. **Do not** treat R1 as a **production** MARS runtime.
- **Full runtime:** a complete multi-agent runtime, workers, deployment assets, and production-grade queue/orchestrator services remain **planned** / **out-of-scope** for what R1 proves — per `AGENTS.md` and the master build map **planned-implementation** stance for the **whole** system.

## Contract files in `mars-runtime/` (v0)

- `execution-bridge-v0.md` — Execution Bridge contract v0 (documentation only).
- `execution-queue-v0.md` — Execution Queue / Job System contract v0 (documentation only).
- `execution-orchestrator-v0.md` — Execution Orchestrator contract v0 (documentation only).
- `execution-context-v0.md` — Execution Context Model contract v0 (documentation only).
- `run-lifecycle-v0.md` — Run Lifecycle Model contract v0 (documentation only).
- `resource-quota-v0.md` — Resource / Concurrency Model contract v0 (documentation only).
- `environment-model-v0.md` — Environment separation model (local/staging/production), documentation only.
- `configuration-model-v0.md` — Runtime configuration model by config domain, documentation only.
- `secrets-management-v0.md` — Secrets/credentials handling posture, documentation only.
- `integration-surfaces-v0.md` — Integration surface model and bridge-only routing rule, documentation only.
- `deployment-model-v0.md` — Conceptual deployment layers (control/runtime/storage), documentation only.
- `architecture-map.md` — repository-folder mapping to documented MARS layers.

## Status note

- Phase 1 remains **documentation-first** for MARS as a product: contracts here are the **primary** in-tree artefacts; R1 scripts are **experimental** and **non-production**.
- The v0 contracts do **not** by themselves claim a shipped runtime; the **minimal R1** code does **not** replace or complete the **planned** full runtime (see above).
