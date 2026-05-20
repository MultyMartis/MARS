# MARS Website Factory — Accessibility Drift Taxonomy

**Status:** **documented** — Website Factory drift vocabulary for human-supervised accessibility intent QA.  
**Not:** automated accessibility detector, WCAG lint engine, assistive technology simulator, runtime validator, or universal accessibility ontology.

**Parent layer:** [accessibility-intent-governance.md](accessibility-intent-governance.md).  
**Operational model:** [operational-accessibility-model.md](operational-accessibility-model.md).  
**Forge checklist:** [`../../agents/mars-forge/accessibility-intent-checklist.md`](../../agents/mars-forge/accessibility-intent-checklist.md).

---

## 1. Purpose

This taxonomy names accessibility drift patterns so Website Factory and Forge work can report accessibility problems without pretending to run a full audit.

Use it when reviewing:

- semantic HTML and ARIA;
- headings, landmarks, labels, roles, and states;
- focus visibility and keyboard flow;
- forms and validation;
- CTA and custom-control behavior;
- mobile accessibility continuity;
- contrast and state readability;
- screen-reader noise or missing assistive meaning.

Taxonomy names are qualitative governance labels. They are not automated findings.

---

## 2. Drift Families

| Family | Core risk |
|--------|-----------|
| **Semantic drift** | Markup, roles, headings, labels, or landmarks do not match actual meaning. |
| **Keyboard drift** | Keyboard path becomes incomplete, invisible, trapped, or unpredictable. |
| **Assistive contamination** | Screen-reader output becomes noisy, duplicate, misleading, or decorative. |
| **Interaction accessibility drift** | Hover, custom controls, disclosures, modals, CTAs, or states fail non-pointer users. |
| **Mobile accessibility drift** | Responsive collapse removes labels, order, tap clarity, focus, or state readability. |
| **Contrast and state drift** | Readability or state distinction is claimed without trustworthy evidence. |
| **Accessibility theater** | Symbolic compliance replaces operational usability. |

---

## 3. Canonical Drift Patterns

| Pattern | Definition | Typical symptom | Governance response |
|---------|------------|-----------------|---------------------|
| **Decorative ARIA spam** | ARIA added broadly without semantic need. | Redundant roles, labels on decorative icons, repeated hidden text. | Remove noise, restore native semantics, justify remaining ARIA. |
| **Focus invisibility** | Keyboard focus exists technically but cannot be seen or followed. | Outline removed, ring blends into surface, inconsistent focus treatment. | Restore visible focus aligned with state integrity. |
| **Keyboard dead-ends** | Keyboard users cannot reach, activate, leave, or recover from part of the interface. | Modal trap, menu trap, skipped CTA, unreachable custom card. | Fix keyboard path or escalate before freeze. |
| **Fake semantic structure** | Markup claims structure that content/behavior does not support. | Fake landmarks, fake buttons, heading levels used for size, div controls. | Rebuild semantic HTML or record structural change need. |
| **Screen-reader contamination** | Assistive output is noisy, duplicated, misleading, or decorative. | Repeated icon names, duplicated labels, hidden marketing copy, live-region spam. | Reduce output to concise truthful meaning. |
| **Interaction trap drift** | Interaction flow traps focus, pointer, scroll, modal, or keyboard context. | User cannot escape overlay, sticky layer blocks target, disclosure state unclear. | Restore recoverability and state semantics. |
| **Contrast hallucination** | Contrast is claimed safe because it “looks fine” or tooling is assumed. | Low-contrast text, invisible focus, unreadable disabled/placeholder text. | Inspect, adjust with hierarchy restraint, or record **SAFE UNKNOWN**. |
| **Inaccessible hover dependency** | Required content or controls depend on hover. | Tooltips, labels, actions, or reveal content appear only on hover. | Provide keyboard/mobile equivalent or remove dependency. |
| **Mobile accessibility collapse** | Responsive behavior breaks labels, order, focus, tap clarity, or state feedback. | Hidden labels, icon-only controls, sticky CTA obstruction, dense unreadable validation. | Re-anchor to mobile accessibility continuity. |
| **Semantic-role inflation** | More roles, headings, landmarks, or labels are added than structure warrants. | Every region becomes a landmark; every visual label becomes assistive label. | Reduce semantic hierarchy to meaningful structure. |
| **Accessibility theater** | Compliance-looking artifacts do not improve real usability. | Badges, overlays, vague inclusive copy, ARIA wrappers without task improvement. | Record as fake accessibility and refocus on operational use. |
| **Overengineered accessibility wrappers** | Custom abstractions replace simple native semantics and increase failure risk. | Custom button/link/input wrappers with uncertain focus, role, keyboard, and state behavior. | Prefer native HTML or require component contract evidence. |
| **Accessibility inconsistency** | Similar controls have different accessible names, focus, keyboard, or state behavior without reason. | CTAs, links, cards, forms, or nav items behave inconsistently by section. | Normalize by role or document source-authorized exception. |

---

## 4. ARIA and Semantic Drift

| Pattern | Why it matters |
|---------|----------------|
| **ARIA everywhere** | More attributes can make output worse when native semantics already work. |
| **Role contradiction** | ARIA role says one thing while behavior and visual affordance say another. |
| **Redundant role noise** | Native elements receive unnecessary roles that add maintenance risk. |
| **Fake control semantics** | Element announces as control but lacks keyboard, focus, or state behavior. |
| **Decorative label pollution** | Decorative icons, badges, or flourishes are announced as meaningful content. |
| **Landmark inflation** | Too many landmarks destroy orientation instead of supporting it. |

Rule: ARIA is a semantic repair tool, not a decoration layer.

---

## 5. Focus and Keyboard Drift

| Pattern | Why it matters |
|---------|----------------|
| **Invisible focus** | Users cannot know where they are. |
| **Focus order mismatch** | Keyboard path contradicts visual/task order. |
| **Focus loss after action** | User acts and orientation disappears. |
| **Keyboard trap** | User cannot exit modal, menu, carousel, sticky layer, or custom control. |
| **Keyboard neglect** | Pointer behavior exists but keyboard equivalent is missing. |
| **Focus style lottery** | Comparable controls use inconsistent focus visibility and intensity. |

Rule: focus and keyboard continuity are operational infrastructure, not optional accessibility polish.

---

## 6. Screen-Reader Drift

| Pattern | Why it matters |
|---------|----------------|
| **Duplicate announcement** | Visible text, aria-label, title, and hidden text repeat the same content. |
| **Verbose hidden marketing** | Hidden content adds persuasion instead of useful meaning. |
| **Live-region spam** | Routine or decorative changes interrupt assistive users. |
| **Missing state announcement** | Expanded, current, selected, invalid, loading, or error state is unclear. |
| **Icon announcement clutter** | Decorative or repeated icons pollute reading flow. |
| **DOM/visual order split** | Assistive order no longer matches the intended task flow. |

Rule: screen-reader clarity requires less noise and more truthful structure.

---

## 7. Mobile Accessibility Drift

| Pattern | Why it matters |
|---------|----------------|
| **Desktop hover leakage** | Hover logic is copied to mobile where it cannot operate. |
| **Hidden mobile labels** | Labels disappear to save space, leaving controls ambiguous. |
| **Icon-only mobile controls** | Controls rely on visual recognition without useful names. |
| **Tap ambiguity** | User cannot tell what is tappable or what action will occur. |
| **Mobile focus neglect** | Focus and keyboard behavior are ignored on narrow/touch contexts. |
| **Sticky obstruction** | Sticky/fixed UI hides content, focus, validation, or CTA context. |
| **Collapsed validation loss** | Error/help text loses association with fields after stacking. |

Rule: mobile accessibility is not solved by fitting content into the viewport.

---

## 8. Form Accessibility Drift

| Pattern | Why it matters |
|---------|----------------|
| **Placeholder-only label** | Label disappears during entry and may not provide durable accessible name. |
| **Unassociated error** | Error exists visually but is not tied to the field. |
| **Validation panic** | Styling overwhelms correction and damages trust. |
| **Required ambiguity** | Required/optional state is unclear. |
| **Submission-state ambiguity** | User cannot tell whether the form is loading, failed, submitted, or recoverable. |
| **Custom input opacity** | Selects, date pickers, uploads, masks, or checkboxes hide keyboard/state semantics. |

Rule: form accessibility requires serious labels, instructions, validation, and recovery.

---

## 9. Contrast and State Drift

| Pattern | Why it matters |
|---------|----------------|
| **Contrast hallucination** | Readability is assumed without evidence. |
| **Focus contrast failure** | Focus indicator disappears on some surfaces. |
| **Disabled opacity ambiguity** | Disabled, secondary, placeholder, and low-priority text collapse visually. |
| **Color-only meaning** | Error/success/required/current state relies only on color where meaning matters. |
| **Contrast panic styling** | High-contrast patches create false severity or destroy hierarchy. |

Rule: contrast should support readability and state distinction while preserving trust.

---

## 10. Behavioral Noise Indicators

The following symptoms usually indicate accessibility fatigue or contamination:

- more accessibility attributes than meaningful structure;
- repeated hidden labels for every icon or badge;
- focus jumps after minor interactions;
- live announcements for decorative changes;
- forms announce too much before the user acts;
- mobile controls lose names or tap clarity;
- visible semantics and assistive semantics tell different stories;
- keyboard users must guess where interaction moved.

---

## 11. Severity Guidance

| Severity | Accessibility drift condition |
|----------|-------------------------------|
| **Blocker** | Keyboard trap, critical CTA/form inaccessible, invisible focus in action path, misleading role on critical control, or hover-only required action. |
| **Major** | Screen-reader contamination in key flow, mobile accessibility collapse, fake semantic structure, inaccessible custom control, major contrast/focus uncertainty. |
| **Minor** | Local redundant ARIA, inconsistent non-critical labels, decorative icon announcement, or focus styling mismatch not blocking task completion. |
| **Observation** | Accessibility remains intentionally restrained and semantically sound; no change required, but evidence limits may be noted. |

Severity remains human-supervised and source-/scope-dependent.

---

## 12. Reporting Vocabulary

Use this compact vocabulary in `ACCESSIBILITY FINDINGS`:

```text
Accessibility taxonomy:
- Pattern(s): <taxonomy names>
- Severity: blocker | major | minor | observation | SAFE UNKNOWN
- Source authority: observed | inferred | assumed | unknown
- Affected surface: semantics | focus | keyboard | CTA | form | state | mobile | contrast | assistive output | custom control | other
- Disposition: pass | partial | fail | deferred | HITL required | accessibility review required
```

---

## 13. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| No keyboard review was performed | Cannot claim keyboard continuity or no traps. |
| No assistive output review was performed | Cannot claim screen-reader clarity. |
| Focus style varies across surfaces | Cannot claim focus survivability without checking states. |
| Contrast is not inspected | Cannot claim contrast trust. |
| Custom control contract is missing | Cannot prove role, name, state, keyboard, and focus behavior. |
| Mobile collapse changes labels/order | Cannot prove mobile accessibility continuity. |
| Existing ARIA has no known rationale | Cannot distinguish necessary enhancement from contamination. |

**Action:** escalate to source note, implementation evidence, manual review, HITL, or scoped accessibility specialist review.

---

## 14. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial accessibility drift taxonomy for ARIA spam, focus/keyboard drift, semantic mismatch, screen-reader contamination, mobile collapse, contrast hallucination, accessibility theater, wrappers, and inconsistency. |
