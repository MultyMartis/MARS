# FP-0002 V9-06D9-0 Full Port Implementation Wave Plan v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9-0-full-visual-port-charter/full-port-implementation-wave-plan.json`

## Framing

Move from **lightweight MVP skeleton** (D7-B + D8 seeds) to **full static V9 visual parity** on WordPress runtime.

## Wave sequence

| Wave | Objective | Mutation type | Runtime delivery | DB checkpoint | Risk | Acceptance |
|------|-----------|---------------|:---:|:---:|:---:|------------|
| **D9-B** | Header + fonts + global assets + messenger/icon parity | source/theme, runtime | yes | no | MED | Fonts 200; messengers visible; nav aligned |
| **D9-C** | Home hero media/overlay parity | source, ACF seed, media, runtime | yes | yes | LOW-MED | `hero__media` visible |
| **D9-D** | Home missing sections template transfer | source, ACF JSON, runtime | yes | no | HIGH | ≥18 home sections |
| **D9-E** | Home ACF/content/media seed | DB seed, media | no | yes | MED | Gallery/reviews/specialists populated |
| **D9-F** | Density/spacing/vendor CSS/JS parity | source, runtime | yes | no | MED | Sliders/lightbox work; density ↑ |
| **D9-G** | Secondary pages parity | source, partial seed, runtime | yes | yes | MED | Hub/service/contacts QA |
| **D9-H** | Full visual parity QA | docs/evidence | no | no | LOW | Repeat D9-A audit PASS |
| D8-F (optional) | Admin UX repair | source only | yes | no | LOW | Russian labels — **after** visual parity |

## D9-B detail (first wave)

**Files likely touched:**
- `inc/assets.php` — vendor enqueue foundation
- `assets/css/v9-style.css` — font path rewrite
- `inc/site-chrome.php` — default messenger rows fallback
- `template-parts/navigation/messenger-links.php` — V9 `#` placeholder parity
- `template-parts/navigation/primary-desktop.php` — nav alignment
- Menu seed script or fallback nav

**Safety gates:** PHP lint; font network audit; messenger DOM smoke; no broad git staging.

**Rollback:** Redeploy prior theme package from manifest.

## D9-C through D9-H

See architecture docs for section-level acceptance. D9-C immediately follows D9-B (hero is wave 2, not wave 1).

## D8-F position

Admin UX repair remains **optional after visual parity** unless operator explicitly prioritizes Olga labels before D9-H.

## Result

Wave plan complete. Recommended order: **D9-B → D9-C → D9-D → D9-E → D9-F → D9-G → D9-H**.
