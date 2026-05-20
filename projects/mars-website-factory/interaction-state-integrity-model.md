# MARS Website Factory — Interaction State Integrity Model

**Status:** **documented** — Website Factory model for human-supervised UI state integrity review.  
**Not:** runtime state machine, component library implementation, automatic accessibility validator, form framework, or universal state truth.

**Parent layer:** [state-behavioral-consistency-governance.md](state-behavioral-consistency-governance.md).  
**Taxonomy:** [ui-state-taxonomy.md](ui-state-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/state-consistency-checklist.md`](../../agents/mars-forge/state-consistency-checklist.md).

---

## 1. Purpose

This model defines what integrity means for common interaction states. It helps Website Factory and Forge distinguish:

- honest state feedback from decorative behavior;
- restrained operational clarity from visual under-signaling;
- accessibility-sensitive states from optional polish;
- calm predictability from state fatigue.

The model is qualitative. It does not prescribe exact colors, tokens, animation durations, or component APIs.

---

## 2. Core Principle

```text
STATE FEEDBACK MUST BE TRUE, VISIBLE, PROPORTIONATE, AND CONSISTENT.
```

State behavior should answer:

- What can the user do?
- What is currently selected, focused, active, unavailable, loading, invalid, successful, or failed?
- What changed after the user acted?
- What should the user do next?

If a state cannot answer one of these questions, it should not become louder. It should become clearer.

---

## 3. Hover State Integrity

Hover integrity means hover feedback clarifies action, priority, or affordance without creating false meaning.

Expected:

- hover appears only on actionable or source-authorized reactive elements;
- hover strength follows hierarchy;
- hover does not imply unavailable functionality;
- hover does not reveal required information without keyboard/mobile equivalent;
- same component role uses the same hover family unless source documents an exception.

Drift:

- hover on static proof, decorative cards, or non-clickable icons;
- hover hierarchy inversion;
- hover-only usability;
- hover carpet across all cards;
- hover copied from a library or previous section without role logic.

---

## 4. Focus State Integrity

Focus integrity means keyboard users can always see where they are and what will activate.

Expected:

- focus state remains visible and consistent;
- focus treatment has enough contrast and persistence to be useful;
- focus order follows meaningful interaction sequence;
- focus is not replaced by hover-only styling;
- focus styles do not randomly change between CTAs, links, form fields, and navigation.

Drift:

- outline removed for visual cleanliness;
- focus ring invisible on dark/light surfaces;
- keyboard path skips actionable elements;
- modal/disclosure focus behavior is unknown but claimed safe;
- focus styling differs by component accident.

**Rule:** focus visibility is an integrity requirement, not aesthetic decoration.

---

## 5. Active State Integrity

Active integrity means the interface confirms input without falsely claiming completion.

Expected:

- active/pressed state is brief and tied to actual user action;
- active feedback is distinct from disabled, selected, and success states;
- pressed state does not obscure label, icon, or target;
- mobile tap feedback remains clear and calm;
- repeated CTAs share active-state semantics.

Drift:

- active state looks like success before outcome is known;
- active state is so subtle that action registration is unclear;
- active state becomes a theatrical effect;
- desktop active behavior has no mobile equivalent;
- active state changes CTA hierarchy.

---

## 6. Disabled State Semantics

Disabled state semantics must communicate unavailability honestly.

Expected:

- disabled controls are visually distinct from enabled and secondary states;
- disabled reason is available when needed for task clarity;
- disabled control does not behave as enabled;
- disabled styling does not rely only on weak opacity when ambiguity remains;
- disabled state remains understandable on mobile and keyboard flows.

Drift:

- fake disabled opacity;
- disabled-looking controls still submit or navigate;
- valid actions look disabled because of visual restraint;
- disabled and loading states visually collapse;
- disabled CTA is used as pressure or mystery.

**Rule:** disabled must be unambiguous. If the reason is critical to action, silence is drift.

---

## 7. Validation State Semantics

Validation semantics should guide correction and confidence.

Expected:

- validation timing is predictable: live, blur, submit, or documented combination;
- field-level and form-level messages do not contradict each other;
- severity matches the issue;
- copy explains recovery, not just failure;
- validation does not create visual panic or shame;
- success/valid feedback is restrained and useful.

Drift:

- validation overload;
- glowing validation;
- every field screams at once;
- error messages appear far from fields;
- valid/success state competes with primary CTA;
- validation timing chaos.

**Rule:** validation should guide, not punish.

---

## 8. Success / Error Restraint

Success and error states are trust events. They should be clear enough to orient the user and restrained enough to avoid fatigue.

Success expected:

- confirms a real completed outcome;
- uses proportionate feedback;
- does not interrupt the next task unnecessarily;
- avoids repeated celebration for minor actions.

Error expected:

- states what failed;
- preserves recovery path;
- distinguishes recoverable field issues from system-level failures;
- avoids panic styling unless severity truly warrants it.

Drift:

- success celebration spam;
- confetti or large animation for minor actions;
- error panic styling;
- recoverable errors styled as catastrophes;
- errors without recovery guidance;
- success shown before a real outcome.

---

## 9. Loading-State Seriousness

Loading seriousness means waiting feedback represents a real process and helps the user understand state.

Expected:

- loading appears only for real waiting, submission, fetching, rendering, or processing;
- loading has clear scope: page, section, form, button, card, or media;
- loading does not hide critical context longer than needed;
- loading has completion, failure, timeout, or retry semantics where relevant;
- decorative skeletons, shimmer, and spinners are avoided unless state role is real.

Drift:

- infinite spinners everywhere;
- decorative loading systems;
- skeleton wallpaper;
- button spinner without actual submission;
- fake progress bar;
- loading that blocks recovery or creates ambiguity.

**Rule:** loading should not become theatrical.

---

## 10. Mobile State Continuity

Mobile state continuity means narrow and touch contexts preserve state meaning without relying on desktop hover.

Expected:

- tap feedback replaces or complements hover where needed;
- focus and keyboard behavior remain meaningful;
- mobile disabled, validation, loading, success, and error states remain legible;
- sticky/fixed state behavior does not obstruct content or pressure conversion;
- mobile CTA states preserve hierarchy and trust.

Drift:

- desktop hover leakage;
- tap state invisibility;
- mobile focus neglect;
- compressed validation messages;
- sticky state confusion;
- mobile CTA pressure escalation.

**Rule:** mobile interaction states matter because mobile is not desktop minus hover.

---

## 11. Behavioral Hierarchy Preservation

State strength should follow role:

1. **Critical actions and form recovery** require the clearest feedback.
2. **Navigation and current location** require predictable orientation.
3. **Primary CTA** requires clear but restrained hover/focus/active/loading/disabled behavior.
4. **Secondary CTA** remains behaviorally subordinate.
5. **Cards and media** receive state only when action or source authority exists.
6. **Proof, trust, and decorative objects** usually remain stable.

Behavioral hierarchy fails when every object gets similar hover, focus, glow, loading, success, or error treatment.

---

## 12. State Escalation Drift

State escalation happens when feedback becomes louder because previous state behavior made the interface noisy.

Symptoms:

- hover gets stronger to compete with animated cards;
- validation gets brighter because error placement is unclear;
- CTA loading becomes theatrical because submission confidence is weak;
- success animation grows because confirmation copy is insufficient;
- mobile states become sticky, pulsing, or oversized to survive density.

Response:

- reduce earlier state noise;
- restore role-based hierarchy;
- clarify copy, placement, and grouping;
- keep feedback proportional;
- record escalation in `STATE CONSISTENCY FINDINGS`.

---

## 13. Feedback Restraint

Feedback restraint means state behavior is strong enough to communicate and calm enough to preserve trust.

Acceptable restrained feedback:

- subtle hover/focus/active transitions that preserve contrast;
- clear focus ring or equivalent visible focus indicator;
- button-level loading for real submission;
- concise validation message near the field;
- calm success confirmation;
- recoverable error state with next step.

Forbidden by default:

- glowing validation;
- infinite shimmer/spinners as decoration;
- panic red floods for minor errors;
- confetti for ordinary form submission;
- disabled states that are only decorative opacity;
- motion-heavy state behavior without source authority.

---

## 14. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| State examples are absent | Cannot infer hover, focus, active, disabled, loading, validation, success, or error intensity. |
| State roles conflict | Cannot distinguish disabled, loading, secondary, selected, current, or inactive states. |
| Mobile state is unspecified | Cannot define tap/focus/validation/loading continuity from desktop source. |
| Form validation rules are missing | Cannot decide timing, severity, summary behavior, or success/error persistence. |
| Accessibility state impact is unclear | Cannot claim keyboard/focus/disabled/reduced-motion integrity without evidence. |
| Existing implementation differs from source | Need authority decision before preserving or removing state behavior. |

**Action:** resolve through annotated state source, implementation-pack state rule, prototype, component note, HITL, or accessibility review.

---

## 15. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Interaction State Integrity Model — hover, focus, active, disabled, validation, success/error, loading, mobile continuity, hierarchy, and escalation. |
