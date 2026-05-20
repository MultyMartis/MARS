# MARS Website Factory - Layout Shell Governance

**Status:** **documented** - Website Factory layout shell governance and human-supervised shell ownership methodology only.  
**Not:** layout engine, navigation runtime, framework mandate, automatic header generator, or universal site shell architecture.

**Core principle:** **HEADER != HERO**.  
The persistent shell and the hero system may cohabit the first viewport, but they do not share ownership by default.

**Related layers:** [first-screen-decomposition-model.md](first-screen-decomposition-model.md), [background-ownership-governance.md](background-ownership-governance.md), [responsive-intent-governance.md](responsive-intent-governance.md), [implementation-reliability-governance.md](implementation-reliability-governance.md), [compositional-structure-awareness.md](compositional-structure-awareness.md).  
**Forge findings category:** `LAYOUT SHELL FINDINGS`.

---

## 1. Purpose

Layout Shell Governance separates persistent layout and navigation architecture from page-local hero composition.

It covers:

- layout shell;
- persistent navigation layer;
- shell continuity;
- shell survivability;
- navigation architecture;
- shell-to-section relationship;
- shell readability;
- shell ownership.

---

## 2. Canonical Definition

| Concept | Meaning |
|---------|---------|
| **Layout shell** | Persistent structural wrapper that governs page frame, navigation placement, global background behavior, and repeated page-level regions. |
| **Header layer** | The visible navigation / brand / menu region inside the shell. |
| **Hero system** | Page-local opening content system: headline, support copy, primary CTA, proof, media, and hero-local atmosphere. |
| **Shell continuity** | The shell remains understandable and consistent across sections and breakpoints. |
| **Shell-to-section relationship** | Sections live inside or beneath the shell without stealing global navigation ownership. |

**Rule:** Header may visually overlap or sit on top of the hero, but it is not the hero. Hero changes must not silently rewrite shell architecture.

---

## 3. Ownership Boundaries

| Decision | Default owner |
|----------|---------------|
| Brand mark, nav links, mobile menu trigger | Header / navigation layer |
| First-screen H1, offer, hero CTA, hero proof | Hero layer |
| Persistent page padding, max-width, nav z-index | Layout shell |
| Hero-local media, focal art, headline atmosphere | Hero system |
| Global shell background or page chrome | Layout shell or background governance |
| Mobile menu overlay behavior | Mobile navigation layer, not hero |

---

## 4. Canonical Rules

- Keep header, hero, mobile navigation, background, and conversion environment separate in naming and review.
- Do not solve hero spacing by making header semantics page-local unless the design explicitly says so.
- Do not let background art decide navigation architecture.
- Preserve shell readability: a future operator should know what owns navigation, overlay, z-index, and page frame.
- Report shell findings when first-screen work touches persistent navigation, shell background, or mobile menu ownership.

---

## 5. Anti-Patterns

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Header/hero merge** | Persistent navigation becomes page-local hero implementation. |
| **Hero owns nav** | Hero styling controls nav behavior, z-index, or mobile menu without authority. |
| **Shell opacity** | Operators cannot tell what owns page frame, navigation, or background. |
| **Background-driven header** | Nav architecture changes because one hero background needs it. |
| **Mobile menu as hero detail** | Mobile navigation is implemented as a local hero effect. |
| **Shellless first screen** | First viewport is built as one visual blob with no ownership map. |

---

## 6. Drift Patterns

- **Header/hero confusion** - header and hero are treated as one implementation unit.
- **Shell continuity drift** - navigation or page frame changes per section without governance.
- **Shell readability erosion** - layout structure works visually but ownership is unreadable.
- **Navigation architecture drift** - menu behavior is decided by local first-screen pressure.

---

## 7. Triumph V3 Lesson

Triumph V3 showed that “first screen” is too broad as an implementation object. Header/navigation, hero content, atmosphere, and conversion pressure must be decomposed before production work.

The lesson is architectural governance: **HEADER != HERO**. It is not a fixed implementation pattern.

---

## 8. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Header appears visually integrated into hero | Cannot prove whether it is shell-owned or hero-local. |
| Mobile nav source is absent | Cannot determine overlay, trigger, focus, or ownership behavior. |
| Background crosses header and hero | Requires background ownership mapping. |
| Existing code couples nav and hero styles | Cannot prove safe scoped changes. |
| Source does not define sticky/fixed behavior | Do not invent shell behavior. |

**Action:** map shell/header/hero/mobile ownership before styling or responsive closure.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial Layout Shell Governance layer; formalizes HEADER != HERO from Triumph V3 lessons. |
