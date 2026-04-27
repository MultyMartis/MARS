# `control-plane`

## Purpose

MARS **Control Plane** (orchestration): task decomposition, routing, dispatch, workflow run state, and handoff between agents — **documented** in `web-gpt-sources/02_architecture.md` as a target **Control Plane** layer.

## Control Plane v0 (contract)

This directory holds a **planned** contract slice (not an implementation):

| File | Content |
|------|--------|
| `contract.md` | v0 **purpose**, **responsibilities** / **non-responsibilities**, **input** / **output** contracts, **required signals**, relation to **Main Brain** (legacy). |
| `components.md` | v0 **logical** components: Orchestrator/Supervisor, Planner, Router, Dispatcher, State Manager, Handoff Manager. |

**Status:** **Planned** — v0 is a design contract; there is no runtime, agents, or registries here yet. Do not treat these files as proof of shipped code.

## Relation to MARS architecture

Implements the **Control Plane** *role* in the documented stack: consumes **Interface** and policy inputs, coordinates **Agent** / **Workflow** / **Model** / **Tool** layers, consults **Security** and **Memory** per architecture — as **documented** and when implemented, not as if already present in-repo.

## Legacy

**Main Brain** in legacy docs is described as a conceptual predecessor; v0 is the **normalized** successor **role** — see `contract.md` §7.

## See also

- `../mars-runtime/architecture-map.md` — repository layout vs layers.
