# MARS Website Factory — Reference Project Artifact Tree v0

**Status:** **documentation only** — **multi-artifact governance** and **dependency narrative** for the canonical production chain.  
**Not claimed:** automated invalidation engines, artifact repositories, or schema validators executing in runtime.

**Version:** v0.

**Related:** [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md), [artifact-types-v0.md](artifact-types-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [reference-project-model-v0.md](reference-project-model-v0.md), [reference-delivery-package-v0.md](reference-delivery-package-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md).

---

## 1. Lineage philosophy

**Lineage** means every material artifact knows its **upstream** producers and **downstream** consumers, so changes can be traced without implying an automated graph engine. **Documentation discipline:** when upstream content changes, downstream artifacts are **assumed stale** until re-validated or re-approved per [revision-semantics-v0.md](revision-semantics-v0.md) and [regeneration-semantics-v0.md](regeneration-semantics-v0.md).

**Validator** checks are **bounded**; lineage does **not** guarantee semantic correctness — only **traceability** and **gate alignment**.

---

## 2. Artifact inheritance

**Artifact inheritance** is the rule that downstream bundles **carry forward** explicit decisions from upstream (e.g. `site_type_id`, trust posture, CTA policy) unless a **revision** or **supersede** event documents a breaking change. Inheritance of **approvals** and **QA verdicts** follows [approval-semantics-v0.md](approval-semantics-v0.md) and [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) — never silent.

---

## 3. Freeze semantics

A **frozen** artifact (or region of an artifact) is **immutable** for handoff until a **freeze-breaking** event (revision, regeneration, waiver with scope) is recorded under HITL authority. **Mutable** artifacts accept controlled edits with **QA linkage** re-evaluated. See [artifact-state-model-v0.md](artifact-state-model-v0.md) and [stage-state-model-v0.md](stage-state-model-v0.md).

---

## 4. Supersede vs revision

| Concept | Meaning |
|---------|--------|
| **Revision** | A **new version** of an artifact lineage with **documented scope**; may reset downstream QA and approvals per policy. |
| **Supersede** | A **replacement** artifact that **displaces** a prior version for operational truth (e.g. new canonical sitemap); stronger downstream invalidation than a minor revision. |

Both require **human-visible** rationale in runbooks; **no** autonomous promotion.

---

## 5. Canonical stage → artifact chain (v0)

Ordered chain for **reference project** documentation:

```text
Intake → Strategy → IA → Blueprint → Design → Frontend → QA → Delivery
```

**Note:** [workflow-map.md](workflow-map.md) also names **Wireframe** between blueprint and design; v0 treats wireframes as **part of** the **Design** preparation bundle unless a project charter splits them. **SAFE UNKNOWN:** tooling-specific wireframe storage.

---

## 6. Per-stage artifact responsibilities

Legend: **Owner** = **accountable human role** (agents are **planned** per [agent-map.md](agent-map.md)); **Mutable/Frozen** = default posture at gate exit; **Invalidation** = typical downstream impact on **truth** (human must re-run QA / approvals as applicable).

### 6.1 Intake

| Aspect | Content |
|--------|---------|
| **Primary artifacts** | Intake summary, scope draft, constraints, stakeholder map, compliance flags. |
| **Upstream** | External briefs, legacy exports (**optional**). |
| **Downstream** | Strategy, IA (classification inputs). |
| **Owner** | PM / lead (HITL). |
| **Mutable / frozen** | Mutable until **G1** confirmation; then **frozen** baseline for scope disputes. |
| **Invalidation impact** | **High** — changing goals invalidates strategy hypotheses and later IA/blueprint. |
| **QA linkage** | Completeness QA (intake checklist); no production QA yet. |
| **Approval linkage** | **G1** per [workflow-map.md](workflow-map.md). |

### 6.2 Strategy

| Aspect | Content |
|--------|---------|
| **Primary artifacts** | Positioning, messaging architecture, SEO/conversion **hypotheses**, risk register slice. |
| **Upstream** | Intake. |
| **Downstream** | IA, Blueprint (objectives, intent dimensions). |
| **Owner** | Marketing / strategy lead + PM. |
| **Mutable / frozen** | Mutable during exploration; **frozen** after **G2** for handoff. |
| **Invalidation impact** | **High** for IA URLs, blueprint objectives, design narrative, frontend copy. |
| **QA linkage** | Strategy QA (consistency, SAFE UNKNOWN boundaries). |
| **Approval linkage** | **G2** (brand/compliance sensitivity). |

### 6.3 IA (Information Architecture)

| Aspect | Content |
|--------|---------|
| **Primary artifacts** | Sitemap, navigation model, URL policy, parent/child page graph seeds (see [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md)). |
| **Upstream** | Intake, Strategy. |
| **Downstream** | Blueprint (per-page structure), Design (nav patterns), Frontend (routes), SEO (internal links). |
| **Owner** | IA / UX lead. |
| **Mutable / frozen** | Mutable; **frozen** after **G3** slice for blueprint batch. |
| **Invalidation impact** | **Very high** — URL/nav changes ripple to blueprint, content, internal links, QA matrices. |
| **QA linkage** | IA QA (orphans, depth, cannibalization risks flagged). |
| **Approval linkage** | **G3** (shared with blueprint in practice; may be split by charter). |

### 6.4 Blueprint

| Aspect | Content |
|--------|---------|
| **Primary artifacts** | Per-page blueprint payloads per [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), block choices per [block-registry-v0.md](block-registry-v0.md). |
| **Upstream** | Strategy, IA, registries. |
| **Downstream** | Design, Frontend, QA scenarios. |
| **Owner** | PM + tech lead; UX input. |
| **Mutable / frozen** | Mutable; **frozen** per page or batch after **blueprint approval**; partial freeze allowed per [approval-semantics-v0.md](approval-semantics-v0.md). |
| **Invalidation impact** | **High** for design comps, component specs, frontend structure, QA cases. |
| **QA linkage** | [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md) and project QA matrix. |
| **Approval linkage** | **G3** (scope/size/cost). |

### 6.5 Design

| Aspect | Content |
|--------|---------|
| **Primary artifacts** | Visual design system application, comps/specs per [design-handoff-contract-v0.md](design-handoff-contract-v0.md). |
| **Upstream** | Blueprint (+ optional wireframes). |
| **Downstream** | Frontend (tokens, layout, assets), QA (visual/accessibility intent). |
| **Owner** | Design lead / client HITL. |
| **Mutable / frozen** | Mutable; **frozen** after **G5** for matched pages/components. |
| **Invalidation impact** | **High** for frontend implementation and visual QA. |
| **QA linkage** | Design QA lane (planned agent + human). |
| **Approval linkage** | **G5** before frontend production. |

### 6.6 Frontend

| Aspect | Content |
|--------|---------|
| **Primary artifacts** | Static sources per [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [frontend-artifact-model-v0.md](frontend-artifact-model-v0.md). |
| **Upstream** | Blueprint, Design. |
| **Downstream** | QA execution artifacts, Delivery packages. |
| **Owner** | Tech lead; **Gulp Frontend Agent** role is **legacy-bridge / planned** per [`../../agents/registry.md`](../../agents/registry.md). |
| **Mutable / frozen** | Mutable in dev; **freeze** on release candidate per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md). |
| **Invalidation impact** | **Medium–high** — affects QA retest scope, export bundle. |
| **QA linkage** | Build QA, accessibility checks, cross-page regression (see multi-page doc). |
| **Approval linkage** | **G6** (PR / file set). |

### 6.7 QA

| Aspect | Content |
|--------|---------|
| **Primary artifacts** | QA results / payloads per [qa-result-payloads-v0.md](qa-result-payloads-v0.md), waivers, blockers. |
| **Upstream** | All prior stage artifacts relevant to scope. |
| **Downstream** | Delivery **only** if gates pass or waivers are authorized. |
| **Owner** | QA lead; **Validator** where routed — **not** omniscient. |
| **Mutable / frozen** | Verdicts **frozen** once attached to a **delivery candidate**; superseded by explicit new run IDs in runbooks. |
| **Invalidation impact** | **Blocking** for delivery when failed blockers exist. |
| **QA linkage** | Meta — QA on QA is **human process**; no hidden automation. |
| **Approval linkage** | **G7** / pre-delivery HITL per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md). |

### 6.8 Delivery

| Aspect | Content |
|--------|---------|
| **Primary artifacts** | Export / release bundle, handoff notes, rollback notes per [reference-delivery-package-v0.md](reference-delivery-package-v0.md). |
| **Upstream** | QA-passed frontend + configs + docs. |
| **Downstream** | **Live environment** (outside factory docs) — **SAFE UNKNOWN** stack. |
| **Owner** | Ops / client HITL. |
| **Mutable / frozen** | Release tag **frozen**; hotfix path = new **revision** lifecycle. |
| **Invalidation impact** | Operational — post-release issues enter **revision** or **incident** track, not silent overwrite. |
| **QA linkage** | Pre-delivery validation slice; smoke in target env if charter requires. |
| **Approval linkage** | **Release approval** — **no** self-approval (see HITL governance). |

---

## 7. Changelog

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-12 | Initial **Reference Project Artifact Tree v0** — lineage, inheritance, freeze, supersede/revision, per-stage table. |
