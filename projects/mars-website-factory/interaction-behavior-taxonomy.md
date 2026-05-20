# MARS Website Factory — Interaction Behavior Taxonomy

**Status:** **documented** — Website Factory drift vocabulary for human-supervised interaction QA.  
**Not:** automated interaction detector, UX lint engine, analytics model, runtime validator, or universal behavior ontology.

**Parent layer:** [interaction-intent-governance.md](interaction-intent-governance.md).  
**Motion model:** [motion-restraint-model.md](motion-restraint-model.md).  
**Forge checklist:** [`../../agents/mars-forge/interaction-intent-checklist.md`](../../agents/mars-forge/interaction-intent-checklist.md).

---

## 1. Purpose

This taxonomy names interaction drift patterns so Website Factory and Forge work can report behavior problems without inventing redesign language.

Use it when reviewing:

- hover behavior;
- CTA interaction;
- animation and transition behavior;
- perceived affordance;
- mobile tap behavior;
- card, media, form, disclosure, and navigation states;
- decorative or template-inherited behavior.

Taxonomy names are qualitative governance labels. They are not automated findings.

---

## 2. Drift Families

| Family | Core risk |
|--------|-----------|
| **Invented interaction** | Behavior absent from source, handoff, project pack, or HITL decision. |
| **Decorative interaction** | Behavior exists to look lively, not to clarify meaning. |
| **Contaminated interaction** | Behavior copied from SaaS dashboards, templates, component libraries, prior sections, or unrelated projects. |
| **Misleading affordance** | The interface promises action, clickability, drag, reveal, or state that is absent or different. |
| **Behavioral overload** | Too many reactive elements compete for attention and create fatigue. |
| **CTA behavior drift** | Conversion actions become inconsistent, noisy, pressured, or weak. |
| **Mobile interaction drift** | Desktop hover/motion assumptions damage mobile usability or intent. |

---

## 3. Canonical Drift Patterns

| Pattern | Definition | Typical symptom | Governance response |
|---------|------------|-----------------|---------------------|
| **Hover hallucination** | Inventing hover behavior not present in source or required by semantics. | Cards lift, icons animate, images zoom, or panels glow without authority. | Remove, restrain, or record **SAFE UNKNOWN** unless source/HITL charters it. |
| **Animation spam** | Motion applied broadly until behavior becomes visual noise. | Every section reveals, every card moves, every control transitions. | Reduce to meaningful feedback, orientation, or hierarchy support. |
| **Fake SaaS behavior** | App/dashboard microinteractions leak into commercial frontend. | Floating cards, badge hover states, app-like panels, dashboard control gestures. | Re-anchor to commercial page role and design intent governance. |
| **Decorative hover drift** | Hover effects spread to elements without interaction role. | Non-clickable proof cards, icons, stats, or decorative blocks react on hover. | Require hover authority or make the element stable. |
| **CTA animation screaming** | CTA motion tries to force attention. | Pulsing, bouncing, glowing, shaking, or looping button animation. | Restore calm CTA feedback and conversion tone. |
| **Motion overload** | Aggregate movement overwhelms cadence. | Scroll reveals, hover lifts, parallax, counters, sticky motion, and transitions all compete. | Apply motion restraint and preserve reading rhythm. |
| **Fake tactile illusion** | Effects simulate physicality without useful interaction. | Magnetic cursor, exaggerated press depth, rubbery cards, 3D tilt without source. | Reject unless explicitly chartered and semantically useful. |
| **Dead-click zones** | Areas look interactive but do nothing. | Cursor changes, card styling, hover response, or button-like visuals without action. | Bind intended action, change affordance, or report source ambiguity. |
| **Misleading affordance** | Behavior suggests a different function than reality. | Static image looks like gallery, card looks selectable, icon looks like button. | Align visual and behavior semantics. |
| **Interaction inconsistency** | Similar elements behave differently without reason. | Same CTA family has different hover, transition, active, or disabled behavior by section. | Normalize by role or document source-specific exception. |
| **Decorative cursor behavior** | Cursor effects are used as brand theater without utility. | Custom cursor trails, magnetic following, cursor blobs, hover distortion. | Reject by default for operational/commercial seriousness. |
| **Fake premium transitions** | Slow cinematic transitions imitate luxury instead of supporting use. | Long fades, blur reveals, staggered drama, hero-only theater copied everywhere. | Use restrained, hierarchy-preserving motion if any. |
| **Infinite motion contamination** | Looping movement continues after it has communicated nothing. | Endless pulse, shimmer, float, marquee, breathing glow, rotating icon. | Stop looping motion unless source/brand and usability justify it. |

---

## 4. Hover-Specific Drift

| Pattern | Why it matters |
|---------|----------------|
| **Hover-only usability** | Required information or control appears only on hover; unsafe for mobile and keyboard use. |
| **Hover hierarchy inversion** | A secondary card or CTA becomes stronger than the primary object on hover. |
| **Hover carpet** | Every visible object has hover response, flattening behavioral hierarchy. |
| **Hover as decoration** | Hover is used because a card exists, not because the card is actionable. |
| **Hover state contradiction** | Hover implies clickability while the element is static or disabled. |

Rule: hover should clarify affordance or priority. It should not create a second design system.

---

## 5. CTA Behavior Drift

| Pattern | Why it matters |
|---------|----------------|
| **CTA animation screaming** | Pressure behavior reduces trust and creates fatigue. |
| **Primary / secondary behavior collapse** | Secondary CTA receives equal or stronger motion than primary CTA. |
| **CTA behavior lottery** | Same CTA role behaves differently across sections with no source reason. |
| **CTA pulse dependency** | CTA visibility depends on animation instead of placement, hierarchy, or density control. |
| **Mobile CTA pressure** | Sticky, pulsing, oversized, or repeated mobile CTAs create coercive tone. |

Rule: CTA behavior must preserve conversion tone, not compensate for weak hierarchy.

---

## 6. Mobile Interaction Drift

| Pattern | Why it matters |
|---------|----------------|
| **Desktop hover leakage** | Desktop hover logic is copied into mobile without equivalent tap/focus logic. |
| **Tap ambiguity** | User cannot tell whether a card, icon, image, row, or label is tappable. |
| **Scroll-motion fatigue** | Reveals, parallax, sticky elements, and animated counters compete with reading. |
| **Dense-stack motion** | Long mobile stacks animate every item, creating delay and fatigue. |
| **Gesture invention** | Swipe, drag, carousel, or accordion behavior is invented without source authority. |

Rule: mobile behavior is governed by responsive intent and operational readability, not desktop novelty.

---

## 7. Behavioral Noise Indicators

The following symptoms usually indicate interaction overload:

- more elements react than remain stable;
- user movement triggers constant visual changes;
- CTA, cards, icons, and proof all animate in the same viewport;
- motion has no clear beginning/end or feedback role;
- repeated animations slow scanning;
- hover states make static information look clickable;
- mobile stack feels like a sequence of effects rather than content;
- serious commercial tone starts reading like template theater.

---

## 8. Severity Guidance

| Severity | Interaction drift condition |
|----------|-----------------------------|
| **Blocker** | Misleading affordance, dead-click critical CTA, hover-only required usability, invented interaction that changes meaning, or mobile interaction that blocks action. |
| **Major** | CTA inconsistency, motion overload, hover hallucination on key cards, fake SaaS behavior that changes tone, or repeated interaction fatigue. |
| **Minor** | Local decorative hover or transition that does not block meaning but should be restrained before freeze. |
| **Observation** | Interaction is calm and stable; no change required, but source authority or mobile state remains worth noting. |

Severity remains human-supervised and source-dependent.

---

## 9. Reporting Vocabulary

Use this compact vocabulary in `INTERACTION INTENT FINDINGS`:

```text
Interaction taxonomy:
- Pattern(s): <taxonomy names>
- Severity: blocker | major | minor | observation | SAFE UNKNOWN
- Source authority: observed | inferred | assumed | unknown
- Affected behavior: hover | click | focus | CTA | card | form | motion | mobile | scroll | other
- Disposition: pass | partial | fail | deferred | HITL required
```

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Static source has no state examples | Cannot infer hover, active, focus, or transition behavior. |
| Component looks interactive but role is unclear | Cannot distinguish card link, static card, gallery item, or decorative panel. |
| Existing code includes unexplained behavior | Cannot prove whether behavior is legacy, approved, or contamination. |
| Mobile behavior is absent | Cannot infer tap, sticky, disclosure, or gesture behavior from desktop hover. |
| CTA behavior conflicts across sources | Cannot choose conversion interaction without priority rule. |
| Brand asks for premium feel but motion rules are absent | Cannot invent cinematic behavior from vague premium language. |

**Action:** escalate to source note, implementation-pack rule, annotated state, or HITL decision.

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial interaction behavior drift taxonomy for hover, CTA, motion, affordance, mobile behavior, and contamination. |
