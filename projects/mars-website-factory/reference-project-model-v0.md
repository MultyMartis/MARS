# MARS Website Factory — Reference Project Model v0

**Status:** **documentation only** — operational **reference architecture** and **lifecycle vocabulary** for how a factory-backed website effort is classified and bounded.  
**Not claimed:** storage backends, persisted project records, orchestration daemons, autonomous runs, or a project database.

**Version:** v0.

**Related:** [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [stage-state-model-v0.md](stage-state-model-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [reference-project-lifecycle-v0.md](reference-project-lifecycle-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md), [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md).

---

## 1. Purpose

This document defines what a **reference project** is in the Website Factory sense: a **documentation-first** pattern for describing **project kind**, **scope**, **artifact sets**, **QA / delivery / approval posture**, and **orchestration boundaries** — without asserting that any engine materializes or stores these fields.

---

## 2. Definitions

### 2.1 Reference project

A **reference project** is a **normative pattern** (templates, gates, artifact expectations, HITL rules) used to align human- or Cursor-driven work with factory contracts. It is **not** automatically instantiated as a runtime object; it is the **conceptual shell** under which **production**, **sandbox**, **migration**, or **demo** efforts are described.

### 2.2 Production project

A **production project** is a factory-scoped effort whose **delivery_state** targets **customer-facing or revenue-bearing** publication. It carries the **strictest** QA, approval, and freeze discipline. **SAFE UNKNOWN:** hosting, CI, and credential systems until specified outside this pack.

### 2.3 Sandbox project

A **sandbox project** applies the same **stage and artifact vocabulary** as production but allows **relaxed** gates (explicitly declared in `hitl_policy` / runbook). Outcomes are **not** delivery candidates unless escalated with a **scope change** and **fresh approvals** per [approval-semantics-v0.md](approval-semantics-v0.md).

### 2.4 Migration project

A **migration project** coordinates **from** a legacy or external site/asset set **to** a factory-shaped artifact tree. It stresses **lineage**, **invalidation**, and **partial reuse** (see [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md)). **SAFE UNKNOWN:** automated importers or CMS APIs — not claimed here.

### 2.5 Demo project

A **demo project** is a **time-bounded**, often **reduced-scope** effort for training, sales engineering, or internal proof. It **must** be labeled so **delivery** and **approval** semantics do not silently inherit production authority. **Forbidden:** presenting demo **delivery acceptance** as production **release approval** (see [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md)).

---

## 3. Normalized fields (conceptual)

The following fields are **logical** descriptors for traceability in docs and runbooks. They are **not** a database schema and **not** evidence of persisted state.

| Field | Meaning |
|--------|---------|
| **project_id** | Stable identifier for the effort (align with [`../../registry/project-registry.md`](../../registry/project-registry.md) when registered). |
| **project_type** | One of: `reference` \| `production` \| `sandbox` \| `migration` \| `demo` (see §2). |
| **site_type_id** | Classification key from [site-type-registry-v0.md](site-type-registry-v0.md); drives defaults for strategy, blocks, SEO, QA emphasis. |
| **project_scope** | What is **in** / **out**: pages, locales, brands, legal constraints, integrations **as declared** in intake/strategy artifacts. |
| **workflow_scope** | Which **factory stages** are active (e.g. blueprint-only refresh vs full pipeline); must stay consistent with [website-factory-workflow-v0.md](website-factory-workflow-v0.md). |
| **execution_mode** | **Human-supervised** execution surface today per `governance/execution-model.md` (e.g. Cursor). **SAFE UNKNOWN:** future binding labels until an execution bridge wire exists for Website Factory. |
| **artifact_set** | The **multi-artifact** bundle expected at the current lifecycle position (see [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md)). |
| **qa_state** | Aggregate conceptual QA posture for the project slice (gates, waivers, blockers) per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) and [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md). **Validator** is **not** an omniscient oracle — see [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md). |
| **delivery_state** | Where the project sits relative to **candidates**, **export**, and **release** per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) and [reference-delivery-package-v0.md](reference-delivery-package-v0.md). |
| **approval_state** | Human-gated approvals and conditions per [approval-semantics-v0.md](approval-semantics-v0.md) and [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md). |
| **hitl_policy** | Who may approve / reject / freeze / reopen / waive / escalate for this **project_type** and **workflow_scope** (see HITL governance doc). |
| **lifecycle_state** | Coarse project lifecycle node per [reference-project-lifecycle-v0.md](reference-project-lifecycle-v0.md). |
| **orchestration_scope** | What **multi-page** and **cross-artifact** dependencies are in play (see [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md)). **Documentation only** — no daemon, no queue, no hidden state engine. |

---

## 4. SAFE UNKNOWN (explicit)

| Topic | Boundary |
|--------|----------|
| **Storage** | Where artifacts live (Git only, DMS, CMS, object store) is **unknown** until a project charter or integration contract names it. |
| **Runtime persistence** | No claim that MARS or Website Factory persists `lifecycle_state` / `qa_state` in a database in this repository. |
| **Project database** | Any future **project record** store is **planned-implementation** and **out of scope** for v0 proof. |
| **Orchestration engine** | **No** in-repo workflow engine for Website Factory; coordination remains **human-visible** prompts, checklists, and signals per governance. |

---

## 5. Changelog

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-12 | Initial **Reference Project Model v0** — project kinds, conceptual fields, SAFE UNKNOWN boundaries. |
