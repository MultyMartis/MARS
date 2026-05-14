# MARS — repository map → architecture layers

**Status:** **documented target mapping** — this file is a **glossary-style** map from **repository folders** to **architecture layers** described in `web-gpt-sources/02_architecture.md` and related docs. It is **not** an implementation inventory, **not** a shipped topology, and **not** authoritative proof that each folder contains runnable code.

**Experimental R1 (narrow):** `mars-runtime/` also holds **minimal** JavaScript experiments (see `README.md` under this folder). That code is **partial**, **non-production**, and **does not** implement the **Control Plane**, autonomous **orchestration**, or a **MARS process manager**. Treat it as **R1 bridge/adapter demos** aligned with contracts — **not** as the **MARS runtime** product.

**Surrounding operational reality (Phase 1):** Day-to-day work on this repository follows the **documentation-first** posture in `../AGENTS.md` and `../governance/execution-model.md` (human-controlled editor/shell). **External** systems (e.g. n8n, SaaS) may execute workflows **outside** this tree; they are **not** defined or guaranteed by this map.

| Repository folder | MARS layer (as documented) |
|-------------------|----------------------------|
| `mars-runtime/` | **DevOps / Runtime** — **in-tree today:** v0 **contracts** (markdown) + **R1** manual demo scripts — **not** shipped workers/queues/schedulers (those remain **documented target** only until separately evidenced); see folder `README.md` |
| `control-plane/` | **Control Plane** — orchestration, routing, workflow state, handoff |
| `agents/` | **Agent Layer** — agent implementations, registries (future) |
| `workflows/` | **Workflow Layer** — flows, graphs, HITL, playbooks (future) |
| `memory/` | **Memory Layer** — short/long-term memory, session context (future) |
| `tools/` | **Tool Layer** — tools, MCP, sandboxes, permissions (future) |
| `models/` | **Model Layer** — LLM providers, routing, adapters, embeddings (future) |
| `storage/` | **Storage Layer** — DB, vectors, files, audit/state stores (future) |
| `interfaces/` | **Interface Layer** — API, chat, CLI, webhooks, IDE channels (future) |
| `observability/` | **Observability Layer** — traces, logs, metrics, run history (future) |
| `evaluation/` | **Evaluation Layer** — evals, golden sets, scenario tests (future) |
| `security/` | **Security / Guardrails** — policy, validation, secrets handling, sandbox (future) |

### Notes (documented elsewhere, not separate top-level folders here)

- **Identity** policies tie into **Security** and **Control Plane**; no `identity/` folder in this initial layout.
- **Knowledge / RAG** in the documentation is a cross-cutting concern: planned bindings typically involve **Model**, **Memory**, and **Storage**; see `web-gpt-sources/08_storage_rag.md` and related docs.
- **`projects/`** (repository root) holds **project documentation packs** for systems **outside** MARS core runtime — e.g. [**MARS Website Factory**](../projects/mars-website-factory/README.md) (**strategic planned** under `projects/mars-website-factory/`): **documentation-first** multi-agent website production direction (**not** runtime-ready automation). [**MetaBOT — SEO Content Agent**](../projects/metabot-seo-content-agent/README.md) (**canonical** under `projects/metabot-seo-content-agent/`): **external multi-workflow AI system** (n8n owns execution); MARS stores architecture/contracts/knowledge only — see [integration-boundary.md](../projects/metabot-seo-content-agent/integration-boundary.md). Early spec / bridge material may remain under `projects/seo-content-agent/` as **legacy** (see that folder’s README).
