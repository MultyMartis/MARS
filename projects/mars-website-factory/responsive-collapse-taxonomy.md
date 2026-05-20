# MARS Website Factory — Responsive Collapse Taxonomy

**Status:** **documented** — drift vocabulary for human-supervised responsive QA.  
**Not:** automated detector, breakpoint scoring model, responsive engine, or universal design truth.

**Purpose:** name recurring responsive drift patterns where a viewport implementation may mechanically survive while losing visual, semantic, or compositional intent.

**Parent layer:** [responsive-intent-governance.md](responsive-intent-governance.md).  
**Mobile method:** [mobile-composition-preservation.md](mobile-composition-preservation.md).  
**Forge checklist:** [`../../agents/mars-forge/responsive-intent-checklist.md`](../../agents/mars-forge/responsive-intent-checklist.md).

---

## 1. How to Use

Use this taxonomy in **RESPONSIVE INTENT FINDINGS** when reviewing mobile, tablet, or narrow desktop states.

Each finding should include:

- source / viewport reviewed;
- observed responsive behavior;
- drift type from this taxonomy;
- severity: `PASS`, `PARTIAL`, `FAIL`, or `SAFE UNKNOWN`;
- disposition: tune, defer, escalate structure, or require HITL.

Taxonomy labels do not prove failure by themselves. They give operators shared language for a human read.

---

## 2. Drift Patterns

| Drift pattern | Definition | Typical symptom |
|---------------|------------|-----------------|
| **Accordion collapse drift** | Disclosure mechanics hide or reorder important hierarchy without preserving the section argument. | Primary proof or conditions disappear behind low-signal tabs/accordions. |
| **Stack flattening** | Multi-role composition collapses into equal vertical blocks. | Hero, proof, CTA, and support cards all read with similar weight. |
| **Hierarchy inversion** | A secondary object becomes more prominent than the primary object after collapse. | Trust badge, image, price, or secondary CTA appears before / louder than the main claim. |
| **CTA overweight on mobile** | CTA treatment becomes more aggressive than source intent. | Huge sticky button, repeated full-width CTAs, or high-contrast action after every small block. |
| **Mobile dashboard effect** | Marketing / narrative content becomes compact app UI. | Dense card grids, tight controls, small gaps, and panel logic dominate the narrow viewport. |
| **Endless-stack fatigue** | Long vertical sequence lacks resets, grouping, or cadence changes. | User scrolls through repeated cards with no narrative breath. |
| **Desktop-to-mobile contamination** | Desktop grid assumptions dictate mobile behavior without re-reading mobile attention. | Column order, equal card sizing, or wide line logic copied into narrow screens. |
| **Compressed trust drift** | Trust/proof loses credibility or relationship to claims because it is squeezed or displaced. | Reviews, logos, guarantees, or metrics become tiny, crowded, or disconnected. |
| **Over-centered mobile drift** | Everything is centered until hierarchy, operational seriousness, and scan path flatten. | Dense service/spec sections read like generic landing blocks. |
| **Tap-zone suffocation** | Usability survives visually but interactive spacing is cramped. | Buttons, links, form fields, and controls compete in narrow vertical space. |
| **Mobile cadence collapse** | Mobile spacing compresses narrative beats into a continuous feed. | Section boundaries, CTA isolation, and dense/light transitions disappear. |

---

## 3. Additional Named Risks

| Risk | Meaning |
|------|---------|
| **Composition collapse** | Visual clusters lose grouping or dominance after reflow. |
| **CTA collapse** | Primary / secondary / helper CTA relationships become unclear. |
| **Visual flattening** | Surface, type, media, and CTA weights equalize. |
| **Stack contamination** | One stack inherits spacing or component treatment from another unchartered stack. |
| **Mobile overload** | Too many dense objects compete within one mobile beat. |
| **Survivability-only implementation** | Breakpoints pass overflow checks but fail intent preservation. |

---

## 4. Anti-Patterns

Forbidden responsive drift vocabulary:

| Anti-pattern | Why it is forbidden drift |
|--------------|---------------------------|
| **“Just stack everything”** | Treats responsive work as mechanics, not intent preservation. |
| **Giant mobile cards** | Inflates every object until hierarchy and scan speed collapse. |
| **Dashboard mobile feel** | Imports app density into narrative / commercial pages. |
| **Over-centered layouts** | Removes purposeful alignment and operational reading path. |
| **Tap-zone collapse** | Sacrifices usability and confidence to compactness. |
| **Hierarchy inversion** | Lets supporting material overpower primary meaning. |
| **Mobile CTA screaming** | Uses mobile width to over-pressure conversion. |
| **Endless vertical fatigue** | Creates unbroken scroll with no cadence resets. |
| **Excessive mobile compression** | Reduces spacing until grouping and readability fail. |
| **Survivability-only implementation** | Declares success because content fits, not because intent survives. |

---

## 5. Severity Guidance

| Severity | Use when |
|----------|----------|
| **PASS** | Responsive state preserves hierarchy, grouping, cadence, CTA pacing, and readability. |
| **PARTIAL** | Mechanics pass, but one or more intent dimensions are unresolved or deferred. |
| **FAIL** | Responsive state changes section meaning, dominance, CTA pressure, grouping, or readability beyond approved intent. |
| **SAFE UNKNOWN** | Source authority is missing or conflicting; fidelity cannot be established. |

**Rule:** Do not upgrade `PARTIAL` to `PASS` because there is no overflow. Mechanical survival is only one input.

---

## 6. Triumph V2 Lessons Captured

Triumph V2 provides reusable taxonomy examples:

- Dense service/equipment zones risk **mobile dashboard effect** and **endless-stack fatigue**.
- Price / offer / CTA clusters risk **composition collapse** and **CTA collapse** if separated too far.
- Proof and trust zones risk **compressed trust drift** when logos, ratings, and reviews shrink into low-authority decoration.
- Hero and CTA sections risk **CTA overweight on mobile** when full-width action treatments become visually louder than the approved source.
- Global desktop or foundation assumptions can create **desktop-to-mobile contamination** when mobile hierarchy is not separately read.

These are lessons for Website Factory responsive governance, not claims that every Triumph section has every drift type.

---

## 7. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial responsive collapse taxonomy for intent-preserving responsive QA. |
