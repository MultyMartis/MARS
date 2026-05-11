# MARS Website Factory — Dependency Invalidation v0

**Status:** **documentation only** — defines how **changes propagate** through the factory's stage / artifact / approval / QA / lane dependencies. **Not** a dependency graph engine, **not** an automatic cascade, **not** a runtime invalidation service.

**Version:** v0.

**Related:** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [stage-state-model-v0.md](stage-state-model-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), [design-handoff-contract-v0.md](design-handoff-contract-v0.md), [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [site-type-registry-v0.md](site-type-registry-v0.md), [block-registry-v0.md](block-registry-v0.md), [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [`../../governance/dependency-map.md`](../../governance/dependency-map.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md).

---

## 1. Purpose

Factory artifacts depend on each other. When an upstream artifact changes ([revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md)), downstream artifacts, approvals, and QA verdicts may become **stale**. This document defines:

- **what** propagates downstream when an upstream artifact changes;
- **how** invalidation is declared, acknowledged, and resolved;
- **which** stages, artifacts, approvals, QA lanes, and contract fields are affected by common change classes (site type, CTA, trust, blocks, mobile UX);
- **HITL anchoring** for partial reruns;
- **honesty boundary** — invalidation is **prose discipline**, not an automatic cascade.

---

## 2. What invalidation means

**Invalidation** is the **explicit declaration** that an artifact, approval, QA verdict, or stage instance is **stale** for the affected scope and **cannot** be consumed downstream as a valid baseline.

| Invalidation target | Effect |
|---------------------|--------|
| **Stage instance** | Moves to `invalidated` ([stage-state-model-v0.md](stage-state-model-v0.md) §2) until rerun. |
| **Artifact revision** | Moves to `invalidated` ([artifact-state-model-v0.md](artifact-state-model-v0.md) §2) until revised / regenerated. |
| **Approval** | Inherited approval is **broken** for the affected scope ([approval-semantics-v0.md](approval-semantics-v0.md) §7). Direct approval may be **revoked** ([approval-semantics-v0.md](approval-semantics-v0.md) §9). |
| **QA verdict** | Becomes **stale** ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)) for the affected scope. |
| **Delivery candidate** | Cannot be released without re-validation ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md)). |

Invalidation is **not silent staleness**. A downstream artifact that **could** be stale but has **not been invalidated** continues to represent the last-approved baseline. Honest factory practice is to **explicitly invalidate** what changes affected.

---

## 3. Upstream vs downstream invalidation

| Direction | Definition |
|-----------|-------------|
| **Upstream invalidation** | When a downstream stage discovers that an **upstream** artifact would need to change to satisfy its objective ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §5 re-gate rule). The downstream stage **stops** and requests an upstream re-gate; until upstream stabilizes, the downstream stage stays `blocked` or `invalidated`. |
| **Downstream invalidation** | When an **upstream** change propagates **forward** to downstream artifacts, approvals, and QA verdicts. The downstream stage instances move from `approved` / `frozen` to `invalidated` for the affected scope. |

Most factory invalidations are **downstream propagations** triggered by upstream revisions or regenerations. Upstream invalidations are less common and usually require **STRUCTURE CHANGE** ([orchestration-signals-v0.md](orchestration-signals-v0.md)).

---

## 4. Artifact dependency chains

The canonical upstream → downstream chain follows [website-factory-workflow-v0.md](website-factory-workflow-v0.md) §"Artifact flow map":

```text
Intake artifact
  → Strategy artifact + SEO strategy artifact
    → IA artifact
      → Blueprint artifact (per page / per template)
        → QA artifact (blueprint slice)
        → Design handoff artifact
          → Design artifact
            → QA artifact (design lane)
            → Frontend handoff artifact
              → Frontend production artifact
                → QA artifact (frontend lane)
                → Validation artifact (final)
                  → Approval artifact (release)
                    → Delivery artifact
```

Dependency rules:

- A downstream artifact **depends on** every upstream artifact that its production prompt consumed ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §2).
- Dependencies are **cited explicitly** in lineage ([artifact-state-model-v0.md](artifact-state-model-v0.md) §6).
- Cross-stage **reach-throughs** are recorded explicitly; silent reach-throughs are forbidden ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §9).
- **Registries** ([site-type-registry-v0.md](site-type-registry-v0.md), [block-registry-v0.md](block-registry-v0.md)) are **shared dependencies**: a registry amendment can invalidate many artifacts simultaneously.

---

## 5. Stage invalidation propagation

| Upstream stage state change | Downstream stage propagation |
|------------------------------|------------------------------|
| `frozen → in_review` (freeze break) | All downstream stage instances that consumed the prior frozen baseline move from `approved` / `frozen` to `invalidated` **for the affected scope**. |
| `approved → in_review` (revision before freeze) | Downstream stages in `executing` or `qa_review` for the affected scope move to `blocked` until the upstream revision stabilizes. |
| `approved → invalidated` | Downstream stages cascade to `invalidated`. |
| `frozen → invalidated` | Downstream stages cascade to `invalidated`. |
| `approved → rejected` | Downstream stages cascade to `invalidated`. |
| `executing` re-entry on upstream | Downstream stages remain `blocked` until upstream stabilizes. |

Propagation rules:

- Propagation is **scope-bounded**, not blanket. A revision affecting one page typically does not invalidate downstream stages for other pages.
- Propagation is **declared in the REPORT** for the revising stage and **acknowledged in the REPORT** for the affected downstream stage.
- Propagation **never** auto-rerun downstream stages; rerun is a HITL-anchored decision ([regeneration-semantics-v0.md](regeneration-semantics-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md)).

---

## 6. QA invalidation

Per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md):

| Cause | Effect on QA |
|-------|--------------|
| Upstream artifact revised / regenerated | QA verdicts for the affected scope on **the revised artifact and all downstream artifacts** become **stale**. |
| Registry amendment | QA verdicts that depended on registry rows for compatibility / classification become stale. |
| Contract amendment | QA verdicts that asserted contract conformance under the prior version become stale. |
| HITL revocation of approval | QA verdicts tied to the revoked approval become stale (verdict was per revision; revocation invalidates the revision baseline). |

QA-invalidation rules:

- Stale verdicts **are preserved** in QA history (append-only audit).
- Re-running QA produces **new verdicts** attached to the new revision id.
- A "QA passed before, so it still passes" claim after upstream change is forbidden — re-assess in scope.

---

## 7. Approval invalidation

Per [approval-semantics-v0.md](approval-semantics-v0.md):

| Cause | Effect on approval |
|-------|---------------------|
| Upstream artifact moves to `invalidated` / `superseded` / `deprecated` | Inherited approval at the downstream gate is **broken** for the affected scope. |
| Approval explicitly revoked under HITL | Direct approval is **revoked**; downstream inherited approval is broken. |
| Approval expires | Approval is no longer valid for **future** consumption ([approval-semantics-v0.md](approval-semantics-v0.md) §8). |
| `SECURITY RISK` finding on the approved scope | Approval is provisionally **frozen pending re-review**; HITL revocation expected. |

Approval-invalidation rules:

- An invalidated approval is **recorded as a revocation event** ([approval-semantics-v0.md](approval-semantics-v0.md) §9) when explicitly revoked, or as a **broken inheritance** entry when upstream propagation applies.
- Downstream stages **cannot rely** on a broken or revoked approval; they move to `blocked` or `invalidated` until a new approval is recorded.
- Approval-invalidation is **never silent**.

---

## 8. Frontend invalidation

Frontend artifacts ([frontend-artifact-model-v0.md](frontend-artifact-model-v0.md), [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md)) are **last in the chain** and therefore among the most frequently invalidated.

| Upstream cause | Frontend impact |
|-----------------|------------------|
| Blueprint revision (CTA / section / content) | Frontend handoff for affected blueprint → `invalidated`; frontend source files for affected sections → `invalidated`. |
| Design revision (visual direction / tokens / component variants) | Frontend handoff (component-state, asset list, breakpoint behavior) → `invalidated`; frontend source for affected components → `invalidated`. |
| IA revision (URL pattern / routing) | Frontend handoff for affected URLs → `invalidated`; frontend production routing → `invalidated`. |
| Site type pivot | Most frontend artifacts → `invalidated` or `superseded`. |
| Block registry amendment | Frontend components mapped to revised blocks → `invalidated`. |
| Frontend QA finding (heuristic / responsive / a11y) | Frontend production source affected → `invalidated` until revised; downstream final validation → `invalidated`. |

Frontend invalidation **always** invalidates dependent Frontend QA verdicts ([§6](#6-qa-invalidation)).

---

## 9. SEO invalidation

SEO artifacts (SEO strategy artifact, blueprint `seo_intent` per [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), SEO QA verdicts) invalidate when:

| Upstream cause | SEO impact |
|-----------------|-------------|
| Strategy revision (positioning / funnel) | SEO strategy artifact → `invalidated`; blueprint `seo_intent` for affected pages → `invalidated`. |
| IA revision (URL pattern / template structure) | Blueprint `seo_intent` (URL, heading hierarchy, meta) → `invalidated`. |
| Blueprint revision (titles, headings, schema) | SEO QA verdicts for the affected page → stale. |
| Site type pivot | Full SEO re-assessment. |
| New evidence on SERP / competitive landscape (out-of-band) | SEO strategy artifact may move to revision under HITL. |

SEO invalidation **does not** automatically invalidate frontend; only if the SEO revision changes blueprint fields that frontend consumes (titles, meta, schema markers).

---

## 10. Design invalidation

Design artifacts ([design-handoff-contract-v0.md](design-handoff-contract-v0.md), design production artifact, Design QA verdicts) invalidate when:

| Upstream cause | Design impact |
|-----------------|----------------|
| Blueprint revision (sections, CTA, trust) | Design handoff `section_visual_map`, `component_variants` for affected sections → `invalidated`; design production for affected pages → `invalidated`. |
| Strategy / brand revision | Design handoff `visual_direction`, `typography_direction`, `color_direction` → `invalidated`. |
| Site type pivot | Full design re-assessment (often supersede). |
| Block registry amendment | Design handoff for revised blocks → `invalidated`. |
| Mobile UX revision (breakpoint behavior) | Design handoff `responsive_behavior` → `invalidated`. |

Design invalidation cascades to frontend (per [§8](#8-frontend-invalidation)) when the design changes anchor frontend handoff fields.

---

## 11. Common change examples

The following examples are **illustrative** and align with [website-factory-workflow-v0.md](website-factory-workflow-v0.md). They do not introduce new behaviors beyond §1–§10.

### 11.1 Site type changed

| Aspect | Detail |
|--------|--------|
| **Upstream** | Site type classification artifact (S02) revised: e.g. landing page → e-commerce. |
| **Signal** | **STRUCTURE CHANGE** (likely supersede on many downstream artifacts). |
| **Invalidation cascade** | Strategy artifact, SEO strategy, IA artifact, blueprint set, design handoff, design artifact, frontend handoff, frontend production, all QA artifacts → `invalidated` (some → `superseded` if a new artifact_id is opened). |
| **Approval invalidation** | All G1+ approvals broken for affected scope. |
| **HITL** | G1 re-gate; G2 re-gate; G3 re-gate; downstream gates as stages stabilize. |
| **Rerun scope** | Often the entire downstream chain; per-artifact decisions about revision vs supersede are HITL-driven. |

### 11.2 CTA model changed

| Aspect | Detail |
|--------|--------|
| **Upstream** | Strategy / Conversion intent revision: CTA model shifts (e.g. from "book demo" to "start free trial"). |
| **Signal** | None mandatory if scoped; **STRUCTURE CHANGE** if funnel topology changes. |
| **Invalidation cascade** | Blueprint `CTA_strategy`, `conversion_points` per [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md) → `invalidated`; design handoff CTA-bearing sections → `invalidated`; design artifact CTA staging → revised; frontend production CTA components → revised. |
| **QA invalidation** | Conversion QA, SEO QA (if CTA copy affects metadata), Frontend QA (if click events affected) → stale. |
| **Approval invalidation** | G2 (commercial scope) re-gate; G3 (blueprint) re-gate; G5 / G6 as downstream stabilizes. |
| **Rerun scope** | Field revision or partial regeneration on blueprint CTA fields and downstream consumers. |

### 11.3 Trust model changed

| Aspect | Detail |
|--------|--------|
| **Upstream** | Trust semantics revision ([trust-semantics-v0.md](trust-semantics-v0.md)): added compliance badge / removed unverifiable claim. |
| **Signal** | **SECURITY RISK** if compliance / legal driven; otherwise **NEED HUMAN APPROVAL**. |
| **Invalidation cascade** | Blueprint `trust_signals` / trust blocks → `invalidated`; design handoff trust visual surfaces → `invalidated`; design / frontend production trust sections → revised. |
| **QA invalidation** | Conversion QA (trust honesty), SEO QA (schema honesty if relevant), Validator overlap (policy) → stale. |
| **Approval invalidation** | G2 / G3 re-gate; G5 / G6 as downstream stabilizes. |
| **Rerun scope** | Often partial regeneration on trust-bearing fields; legal review required when compliance scope changes. |

### 11.4 Block structure changed

| Aspect | Detail |
|--------|--------|
| **Upstream** | Block Registry amendment ([block-registry-v0.md](block-registry-v0.md)) under governance: new block id, retired block id, or changed semantic mapping. |
| **Signal** | **STRUCTURE CHANGE**. |
| **Invalidation cascade** | Blueprints that use affected blocks → `invalidated` (block ordering, semantic mapping fields); design handoff for affected blocks → `invalidated`; frontend production for affected components → `invalidated`. |
| **QA invalidation** | Blueprint QA (block validity), Design QA (semantic → visual), Frontend QA (component conformance) → stale. |
| **Approval invalidation** | G3 re-gate; G5 / G6 as downstream stabilizes. |
| **Rerun scope** | Field or structural revision per affected blueprint + downstream. |

### 11.5 Mobile UX changed

| Aspect | Detail |
|--------|--------|
| **Upstream** | Design / Design QA revision: mobile breakpoint behavior changes (e.g. hamburger nav redesign, mobile CTA placement). |
| **Signal** | None mandatory; **STRUCTURE CHANGE** if it forces handoff shape change. |
| **Invalidation cascade** | Design handoff `responsive_behavior` → revised; frontend handoff breakpoint notes → revised; frontend production mobile CSS / JS → `invalidated` for affected components. |
| **QA invalidation** | Design QA (mobile fidelity), Frontend QA (responsive heuristic) → stale. |
| **Approval invalidation** | G5 re-gate (if freeze breaking); G6 re-gate on frontend. |
| **Rerun scope** | Partial regeneration on mobile-affected components. |

---

## 12. Acknowledgment discipline

Every invalidation **must** be acknowledged in the **revising stage's REPORT** and in the **affected downstream stage's REPORT** ([reporting-standard-v0.md](reporting-standard-v0.md)).

Required fields in the REPORT:

| Field | Content |
|-------|---------|
| **invalidating stage** | Stage id + revision id. |
| **invalidating artifact(s)** | artifact_id + revision id + state transition. |
| **affected downstream stages** | Stage id list. |
| **affected downstream artifacts** | artifact_id + revision id list. |
| **affected QA verdicts** | QA artifact references that are now stale. |
| **affected approvals** | Approval artifact references that are now broken or revoked. |
| **HITL anchor** | Approver(s) consulted / required. |
| **rerun plan** | Revision class ([revision-semantics-v0.md](revision-semantics-v0.md)) or regeneration class ([regeneration-semantics-v0.md](regeneration-semantics-v0.md)) per affected artifact. |

A revision or regeneration that does **not** acknowledge its downstream invalidation impact is **incomplete** and must be rejected at re-gate.

---

## 13. HITL anchoring for partial rerun

A **partial rerun** rebuilds only the affected downstream slice rather than the full chain. Per [regeneration-semantics-v0.md](regeneration-semantics-v0.md) §6 + §10:

- A partial rerun **requires** HITL approval of the **scope** of the rerun.
- Partial rerun scope is enumerated: which artifacts, which pages, which lanes, which stages.
- Partial rerun **does not** require rerunning unaffected downstream artifacts.
- Partial rerun **does** require re-QA on the affected scope.
- Partial rerun **does** require re-gate on the affected scope.

Forbidden:

- "We can probably skip the design re-gate since the change was small" — re-gate is HITL-anchored, not opinion-anchored.
- "We'll rerun everything to be safe" — unbounded rerun is unsafe regeneration ([regeneration-semantics-v0.md](regeneration-semantics-v0.md) §5).

---

## 14. Tie to MARS dependency map

The MARS-wide [`../../governance/dependency-map.md`](../../governance/dependency-map.md) tracks **system-level entity → entity edges**. The Website Factory invalidation model is **scoped** to Website Factory artifact and stage dependencies; it **does not** replace or duplicate the dependency map's entity rows.

When future Control Plane work binds factory artifacts to dependency-map entities ([`../../mars-runtime/run-lifecycle-v0.md`](../../mars-runtime/run-lifecycle-v0.md)), the invalidation rules here will inform **runtime-level cascade design** — but until then, invalidation remains **prose discipline**.

---

## 15. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| "Invalidation cascade ran automatically." | No engine exists. | Acknowledge invalidation in REPORT; rerun is HITL-anchored. |
| "Downstream artifact was fine since QA was old." | Stale QA assumed pass. | Mark downstream QA stale; re-assess. |
| "We only invalidated the artifact, not the QA." | QA staleness omitted. | Invalidate QA verdicts too. |
| "Approval still valid since artifact was only minorly revised." | Approval scope ignored. | Re-gate per [approval-semantics-v0.md](approval-semantics-v0.md). |
| "Skipped invalidation because change felt cosmetic." | Silent staleness. | Even cosmetic revisions create new revision ids and need explicit invalidation acknowledgment. |
| "Partial rerun without scope enumeration." | Unbounded rerun. | Enumerate scope; HITL approval of partial rerun scope. |
| "Block registry change applied to one project, ignored others." | Cross-project staleness. | Registry amendments are governed; affected projects must acknowledge. |

---

## 16. Non-claims

- This document does **not** ship a dependency graph engine.
- It does **not** assume any automatic cascade.
- It does **not** define wire formats for invalidation events.
- It does **not** replace HITL judgment with predictable invalidation behavior.

What it **does** do is define **how propagation is named, declared, acknowledged, and resolved** so factory changes do not silently invalidate downstream baselines.

---

## 17. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial dependency invalidation semantics (documentation only). |
