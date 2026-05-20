# MARS Forge — State Consistency Checklist

**Status:** Forge overlay checklist for **human-supervised** state and behavioral consistency QA.  
**Not:** automated state detector, runtime UI engine, accessibility audit AI, component library spec, autonomous redesign, or universal UI-state truth.

**Factory methodology:** [`../../projects/mars-website-factory/state-behavioral-consistency-governance.md`](../../projects/mars-website-factory/state-behavioral-consistency-governance.md).  
**UI state taxonomy:** [`../../projects/mars-website-factory/ui-state-taxonomy.md`](../../projects/mars-website-factory/ui-state-taxonomy.md).  
**Integrity model:** [`../../projects/mars-website-factory/interaction-state-integrity-model.md`](../../projects/mars-website-factory/interaction-state-integrity-model.md).

---

## 1. When to Run

Run this checklist:

- when hover, focus, active, selected, current, disabled, readonly, loading, validation, success, error, CTA state, keyboard behavior, mobile tap state, form state, or navigation state is in scope;
- after source interpretation QA identifies what states are observed, inferred, assumed, or unknown;
- alongside interaction intent, responsive intent, design intent, visual reconciliation, content density, cadence, and rhythm QA when states affect their read;
- before section freeze or before declaring state behavior acceptable.

This checklist does not authorize inventing new UI state systems, validation frameworks, loading systems, accessibility products, or mandatory interaction aesthetics without source authority or HITL.

---

## 2. Authority and Scope

- [ ] Active design version, source screen, and implementation pack are identified.
- [ ] UI states are classified as observed / inferred / assumed / unknown.
- [ ] Missing hover, focus, active, disabled, loading, validation, success, error, keyboard, or mobile states are recorded as **SAFE UNKNOWN** when material.
- [ ] Existing code state behavior is checked against active source before being preserved.
- [ ] No archived mockup, SaaS template, dashboard pattern, component-library default, or previous project state behavior overrides active source.
- [ ] Any state not source-authorized is restrained, removed, deferred, or escalated.

---

## 3. Hover State QA

- [ ] Hover states reinforce action, affordance, or hierarchy, not decoration.
- [ ] Non-clickable elements do not hover as if clickable.
- [ ] Hover strength follows primary / secondary / supporting hierarchy.
- [ ] Similar components use consistent hover behavior unless source documents an exception.
- [ ] Hover-only usability is absent or escalated.
- [ ] Mobile equivalent is known, restrained, or recorded as **SAFE UNKNOWN**.

---

## 4. Focus and Keyboard QA

- [ ] Focus state remains visible across surfaces and components.
- [ ] Focus style is consistent for comparable controls.
- [ ] Focus is not replaced by hover-only behavior.
- [ ] Keyboard path reaches actionable elements in meaningful order where in scope.
- [ ] Focus does not become visually confused with hover, active, selected, disabled, success, or error states.
- [ ] Accessibility-sensitive uncertainty is recorded as **SAFE UNKNOWN** or escalated.

---

## 5. Active / Pressed State QA

- [ ] Active/pressed feedback confirms input without claiming completion.
- [ ] Active state is visually distinct from disabled, selected, and success states.
- [ ] Mobile tap feedback is clear and not sticky or confusing.
- [ ] CTA active states are consistent across repeated CTA roles.
- [ ] Active feedback does not change CTA hierarchy or create pressure.

---

## 6. Disabled State QA

- [ ] Disabled controls are clearly distinct from enabled and secondary controls.
- [ ] Disabled-looking controls do not remain clickable unless source explains the state.
- [ ] Enabled controls do not look disabled through over-restraint.
- [ ] Disabled state is not communicated only by ambiguous opacity when action clarity matters.
- [ ] Disabled/loading/readonly/secondary states are not visually collapsed into one ambiguous state.
- [ ] Missing disabled reason or behavior is recorded as **SAFE UNKNOWN** when material.

---

## 7. Loading-State QA

- [ ] Loading state represents real waiting, submission, fetching, rendering, or processing.
- [ ] Loading scope is clear: page, section, form, button, card, media, or other.
- [ ] Loading state has completion, failure, timeout, retry, or next-step semantics where relevant.
- [ ] No decorative spinner, skeleton, shimmer, fake progress bar, or theatrical loading is introduced without authority.
- [ ] CTA loading does not become pressure or fake seriousness.
- [ ] Infinite loading ambiguity is flagged.

---

## 8. Validation-State QA

- [ ] Validation timing is known or documented: live, blur, submit, summary, or combined.
- [ ] Validation guides correction instead of punishing the user.
- [ ] Field-level and form-level messages are not contradictory.
- [ ] Error copy explains recovery where needed.
- [ ] Success/valid feedback is restrained and does not compete with primary action.
- [ ] No glowing validation, panic styling, or validation overload introduced.
- [ ] Missing validation rules are recorded as **SAFE UNKNOWN**.

---

## 9. Success / Error QA

- [ ] Success state confirms a real completed outcome.
- [ ] Success feedback is proportionate and does not spam celebration.
- [ ] Error state explains what failed and what can happen next.
- [ ] Error severity matches task severity.
- [ ] Recoverable errors do not receive catastrophic styling.
- [ ] Success/error treatment stays consistent across comparable forms, CTAs, and flows.

---

## 10. CTA State Consistency QA

- [ ] Primary CTA hover/focus/active/loading/disabled behavior is consistent across comparable sections.
- [ ] Secondary and tertiary CTA states remain behaviorally subordinate.
- [ ] CTA states clarify action without pressure, fake urgency, or decorative motion.
- [ ] CTA disabled/loading states are unambiguous.
- [ ] Mobile CTA states preserve hierarchy, trust, and tap clarity.
- [ ] Repeated CTA blocks do not escalate state drama section by section.

---

## 11. Mobile State Continuity QA

- [ ] Desktop hover assumptions are not blindly copied into mobile.
- [ ] Tap feedback is clear and brief where action exists.
- [ ] Mobile focus, disabled, validation, loading, success, and error states remain legible.
- [ ] Sticky/fixed state behavior does not obstruct content or pressure conversion without source authority.
- [ ] Missing mobile state authority is recorded as **SAFE UNKNOWN**.

---

## 12. Taxonomy QA

Check for:

- [ ] hover inconsistency;
- [ ] CTA state drift;
- [ ] fake disabled state;
- [ ] misleading affordance;
- [ ] infinite loading ambiguity;
- [ ] validation overload;
- [ ] success-state celebration spam;
- [ ] error-state panic drift;
- [ ] focus invisibility;
- [ ] keyboard-state neglect;
- [ ] state mismatch across components;
- [ ] behavioral fragmentation;
- [ ] mobile-state inconsistency;
- [ ] dashboard-state contamination;
- [ ] decorative loading systems.

Record matches using [`ui-state-taxonomy.md`](../../projects/mars-website-factory/ui-state-taxonomy.md).

---

## 13. Escalation Boundary

Stop and escalate when a state consistency fix would:

- invent a form validation model, loading system, disclosure state, sticky state, modal state, custom focus system, or accessibility behavior beyond scope;
- change CTA meaning, availability, order, pressure, or conversion tone;
- make static proof/content interactive without source authority;
- remove behavior that may be intentionally chartered but lacks documentation;
- add decorative success, error, loading, or validation drama to satisfy “modern,” “premium,” or “more interactive” language;
- require accessibility-sensitive behavior not covered by current scope;
- alter mobile state semantics without mobile source or HITL.

Use **PARTIAL — state consistency** or **SAFE UNKNOWN** rather than silent state invention.

---

## 14. REPORT Block

Use this block when state consistency QA is in scope:

```text
STATE CONSISTENCY FINDINGS — <section or block_id> — <source ref>

State authority: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Active source:
- States observed:
- States inferred:
- Missing / unknown states:
- SAFE UNKNOWN resolver:

Hover / focus integrity: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Hover hierarchy:
- Focus visibility:
- Keyboard-state risk:
- Mobile equivalent:

CTA state consistency: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Primary CTA states:
- Secondary / tertiary states:
- Disabled / loading ambiguity:
- Mobile CTA state:

Validation / success / error: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Validation timing and guidance:
- Success restraint:
- Error recovery and severity:

Loading-state seriousness: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Loading scope:
- Real waiting / process authority:
- Infinite or decorative loading risk:

UI state taxonomy:
- Patterns:
- Severity:
- Contamination risk:

Disposition:
- Freeze impact:
- Action: no action | restrained | normalized | removed | deferred | HITL required | accessibility review required
- Evidence:
```

---

## 15. Not Claimed

- No automatic state detection.
- No runtime UI state engine.
- No automated accessibility AI or full WCAG audit.
- No universal hover, focus, validation, loading, success, or error aesthetics.
- No autonomous state redesign.

Defer to Website Factory state governance, source authority, project implementation packs, HITL decisions, foundation QA, and accessibility scope where applicable.

---

## 16. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge state consistency checklist; adds `STATE CONSISTENCY FINDINGS`. |
