# `models`

## Purpose

Reserved for **LLM and embedding** integration: providers, routing, adapters, fallbacks, rerank/embeddings, as described in the **Model Layer** in `web-gpt-sources/02_architecture.md` and `07_tools_models.md`.

## Relation to MARS architecture

Implements the **Model Layer**. Called by the **Control Plane** and **Agents**; may support RAG and retrieval **when** those features exist per documentation (cross-layer).

## Status

**Planned** — no model adapters or provider code in this repository in this phase.
