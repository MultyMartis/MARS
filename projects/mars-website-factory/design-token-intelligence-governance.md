# MARS Website Factory — Design Token Intelligence Governance

**Status:** **documented** — Website Factory semantic token governance and human-supervised design-system methodology only.  
**Not:** runtime token engine, universal token architecture, autonomous design-system AI, style linter, theme generator, or deployed enforcement system.

**Core principle:** design tokens are **semantic design intent infrastructure**.  
They are not merely variables, JSON values, spacing maps, color references, or a way to centralize repeated values.

**Companion documents:** [token-semantic-layer-model.md](token-semantic-layer-model.md), [token-drift-taxonomy.md](token-drift-taxonomy.md).  
**Related layers:** [design-system-intent-governance.md](design-system-intent-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [canonical-vertical-cadence-system.md](canonical-vertical-cadence-system.md), [responsive-intent-governance.md](responsive-intent-governance.md), [interaction-intent-governance.md](interaction-intent-governance.md), [state-behavioral-consistency-governance.md](state-behavioral-consistency-governance.md), [implementation-reliability-governance.md](implementation-reliability-governance.md).  
**Forge checklist:** [`../../agents/mars-forge/design-token-checklist.md`](../../agents/mars-forge/design-token-checklist.md).

---

## 1. Positioning

Design Token Intelligence Governance formalizes how Website Factory reads, names, applies, overrides, and escalates tokens so they preserve intent instead of only making values look systematic.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Semantic token meaning, hierarchy, continuity, and controlled deviation | Universal token methodology or mandatory token architecture |
| Human-supervised token QA for frontend production | Runtime theming, token engines, or automatic token linting |
| Drift vocabulary for token mismatch, alias confusion, override chaos, and fake consistency | Redesigning Triumph or any other project by token taste alone |
| Design-system trust as frontend infrastructure philosophy | Autonomous design-system generation or enforcement |

The governance question is not “is this value tokenized?”  
The governance question is: **does this token choice preserve semantic meaning, hierarchy stability, visual continuity, behavioral consistency, responsive integrity, and design-system trust?**

---

## 2. Canonical Definition

**Design token intelligence** is the discipline of treating token systems as semantic infrastructure:

- **Semantic meaning** — token names and aliases express role, not only value.
- **Hierarchy stability** — primary, secondary, supporting, muted, danger, success, elevated, compact, dense, and spacious roles stay readable.
- **Visual continuity** — colors, spacing, radius, shadows, typography, and surfaces remain coherent across sections.
- **Behavioral consistency** — hover, focus, active, disabled, loading, validation, success, and error states use comparable token logic.
- **Responsive integrity** — breakpoint-specific values preserve the same intent at narrower widths.
- **Design-system trust** — operators can understand why a token exists, when to use it, and when an override is justified.

Tokens should not be justified merely by:

- “the value repeats”;
- “it reduces duplication”;
- “it looks systematic”;
- “the design system should have everything”;
- “the component library already names it this way.”

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Semantic token** | A token named by role or intent, not by raw value alone. |
| **Intent-preserving token** | A token that keeps the intended visual, behavioral, responsive, or semantic role stable across usage. |
| **Token hierarchy** | Relationship between primitive, semantic, contextual, behavioral, responsive, state, and intent tokens. |
| **Semantic aliasing** | Mapping one token layer to another while preserving meaning and avoiding role confusion. |
| **Token continuity** | Stable token meaning across sections, breakpoints, components, and states. |
| **Token escalation** | A local value or contextual token is promoted to broader scope without sufficient reuse, authority, or semantic clarity. |
| **Token contamination** | Tokens inherit visual language from frameworks, previous sections, dashboards, archived versions, or unrelated projects. |
| **Override fragmentation** | Repeated local overrides erode token trust and make the system unreadable. |
| **Responsive token integrity** | Viewport-specific token adaptations preserve hierarchy, cadence, and composition intent. |
| **Visual-token drift** | Token names imply one visual role while implementation produces another. |
| **Behavioral-token mismatch** | State or interaction tokens imply behavior that does not match the component role. |
| **Semantic token pressure** | A token is overloaded to serve too many roles because creating, renaming, or scoping another token feels inconvenient. |
| **Design-system trust erosion** | Operators stop trusting token names because values, aliases, overrides, and scope no longer explain intent. |
| **Token readability** | The hierarchy and naming are understandable enough for humans to audit and maintain. |

---

## 4. Canonical Rules

- **Semantic naming matters.** Token names should describe role, state, context, or intent. Raw-value naming is acceptable at primitive layer, but not as a substitute for semantic roles.
- **Token hierarchy must stay readable.** A system that requires long alias chains to understand one color, gap, radius, or state is already at drift risk.
- **Not every repeated value deserves a token.** Repetition is evidence, not authority. Tokenize when the repeated value carries reusable intent.
- **Not every token deserves global scope.** Local context, section role, project pack, component family, or breakpoint may justify narrower scope.
- **Not every override is bad.** Controlled deviation is valid when source authority, section role, accessibility, responsive fidelity, or behavioral consistency requires it.
- **Overrides must justify existence.** An override should explain why a token cannot represent the local intent without damaging global meaning.
- **Responsive tokens require continuity.** Breakpoint changes should preserve hierarchy, cadence, composition, CTA pressure, and readability.
- **Behavioral states require consistency.** State tokens should not make comparable controls behave or read differently without role authority.
- **Token escalation should stay restrained.** Promote local tokens only when reuse, role clarity, and maintenance value are proven.
- **Token systems must preserve intent.** Centralized values that hide visual inconsistency are not a design system.
- **Local context may justify controlled deviation.** The decision must be explicit enough to audit later.

The issue is not token creation itself. The issue is **uncontrolled token evolution**.

---

## 5. Token Families Under Governance

| Token family | Governance read |
|--------------|-----------------|
| **Color tokens** | Semantic color must match role: primary, accent, surface, text, muted, border, danger, success, warning, focus. |
| **Spacing tokens** | Spacing must preserve cadence, density, grouping, and responsive breathing; not random margin replacement. |
| **Radius tokens** | Radius families must reflect surface role, CTA tone, inputs, media, and project visual language. |
| **Shadow / elevation tokens** | Depth must express hierarchy or containment; no fake premium glow or SaaS contamination. |
| **Typography tokens** | Type scale, weight, line-height, and rhythm must preserve readable hierarchy and commercial tone. |
| **State tokens** | Hover, focus, active, disabled, loading, validation, success, and error tokens must preserve behavioral clarity. |
| **Responsive tokens** | Breakpoint tokens must preserve intent instead of only compressing values. |
| **Intent tokens** | High-level roles such as `hero`, `proof`, `cta`, `footer`, `dense`, `trust`, or `operational` are valid only when they remain readable and restrained. |

---

## 6. Override Governance

Overrides are controlled when they:

- are source-anchored or HITL-approved;
- preserve semantic meaning better than the existing token;
- are scoped to the smallest honest context;
- do not silently alter comparable components;
- are recorded in `DESIGN TOKEN FINDINGS` when material.

Overrides become drift when they:

- patch local taste without authority;
- duplicate token intent under a new name;
- bypass responsive, state, or accessibility expectations;
- create a second visual language behind a semantic name;
- leak from one section, breakpoint, state, or project into another.

---

## 7. Anti-Patterns

Forbidden drift vocabulary:

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Token everything** | Creates noise and hides which values carry actual intent. |
| **Meaningless token aliases** | Gives semantic-looking names to values without role clarity. |
| **Random local overrides** | Makes the token system advisory instead of trusted. |
| **Giant token maps** | Centralizes values while making usage and hierarchy unreadable. |
| **Unreadable token naming** | Forces operators to guess intent from long or arbitrary names. |
| **Fake design-system rigor** | Uses tokens everywhere while visual meaning remains inconsistent. |
| **Token proliferation** | Adds new tokens instead of resolving scope, hierarchy, or alias confusion. |
| **Visual inconsistency behind semantic names** | Same token role produces conflicting visual outcomes across contexts. |
| **Override spaghetti** | Overrides layer on top of overrides until the source of truth is unknowable. |
| **Accidental token hierarchy collapse** | Primitive, semantic, contextual, and state tokens blur into one flat map. |

---

## 8. Forge / QA Expectations

When Forge is selected, design token intelligence is reviewed before freeze when tokens, variables, theme values, local overrides, state styles, responsive values, spacing/radius/shadow families, or design-system consistency are in scope:

- Run [`design-token-checklist.md`](../../agents/mars-forge/design-token-checklist.md) alongside design intent, cadence, responsive intent, interaction intent, state consistency, and visual reconciliation when token choices affect those reads.
- Record **DESIGN TOKEN FINDINGS** for semantic token QA, token continuity QA, override governance QA, responsive token QA, token drift QA, and design-system integrity QA.
- Use [token-semantic-layer-model.md](token-semantic-layer-model.md) to classify layer, alias, inheritance, override, and escalation questions.
- Use [token-drift-taxonomy.md](token-drift-taxonomy.md) to name drift patterns.
- Run implementation reliability QA when token choices, local values, or overrides affect scoped evolution, rebuild predictability, breakpoint integrity, or regression survivability; record `IMPLEMENTATION RELIABILITY FINDINGS` per [`implementation-reliability-checklist.md`](../../agents/mars-forge/implementation-reliability-checklist.md).
- Treat findings as human-supervised governance, not automated scoring.
- Escalate **SAFE UNKNOWN** when token authority, layer ownership, alias intent, responsive mapping, state mapping, or override rationale cannot be established.

---

## 9. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory token lessons:

- Operational visual seriousness can be weakened by radius, shadow, color, or spacing tokens imported from unrelated SaaS defaults.
- A design system can look consistent while hiding semantic mismatch between section role and token role.
- Dense equipment, proof, price, and CTA sections need token continuity across cadence, responsive collapse, and state behavior.
- Local deviations may be valid when a source screen needs a contrast reset, CTA isolation, or screen-local surface role.
- Tokenizing every repeated value would have made the project harder to audit; the useful question is whether the value carries reusable intent.
- Missing token authority should be reported as **SAFE UNKNOWN**, not solved by inventing global tokens.

These are Website Factory lessons, not Triumph-only token prescriptions.

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| No project token source exists | Cannot prove whether values are intentional tokens, local decisions, or legacy leftovers. |
| Token aliases conflict | Cannot determine which semantic role owns the value. |
| Existing code overrides design tokens | Cannot prove whether override is approved deviation or drift. |
| Responsive token behavior is missing | Cannot infer breakpoint values beyond survivability. |
| State token behavior is absent | Cannot invent hover/focus/disabled/loading/validation token semantics. |
| Design system naming is unreadable | Cannot audit intent from token names alone. |
| Active source contradicts token defaults | Need authority decision before preserving global defaults or screen-local deviation. |

**Action:** document the resolver: implementation-pack token note, design system rule, source export, HITL decision, or project-specific token map.

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Design Token Intelligence Governance layer — semantic token intent, hierarchy, drift, override governance, Forge `DESIGN TOKEN FINDINGS`; documentation only. |
| v0.1 | 2026-05-17 | Linked Implementation Reliability Governance for override stability, scoped evolution, rebuild predictability, and `IMPLEMENTATION RELIABILITY FINDINGS`. |
