# MARS Website Factory — Artifact Architecture Layer v0 (overview)

**Status:** **documentation only** — **semantics and contracts in prose**, aligned with [Website Factory Workflow v0](website-factory-workflow-v0.md).  
**Not claimed:** executable schemas, JSON Schema enforcement, a validation engine in this repo, automated site generation, or serialization guarantees at runtime.

**Version:** v0.

**Related:** [artifact-types-v0.md](artifact-types-v0.md), [page-objective-model-v0.md](page-objective-model-v0.md), [section-payload-model-v0.md](section-payload-model-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md); registries and handoffs per [registries.md](registries.md).

---

## Why this layer exists

The factory already defines **stages**, **contracts**, and **registries**. The **artifact architecture layer** adds a shared vocabulary for **what crosses stage boundaries**: normalized meanings for objectives, sections, CTAs, trust, SEO/conversion intent, frontend bundles, and QA outputs. That reduces ad hoc prose, makes **handoffs** comparable across projects, and keeps future **orchestration** (Control Plane, Tasks) aligned with the same semantics **without** pretending those systems exist today.

---

## Terms (distinct roles)

| Term | Meaning in v0 |
|------|----------------|
| **Workflow** | Ordered **stages** and gates ([website-factory-workflow-v0.md](website-factory-workflow-v0.md)) — the **process** story. |
| **Agent** | A **planned role** ([agent-map.md](agent-map.md)) that may **produce or review** artifacts; **not** proof of implementation. |
| **Artifact** | A **logical deliverable** at a stage boundary (memo, blueprint set, handoff pack, build bundle, report). Identified in documentation by stable **artifact_id** philosophy (see [artifact-types-v0.md](artifact-types-v0.md)). |
| **Payload** | The **field-level content shape** carried inside an artifact for machine- and human-oriented exchange — still **conceptual** in v0; **not** a mandated wire format. |
| **Contract** | Authoritative **field vocabulary and rules** for a class of artifacts (e.g. [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md)). Contracts are **SoT for meaning**; they do **not** execute. |
| **Registry** | Canonical **rows** for classification or blocks ([site-type-registry-v0.md](site-type-registry-v0.md), [block-registry-v0.md](block-registry-v0.md)) — **vocabulary and compatibility**, not a hosted service. |

---

## Why normalized semantics matter

- **Interoperability:** Strategy, blueprint, design, and frontend teams (or future agents) reference the same **intent classes** instead of re-inventing labels per page.
- **QA discipline:** Checklists and Validator-oriented checks can cite **stable categories** (severity, evidence, escalation) when those layers mature ([qa-validation-model.md](qa-validation-model.md)).
- **Governance:** **SAFE UNKNOWN**, **HITL**, and **NEED HUMAN APPROVAL** attach to **named artifact boundaries** rather than vague “the doc.”

---

## Reusable artifact discipline for MARS

MARS spans many contracts. Website Factory artifact semantics are **scoped** to static, registry-driven website production. They **reuse** MARS-wide signals (`governance/system-signals-dictionary.md`, `workflows/task-contract-v0.md`) and **do not** replace them. Cross-project reuse = **shared definitions** in this pack + links to registry rows, **not** a universal JSON envelope in v0.

---

## Relationship to future orchestration / runtime

When a Control Plane or Execution Bridge exists, artifacts described here are **candidates** for Task attachments, state store records, or human runbooks. **Binding format, storage, and versioning** remain **SAFE UNKNOWN** until specified elsewhere. This layer **prepares** orchestration; it **does not** implement it.

---

## Relationship to HITL

Artifacts that **freeze** scope (approved blueprint batch, frozen design baseline, release approval) are **immutability-oriented** at the process level: changes after approval should **re-trigger** gates per workflow. HITL is **not** replaced by richer payloads — explicit gates in [workflow-map.md](workflow-map.md) and workflow v0 stay authoritative.

---

## Relationship to Validator

**Validator Agent** (planned) supplies **cross-cutting** structural/policy checks ([qa-validation-model.md](qa-validation-model.md)). Artifact-layer **QA result payloads** describe what specialist QA and Validator **might** emit **as concepts**; they **do not** assert Validator code paths or automated enforcement.

---

## Non-runtime boundary (explicit)

- These documents are **conceptual contracts** and **semantic models**.
- They are **not** executable schemas, **not** runtime serialization guarantees, and **not** evidence of automation.

---

*Last updated: 2026-05-11 — Artifact Architecture Layer v0 overview.*
