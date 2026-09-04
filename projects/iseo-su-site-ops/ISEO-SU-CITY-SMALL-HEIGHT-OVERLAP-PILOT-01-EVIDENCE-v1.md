# ISEO-SU CITY SMALL-HEIGHT OVERLAP PILOT 01 — EVIDENCE

**Task ID:** `ISEO-SU-SITE-OPS-CITY-SMALL-HEIGHT-OVERLAP-PILOT-01`  
**Date (UTC):** 2026-09-04  
**Pilot:** Novosibirsk only  
**Status:** **AWAITING OPERATOR VISUAL APPROVAL**  
**Sibling / niche / USA/UAE rollout:** **DEFERRED** until explicit operator approval

---

## 1. Pilot scope

| Field | Value |
|-------|-------|
| Pilot URL | https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html |
| Canonical HTML | `projects/iseo-su-site-ops/production-source/static-html/services/seo/prodvizhenie-v-novosibirske.html` |
| Pilot CSS | `projects/iseo-su-site-ops/production-source/css/city-seo-novosibirsk-height-pilot.css` |
| Body class | `city-seo-novosibirsk-height-pilot` |
| Global `main.css` mutated | **NO** |
| Sibling city pages mutated | **NO** |

Comparison references (read-only / unchanged): hub `b-regionakh.html`, SPB, Kazan, Ekaterinburg, Krasnoyarsk.

---

## 2. Root cause

| Field | Finding |
|-------|---------|
| FIRST SCREEN SOURCE | `.page_scene` → `.page_scene_inner` → `.page_scene__description` (H1 + intro) + `.page_scene__info`; then `</header>` → `<main id="SecondScreen">` |
| FIRST SCREEN HEIGHT RULE | Shared `main.css`: `.page_scene_inner { display:flex; align-items:center; height:100vh; padding-bottom:70px; box-sizing:border-box; }` |
| SECOND SCREEN POSITIONING RULE | `#SecondScreen` is normal document flow after the first-screen block (not absolute). Collision is visual: overflowing first-screen copy sits on top of the next section’s start |
| WHY ORIGINAL / SHORTER PAGES DO NOT OVERLAP | Intro fits inside ~100vh; no overflow past the fixed-height box |
| WHY NOVOSIBIRSK DOES | Longer approved city intro exceeds viewport height; fixed `height:100vh` caps layout box while content overflows; SecondScreen starts at ~100vh and overlaps overflowing copy |
| `#city-seo-cross-nav` | **Not** the cause (lives inside SecondScreen content, after the collision boundary) |

---

## 3. Fix principle (pilot isolation)

Preferred architecture (reusable later): replace restrictive fixed `height: 100vh` with `height: auto` + `min-height: 100vh` so the first screen grows with content and SecondScreen remains in normal flow after it.

**Pilot method (no sibling production change):**

1. Add body class `city-seo-novosibirsk-height-pilot` on Novosibirsk only.
2. Link page-specific stylesheet `../../css/city-seo-novosibirsk-height-pilot.css` after `media.css`.
3. Rule:

```css
body.city-seo-novosibirsk-height-pilot .page_scene_inner {
	height: auto;
	min-height: 100vh;
	position: relative;
}
```

Protected content unchanged: title, description, H1, intro, FAQ, cross-city nav, hub backlink, canonical, robots, sitemap, forms, consent, calculator, Metrika.

---

## 4. Backup

| Field | Value |
|-------|-------|
| Timestamp | `20260904T045143Z` |
| Backup dir | `X:\AI MARS\local\sites\iseo-su-production\_city-small-height-overlap-pilot-01\20260904T045143Z\` |
| Production HTML | `/home/n/nikel0rv/i-seo.su/public_html/services/seo/prodvizhenie-v-novosibirske.html` |
| HTML SHA-256 before | `de54cb53b728f26fa8d63e0d03868154347a1c8006d828ec042f0f55d61ebf8d` |
| Pilot CSS before | absent (new file) |

---

## 5. Deploy / hashes after

| Artifact | SHA-256 |
|----------|---------|
| HTML after (source = production SFTP) | `2ef7a39c6cd72c48adee44ac77b9b16cea9f43ebc82d07490d6941330e2e41e5` |
| Pilot CSS after | `a3e5323b6e13da985f96366363426c09ddb6d37e8f046c5604e768b8a68cc339` |
| PRODUCTION/SOURCE ALIGNED | **YES** |

Validate JSON: `projects/iseo-su-site-ops/tools/_city-small-height-overlap-pilot-01-validate.json`  
Deploy script: `projects/iseo-su-site-ops/tools/_city-small-height-overlap-pilot-01-deploy-validate.py`

---

## 6. Viewport matrix (post-deploy Playwright)

| Viewport | Overlap | Clipped | Intro visible | CTA visible | Pass |
|----------|---------|---------|---------------|-------------|------|
| 1920×1080 | NO | NO | YES | YES | PASS |
| 1440×900 | NO | NO | YES | YES | PASS |
| 1366×768 | NO | NO | YES | YES | PASS |
| 1280×720 | NO | NO | YES | YES | PASS |
| 1366×650 | NO | NO | YES | YES | PASS |
| 1440×600 | NO | NO | YES | YES | PASS |
| 390×844 | NO | NO | YES | YES | PASS |
| 360×800 | NO | NO | YES | YES | PASS |

Low-height example (1440×600): `.page_scene_inner` computed height ≈ **1094px**, `min-height` = 600px; `second_top_doc` > `content_bottom_doc`; gap ≈ **140px**.

---

## 7. Controls / regression

| Check | Result |
|-------|--------|
| Hub / SPB / Kazan / EKB / Krasnoyarsk remote SHA | **UNCHANGED** |
| Static sitemap URL count | **139** (expected 139; unchanged by this task) |
| Title / H1 / description / canonical | **UNCHANGED** |
| Form / consent / calculator smoke | healthy markers present |
| HTTP pilot | **200** |

---

## 8. Visual evidence paths

Directory:

`X:\AI MARS\projects\iseo-su-site-ops\evidence\city-small-height-overlap-pilot-01\screenshots\20260904T045143Z\`

Notable:

- Normal desktop: `pilot-1920x1080.png`
- Low-height + boundary: `pilot-1440x600.png`, `pilot-1440x600-boundary.png`, `pilot-1366x650-boundary.png`, `pilot-1280x720-boundary.png`

Boundary shots are scrolled so first-screen text ends, then SecondScreen begins, with no overlap.

---

## 9. Rollout

| Field | Value |
|-------|--------|
| PILOT | Novosibirsk |
| STATUS | AWAITING OPERATOR VISUAL APPROVAL |
| Potential rollout to other city/niche/INTL pages | **DEFERRED** — separate charter after operator approval |
| Do not auto-patch | other 4 city pages; 7 niche; USA/UAE; global `main.css` alone |

---

## 10. Operator next step

Visually inspect:

https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html

Especially desktop **width ≥ 1280** with **height ≤ 720** (e.g. 1440×600, 1366×650).

Only after explicit approval may a follow-up rollout task generalize the same `min-height` pattern.
