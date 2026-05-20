# Implementation reliability checklist — MARS Forge

**Status:** Forge overlay checklist for **human-supervised** implementation reliability QA.  
**Not:** automated CSS linting, runtime frontend enforcement, autonomous repair, universal frontend architecture, or replacement for foundation QA.

**Website Factory layers:**

- [Implementation Reliability Governance](../../projects/mars-website-factory/implementation-reliability-governance.md)
- [Frontend Stability Model](../../projects/mars-website-factory/frontend-stability-model.md)
- [Implementation Drift Taxonomy](../../projects/mars-website-factory/implementation-drift-taxonomy.md)

Use this checklist during Forge QA / pre-freeze when CSS scope, include graph, breakpoints, overrides, regression impact, rebuild behavior, JS ownership, or maintainability are in scope.

---

## 1. Authority and Scope

- [ ] Active design version, source screen, `block_id`, and implementation pack are identified.
- [ ] Files touched are scoped to the requested slice or justified by explicit shared ownership.
- [ ] No generated/build artifact is hand-edited as source.
- [ ] Existing implementation ownership is identified or marked **SAFE UNKNOWN**.
- [ ] Reliability review is coordinated with source interpretation, visual reconciliation, composition awareness, responsive intent, and design token QA where relevant.
- [ ] No local fix silently becomes a global rule, token change, include change, or framework decision.

---

## 2. Implementation Stability QA

- [ ] Structure, styles, behavior, breakpoints, and includes can be explained from visible source.
- [ ] Current visual correctness does not depend on hidden globals, neighbor sections, import-order luck, or manual generated-file edits.
- [ ] Future scoped changes have a visible owner and expected blast radius.
- [ ] Any known fragility is recorded as **IMPLEMENTATION RELIABILITY FINDINGS**.
- [ ] Freeze disposition is stable, stable with monitored risk, partial, SAFE UNKNOWN, or escalation required.

---

## 3. Deterministic Rebuild QA

- [ ] Build/source path is documented for the project or marked **SAFE UNKNOWN**.
- [ ] Source edits are sufficient to reproduce the intended output.
- [ ] No undocumented manual post-build patch is required.
- [ ] Include/import order dependencies are intentional and readable.
- [ ] Generated files are not treated as canonical source.
- [ ] Rebuild behavior is not claimed deterministic when scripts, paths, or generated output ownership are unknown.

---

## 4. Scoped-Fix QA

- [ ] Fix is applied at the smallest honest owner: block, component, token, breakpoint, include, or JS module.
- [ ] Shared file edits include a visible reason and regression impact.
- [ ] Local fix does not require repeated exceptions in unrelated scopes.
- [ ] Patch layering is flagged when multiple fixes accumulate around the same issue.
- [ ] Structural escalation is surfaced when local tuning cannot resolve the underlying owner problem.

---

## 5. Override Governance QA

- [ ] Overrides are source-anchored, HITL-approved, or explicitly documented as risk.
- [ ] Override scope is bounded to intended section/component/state/breakpoint.
- [ ] `!important`, long selector chains, broad utility overrides, and forced layout hacks are absent or justified.
- [ ] Override rationale explains why the normal token/component/selector path is insufficient.
- [ ] Override does not leak into unrelated sections, frozen blocks, states, or breakpoints.

---

## 6. Include-Chain Integrity QA

- [ ] Partial/include ownership is visible for the slice.
- [ ] Include graph remains unchanged unless documented as approved structure work.
- [ ] Import order does not hide local behavior or create neighbor-section dependency.
- [ ] Shared partial edits are checked against known consumers.
- [ ] Include-chain contamination is recorded when a block depends on unrelated section order or styles.

---

## 7. Breakpoint Integrity QA

- [ ] Breakpoint rules remain readable and consistent with responsive intent.
- [ ] Mobile/tablet behavior is not a second implementation hidden behind overrides.
- [ ] No emergency breakpoint hack introduces regression at another width.
- [ ] Breakpoint-specific values preserve hierarchy, cadence, grouping, CTA pressure, visual weight, and operational readability or defer to `RESPONSIVE INTENT FINDINGS`.
- [ ] Breakpoint explosion is flagged when local exceptions multiply.

---

## 8. Regression Survivability QA

- [ ] Previously frozen or validated sections likely affected by the change are identified.
- [ ] Global selectors, tokens, shared components, includes, utilities, and JS hooks receive impact notes when touched.
- [ ] Adjacent-section and shared-consumer spot checks are planned or marked **SAFE UNKNOWN**.
- [ ] Regression cascade is flagged when one fix triggers repeated secondary fixes.
- [ ] Freeze impact is recorded when reliability risk remains.

---

## 9. Implementation Readability QA

- [ ] Source naming, selector scope, class ownership, and file placement are understandable.
- [ ] Future operator can identify what owns structure, style, behavior, breakpoint rules, and overrides.
- [ ] Comments are used only when they clarify non-obvious reliability decisions.
- [ ] Duplicate implementations are identified or justified.
- [ ] Emergency patches are named as temporary, normalized, or accepted with monitored risk.

---

## 10. Drift Taxonomy QA

Check for:

- [ ] CSS spaghetti;
- [ ] include-chain contamination;
- [ ] breakpoint explosion;
- [ ] unsafe local override;
- [ ] regression cascade;
- [ ] implementation duplication;
- [ ] hidden coupling;
- [ ] rebuild unpredictability;
- [ ] patch layering;
- [ ] selector escalation;
- [ ] utility abuse;
- [ ] implementation erosion;
- [ ] scope leakage;
- [ ] emergency-fix accumulation.

Record matches using [implementation-drift-taxonomy.md](../../projects/mars-website-factory/implementation-drift-taxonomy.md).

---

## 11. Escalation Boundary

Stop or escalate when a reliability fix would:

- redesign the page or invent frontend architecture outside source authority;
- create a global CSS/token/component rule to solve one local issue without HITL;
- restructure includes, wrappers, or DOM boundaries without approved structure change;
- hide unresolved source interpretation, visual, responsive, or composition uncertainty behind CSS force;
- require generated-file editing or undocumented build steps;
- produce a stable-looking result with unknown regression impact.

Use **PARTIAL — implementation reliability**, **SAFE UNKNOWN**, or **HITL required** rather than silent patch layering.

---

## 12. REPORT Block

Use this block when implementation reliability QA is in scope:

```text
IMPLEMENTATION RELIABILITY FINDINGS — <section or block_id> — <source ref>

Implementation stability: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Stable / fragile read:
- Ownership clarity:
- Coupling boundaries:
- Structural escalation drift:

Deterministic rebuild QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Source/build path:
- Generated artifact boundary:
- Manual step risk:

Scoped-fix QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Fix owner:
- Shared impact:
- Patch layering risk:

Override governance QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Overrides:
- Scope / rationale:
- Leakage risk:

Breakpoint integrity QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Breakpoint model:
- Emergency hacks:
- Width regression risk:

Include-chain QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Include/partial ownership:
- Import/order dependency:
- Contamination risk:

Regression survivability QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Frozen / adjacent sections:
- Shared consumers:
- Spot-check result or SAFE UNKNOWN:

Implementation readability QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Selector/source readability:
- Duplicate implementation risk:
- Future operator clarity:

Implementation drift taxonomy:
- Patterns:
- Severity:
- Freeze impact:

Disposition:
- Action: no action | scoped fix | normalized | deferred | monitored risk | HITL required | structure escalation
- Evidence:
```

---

## 13. Not Claimed

- No automatic implementation reliability detection.
- No CSS linter, style architecture mandate, or framework prescription.
- No autonomous repair or self-healing frontend.
- No redesign of Triumph or any project.
- No runtime enforcement or hidden governance engine.

Defer to Website Factory governance layers, project implementation packs, foundation QA, and HITL decisions where scoped.

---

## 14. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge implementation reliability checklist; adds `IMPLEMENTATION RELIABILITY FINDINGS`. |
