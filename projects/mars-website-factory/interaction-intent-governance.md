# MARS Website Factory — Interaction Intent Governance

**Status:** **documented** — Website Factory interaction governance and human-supervised frontend methodology only.  
**Not:** runtime UX engine, autonomous interaction AI, universal motion truth, mandatory animation style, or deployed behavior validator.

**Core principle:** frontend quality depends not only on layout, rhythm, responsiveness, visual intent, source interpretation, and content density. It also depends on **how the interface behaves**.

**Companion documents:** [interaction-behavior-taxonomy.md](interaction-behavior-taxonomy.md), [motion-restraint-model.md](motion-restraint-model.md).  
**Related layers:** [strategic-intent-governance.md](strategic-intent-governance.md), [state-behavioral-consistency-governance.md](state-behavioral-consistency-governance.md), [accessibility-intent-governance.md](accessibility-intent-governance.md), [design-system-intent-governance.md](design-system-intent-governance.md), [design-token-intelligence-governance.md](design-token-intelligence-governance.md), [responsive-intent-governance.md](responsive-intent-governance.md), [source-interpretation-governance.md](source-interpretation-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [content-density-governance.md](content-density-governance.md).  
**Forge checklist:** [`../../agents/mars-forge/interaction-intent-checklist.md`](../../agents/mars-forge/interaction-intent-checklist.md).

---

## 1. Positioning

Interaction Intent Governance formalizes the behavior layer between static visual implementation and user-facing frontend experience.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Interaction meaning, hierarchy, restraint, and consistency | Universal animation systems or product-wide motion truth |
| Hover, focus, active, click, scroll, CTA, and mobile behavior as human-supervised intent | Runtime behavior engines, telemetry, or autonomous UX scoring |
| Drift vocabulary for fake UX invention, interaction overload, and behavioral contamination | Redesigning a project or inventing missing interactive features |
| Website Factory commercial frontend methodology | Mandatory premium motion, SaaS microinteraction defaults, or decorative animation style |

The governance question is not “does the interface feel modern?”  
The governance question is: **does the behavior preserve operational clarity, semantic meaning, conversion tone, visual seriousness, responsive intent, and commercial trust?**

---

## 2. Canonical Definition

**Interaction intent** is the governed meaning of how interface elements react, remain stable, invite action, confirm state, or intentionally do nothing.

Interaction behavior must preserve:

- **Operational clarity** — the user understands what can be done and what is stable information.
- **Semantic meaning** — behavior reinforces the role of a CTA, link, disclosure, form, card, media object, or proof element.
- **Conversion tone** — action paths guide without pressure, noise, or fake urgency.
- **Visual seriousness** — behavior does not turn a serious commercial interface into toy-like motion or dashboard theater.
- **Responsive intent** — mobile and tablet interaction preserve hierarchy, tap safety, and calm operation.
- **Commercial trust** — interactions feel deliberate, not gimmicky, deceptive, or over-engineered.

It must not be justified merely by:

- “feel modern”;
- “look animated”;
- “feel premium”;
- “make it more interactive”;
- “add microinteractions everywhere.”

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Interaction intent** | The intended role, restraint, and meaning of interface behavior. |
| **Interaction semantics** | The relationship between behavior and element meaning: CTA, link, card, disclosure, media, form, proof, navigation, or decorative object. |
| **Behavioral hierarchy** | Which elements deserve stronger, weaker, or no reaction based on semantic priority and conversion role. |
| **Motion restraint** | The discipline of using motion only where it supports meaning, orientation, feedback, or hierarchy. |
| **Interaction density** | How many reactive behaviors exist in one section, viewport, or user path. |
| **Hover authority** | Whether an element is allowed to react on hover because its role and source authority justify it. |
| **Interaction overload** | Too many reactions, transitions, moving elements, hover effects, or state changes competing for attention. |
| **Fake premium motion** | Decorative cinematic or luxury-like motion used to simulate value without source, brand, or semantic authority. |
| **Interaction contamination** | Imported behavior from SaaS dashboards, templates, component libraries, previous projects, or unrelated sections. |
| **Behavioral noise** | Interaction effects that do not clarify action, state, hierarchy, or feedback. |
| **Decorative interaction drift** | Non-functional behavior spreading across elements because it “looks nice.” |
| **CTA behavior consistency** | Primary, secondary, and tertiary CTAs behave predictably across sections and viewport states. |
| **Operational interaction tone** | Calm, stable, clear behavior appropriate for commercial and task-oriented interfaces. |
| **Dead interaction zones** | Areas that look clickable, draggable, expandable, or hoverable but do nothing. |
| **Motion escalation** | Each new element gets stronger motion to compete with earlier motion. |
| **Interaction fatigue** | User attention is worn down by constant movement, hover changes, pulses, reveals, or behavioral novelty. |

---

## 4. Canonical Rules

- **Interaction must support meaning.** Behavior is acceptable when it clarifies affordance, confirms action, preserves orientation, reveals approved content, or reinforces hierarchy.
- **Not every element should react.** Static informational objects may intentionally stay calm and stable.
- **Hover should reinforce hierarchy.** Hover behavior should make actionable priority clearer, not make every card compete.
- **Motion must not overpower cadence.** The page's reading rhythm and section pacing remain stronger than decorative transitions.
- **CTA behavior must stay consistent.** Primary CTAs should not pulse in one section, slide in another, glow elsewhere, and stay static on mobile without reason.
- **Mobile interaction requires restraint.** Hover-only behavior, tiny tap zones, excessive reveals, and scroll-triggered noise are unsafe mobile defaults.
- **Decorative motion must be justified.** If motion does not support meaning, orientation, hierarchy, feedback, or approved brand expression, it is drift.
- **Interaction should preserve trust.** No misleading affordance, fake tactile effect, fake loading drama, endless pulsing, or pressure animation.
- **Behavioral escalation is dangerous.** Adding stronger motion to solve unclear hierarchy usually creates more noise.

---

## 5. Interaction Semantics

Different elements carry different behavior authority.

| Element role | Interaction expectation |
|--------------|-------------------------|
| **Primary CTA** | Clear affordance and consistent feedback; restraint beats screaming. |
| **Secondary CTA** | Subordinate behavior; must not visually or behaviorally overtake primary CTA. |
| **Text link** | Recognizable affordance; hover/focus may clarify without theatrical motion. |
| **Card** | Reacts only when the whole card is actionable or source charters card-level affordance. |
| **Proof / trust item** | Usually stable; motion must not make proof feel like decoration or ad inventory. |
| **Media / gallery** | Interaction must match actual functionality: zoom, carousel, video, or static image. |
| **Form control** | Feedback must support input clarity, validation, focus, and error recovery. |
| **Decorative object** | Default is no interaction unless approved brand motion explicitly charters it. |
| **Navigation** | Predictable state and orientation; avoid novelty that hides location or target. |

**Rule:** an element that looks interactive must either perform a clear action or be visually demoted so it does not promise behavior.

---

## 6. Behavioral Hierarchy

Interaction strength should follow page hierarchy:

1. **Critical actions** may receive the clearest feedback.
2. **Navigation and forms** receive predictable operational states.
3. **Clickable cards or disclosures** receive enough affordance to explain clickability.
4. **Supportive proof and content** stay stable unless the source gives them interaction role.
5. **Decorative surfaces** default to no interaction.

Behavioral hierarchy fails when every card lifts, every icon spins, every CTA pulses, every image zooms, and every cursor move triggers visual change.

---

## 7. Hover Authority

Hover is not a decoration budget. It is a behavior state with semantic cost.

Acceptable hover:

- reinforces that an element is actionable;
- clarifies primary vs secondary action;
- supports focus and keyboard parity where applicable;
- provides restrained feedback without changing meaning;
- follows the same behavior family as similar elements.

Forbidden hover drift:

- hover effects on non-clickable decorative objects;
- card lift on every visual group when only some groups are actionable;
- hover-only information required for usability;
- hover behavior that changes CTA hierarchy;
- hover behavior copied from SaaS templates without project authority;
- noisy cursor-following or fake tactile effects.

---

## 8. Motion Restraint

Motion is governed by [motion-restraint-model.md](motion-restraint-model.md).

Core posture:

- Motion may guide orientation, feedback, reveal, continuity, or hierarchy.
- Motion should be brief, calm, and subordinate to content unless the approved source says otherwise.
- Motion must not create fake premium feel, cinematic theater, or constant behavioral pressure.
- Motion should usually reduce on mobile and dense sections.
- Motion must never substitute for unclear structure, weak hierarchy, missing proof, or poor CTA semantics.

---

## 9. CTA Behavior Consistency

CTA behavior is a conversion-governance concern, not a local animation choice.

Expectations:

- Primary CTA behavior is stable across comparable sections.
- Secondary CTA behavior stays visibly and behaviorally subordinate.
- Repeated CTA blocks do not escalate animation to regain attention.
- CTA hover/focus states support clarity, not pressure.
- Mobile CTA behavior avoids endless sticky, pulsing, vibrating, or oversized pressure patterns unless explicitly chartered.
- CTA motion never compensates for buried CTA placement or poor density.

---

## 10. Mobile Interaction Restraint

Mobile interaction must be calmer than desktop by default because narrow viewports amplify motion, density, and fatigue.

Mobile rules:

- Do not rely on hover-only usability.
- Avoid scroll-triggered motion that fights reading cadence.
- Keep tap feedback clear and brief.
- Avoid decorative parallax, floating UI, and infinite motion in dense mobile stacks.
- Preserve tap safety and visible hierarchy.
- Reduce or remove decorative motion where it harms operational readability.

Missing mobile interaction states should be recorded as **SAFE UNKNOWN**, not solved by desktop hover assumptions.

---

## 11. Interaction Behavior Taxonomy

Drift vocabulary lives in [interaction-behavior-taxonomy.md](interaction-behavior-taxonomy.md).

High-risk families:

- hover hallucination;
- animation spam;
- fake SaaS behavior;
- CTA animation screaming;
- misleading affordance;
- dead-click zones;
- fake premium transitions;
- infinite motion contamination;
- decorative cursor behavior;
- interaction inconsistency.

Use taxonomy names in Forge `INTERACTION INTENT FINDINGS`.

---

## 12. Anti-Patterns

Forbidden drift:

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Animation everywhere** | Equalizes behavior and destroys hierarchy. |
| **Floating UI behavior** | Imports dashboard/app language into commercial narrative without authority. |
| **Fake luxury motion** | Simulates premium value through cinematic delay, glow, and reveal theater. |
| **Noisy hover systems** | Turns scanning into constant visual disturbance. |
| **Random transitions** | Makes behavior feel ungoverned and template-driven. |
| **Inconsistent CTA interaction** | Breaks conversion tone and user expectations. |
| **Endless pulsing buttons** | Creates pressure, fatigue, and trust erosion. |
| **Hover-only usability** | Fails mobile, keyboard, and accessibility expectations. |
| **Fake tactile effects** | Implies physical interaction without function or source authority. |
| **Dashboard microinteraction contamination** | Imports product UI behavior into landing pages or operational commercial sections. |
| **Motion without semantic role** | Adds behavioral noise without meaning. |

---

## 13. Forge / QA Expectations

When Forge is selected, interaction intent is reviewed before freeze:

- Run [`interaction-intent-checklist.md`](../../agents/mars-forge/interaction-intent-checklist.md) when hover, click, focus, CTA behavior, JS hooks, transition, animation, scroll behavior, mobile interaction, or perceived affordance is in scope.
- Record **INTERACTION INTENT FINDINGS** for interaction semantics, hover authority, CTA behavior consistency, motion restraint, behavioral hierarchy, dead zones, overload, and contamination.
- Run design token QA when hover, focus, active, transition, motion, CTA, or affordance behavior depends on behavioral tokens, semantic aliases, or local token overrides; record `DESIGN TOKEN FINDINGS` per [`design-token-checklist.md`](../../agents/mars-forge/design-token-checklist.md).
- Run state consistency QA when interaction behavior depends on hover/focus/active/disabled/loading/validation/success/error state integrity, CTA state consistency, keyboard state, or mobile state continuity; record `STATE CONSISTENCY FINDINGS` per [`state-consistency-checklist.md`](../../agents/mars-forge/state-consistency-checklist.md).
- Run accessibility intent QA when behavior affects keyboard continuity, focus survivability, hover dependency, custom controls, assistive predictability, interaction traps, or mobile accessibility continuity; record `ACCESSIBILITY FINDINGS` per [`accessibility-intent-checklist.md`](../../agents/mars-forge/accessibility-intent-checklist.md).
- Run strategic intent QA when behavior changes CTA strategic role, conversion pressure, business trust, operational seriousness, or stakeholder intent continuity; record `STRATEGIC INTENT FINDINGS` per [`strategic-intent-checklist.md`](../../agents/mars-forge/strategic-intent-checklist.md).
- Use [interaction-behavior-taxonomy.md](interaction-behavior-taxonomy.md) for named drift patterns.
- Use [motion-restraint-model.md](motion-restraint-model.md) for motion posture and escalation review.
- Treat findings as human-supervised governance, not automated behavior scoring.
- Escalate **SAFE UNKNOWN** when source authority does not define hover states, clickability, motion, mobile interaction, disclosure behavior, or CTA behavior.

---

## 14. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory interaction lessons:

- Operational landing pages can be visually strong while intentionally calm in behavior.
- A serious industrial/commercial tone can be weakened by SaaS hover lifts, fake premium motion, or decorative cursor effects.
- CTA clarity does not require animation; repeated CTA animation would create pressure and fatigue.
- Dense equipment, proof, pricing, and trust sections benefit from stable behavior rather than constant reactive cards.
- Missing hover or mobile interaction source should not authorize invented UX behavior.
- Dead-looking or fake-clickable zones are as harmful as over-animation because both damage trust.

These are Website Factory lessons, not Triumph-specific animation rules.

---

## 15. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Missing hover / active / focus source | Cannot prove intended interaction state. |
| Unclear clickability | Cannot tell whether card, image, icon, or row should be actionable. |
| Missing mobile interaction source | Desktop hover cannot define mobile tap behavior. |
| Motion not chartered | Cannot infer animation style from static visual source alone. |
| CTA behavior inconsistent across source artifacts | Need priority rule or HITL before implementation confidence. |
| Existing code has behavior absent from active source | Need authority decision before preserving or removing it. |
| Decorative element appears interactive | Need source or HITL to decide affordance vs demotion. |
| Accessibility impact unclear | Interaction may affect keyboard, focus, reduced motion, or usability expectations. |

**Action:** document what is unknown, what would resolve it, whether implementation should stop, continue with disclosed restraint, or require HITL.

---

## 16. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Interaction Intent Governance layer — behavior, hover, CTA, motion restraint, interaction density, anti-drift, Forge reporting. |
| v0.1 | 2026-05-17 | Linked State & Behavioral Consistency Governance for hover/focus/CTA/loading/validation state integrity and `STATE CONSISTENCY FINDINGS`. |
| v0.2 | 2026-05-17 | Linked Accessibility Intent Governance for keyboard continuity, focus survivability, hover dependency, assistive predictability, and `ACCESSIBILITY FINDINGS`. |
| v0.3 | 2026-05-17 | Linked Design Token Intelligence Governance for behavioral-token mismatch, CTA token continuity, and `DESIGN TOKEN FINDINGS`. |
