# MARS Website Factory — Revision Semantics v0

**Status:** **documentation only** — defines how **revisions** to approved or frozen artifacts behave in the factory. **Not** a revision engine, **not** a versioning service, **not** an automated diff / merge tool.

**Version:** v0.

**Related:** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [stage-state-model-v0.md](stage-state-model-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md), [artifact-types-v0.md](artifact-types-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Purpose

A **revision** is a **deliberate, scope-bounded change** to an artifact that is **already past `draft`** ([artifact-state-model-v0.md](artifact-state-model-v0.md) §2). [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §6 names revision **types**; [artifact-state-model-v0.md](artifact-state-model-v0.md) §9 names revision as one of three replacement mechanisms.

This document defines:

- when a revision **may** be requested;
- what **scope** a revision covers;
- what **lineage** a revision creates;
- who **owns** a revision;
- what **impact** a revision causes;
- when a revision **breaks freeze**;
- when a revision **escalates** to STRUCTURE CHANGE / SECURITY RISK;
- how QA **resets** after a revision;
- how revision **history** is preserved.

A revision is **not** a regeneration ([regeneration-semantics-v0.md](regeneration-semantics-v0.md)), **not** a supersede ([artifact-state-model-v0.md](artifact-state-model-v0.md) §9), **not** a rollback ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) §rollback).

---

## 2. Revision requests

A revision request is a **prompt** (and accompanying HITL decision when required) that identifies:

| Field | Content |
|-------|---------|
| **artifact_id** | Stable artifact identifier ([artifact-types-v0.md](artifact-types-v0.md)). |
| **current revision** | The revision id being revised. |
| **target revision** | The new revision id that will result (e.g. `v1` → `v1.1`, or `v1` → `v2` for structural revision). |
| **scope** | Which fields, sections, pages, or sub-artifacts are in scope. |
| **trigger** | QA finding / HITL request / upstream invalidation / SECURITY RISK / SAFE UNKNOWN gap / STRUCTURE CHANGE. |
| **expected downstream impact** | Which downstream artifacts are likely to move to `invalidated` ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)). |
| **HITL gate** | Whether a HITL approval is required to **open** the revision (e.g. freeze breaking) and to **close** it (re-gate). |

A revision request that omits scope is **not** a revision — it is a redo. The factory forbids unbounded redo.

---

## 3. Revision scope

Revision scope is **always bounded** and falls into one of four classes:

| Class | Description | Typical revision id pattern |
|-------|--------------|------------------------------|
| **Bounded CR** | Address a defined list of QA-found corrections within an artifact's current revision boundary. | `v1` → `v1.1`. |
| **Field revision** | Change one or a few named fields (e.g. CTA label, trust block, meta description). | `v1` → `v1.1` or `v1.2`. |
| **Structural revision** | Change structural fields (e.g. blueprint block ordering, site_type_id, IA branch). Often accompanied by `STRUCTURE CHANGE`. | `v1` → `v2`. |
| **Cross-page revision** | Apply a revision pattern across a defined batch of artifacts (e.g. updated CTA model across 10 pages). | New revision per artifact_id, coordinated by batch id in REPORT. |

Forbidden:

- silently widening scope mid-revision;
- treating a structural revision as a bounded CR (and vice versa);
- batch revisions without explicit enumeration of affected artifact_ids.

Scope widening **requires** a new revision request (or escalation to **STRUCTURE CHANGE**).

---

## 4. Revision lineage

Every revision creates a **lineage row** for the artifact:

| Field | Rule |
|-------|------|
| **predecessor_revision** | Stable reference to the prior revision id. |
| **current_revision** | The new revision id. |
| **scope** | Recorded scope per [§3](#3-revision-scope). |
| **trigger** | Recorded trigger per [§2](#2-revision-requests). |
| **approver** (if HITL-opened) | Named approver who authorized opening the revision. |
| **closing_approver** | Named approver at re-gate. |
| **QA history** | All QA findings for prior revisions remain attached to their revision ids; new findings open against the current revision ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)). |

A revision **never** deletes prior lineage. Prior revisions move to `superseded` for the **active baseline**, but remain in audit ([artifact-state-model-v0.md](artifact-state-model-v0.md) §9).

---

## 5. Revision ownership

| Revision class | Owner | Approver(s) |
|----------------|--------|-------------|
| Bounded CR | Stage's primary owner role ([stage-state-model-v0.md](stage-state-model-v0.md) §7). | Same gate as original approval (G3 / G5 / G6 / etc.). |
| Field revision | Stage's primary owner. | Same gate; HITL may delegate to a narrower role where scope is small (recorded in Approval artifact). |
| Structural revision | Stage's primary owner + relevant upstream owners if scope crosses stage boundaries. | **STRUCTURE CHANGE** typically requires re-approval at the affected upstream gate. |
| Cross-page revision | PM coordinates; per-page owner roles execute. | Batch HITL approval. |

The QA lane ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §10) **does not** own revisions; QA recommends, HITL approves, production owners execute.

---

## 6. Revision impact

Revisions cause **explicit downstream impact** per [dependency-invalidation-v0.md](dependency-invalidation-v0.md):

| Revision class | Typical downstream impact |
|----------------|----------------------------|
| Bounded CR | Often no invalidation; downstream may continue if CRs do not intersect downstream consumption. |
| Field revision | Localized invalidation — downstream artifacts that reference the revised field move to `invalidated` for the affected scope. |
| Structural revision | Broad invalidation — most downstream artifacts that depend on the revised structure move to `invalidated`. |
| Cross-page revision | Batch invalidation across the affected pages' downstream artifacts. |

Impact rules:

- Impact is **declared in the revision request** and **acknowledged in the closing REPORT**.
- Downstream invalidation is **not** automatic state propagation — it is a **prose entry** in the REPORT that downstream owners read and act on.
- "Revision had no downstream impact" requires evidence (the revised fields are not referenced downstream).

---

## 7. Revision freeze breaking

A revision that targets a `frozen` artifact ([artifact-state-model-v0.md](artifact-state-model-v0.md) §3) is a **freeze break**.

| Aspect | Detail |
|--------|--------|
| **Trigger** | HITL-authorized revision request on a frozen artifact. |
| **Authority** | Same or higher-authority approver as the original freeze approval. |
| **Recording** | Revision lineage entry + Approval artifact for the reopen. |
| **State transitions** | Artifact: `frozen → in_review` (after authoring); stage: `frozen → executing` ([stage-state-model-v0.md](stage-state-model-v0.md) §9). |
| **Downstream effect** | Downstream artifacts that consumed the frozen baseline move to `invalidated` for affected scope. |
| **Forbidden** | Silent freeze breaking; "small tweak" without HITL; mid-revision scope widening without new HITL pass. |

A freeze break is **not** routine. Most revisions occur **before freeze** (i.e. on `approved` artifacts). Freeze breaks should be the **exception** and should be recorded as such in lineage and REPORT bodies.

---

## 8. Revision escalation

Some revisions escalate beyond a single stage:

| Trigger | Escalation signal | Effect |
|---------|--------------------|--------|
| Revised fields force a contract shape change | **STRUCTURE CHANGE** ([`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md)) | New `artifact_id` (or major version bump); upstream stages re-plan affected slices. |
| Revision arises from a security finding | **SECURITY RISK** | Stop line; emergency revision with HITL; never silent. |
| Revision arises from a missing binding | **UNKNOWN** | Hard stop until binding resolved; revision request may stall. |
| Revision arises from bounded uncertainty | **SAFE UNKNOWN** | Bounded continuation per [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md); HITL approval for the bounded scope. |
| Revision arises from a contract gap | **STRUCTURE CHANGE** | Contract amendment under governance + revised artifact. |

Escalation rules:

- The escalation signal appears in the **revision request prompt** AND in the **closing REPORT** ([reporting-standard-v0.md](reporting-standard-v0.md)).
- **Multiple signals** may apply to a single revision; enumerate all.
- Escalation **does not** retroactively classify all prior revisions; each revision carries its own signal set.

---

## 9. Revision QA reset

Per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md):

| Revision class | QA reset behavior |
|----------------|--------------------|
| Bounded CR | QA findings for the CR items are re-evaluated; QA history for other findings carries forward to the new revision. |
| Field revision | QA findings that intersect the revised field are reset; non-intersecting findings carry forward. |
| Structural revision | All QA findings for affected categories are reset; QA reruns the affected categories. |
| Cross-page revision | Batch QA: per-page QA findings reset per affected page. |

Rules:

- QA verdicts **do not** carry over silently from a prior revision; the new revision is re-assessed in scope.
- Findings that are **explicitly carried forward** must be enumerated in the new QA REPORT with rationale.
- A revision **does not** auto-resolve findings — only QA re-assessment + HITL waiver / resolution can close findings.

---

## 10. Revision history philosophy

Revision history is **append-only audit**:

| Principle | Detail |
|-----------|--------|
| **Never delete** | Prior revision content remains in lineage; superseded for active baseline ([artifact-state-model-v0.md](artifact-state-model-v0.md) §9). |
| **Always cite** | New revision lineage cites predecessor revision id explicitly. |
| **Reason-bearing** | Each revision lineage row names the trigger and scope. |
| **HITL-traceable** | Approval artifacts attach to revision lineage rows. |
| **QA-traceable** | QA verdicts attach per revision; carry-forward findings are explicitly enumerated. |

Forbidden:

- silent overwrite of an artifact body without a revision lineage entry;
- "rebased" revisions that hide intermediate work;
- merging revisions across artifact_ids.

History is **prose discipline** in v0; no versioning service is implied. Project-level conventions for revision id format (e.g. `v1.0.0` vs `2026-05-11-rev2`) are out of scope; consistency within a project is recommended.

---

## 11. Revision examples

The following examples are **illustrative** and align with [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), [design-handoff-contract-v0.md](design-handoff-contract-v0.md), and [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md). They do **not** define new behaviors beyond §2–§10.

### 11.1 Changing CTA

| Aspect | Detail |
|--------|--------|
| **Trigger** | Conversion QA finding: CTA model mismatch with funnel narrative ([cta-semantics-v0.md](cta-semantics-v0.md)). |
| **Revision class** | Field revision on blueprint artifact (CTA fields) + propagated CR on design / frontend handoff. |
| **Scope** | CTA label, CTA destination, CTA staging per affected pages. |
| **Downstream impact** | Design handoff (`section_visual_map` for CTA-bearing sections) → `invalidated` for affected pages; frontend handoff (CTA target paths, click events) → `invalidated`; design / frontend production → `invalidated` for affected pages. |
| **QA reset** | Conversion QA + SEO QA (if CTA copy changed metadata) re-runs on affected pages. |
| **HITL** | G3 re-gate on blueprint batch (commercial scope); G5 re-gate on design (if visual changes); G6 re-gate on frontend. |
| **Signal** | None mandatory; **SAFE UNKNOWN** if conversion target uncertain. |

### 11.2 Changing site type

| Aspect | Detail |
|--------|--------|
| **Trigger** | HITL discovery that the site is not a landing page but an e-commerce catalog (Site Type Registry mismatch). |
| **Revision class** | Structural revision — `STRUCTURE CHANGE`. |
| **Scope** | `site_type_id` on intake / classification artifact; cascades to strategy, SEO, IA, blueprint, design, frontend. |
| **Downstream impact** | All downstream artifacts move to `invalidated` for the affected scope; many require `superseded` rather than revised (new artifact_ids). |
| **QA reset** | Full QA reset for affected lanes. |
| **HITL** | G1 re-gate on intake; G2 re-gate on strategy; G3 re-gate on IA / blueprint; G5 / G6 as downstream stabilizes. |
| **Signal** | **STRUCTURE CHANGE**; possibly **SAFE UNKNOWN** during transition. |

### 11.3 Changing IA

| Aspect | Detail |
|--------|--------|
| **Trigger** | Strategy approval extension requires new URL pattern / template. |
| **Revision class** | Structural revision on IA artifact. |
| **Scope** | Sitemap nodes, URL pattern, template assignment for affected branches. |
| **Downstream impact** | Blueprint artifacts for affected URLs → `invalidated`; design handoff for affected templates → `invalidated`; frontend handoff → `invalidated`. |
| **QA reset** | SEO QA (URL / heading hierarchy), Conversion QA (funnel reachability), Frontend QA (routing) re-run on affected pages. |
| **HITL** | G3 re-gate on IA + blueprint batch. |
| **Signal** | **STRUCTURE CHANGE** if scope shifts; otherwise field revision. |

### 11.4 Changing visual direction

| Aspect | Detail |
|--------|--------|
| **Trigger** | Brand pivot or client direction change post-G4. |
| **Revision class** | Structural revision on design artifact (or supersede if total redesign). |
| **Scope** | `visual_direction`, `typography_direction`, `color_direction`, `component_variants` per [design-handoff-contract-v0.md](design-handoff-contract-v0.md). |
| **Downstream impact** | Frontend handoff (component-state, asset list, breakpoint behavior) → `invalidated`; frontend production source → `invalidated` for affected components. |
| **QA reset** | Design QA, Frontend QA (visual fidelity, responsive) re-run. |
| **HITL** | G5 re-gate (design freeze break); G6 re-gate on frontend if visual changes propagate. |
| **Signal** | **STRUCTURE CHANGE** if tokens / component set changes shape; otherwise field revision. |

### 11.5 Changing frontend structure

| Aspect | Detail |
|--------|--------|
| **Trigger** | Build-time discovery that an agreed component does not satisfy responsive / accessibility heuristic; or change in static-stack decision (within static feasibility per [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md)). |
| **Revision class** | Field revision (component refactor within agreed handoff) or structural revision (handoff shape change). |
| **Scope** | Source files; component templates; SCSS module organization; data-* attributes per [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md). |
| **Downstream impact** | Frontend production source → revised; Frontend QA → re-run; final validation → re-run if release tag intent moves. |
| **QA reset** | Frontend QA (build, semantics, responsive, JS scope). |
| **HITL** | G6 re-gate on frontend PR / file set; if structural, also re-confirm tech-lead handoff approval. |
| **Signal** | **SAFE UNKNOWN** for CI / hosting if not evidenced; **STRUCTURE CHANGE** if static feasibility itself is in question. |

---

## 12. Tie to artifact-transfer-prompt-rules

This document **realizes** [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §6 ("Revision handling"). Conflicts must be resolved in favor of the **operational** semantics here for **lifecycle behavior**, while §6 remains the **prompt-discipline** anchor.

| §6 row | This document's anchor |
|--------|------------------------|
| Bounded CR | [§3](#3-revision-scope) class **Bounded CR** + [§9](#9-revision-qa-reset). |
| Structure change | [§3](#3-revision-scope) class **Structural revision** + [§8](#8-revision-escalation). |
| Security override | [§8](#8-revision-escalation) **SECURITY RISK** row. |
| Supersede | Use [artifact-state-model-v0.md](artifact-state-model-v0.md) §9 supersede mechanism (revision is **not** supersede). |

---

## 13. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| "Quick tweak — no revision id needed." | Silent body mutation. | New revision id + lineage entry. |
| "Same revision id, new scope." | Hidden scope change. | New revision id per scope change. |
| "Revision auto-resolves prior findings." | QA reset bypassed. | Re-assess in scope; carry-forward findings explicit. |
| "Frozen artifact revised without HITL." | Freeze break. | HITL approval to open + new revision id. |
| "Structural revision marked as bounded CR." | Severity hidden. | Recognize as structural; emit `STRUCTURE CHANGE`. |
| "Revision impact ignored because downstream was already mid-flight." | Silent invalidation. | Mark downstream as `invalidated` per [dependency-invalidation-v0.md](dependency-invalidation-v0.md). |
| "Revision merged across artifact_ids." | Lineage destroyed. | Per-artifact revision; cross-reference in REPORT. |

---

## 14. Non-claims

- This document does **not** ship a versioning service.
- It does **not** assume a runtime tracks revisions automatically.
- It does **not** define a wire format for revision metadata.
- It does **not** replace HITL judgment with predictable revision behavior.

What it **does** do is define **the lifecycle behavior of revisions** so changes to approved or frozen artifacts remain **bounded, traceable, and HITL-anchored**.

---

## 15. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial revision semantics (documentation only). |
