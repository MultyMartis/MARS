# MARS Website Factory — Frontend Stability Model

**Status:** **documented** — conceptual model for human-supervised frontend implementation stability.  
**Not:** universal frontend architecture, CSS framework prescription, runtime stability engine, autonomous refactor system, or automated maintainability score.

**Parent layer:** [implementation-reliability-governance.md](implementation-reliability-governance.md).  
**Companion taxonomy:** [implementation-drift-taxonomy.md](implementation-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/implementation-reliability-checklist.md`](../../agents/mars-forge/implementation-reliability-checklist.md).

---

## 1. Purpose

The Frontend Stability Model gives Website Factory operators a vocabulary for deciding whether a frontend implementation is stable enough to freeze, maintain, and evolve.

The model treats visual correctness, semantic correctness, responsive survival, and build success as necessary but insufficient. A stable implementation must also remain readable, scoped, predictable, and regression-survivable.

---

## 2. Stable Implementation

A **stable implementation** has these properties:

| Property | Meaning |
|----------|---------|
| **Deterministic structure** | DOM, includes, partials, imports, and build order are understandable and repeatable. |
| **Scoped modification** | A change can be made in the smallest honest owner without surprising unrelated sections. |
| **Controlled override strategy** | Exceptions are named, justified, bounded, and not treated as silent new defaults. |
| **Regression isolation** | Frozen or previously validated sections are protected from accidental selector, token, include, or breakpoint impact. |
| **Breakpoint survivability** | Responsive rules preserve intent and remain readable across future edits. |
| **Implementation readability** | Future operators can explain structure, styling, hooks, and overrides without relying on undocumented memory. |
| **Coupling boundaries** | Dependencies between components, globals, utilities, tokens, includes, and JS hooks are visible. |
| **Scoped evolution** | Broader changes are escalated when local fixes would multiply or hide structural problems. |

Stable does not mean static. It means the implementation can evolve without losing explainability and control.

---

## 3. Fragile Implementation

A **fragile implementation** may look correct in the current viewport or pass a build, but depends on unstable conditions:

- CSS specificity or utility overrides fight the source structure.
- Breakpoint rules repair desktop assumptions instead of expressing responsive intent.
- Include order or import order silently determines visual behavior.
- Local fixes leak into shared components or frozen sections.
- Duplicate implementations diverge behind similar markup or naming.
- JS hooks depend on implicit lifecycle timing, double-bind prevention by luck, or neighbor markup.
- Operators cannot tell which file owns a visible behavior.

Fragility is a freeze risk because it turns future scoped work into regression discovery.

---

## 4. Deterministic Structure

Structure is deterministic when:

- source files, partials, includes, imports, and generated outputs have a known path;
- rebuild behavior does not depend on manual generated-file edits;
- include order is intentional rather than accidental;
- shared styles and block styles have readable ownership;
- JS hook initialization is idempotent and scoped.

Structure is non-deterministic when:

- a section only works after undocumented manual post-build edits;
- changing import order unexpectedly changes unrelated sections;
- generated files are treated as source;
- hidden globals compensate for missing block styles;
- the same visible component has multiple competing source definitions.

---

## 5. Scoped Modification

A scoped modification changes the smallest honest owner:

| Scope | Healthy use | Drift risk |
|-------|-------------|------------|
| **Block / section partial** | Local layout, spacing, surfaces, component variants | Local selector leaks into neighbors |
| **Component partial** | Shared component behavior with documented reuse | Accidental broad change to unrelated pages |
| **Token / variable** | Stable semantic value or project-wide rule | Global value changed to fix one section |
| **Breakpoint block** | Viewport-specific adaptation preserving intent | Emergency mobile implementation hidden in overrides |
| **JS module / hook** | One owner for behavior and lifecycle | Double-bind, race, or shared hook contamination |
| **Include / layout shell** | Approved structural boundary change | Silent regrouping or include-chain contamination |

If a local change requires repeated exceptions in other scopes, it may indicate structural escalation drift.

---

## 6. Controlled Override Strategy

Controlled overrides are allowed when they are:

- anchored to active source, implementation pack, HITL decision, or documented bugfix need;
- scoped to block/component/breakpoint/state rather than broad globals;
- named in a way that explains why normal tokens or components are insufficient;
- reversible or later normalizable;
- included in **IMPLEMENTATION RELIABILITY FINDINGS** when material.

Unsafe overrides usually have one of these shapes:

- `!important` escalation without owner rationale;
- utility class piles replacing source-owned styles;
- breakpoint-only patches with no relation to responsive intent;
- broad selector overrides to fix one local object;
- duplicated CSS copied from a neighbor section to avoid understanding ownership.

---

## 7. Regression Isolation

Regression isolation means the blast radius of a change is visible before freeze.

Operators should ask:

- Does this edit touch a global selector, token, mixin, import, include, JS hook, or shared component?
- Which frozen sections could change because of this edit?
- Is the behavior local by selector scope, import path, `block_id`, component ownership, or runtime hook?
- Does a breakpoint fix alter desktop/tablet/mobile behavior beyond the target slice?
- Is a regression spot-check required for adjacent or shared consumers?

Regression survivability is not a promise of zero defects. It is a discipline of visible impact and bounded change.

---

## 8. Breakpoint Survivability

Breakpoint survivability means responsive code can survive future edits without collapsing into patch layering.

Healthy breakpoint behavior:

- rules follow an intentional breakpoint model;
- layout changes preserve hierarchy, cadence, grouping, CTA pressure, and visual weight;
- viewport-specific overrides are named by role or scope;
- mobile/tablet rules do not duplicate entire desktop sections;
- changes at one width do not create unexplained regressions at another.

Fragile breakpoint behavior:

- emergency hacks accumulate at narrow widths;
- selector specificity differs wildly between breakpoints;
- mobile is a second implementation with hidden assumptions;
- breakpoint order determines behavior in ways the operator cannot explain;
- local fixes require repeated offsets, negative margins, or forced widths.

---

## 9. Coupling Boundaries

Coupling is not always bad. Hidden coupling is the risk.

Visible coupling:

- documented shared components;
- intentional token families;
- named include dependencies;
- explicit JS hook ownership;
- known global foundation rules.

Hidden coupling:

- a block depends on previous-section CSS;
- a local utility silently changes shared component behavior;
- a JS module assumes markup from another include;
- a token is changed globally for a one-section visual correction;
- a breakpoint rule works only because import order currently masks another rule.

The stability requirement is to keep coupling visible enough to audit.

---

## 10. Structural Escalation Drift

**Structural escalation drift** happens when a local implementation problem repeatedly asks for broader fixes without an explicit governance decision.

Signals:

- one spacing fix requires selector changes in multiple files;
- a breakpoint fix requires changing DOM order, shared wrappers, and utility rules;
- a visual issue cannot be solved without moving include boundaries;
- a local override becomes a token change, then a global reset, then a component rewrite;
- fixes keep expanding because the true owner is unknown.

Decision:

- If local tuning is enough, keep the change scoped.
- If the owner is unknown, record **SAFE UNKNOWN**.
- If structure must change, escalate as a documented structure change or HITL decision.
- If a temporary patch is accepted, record the entropy and freeze impact.

---

## 11. Stability Disposition

Use these labels in implementation reliability review:

| Disposition | Meaning |
|-------------|---------|
| **Stable** | Scoped, readable, deterministic, and regression impact is bounded. |
| **Stable with monitored risk** | A known exception exists but is documented, scoped, and acceptable for freeze. |
| **Fragile** | Current output may work, but coupling, overrides, breakpoints, or readability create material risk. |
| **Partial — implementation reliability** | Some stability dimensions are unresolved but explicitly deferred. |
| **SAFE UNKNOWN** | Ownership, build behavior, coupling, or impact cannot be established from current evidence. |
| **Escalation required** | Local fix would hide or expand structural drift; HITL or structure decision needed. |

---

## 12. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Frontend Stability Model — stable vs fragile implementation, deterministic structure, scoped modification, override strategy, regression isolation, breakpoint survivability, coupling boundaries, and structural escalation drift. |
