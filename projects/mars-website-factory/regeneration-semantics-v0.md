# MARS Website Factory — Regeneration Semantics v0

**Status:** **documentation only** — defines how **regeneration** (the re-production of artifact content, full or partial) behaves in the factory. **Not** a regeneration engine, **not** autonomous AI authoring, **not** an automatic rebuild service.

**Version:** v0.

**Related:** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [stage-state-model-v0.md](stage-state-model-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md), [artifact-types-v0.md](artifact-types-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Purpose

**Regeneration** is the act of **re-producing artifact content** (often by re-running a production prompt) rather than editing the prior content in place. It overlaps with revision ([revision-semantics-v0.md](revision-semantics-v0.md)) but is **distinct**:

| Aspect | Revision | Regeneration |
|--------|----------|--------------|
| **Action** | Edit specific fields. | Re-produce content. |
| **Scope** | Bounded fields / sections. | Bounded **or** full artifact body. |
| **Author input** | Targeted CRs or change requests. | Re-issued production prompt (possibly with updated context). |
| **Typical trigger** | QA finding, HITL request. | Upstream change requires fresh production; or a regeneration request from HITL when authoring quality is unacceptable. |

Regeneration is **not** "AI rebuilds the whole project autonomously". Per [safe-unknown-boundary.md](safe-unknown-boundary.md) and [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), the factory **does not** claim autonomous regeneration.

This document defines:

- partial vs full regeneration;
- safe vs unsafe regeneration;
- regeneration **boundaries** ([§4](#4-regeneration-boundaries));
- regeneration **triggers** ([§5](#5-regeneration-triggers));
- **dependency-aware** regeneration ([§6](#6-dependency-aware-regeneration));
- QA **invalidation** after regeneration ([§7](#7-qa-invalidation-after-regeneration));
- HITL anchoring;
- relationship to revision and supersede.

---

## 2. Partial regeneration

**Partial regeneration** re-produces a **bounded subset** of an artifact's content while leaving the rest intact.

| Aspect | Detail |
|--------|--------|
| **Scope** | Named fields, named sections, named pages, named blocks. |
| **Authoring** | Production prompt explicitly states which fields are regenerated and which are preserved. |
| **Output state** | New revision id ([artifact-state-model-v0.md](artifact-state-model-v0.md) §3). |
| **QA reset** | Only on the regenerated subset + any QA categories that span the artifact ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) §gate reset). |
| **HITL** | Re-gate at the relevant gate per scope; partial regeneration usually re-runs through the same gate that approved the prior revision. |
| **Examples** | Regenerate hero section copy across 5 pages; regenerate meta descriptions for a SEO-affected branch; regenerate the CTA staging visual for landing template. |

Partial regeneration **requires explicit enumeration** of regenerated content. "Regenerate the page" without enumeration is **not** partial regeneration.

---

## 3. Full regeneration

**Full regeneration** re-produces the **entire** artifact body.

| Aspect | Detail |
|--------|--------|
| **Scope** | All authoring-relevant fields of the artifact. |
| **Authoring** | Production prompt re-issues against current upstream baselines. |
| **Output state** | New revision id (or new artifact_id if structural reset — see [§8](#8-relationship-to-revision-and-supersede)). |
| **QA reset** | Full QA reset for the artifact's QA lane(s). |
| **HITL** | Re-gate at the same gate that approved the prior revision. |
| **Examples** | Re-author a single blueprint after IA revision; re-author the visual direction after brand pivot; re-author an entire SEO hypothesis after market repositioning. |

Full regeneration is **scoped to the artifact**, not to the project. A "full project regeneration" is **not** a v0 concept; it would be a sequence of HITL-approved per-artifact regenerations.

---

## 4. Safe regeneration

A regeneration is **safe** when:

- the **scope** is explicit and bounded ([§2](#2-partial-regeneration) / [§3](#3-full-regeneration));
- the **trigger** is recorded ([§5](#5-regeneration-triggers));
- the **upstream baseline** is `approved` or `frozen` ([artifact-state-model-v0.md](artifact-state-model-v0.md));
- the **downstream impact** is declared ([dependency-invalidation-v0.md](dependency-invalidation-v0.md));
- the **HITL re-gate** is planned and recorded;
- the **QA reset** is planned per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md);
- **SAFE UNKNOWN** entries from the prior revision are either resolved or explicitly carried forward with rationale.

A safe regeneration is **prose-disciplined**: the prompt and the report ([reporting-standard-v0.md](reporting-standard-v0.md)) name the boundary, the trigger, the impact, and the HITL anchor.

---

## 5. Unsafe regeneration

A regeneration is **unsafe** (forbidden) when:

- the **scope is unbounded** ("regenerate everything");
- the **trigger is unstated**;
- the **upstream baseline is itself `draft`, `invalidated`, `superseded`, `deprecated`, or `archived`**;
- the **downstream impact is unacknowledged**;
- the **HITL gate is bypassed** ("we'll re-approve after");
- the **QA reset is skipped**;
- the **prior content is discarded silently** (no lineage entry).

An unsafe regeneration is a **silent rewrite**. The factory **does not allow** silent rewrites.

If a request appears unsafe, emit **NEED HUMAN APPROVAL** or **STRUCTURE CHANGE** per [orchestration-signals-v0.md](orchestration-signals-v0.md) and **pause** until scope, trigger, and HITL anchor are explicit.

---

## 6. Regeneration boundaries

Every regeneration **must** name its **boundaries**:

| Boundary | Question to answer |
|----------|--------------------|
| **Content boundary** | Which fields / sections / blocks are regenerated? Which are preserved? |
| **Page / template boundary** | Which pages / templates are affected? |
| **Stage boundary** | Which workflow stage(s) ([website-factory-workflow-v0.md](website-factory-workflow-v0.md) §S01–S15) are re-entered? |
| **Lane boundary** | Which QA lanes ([qa-validation-model.md](qa-validation-model.md)) re-run? |
| **HITL boundary** | Which HITL gates ([workflow-map.md](workflow-map.md) §Artifact approval gates) are re-issued? |
| **Time boundary** | Within which execution scope (project / batch / release cycle)? |

Forbidden:

- regenerating an artifact while leaving its **declared scope** as "TBD";
- regenerating one artifact while ignoring its **upstream and downstream lineage**.

---

## 7. Regeneration triggers

| Trigger | Typical class | Notes |
|---------|----------------|-------|
| Upstream revision propagated invalidation ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)) | Partial or full regeneration of affected downstream artifacts. | Most common. |
| QA found content quality below threshold | Partial regeneration of the affected fields. | Distinct from a bounded CR; QA recommends regeneration when authoring quality is the issue. |
| HITL requested re-authoring | Partial or full regeneration. | HITL-driven; explicit scope in request. |
| Structural revision upstream | Full regeneration of affected downstream artifacts (or supersede). | Often combined with **STRUCTURE CHANGE**. |
| SAFE UNKNOWN resolved (new evidence) | Partial regeneration of the affected fields. | New evidence may invalidate prior SAFE UNKNOWN entries. |
| Security finding | Targeted regeneration (or supersede if scope is severe). | **SECURITY RISK** signal; HITL-mandatory. |

A regeneration **without** a recorded trigger is **unsafe**.

---

## 8. Dependency-aware regeneration

Regeneration **must respect** upstream/downstream dependencies ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)).

| Rule | Detail |
|------|--------|
| **Regenerate only when upstream is stable** | An artifact whose upstream is `draft` / `invalidated` / `superseded` / `deprecated` cannot be reliably regenerated; regeneration must wait or upstream must be stabilized first. |
| **Declare downstream impact** | The regeneration request enumerates which downstream artifacts move to `invalidated`. |
| **Cascade explicitly** | If regenerating Artifact A invalidates Artifacts B, C, D downstream, the regeneration request says so; B / C / D's owners are notified via REPORT. |
| **No partial regeneration when scope is structural** | A bounded CR-shaped regeneration that actually changes structure must be reclassified as full regeneration (or supersede) with **STRUCTURE CHANGE**. |

Dependency awareness is **prose discipline** in v0; no dependency graph engine is implied.

---

## 9. QA invalidation after regeneration

Per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md):

| Regeneration class | QA invalidation |
|--------------------|------------------|
| Partial | QA findings for the regenerated subset are **stale**; non-overlapping findings carry forward (explicit enumeration required). |
| Full | QA findings for the artifact are **fully stale**; re-QA in scope. |
| Cross-page partial | Per-page QA findings for affected pages are stale; non-affected pages preserve QA. |

Rules:

- A regeneration **does not** carry over prior QA verdicts implicitly.
- **Carry-forward findings** must be enumerated in the new QA REPORT with rationale.
- **Stale findings** that the new revision should be re-checked against are listed explicitly.
- A "regeneration passed QA" claim **without** a new QA REPORT is fabrication ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §4).

---

## 10. HITL anchoring

Regeneration is **HITL-anchored** at three points:

| Anchor | When |
|--------|------|
| **Opening** | HITL approves the regeneration request (scope + trigger + impact). Required for `frozen` artifacts; recommended for `approved` artifacts at risk of freeze break. |
| **Mid-flight** | HITL re-decides if scope widens beyond the approved boundary. |
| **Closing** | HITL re-gate at the artifact's standard gate (G1–G7 per [workflow-map.md](workflow-map.md)). |

Forbidden:

- agent-side regeneration that bypasses opening HITL;
- silent scope widening mid-regeneration;
- closing a regeneration without re-gate.

---

## 11. Relationship to revision and supersede

Regeneration vs revision vs supersede ([artifact-state-model-v0.md](artifact-state-model-v0.md) §9):

| Mechanism | Use when | New artifact_id? | New revision id? |
|-----------|----------|-------------------|------------------|
| **Revision** | Targeted edits to specific fields; scope is small. | No. | Yes. |
| **Regeneration (partial)** | Re-produce content for a bounded subset; authoring is fresh rather than incremental. | No. | Yes. |
| **Regeneration (full)** | Re-produce the entire artifact body; structural integrity remains. | No (usually). | Yes. |
| **Supersede** | New artifact entirely replaces the prior one; structural identity has shifted. | Yes. | n/a (new artifact_id starts at `draft`). |

Forbidden:

- treating full regeneration as supersede when the artifact_id should remain stable;
- treating supersede as regeneration when the artifact identity has changed.

The choice between regeneration and supersede is itself a **HITL decision** anchored in [approval-semantics-v0.md](approval-semantics-v0.md). When in doubt, escalate via **STRUCTURE CHANGE**.

---

## 12. No autonomous regeneration

Per [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md) and [safe-unknown-boundary.md](safe-unknown-boundary.md):

| Forbidden claim | Honest alternative |
|-----------------|---------------------|
| "AI auto-regenerated the entire project after the brand change." | Regeneration is a HITL-anchored, bounded, multi-prompt sequence. |
| "Regenerated all pages overnight." | Each affected artifact has its own regeneration request, prompt, QA, and HITL re-gate. |
| "Regenerated the blueprint and synced design / frontend automatically." | Regeneration of blueprint invalidates downstream; downstream regeneration is a separate sequence. |
| "Self-healing regeneration." | Self-Heal v0 is **plan-only** ([`../../interfaces/self-heal-v0.md`](../../interfaces/self-heal-v0.md)); regeneration plans are not executed automatically. |
| "Regeneration improved quality without any new evidence." | Regeneration requires a recorded trigger. |

The factory's regeneration model is **bounded, HITL-anchored, evidence-bearing prose discipline**.

---

## 13. Examples

These examples are **illustrative** and do not define new behaviors.

### 13.1 Regenerating hero copy across 5 landing pages

- **Trigger**: SEO QA found weak title / heading hierarchy on 5 pages.
- **Class**: Partial regeneration (cross-page).
- **Scope**: Hero section title + H1 + meta description on 5 named blueprint artifact_ids.
- **Upstream**: Strategy / SEO hypothesis `approved` (G2).
- **Downstream impact**: Design handoff hero-section visual map → minor revision; frontend production hero markup → revised.
- **QA reset**: SEO QA + Conversion QA per affected page.
- **HITL**: G3 re-gate on blueprint batch (limited scope); G5 / G6 as downstream stabilizes.

### 13.2 Full regeneration of design visual direction after brand pivot

- **Trigger**: HITL direction change.
- **Class**: Full regeneration (likely escalates to supersede if tokens / component set changes shape — see [§11](#11-relationship-to-revision-and-supersede)).
- **Scope**: `visual_direction`, `typography_direction`, `color_direction`, `component_variants` per [design-handoff-contract-v0.md](design-handoff-contract-v0.md).
- **Upstream**: Strategy `approved` (G2) with brand pivot recorded; design handoff revised.
- **Downstream impact**: Frontend handoff (component-state, asset list) → `invalidated`; frontend production → `invalidated`.
- **QA reset**: Design QA + Frontend QA visual lane.
- **HITL**: G5 re-gate (freeze break) + G6 re-gate.
- **Signal**: **STRUCTURE CHANGE** if scope warrants supersede.

### 13.3 Regenerating frontend source after responsive heuristic failure

- **Trigger**: Frontend QA found responsive heuristic failure on a component at mobile breakpoint.
- **Class**: Partial regeneration (component-scoped).
- **Scope**: Source for one component + its SCSS module + data-* event scope per [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md).
- **Upstream**: Frozen design (G5) + frozen blueprint (G3).
- **Downstream impact**: Frontend QA re-run; final validation re-run if release tag intent moves.
- **QA reset**: Frontend QA responsive + a11y categories.
- **HITL**: G6 re-gate.
- **Signal**: **SAFE UNKNOWN** if CI evidence absent.

---

## 14. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| "Regenerated everything." | Unbounded scope. | Enumerate scope per [§6](#6-regeneration-boundaries). |
| "Regenerated to fix unknown quality issues." | Trigger missing. | Record trigger per [§7](#7-regeneration-triggers); often a QA finding. |
| "Regeneration auto-passed QA." | QA reset bypassed. | Re-QA in scope per [§9](#9-qa-invalidation-after-regeneration). |
| "AI regenerated the project." | Autonomous claim. | Bounded, HITL-anchored, multi-prompt sequence. |
| "Regeneration without new revision id." | Lineage hidden. | New revision id per regeneration. |
| "Regenerated frozen artifact silently." | Freeze break. | HITL approval to open + new revision id. |
| "Regeneration treated as supersede." | Identity confusion. | Use supersede only when artifact identity changes. |
| "Partial regeneration applied to structural fields." | Class mismatch. | Reclassify as full regeneration or supersede; emit `STRUCTURE CHANGE`. |

---

## 15. Non-claims

- This document does **not** ship a regeneration engine.
- It does **not** assume an LLM autonomously regenerates artifacts.
- It does **not** define wire formats for regeneration metadata.
- It does **not** replace HITL judgment with predictable regeneration behavior.

What it **does** do is define **bounded, HITL-anchored, dependency-aware regeneration discipline** so re-producing artifact content remains **honest, traceable, and audit-bearing**.

---

## 16. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial regeneration semantics (documentation only). |
