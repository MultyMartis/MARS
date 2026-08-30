# Screen 01 — Hero — Desktop metadata v1

**Factory Project:** FP-0003 — OVERSEO  
**Screen:** SCREEN-01-HERO  
**Version:** v1  
**Export:** `../exports/SCREEN-01-HERO-DESKTOP-v1.png`  

---

## Canvas

| Field | Value |
|-------|-------|
| Width | **1920px** |
| Height | **820px** (content-driven; no arbitrary crop) |
| Method | HTML/CSS design render → Puppeteer PNG export |

---

## Container geometry

| Field | Value |
|-------|-------|
| Container max-width | **1300px** |
| Outer free space at 1920 | **310px** each side |
| Inner horizontal padding | **50px** each side |
| Effective content width | **1200px** |

---

## Grid

| Region | Layout |
|--------|--------|
| Header | Flexbox — logo / nav / actions inside container |
| Hero body | CSS Grid **7fr + 5fr**, gap **50px** |
| Full-bleed | Background wash + blurred accent orbs on `.hero__bleed` |

---

## Vertical rhythm

| Region | Padding |
|--------|---------|
| Header top | **28px** (maps to scale via local composition) |
| Hero body top (below header) | **40px** |
| Hero section bottom | **70px** |

Section owns rhythm — not child margins.

---

## Typography roles (this screen)

| Element | Font | Size / line |
|---------|------|-------------|
| H1 (hero title) | Literata | 52px / 56px |
| Lead | Onest | 20px / 24px |
| Header / CTA labels | Onest uppercase | 12px / 16px |
| Logo word | Literata | 22px |

---

## Color (major)

| Role | Hex |
|------|-----|
| Hero wash | `#EEF6F2` |
| Violet accent | `#8B7EC8` |
| Turquoise accent | `#5BAFA0` |
| Mint accent | `#A8D5C5` |
| Text | `#1E2A28` |
| Muted text | `#4A5C58` |

---

## Radius

| Use | Value |
|-----|-------|
| Primary (`--radius-main`) | **24px** |
| Logo mark | **8px** (local; not a second system radius) |

---

## Layers

| Layer | Owner |
|-------|-------|
| Gradient wash, accent blurs | Full-bleed `.hero__bleed` |
| Header, copy, CTAs, visual frame | `.container` (1300px) |
| Organic SVG visual | Container-aligned column; **PLACEHOLDER VISUAL — REQUIRES FINAL ASSET** |

---

## Responsive intent (desktop master → future)

| Element | Intent ≤1024 |
|---------|----------------|
| Header | Logo + burger; actions collapse to menu drawer or stacked compact row |
| Hero grid | Single column — title → lead → visual → CTAs |
| Visual | Full container width; aspect ratio preserved |
| Decorative blurs | Reduced opacity / simplified |
| Title | Step down to ~36–40px range using type scale |

---

## Content locks

| Item | Status |
|------|--------|
| Logo mark + Overseo word | FINAL reference reproduction |
| Hero title | LOCKED (Olga wording) |
| Hero lead | LOCKED (Olga wording) |
| Header actions semantics | LOCKED — Меню / Оставить заявку / Задать вопрос |

---

*Metadata v1 — supports future Gulp implementation pack. Not operator approval.*
