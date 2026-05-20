# MARS Forge — Accessibility Intent Checklist

**Status:** Forge overlay checklist for **human-supervised** accessibility intent QA.  
**Not:** automated WCAG audit, accessibility scanner, screen-reader simulator, runtime accessibility AI, autonomous remediation, or universal accessibility truth.

**Factory methodology:** [`../../projects/mars-website-factory/accessibility-intent-governance.md`](../../projects/mars-website-factory/accessibility-intent-governance.md).  
**Operational model:** [`../../projects/mars-website-factory/operational-accessibility-model.md`](../../projects/mars-website-factory/operational-accessibility-model.md).  
**Drift taxonomy:** [`../../projects/mars-website-factory/accessibility-drift-taxonomy.md`](../../projects/mars-website-factory/accessibility-drift-taxonomy.md).

---

## 1. When to Run

Run this checklist:

- when semantics, headings, landmarks, CTAs, links, forms, labels, custom controls, ARIA, focus, keyboard behavior, contrast, mobile states, validation, loading, success/error, or assistive output are in scope;
- after source interpretation QA identifies what accessibility behavior is observed, inferred, assumed, or unknown;
- alongside interaction intent, state consistency, responsive intent, design intent, visual reconciliation, content density, cadence, and rhythm QA when accessibility affects their read;
- before section freeze or before declaring accessibility behavior acceptable.

This checklist does not authorize inventing accessibility products, custom control systems, compliance overlays, ARIA-heavy wrappers, or mandatory aesthetics without source authority, implementation evidence, or HITL.

---

## 2. Authority and Scope

- [ ] Active design version, source screen, implementation pack, and target section/block are identified.
- [ ] Accessibility-relevant behavior is classified as observed / inferred / assumed / unknown.
- [ ] Existing code semantics, ARIA, focus, keyboard behavior, and labels are checked before being preserved.
- [ ] Missing focus, keyboard, mobile, form, contrast, assistive-output, or custom-control evidence is recorded as **SAFE UNKNOWN** when material.
- [ ] No archived mockup, SaaS template, accessibility widget, dashboard pattern, or previous project behavior overrides active source and semantic correctness.
- [ ] Accessibility remains restrained unless enhancement solves a real usability or semantic gap.

---

## 3. Semantic Accessibility QA

- [ ] Native HTML is used where it matches actual meaning: button, link, input, label, list, heading, section, table, form.
- [ ] Links navigate and buttons act; roles do not contradict behavior.
- [ ] Heading order supports real document hierarchy, not visual size alone.
- [ ] Landmarks are useful and not inflated.
- [ ] Icon semantics are correct: decorative icons hidden from assistive output, functional icons named.
- [ ] Accessible names are concise and user-meaningful.
- [ ] No fake semantic wrappers, div controls, or role inflation are introduced.

---

## 4. ARIA Restraint QA

- [ ] ARIA is absent where native semantics already solve the role/name/state.
- [ ] Any ARIA used has a clear reason: state, relationship, description, current item, disclosure, or status.
- [ ] ARIA does not duplicate visible text into noisy repeated announcements.
- [ ] `aria-label`, hidden text, and descriptions do not become marketing copy.
- [ ] `aria-expanded`, `aria-current`, `aria-invalid`, `aria-describedby`, or live regions match real behavior when used.
- [ ] No decorative ARIA spam, semantic-role inflation, or accessibility wrapper drift appears.

---

## 5. Focus Survivability QA

- [ ] Focus remains visible on every actionable element in scope.
- [ ] Focus treatment survives light/dark surfaces, cards, CTAs, forms, nav, and mobile states.
- [ ] Focus style is consistent for comparable controls.
- [ ] Focus is distinct from hover, active, selected, disabled, success, and error states.
- [ ] Focus is not removed for visual cleanliness.
- [ ] Focus after interaction remains meaningful or **SAFE UNKNOWN** is recorded.

---

## 6. Keyboard Continuity QA

- [ ] Keyboard path reaches actionable elements in meaningful order.
- [ ] Keyboard activation matches expected role.
- [ ] No keyboard dead-end or trap exists in scoped modals, menus, disclosures, sticky layers, custom controls, or forms.
- [ ] Hover-only information has keyboard and mobile equivalent, or is removed/escalated.
- [ ] Custom controls have role, name, state, focus, and keyboard behavior evidence.
- [ ] Missing keyboard evidence is recorded as **SAFE UNKNOWN**, not assumed safe.

---

## 7. CTA Accessibility QA

- [ ] Primary CTA label clearly names the action or destination.
- [ ] Secondary CTA remains semantically and visually subordinate.
- [ ] CTA focus, hover, active, disabled, loading, and mobile states preserve trust.
- [ ] CTA does not rely on animation, hover, icon-only recognition, or visual-only affordance.
- [ ] Repeated CTA labels and state behavior remain consistent by role.
- [ ] Sticky or mobile CTA behavior does not obstruct content, trap focus, or create pressure without authority.

---

## 8. Form Accessibility QA

- [ ] Inputs have durable labels; placeholder-only labeling is absent or escalated.
- [ ] Required/optional state is understandable.
- [ ] Helper text and error messages are associated with the relevant fields when implementation is in scope.
- [ ] Validation timing is known or recorded as **SAFE UNKNOWN**.
- [ ] Errors explain recovery and do not rely only on color or panic styling.
- [ ] Submission, loading, success, and failure states are clear and truthful.
- [ ] Custom selects, checkboxes, uploads, date pickers, masks, or other controls have accessibility contract evidence.

---

## 9. State Accessibility QA

- [ ] Disabled states do not remain clickable or visually ambiguous.
- [ ] Loading states represent real waiting, submission, fetching, or processing.
- [ ] Selected/current/expanded/invalid/success/error states match actual behavior.
- [ ] State meaning does not rely only on color when meaning matters.
- [ ] State feedback remains consistent across comparable controls and breakpoints.
- [ ] Accessibility-state drift is recorded under both `ACCESSIBILITY FINDINGS` and, when relevant, `STATE CONSISTENCY FINDINGS`.

---

## 10. Mobile Accessibility QA

- [ ] Mobile/touch layout preserves labels, tap clarity, reading order, and CTA meaning.
- [ ] Desktop hover assumptions are not copied into mobile as accessibility behavior.
- [ ] Icon-only mobile controls have useful accessible names or are escalated.
- [ ] Sticky/fixed UI does not obstruct content, focus, form messages, or navigation.
- [ ] Collapsed sections preserve expanded/collapsed state where relevant.
- [ ] Mobile validation, focus, disabled, loading, success, and error states remain legible.
- [ ] Missing mobile accessibility authority is recorded as **SAFE UNKNOWN**.

---

## 11. Assistive Predictability QA

- [ ] Reading order matches user task order in the scoped section.
- [ ] Headings and landmarks allow useful skimming without inflation.
- [ ] Screen-reader output is not polluted by decorative icons, duplicate labels, hidden marketing, or live-region spam.
- [ ] Important state changes are not purely visual when assistive communication is required.
- [ ] Accessible labels and descriptions remain concise.
- [ ] No claim of screen-reader clarity is made without evidence or disclosed scope limit.

---

## 12. Contrast Trust QA

- [ ] Important text, CTAs, form controls, focus indicators, and state messages read clearly on their surfaces.
- [ ] Disabled, placeholder, secondary, and low-priority text do not collapse into unreadable ambiguity.
- [ ] Focus indicator remains visible against relevant backgrounds.
- [ ] Error/success/required/current meanings do not rely on color alone where task clarity matters.
- [ ] Contrast corrections preserve hierarchy and avoid panic styling.
- [ ] Unverified contrast is recorded as **SAFE UNKNOWN**, not declared safe by feel.

---

## 13. Taxonomy QA

Check for:

- [ ] decorative ARIA spam;
- [ ] focus invisibility;
- [ ] keyboard dead-ends;
- [ ] fake semantic structure;
- [ ] screen-reader contamination;
- [ ] interaction trap drift;
- [ ] contrast hallucination;
- [ ] inaccessible hover dependency;
- [ ] mobile accessibility collapse;
- [ ] semantic-role inflation;
- [ ] accessibility theater;
- [ ] overengineered accessibility wrappers;
- [ ] accessibility inconsistency.

Record matches using [`accessibility-drift-taxonomy.md`](../../projects/mars-website-factory/accessibility-drift-taxonomy.md).

---

## 14. Escalation Boundary

Stop and escalate when an accessibility fix would:

- invent a custom control, modal, disclosure, validation model, focus manager, live-region system, or accessibility overlay;
- add ARIA everywhere instead of correcting semantic HTML;
- claim screen-reader support without evidence;
- change CTA meaning, form flow, state behavior, or responsive order;
- require legal/compliance interpretation outside current scope;
- require project-specific accessibility standard, specialist audit, or HITL decision;
- redesign Triumph or any project by accessibility taste alone.

Use **PARTIAL — accessibility intent** or **SAFE UNKNOWN** rather than silent accessibility theater.

---

## 15. REPORT Block

Use this block when accessibility intent QA is in scope:

```text
ACCESSIBILITY FINDINGS — <section or block_id> — <source ref>

Accessibility authority: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Active source:
- Accessibility behavior observed:
- Accessibility behavior inferred:
- Missing / unknown accessibility evidence:
- SAFE UNKNOWN resolver:

Semantic accessibility: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Native semantics:
- Heading / landmark integrity:
- Labels / names / roles:
- ARIA restraint:

Focus / keyboard survivability: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Focus visibility:
- Keyboard order / activation:
- Trap / dead-end risk:
- Hover dependency:

CTA / form accessibility: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- CTA labels and states:
- Form labels / helper text:
- Validation / error recovery:
- Submission / loading / success / failure:

Mobile accessibility continuity: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Mobile order / labels:
- Tap clarity:
- Sticky / fixed obstruction:
- Mobile state legibility:

Assistive predictability: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Screen-reader clarity evidence:
- Duplicate / noisy output risk:
- State announcement risk:

Contrast trust: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Text / CTA / form readability:
- Focus contrast:
- State distinction:

Accessibility taxonomy:
- Patterns:
- Severity:
- Contamination / theater risk:

Disposition:
- Freeze impact:
- Action: no action | semantic correction | restrained enhancement | removed noise | deferred | HITL required | accessibility review required
- Evidence:
```

---

## 16. Not Claimed

- No full WCAG audit.
- No automated accessibility testing.
- No screen-reader simulation or cross-AT matrix.
- No runtime accessibility AI.
- No universal accessibility aesthetics.
- No autonomous remediation.

Defer to Website Factory accessibility governance, source authority, project implementation packs, HITL decisions, foundation QA, and specialist accessibility scope where applicable.

---

## 17. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge accessibility intent checklist; adds `ACCESSIBILITY FINDINGS`. |
