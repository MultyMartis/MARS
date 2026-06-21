# SITE-001 WF-V2-W1 Hybrid Header Decision v1

**Type:** Automated decision record — WF V2 Wave 1 Hybrid Header  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Execution:** [SITE-001-WFV2-W1-HEADER-EXECUTION-v1.md](SITE-001-WFV2-W1-HEADER-EXECUTION-v1.md)  
**Change request:** CR-SITE-001-WFV2-W1-2026-06-10

---

## Automated verdict

| Criterion | Result |
|-----------|--------|
| 8-URL verification matrix | **PASS** (8/8) |
| W5-C PDP preservation | **PASS** |
| Phone/WhatsApp rail-only (desktop) | **PASS** |
| Callback in primary band | **PASS** |
| Original logo (no invert) | **PASS** |
| Dropdown «Услуги» / «Ещё» | **PASS** |
| No sticky header | **PASS** |
| Promo strip visible, no overlap | **PASS** |
| Mobile offcanvas | **PASS** |
| CSS marker deployed | **PASS** |

**Automated decision:** **PASS WITH NOTES**

---

## Notes

1. **Operator visual HITL PENDING** — automated checks confirm structure and markers; 3-second «closer to V2 concept» test requires human review of before/after screenshots.
2. **Hybrid direction** — implements approved HITL override (not pure-light spec `02`, not W5-A graphite).
3. **W5-C unchanged** — used PDP commercial stage intact on target URL.
4. **CSS cache** — hard-refresh recommended (`max-age=604800` on theme CSS).

---

## Operator action required

| Step | Action |
|------|--------|
| 1 | Hard-refresh [homepage](https://sibcar.new-site.space/) — compare to concept mock `01` |
| 2 | Review screenshots in `qa/wfv2-w1-header-screenshots/` |
| 3 | Confirm header reads cleaner than Baseline V1 |
| 4 | Hover «Услуги» and «Ещё» at 1440px |
| 5 | Check used PDP header + stage unchanged |

| Outcome | Action |
|---------|--------|
| Visual **PASS** | Mark WF-V2-W1 **ACCEPTED** → authorize WF-V2-W2 (Used PDP Flat Stage) |
| Visual **FAIL** | T1 rollback from `pre-wfv2-w1-header-20260610-0216` |

---

## Authorization

| Action | Status |
|--------|--------|
| Commit | **NOT AUTHORIZED** |
| Push | **NOT AUTHORIZED** |
| Production | **NOT AUTHORIZED** |
