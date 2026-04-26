# `storage`

## Purpose

Reserved for **persistence**: operational DBs, vector stores, file/object storage, audit and state — the **Storage Layer** in `web-gpt-sources/02_architecture.md` and `08_storage_rag.md`. Knowledge/RAG in the docs often **uses** this layer together with **Model** and **Memory**; a dedicated top-level RAG module is not created in this initial map (see `mars-runtime/architecture-map.md`).

## Relation to MARS architecture

Implements the **Storage Layer** via **adapters** in the target design. Does **not** by itself represent the full “Knowledge / RAG” feature area until such code exists.

## Status

**Planned** — no adapters or databases implemented here yet.
