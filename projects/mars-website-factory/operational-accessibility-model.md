# MARS Website Factory — Operational Accessibility Model

**Status:** **documented** — Website Factory model for human-supervised operational accessibility review.  
**Not:** WCAG engine, automated screen-reader validator, runtime remediation system, compliance certification, or universal accessibility truth.

**Parent layer:** [accessibility-intent-governance.md](accessibility-intent-governance.md).  
**Taxonomy:** [accessibility-drift-taxonomy.md](accessibility-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/accessibility-intent-checklist.md`](../../agents/mars-forge/accessibility-intent-checklist.md).

---

## 1. Purpose

This model defines what Website Factory means by operational accessibility:

```text
ACCESSIBILITY = TRUSTED OPERATIONAL USABILITY
```

The model helps Forge and human operators distinguish:

- semantic-first accessibility from ARIA decoration;
- keyboard survivability from pointer-only usability;
- restrained enhancement from accessibility theater;
- screen-reader clarity from assistive contamination;
- trustworthy states from fake accessibility patches.

It is qualitative methodology. It does not prescribe exact token values, legal compliance scope, assistive technology matrices, or component APIs.

---

## 2. Semantic-First Accessibility

Semantic-first accessibility means structure and controls carry their meaning through native HTML before enhancement.

Expected:

- headings express real document hierarchy;
- links navigate and buttons act;
- lists, sections, forms, labels, fieldsets, tables, and landmarks are used when they match actual meaning;
- custom roles appear only when native semantics cannot express the component;
- accessible names describe user-relevant meaning, not internal implementation or decorative copy.

Drift:

- div/button imitation;
- fake heading levels for visual size;
- ARIA role inflation;
- duplicate labels and redundant landmarks;
- semantic wrappers used to look compliant while behavior remains wrong.

**Rule:** if native HTML solves the meaning, adding ARIA must clear a higher bar.

---

## 3. Keyboard-First Survivability

Keyboard-first survivability means a user can move through core actions, forms, navigation, disclosures, CTAs, and custom controls without a mouse.

Expected:

- actionable elements are keyboard reachable in meaningful order;
- focus is visible and recoverable;
- keyboard activation matches the control role;
- modal, menu, disclosure, sticky, carousel, or custom behavior does not trap users;
- skip paths or landmark structure support orientation when page complexity warrants it.

Drift:

- keyboard dead-ends;
- focus lost after interaction;
- mouse-only hover reveals;
- custom controls without keyboard activation;
- focus jumps into hidden or irrelevant elements;
- trapped modals, menus, or sticky layers.

**Rule:** keyboard continuity is not optional polish. It is operational survivability.

---

## 4. Restrained Accessibility Enhancement

Restrained enhancement means accessibility additions are deliberate, minimal, and role-based.

Acceptable:

- `aria-expanded` for real disclosures;
- `aria-current` for active navigation context;
- `aria-describedby` for concise field help or error association;
- polite live region for meaningful async status when needed;
- visually hidden text that clarifies an otherwise ambiguous control;
- native focus styling adjusted to remain visible and design-consistent.

Risky by default:

- labels on every decorative icon;
- live regions for routine visual changes;
- redundant roles on native elements;
- verbose hidden text that repeats visible content;
- wrapper components whose accessibility contract is unclear;
- ARIA used to compensate for incorrect HTML.

**Rule:** enhancement should reduce user uncertainty. If it increases assistive noise, it is drift.

---

## 5. Predictable Interaction Flow

Accessible interaction flow means users can anticipate what happens before, during, and after action.

Expected:

- CTAs have clear names, roles, states, and destination/action expectations;
- disabled, loading, validation, success, and error states remain truthful;
- disclosures, tabs, menus, and modals communicate expanded/current/selected state where relevant;
- repeated controls behave consistently;
- focus movement after action is deliberate and recoverable.

Drift:

- fake disabled or fake loading states;
- action results announced visually but not semantically;
- CTA labels that hide the real action;
- inconsistent focus after repeated patterns;
- custom behavior that works by mouse but not keyboard.

**Rule:** accessibility must stay behaviorally consistent with interaction intent and state integrity.

---

## 6. Mobile Accessibility Continuity

Mobile accessibility continuity means narrow and touch contexts preserve labels, tap clarity, focus, readable text, state feedback, and assistive order.

Expected:

- tap targets remain clear and reachable;
- mobile order preserves semantic reading path;
- labels and helper text do not disappear when layout collapses;
- validation remains associated with fields;
- sticky/fixed UI does not obstruct content or trap focus;
- hover-only content has mobile and keyboard equivalents or is removed.

Drift:

- mobile accessibility collapse;
- text or labels hidden to save space;
- icon-only mobile controls without useful names;
- sticky CTA blocking focus or content;
- collapsed sections with unclear expanded state;
- desktop hover assumptions copied into touch context.

**Rule:** mobile is an accessibility context, not a smaller screenshot.

---

## 7. Accessible CTA Hierarchy

Accessible CTA hierarchy means conversion paths remain clear without pressure, ambiguity, or assistive noise.

Expected:

- primary CTA label names the action clearly;
- secondary CTA remains semantically and visually subordinate;
- repeated CTA labels stay consistent unless section role changes;
- focus and active states are visible;
- loading/disabled states communicate actual availability;
- mobile CTA presentation avoids obstruction or coercion.

Drift:

- “click here” labels with no destination meaning;
- icon-only CTA without name;
- pulsing/sticky pressure that harms trust;
- secondary CTA receiving stronger accessible emphasis than primary;
- disabled-looking CTA that still acts;
- CTA hidden behind hover, animation, or visual-only affordance.

**Rule:** CTA accessibility supports trust. It must not become conversion theater.

---

## 8. Form Accessibility Seriousness

Forms require higher seriousness because mistakes, uncertainty, and recovery directly affect user trust.

Expected:

- every input has a durable label;
- required/optional state is understandable;
- helper text and error messages are associated with fields;
- validation timing is predictable;
- errors explain recovery;
- submission, loading, success, and failure states are clear;
- focus supports correction after failed submission.

Drift:

- placeholder-only labels;
- errors shown visually but not associated;
- validation panic styling;
- all fields announced as urgent;
- success claimed before real outcome;
- masked required fields;
- inaccessible custom selects, date pickers, or upload controls.

**Rule:** forms must remain understandable before they become visually impressive.

---

## 9. State Accessibility Integrity

State accessibility integrity means hover, focus, active, current, selected, disabled, loading, validation, success, and error states remain meaningful across visual and assistive contexts.

Expected:

- focus visible and distinct;
- disabled state truthfully blocks action;
- loading state represents real waiting;
- current/selected state matches navigation or selection reality;
- validation, success, and error states preserve recovery;
- reduced-motion or motion-sensitive uncertainty is surfaced when relevant.

Drift:

- focus invisibility;
- selected/current state mismatch;
- fake disabled opacity;
- decorative loading;
- inaccessible validation;
- success/error ambiguity;
- accessibility-state drift hidden behind visual polish.

**Rule:** state accessibility is trust infrastructure.

---

## 10. Assistive Readability

Assistive readability means screen-reader and keyboard users receive concise, ordered, truthful output.

Expected:

- page structure can be skimmed by headings and landmarks;
- labels avoid duplicate visible text unless useful;
- icons are hidden when decorative and named when functional;
- live updates are limited to meaningful changes;
- hidden text clarifies, not markets;
- reading order follows user task order.

Drift:

- screen-reader contamination from redundant labels;
- decorative icons announced repeatedly;
- live-region spam;
- duplicate landmarks;
- hidden marketing paragraphs;
- visual order and DOM order diverge without reason.

**Rule:** more assistive text is not automatically more accessibility.

---

## 11. Contrast Trust

Contrast trust means readability, state distinction, and emphasis are believable without panic styling.

Expected:

- important text and controls are readable against their surfaces;
- focus, error, disabled, and active states remain distinguishable;
- contrast supports hierarchy rather than flattening every element;
- low-emphasis text is not used for critical instructions;
- visual changes remain consistent across light/dark surfaces.

Drift:

- contrast hallucination: claiming contrast is safe without inspection;
- panic high-contrast patches that destroy hierarchy;
- disabled, placeholder, and secondary text collapsing into unreadable gray;
- focus ring disappearing on dark/light surface changes;
- state colors that rely on color alone when meaning matters.

**Rule:** contrast is a trust signal. It should clarify, not theatricalize.

---

## 12. Accessibility Escalation Drift

Accessibility escalation drift happens when each concern is solved by adding more wrappers, labels, roles, announcements, or contrast drama instead of restoring simple semantic clarity.

Symptoms:

- ARIA added to compensate for wrong elements;
- hidden labels become verbose marketing copy;
- live regions announce minor style changes;
- focus is scripted around bad DOM order;
- custom control wrappers multiply;
- contrast patches become louder than section hierarchy.

Response:

- return to native semantics;
- reduce redundant assistive output;
- repair focus and keyboard flow at the source;
- align state behavior with actual capability;
- record drift in `ACCESSIBILITY FINDINGS`;
- escalate when project-specific accessibility scope requires specialist review.

---

## 13. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Assistive behavior was not checked | Cannot claim screen-reader clarity or lack of contamination. |
| Keyboard path was not tested | Cannot claim continuity, focus order, or no traps. |
| Custom control semantics are unclear | Cannot prove role, name, state, and keyboard behavior. |
| Mobile collapse changes labels/order | Cannot infer accessible continuity from desktop layout. |
| Form validation rules are absent | Cannot define error association, timing, or recovery semantics. |
| Contrast or focus visibility is uncertain | Cannot claim readable and navigable states. |
| ARIA exists without known reason | Cannot distinguish enhancement from contamination. |

**Action:** resolve through implementation evidence, manual keyboard review, assistive spot-check, annotated source, implementation-pack note, HITL, or scoped accessibility review.

---

## 14. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Operational Accessibility Model — semantic-first, keyboard-first, restrained enhancement, mobile continuity, CTA/form/state integrity, assistive readability, contrast trust, and escalation drift. |
