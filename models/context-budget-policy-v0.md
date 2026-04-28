# MARS — Context Budget Policy v0

**Status:** **documentation only** — rules for **what** may enter an LLM **context** and **how** to **prioritise** and **cap** sources under token and risk constraints. **No** tokenizer, **no** context builder implementation in this repository phase ([../AGENTS.md](../AGENTS.md)).

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- Prevent **unbounded** context growth that drives **cost**, **latency**, and **exfiltration** / **injection** surface ([../governance/risk-register.md](../governance/risk-register.md)).
- Align **prompt assembly** with **memory** governance and RAG **as defined in** [../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md).
- Give **Self-Describe / Introspection** a clear story: which **artefacts** are **safe** to **summarise** into model context vs which must remain **out-of-band** ([../interfaces/introspection-v0.md](../interfaces/introspection-v0.md)).

**SAFE UNKNOWN:** Exact truncation algorithms, structured **pack** formats, and per-agent **prompt templates** are **not** specified in v0.

---

## 2. Context budget rules (v0)

- **Rule CTX-01 — Boundedness:** Every model call **must** declare or inherit a **token budget** (input and output caps) consistent with [cost-token-budget-v0.md](cost-token-budget-v0.md).
- **Rule CTX-02 — Priority order:** When content does not fit, **drop** or **summarise** lower-priority sources **before** higher-priority ones (**section 4**).
- **Rule CTX-03 — Policy gate:** If **required** content (e.g. **task contract** core) does not fit after **minimum** trims, **do not** call the model — return **DENY** / **NEED HUMAN APPROVAL** / **STRUCTURE CHANGE** per governance signals.
- **Rule CTX-04 — Relevance:** **Irrelevant** logs, **stale** RAG, or **off-scope** registry dumps **must** be **excluded** by default.

---

## 3. What **can** enter model context

When policy, routing, and budgets allow, the following **may** be included **subject** to **section 4** dimensions:

| Source | Notes |
|--------|--------|
| **Task contract** | Core **scope_in**, objectives, constraints from [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md). **Highest** priority. |
| **Relevant registry entries** | **Minimal** slices (e.g. agent role summary, **tool_id** metadata) — not full governance dumps. |
| **Selected memory** | Only chunks **approved** for read and consistent with [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) and task **data** class. |
| **Selected RAG chunks** | Retrieved text **must** pass the same **PII** / **secrecy** filters as memory, **as defined in** [../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md) **and** this policy (**documentation** **only**). |
| **Tool results** | Sanitised per [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md) and threat model; **large** outputs **summarise** or **truncate** with explicit **loss** markers. |

---

## 4. What **must NOT** enter context

| Category | Rationale |
|----------|-----------|
| **Secrets** | API keys, signing keys, private tokens — [../security/threat-model-v0.md](../security/threat-model-v0.md). |
| **Raw credentials** | Passwords, long-lived session cookies, **unredacted** connection strings. |
| **Unnecessary PII** | Minimise to what the task requires; **unapproved** PII **must not** be written or **re**-**surfaced** contrary to [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md). |
| **Irrelevant logs** | Noise, **full** lifecycle logs, **debug** streams — **risk** of **injection** and **cost** blow-up. |

---

## 5. Budget dimensions (v0)

| Dimension | Role |
|-----------|------|
| **Token budget** | Hard or soft caps on **input** / **output** tokens tied to **run** and **project** ([cost-token-budget-v0.md](cost-token-budget-v0.md)). |
| **Source priority** | Ordering: **task contract** > **safety** / **policy** snippets > **selected memory** / **RAG** > **tool results** > **optional** introspection summaries. |
| **Freshness** | Prefer **newer** evidence when duplicates exist; **expire** stale RAG **per** [../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md) **and** [../memory/knowledge-freshness-v0.md](../memory/knowledge-freshness-v0.md) (**documentation**). |
| **Risk level** | **High**-**risk** tasks **tighten** inclusion (smaller **tool** raw dumps, **stricter** redaction). |

---

## 6. Relations to other artefacts

| Artefact | Relation |
|----------|----------|
| [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) | **Writes** to durable memory are **separate** from **prompt** assembly, but **both** must avoid **unapproved** PII and **secrets**. |
| **RAG** ([rag-architecture-v0.md](../memory/rag-architecture-v0.md)) | Retrieval **feeds** context **only** through **this** policy’s filters and **budgets**; **cross-link** **required** between this file and [../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md). |
| [../interfaces/introspection-v0.md](../interfaces/introspection-v0.md) / Self-Describe | **Introspection** outputs for **operators** **must not** be **blindly** pasted into **user**-**facing** model context; **summaries** **only**, with **path** truth per [../AGENTS.md](../AGENTS.md). |
| [model-routing-v0.md](model-routing-v0.md) | **context size** input; routing may switch models when **feasible** and **allowed**. |

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Context Budget Policy v0** — allowed/forbidden sources, dimensions, relations to memory, RAG ([rag-architecture-v0.md](../memory/rag-architecture-v0.md)), introspection. |

---

*End of MARS Context Budget Policy v0.*
