# SITE-001 W4 Used PDP Decision v1

**Type:** Post-execution decision — W4 Used PDP Structural Visual Slice  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-W4-2026-06-09

**Inputs:**

- [SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md](SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md)
- [SITE-001-W4-USED-PDP-EXECUTION-v1.md](SITE-001-W4-USED-PDP-EXECUTION-v1.md)
- `.recovery-temp/site-001-w4-result.json`

---

## Decision

# **PASS WITH NOTES**

W4 structural-visual slice **deployed successfully** on TEST used PDP. Technical verification **6/6 PASS**. Expected visual impact **7–8/10** pending operator visual sign-off (screenshots not captured in execution session).

---

## Gate assessment

| Gate | Result |
|------|--------|
| Pre-write charter + CR + rollback + backup | **PASS** |
| Design plan before implementation | **PASS** |
| Scope compliance (no PHP/JS/DB) | **PASS** |
| W4 markers on target PDP | **PASS** (4/4) |
| Regression URLs (no w4 leak) | **PASS** (5/5) |
| Cache clear | **PASS** |
| Operator visual HITL | **PENDING** — screenshots required |
| Production authorization | **NOT AUTHORIZED** |

---

## Rationale

### Why PASS

1. **First meaningful PDP composition change** — hero unified shell, commercial offer band, spec card grid, light trust strip address root cause (OpenCart widget stack) that CSS-only waves could not fix.
2. **Scoped correctly** — `.used_car_page` CSS + `product.twig` (used-only template); zero w4 marker leak on catalog/home/about/contact.
3. **Preserves business logic** — all forms, modal hooks, Swiper/Fancybox classes, twig variables unchanged.
4. **Rollback ready** — T1 backup `pre-w4-20260609` with 3 files.

### Why WITH NOTES

1. **Operator visual sign-off pending** — HTTP marker verification ≠ perceptual 7/10 confirmation; operator must open target URL and capture before/after screenshots per execution checklist.
2. **W3 cosmetic waves superseded for PDP** — W3WF-01 remains **ON HOLD** per Visual Change Failure Audit; W4 is the authorized structural path for used PDP only.
3. **New PDP / catalog / homepage unchanged** — impact isolated to used PDP as intended; operator may expect sitewide change — clarify expectation.

---

## Rollback recommendation

**NO rollback** at this time. Rollback only if operator visual review FAIL or regression discovered.

T1 path: restore `pre-w4-20260609` → [SITE-001-W4-USED-PDP-ROLLBACK-PLAN-v1.md](SITE-001-W4-USED-PDP-ROLLBACK-PLAN-v1.md).

---

## Next actions (operator)

1. Hard-refresh target PDP (`Ctrl+Shift+R`) — cache headers may be `max-age=604800`.
2. Capture desktop/tablet/mobile screenshots (hero, equipment, credit form).
3. Rate visual impact 1–10 on used PDP only.
4. If **≥7/10** — accept W4; consider W4-B (catalog) or W4-C (new PDP) as separate charters.
5. If **<7/10** — document gaps; iterate W4-I2 within same scope or T1 rollback.

---

## W3 wave status update

| Wave | Status after W4 |
|------|-----------------|
| W3COLOR / W3ATMOSPHERE / W3WF | **STOPPED** for sitewide cosmetic expectation |
| W4 Used PDP | **ACTIVE on TEST** — this decision |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **DECISION** — W4 PASS WITH NOTES; operator visual HITL pending |

*SITE-001 W4 Used PDP Decision v1 — TEST only.*
