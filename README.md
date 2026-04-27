# MARS

**Multi-Agent Runtime System**

This directory is the **main local working copy** of the MARS project: design notes, the Phase 1 documentation pack, and future source code are expected to live here.

## What this repository contains (by status)

### Documented architecture

- Design and system documentation is maintained as Markdown under [`web-gpt-sources/`](web-gpt-sources/).  
- **Status:** **documented** — these files describe the intended shape of MARS (layers, components, security, observability, interfaces, rules, migration, roadmap). They are **documentation**, not a guarantee that any particular piece is implemented.

### Planned implementation

- A runnable multi-agent runtime, services, agents, tools, storage integrations, and deployment assets are **planned** for later phases.  
- **Status:** **planned** — this repository does **not** yet contain application/runtime code for MARS; Phase 1 is documentation-only.

### Legacy / imported material

- The `web-gpt-sources/` pack originated as a **Web-GPT** documentation import: it is **legacy imported** reference material used to bootstrap the written architecture. Treat it as input to the design; it may be revised, split, or replaced as MARS evolves.

## Current phase

**Phase 1 — documentation-first; Stages 0 through 8.5 complete**

- **Status:** Stages **0–8.5** **documentation** (including **Runtime Readiness** **P0** **contracts**) is **complete** in this repository.  
- **Next:** **Stage 9** (Tool registry / tool permissions) **per** `governance/master-build-map.md` — after any **project-agreed** **backup** of this tree.  
- **Implementation:** **No** **runnable** **MARS** **runtime**, services, or application code is evidenced here yet; **planned-implementation** remains **future** work per `AGENTS.md`.

## Repository layout

| Path | Role |
|------|------|
| `governance/` | Boundaries, execution/state/versioning models, capability map, **master build map** |
| `registry/` | **Project registry** and other registry-style anchors (`project-registry.md`) |
| `logs/` | **Lifecycle log** (documented lifecycle events, append-only discipline) |
| `control-plane/` | Control plane contract and components (documentation) |
| `agents/` | Agent registry, cards, factory/builder documentation |
| `workflows/` | Task contract, workflow standard, execution flow, failure model (MARS-native contracts) |
| `interfaces/` | Introspection, self-check, self-audit, self-describe, self-heal, recovery playbooks (v0 contracts) |
| `security/` | Security README and MARS-native security/threat/permissions contracts (documentation) |
| `tools/` | Tool layer placeholder and future tool-registry contracts |
| `models/` | Model layer placeholder and future provider-routing contracts |
| `storage/` | Storage / checkpoint / runtime-state **documentation** (contracts; no adapters) |
| `memory/` | Memory **documentation** and memory-write policy (contracts) |
| `observability/` | Observability placeholder and future contracts |
| `evaluation/` | Evaluation placeholder and future contracts |
| `mars-runtime/` | DevOps/runtime documentation (e.g. architecture map, **Execution Bridge v0**); **no** shipped runtime unless sources prove otherwise |
| `web-gpt-sources/` | Numbered topic Markdown files (system, architecture, core, agents, …) — **legacy imported** pack |

---

*Last updated: 2026-04-27 (Stages 0–8.5 documentation complete; Stage 9 next; no runtime implementation in-repo).*
