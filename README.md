# MARS

**Multi-Agent Runtime System**

This directory is the **main local working copy** of the MARS project: design notes, the Phase 1 documentation pack, **v0 contracts and minimal experimental R1** JavaScript under [`mars-runtime/`](mars-runtime/), and **future** broader implementation as phases progress. The repository remains **primarily documentation-first**; R1 is narrow and **not** a full production runtime (see **Planned implementation** below).

## What this repository contains (by status)

### Documented architecture

- Design and system documentation is maintained as Markdown under [`web-gpt-sources/`](web-gpt-sources/).  
- **Status:** **documented** — these files describe the intended shape of MARS (layers, components, security, observability, interfaces, rules, migration, roadmap). They are **documentation**, not a guarantee that any particular piece is implemented.

### Planned implementation

- A production-grade multi-agent runtime, services, agents, tools, storage integrations, and deployment assets are **planned** for later phases.  
- **Status:** **planned** for the full system — this repository is **primarily documentation-first** in Phase 1. It also contains **minimal experimental R1** JavaScript under [`mars-runtime/`](mars-runtime/) that demonstrates a **narrow** task → bridge → adapter → webhook flow. R1 is **not** a full MARS runtime, **not** production-ready, and does **not** imply that the complete planned implementation exists in-tree.

### Legacy / imported material

- The `web-gpt-sources/` pack originated as a **Web-GPT** documentation import: it is **legacy imported** reference material used to bootstrap the written architecture. Treat it as input to the design; it may be revised, split, or replaced as MARS evolves.

## Current phase

**Phase 1 — documentation-first; Stages 0 through 8.5 complete**

- **Status:** Stages **0–8.5** **documentation** (including **Runtime Readiness** **P0** **contracts**) is **complete** in this repository.  
- **Next:** **Stage 9** (Tool registry / tool permissions) **per** `governance/master-build-map.md` — after any **project-agreed** **backup** of this tree.  
- **Implementation:** There is **no** full production **MARS** runtime, services stack, or application platform evidenced here. **Minimal R1** experimental scripts under `mars-runtime/` prove only that **narrow** integration path; production orchestration, queues, concurrency, memory, and model routing remain **external** or **planned**. **Planned-implementation** for the **complete** system remains **future** work per `AGENTS.md`.

## Repository layout

| Path | Role |
|------|------|
| `governance/` | Boundaries, execution/state/versioning models, capability map, **master build map**; parallel chat lanes ([`governance/parallel-cursor-chat-work-mode-v0.md`](governance/parallel-cursor-chat-work-mode-v0.md)) |
| `registry/` | **Project registry** and other registry-style anchors (`project-registry.md`) |
| `projects/` | **Project documentation packs** — e.g. `projects/mars-website-factory/` (**strategic planned** — multi-agent **documentation-first** website production system; **not** runtime-ready); `projects/metabot-seo-content-agent/` (**canonical** — **MetaBOT** SEO Content Agent, **external multi-workflow AI system**, n8n runtime; not a simple tool adapter); `projects/seo-content-agent/` (**legacy** — early spec / bridge; do not extend) |
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
| `mars-runtime/` | v0 **architecture contracts** (e.g. architecture map, **Execution Bridge v0**) **and** **minimal experimental R1** JavaScript (narrow task → bridge → adapter → webhook demo; **not** a full production runtime) |
| `web-gpt-sources/` | Numbered topic Markdown files (system, architecture, core, agents, …) — **legacy imported** pack |

---

*Last updated: 2026-05-11 (`projects/mars-website-factory/` — **strategic planned** Website Factory doc pack (**document-first**; **not** runtime-ready); **Site Type Registry v0** and **Block Registry v0** live as Markdown in that pack; `projects/metabot-seo-content-agent/` is the **canonical** MetaBOT SEO Content Agent doc pack; `projects/seo-content-agent/` is **legacy**; Stages 0–8.5 documentation complete; Stage 9 next per `governance/master-build-map.md`; **minimal R1** experiments under `mars-runtime/` only — **no** full MARS production runtime in-repo).*
