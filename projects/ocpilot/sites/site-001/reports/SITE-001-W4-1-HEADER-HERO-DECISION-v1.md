# SITE-001 W4.1 Header & Hero Authority Decision v1

**Type:** Wave decision — W4.1 Header & Hero Authority  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Execution report:** [SITE-001-W4-1-HEADER-HERO-EXECUTION-v1.md](SITE-001-W4-1-HEADER-HERO-EXECUTION-v1.md)

---

## Verdict

**PASS WITH NOTES** — technical verification complete; operator visual sign-off **PENDING**

---

## Criteria assessment

| Criterion | Result |
|-----------|--------|
| Header visible and usable | **PASS** — 9/9 URLs |
| Nav links, logo, phone/WhatsApp/callback present | **PASS** |
| Promo strip present | **PASS** |
| PDP W4 layout preserved | **PASS** — all `w4-used-*` markers live |
| No footer regression | **PASS** — footer.twig not modified |
| No PHP/Twig errors | **PASS** — HTTP 200 all URLs |
| W3UX-C1 / W3ATMOSPHERE markers preserved | **PASS** |
| First-screen visual impact ≥7/10 | **PENDING** — operator HITL required |

---

## Notes

| ID | Note |
|----|------|
| N-W4-1-01 | Promo strip CSS applies globally to `.lcd_display.header` — catalog pages benefit without twig edits |
| N-W4-1-02 | Header sticky on desktop; reverts to `position: relative` on mobile ≤767px |
| N-W4-1-03 | Visual impact assessment requires operator hard-refresh (CSS cache `max-age=604800` risk per audit 4.127) |
| N-W4-1-04 | If visual impact not obvious → **FAIL** → T1 rollback from `pre-w4-1-stable-20260609-1506` recommended |

---

## Rollback reference

T1 restore: [SITE-001-W4-1-HEADER-HERO-ROLLBACK-PLAN-v1.md](SITE-001-W4-1-HEADER-HERO-ROLLBACK-PLAN-v1.md)  
Backup: `pre-w4-1-stable-20260609-1506`

---

## Operator next action

1. Hard-refresh TEST (Ctrl+Shift+R)  
2. Review screenshots in `qa/w4-1-header-hero-screenshots/`  
3. Rate first-screen impact on homepage + used PDP (target **7/10**)  
4. Accept W4.1 or authorize T1 rollback

---

## Authorization status

| Action | Status |
|--------|--------|
| Commit | **NOT AUTHORIZED** |
| Push | **NOT AUTHORIZED** |
| Production | **NOT AUTHORIZED** |

*SITE-001 W4.1 Header & Hero Authority Decision v1*
