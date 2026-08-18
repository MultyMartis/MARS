# Forge WordPress — Design system foundation v1

**ID:** FW-S-34  
**Status:** ACTIVE — CANONICAL DEFAULT (architecture only)  
**Date:** 2026-08-18  
**Not:** brand values, clinical palette, or a claim that FP-0002 pixels are universal.

**Rule:** PROJECT BRAND VALUES MAY CHANGE. TOKEN **ARCHITECTURE** SHOULD NOT.

Fill values in [DESIGN-SYSTEM-MAP](../templates/FORGE-WORDPRESS-DESIGN-SYSTEM-MAP-TEMPLATE-v1.md). This standard defines **what must exist**.

---

## 1. Token layers

| Layer | Exists as | Brand-specific? |
|-------|-----------|-----------------|
| Typography tokens | `--font-body`, `--font-heading`, `--fs-*`, `--lh-*`, `--fw-*` | values yes; names no |
| Spacing scale | `--space-1` … `--space-8` (or project equivalent named scale) | values yes |
| Container widths | `--container`, `--container-narrow` | values yes |
| Breakpoints | named, owned (see §4) | values mostly shared |
| Radius | `--radius-s/m/l` or none if design is square | optional |
| Border | `--border-w`, `--border-c` | values yes |
| Elevation | `--shadow-*` **only if used** | optional |
| Semantic colors | `--color-bg`, `--color-fg`, `--color-accent`, `--color-danger`, `--color-muted` | values yes |
| Interactive states | hover / focus-visible / active / disabled tokens or documented equivalents | yes |

Do not encode brand names into token identifiers (`--shpigovsky-blue`). Use role names.

Website Factory CSS Variable First / Universal Style Scale laws apply when the frontend originated in Factory. WP theme CSS must **preserve** those tokens, not invent a second anonymous scale.

---

## 2. Component primitives (architecture)

Every custom service/company site maps these primitives before page art:

| Primitive | Token / contract |
|-----------|------------------|
| Buttons | one base + explicit variants; loading/disabled |
| Links | in-content vs nav vs button-styled (do not mix semantics) |
| Inputs | text, email, tel, textarea, select; error/success |
| Cards | one card family; variants listed in component inventory |
| Sections | vertical rhythm via spacing scale; not magic numbers per page |
| Headings | H1–H3 (H4+ only if design has them) tied to `--fs-*` |
| Content typography | body, lead, caption, lists, quotes |

---

## 3. Interactive states

Document default / hover / `:focus-visible` / active / disabled / current.

Unify hover and keyboard focus **visually enough** that keyboard users are not invisible. Do not use `outline: none` without a replacement.

---

## 4. Breakpoint ownership

Named breakpoints live in **one** place (CSS custom properties, SCSS map, or documented CSS file header).

Typical WP Forge set (adjust to design, do not invent extras):

| Name | Typical use |
|------|-------------|
| wide-desktop | extra margin / large type if design has it |
| desktop | default layout ≥ ~1025px unless design says otherwise |
| tablet | stacked grids, condensed nav |
| narrow-mobile | single column, larger tap targets |
| chrome/viewport | `100dvh` / `visualViewport` — not a screenshot width |

**Avoid** page-specific arbitrary breakpoints unless a component inventory row proves the need.

Physical viewport and browser chrome are first-class: iOS URL bar, Android nav, `100vh` vs `100dvh`. See [FRONTEND-INTERACTION-OWNERSHIP](FORGE-WORDPRESS-FRONTEND-INTERACTION-OWNERSHIP-STANDARD-v1.md).

---

## 5. Motion

Motion tokens (`--duration-*`, `--ease-*`) if any decorative motion exists. Reduced-motion fallback is mandatory — [ACCESSIBILITY-BASELINE](FORGE-WORDPRESS-ACCESSIBILITY-BASELINE-v1.md).

---

## 6. What this is not

- Not a Figma library claim  
- Not permission to restyle a PIXEL_PERFECT design  
- Not extracted CSS from FP-0002  

---

*FW-S-34 v1.*
