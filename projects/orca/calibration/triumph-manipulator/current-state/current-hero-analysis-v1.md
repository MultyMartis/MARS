# Current Hero Analysis v1 — zakaz v5

**Partial (canonical v6):** `workspaces/triumph-manipulator-landing-v6/src/partials/sections/v5-ppc/zakaz/screen-01-hero.html`
**Styles:** `workspaces/triumph-manipulator-landing-v6/src/scss/sections/_v5-hero-extensions.scss`
**Wrapper:** `index.html` → `.first-screen` with `hero-bg-final.jpg` + multi-layer overlay

## Layout model

```text
.first-screen (bg img + overlay)
  └── .hero.hero--v5
        └── .hero__shell
              ├── .hero__main [grid 1.06fr | 420px]
              │     ├── .hero__content (H1, lead, specs)
              │     └── .hero__aside (inline form)
              └── .hero__lower
                    ├── .hero-proof--v5 (4 items)
                    └── .hero__cargo-block (6 cards)
```

## Copy (locked in repo)

| Element | Text |
|---------|------|
| H1 | Аренда манипулятора **в Краснодаре** (span on geo) |
| Lead | Перевозка … манипулятором **5 т**. Подача … Без посредников. |
| Specs | Борт 5 т · Стрела 3 т · Вылет 14 м · Кузов 6.2×2.2 · Мин. заказ 2 ч |
| Form H2 | Рассчитать стоимость |
| Proof strip | От 30 мин · Мин. заказ · Опытные водители · Для юрлиц — безнал |

## Visual / hierarchy observations

| Factor | Assessment |
|--------|------------|
| **Focus hierarchy** | H1 → lead → specs → form title — clear top-down |
| **CTA visibility** | Form in right column on desktop; primary button inside form |
| **Image competition** | Machine photo is **background**, not competing with H1 (productive) |
| **Semantic load** | 5 specs + 4 proof + 6 cargo = **high** but layered in lower band |
| **Trust in hero** | No 4.9★ line in hero — reviews deferred to § trust block |

## SCSS intent (evidence)

- `hero--v5` uses `clamp()` typography, `text-wrap: balance`, red text-shadow on geo span
- PPC pages: separated `first-screen__bg-media` + gradient overlay (not legacy pseudo-bg only)
- Mobile (`max-width: 760px`): stronger overlay, stacked grid (form below content)

## Comparison anchors

| Version | Role |
|---------|------|
| v4 `screen-01-hero.html` (index) | **Anti-pattern** — fleet, fake price, 5–10 т |
| v4 `zakaz/screen-01-hero.html` | Intermediate — form + proof; had `hero__notice` |
| v5 `zakaz/screen-01-hero.html` | Current — lower band cargo + proof; no notice |

## Calibration note

Hero is **production-mature** for capability clarity and CTA placement; **trust strip semantics** diverge from ORCA blueprint (see drift docs).
