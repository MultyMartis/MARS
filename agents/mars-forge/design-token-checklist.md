# Design token checklist — MARS Forge

**Status:** Forge overlay checklist for **human-supervised** design token intelligence QA.  
**Not:** automated token linting, runtime token enforcement, universal token architecture, autonomous design-system AI, or style dictionary requirement.

**Website Factory layers:**

- [Design Token Intelligence Governance](../../projects/mars-website-factory/design-token-intelligence-governance.md)
- [Token Semantic Layer Model](../../projects/mars-website-factory/token-semantic-layer-model.md)
- [Token Drift Taxonomy](../../projects/mars-website-factory/token-drift-taxonomy.md)
- [RU landing QA preset](../../projects/mars-website-factory/ru-landing-qa-preset-v1.md) — when responsive/token QA on **Russian commercial** landings

Use this checklist during Forge QA / pre-freeze when tokens, variables, theme values, local overrides, responsive values, state values, or design-system consistency are in scope.

---

## 1. Authority and Scope

- [ ] Active design version, source screen, and implementation pack are identified.
- [ ] Project token source is identified or marked **SAFE UNKNOWN**.
- [ ] Token decisions are checked against design system intent, visual reconciliation, cadence, responsive intent, interaction intent, and state consistency where relevant.
- [ ] Existing code tokens are checked against active source before being preserved.
- [ ] No archived mockup, previous section, framework default, SaaS template, or unrelated project token overrides the active source.
- [ ] Any token gap, contradiction, or missing authority is recorded as **SAFE UNKNOWN** instead of solved by silent global invention.

---

## 2. Semantic Token QA

- [ ] Token names express role, state, context, or intent at non-primitive layers.
- [ ] Raw value naming is confined to primitive or base-scale usage.
- [ ] Semantic aliases preserve meaning and do not overload one name across incompatible roles.
- [ ] Token hierarchy is readable enough for a future operator to audit.
- [ ] Token choices preserve semantic meaning, hierarchy stability, visual continuity, behavioral consistency, responsive integrity, and design-system trust.

---

## 3. Token Layer QA

- [ ] Primitive tokens are not treated as semantic authority.
- [ ] Semantic tokens map to stable roles.
- [ ] Contextual tokens are scoped to real component, section, page, or project context.
- [ ] Behavioral tokens match interaction meaning and CTA behavior consistency.
- [ ] Responsive tokens preserve intent across breakpoints.
- [ ] State tokens preserve hover/focus/active/disabled/loading/validation/success/error clarity.
- [ ] Intent tokens are used only when high-level role meaning is stable and reviewable.

---

## 4. Override Governance QA

- [ ] Local overrides are source-anchored, HITL-approved, or recorded as **SAFE UNKNOWN**.
- [ ] Override scope is the smallest honest scope.
- [ ] Override reason explains which intent the existing token fails to preserve.
- [ ] Override does not leak into unrelated sections, components, states, or breakpoints.
- [ ] Controlled local deviation is allowed when it preserves source intent better than global defaults.
- [ ] Random local overrides, utility nudging, and copy/paste exceptions are flagged.

---

## 5. Responsive Token QA

- [ ] Breakpoint token changes preserve hierarchy, cadence, composition, CTA pacing, visual weight, and operational readability.
- [ ] Mobile tokens are not just compressed desktop values when compression damages intent.
- [ ] Responsive spacing, type, radius, shadow, and surface tokens remain continuous by role.
- [ ] Breakpoint-token divergence is recorded when values survive but intent changes.
- [ ] Missing responsive token authority is recorded as **SAFE UNKNOWN**.

---

## 6. Behavioral and State Token QA

- [ ] CTA hover/focus/active/loading/disabled tokens stay consistent by CTA role.
- [ ] Focus tokens remain visible and accessibility-relevant.
- [ ] Disabled, muted, secondary, readonly, and loading tokens do not collapse into one ambiguous visual state.
- [ ] Validation, success, error, and warning tokens match feedback severity and recovery meaning.
- [ ] Behavioral-token mismatch is flagged when token naming implies behavior the component does not support.

---

## 7. Visual Token QA

- [ ] Color tokens match semantic role and do not hide visual-token mismatch.
- [ ] Spacing tokens support cadence and density rather than random margin replacement.
- [ ] Radius tokens follow role logic for section shells, cards, buttons, inputs, badges, and media.
- [ ] Shadow/elevation tokens have hierarchy or containment purpose; no shadow contamination or fake premium glow.
- [ ] Typography tokens preserve heading/body rhythm, hierarchy, and readability.
- [ ] Design-system illusion is flagged when token usage looks systematic but visual intent is inconsistent.

---

## 8. Drift Taxonomy QA

Check for:

- [ ] random token creation;
- [ ] semantic alias confusion;
- [ ] local override chaos;
- [ ] token inflation;
- [ ] spacing-token fragmentation;
- [ ] breakpoint-token divergence;
- [ ] radius drift;
- [ ] shadow contamination;
- [ ] visual-token mismatch;
- [ ] token spaghetti;
- [ ] semantic inconsistency;
- [ ] design-system illusion;
- [ ] override leakage;
- [ ] behavioral-token mismatch;
- [ ] design-system trust erosion.

Record matches using [token-drift-taxonomy.md](../../projects/mars-website-factory/token-drift-taxonomy.md).

---

## 9. Escalation Boundary

Stop and escalate when a token fix would:

- define a global token architecture without project authority;
- create or rename broad semantic tokens without HITL or implementation-pack support;
- replace a project design system by local preference;
- invent responsive or state token behavior absent from source;
- hide visual inconsistency behind semantic names;
- change design system tone, CTA pressure, state behavior, or accessibility-sensitive focus/feedback without authority;
- turn one local deviation into global scope.

Use **PARTIAL — design token intelligence** or **SAFE UNKNOWN** rather than silent token invention.

---

## 10. REPORT Block

Use this block when design token intelligence QA is in scope:

```text
DESIGN TOKEN FINDINGS — <section or block_id> — <source ref>

Token authority: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Active source:
- Token source / implementation pack:
- Token layers in scope:
- SAFE UNKNOWN resolver:

Semantic token QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Naming clarity:
- Alias relationships:
- Token hierarchy readability:
- Semantic pressure:

Token continuity QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Color / surface continuity:
- Spacing / cadence continuity:
- Radius / shadow continuity:
- Typography continuity:

Override governance QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Local overrides:
- Scope / rationale:
- Leakage risk:
- Controlled deviation:

Responsive token QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Breakpoint continuity:
- Mobile cadence / hierarchy:
- Responsive token drift:

Behavioral / state token QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- CTA states:
- Focus / disabled / loading:
- Validation / success / error:
- Behavioral-token mismatch:

Token drift taxonomy:
- Patterns:
- Severity:
- Design-system trust risk:

Disposition:
- Freeze impact:
- Action: no action | normalized | scoped override | deferred | HITL required | design-system review required
- Evidence:
```

---

## 11. Not Claimed

- No automatic token detection.
- No style-lint or runtime enforcement.
- No universal token hierarchy for every project.
- No autonomous design-system generation.
- No redesign of Triumph or any project by token methodology alone.

Defer to Website Factory governance layers, project implementation packs, visual reconciliation, design intent, cadence, responsive intent, interaction/state/accessibility checklists, and foundation QA where scoped.
