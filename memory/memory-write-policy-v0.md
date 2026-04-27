# MARS — Memory Write Policy v0

**Status:** documented — contract only. This file defines when and how **memory** (durable, recall-oriented knowledge) may be written in MARS design. It does **not** specify a vector store, RAG stack, or implementation. Per [../AGENTS.md](../AGENTS.md), no memory backend or write pipeline is **claimed** unless the repository contains evidence of code or adapters.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Storage technology, message formats, and exact field names in a future schema remain TBD until a machine contract is adopted. This v0 is **normative** for documentation: which actor types may propose writes, and which artefacts a write must carry in human or contract form.

---

## 1. Purpose

- **Bound** durable memory mutations (not ephemeral context) to authoritative sources, project/entity scope, retention, and quality signals so Tool, RAG, and future runtime work do not assume ungoverned “facts.”
- **Distinguish** long-term or semantic **memory** (this policy) from **execution** state **durability** (see [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md)) and from **governance** event logging (see [../logs/lifecycle-log.md](../logs/lifecycle-log.md)).
- **Align** write authority with [../security/permissions-v0.md](../security/permissions-v0.md) and [../security/guardrails-v0.md](../security/guardrails-v0.md) at contract level (no enforcement engine in Phase 1 repository).

---

## 2. What counts as a memory write

A **memory write** is any intended persistence of content into a MARS **memory** surface that is not purely ephemeral (e.g. single request / single turn) and is meant to be retrieved later for grounding, recall, recommendation, or orchestrator or agent decision-support (as documented or future implementation). Examples of in-scope **actions** (conceptual, not an implementation claim):

- **Create** a new memory item (fact, note, summary, episode, vector-chunk metadata).
- **Update** a declared version of an item: append supersession, tombstone, or revised value per **§4** and **§5**.
- **Delete** or **tombstone** (logical delete) per retention or legal policy in **§5**.

**Out of scope** for this policy (by design; these surfaces remain important):

- **Runtime State Store** facets `state`, `checkpoints`, `results`, `errors` — normative in [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) and [../storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md) (execution durability). A bridge artefact (e.g. a summary) may **feed** both execution views and **memory** only if **§4** requirements are satisfied for the **memory** side.
- **Append-only** governance rows in [../logs/lifecycle-log.md](../logs/lifecycle-log.md) — not substitutes for memory. Do not duplicate the same **truth** in two SoTs; prefer a link or `event_id` when a write is **triggered** by a governance event.

---

## 3. Allowed writers (actor classes)

| Writer | Description | Contract expectation |
|--------|--------------|------------------------|
| **Control Plane** | Orchestrator / router that applies policy and task constraints ([../control-plane/contract.md](../control-plane/contract.md)) | May orchestrate writes only within routed steps, declared passport scope, and workflow/approval as documented. |
| **Memory Agent** | An agent **role** (or equivalent in [../agents/registry.md](../agents/registry.md) / card) dedicated to curated memory: ingest, reconcile, tombstone | May propose or author writes as **actor** in metadata; must still meet **§4** (source, confidence, retention, scope). |
| **approved Workflow** | A run or graph that governance or registry marks as **allowed** to emit memory writes (explicit capability, not “any” workflow) | Permitted only if the workflow (or its row or doc) states **memory** write **intent** and the same **§3b** prohibitions apply. |
| **Human operator** | A person with accountable approval (HITL, owner, maintainer) | May direct or approve writes; **author** / **actor** fields in **§4** must be explicit. |

**Not allowed** as sole, unreviewed **originator** in contract interpretation: ad-hoc “system” or **anonymous** write without a class above and without **§4** metadata.

---

## 3b. Prohibited content (what must not be written)

| Category | Rule |
|----------|------|
| **Unsourced facts** | No memory item that states a **factual** claim without a **§4** source reference (document + section, run/output id, or explicit human attestation and identity). |
| **Secrets** | No API keys, tokens, signing keys, HMAC material, private keys, session secrets, or unredacted bearer material. |
| **Raw credentials** | No passwords, connection strings with passwords, raw OAuth refresh tokens, or unencrypted PATs. |
| **Unapproved PII** | No **personally identifying data** without documented approval ([../security/approval-gates.md](../security/approval-gates.md), [../governance/risk-register.md](../governance/risk-register.md)) and a stated minimization, purpose, and retention path. v0: **governance** and risk or lifecycle **note** — not an in-repo product **control** until **implementation**. |
| **Speculative conclusions as facts** | Hypotheses, guesses, and model inferences must be labelled (confidence, non-factual framing); they must not be stored as **certain** truths without **§4** warranting (e.g. independent source or HITL confirmation). |

---

## 4. Write requirements (minimum metadata)

Each **conforming** memory write (documentation or future machine schema) must be able to supply:

| Field | Description |
|-------|-------------|
| **Source reference** | Evidence for the item: path and section, governance id, or `run_id` / `task_id` (or other correlator), or human attestation. **Required** for **factual** claims. |
| **`entity_id` / `project_id`** | When the item is scoped to a project or **entity** in governance, set id(s) using authoritative [../registry/project-registry.md](../registry/project-registry.md) for `project_id`. Use `—` or omit only if **global** / system scope is **explicit** (avoid silent unscoped inference). |
| **Timestamp** | When the write or logical version was asserted (ISO-8601 recommended). Clock trust: **SAFE UNKNOWN** until a runtime. |
| **Author / actor** | §3 class plus an identifiable id (agent id, human handle + **role**, or **orchestrated** step as documented). |
| **Confidence level** | Ordinal or labelled (e.g. high / medium / low / **inferred**). Inference must not map to “certain” without gating. |
| **TTL or retention policy** | Time-to-live, legal or contract **hold**, or **governance** deletion class. Indefinite retention only if **explicit** and **risk-acknowledged** (see [../governance/risk-register.md](../governance/risk-register.md)). |
| **Update / delete rules** | Whether the operation is **append**, version **supersede**, or **tombstone**; link to prior **record** id on correction. Align with the append-first, no-silent-rewrite **spirit** in [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) §5: memory SoT is **different** from run state, but the same **discipline** applies. |

**Task contract:** [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md) `scope_in`, `constraints`, `risk_level` — a memory **write** must not **exceed** the task’s stated bounds (design; future **enforcement** TBD).

---

## 5. Update and delete rules (v0)

1. **No** silent in-place rewrites of a **committed** memory **artefact** that **erase** **provenance**. Corrections **append** a new version or **tombstone** the old with a pointer; see [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) **§5** for analogous state durability.  
2. **Delete** = **tombstone** or governance-approved **purge** with a **recorded** **reason** (full audit path **TBD**; [../governance/risk-register.md](../governance/risk-register.md) for **compliance** and **residual** risk).  
3. **PII** / **compliance**-sensitive **revisions** require HITL or **governance** per [../security/approval-gates.md](../security/approval-gates.md). No automated, broad, undocumented erasure in v0.

---

## 6. Memory types (v0 taxonomy)

| Type | Description |
|------|-------------|
| **Project memory** | Durable **knowledge** tied to a `project_id`: decisions, constraints, glossary, accepted invariants, aligned with [../registry/project-registry.md](../registry/project-registry.md). |
| **Agent memory** | **Longer-lived** knowledge for a **specific** agent: playbooks, preferences, learned **tactics** (only when **approved**). |
| **Workflow memory** | Reusable or run-aggregated facts **scoped** to a workflow or pattern (e.g. **reusable** **orchestration** lessons). |
| **User memory** | End-user–scoped **preferences** or **history** where PII and consent **rules** **apply**; **highest** gating (§3b, **registers**). |
| **Semantic memory** | Factual or conceptual **store** (often retrieval-oriented, **RAG**-aligned); every chunk or **record** needs **§4**; no speculative “facts” without warranting. |
| **Episodic memory** | **Time-ordered** or run-linked **episodes** (what **happened**; `trace` or `run_id` when **available**). |

Types are not mutually exclusive — a future schema may tag one **physical** artefact with **several** labels. Vector vs blob vs row store: **SAFE UNKNOWN**.

---

## 7. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [../registry/project-registry.md](../registry/project-registry.md) | **Authoritative** `project_id` and **status**; project-scoped writes should reference a row, or the scope is **SAFE UNKNOWN** for governance purposes until **resolved** (introspection / registry rules). |
| [../logs/lifecycle-log.md](../logs/lifecycle-log.md) | **Material** policy or schema **changes** affecting **memory** may **append** a **lifecycle** row. Do **not** conflate **governance** log **events** with **memory** SoT (see **§2**). |
| [../governance/risk-register.md](../governance/risk-register.md) | PII, retention, and write-authority risks; this policy informs mitigations (documentation-level) for e.g. **RISK-V0-0011**, **RISK-V0-0007**. |
| [../security/permissions-v0.md](../security/permissions-v0.md) | **`write`**, **`external-call`**, and HITL-related gates **bound** how **§3** actors may exercise **proposed** **mutations** (contract-time; no runtime in Phase 1). |
| [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) | **Execution** state **vs** durable **knowledge**; **bridge** at the storage boundary only with **explicit** **mapping** (**§2**). |

---

## 8. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Memory** **Write** **Policy** v0 — purpose, allowed **writers**, prohibited **content**, **metadata** requirements, **memory** **types**, **relations** to registry / logs / risk / permissions / runtime state store, **update** rules; **implementation** and backend **SAFE UNKNOWN** (Phase 1). |

---

*End of MARS Memory Write Policy v0.*