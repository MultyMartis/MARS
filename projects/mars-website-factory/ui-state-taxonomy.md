# MARS Website Factory — UI State Taxonomy

**Status:** **documented** — Website Factory drift vocabulary for human-supervised UI state QA.  
**Not:** automated state detector, accessibility audit engine, runtime validator, component library spec, or universal UI-state ontology.

**Parent layer:** [state-behavioral-consistency-governance.md](state-behavioral-consistency-governance.md).  
**Integrity model:** [interaction-state-integrity-model.md](interaction-state-integrity-model.md).  
**Forge checklist:** [`../../agents/mars-forge/state-consistency-checklist.md`](../../agents/mars-forge/state-consistency-checklist.md).

---

## 1. Purpose

This taxonomy names UI state drift patterns so Website Factory and Forge work can report state behavior problems without inventing redesign language.

Use it when reviewing:

- hover, focus, active, pressed, selected, current, disabled, readonly, loading, validation, success, and error states;
- CTA state behavior across repeated conversion moments;
- form and navigation feedback;
- mobile/tap and keyboard state continuity;
- component state consistency across sections and breakpoints;
- template, dashboard, or library state contamination.

Taxonomy names are qualitative governance labels. They are not automated findings.

---

## 2. Drift Families

| Family | Core risk |
|--------|-----------|
| **Affordance drift** | The state promises capability or action that is absent, unavailable, or different. |
| **Feedback drift** | Feedback is too weak, too loud, misleading, late, early, or inconsistent. |
| **State hierarchy drift** | Primary, secondary, disabled, error, or success states compete at the wrong intensity. |
| **Accessibility-state drift** | Focus, keyboard, validation, disabled, or reduced-motion-sensitive states become invisible or unreliable. |
| **Cross-component drift** | Similar components use different state rules without source authority. |
| **Breakpoint state drift** | Mobile/tablet state behavior loses meaning or diverges from desktop without documented intent. |
| **Contaminated state behavior** | Dashboard, SaaS, template, or library defaults override project state intent. |

---

## 3. Canonical Drift Patterns

| Pattern | Definition | Typical symptom | Governance response |
|---------|------------|-----------------|---------------------|
| **Hover inconsistency** | Similar elements use different hover behavior without source authority. | Same cards lift in one section, glow in another, and stay static elsewhere. | Normalize by role or document exception. |
| **CTA state drift** | CTA states change hierarchy, pressure, or feedback across repeated CTA roles. | Primary button pulses in one place, only changes color elsewhere, loses focus state on mobile. | Re-anchor to CTA role and state integrity model. |
| **Fake disabled state** | A control looks unavailable without truthful disabled semantics or remains clickable while dimmed. | Low opacity link still works, button appears dead but submits. | Align visual, DOM/behavior, copy, and accessibility semantics. |
| **Misleading affordance** | State styling suggests clickability, selection, drag, loading, or validation that is not real. | Static card hovers like a button; icon looks like a control. | Bind intended action, demote affordance, or report ambiguity. |
| **Infinite loading ambiguity** | Loading feedback has no clear source, progress, timeout, or completion semantics. | Endless spinners, shimmer everywhere, no outcome message. | Restrict loading to real async work and disclose unknowns. |
| **Validation overload** | Validation feedback overwhelms the user instead of guiding recovery. | Every field glows red, multiple messages repeat, error summary competes with form. | Reduce to clear, recoverable guidance. |
| **Success-state celebration spam** | Success feedback becomes decorative celebration rather than confirmation. | Confetti, large animations, repeated success banners after small actions. | Confirm completion with restraint. |
| **Error-state panic drift** | Error treatment escalates severity beyond task reality. | Aggressive red floods, alarming copy, shaking controls, full-page panic for recoverable field errors. | Preserve trust and recovery path. |
| **Focus invisibility** | Keyboard focus is hidden, inconsistent, or visually lost. | Outline removed, focus blends into background, focus appears only in some sections. | Restore visible focus or escalate accessibility uncertainty. |
| **Keyboard-state neglect** | State behavior exists for mouse but not keyboard. | Hover reveals required controls; focus order skips actionable elements. | Align keyboard and pointer affordance or escalate. |
| **State mismatch across components** | Same semantic role uses different state families. | Forms, cards, and CTAs each invent local disabled/loading/error styles. | Normalize by role and source authority. |
| **Behavioral fragmentation** | State rules vary enough that the interface feels assembled from unrelated systems. | Navigation, CTA, forms, and cards all use different feedback tone. | Re-anchor to project state philosophy. |
| **Mobile-state inconsistency** | Mobile loses or invents state behavior relative to role. | Desktop hover has no tap equivalent; mobile active state is sticky or unclear. | Review mobile state continuity and record unknowns. |

---

## 4. Hover / Focus Drift

| Pattern | Why it matters |
|---------|----------------|
| **Hover hierarchy inversion** | Secondary objects become behaviorally stronger than primary actions. |
| **Hover carpet** | Every object reacts and hierarchy collapses. |
| **Hover-only state** | Required information or action exists only on hover, excluding touch and keyboard users. |
| **Focus ring lottery** | Focus style differs randomly across controls. |
| **Focus suppression** | Focus visibility is removed for visual cleanliness. |

Rule: hover may clarify affordance; focus must preserve keyboard clarity.

---

## 5. Disabled / Loading Drift

| Pattern | Why it matters |
|---------|----------------|
| **Fake disabled opacity** | Opacity alone can look like secondary priority, not true unavailability. |
| **Disabled-but-clickable** | Trust breaks because state and action disagree. |
| **Clickable-but-disabled-looking** | Users may avoid valid actions. |
| **Decorative spinner** | Loading appears without real process or waiting state. |
| **Skeleton wallpaper** | Loading placeholders become visual style, not state communication. |
| **Infinite waiting ambiguity** | User cannot tell whether progress exists, failed, or stalled. |

Rule: unavailable and waiting states must be truthful, not decorative.

---

## 6. Validation / Success / Error Drift

| Pattern | Why it matters |
|---------|----------------|
| **Glowing validation** | Visual drama can obscure actual correction guidance. |
| **Punitive validation** | Feedback feels like blame rather than help. |
| **Validation timing chaos** | Some fields validate live, some on blur, some on submit without reason. |
| **Success celebration overload** | Confirmation becomes noise and may interrupt the next task. |
| **Error panic styling** | Recoverable problems feel catastrophic. |
| **Error without recovery** | User sees failure but not next step. |

Rule: validation guides, success confirms, error preserves trust.

---

## 7. CTA State Drift

| Pattern | Why it matters |
|---------|----------------|
| **CTA behavior lottery** | Same CTA role behaves differently across sections. |
| **Primary/secondary state collapse** | Secondary CTA receives equal or stronger hover/focus/active feedback. |
| **Loading as pressure** | CTA loading animation is used to imply urgency or sophistication. |
| **Disabled CTA ambiguity** | User cannot tell whether CTA is unavailable, secondary, submitted, or visually muted. |
| **Mobile CTA state mismatch** | Mobile CTA changes pressure, disabled, focus, or active behavior without source reason. |

Rule: CTA state behavior is conversion governance, not local decoration.

---

## 8. Breakpoint / Mobile Drift

| Pattern | Why it matters |
|---------|----------------|
| **Desktop hover leakage** | Desktop state assumptions fail on touch. |
| **Tap state invisibility** | User receives no confirmation that tap registered. |
| **Mobile focus neglect** | Keyboard and assistive flows are ignored on narrow screens. |
| **Mobile validation compression** | Error/help text becomes cramped or separated from the field. |
| **Sticky state confusion** | Fixed CTA, nav, or notification states obstruct or pressure the user. |

Rule: mobile state behavior is part of responsive intent, not a fallback.

---

## 9. Severity Guidance

| Severity | UI state drift condition |
|----------|--------------------------|
| **Blocker** | Hidden focus on critical flow, misleading disabled/active CTA, fake success/failure, validation that blocks recovery, or mobile state that prevents action. |
| **Major** | CTA state drift, infinite loading ambiguity, keyboard-state neglect, error panic styling, or cross-component state mismatch in repeated elements. |
| **Minor** | Local hover inconsistency, excessive success feedback, or decorative state styling that does not block action but should be restrained. |
| **Observation** | State behavior is intentionally calm and stable; no change required, but source authority may be noted. |

Severity remains human-supervised and source-dependent.

---

## 10. Reporting Vocabulary

Use this compact vocabulary in `STATE CONSISTENCY FINDINGS`:

```text
UI state taxonomy:
- Pattern(s): <taxonomy names>
- Severity: blocker | major | minor | observation | SAFE UNKNOWN
- Source authority: observed | inferred | assumed | unknown
- Affected state: hover | focus | active | disabled | loading | validation | success | error | CTA | mobile | keyboard | other
- Disposition: pass | partial | fail | deferred | HITL required | accessibility review required
```

---

## 11. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Static source has no state examples | Cannot infer state family or intensity from static layout alone. |
| Component role is unclear | Cannot decide whether object is static, link, button, disclosure, form control, or disabled state. |
| Existing code includes unexplained state behavior | Cannot prove whether behavior is approved, legacy, or contamination. |
| Mobile state behavior is absent | Cannot infer tap, active, focus, validation, or sticky behavior from desktop hover. |
| Validation rules are missing | Cannot decide timing, severity, placement, or recovery pattern. |
| Accessibility impact is unclear | Cannot claim focus, keyboard, disabled, or reduced-motion integrity without evidence. |

**Action:** escalate to annotated state source, implementation-pack rule, component-state note, prototype, HITL decision, or accessibility review.

---

## 12. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial UI state taxonomy for hover, CTA, disabled, loading, validation, success/error, focus, keyboard, cross-component, and mobile state drift. |
