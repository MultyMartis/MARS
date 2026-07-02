# FP-0002 — Responsive Rules Reality Map v1

**Audit ID:** `home-style-baseline-01`  
**Authority:** `f5a9ecd7`  
**Date:** 2026-06-26

**Viewport bands used in this audit:**

| Band | Range |
|------|-------|
| Desktop | ≥1025px |
| Tablet | ≤1024px |
| Mobile | ≤930px (hero type) + ≤1024 layout |
| Small mobile | ≤560px, ≤390px |

---

## Pattern matrix

| Pattern | Desktop | ≤1024 | Mobile | Small mobile | Reusable rule |
| ------- | ------- | ----- | ------ | ------------ | ------------- |
| **Container gutters** | 30px `--pad-x` | 15px `--pad-gap-line` | 15px | 15px | **Yes** — global |
| **Section padding Y** | 50px `--pad-y` | 50px | 50px | 50px | **Yes** — no mobile reduction |
| **Header** | Full top + nav row | Mobile bar; off-canvas menu | Messengers in bar | Messengers hidden @560; phone 14px @390 | Site-wide |
| **Hero home** | 70vh + max-height cascade | height auto; min 320px | Title 40px @930 | same | Use `hero--inner` for services |
| **Recovery intro cards** | 3-col grid | 1-col | 1-col | 1-col | **Yes** |
| **Founder quote** | 2-col grid | 1-col stack | variant-b mask vertical | same | Variant param |
| **Treatment accordion** | Full service leaders | Hide dotted leader | same | same | **Yes** |
| **Gallery slider** | 3.5 slides Swiper | 2.15–3.15 slides | partial peek | partial peek | Swiper breakpoints in JS |
| **Feature grid** | 3-col | 1-col | 1-col | 1-col | **Yes** |
| **Staff / landscape photos** | 448px / 584px height | 240px / 220px | scaled | scaled | Proportional scale formula |
| **Recovery life stages** | flex row, 3 stages | **no stack rule** | horizontal flex persists | overflow risk | **Verify on Services** |
| **Reviews slider** | 2.5 slides | 1.35–2.5 slides | peek | peek | JS breakpoints |
| **Requirements CTA band** | 3-col grid | 1-col stack | phone 24px | same | **Yes** |
| **Program directions** | row card + image | unchanged flex | may wrap tight | same | Partial reuse |
| **Comfort gallery** | 3-col; wide span 2 | 1-col | 1-col | 1-col | **Proven on Services** |
| **Videos grid** | 2-col | 1-col | 1-col | 1-col | If block used |
| **Specialists slider** | 3.5 slides | 1.35–2.5 | peek | peek | JS |
| **Articles grid** | 3-col | 1-col | 1-col | 1-col | Blog pattern |
| **FAQ accordion** | full width items | same | same | same | **Proven on Services** |
| **Final form band** | 2-col copy+form | 1-col stack | 1-col | 1-col | **Proven on Services** |
| **Modal** | centered dialog | padding 10px; 1-col fields | same | same | Site-wide |
| **Off-canvas** | disabled @1025+ | slide panel | same | same | Site-wide |

---

## Slider activation summary (from `main.js`)

| Hook | Desktop slides | 768 | 320 |
|------|----------------|-----|-----|
| `data-gallery-slider` | 3.5 / gap 30 | 3.15 / 20 | 2.15 / 10 |
| `data-reviews-slider` | 2.5 / 30 | 2.5 / 20 | 1.35 / 10 |
| `data-specialists-slider` | 3.5 / 30 | 2.5 / 20 | 1.35 / 10 |

**Reusable rule:** partial slide widths on mobile for peek; shared pagination styling; `watchOverflow: true`.

---

## Horizontal overflow protection

- `overflow-x: clip` on `html`, `body`, `main`, `.intro-section`
- `.home-gallery`, `.home-reviews`, `.home-specialists` — `overflow: hidden` on section or slider
- Swiper `overflow: visible` on some sliders — peek intentional

---

## Hide/show behavior

| Element | Hidden when |
|---------|-------------|
| Desktop header top/bottom | ≤1024 |
| Mobile header bar | ≥1025 |
| Service dotted leader | ≤1024 |
| Mobile messengers | ≤560 |
| Accordion panels | `[hidden]` until expanded |

---

## Typography scaling (responsive)

Only **hero** and **CTA phone** scale significantly across breakpoints. Section H2s remain 36px at all widths (operator choice).

---

## Exceptions requiring planning audit

1. `.home-recovery-life__stages` — no `@1024` column/stack override  
2. `@media (max-width: 767px)` — empty placeholder block  
3. Program direction row — image + text may need mobile stack on Services if copy longer

---

*End of responsive rules reality map v1.*
