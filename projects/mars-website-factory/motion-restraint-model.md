# MARS Website Factory — Motion Restraint Model

**Status:** **documented** — Website Factory motion philosophy for human-supervised commercial frontend work.  
**Not:** animation library, motion token system, runtime motion engine, automatic reduced-motion enforcement, or universal motion truth.

**Parent layer:** [interaction-intent-governance.md](interaction-intent-governance.md).  
**Taxonomy:** [interaction-behavior-taxonomy.md](interaction-behavior-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/interaction-intent-checklist.md`](../../agents/mars-forge/interaction-intent-checklist.md).

---

## 1. Purpose

Motion can improve orientation, feedback, continuity, and hierarchy. It can also create fake premium behavior, visual noise, interaction fatigue, and commercial distrust.

This model gives Website Factory a restrained motion vocabulary so frontend work can decide when motion is acceptable, when it should be reduced, and when it is drift.

---

## 2. Core Principle

```text
MOTION SUPPORTS MEANING. MOTION DOES NOT CREATE MEANING.
```

Motion must not compensate for:

- unclear hierarchy;
- weak CTA placement;
- missing proof;
- poor grouping;
- excessive content density;
- low visual seriousness;
- missing source authority.

Operational interfaces may intentionally stay restrained, calm, and stable.

---

## 3. Motion Categories

| Category | Governance read |
|----------|-----------------|
| **Acceptable motion** | Motion that supports feedback, orientation, reveal, continuity, or hierarchy without overpowering content. |
| **Restrained motion** | Short, calm, low-amplitude behavior that confirms interaction or state while preserving cadence. |
| **Operational motion** | Functional motion for menus, forms, disclosures, validation, focus, or state changes. |
| **Decorative motion** | Motion with no direct semantic or operational role; requires explicit source/brand authority. |
| **Hierarchy-preserving motion** | Motion that reinforces primary/secondary relationships instead of making every element compete. |
| **CTA motion discipline** | CTA feedback that clarifies action without pressure, screaming, or inconsistency. |
| **Mobile motion restraint** | Reduced behavior on narrow viewports to protect readability, tap clarity, and attention. |
| **Motion escalation drift** | Increasing intensity or quantity of motion to solve attention problems created by prior motion. |
| **Motion fatigue** | User attention erodes because motion repeats, loops, delays reading, or competes with scanning. |
| **Fake cinematic behavior** | Slow, dramatic, luxury-like transitions used to simulate value without project authority. |

---

## 4. Acceptable Motion

Acceptable motion has at least one semantic role:

- confirms a click, tap, focus, input, submit, open, close, or validation state;
- reveals content that is actually hidden by a governed disclosure;
- maintains orientation during menu, accordion, modal, or carousel transitions;
- reinforces primary vs secondary hierarchy without creating new priority;
- eases a layout change that would otherwise feel abrupt;
- supports approved brand expression without harming clarity.

Acceptable motion is:

- brief;
- predictable;
- scoped;
- reversible where relevant;
- consistent by component role;
- subordinate to content cadence.

---

## 5. Restrained Motion

Restrained motion is the Website Factory default.

Good restrained motion:

- uses subtle opacity, color, border, shadow, transform, or state transition only where it clarifies behavior;
- avoids exaggerated distance, bounce, elastic, tilt, blur, glow, or 3D effects;
- does not loop by default;
- does not delay access to content;
- does not make secondary elements compete with primary ones;
- can be removed without destroying meaning.

If motion is the only thing making an element understandable, the structure or visual hierarchy likely needs review.

---

## 6. Operational Motion

Operational motion supports task clarity.

Acceptable examples:

- menu open/close transition;
- accordion expand/collapse when the disclosure is source-authorized;
- form focus, validation, loading, success, or error state;
- modal open/close orientation;
- active navigation state;
- carousel movement when carousel behavior is explicitly chartered;
- restrained button feedback.

Operational motion must be deterministic and stateful. It should not feel like decoration.

---

## 7. Decorative Motion

Decorative motion is high-risk.

It may be acceptable only when:

- approved source or brand direction explicitly charters it;
- it does not obscure copy, proof, CTA, or task flow;
- it does not create false affordance;
- it does not loop endlessly without reason;
- mobile behavior remains calm and readable;
- it does not contaminate other sections.

Reject decorative motion when it exists only to:

- make the page “feel premium”;
- add energy to weak content;
- imitate SaaS templates;
- fill whitespace;
- compensate for poor hierarchy;
- create fake tactile or cinematic behavior.

---

## 8. Hierarchy-Preserving Motion

Motion must respect behavioral hierarchy.

| Element role | Motion posture |
|--------------|----------------|
| **Primary CTA** | Clear feedback; no pressure loops unless explicitly chartered. |
| **Secondary CTA** | Lighter feedback than primary CTA. |
| **Navigation** | Predictable orientation and active state. |
| **Clickable card** | Subtle affordance if the whole card is genuinely actionable. |
| **Static card / proof** | Usually no motion. Stability can be the correct behavior. |
| **Hero media** | Motion only if source/brand charters it and it does not steal CTA focus. |
| **Dense lists / specs / proof grids** | Avoid item-by-item animation that slows scanning. |

Motion fails hierarchy when every object moves with similar intensity.

---

## 9. CTA Motion Discipline

CTA motion should help the user recognize and confirm action.

Allowed by default:

- restrained hover/focus feedback;
- brief active/pressed state;
- loading state only when real submission or async action exists;
- success/error feedback for forms;
- consistent transition family across same CTA role.

Forbidden without explicit authority:

- endless pulsing;
- bouncing;
- shaking;
- glowing as pressure;
- fake loading drama;
- cinematic reveal delays before CTA access;
- different animation style per repeated CTA;
- secondary CTA motion louder than primary CTA.

CTA behavior must preserve trust. A serious commercial interface should guide, not beg.

---

## 10. Mobile Motion Restraint

Mobile amplifies motion cost.

Mobile motion should:

- reduce or remove decorative effects;
- avoid hover-derived behavior;
- keep tap feedback immediate and clear;
- avoid scroll reveal chains in dense content;
- avoid parallax, floating, and infinite motion unless explicitly chartered;
- preserve reading cadence and tap safety;
- respect unknown mobile states as **SAFE UNKNOWN**.

If a motion effect works only because desktop has space and hover, it is not automatically valid on mobile.

---

## 11. Motion Escalation Drift

Motion escalation happens when each new section or component needs more motion to compete.

Symptoms:

- primary CTA starts pulsing because cards already animate;
- hero gets cinematic reveal, then proof needs stagger, then specs need counters;
- hover lifts become stronger across the page;
- static sections feel “unfinished” only because neighbors move too much;
- mobile stack becomes a queue of delayed reveals.

Response:

- remove or reduce earlier decorative motion;
- restore hierarchy through layout, typography, spacing, and content grouping;
- keep motion role-specific;
- report escalation under `INTERACTION INTENT FINDINGS`.

---

## 12. Motion Fatigue

Motion fatigue appears when behavior makes reading harder.

Common causes:

- looping pulses or floating effects;
- repeated scroll reveals;
- staggered cards in long grids;
- animated counters without commercial need;
- hover effects on every card;
- cursor-following decoration;
- parallax during content-heavy sections;
- transitions that delay action.

Motion fatigue is especially dangerous in operational, industrial, B2B, service, pricing, proof, FAQ, and form sections where trust and clarity matter more than novelty.

---

## 13. Fake Cinematic Behavior

Fake cinematic behavior is motion theater without source authority.

Examples:

- slow hero reveal that delays comprehension;
- blur/fade sequences pretending to be premium;
- parallax depth unrelated to content;
- dramatic page-load entrances;
- luxury-like easing copied from portfolio sites;
- excessive staggered typography;
- modal-like focus effects on non-modal content.

Rule: cinematic motion requires explicit project authority. It is not inferred from “premium,” “modern,” or “high-end.”

---

## 14. Reduced-Motion Honesty

This documentation does not claim an automated reduced-motion system.

Governance expectation:

- do not add unnecessary motion;
- avoid motion that is required for understanding;
- prefer stable fallbacks for content and CTA access;
- document accessibility uncertainty as **SAFE UNKNOWN** when motion may affect focus, vestibular comfort, keyboard use, or reduced-motion expectations.

Implementation details belong to the target frontend project and foundation QA scope.

---

## 15. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Static source provides no motion state | Cannot infer animation from layout alone. |
| Brand asks for “premium” but gives no motion examples | Cannot decide cinematic behavior from vague tone. |
| CTA animation is absent from source | Cannot add pulse/glow/bounce as conversion improvement. |
| Existing animation has no source authority | Cannot tell whether it is approved, legacy, or contamination. |
| Mobile motion behavior is unspecified | Cannot copy desktop hover/reveal behavior into tap/scroll context. |
| Accessibility or reduced-motion impact is unclear | Cannot claim motion is safe without implementation evidence. |

**Action:** resolve via annotated state, implementation-pack rule, approved prototype, brand motion note, or HITL decision.

---

## 16. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Motion Restraint Model — acceptable, restrained, operational, decorative, hierarchy, CTA, mobile, escalation, fatigue, and fake cinematic behavior. |
