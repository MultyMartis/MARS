# MARS Website Factory — Artifact Bus Layer v0 — Overview

**Status:** **documentation only** — **document-first transfer semantics**, **operational orchestration discipline**, and **lifecycle transfer model** for how logical artifacts are referenced, routed, published, consumed, and invalidated across factory stages. **Not** a queue system, **not** an event engine, **not** a runtime message bus, **not** Kafka/RabbitMQ/etc., **not** an execution daemon, **not** hidden transport, **not** autonomous orchestration.

**Version:** v0.

**Related:** [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md), [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md), [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md), [safe-unknown-boundary.md](safe-unknown-boundary.md); **Artifact Bus sibling docs:** [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md), [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md), [artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md), [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md), [artifact-publication-semantics-v0.md](artifact-publication-semantics-v0.md), [artifact-consumption-rules-v0.md](artifact-consumption-rules-v0.md), [artifact-governance-rules-v0.md](artifact-governance-rules-v0.md), [delivery-bus-semantics-v0.md](delivery-bus-semantics-v0.md), [artifact-transfer-qa-rules-v0.md](artifact-transfer-qa-rules-v0.md).

---

## 1. Purpose

Earlier layers define **what** artifacts are ([artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md)), **how** prompts reference them at boundaries ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md)), **how** lifecycle behaves over time ([execution-semantics-overview-v0.md](execution-semantics-overview-v0.md)), and **how** meaning is attributed and invalidated semantically ([semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md)).

The **Artifact Bus Layer v0** adds a **normalized vocabulary for artifact movement** as **authored documentation and REPORT discipline** — without implying that any software component moves bytes between stages automatically.

---

## 2. Core definitions

| Term | Meaning in v0 |
|------|----------------|
| **Artifact bus** | The **named set of semantics** in this layer: envelope fields, routing rules, transfer rules, lineage, publication, consumption, governance, delivery-bus movement, and transfer QA. A **logical** bus — **prose and checklist authority**, not a deployed service. |
| **Transfer** | A **declared** movement of responsibility or reliance from **source_stage** to **target_stage** for a given **artifact_id** / **revision_id**, recorded in prompts, envelopes, and REPORTs. **Transfer ≠** TCP/HTTP/file sync. |
| **Publish** | Making an artifact **available for consumption** under a **publication class** (draft, review, approved, frozen, etc.) per [artifact-publication-semantics-v0.md](artifact-publication-semantics-v0.md). Publishing is **declared**; it does **not** imply pushing to a registry service or CDN. |
| **Consume** | A downstream stage **accepts** an upstream artifact as input under stated envelope rules; may **reject**, **partially consume**, **invalidate**, or **reopen** per [artifact-consumption-rules-v0.md](artifact-consumption-rules-v0.md). |
| **Route** | An **allowed** or **forbidden** path of transfer between workflow stages (or substages such as QA lanes), per [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md). |
| **Lineage** | Parent/child/sibling/supersede/rollback relationships between artifact instances, per [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md). |
| **Transfer authority** | **Who** may authorize a route or publication step (role + HITL gate). Aligns with [approval-semantics-v0.md](approval-semantics-v0.md) and [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md). **No** agent self-authorization for freeze or release. |
| **Transfer freeze** | A **bus-level** agreement that a given artifact (or envelope) **may not** be re-routed or re-published without HITL reopening — mirrors artifact/stage freeze in execution semantics; see [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md) §route freeze. |
| **Transfer invalidation** | Declaring that a previously valid **transfer** (or consumption assumption) is **no longer trustworthy** because upstream revision, semantic invalidation, or QA failure changed the basis; per [artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md) and [dependency-invalidation-v0.md](dependency-invalidation-v0.md). |
| **Stale transfer** | A consumption or routing decision that **still references** an upstream revision, approval, QA verdict, or semantic state that has been **superseded, invalidated, or expired**. Must be **explicitly flagged** — never silent. |
| **Orphan artifact** | An artifact (or envelope) whose **lineage parent** is missing, **superseded without consumer update**, or whose **declared dependencies** no longer resolve. Consumption is **blocked** until lineage is repaired or **SAFE UNKNOWN** is bounded with HITL. |
| **Artifact state propagation** | **Declared** refresh of envelope / REPORT fields (e.g. **qa_state**, **semantic_state**, **approval_state**) so downstream readers see **current** upstream truth after a revision, invalidation, or QA outcome. This is **authoring discipline** and **traceable narrative** — **not** background synchronization, **not** pub/sub, **not** a hidden invalidation engine, **not** autonomous orchestration. |

---

## 3. Explicit non-claims

| Topic | This layer does **not** claim |
|--------|-------------------------------|
| Transport | A message broker, topic, subscription, or background worker moving artifacts. |
| Execution | Async pipelines, schedulers, or daemons applying these rules automatically. |
| State store | That MARS or Cursor persists envelope rows unless a **future** contract evidences it (**SAFE UNKNOWN**). |
| Completeness | That every project fills every envelope field — gaps follow [safe-unknown-boundary.md](safe-unknown-boundary.md). |

---

## 4. Relationship to adjacent layers

| Layer | Relationship |
|-------|----------------|
| Artifact Architecture | Bus semantics **presuppose** artifact types and contracts; bus adds **movement and envelope** vocabulary. |
| Execution Semantics | Stage/artifact/approval/QA/delivery states **inform** envelope fields and transfer validity; bus **does not** replace those documents. |
| Semantic Relationship | **semantic_state**, freeze, and invalidation triggers **align** with semantic layer; bus routes **carry** semantic obligations as **declared fields**, not as auto-sync. |
| Prompt Standards | Prompts **cite** envelopes and routes per [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) and [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md). |

---

## 5. Document set (v0)

| Document | Role |
|----------|------|
| [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md) | **This file** — definitions, philosophy, non-claims. |
| [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md) | Normalized envelope fields, immutability regions, supersede/stale/orphan. |
| [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md) | Allowed/forbidden/partial/QA/delivery/invalidation routes; authority; freeze. |
| [artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md) | Inheritance, invalidation, downgrade, freeze break, partial transfer. |
| [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md) | Parent/child/sibling/supersede/rollback/branch/frozen lineage; drift; orphaning. |
| [artifact-publication-semantics-v0.md](artifact-publication-semantics-v0.md) | Publication classes, authority, visibility, freeze, rollback. |
| [artifact-consumption-rules-v0.md](artifact-consumption-rules-v0.md) | Consume / reject / invalidate / reopen / partial acceptance. |
| [artifact-governance-rules-v0.md](artifact-governance-rules-v0.md) | Anti-patterns: silent replacement, hidden revision, fake approval inheritance. |
| [delivery-bus-semantics-v0.md](delivery-bus-semantics-v0.md) | Release candidate, delivery candidate, packages, freeze, rollback authorities. |
| [artifact-transfer-qa-rules-v0.md](artifact-transfer-qa-rules-v0.md) | QA for transfer layer: severities, blocking, waivers, SAFE UNKNOWN. |

---

## 6. Operating principles (one-line)

1. **Bus = semantics + discipline**, not wires.  
2. **Every transfer is attributable** (who, which gate, which revision).  
3. **Routing follows workflow truth** ([website-factory-workflow-v0.md](website-factory-workflow-v0.md)).  
4. **Invalidation is explicit** — no hidden cascade.  
5. **Publication and consumption are symmetric obligations** (publish honestly / consume honestly).  
6. **SAFE UNKNOWN** where binding format or tooling is unspecified.

---

## 7. Revision history

| Date | Change |
|------|--------|
| 2026-05-12 | **v0** — initial Artifact Bus Layer overview (documentation only). |
| 2026-05-12 | **v0** — **artifact state propagation** definition added; removed stray non-pack appendix from file tail. |
