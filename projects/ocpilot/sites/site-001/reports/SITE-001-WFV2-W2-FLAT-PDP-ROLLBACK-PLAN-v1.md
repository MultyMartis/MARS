# SITE-001 WF-V2-W2 Flat PDP Rollback Plan v1

**Type:** T1 rollback plan — WF V2 Wave 2 Used PDP Flat Stage  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-WFV2-W2-2026-06-10

---

## Trigger conditions

| Condition | Action |
|-----------|--------|
| Operator visual HITL **FAIL** (change not obvious / regression) | **T1 rollback** |
| 8-URL verification **FAIL** | **T1 rollback** |
| Modal / dropdown / responsive regression | **T1 rollback** |
| W2 CSS leak to non-used PDP pages | **T1 rollback** |

---

## T1 procedure

1. Locate backup folder `pre-wfv2-w2-flat-pdp-YYYYMMDD-HHMM` under  
   `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\`
2. FTP **STOR** restore:

| Remote path | Local backup file |
|-------------|-------------------|
| `catalog/view/theme/auto/template/product/product.twig` | `catalog__view__theme__auto__template__product__product.twig` |
| `css/main.css` | `css__main.css` |
| `css/media.css` | `css__media.css` |

3. OpenCart admin — clear system + modification + image cache; run modification refresh.
4. Hard-refresh QA (CSS `max-age=604800` on TEST).
5. Re-run 8-URL verification matrix.
6. Confirm absent: `WF-V2-W2 Flat Used PDP Stage` in live CSS; `wfv2-flat-pdp` in used PDP HTML.
7. Confirm present: W5-C commercial stage surfaces restored; WF-V2-W1 header unchanged.

---

## Post-rollback state

| Layer | State |
|-------|--------|
| Header | WF-V2-W1 Hybrid Header (unchanged) |
| Used PDP | W5-C Commercial Stage (pre-W2) |
| Homepage / catalog | Unchanged |

**Prior baseline if W2 backup lost:** `pre-wfv2-w1-header-20260610-0216` (CSS only — product.twig from W5-C backup `pre-w5c-commercial-stage-20260610-0002`).

---

## Rollback verification matrix

Same 8 URLs as execution charter. Used PDP must show W5-C card surfaces; no `wfv2-flat-pdp`.

---

## Operator sign-off

| Field | Value |
|-------|-------|
| Rollback executed by | _pending_ |
| Rollback verified | _pending_ |
| Decision doc | Update [SITE-001-WFV2-W2-FLAT-PDP-DECISION-v1.md](SITE-001-WFV2-W2-FLAT-PDP-DECISION-v1.md) |

*SITE-001 WF-V2-W2 Flat PDP Rollback Plan v1 — TEST only.*
