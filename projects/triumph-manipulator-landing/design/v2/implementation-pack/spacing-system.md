# V2 — Spacing system (implementation pack v0)

**Scope:** Section rhythm, container behavior, and spacing scale for V2 implementation. Aligns with [triumph-manipulator-design-system.md](../../../design-system/triumph-manipulator-design-system.md) §12–15; **pixel confirmation** against **`design/v2/`** per screen.

## Source discipline

- **`design/v2/`** = authority when **visual spacing** conflicts with generic tokens.
- Design system = default **scale** when mock is ambiguous.

---

## Base unit

- Vertical rhythm: **8px** multiples for padding/margins tied to sections and large gaps.

---

## Container

| Token / behavior | Desktop | ≤1024 | ≤768 |
|------------------|---------|-------|------|
| Max content width | **1540px** (centered) | same | same |
| Horizontal padding | **72px** | **32px** | **16px** |

Full-bleed bands (e.g. dark strips) still align inner content to the container.

---

## Section rhythm (defaults)

| Zone | Desktop | Tablet (≤1024) | Mobile (≤768) |
|------|---------|----------------|----------------|
| Section `padding-block` | 96px | 72px | 56px |
| Large gap between major sub-blocks | 64px | 48px | 40px |

Adjust **only** when **`NN.png`** clearly shows different breathing room — then **document** deviation in QA notes.

---

## In-section spacing

- Section title block → content: **32px** desktop, **24px** mobile.
- Paragraph stack: **16px** between blocks.
- Form fields: **16px** vertical rhythm (field + error).

---

## Anti-drift

- Do not collapse section padding to “look tighter” without mock alignment.
- Do not mix ad-hoc `margin-top` on wrappers that break the **8px** ladder across breakpoints.
