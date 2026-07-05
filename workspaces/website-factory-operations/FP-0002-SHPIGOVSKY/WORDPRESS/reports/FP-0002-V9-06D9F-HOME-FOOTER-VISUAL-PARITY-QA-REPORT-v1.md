# REPORT — FP-0002 V9-06D9-F HOME + FOOTER VISUAL PARITY QA

**Date:** 2026-07-05  
**Commit base:** `3546f80bcf16dde3686dc40c55bf8ea99f69e2d0` (D9-E HEAD)  
**Mode:** Read-only QA — no repairs performed

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: `X:\AI MARS`
- Branch: `mars/canonical-post-recovery`
- Local HEAD: `3546f80bcf16dde3686dc40c55bf8ea99f69e2d0`
- Local short HEAD: `3546f80b`
- Remote HEAD: `3546f80bcf16dde3686dc40c55bf8ea99f69e2d0`
- Remote short HEAD: `3546f80b`
- Ahead: 0
- Behind: 0
- Foreign WIP: present (untracked helpers, `.recovery-temp/`, unrelated modified workspaces) — unstaged
- Pre-existing staged files: none
- Strict HEAD gate: PASS
- Result: **PASS**

## 2. Authorization and scope

- Operator authorization: V9-06D9-F Home + Footer Visual Parity QA
- Task mode: READ-ONLY QA
- Runtime delivery: NOT_PERFORMED
- Source/theme changes: 0
- Runtime file writes: 0
- DB writes: 0
- ACF writes: 0
- ACF JSON changes: 0
- Options writes: 0
- Menu writes: 0
- Rewrite/permalink changes: 0
- Plugin source changes: 0
- V9 src/dist changes: 0
- Media uploads: 0
- Documentation/evidence writes: YES (approved paths only)
- Result: **PASS**

## 3. Home section QA

| Area | Static V9 | Runtime D9-F | Result | Notes |
|---|---|---|---|---|
| Main section count | 19 | 19 | PASS | `<main>` sections |
| Section order | 19-block V9 order | identical | PASS | all 19 orderMatch |
| Hero CTA | Записаться на консультацию | same | PASS | |
| Gallery / reviews / specialists blocks | present | present | PASS | structure only |
| FAQ `aria-labelledby` | `faq-heading` | `comfort-heading` | FAIL | transplant typo |
| FAQ heading `id` | `faq-heading` | `comfort-heading` | FAIL | duplicate with comfort |
| FAQ heading text | Нас часто спрашивают | Комфорт, приватность, забота | FAIL | wrong copy |
| FAQ classification | PASS | MINOR_REPAIR_REQUIRED | MINOR_REPAIR_REQUIRED | `template-parts/home/faq.php` |
| Duplicate `comfort-heading` ids | 1 | 2 | FAIL | comfort + faq |
| Mobile stacking (proxy) | — | screenshots captured | PASS | no gross break observed |
| **Overall home** | — | — | **PARTIAL** | single FAQ defect |

## 4. Footer QA

| Area | Static V9 | Runtime D9-F | Result | Notes |
|---|---|---|---|---|
| Layout | site-footer | site-footer | PASS | D9-D transplant |
| Logo | yes | yes | PASS | |
| Nav columns | yes | yes | PASS | |
| Contacts | yes | yes | PASS | |
| Privacy/legal | yes | yes | PASS | |
| Scroll-to-top | not in DOM proxy | not in DOM proxy | PARTIAL | non-blocking observation |
| Credit | yes | yes | PASS | |
| Secondary routes | — | 7/7 footer present | PASS | |
| **Overall footer** | — | — | **PASS** | |

## 5. Slider/vendor QA

| Component | Expected | Runtime D9-F | Result | Notes |
|---|---|---|---|---|
| Specialists heading | Специалисты центра / specialists-heading | correct | PASS | D9-E fix verified |
| Gallery pagination | V9 styled dots | present + css order OK | PASS | |
| Reviews pagination | V9 styled dots | present | PASS | |
| Specialists pagination | V9 styled dots | present | PASS | |
| Swiper CSS order | before v9-style.css | PASS | PASS | |
| Default blue bullets | absent | absent (proxy) | PASS | |
| Vendor 404s | none | none in set | PASS | |
| **Overall slider/vendor** | — | — | **PASS** | |

## 6. Asset/network/console QA

| Check | Result | Notes |
|---|---|---|
| Swiper CSS/JS HTTP 200 | PASS | |
| Fancybox CSS/JS HTTP 200 | PASS | |
| v9-style.css / v9-shell.js | PASS | |
| CSS cascade order | PASS | vendor before theme |
| Sample theme images | PASS | logo + hero |
| Console fatals | PASS | static proxy; no blocking errors |
| **Overall** | **PASS** | |

## 7. Secondary route safety QA

| Route | HTTP | Header | Footer | Fatal | Result |
|---|---:|---|---|---|---|
| `/` | 200 | yes | yes | no | PASS |
| `/uslugi/` | 200 | yes | yes | no | PASS |
| `/uslugi/zavisimosti/` | 200 | yes | yes | no | PASS |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | yes | yes | no | PASS |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | yes | yes | no | PASS |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | yes | yes | no | PASS |
| `/kontakty/` | 200 | yes | yes | no | PASS |

## 8. Visual findings register

| Finding | Severity | Repair needed | Recommended task |
|---|---|---:|---|
| FAQ uses `comfort-heading` id/aria and comfort copy instead of `faq-heading` / «Нас часто спрашивают» | MINOR | yes | CREATE_V9_06D9G_MICRO_VISUAL_REPAIR_TASK |
| Duplicate `id="comfort-heading"` on comfort + FAQ sections | MINOR | yes | same micro repair |
| Scroll-to-top marker not detected in DOM scan | LOW | no | observe only |

## 9. ACF/admin editability readiness

- Visual parity readiness: PARTIAL
- Blocking visual issues: none
- Minor visual issues: FAQ transplant typo (2 related findings)
- ACF wiring recommended now: **NO**
- Recommended next phase: **CREATE_V9_06D9G_MICRO_VISUAL_REPAIR_TASK**
- Reason: Correct FAQ DOM contract before binding ACF fields

## 10. Screenshots

| Screenshot | Captured | Result |
|---|---:|---|
| static-home-full-desktop-reference.png | yes | PASS |
| static-home-full-mobile-reference.png | yes | PASS |
| static-footer-desktop-reference.png | yes | PASS |
| static-footer-mobile-reference.png | yes | PASS |
| static-specialists-desktop-reference.png | yes | PASS |
| static-slider-dots-reference.png | yes | PASS |
| static-faq-desktop-reference.png | yes | PASS |
| runtime-home-full-desktop-d9f.png | yes | PASS |
| runtime-home-full-mobile-d9f.png | yes | PASS |
| runtime-footer-desktop-d9f.png | yes | PASS |
| runtime-footer-mobile-d9f.png | yes | PASS |
| runtime-specialists-desktop-d9f.png | yes | PASS |
| runtime-slider-dots-d9f.png | yes | PASS |
| runtime-faq-desktop-d9f.png | yes | PASS |
| runtime-services-hub-desktop-d9f.png | yes | PASS |
| runtime-service-74-desktop-d9f.png | yes | PASS |
| runtime-contacts-desktop-d9f.png | yes | PASS |

17/17 captured. Manifest: `validation/v9-06d9f-home-footer-visual-parity-qa/screenshot-manifest.json`

## 11. No-scope-drift

- DB writes: 0
- ACF writes: 0
- ACF JSON changes: 0
- Source/theme changes: 0
- Runtime delivery: NOT_PERFORMED
- Runtime file writes: 0
- Options writes: 0
- Menu writes: 0
- Page/service/contact writes: 0
- Rewrite flush: NO
- Object changes: 0
- Media uploads: 0
- Plugin changes: 0
- V9 src/dist changes: 0
- Secrets/API keys: 0
- Result: **PASS**

## 12. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06D9F-HOME-FOOTER-VISUAL-PARITY-QA-REPORT-v1.md` | created | task report |
| `architecture/FP-0002-V9-06D9F-*.md` (6 files) | created | QA architecture pack |
| `validation/v9-06d9f-home-footer-visual-parity-qa/*.json` | created | machine evidence |
| `validation/v9-06d9f-home-footer-visual-parity-qa/screenshots/*` | created | visual evidence |
| `WORDPRESS/README.md` | updated | phase status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | updated | D9-F entry |
| `FP-0002-SHPIGOVSKY/PROJECT-STATUS.md` | updated | phase status |

## 13. Git checkpoint

*(filled after commit)*

## 14. Final verdict

**PARTIAL PASS**

V9-06D9-F Home + Footer Visual Parity QA:
**COMPLETE**

Runtime delivery:
NOT_PERFORMED

Source/theme changes:
0

Runtime file writes:
0

DB writes:
0

ACF writes:
0

ACF JSON changes:
0

Home visual parity:
PARTIAL

Footer visual parity:
PASS

Slider/vendor parity:
PASS

Secondary route safety:
PASS

No-scope-drift:
PASS

ACF/admin editability readiness:
NOT_READY

Recommended next phase:
CREATE_V9_06D9G_MICRO_VISUAL_REPAIR_TASK

## 15. Recommended next action

**CREATE_V9_06D9G_MICRO_VISUAL_REPAIR_TASK**

## 16. Final safety statement

Target folder:
X:\AI MARS

Volume:
AI WS / X:

Runtime:
X:\MARS-Localhost\sites\wordpress\projects\shpigovsky

V9-06D9-F Home + Footer Visual Parity QA performed:
YES

Runtime delivery performed:
NO

Source/theme changes:
0

Runtime file writes:
0

Database writes:
0

ACF writes:
0

ACF JSON changes:
0

Native content writes:
0

Options writes:
0

Menu writes:
0

Service writes:
0

Services Hub writes:
0

Contacts writes:
0

Rewrite flush performed:
NO

Permalink/rewrite changed:
NO

Menus changed:
0

Redirects created:
0

Object create/delete:
0

Media uploads:
0

External API/API keys added:
NO

Production migration performed:
NO

V9 source changed:
NO

V9 dist changed:
NO

Plugin source changed:
NO

Plugin updates run:
0

Plugin installs run:
0

Plugin deletes run:
0

Helper committed:
NO

Secrets committed:
0
