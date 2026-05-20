# V2 — Typography rules (implementation pack v0)

**Scope:** Rules **visible and required** for Triumph V2 landing per **`design/v2/`** + shared design system alignment. Detail: [triumph-manipulator-design-system.md](../../../design-system/triumph-manipulator-design-system.md).

## Source discipline

- **`design/v2/`** = pixel + hierarchy truth for **what appears** (sizes/weights as seen).
- **Design system** = token law (Roboto/Montserrat stack, px-only sizes, line-height, etc.) when mock and code must agree structurally.
- **`design/v1/`** / **`shared-assets/`** — not typography authority.

---

## Fonts

- **Body / UI:** `Roboto`, `Arial`, sans-serif  
- **Display / headings / button labels:** `Montserrat`, `Arial`, sans-serif  

---

## Hard constraints (agents)

| Rule | Detail |
|------|--------|
| `font-size` | **Only `px`** — no `rem` / `em` / `%` / `clamp()` for font-size |
| `letter-spacing` | **Always `0`** everywhere |
| Line-height | Body/list/lead: `calc(font-size + 4px)`; headings & buttons: `1` |
| Border radius | **`0`** on UI (buttons, fields, cards, framed media) |

---

## Token scale (reference)

Use design-system steps (e.g. caption 12, body 16, lead 18, subtitle 22, h3 24, h2 32, h1 48 desktop with step-down ≤1024). **Final per-section sizes** must still **match** active `NN.png` after implementation.

---

## Anti-drift

- Do not substitute fonts or “approximate” weights to “match vibe.”
- Do not add tracking or transform to headings for emphasis.
