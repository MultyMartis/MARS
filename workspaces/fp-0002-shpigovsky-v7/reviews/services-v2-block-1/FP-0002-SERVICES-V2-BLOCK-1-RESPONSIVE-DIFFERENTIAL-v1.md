# FP-0002 — Services V2 Block 1 Responsive Differential v1

**Date:** 2026-06-26  
**Preview:** `http://127.0.0.1:4174/uslugi-v2.html`

## Breakpoint review

| Width | Hero | Breadcrumbs | Subnav | Overflow |
| ----- | ---- | ----------- | ------ | -------- |
| 320 | Derived ≤390 rules | Wrap | Horizontal scroll | 0 |
| 390 | Stack + 30px title | 11px / wrap | Scroll row | 0 (`sw=373`) |
| 430 | ≤1024 mobile hero | Wrap | Scroll | 0 |
| 768 | ≤1024 mobile hero | Wrap | Scroll | 0 |
| 1024 | Mobile rules at boundary | Wrap | Scroll | 0 |
| 1025 | Desktop hero 628 aspect | 14px | Row wrap | 0 |
| 1280 | Desktop layout | Row | Row | 0 |
| 1398 | Reference desktop | Row | Row | 0 |
| 1440 | Desktop layout | Row | Row | 0 |
| 1920 | Centered 1400 shell | Row | Row | 0 |

## Visual differential

| Element | Figma/PNG target | V2 | V1 | V2 verdict |
| ------- | ---------------- | -- | -- | ---------- |
| Hero shell | 1400×628 rounded banner | Match | Match | PASS |
| Hero content alignment | Left overlay column | Left stack, no frosted panel | Centered frosted panel | PASS (structural fix) |
| Eyebrow | Uppercase white | Implemented | Present | PASS |
| H1 | Лечение и профилактика | Match | Match | PASS |
| Supporting copy | 582px column | Match | Match | PASS |
| CTA | In-banner 334px | In copy block | Split column | PASS |
| Breadcrumbs | Главная / Услуги лечения и профилактики | Implemented | Missing | PASS |
| Submenu | 6 tags | 6 links | Missing | PASS |
| Mobile order | Hero → crumbs → tags (semantic DOM) | Hero → crumbs → tags | Hero only | PASS |

## Aggregate

```text
Hero structural parity: IMPROVED VS V1
Breadcrumb parity: RESTORED
Subnav parity: RESTORED
Mobile parity: PASS (horizontal subnav scroll)
Horizontal overflow: 0 @ 390
```
