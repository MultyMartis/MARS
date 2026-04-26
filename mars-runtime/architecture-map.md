# MARS — repository map → architecture layers

**Status:** **Planned** layout for future code. Documented target layers are in `web-gpt-sources/02_architecture.md` and related files.

| Repository folder | MARS layer (as documented) |
|-------------------|----------------------------|
| `mars-runtime/` | **DevOps / Runtime** — executables, workers, schedulers, queues, deployment/ops (future) |
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
