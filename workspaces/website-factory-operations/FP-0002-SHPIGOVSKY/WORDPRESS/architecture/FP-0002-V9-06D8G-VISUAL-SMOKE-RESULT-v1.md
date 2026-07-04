# FP-0002 V9-06D8G Visual Smoke Result v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d8g-post-seed-qa/visual-smoke-result.json`  
**Screenshots:** `validation/v9-06d8g-post-seed-qa/screenshots/`

---

## Summary

| Metric | Result |
|---|---|
| Required desktop shots | 7 |
| Required mobile shots | 4 |
| Optional mobile shots | 3 |
| Captured (required) | 11/11 |
| Global shell intact | yes |
| Pixel-perfect claim | **no** |
| Overall | **PASS** |

---

## Screenshot manifest (required)

| File | Route | Viewport | Captured | Notes |
|---|---|---|---:|---|
| desktop-home-after-d8g.png | `/` | desktop | yes | Shell + home sections |
| desktop-services-hub-after-d8g.png | `/uslugi/` | desktop | yes | Hub cards + FAQ |
| desktop-service-zavisimosti-after-d8g.png | `/uslugi/zavisimosti/` | desktop | yes | Subdivision stack |
| desktop-service-alkogol-after-d8g.png | `/uslugi/.../alkogol/` | desktop | yes | Alcohol special |
| desktop-service-psych-after-d8g.png | `/uslugi/psihicheskoe-zdorovie/` | desktop | yes | Parent service |
| desktop-service-rpp-after-d8g.png | `/uslugi/rasstroystva-pischevogo-povedeniya/` | desktop | yes | Parent service |
| desktop-contacts-after-d8g.png | `/kontakty/` | desktop | yes | Seeded intro + locations |
| mobile-home-after-d8g.png | `/` | mobile | yes | No catastrophic overflow |
| mobile-services-hub-after-d8g.png | `/uslugi/` | mobile | yes | Nav/shell OK |
| mobile-service-alkogol-after-d8g.png | alcohol route | mobile | yes | Service stack OK |
| mobile-contacts-after-d8g.png | `/kontakty/` | mobile | yes | Contacts body visible |

---

## Known visual gaps (expected)

- Map embed / static map PNG — operator/media deferred
- Messenger/social links — empty placeholders
- Hero/gallery media — attachment IDs not uploaded
- FAQ answers — technical MVP placeholder copy

---

## Result

**PASS** — suitable for operator visual review; not a pixel-perfect certification.
