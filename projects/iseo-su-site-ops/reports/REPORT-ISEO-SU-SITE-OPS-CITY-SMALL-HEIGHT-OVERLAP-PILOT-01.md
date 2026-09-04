# REPORT — ISEO-SU SITE OPS CITY SMALL-HEIGHT OVERLAP PILOT 01

**Task ID:** `ISEO-SU-SITE-OPS-CITY-SMALL-HEIGHT-OVERLAP-PILOT-01`  
**Date:** 2026-09-04  
**Final status:** **PILOT COMPLETE — NOVOSIBIRSK LOW-HEIGHT OVERLAP FIXED / WAITING FOR OPERATOR VISUAL APPROVAL**

**Pilot URL:** https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html

---

## 1. Execution Summary

Fixed first-screen / `main#SecondScreen` visual overlap on low desktop height for **Novosibirsk only**. Root cause was shared `.page_scene_inner { height: 100vh }` capping layout while long intro overflowed; SecondScreen starts in normal flow and visually collided with overflowing copy. Pilot uses body-scoped CSS (`height:auto; min-height:100vh`) so siblings stay unchanged. Layout-only; SEO/content/sitemap untouched. Operator visual approval required before any rollout.

---

## 2. Preflight

| Check | Result |
|-------|--------|
| CWD | `X:\AI MARS` |
| Volume X: | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Origin tip (sync base) | `61ada673…` (WAVE 04 recorded tip; verified at sync time) |
| Local HEAD | divergent / dirty — **not** used for push |
| Staged | empty |
| Foreign WIP | present — preserved |
| Sync strategy | clean STORAGE worktree onto `origin/mars/canonical-post-recovery` |

---

## 3. Root cause / fix

```
PILOT PAGE:
https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html

ROOT CAUSE:
.page_scene_inner { height: 100vh } — fixed viewport height while Novosibirsk intro is taller than short desktop viewports; content overflows; SecondScreen (normal flow) starts at ~100vh and overlaps overflowing first-screen copy.

FIRST SCREEN HEIGHT MECHANISM:
Shared main.css .page_scene_inner height:100vh (+ padding-bottom:70px, flex center). Pilot overrides: height:auto; min-height:100vh; position:relative (body.city-seo-novosibirsk-height-pilot).

SECOND SCREEN COLLISION MECHANISM:
#SecondScreen is in-flow after header/first screen. Not absolute. Overlap = overflow of fixed-height first box into the vertical space where SecondScreen begins.
```

Pilot files:

- HTML: body class + link to `city-seo-novosibirsk-height-pilot.css`
- CSS: scoped override only

---

## 4. Viewport matrix

```
VIEWPORT 1920x1080: NO OVERLAP / PASS
VIEWPORT 1440x900:  NO OVERLAP / PASS
VIEWPORT 1366x768:  NO OVERLAP / PASS
VIEWPORT 1280x720:  NO OVERLAP / PASS
VIEWPORT 1366x650:  NO OVERLAP / PASS
VIEWPORT 1440x600:  NO OVERLAP / PASS
MOBILE 390x844:     NO OVERLAP / PASS
MOBILE 360x800:     NO OVERLAP / PASS
```

---

## 5. Content / controls guard

```
INTRO CONTENT CHANGED: NO
H1 CHANGED: NO
SEO META CHANGED: NO
CANONICAL CHANGED: NO
SITEMAP CHANGED: NO
STATIC SITEMAP URL COUNT: 139
FORM/CONSENT CHANGED: NO
CALCULATOR CHANGED: NO
CROSS-CITY NAV CHANGED: NO

PILOT PRODUCTION FIX: YES (Novosibirsk HTML + pilot CSS)
SIBLING CITY PAGES MODIFIED: NO
PRODUCTION/SOURCE ALIGNED: YES
```

---

## 6. Backup / evidence

- Backup: `X:\AI MARS\local\sites\iseo-su-production\_city-small-height-overlap-pilot-01\20260904T045143Z\`
- HTML SHA before: `de54cb53…`
- HTML/CSS after: `2ef7a39c…` / `a3e5323b…`
- Screenshots: `X:\AI MARS\projects\iseo-su-site-ops\evidence\city-small-height-overlap-pilot-01\screenshots\20260904T045143Z\`
- Full evidence: [ISEO-SU-CITY-SMALL-HEIGHT-OVERLAP-PILOT-01-EVIDENCE-v1.md](../ISEO-SU-CITY-SMALL-HEIGHT-OVERLAP-PILOT-01-EVIDENCE-v1.md)
- Validate JSON: `tools/_city-small-height-overlap-pilot-01-validate.json`

---

## 7. Final Hard Check

```
PILOT PAGE:
https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html

ROOT CAUSE:
fixed height:100vh on .page_scene_inner + long Novosibirsk intro overflow vs in-flow #SecondScreen

FIRST SCREEN HEIGHT MECHANISM:
shared height:100vh → pilot height:auto + min-height:100vh (scoped)

SECOND SCREEN COLLISION MECHANISM:
normal-flow SecondScreen starts after capped first box while overflow still paints above it

VIEWPORT 1920x1080: NO OVERLAP / PASS
VIEWPORT 1440x900: NO OVERLAP / PASS
VIEWPORT 1366x768: NO OVERLAP / PASS
VIEWPORT 1280x720: NO OVERLAP / PASS
VIEWPORT 1366x650: NO OVERLAP / PASS
VIEWPORT 1440x600: NO OVERLAP / PASS
MOBILE 390x844: NO OVERLAP / PASS
MOBILE 360x800: NO OVERLAP / PASS

INTRO CONTENT CHANGED: NO
H1 CHANGED: NO
SEO META CHANGED: NO
CANONICAL CHANGED: NO
SITEMAP CHANGED: NO
FORM/CONSENT CHANGED: NO
CALCULATOR CHANGED: NO
CROSS-CITY NAV CHANGED: NO

PILOT PRODUCTION FIX: YES
SIBLING CITY PAGES MODIFIED: NO
PRODUCTION/SOURCE ALIGNED: YES

VISUAL EVIDENCE:
X:\AI MARS\projects\iseo-su-site-ops\evidence\city-small-height-overlap-pilot-01\screenshots\20260904T045143Z\

REMOTE SYNC: YES — `3d087501f7572d355bd7fdab38355c3f7dc7b4b5` on `origin/mars/canonical-post-recovery` (worktree `X:\AI MARS STORAGE\git-sync-iseo-su-city-height-overlap-pilot-01\repo`, branch `wave/iseo-su-city-height-overlap-pilot-01`; push ff-only `61ada673..3d087501`)

ROLLOUT STATUS:
WAITING FOR OPERATOR VISUAL APPROVAL

FINAL STATUS:
PILOT COMPLETE — NOVOSIBIRSK LOW-HEIGHT OVERLAP FIXED / WAITING FOR OPERATOR VISUAL APPROVAL
```

---

## 8. STOP

STOP after Novosibirsk pilot. Do **not** patch other city/niche/USA/UAE pages or deploy a global `main.css` change until operator approves this pilot visually.
