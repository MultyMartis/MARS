# MARS Forge — Interaction Intent Checklist

**Status:** Forge overlay checklist for **human-supervised** interaction intent QA.  
**Not:** automated UX scoring, motion engine, runtime interaction validator, autonomous redesign, or universal animation style.

**Factory methodology:** [`../../projects/mars-website-factory/interaction-intent-governance.md`](../../projects/mars-website-factory/interaction-intent-governance.md).  
**Behavior taxonomy:** [`../../projects/mars-website-factory/interaction-behavior-taxonomy.md`](../../projects/mars-website-factory/interaction-behavior-taxonomy.md).  
**Motion model:** [`../../projects/mars-website-factory/motion-restraint-model.md`](../../projects/mars-website-factory/motion-restraint-model.md).

---

## 1. When to Run

Run this checklist:

- when hover, focus, active, click, tap, scroll, transition, animation, disclosure, form, navigation, CTA, card, media, or JS hook behavior is in scope;
- after source interpretation QA identifies what behavior is observed, inferred, assumed, or unknown;
- alongside visual reconciliation, design intent, responsive intent, content density, cadence, and rhythm QA when behavior affects their read;
- before section freeze or before declaring interaction behavior acceptable.

This checklist does not authorize inventing new UX features, animations, carousels, disclosures, sticky CTAs, or gesture systems without source authority or HITL.

---

## 2. Authority and Scope

- [ ] Active design version, source screen, and implementation pack are identified.
- [ ] Interaction states are classified as observed / inferred / assumed / unknown.
- [ ] Missing hover, focus, active, mobile tap, disclosure, or motion states are recorded as **SAFE UNKNOWN** when material.
- [ ] Existing code behavior is checked against active source before being preserved.
- [ ] No archived mockup, SaaS template, component-library default, or previous project behavior overrides active source.
- [ ] Any behavior not source-authorized is restrained, removed, deferred, or escalated.

---

## 3. Interaction Semantics QA

- [ ] Each reactive element has a clear semantic role: CTA, link, form control, disclosure, card link, media control, navigation, or approved decorative behavior.
- [ ] Static content does not look clickable, draggable, expandable, or tappable.
- [ ] Clickable cards have real action and matching affordance.
- [ ] Proof/trust items stay stable unless source charters interaction.
- [ ] Media objects do not imply gallery, zoom, video, or carousel behavior unless implemented and authorized.
- [ ] Decorative elements do not receive interaction by default.
- [ ] Misleading affordance and dead-click zones are flagged.

---

## 4. Behavioral Hierarchy QA

- [ ] Primary CTA has the clearest appropriate feedback.
- [ ] Secondary CTA behavior remains subordinate.
- [ ] Navigation and forms have predictable operational states.
- [ ] Supportive cards, icons, proof, and stats do not compete behaviorally with CTAs.
- [ ] Not every element reacts; stable elements are accepted where calm behavior supports trust.
- [ ] Similar elements behave consistently unless source documents an exception.
- [ ] Behavioral hierarchy survives responsive collapse.

---

## 5. Hover Behavior QA

- [ ] Hover states reinforce action or hierarchy, not decoration.
- [ ] Non-clickable elements do not hover as if clickable.
- [ ] Hover behavior does not change semantic meaning.
- [ ] Hover state does not make secondary content stronger than primary content.
- [ ] Hover-only usability is absent or escalated.
- [ ] Keyboard/focus implications are not hidden behind hover-only behavior.
- [ ] Mobile equivalent is known, restrained, or recorded as **SAFE UNKNOWN**.

---

## 6. CTA Interaction QA

- [ ] Primary CTA behavior is consistent across comparable sections.
- [ ] Secondary and tertiary CTA behavior stays calmer than primary CTA behavior.
- [ ] CTA hover/focus/active states clarify interaction without pressure.
- [ ] CTA does not pulse, bounce, glow, shake, or loop without explicit authority.
- [ ] CTA animation is not used to compensate for weak placement, density, or hierarchy.
- [ ] Mobile CTA behavior is restrained and not coercive.
- [ ] Repeated CTAs do not escalate motion section by section.

---

## 7. Motion Restraint QA

- [ ] Motion supports feedback, orientation, reveal, continuity, hierarchy, or approved brand expression.
- [ ] Decorative motion is justified by source, brand motion note, implementation pack, or HITL.
- [ ] Motion does not overpower cadence, scanning rhythm, or visual seriousness.
- [ ] No fake premium motion, fake cinematic behavior, or luxury-like transition theater introduced.
- [ ] No endless pulse, float, shimmer, breathing glow, marquee, or rotating decoration without authority.
- [ ] Dense sections avoid item-by-item animation that slows scanning.
- [ ] Motion remains calm on mobile and does not create scroll-motion fatigue.

---

## 8. Interaction Density and Overload QA

- [ ] Current viewport has more stable content than reactive decoration.
- [ ] Cards, icons, proof, CTA, media, and navigation do not all animate in one section.
- [ ] Scroll behavior does not compete with reading cadence.
- [ ] Interaction density does not create behavioral noise or fatigue.
- [ ] Motion escalation is checked across current section and neighbors.
- [ ] Interaction does not degrade operational seriousness or commercial trust.

---

## 9. Contamination QA

Check for:

- [ ] hover hallucination;
- [ ] animation spam;
- [ ] fake SaaS behavior;
- [ ] decorative hover drift;
- [ ] CTA animation screaming;
- [ ] motion overload;
- [ ] fake tactile illusion;
- [ ] dead-click zones;
- [ ] misleading affordance;
- [ ] interaction inconsistency;
- [ ] decorative cursor behavior;
- [ ] fake premium transitions;
- [ ] infinite motion contamination.

Record matches using [`interaction-behavior-taxonomy.md`](../../projects/mars-website-factory/interaction-behavior-taxonomy.md).

---

## 10. Mobile Interaction QA

- [ ] No hover-only critical behavior.
- [ ] Tap targets and tap feedback remain clear.
- [ ] Mobile interaction preserves hierarchy, CTA tone, grouping, and operational readability.
- [ ] Desktop hover effects are not blindly copied into mobile.
- [ ] Scroll-triggered behavior does not create delay, fatigue, or content obstruction.
- [ ] Sticky/fixed behavior does not pressure or block content unless source-authorized.
- [ ] Missing mobile interaction authority is recorded as **SAFE UNKNOWN**.

---

## 11. Escalation Boundary

Stop and escalate when an interaction fix would:

- invent a carousel, accordion, modal, sticky CTA, gesture, hover system, custom cursor, or animation family;
- change CTA meaning, order, pressure, or conversion tone;
- make static proof/content interactive without source authority;
- remove behavior that may be intentionally chartered but lacks documentation;
- add decorative motion to satisfy “premium,” “modern,” or “more interactive” language;
- require accessibility-sensitive behavior not covered by current scope;
- alter mobile interaction semantics without mobile source or HITL.

Use **PARTIAL — interaction intent** or **SAFE UNKNOWN** rather than silent UX invention.

---

## 12. REPORT Block

Use this block when interaction intent QA is in scope:

```text
INTERACTION INTENT FINDINGS — <section or block_id> — <source ref>

Interaction authority: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Active source:
- Interaction states observed:
- Interaction states inferred:
- Missing / unknown states:
- SAFE UNKNOWN resolver:

Interaction semantics: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- CTA / link / card / form roles:
- Dead zones / misleading affordance:
- Static elements intentionally stable:

Hover behavior: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Hover authority:
- Hover hierarchy:
- Hover-only usability risk:
- Mobile equivalent:

CTA behavior: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Primary CTA consistency:
- Secondary CTA restraint:
- Motion / pressure risk:
- Mobile CTA behavior:

Motion restraint: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Motion role:
- Decorative motion justification:
- Escalation / fatigue risk:
- Fake premium / cinematic risk:

Interaction taxonomy:
- Patterns:
- Severity:
- Contamination risk:

Disposition:
- Freeze impact:
- Action: no action | restrained | removed | deferred | HITL required | accessibility review required
- Evidence:
```

---

## 13. Not Claimed

- No automatic interaction detection.
- No runtime UX or motion engine.
- No universal hover, CTA, or animation style.
- No autonomous interaction redesign.
- No claim of full accessibility audit.

Defer to Website Factory interaction governance, source authority, project implementation packs, HITL decisions, foundation QA, and accessibility scope where applicable.

---

## 14. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge interaction intent checklist; adds `INTERACTION INTENT FINDINGS`. |
