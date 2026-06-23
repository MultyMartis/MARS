# FP-0002 V6 LOWER HOME SIX CORRECTIONS REVIEW

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**Stable baseline tag:** `fp-0002-v6-full-home-operator-stable-01` (`9018827`)  
**Corrections commit:** pending operator review

## Stable source backup

| Field | Value |
|-------|-------|
| Release ID | `FP-0002-V6-FULL-HOME-OPERATOR-STABLE-01` |
| Archive | `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-FULL-HOME-OPERATOR-STABLE-01-SOURCE.zip` |
| SHA-256 | `c01b7e125f03607b935bc4f71fdd64b2b96e1db37d08179cca8ee419b29ce587` |
| Restore test | PASS |
| Tag on origin | VERIFIED |

## Operator source protection

Operator-authored uncommitted delta at freeze preserved in stable commit: `home-genotyping.html`, `home-rehabilitation-program.html`, `home-rehabilitation-requirements.html`, `style.scss`. No `git restore`, reset, or full-file replacement applied.

## Program direction Figma images

| Direction | Figma frame | Node | Hash | Asset | Dimensions |
|-----------|-------------|------|------|-------|------------|
| 01 Генотипирование | `1:1115` | `1:1123` | `4fa6e0b0…` | `program-genotyping.webp` | 1216×1632 |
| 02 Нейропсихология | `1:1115` | `1:1124` | `8571376f…` | `program-neuropsychology.webp` | 1632×1216 |
| 03 Психокоррекция | `1:1115` | `1:1125` | `6f28af81…` | `program-psychocorrection.webp` | 880×1184 |
| 04 Кинезиотерапия | `1:1115` | `1:1126` | `64992cc0…` | `program-kinesiotherapy.webp` | 880×1184 |

White margins: NONE observed on export.

## Comfort Figma gallery assets

Existing comfort room exports retained (`1:1195`–`1:1207`). Decorative logo tile from `1:1179 Frame 2` rendered to `comfort-gallery-logo-decor.webp` (383×360).

## Comfort Fancybox

| Field | Value |
|-------|-------|
| Version | `@fancyapps/ui` 5.0.36 |
| Source | local npm → `dist/assets/vendor/fancybox/` |
| CDN | NO |
| Group | `data-fancybox="home-comfort"` |
| Photo links | 9 |
| Captions | disabled |

## Decorative logo tile exclusion

Decorative item: `home-comfort__gallery-item_decor` — no `href`, no `data-fancybox`, `pointer-events: none`. Not included in Fancybox group.

## Two video demo cards

| Field | Value |
|-------|-------|
| Preview nodes | `1:4420`, `1:4421` (separate Figma image nodes; desktop section `1:1224` had only combined `1:1230`) |
| Assets | `video-preview-01.webp`, `video-preview-02.webp` |
| Fake URLs | 0 |
| Iframes | 0 |
| Mode | DEMO — `aria-disabled="true"` play buttons, `preventDefault` retained |

## Specialists Swiper

| Field | Value |
|-------|-------|
| Hook | `data-specialists-slider` |
| Desktop slides | 3.5 |
| Tablet slides | 2.5 |
| Mobile slides | 1.35 |
| Instances | 1 |

## FAQ separate visual system

Removed `home-treatment-prevention__*` visual classes from FAQ. Independent classes: `home-faq__list`, `home-faq__item`, `home-faq__question`, `home-faq__answer`, `home-faq__icon`. Item border/radius/padding per spec. Accordion hooks via `data-accordion*`.

Answer 1: DEMO placeholder (pre-existing lorem). Answers 2–10: BLOCKED (empty panels).

## Final form fields

Four fields in order: name, phone, email, message. Submit: `Записаться на консультацию` with `btn btn_dark btn--primary`. Phone Inputmask active. Email required with native validation. Backend: NOT CONNECTED.

## Responsive results

Screenshots captured at 1398 desktop and 390 mobile for all six correction areas. Build validation: PASS.

## Swiper instances

| Block | Instances |
|-------|-----------|
| Gallery | 1 |
| Reviews | 1 |
| Specialists | 1 |
| **Total** | **3** |

## Fancybox validation

Local bundle loaded once. Decorative tile excluded. Photo navigation expected via Fancybox carousel (keyboard Escape supported by library defaults).

## Regressions

Previous upper-home sections: NONE observed in build/dist checks. Gallery/Reviews/Footer: NONE. Operator geometry outside correction scope: preserved.

## Build result

`npm run build` — **Build succeeded**

## Remaining unknowns

- Real video source URLs — SAFE UNKNOWN
- FAQ answers 2–10 exact copy — BLOCKED
- Final form backend endpoint — NOT CONNECTED
- FAQ answer 1 production copy — DEMO (lorem retained from operator baseline)

## Final verdict

**LOWER-HOME CORRECTIONS — IMPLEMENTED_PENDING_OPERATOR_REVIEW**

Stable backup VERIFIED and tagged before corrections. Operator canonical HTML/SCSS preserved outside scoped edits.
