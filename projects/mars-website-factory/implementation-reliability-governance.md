# MARS Website Factory — Implementation Reliability Governance

**Status:** **documented** — Website Factory implementation reliability governance and human-supervised frontend stability methodology only.  
**Not:** runtime frontend engine, autonomous repair AI, universal frontend architecture, CSS framework mandate, rebuild daemon, or automated regression enforcement.

**Core principle:** frontend implementation quality includes **stability over time**.  
It is not merely “works right now,” “looks correct,” or “passes build.”

**Companion documents:** [frontend-stability-model.md](frontend-stability-model.md), [implementation-drift-taxonomy.md](implementation-drift-taxonomy.md).  
**Related layers:** [design-token-intelligence-governance.md](design-token-intelligence-governance.md), [responsive-intent-governance.md](responsive-intent-governance.md), [source-interpretation-governance.md](source-interpretation-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [compositional-structure-awareness.md](compositional-structure-awareness.md), [qa-confidence-governance.md](qa-confidence-governance.md), [governance-prioritization.md](governance-prioritization.md), [human-escalation-governance.md](human-escalation-governance.md), [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md), [temporal-evolution-governance.md](temporal-evolution-governance.md), [operational-workflow-governance.md](operational-workflow-governance.md), [production-readiness-governance.md](production-readiness-governance.md), [failure-recovery-governance.md](failure-recovery-governance.md), [cross-project-transfer-governance.md](cross-project-transfer-governance.md).  
**Forge checklist:** [`../../agents/mars-forge/implementation-reliability-checklist.md`](../../agents/mars-forge/implementation-reliability-checklist.md).

---

## 1. Positioning

Implementation Reliability Governance formalizes the stability layer that sits after source interpretation, visual intent, responsive intent, interaction/state/accessibility intent, and token intelligence.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Stability, predictability, maintainability, scoped evolution, and regression survivability | One mandatory frontend stack, architecture, framework, or CSS methodology |
| Human-supervised implementation reliability QA before freeze | Automated CSS linting, self-healing frontend, or hidden runtime enforcement |
| Drift vocabulary for fragile CSS, include-chain contamination, unsafe overrides, and patch accumulation | Redesigning Triumph or any other project |
| Deterministic production frontend philosophy | A claim that Website Factory contains a runtime frontend engine |

The governance question is not “does the page currently render?”  
The governance question is: **can this implementation survive future scoped changes without hidden coupling, regression cascades, breakpoint collapse, or unreadable patch layering?**

---

## 2. Canonical Definition

**Implementation reliability** is the discipline of building frontend code so that future operators can safely understand, modify, rebuild, and validate it.

It preserves:

- **Stability** — scoped changes do not unpredictably disturb unrelated sections.
- **Predictability** — selectors, includes, breakpoints, tokens, and JS hooks behave from visible ownership.
- **Maintainability** — future fixes remain understandable without archaeology.
- **Controlled evolution** — changes have bounded scope and explicit escalation paths.
- **Regression survivability** — frozen or previously validated sections resist accidental damage.
- **Implementation clarity** — the code explains its structure through naming, scope, and composition.

A correct-looking frontend may still be structurally fragile when it depends on hidden overrides, global selector accidents, breakpoint hacks, include-order luck, duplicated implementations, or unexplained local fixes.

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Implementation reliability** | The ability of frontend source to remain stable, readable, rebuildable, and safely modifiable over time. |
| **Frontend stability** | A state where structure, styles, behavior, breakpoints, and includes can absorb scoped changes without unexpected regression. |
| **Deterministic rebuild** | Re-running the same build path from the same source produces the same intended artifact without manual patch steps, hidden local state, or include-order luck. |
| **Implementation entropy** | Accumulated complexity from patches, overrides, duplication, selector escalation, and undocumented exceptions. |
| **Regression survivability** | Previously validated sections remain intact after adjacent or scoped edits. |
| **Implementation coupling** | A dependency between files, selectors, includes, breakpoints, hooks, or tokens that can spread change impact. |
| **Structural fragility** | A page or section works only because current DOM, CSS order, breakpoint order, or include order happens to align. |
| **Override risk** | The chance that local exceptions, utility overrides, or specificity escalation leak beyond the intended scope. |
| **Implementation contamination** | Code inherits behavior, styling, include assumptions, or patch logic from unrelated sections, older versions, frameworks, or emergency fixes. |
| **Local-fix explosion** | One local correction creates several additional fixes because the underlying structure or scope boundary is unstable. |
| **Breakpoint integrity** | Viewport rules remain readable, bounded, and consistent with source intent instead of becoming emergency overrides. |
| **Include-chain integrity** | Partial/include order, ownership, and dependencies stay explicit enough to avoid accidental cross-section contamination. |
| **Rebuild predictability** | Operators can rebuild without hand-editing generated output, relying on hidden files, or applying undocumented post-build fixes. |
| **Implementation readability** | The source is understandable enough for a future operator to explain what owns structure, styling, behavior, and overrides. |
| **Scoped evolution** | Change is made at the smallest honest scope while preserving visible coupling and escalation when broader structure is required. |

---

## 4. Canonical Rules

- **Scoped fixes are preferred.** Fix the smallest honest owner: block, component, partial, token, breakpoint, or hook.
- **Deterministic rebuilds matter.** A frontend that needs undocumented manual intervention is not reliable.
- **Local overrides require governance.** Overrides are allowed only when source authority, HITL, or project pack rationale explains scope and intent.
- **Breakpoints must remain readable.** Responsive rules should not become a hidden second implementation.
- **Implementation should stay explainable.** A future operator should be able to identify ownership, dependencies, and change impact.
- **Coupling should stay visible.** Hidden dependencies between globals, includes, utilities, selectors, and JS hooks must be surfaced.
- **Regression risk must be surfaced.** Adjacent frozen sections, shared partials, globals, tokens, and breakpoint rules require impact notes when touched.
- **Emergency patches create entropy.** A hotfix may be necessary, but it should be named, scoped, and later normalized or accepted with risk.
- **Implementation readability matters.** Code that works but cannot be audited is not production-stable.
- **Scoped evolution beats patch layering.** When local fixes keep multiplying, escalate structure or source authority instead of stacking patches.

The issue is not local fixing itself. The issue is **uncontrolled implementation evolution**.

---

## 5. Reliability Dimensions

| Dimension | Reliability read |
|-----------|------------------|
| **CSS scope** | Selectors and utilities affect the intended block/component only; specificity remains explainable. |
| **Include graph** | Partials, imports, and includes have visible ownership; order dependency does not hide logic. |
| **Breakpoint model** | Responsive rules preserve intent without multiplying emergency exceptions. |
| **Override strategy** | Local overrides are justified, bounded, and reversible. |
| **Regression boundary** | Frozen or previously validated areas are protected by impact review. |
| **Rebuild behavior** | Source rebuilds deterministically; no generated artifact hand edits or manual post-build patches. |
| **Token integration** | Tokens and local values preserve semantic design intent without override chaos. |
| **JS hook ownership** | `data-*`, modules, and init logic have one owner and do not double-bind or race across slices. |
| **Readability** | The implementation can be explained without relying on memory of emergency fixes. |

---

## 6. Override and Patch Governance

Overrides are controlled when they:

- are source-anchored, HITL-approved, or explicitly marked as temporary risk;
- are scoped to the smallest honest owner;
- state why the normal token, component, selector, include, or breakpoint path is insufficient;
- do not leak into unrelated blocks, states, or viewports;
- are reported in **IMPLEMENTATION RELIABILITY FINDINGS** when material.

Overrides become drift when they:

- stack on top of earlier patches without resolving ownership;
- depend on specificity wars, random utility classes, or include order accidents;
- hide a structural mismatch behind CSS force;
- create breakpoint-only behavior that cannot be explained from source intent;
- spread from one local fix into a shared implementation rule without authority.

---

## 7. Anti-Patterns

Forbidden drift vocabulary:

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Patch-on-patch fixes** | Each fix depends on previous exceptions instead of resolving ownership. |
| **Random utility overrides** | Bypasses scoped source and makes future impact hard to predict. |
| **Selector escalation wars** | Specificity becomes a substitute for structure and scope. |
| **Emergency breakpoint hacks** | Mobile/tablet rules become a second, unreadable implementation. |
| **Duplicate implementations** | Same component or section logic exists twice with divergent behavior. |
| **Hidden dependencies** | A section works because of globals, include order, or neighbor CSS not visible in its owner file. |
| **CSS survivalism** | Styling is written to “fight” the current page rather than express maintainable intent. |
| **Accidental global impact** | A local fix silently changes unrelated sections or frozen blocks. |
| **Implementation panic fixes** | Urgent edits bypass source authority, scope, QA, and regression notes. |
| **“Works now” engineering** | Current visual pass is treated as sufficient even though rebuild, readability, or evolution risk is high. |

---

## 8. Forge / QA Expectations

When Forge is selected, implementation reliability is reviewed before freeze when CSS scope, include graph, breakpoints, overrides, regression risk, rebuild behavior, JS ownership, or maintainability are in scope:

- Run [`implementation-reliability-checklist.md`](../../agents/mars-forge/implementation-reliability-checklist.md) alongside source interpretation, visual reconciliation, compositional structure, responsive intent, and design token QA when stability over time affects the slice.
- Record **IMPLEMENTATION RELIABILITY FINDINGS** for implementation reliability QA, regression survivability QA, breakpoint integrity QA, include-chain QA, scoped-fix QA, and implementation readability QA.
- Use [frontend-stability-model.md](frontend-stability-model.md) to classify stable vs fragile implementation, scoped modification, coupling boundaries, and structural escalation drift.
- Use [implementation-drift-taxonomy.md](implementation-drift-taxonomy.md) to name drift patterns.
- Use [temporal-evolution-governance.md](temporal-evolution-governance.md) when local fixes, override accumulation, freeze changes, version lineage, or patch-history entropy affect long-term project continuity; report `TEMPORAL EVOLUTION FINDINGS` separately.
- Use [operational-workflow-governance.md](operational-workflow-governance.md) when scoped fixes, regression review, rebuild claims, or freeze decisions depend on execution order, checkpoint integrity, handoff clarity, or workflow traceability; report `WORKFLOW DISCIPLINE FINDINGS` separately.
- Use [production-readiness-governance.md](production-readiness-governance.md) when implementation readability, rebuild predictability, maintenance ownership, future-edit safety, or freeze state affects delivery survivability; report `PRODUCTION READINESS FINDINGS` separately.
- Use [failure-recovery-governance.md](failure-recovery-governance.md) when recovery or emergency repair affects trusted-state recovery, rollback integrity, degraded-state handling, panic-fix contamination, or resilience traceability; report `FAILURE RECOVERY FINDINGS` separately.
- Use [cross-project-transfer-governance.md](cross-project-transfer-governance.md) when implementation patterns, CSS structure, breakpoints, JS hooks, templates, or prior-project fixes are reused; report `CROSS-PROJECT TRANSFER FINDINGS` separately.
- Use [governance-prioritization.md](governance-prioritization.md) when implementation reliability findings need severity weighting across critical, operational, continuity, strategic, minor, escalation-only, or informational risk layers; report `RISK WEIGHTING FINDINGS` separately.
- Treat findings as human-supervised governance, not automated scoring.
- Escalate **SAFE UNKNOWN** when implementation ownership, include dependencies, override rationale, rebuild behavior, breakpoint authority, or regression impact cannot be established.
- Use [decision-boundary-model.md](decision-boundary-model.md) when unclear implementation ownership, structural escalation, unsafe overrides, or regression impact crosses from scoped fixing into human decision authority.
- Use [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md) when multiple sessions or roles affect the same implementation scope and ownership, reviewer independence, or validator integrity is unclear.

---

## 9. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory implementation reliability lessons:

- A section can look close to the approved source while still depending on fragile CSS, hidden coupling, or accidental global inheritance.
- Local fixes for hierarchy, rhythm, or responsive behavior can multiply when DOM grouping, include ownership, or breakpoint scope is unclear.
- Breakpoint survivability is weaker when mobile rules are implemented as emergency exceptions instead of readable responsive structure.
- Correct tokens and visual intent do not guarantee stability if overrides, selector specificity, or include order are not governed.
- Frozen sections need regression survivability when adjacent slices, globals, shared partials, or utility classes change.
- Missing implementation ownership should be reported as **SAFE UNKNOWN**, not solved by patch layering.

These are Website Factory lessons, not Triumph-only implementation prescriptions.

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Include ownership is unclear | Cannot prove which partial owns structure, style, or import order. |
| Override rationale is missing | Cannot tell if the exception is approved deviation, emergency patch, or drift. |
| Breakpoint authority is absent | Cannot prove whether viewport-specific rules are intended or survival hacks. |
| Shared selector impact is unclear | Cannot prove whether a local edit will affect frozen or unrelated sections. |
| Rebuild path is not documented | Cannot claim deterministic rebuild behavior. |
| Duplicate implementation exists | Cannot identify which implementation is canonical without HITL or source authority. |
| JS hook ownership is ambiguous | Cannot prove one owner, idempotent init, or safe lifecycle behavior. |

**Action:** document the resolver: implementation-pack rule, source owner, include map, scoped override note, HITL decision, regression note, or project-specific build/readme update.

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Implementation Reliability Governance layer — frontend stability over time, deterministic rebuilds, scoped evolution, implementation drift taxonomy, and Forge `IMPLEMENTATION RELIABILITY FINDINGS`; documentation only. |
| v0.1 | 2026-05-17 | Linked Human Escalation & Decision Boundary Governance for implementation stop conditions, structural authority, and HITL-required reliability boundaries. |
| v0.2 | 2026-05-17 | Linked Multi-Agent Coordination & Responsibility Governance for multi-session implementation ownership, reviewer independence, validator integrity, and handoff survivability. |
| v0.3 | 2026-05-17 | Linked Temporal Evolution & Project Drift Governance for freeze-state integrity, patch-history entropy, cumulative override pressure, and long-term continuity review. |
| v0.4 | 2026-05-17 | Linked Operational Workflow & Execution Discipline Governance for checkpoint integrity, execution sequencing, freeze-validation QA, handoff stability, and workflow traceability. |
| v0.5 | 2026-05-17 | Linked Cross-Project Knowledge Transfer Governance for implementation-pattern portability, operational mismatch reuse, and template overreach review. |
| v0.6 | 2026-05-17 | Linked Failure Recovery & Operational Resilience Governance for trusted-state recovery, rollback integrity, degraded-state handling, panic-fix contamination, and resilience traceability. |
| v0.7 | 2026-05-17 | Linked Governance Prioritization & Risk Weighting for proportional severity, critical implementation risk visibility, and operational-focus preservation. |
| v0.8 | 2026-05-17 | Linked Production Readiness & Delivery Survivability Governance for maintainability continuity, future-edit safety, frozen-build survivability, and post-delivery operational stability. |
