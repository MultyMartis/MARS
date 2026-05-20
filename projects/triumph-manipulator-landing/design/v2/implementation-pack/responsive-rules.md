# V2 — Responsive rules (implementation pack v0)

**Scope:** Breakpoints, stacking, overflow for V2. Tokens from [triumph-manipulator-design-system.md](../../../design-system/triumph-manipulator-design-system.md) §12–14; behavior must be checked against **`design/v2/`** (desktop-first exports — infer stack discipline, do not invent new layouts).

## Source discipline

- **`design/v2/`** = what must remain **recognizable** at each width.
- **`design/v1/`** — not responsive reference.

---

## Breakpoints (implementation ladder)

| Name | Range | Notes |
|------|-------|--------|
| Desktop | **≥1200px** | 12-col grid, default gaps |
| Laptop | **1024–1199px** | 12 cols; gap may reduce (e.g. 24px) |
| Tablet | **768–1023px** | 8 or 12 cols — keep touch targets per design system |
| Mobile | **≤767px** | Primary content **single column**; sidebars stack below |
| Ultra-small | **≤360px** | Shrink **padding first**; font steps in **px** only if needed |

Primary CSS cutoffs referenced in repo: **1024px** and **768px** (container + grid).

---

## Stack behavior

- Hero: form column **stacks under** or **below** main offer per implementation pass — must not clip or hide CTAs; **no horizontal scroll** for main content.
- Multi-column cases (`03`): **three** columns → stacked cards on narrow; preserve **reading order** (LTR, case 1 → 2 → 3).
- Eight-card grid (`04`): collapses to fewer columns then **single column**; card **order 01–08** preserved.
- Matrix (`05`): two-column desktop → **stack columns**; row semantics preserved top-to-bottom.
- Footer (`07`): three columns → stacked blocks; legal bar remains **readable** (wrap, no overflow-hidden truncation of required legal text).

---

## Overflow discipline

- **No** `overflow-x: auto` on page shell to “fix” wide sections — fix grid/gaps.
- Images: `max-width: 100%`, height auto unless mock requires fixed aspect.
- Long URLs / INN in footer: allow wrap or controlled breaks — do not push layout past viewport.

---

## Typography responsive

- Step heading sizes down at **1024 / 768** in **px** only (see typography pack + design system §8).

---

## Anti-drift

- Do not introduce breakpoints absent from project patterns without operator approval.
- Do not treat **stub** HTML as proof of final mobile layout — validate after real content.
