# MARS Website Factory — Accessibility Intent Governance

**Status:** **documented** — Website Factory accessibility governance and human-supervised frontend methodology only.  
**Not:** automated WCAG engine, runtime accessibility AI, universal accessibility truth, mandatory accessibility aesthetics, or deployed accessibility validator.

**Core principle:** Accessibility is not checkbox compliance, ARIA spam, decorative semantics, or fake inclusive theater. Accessibility is **trusted operational usability**.

**Companion documents:** [operational-accessibility-model.md](operational-accessibility-model.md), [accessibility-drift-taxonomy.md](accessibility-drift-taxonomy.md).  
**Related layers:** [interaction-intent-governance.md](interaction-intent-governance.md), [state-behavioral-consistency-governance.md](state-behavioral-consistency-governance.md), [responsive-intent-governance.md](responsive-intent-governance.md), [design-system-intent-governance.md](design-system-intent-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [qa-confidence-governance.md](qa-confidence-governance.md).  
**Forge checklist:** [`../../agents/mars-forge/accessibility-intent-checklist.md`](../../agents/mars-forge/accessibility-intent-checklist.md).

---

## 1. Positioning

Accessibility Intent Governance formalizes how Website Factory preserves usability, trust, predictability, semantic integrity, operational clarity, and interaction survivability.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Semantic-first, keyboard-aware, focus-visible operational usability | Universal accessibility law or certification |
| Human-supervised accessibility drift vocabulary | Automated WCAG scoring, Lighthouse replacement, or screen-reader simulation |
| Accessibility restraint, assistive predictability, and semantic integrity | ARIA-by-default wrappers, decorative compliance theater, or mandatory visual style |
| Forge reporting via `ACCESSIBILITY FINDINGS` | Runtime accessibility AI, autonomous remediation, or redesign of Triumph |

The governance question is not “did tooling pass?”  
The governance question is: **can real users predict, understand, navigate, act, recover, and trust the interface across input and assistive contexts?**

---

## 2. Canonical Definition

**Accessibility intent** is the governed meaning of accessibility behavior: how structure, focus, keyboard flow, labels, contrast, states, responsive behavior, and assistive output support real operational use.

Accessibility must preserve:

- **Usability** — tasks remain understandable and completable.
- **Trust** — labels, roles, states, focus, errors, and CTAs do not mislead.
- **Predictability** — similar controls behave similarly across sections and breakpoints.
- **Semantic integrity** — native HTML and roles match actual meaning.
- **Operational clarity** — accessibility supports task flow, not theater.
- **Interaction survivability** — keyboard, focus, mobile, forms, and state feedback remain usable under real constraints.

It must not be justified merely by:

- “ARIA added”;
- “Lighthouse says green”;
- “screen reader text exists”;
- “looks accessible”;
- “inclusive language added”;
- “compliance checkbox completed.”

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Operational accessibility** | Accessibility as reliable task usability, not symbolic compliance. |
| **Semantic accessibility** | Native structure, headings, landmarks, controls, and roles match actual content and behavior. |
| **Focus survivability** | Focus remains visible, meaningful, and recoverable across components, states, and breakpoints. |
| **Keyboard continuity** | Keyboard path reaches actionable elements in predictable order without dead-ends or traps. |
| **Affordance clarity** | Visual and assistive cues honestly communicate what can be used. |
| **Accessibility restraint** | Enhancements remain sufficient and meaningful; no ARIA or wrapper excess where native semantics work. |
| **Semantic integrity** | Accessible names, roles, states, and hierarchy remain truthful to actual UI behavior. |
| **Accessibility contamination** | Accessibility markup, labels, wrappers, or behaviors copied from unrelated templates without role logic. |
| **Interaction trap drift** | Keyboard, focus, modal, disclosure, sticky, or mobile behavior traps users or blocks recovery. |
| **Accessibility fatigue** | Excessive announcements, labels, focus jumps, verbose hints, or state noise wear down users. |
| **Fake accessibility** | Symbolic or decorative accessibility treatment that does not improve operational use. |
| **Assistive predictability** | Screen-reader and keyboard users can anticipate structure, control behavior, and state changes. |
| **Screen-reader clarity** | Assistive output is concise, ordered, non-duplicative, and semantically truthful. |
| **Contrast trust** | Contrast supports readability and state clarity without panic styling or false confidence. |
| **Accessibility overengineering** | Custom accessibility scaffolding replaces simpler native semantics and increases risk. |

---

## 4. Canonical Rules

- **Semantic HTML first.** Use native elements and structure before ARIA or custom wrappers.
- **ARIA must justify existence.** ARIA is acceptable when it corrects a real semantic gap; it is drift when decorative or redundant.
- **Focus must survive.** Visible focus is not polish; it is navigation state.
- **Keyboard flow matters.** Action paths must not depend on mouse, hover, pointer precision, or visual guessing.
- **Hover must not be mandatory.** Required information or actions cannot exist only on hover.
- **Accessibility should preserve trust.** Labels, roles, disabled states, errors, and CTAs must not promise unavailable or different behavior.
- **Forms must remain understandable.** Labels, instructions, validation, errors, recovery, and submission states require seriousness.
- **Accessibility should support meaning.** Enhancements must clarify role, state, orientation, or recovery.
- **Mobile accessibility matters.** Narrow/touch contexts must preserve tap clarity, focus, readable labels, and state feedback.
- **Accessibility must stay behaviorally consistent.** Focus, keyboard, validation, disabled, loading, success, and error behavior must align with state governance.
- **Accessibility may remain restrained.** Operational systems often need clarity, predictability, semantic correctness, and survivability more than accessibility theatrics.

---

## 5. Accessibility Restraint

Restrained accessibility is not neglect. It means the implementation avoids noisy, fragile, or fake accessibility additions when native semantics and clear UI already provide the better path.

Acceptable restraint:

- native button, link, input, label, heading, list, and section semantics used correctly;
- concise accessible names instead of verbose marketing labels;
- visible focus that fits the design system without disappearing;
- clear form errors without live-region spam;
- calm contrast corrections that preserve hierarchy and trust;
- simple keyboard flow instead of custom focus choreography.

Forbidden restraint:

- removing focus for aesthetics;
- omitting labels because placeholders are visible;
- relying on hover-only explanations;
- hiding interactive state from keyboard users;
- treating mobile as exempt from accessibility behavior;
- calling unknown assistive behavior “fine” without evidence.

---

## 6. Anti-Patterns

Forbidden drift:

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **ARIA everywhere** | Adds noise, duplicates native semantics, and can corrupt assistive output. |
| **Fake semantic wrappers** | Div/span structures pretend to be controls or landmarks without real behavior. |
| **Inaccessible custom controls** | Custom UI lacks keyboard, focus, role, state, or recovery semantics. |
| **Hover-only usability** | Fails keyboard, touch, and assistive contexts. |
| **Invisible focus** | Breaks keyboard orientation and trust. |
| **Semantic inflation** | Landmarks, headings, roles, or labels are exaggerated beyond actual structure. |
| **Decorative accessibility labels** | Labels describe branding theater instead of actionable meaning. |
| **Contrast panic styling** | Overcorrected contrast destroys hierarchy or creates false severity. |
| **Accessibility dashboard contamination** | Compliance widgets, badges, or template patterns pollute operational interface semantics. |
| **Keyboard traps** | Users enter a component, modal, menu, sticky layer, or form state and cannot recover predictably. |
| **Accessibility without semantics** | Tooling patches are added while actual HTML meaning remains wrong. |

---

## 7. Forge / QA Expectations

When Forge is selected, accessibility intent is reviewed before freeze:

- Run [`accessibility-intent-checklist.md`](../../agents/mars-forge/accessibility-intent-checklist.md) when semantics, focus, keyboard behavior, forms, CTAs, custom controls, responsive behavior, interaction states, contrast, or assistive output are in scope.
- Record **ACCESSIBILITY FINDINGS** for semantic accessibility, focus survivability, keyboard continuity, assistive predictability, contrast trust, form seriousness, mobile accessibility continuity, and drift taxonomy matches.
- Use [operational-accessibility-model.md](operational-accessibility-model.md) for operational expectations.
- Use [accessibility-drift-taxonomy.md](accessibility-drift-taxonomy.md) for named drift patterns.
- Treat findings as human-supervised governance, not automated accessibility certification.
- Escalate **SAFE UNKNOWN** when source, implementation evidence, assistive behavior, keyboard path, focus treatment, contrast, or mobile accessibility behavior cannot be verified.

---

## 8. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory accessibility lessons:

- Industrial/commercial seriousness benefits from clear native semantics, not decorative accessibility wrappers.
- Dense equipment, proof, price, review, and form sections need keyboard and screen-reader predictability because visual scanning alone is not enough.
- CTA clarity must include focus, label, state, and keyboard survivability, not only visual dominance.
- Mobile collapse can silently damage labels, tap clarity, focus order, and readable validation if accessibility is treated as desktop-only.
- Accessibility-state drift is a trust issue: hidden focus, fake disabled state, and unclear validation can damage operational confidence.
- Missing accessibility source or evidence should be reported as **SAFE UNKNOWN**, not filled with ARIA theater.

These are Website Factory lessons, not Triumph-specific accessibility aesthetics.

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Assistive output has not been verified | Cannot claim screen-reader clarity without evidence. |
| Focus treatment is absent or unclear | Cannot prove keyboard orientation survives. |
| Keyboard path is untested or custom controls exist | Cannot claim continuity or no traps. |
| Source provides no mobile accessibility behavior | Cannot infer tap/focus/label continuity from desktop source. |
| Contrast is visually uncertain | Cannot claim readable/state-safe contrast without inspection. |
| Form labels, validation, or recovery semantics are missing | Cannot infer serious form accessibility from visual layout. |
| Existing code contains unexplained ARIA | Cannot prove whether it is necessary enhancement or contamination. |
| Accessibility requirements exceed current scope | Need HITL, audit scope, project-specific legal/compliance requirements, or specialist review. |

**Action:** document what is unknown, what would resolve it, whether implementation should stop, continue with disclosed restraint, or require HITL / accessibility review.

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Accessibility Intent Governance layer — trusted operational usability, restraint, semantic integrity, anti-drift, and Forge `ACCESSIBILITY FINDINGS`. |
