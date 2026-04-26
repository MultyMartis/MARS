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

**Phase 1 — Web-GPT source pack / documentation base**

Focus: consolidate the imported documentation set, align naming and structure with MARS, and establish this repo as the single local source of truth before implementation work.

## Repository layout

| Path | Role |
|------|------|
| `web-gpt-sources/` | Numbered topic Markdown files (system, architecture, core, agents, …) |

---

*Last updated: repository initialization checkpoint.*
