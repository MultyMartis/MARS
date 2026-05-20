# MARS Website Factory — Token Semantic Layer Model

**Status:** **documented** — Website Factory token hierarchy model for human-supervised frontend governance.  
**Not:** universal token architecture, runtime token engine, mandatory JSON schema, style dictionary standard, or autonomous design-system compiler.

**Parent governance:** [design-token-intelligence-governance.md](design-token-intelligence-governance.md).  
**Companion taxonomy:** [token-drift-taxonomy.md](token-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/design-token-checklist.md`](../../agents/mars-forge/design-token-checklist.md).

---

## 1. Purpose

This model gives Website Factory operators a shared vocabulary for reading token layers without enforcing one implementation format.

The model answers:

- what kind of token is being used;
- which layer owns its meaning;
- whether aliasing preserves intent;
- whether inheritance is readable;
- whether an override is controlled;
- whether escalation to wider scope is justified.

---

## 2. Canonical Layers

| Layer | Role | Example meaning |
|-------|------|-----------------|
| **Primitive tokens** | Raw values or base scales with little semantic meaning beyond measurement or palette identity. | `color.black`, `space.24`, `radius.8`, `shadow.sm` |
| **Semantic tokens** | Named roles that explain usage across the system. | `color.text.primary`, `color.surface.elevated`, `space.section.relaxed` |
| **Contextual tokens** | Tokens scoped to a component, section, page role, or project context. | `hero.cta.background`, `proof.card.gap`, `footer.surface` |
| **Behavioral tokens** | Tokens that express interaction behavior or feedback intensity. | `cta.hover.background`, `link.focus.ring`, `card.interactive.shadow` |
| **Responsive tokens** | Tokens that adapt intent across breakpoint states. | `space.section.mobile`, `grid.proof.tablet.gap`, `type.hero.mobile` |
| **State tokens** | Tokens for UI state integrity: hover, focus, active, disabled, loading, validation, success, error. | `form.error.border`, `button.disabled.text`, `input.focus.border` |
| **Intent tokens** | High-level role tokens that capture authored design intent when the role is stable and reviewable. | `intent.operational.surface`, `intent.trust.proof`, `intent.cta.primary` |

These layers may be implemented differently per project. The governance requirement is that the meaning remains readable and auditable.

---

## 3. Alias Relationships

Aliasing is valid when a higher layer maps to a lower layer while preserving semantic role:

```text
semantic token -> primitive token
contextual token -> semantic token
behavioral token -> semantic/state token
responsive token -> semantic/contextual token
intent token -> semantic/contextual token
```

Good aliasing:

- keeps role names stable even if primitive values change;
- avoids reusing one semantic token for incompatible roles;
- makes state and responsive changes traceable;
- allows controlled local context without hiding value ownership.

Risky aliasing:

- creates semantic-looking names for raw values with no role;
- maps multiple conflicting meanings to the same alias;
- chains aliases so deeply that humans cannot audit intent;
- uses intent names to justify local taste.

---

## 4. Inheritance Discipline

Token inheritance should follow the smallest honest authority:

1. **Primitive layer** provides base values.
2. **Semantic layer** gives stable roles.
3. **Contextual layer** narrows the role to a component, section, or page context.
4. **Behavioral/state layer** adapts role for interaction and feedback.
5. **Responsive layer** adapts role across viewport intent.
6. **Intent layer** documents high-level purpose only when the purpose is stable enough to audit.

Inheritance is drift when:

- globals override screen-local source authority;
- a local section inherits token behavior from a previous section by accident;
- state tokens inherit color/opacity that makes enabled, disabled, secondary, and muted roles ambiguous;
- responsive tokens inherit desktop scale and only compress, breaking hierarchy or cadence.

---

## 5. Override Governance

Overrides are governed by scope, reason, and continuity.

| Override type | Acceptable when | Drift when |
|---------------|-----------------|------------|
| **Local value override** | One source-chartered exception is needed and broader token change would damage other contexts. | Used to nudge taste without source authority. |
| **Contextual token override** | Component or section role needs a stable local semantic token. | Duplicates an existing semantic token under a new name. |
| **Responsive override** | Breakpoint needs a different value to preserve intent. | Mobile simply shrinks or stacks until hierarchy collapses. |
| **State override** | Interaction or feedback state needs a clearer role. | Hover/focus/disabled/loading styles fragment by component. |
| **Intent override** | A high-level role is explicitly chartered by source or HITL. | Intent token becomes a vague bucket for unrelated values. |

Every material override should answer:

- What intent does the override preserve?
- Why does the existing token fail this context?
- Why is the override scoped here?
- What prevents it from leaking into other contexts?
- Does it affect responsive, state, interaction, accessibility, or visual reconciliation QA?

---

## 6. Escalation Boundaries

Escalate a value to a broader token only when:

- reuse is real, not speculative;
- semantic role is stable across at least one known family of contexts;
- naming is readable;
- responsive and state behavior can remain consistent;
- the token reduces meaningful ambiguity rather than only reducing repetition.

Do not escalate when:

- one section needs a one-off correction;
- the value is repeated accidentally;
- the name would be vague or value-based at semantic layer;
- the token would hide a design conflict;
- the project lacks authority for global design-system meaning.

---

## 7. Semantic Stability

Semantic stability means token meaning remains trustworthy even when values evolve.

Stable:

- `color.text.primary` remains primary readable text;
- `space.section.dense` remains a dense but readable section cadence;
- `button.primary.hover` remains hover feedback for primary CTAs;
- `surface.proof.card` remains a proof/card context and does not become a generic card style.

Unstable:

- `primary` alternates between brand color, CTA color, heading color, and active state;
- `muted` means disabled in one place and secondary text in another;
- `surface.elevated` sometimes means shadow, sometimes border, sometimes white card;
- `mobile` means smaller value without preserving hierarchy or tap clarity.

---

## 8. Layer QA Questions

Use these during Forge review:

- Which token layer owns this decision?
- Is the token name semantic enough for its layer?
- Is the alias relationship readable?
- Is the override source-anchored or HITL-approved?
- Does responsive adaptation preserve the same intent?
- Do state tokens preserve behavior and accessibility integrity?
- Has a local token escalated beyond its authority?
- Would a future operator understand when not to use this token?

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Token source lacks layer distinction | Cannot classify primitive, semantic, contextual, state, or responsive ownership. |
| Alias chain is unreadable | Cannot verify intent preservation. |
| Override reason is missing | Cannot distinguish controlled deviation from drift. |
| Responsive token mapping is absent | Cannot prove breakpoint continuity. |
| State token mapping is absent | Cannot prove hover/focus/disabled/loading/validation consistency. |
| Escalation rationale is missing | Cannot justify global or shared token scope. |

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial token semantic layer model — primitive, semantic, contextual, behavioral, responsive, state, and intent token layers; alias, inheritance, override, escalation, and stability governance. |
