# Responsive foundation system v2

**Status:** documented implementation architecture. **Not** layout engine or auto-responsive AI.

**Default posture:** **mobile-first** (`min-width` media queries) per [frontend-production-rules-v0.md](../frontend-production-rules-v0.md).

**RU commercial landings:** QA widths and typography checks are **authoritative** in [ru-landing-qa-preset-v1.md](../ru-landing-qa-preset-v1.md). Generic viewport lists (e.g. 375 / 768 / 1280) in handoff or visual regression docs are **supplementary** only.

---

## 1. Canonical breakpoints

| Token | Width | Typical use |
|-------|-------|-------------|
| `$bp-sm` | 576px | Large phones, tight grids |
| `$bp-md` | 768px | Tablet, nav collapse |
| `$bp-lg` | 1024px | Desktop layout unlock |
| `$bp-xl` | 1280px | Wide marketing layouts |

**Handoff wins:** if `responsive_rules` lists different values, map them in `_breakpoints.scss` once — do not scatter literals.

```scss
@mixin up($bp) {
  @media (min-width: $bp) { @content; }
}
@mixin down($bp) {
  @media (max-width: $bp - 1px) { @content; }
}
```

Use `up()` by default; `down()` only for exceptions (document in REPORT).

---

## 2. Responsive intent hierarchy

When rules conflict, resolve in this order:

1. **Accessibility / no horizontal scroll** (hard)
2. **Handoff `responsive_rules`**
3. **Conversion survival** (primary CTA visible without excessive scroll)
4. **Composition preservation** (hierarchy, grouping)
5. **Pixel fidelity to static comp** (soft)

Forge responsive *intent* governance is Tier 3 QA vocabulary — this file is **how to implement**.

---

## 3. Section collapse logic

| Pattern | Mobile behavior | Implementation |
|---------|-----------------|----------------|
| **Stack** | Columns → single column | flex/grid `flex-direction: column` at base |
| **Hide non-critical** | Secondary visual hidden | `.is-mobile-hidden` utility — not `display:none` on primary CTA |
| **Reorder** | Proof after CTA if needed | `order` in flex; duplicate content forbidden |
| **Carousel fallback** | Multi-card → scroll snap | one `data-module="slider"` — see js lifecycle |
| **Accordion disclosure** | Long lists | `data-module="accordion"` |

**Collapse taxonomy (QA names):** compression, collision, orphan CTA, whitespace desert — map findings to [responsive-collapse-taxonomy.md](../responsive-collapse-taxonomy.md) when reporting.

---

## 4. Spacing adaptation

- Section gaps: drop one cadence tier below `$bp-md` unless boundary is XL (footer/major CTA).
- Internal component gaps: use spacing scale step −1 on mobile, not arbitrary `%`.
- Sticky/fixed elements: reserve `padding-bottom` on `body` or main when sticky CTA present — avoid content hidden under bar.

---

## 5. Typography scaling

**Direction:** slightly smaller headings on mobile, **never** below 16px on inputs (iOS zoom prevention).

```scss
// Example stepped scale — project defines exact sizes in implementation pack
$font-h1-mobile: clamp(1.75rem, 5vw, 2.5rem);
$font-body: 1rem;
$line-height-body: calc(#{$font-body} + 4px); // rhythm preference
```

Prefer `clamp()` for hero H1; use discrete steps for nav/footer.

---

## 6. Container behavior

- Full-bleed sections: outer wrapper 100vw max with overflow guard; inner `.container` holds content.
- Media backgrounds: `object-fit: cover`; min-height with `aspect-ratio` fallback to prevent CLS.
- Tables: wrap in `.table-scroll` with `overflow-x: auto` — page does not scroll horizontally.

---

## 7. Anti-overflow rules

| Check | Rule |
|-------|------|
| Images | `max-width: 100%`, `height: auto` on content images |
| Long words / unbroken strings | `overflow-wrap: break-word` on **long body copy only** (paragraphs, FAQ bodies, legal) — **not** on body default, headings, or UI. **Forbidden:** `anywhere`, `break-all`, global body `break-word`. See [russian-no-word-splitting-typography-v1.md](../russian-no-word-splitting-typography-v1.md). |
| Flex children | `min-width: 0` on flex items with text |
| Fixed widths | Forbidden on `.container` children unless handoff |
| 100vw hacks | Account for scrollbar — prefer `100%` on section wrapper |

---

## 8. Section replacement survivability

Before freeze after replace:

- **RU commercial:** run [ru-landing-qa-preset-v1.md](../ru-landing-qa-preset-v1.md) widths (supersedes generic two-width spot-check for typography).
- 375px and 768px (supplementary): no horizontal scroll on touched page
- Primary CTA still visible or one scroll max (judgment — document)
- Adjacent section gaps unchanged unless charter says so
- `data-*` hooks still match JS module selectors

Hot-swap: run `destroy()` → replace partial → `initSection()` per [js-lifecycle-system-v2.md](js-lifecycle-system-v2.md).

---

## 9. Desktop-first clarification

Allowed only when handoff explicitly requires desktop-first authoring. Still ship **one** breakpoint file; implement mobile as default overrides at base layer, not an afterthought max-width patch stack.

*Wave 2 — responsive foundation.*
