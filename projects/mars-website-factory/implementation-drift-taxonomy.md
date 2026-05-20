# MARS Website Factory — Implementation Drift Taxonomy

**Status:** **documented** — named implementation drift vocabulary for human-supervised frontend reliability review.  
**Not:** automated detector, CSS linter, runtime enforcement, universal architecture rulebook, or autonomous refactor tool.

**Parent layer:** [implementation-reliability-governance.md](implementation-reliability-governance.md).  
**Stability model:** [frontend-stability-model.md](frontend-stability-model.md).  
**Forge checklist:** [`../../agents/mars-forge/implementation-reliability-checklist.md`](../../agents/mars-forge/implementation-reliability-checklist.md).

---

## 1. Purpose

This taxonomy names implementation drift patterns that make frontend source structurally fragile even when the visible UI appears correct.

Use it in **IMPLEMENTATION RELIABILITY FINDINGS** to avoid vague labels such as “messy CSS,” “probably fine,” or “works for now.”

---

## 2. Drift Patterns

| Drift pattern | Definition | Typical symptom | Governance response |
|---------------|------------|-----------------|---------------------|
| **CSS spaghetti** | Styles are entangled across selectors, utilities, globals, and block files without clear ownership. | Changing one visual rule unexpectedly alters several areas. | Re-scope to owner, document coupling, or escalate. |
| **Include-chain contamination** | Include/import order or neighbor partials silently affect a section. | A block looks correct only when loaded after another partial. | Identify include owner; record SAFE UNKNOWN if ownership is unclear. |
| **Breakpoint explosion** | Responsive rules multiply into many local exceptions without a readable breakpoint model. | Mobile/tablet rules become longer and less explainable than base layout. | Run responsive intent + reliability QA; normalize or escalate. |
| **Unsafe local override** | A one-off exception changes broader behavior or bypasses source-owned styles. | Global selector, utility, or `!important` fixes one object and affects others. | Bound scope, justify, or reject. |
| **Regression cascade** | One fix triggers additional regressions in adjacent or shared areas. | A small change requires repeated follow-up fixes. | Identify hidden coupling and impacted frozen sections. |
| **Implementation duplication** | Same component, section logic, or behavior is implemented in multiple divergent places. | Two similar blocks require separate fixes for the same issue. | Choose canonical owner or record HITL / SAFE UNKNOWN. |
| **Hidden coupling** | Dependencies between files, selectors, tokens, hooks, or includes are not visible from the local code. | Local edit behavior depends on unrelated file state. | Surface dependency and add regression note. |
| **Rebuild unpredictability** | Same source does not reliably produce expected output without manual or hidden steps. | Generated files are hand-edited or post-build changes are required. | Stop deterministic rebuild claim; document resolver. |
| **Patch layering** | New fixes are stacked on top of prior patches without resolving ownership. | Comments, overrides, or utilities accumulate around the same issue. | Normalize, escalate structure, or record monitored risk. |
| **Selector escalation** | Specificity grows to defeat existing rules rather than fix scope. | Long selectors, repeated parent chains, broad `!important` usage. | Re-establish source owner and scope. |
| **Utility abuse** | Utility classes or helper overrides replace maintainable component/block styles. | Markup becomes a pile of local visual corrections. | Move repeated intent to scoped style or token when justified. |
| **Implementation erosion** | Source clarity declines over time through small ungoverned edits. | Future operator cannot explain why rules exist. | Add reliability findings and normalize before freeze when material. |
| **Scope leakage** | Local rules affect unrelated components, sections, states, or breakpoints. | Frozen neighbors change after a scoped fix. | Tighten selector/owner and run regression spot-check. |
| **Emergency-fix accumulation** | Urgent patches remain as permanent architecture without documentation. | Temporary hacks become the default maintenance path. | Mark entropy, create follow-up or HITL decision. |

---

## 3. Related Drift Families

### 3.1 CSS and Selector Drift

Includes:

- CSS spaghetti;
- selector escalation;
- utility abuse;
- unsafe local override;
- patch layering;
- CSS survivalism.

Primary risk: styling becomes a fight against the current cascade rather than an expression of source-owned implementation.

### 3.2 Structure and Include Drift

Includes:

- include-chain contamination;
- hidden coupling;
- implementation duplication;
- scope leakage;
- structural escalation drift.

Primary risk: the visible section depends on boundaries, order, or duplicated ownership that future operators cannot safely change.

### 3.3 Responsive and Breakpoint Drift

Includes:

- breakpoint explosion;
- emergency breakpoint hacks;
- mobile second implementation;
- breakpoint-only patch layering;
- regression cascade across widths.

Primary risk: responsive behavior survives current spot widths but cannot absorb future content, adjacent edits, or source changes.

### 3.4 Rebuild and Regression Drift

Includes:

- rebuild unpredictability;
- generated artifact hand edits;
- hidden manual post-build steps;
- regression cascade;
- emergency-fix accumulation.

Primary risk: build pass and visible pass become non-repeatable or too fragile to trust.

---

## 4. Severity Guidance

| Severity | Meaning |
|----------|---------|
| **P0 — stop / HITL** | Drift blocks deterministic rebuild, changes canonical source, risks broad regression, or requires structural change without authority. |
| **P1 — freeze blocker** | Drift materially affects stability, breakpoint integrity, include ownership, or regression survivability for the slice. |
| **P2 — partial allowed** | Drift is known and bounded; freeze may proceed only with explicit **PARTIAL — implementation reliability** and follow-up. |
| **P3 — monitored risk** | Minor readability or maintainability risk; record if it may matter in future adjacent edits. |

Severity is based on stability impact, not visual loudness. A visually tiny selector leak can be P1 if it affects frozen sections.

---

## 5. Anti-Pattern Phrases

Use these phrases carefully as named drift, not as insults:

- **patch-on-patch fixes**
- **random utility overrides**
- **selector escalation wars**
- **emergency breakpoint hacks**
- **duplicate implementations**
- **hidden dependencies**
- **CSS survivalism**
- **accidental global impact**
- **implementation panic fixes**
- **“works now” engineering**

If one of these phrases appears in a review, include the affected scope, evidence, severity, and recommended resolver.

---

## 6. Taxonomy Use in REPORT

When implementation reliability is in scope, report:

- drift pattern name;
- affected file/scope/block/breakpoint when known;
- regression risk;
- severity;
- whether the fix is scoped, deferred, normalized, or escalated;
- SAFE UNKNOWN if ownership or impact cannot be established.

Example:

```text
Implementation drift taxonomy:
- Pattern: Include-chain contamination
- Scope: <block_id / include / partial>
- Severity: P1
- Risk: local section depends on neighbor partial order
- Disposition: PARTIAL — implementation reliability; HITL/include owner needed
```

---

## 7. Boundaries

This taxonomy does not require one CSS architecture, component model, build system, or framework. It names reliability risk regardless of stack.

It also does not authorize autonomous refactors. A finding may recommend a scoped fix, monitored risk, SAFE UNKNOWN, or HITL escalation, but structural rewrites remain governed by project source authority and Website Factory workflow.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Implementation Drift Taxonomy — CSS spaghetti, include-chain contamination, breakpoint explosion, unsafe local overrides, regression cascade, duplication, hidden coupling, rebuild unpredictability, patch layering, selector escalation, utility abuse, implementation erosion, scope leakage, and emergency-fix accumulation. |
