# SITE-001 W3ATMOSPHERE-01 Discovery v1

**Type:** Pre/post execution discovery — atmosphere layer inventory  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Wave:** W3ATMOSPHERE-01 — Global Atmosphere Refresh  
**Inputs:** [SITE-001-W3COLOR-01-DISCOVERY-v1.md](SITE-001-W3COLOR-01-DISCOVERY-v1.md) · [SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md](SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md)

**Evidence (local, not in git):** `.recovery-temp/site-001-w3atmosphere-01-discovery.json` · `.recovery-temp/site-001-w3atmosphere-01-result.json`

---

## Executive summary

Pre-execution live CSS (post-W3VIS rollback, active W3-V + W3V2 + W3UX-C1): `main.css` 118 851 bytes / 7 418 lines · `media.css` 31 485 bytes. No `--w3color-*` tokens · no W3ATMOSPHERE marker. Canvas `#F7F8FA` — insufficient contrast vs white cards. Legacy literals remain in base layer (56× red, 48× dark, 24× grey borders, 68× `border-radius: 4px`).

Post-execution: W3ATMOSPHERE block appended after W3V2 · 31 `--w3color-*` tokens · canvas `#EEF1F5` live · `main.css` 129 060 bytes / 7 771 lines · `media.css` 32 601 bytes / 2 293 lines.

---

## Pre-execution baseline

| Layer | Status |
|-------|--------|
| W3-V | **ACTIVE** |
| W3V2 | **ACTIVE** |
| W3UX-C1 | **ACTIVE** |
| W3VIS-01A/01B | **ROLLED BACK** |
| W3ATMOSPHERE-01 | **NOT PRESENT** |

| Metric | Value |
|--------|-------|
| Body canvas (W3V2) | `#F7F8FA` |
| Legacy red `rgb(170,3,3)` | 56 hits |
| Legacy dark `rgb(33,36,43)` | 48 hits |
| Legacy border `rgb(208,208,208)` | 24 hits |
| `border-radius: 4px` | 68 hits |
| `four_blocks` in W3V2 card group | **NO** |
| Footer 10px near-black seams | **YES** (base layer) |

---

## Target atmosphere system (execution)

| Role | Token / value |
|------|---------------|
| Canvas | `#EEF1F5` (`--w3color-canvas`) |
| Card | `#FFFFFF` |
| Raised (tools) | `#FAFBFC` |
| Sunken | `#E4E8ED` |
| Graphite gradient top | `#353A45` |
| Graphite gradient bottom | `#272B33` |
| Card radius | 12px unified |
| Shadow | graphite sm/md/lg stack |

---

## Post-execution inventory

| Check | Result |
|-------|--------|
| W3ATMOSPHERE marker in live CSS | **YES** |
| `--w3color-canvas` live | **YES** — `#EEF1F5` |
| W3V2 bridge tokens remapped | **YES** |
| W3VIS markers absent | **YES** |
| Legacy base literals purged entirely | **NO** — base rules retained; override layer covers atmosphere selectors |
| Backup | `pre-w3atmosphere-01-20260609-1156` |

---

## Scope compliance

| Boundary | Honored |
|----------|---------|
| Files touched | `css/main.css`, `css/media.css` only |
| DOM/Twig/PHP/JS | **NONE** |
| Spacing/padding/margin | **NONE** |
| Layout/typography scale | **NONE** |
| PDP hierarchy | **NONE** |

---

## Risk notes

- Base-layer legacy literals remain — visual impact mitigated by post-W3V2 override + W3ATMOSPHERE block cascade.
- Operator should confirm footer gradient and form focus on live scroll (automated screenshots cover header/catalog/home).
