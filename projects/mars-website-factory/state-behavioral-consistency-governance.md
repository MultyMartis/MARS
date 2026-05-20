# MARS Website Factory — State & Behavioral Consistency Governance

**Status:** **documented** — Website Factory state-behavior governance and human-supervised frontend methodology only.  
**Not:** runtime UI engine, automated accessibility AI, universal UI-state truth, mandatory interaction aesthetics, or deployed behavior validator.

**Core principle:** frontend quality depends not only on visuals, responsiveness, interaction intent, motion restraint, source interpretation, and content density. It also depends on **consistent UI state behavior**.

**Companion documents:** [ui-state-taxonomy.md](ui-state-taxonomy.md), [interaction-state-integrity-model.md](interaction-state-integrity-model.md).  
**Related layers:** [interaction-intent-governance.md](interaction-intent-governance.md), [accessibility-intent-governance.md](accessibility-intent-governance.md), [responsive-intent-governance.md](responsive-intent-governance.md), [design-system-intent-governance.md](design-system-intent-governance.md), [design-token-intelligence-governance.md](design-token-intelligence-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md).  
**Forge checklist:** [`../../agents/mars-forge/state-consistency-checklist.md`](../../agents/mars-forge/state-consistency-checklist.md).

---

## 1. Positioning

State & Behavioral Consistency Governance formalizes the operational trust layer of frontend behavior: hover, focus, active, disabled, loading, validation, success, error, mobile/tap, keyboard, and CTA states.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| State integrity, state hierarchy, feedback restraint, and behavioral predictability | Universal component-state design systems |
| Consistent hover, focus, CTA, loading, validation, success, and error semantics | Runtime state machines, UI engines, or automated accessibility products |
| Human-supervised drift vocabulary for state mismatch and behavioral ambiguity | Mandatory hover aesthetics, animation style, or visual drama |
| Commercial frontend trust philosophy for Website Factory | Redesigning Triumph or any other project by state taste alone |

The governance question is not “does the interface look interactive?”  
The governance question is: **does each state preserve trust, clarity, predictability, interaction consistency, operational seriousness, and accessibility integrity?**

---

## 2. Canonical Definition

**Behavioral consistency** means comparable UI roles behave predictably across sections, components, and breakpoints.

**State integrity** means every visual state honestly communicates what the user can do, what has happened, what is currently happening, and what requires attention.

UI state behavior must preserve:

- **Trust** — states do not fake capability, urgency, progress, or completion.
- **Clarity** — users can distinguish clickable, focused, disabled, loading, valid, invalid, successful, and failed states.
- **Predictability** — similar objects behave in similar ways unless source authority documents an exception.
- **Interaction consistency** — CTAs, forms, links, cards, and navigation maintain stable state rules.
- **Operational seriousness** — feedback remains calm and useful, not theatrical.
- **Accessibility integrity** — focus, keyboard, disabled, validation, and reduced-motion uncertainty are surfaced honestly.

It must not be justified merely by:

- “has hover”;
- “looks disabled”;
- “feels modern”;
- “shows a spinner”;
- “has transitions”;
- “celebrates success.”

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Behavioral consistency** | Comparable UI roles maintain predictable behavior and feedback across the page or system. |
| **State integrity** | A state honestly reflects availability, focus, progress, validation, success, error, or action feedback. |
| **Hover hierarchy** | Hover strength follows element priority; primary actions and secondary content do not react as peers. |
| **Focus authority** | Focus state remains visible, meaningful, and keyboard-relevant without being visually random or hidden. |
| **Validation semantics** | Form feedback guides correction and confidence rather than punishing or overwhelming the user. |
| **Interaction trust** | The user can believe that affordances, progress, disabled states, and feedback are truthful. |
| **Behavioral predictability** | Similar elements behave similarly by role, not by local decoration. |
| **State contamination** | State treatment leaks from dashboards, templates, libraries, previous projects, or unrelated components. |
| **CTA state consistency** | Primary, secondary, and tertiary CTAs keep stable hover/focus/active/loading/disabled behavior. |
| **Interaction-state mismatch** | Visual state implies a different behavior than the component actually supports. |
| **Behavioral ambiguity** | The user cannot tell whether an element is enabled, disabled, focused, loading, invalid, complete, or actionable. |
| **State escalation** | States become louder over time to compete with other state effects. |
| **State fatigue** | Excessive feedback, validation, loading, hover, and success/error styling wears down attention and trust. |
| **Affordance integrity** | Visual affordance, state behavior, and actual capability remain aligned. |
| **Feedback restraint** | State feedback is sufficient and calm; it avoids drama when simple clarity is enough. |

---

## 4. Canonical Rules

- **Hover must preserve hierarchy.** Hover should clarify action and priority, not make every element compete.
- **Focus must remain visible.** Removing or hiding focus is drift unless another accessible, visible focus treatment exists in scope.
- **Disabled must be unambiguous.** Disabled controls must not look merely low-contrast, decorative, or broken.
- **Validation should guide, not punish.** Errors should identify what needs correction without panic styling or shame tone.
- **Success states should stay restrained.** Completion feedback should confirm outcome without celebration spam.
- **Error states should preserve trust.** Error styling should be clear, recoverable, and serious, not alarming theater.
- **Loading should not become theatrical.** Loading states require real progress or waiting semantics; decorative spinners are drift.
- **State behavior must stay consistent across breakpoints.** Mobile cannot silently lose focus, validation, CTA, loading, or disabled semantics.
- **Mobile interaction states matter.** Tap, active, keyboard, form, and touch feedback are not optional because desktop hover exists.
- **Not every state needs visual drama.** Operational systems may intentionally stay restrained, predictable, and calm.

---

## 5. State Families

| State family | Governance expectation |
|--------------|------------------------|
| **Hover** | Clarifies affordance and role; does not create false clickability or hierarchy inversion. |
| **Focus** | Visible, consistent, keyboard-meaningful, and not replaced by hover-only behavior. |
| **Active / pressed** | Briefly confirms action; does not imply success before success is known. |
| **Disabled** | Communicates unavailable action clearly and honestly; not just weak opacity. |
| **Loading** | Represents real waiting, submission, or async work; not decorative progress theater. |
| **Validation** | Guides correction; severity and timing match user task. |
| **Success** | Confirms completion with restraint; does not compete with next task. |
| **Error** | Explains failure and recovery; does not erode trust through panic styling. |
| **CTA states** | Primary and secondary CTAs maintain stable state hierarchy across sections. |
| **Mobile / tap** | Preserves equivalent behavioral meaning where hover does not exist. |

---

## 6. Interaction Trust

Interaction trust is damaged when the interface:

- looks enabled but cannot be used;
- looks disabled but remains clickable;
- shows loading without real work;
- reports success before a real outcome;
- makes error states louder than the task requires;
- hides focus from keyboard users;
- changes CTA behavior between identical roles;
- treats mobile as a reduced version of desktop hover rather than a real state context.

Trust is preserved by small, truthful feedback. Calm state behavior can be a quality signal.

---

## 7. Anti-Patterns

Forbidden drift:

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Glowing validation** | Turns correction into spectacle and may confuse severity. |
| **Infinite spinners everywhere** | Fakes progress and creates waiting ambiguity. |
| **Fake disabled opacity** | Low opacity alone may not communicate disabled semantics or accessibility. |
| **Hover chaos** | Every object reacts, flattening behavioral hierarchy. |
| **Success celebration overload** | Completion feedback becomes noise and pressure. |
| **Error panic styling** | Errors feel catastrophic instead of recoverable. |
| **Inconsistent focus rings** | Keyboard path becomes unpredictable or invisible. |
| **Inaccessible keyboard flow** | State behavior exists for mouse only. |
| **CTA behavioral mismatch** | Same CTA role changes hover/focus/loading/disabled behavior without reason. |
| **Dashboard-state contamination** | App-control state language leaks into commercial frontend without authority. |
| **Decorative loading systems** | Spinners, skeletons, shimmer, and progress bars appear without real state semantics. |

---

## 8. Forge / QA Expectations

When Forge is selected, state consistency is reviewed before freeze:

- Run [`state-consistency-checklist.md`](../../agents/mars-forge/state-consistency-checklist.md) when hover, focus, active, disabled, loading, validation, success, error, CTA state, keyboard behavior, or mobile state behavior is in scope.
- Record **STATE CONSISTENCY FINDINGS** for state authority, hover/focus integrity, CTA state consistency, loading seriousness, validation semantics, success/error restraint, mobile state continuity, and behavioral fragmentation.
- Run design token QA when state behavior depends on state tokens, focus tokens, disabled/loading/validation aliases, CTA state values, or state-specific overrides; record `DESIGN TOKEN FINDINGS` per [`design-token-checklist.md`](../../agents/mars-forge/design-token-checklist.md).
- Run accessibility intent QA when state behavior affects semantic integrity, focus survivability, keyboard continuity, assistive predictability, contrast trust, form recovery, or accessibility-state drift; record `ACCESSIBILITY FINDINGS` per [`accessibility-intent-checklist.md`](../../agents/mars-forge/accessibility-intent-checklist.md).
- Use [ui-state-taxonomy.md](ui-state-taxonomy.md) for named drift patterns.
- Use [interaction-state-integrity-model.md](interaction-state-integrity-model.md) for state-family expectations.
- Treat findings as human-supervised governance, not automated state scoring.
- Escalate **SAFE UNKNOWN** when source authority does not define states, disabled behavior, loading semantics, validation timing, mobile equivalents, keyboard focus, or success/error treatment.

---

## 9. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory state behavior lessons:

- Operational commercial pages can feel stronger when state feedback stays calm and predictable.
- CTA clarity requires consistent hover/focus/active semantics more than decorative animation.
- Dense service, price, proof, and form sections should avoid validation or loading drama that damages seriousness.
- Mobile state continuity matters because desktop hover cannot define tap, focus, or form feedback.
- Missing state source should not authorize fake disabled, fake loading, or invented validation behavior.
- Accessibility-state drift is a trust issue, not a late polish issue.

These are Website Factory lessons, not Triumph-specific state aesthetics.

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Static source provides no state examples | Cannot infer hover, focus, active, disabled, loading, validation, success, or error behavior. |
| Disabled semantics are unclear | Cannot tell whether a control is unavailable, secondary, pending, or decorative. |
| Loading state is absent from source | Cannot invent spinner, skeleton, shimmer, progress, or fake waiting behavior. |
| Validation timing is unspecified | Cannot decide on blur, submit, live, inline, summary, or combined feedback. |
| Success/error treatment is missing | Cannot infer intensity, placement, wording, or persistence. |
| Mobile state behavior is absent | Cannot copy desktop hover into tap/focus context. |
| Keyboard/focus impact is unclear | Cannot claim accessible state behavior without implementation evidence. |
| Existing code has unexplained states | Cannot prove whether behavior is approved, legacy, or contamination. |

**Action:** document what is unknown, what would resolve it, whether implementation should stop, continue with restrained disclosed defaults, or require HITL / accessibility review.

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial State & Behavioral Consistency Governance layer — state integrity, trust, predictability, accessibility-state drift, anti-patterns, and Forge reporting. |
| v0.1 | 2026-05-17 | Linked Accessibility Intent Governance for semantic integrity, focus survivability, keyboard continuity, assistive predictability, contrast trust, and `ACCESSIBILITY FINDINGS`. |
| v0.2 | 2026-05-17 | Linked Design Token Intelligence Governance for state-token continuity, behavioral-token mismatch, and `DESIGN TOKEN FINDINGS`. |
