# `models`

## Purpose

Reserved for **LLM and embedding** integration: providers, routing, adapters, fallbacks, rerank/embeddings, as described in the **Model Layer** in `web-gpt-sources/02_architecture.md` and `07_tools_models.md`.

## Relation to MARS architecture

Implements the **Model Layer** (documentation). Called by the **Control Plane** and **Agents**; RAG and retrieval semantics **as defined in** [../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md) (cross-layer).

## Model Layer v0 contracts (Stage 10)

| Document | Role |
|----------|------|
| [model-registry-v0.md](model-registry-v0.md) | Registry **fields**, **status** lifecycle, **planned-only** example rows (OpenRouter, OpenAI-compatible, local placeholder). |
| [model-policy-v0.md](model-policy-v0.md) | Task → model rules, risk tiers, PII, **no default unrestricted model**, cross-refs to security / memory / risk register. |
| [model-routing-v0.md](model-routing-v0.md) | Control-plane **routing inputs/outputs**, fallback rules (**documentation**; no implementation claim). |
| [context-budget-policy-v0.md](context-budget-policy-v0.md) | What may / must not enter **context**; budget dimensions; memory / RAG ([rag-architecture-v0.md](../memory/rag-architecture-v0.md)) / introspection relations. |
| [cost-token-budget-v0.md](cost-token-budget-v0.md) | Per-run / per-project **token** and **cost** budget **fields** and **outcomes** (`ALLOW`, `WARN`, `DENY`, **NEED HUMAN APPROVAL**). |

## Core dependencies (SoT)

This Model Layer relies on:

- [../security/permissions-v0.md](../security/permissions-v0.md)
- [../security/threat-model-v0.md](../security/threat-model-v0.md)
- [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md)
- [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md)
- [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md)

## Status

**Documentation only** — Stage **10** **partial-docs**: Model Layer **v0** markdown contracts exist under this folder; **no** provider wiring, **no** API keys, **no** SDKs, **no** runtime router or adapter **implementation** is evidenced in this repository ([../AGENTS.md](../AGENTS.md)).

**Not in scope yet:** live provider adapters, executable routing engines, secrets/config handling, cost telemetry pipelines (**planned-implementation** / **SAFE UNKNOWN** until a later stage evidences them).
