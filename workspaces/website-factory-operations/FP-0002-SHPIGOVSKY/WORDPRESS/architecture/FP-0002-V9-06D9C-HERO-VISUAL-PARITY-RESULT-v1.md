# FP-0002 V9-06D9-C — Hero Visual Parity Result

**Date:** 2026-07-05

## Before

- Static: photo hero with `hero__media`, 620px height, panel + CTA
- Runtime: panel/CTA only; no `hero__media`; light/empty background

## After

- Runtime: `hero__media` + theme hero PNG (HTTP 200)
- Panel, title, tagline, CTA visible over photo
- Hero height unchanged (620px CSS box)

## Remaining non-hero deltas (out of D9-C scope)

- CTA label: runtime uses D8-A option text ("Заказать звонок") vs static "Записаться на консультацию"
- Other Home sections still missing (D9-D scope)

## Verdict

**Hero media parity:** PASS  
**Hero visual parity:** PASS (media layer restored)

**Evidence:** `validation/v9-06d9c-home-hero-parity-repair/visual-result.json`
