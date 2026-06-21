# SITE-001 W5-A Header Shell Recomposition Decision v1

**Type:** Execution decision — W5-A Header Shell  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Execution input:** [SITE-001-W5A-HEADER-SHELL-EXECUTION-v1.md](SITE-001-W5A-HEADER-SHELL-EXECUTION-v1.md)  
**Design authority:** [SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md](SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md) §2.1

---

## Technical verdict

| Gate | Result |
|------|--------|
| Pre-write backup + manifest | **PASS** |
| File allow-list respected | **PASS** — header.twig + main.css + media.css only |
| Forbidden scope (PHP/JS/DB/product/footer) | **PASS** — none modified |
| 8-URL verification matrix | **PASS** |
| W4 Used PDP preservation | **PASS** |
| Cache clear | **PASS** |
| W4.1 sticky removed | **PASS** — `position: static` on `.w5a-header-shell` |
| Promo visible on catalog/PDP | **PASS** |
| Callback / phone / menu functional | **PASS** (marker + HTTP) |

**Technical decision:** **PASS WITH NOTES** — execution complete; operator visual HITL **PENDING**.

---

## Architecture checklist (Concept B §2.1)

| Requirement | Evidence | Status |
|-------------|----------|--------|
| One dealer shell (not 3 bands) | Contact rail + primary band unified; promo inset via CSS | **PASS** |
| Centered navigation | `.w5a-nav__group` flex center in primary band | **PASS** |
| Static header | W5-A-A sticky override | **PASS** |
| Logo anchor in primary band | `.w5a-header__logo-zone`; tagline demoted (hidden) | **PASS** |
| CTA hierarchy callback > phone > WA | `.w5a-cta--primary/secondary/supportive` | **PASS** |
| Promo integrated (not third strip) | Sibling `.lcd_display.header` inset margins + shared shell shadow | **PASS WITH NOTES** — DOM still sibling; visual integration CSS-only (charter scope) |
| Frozen menu/URLs/content | Twig links unchanged | **PASS** |

---

## Visual impact assessment (automated evidence)

| Signal | Before | After |
|--------|--------|-------|
| Band count at silhouette | 3 competing strips | 2 zones + inset promo |
| Nav position (homepage) | Below hero slider | Above hero slider (post `header_cup` fix) |
| Toolbar logo + tagline noise | High | Logo only in primary band |
| Screenshot delta | `w5a-header-shell-screenshots/before-*` vs `after-*` | **Visible structural change** |

**Automated 3-second test:** **INCONCLUSIVE** — requires operator HITL (logo-hidden silhouette rating).

---

## Notes

1. **`header_cup` order** — initial deploy placed hero between contact rail and nav; corrected same session.  
2. **Nav/CTA density** — desktop 1440px required CSS gap reduction; monitor on 1280px viewports.  
3. **Promo DOM** — remains page-template sibling; W5-A achieves inset via CSS only (product.twig out of scope).

---

## Operator actions required

1. Hard-refresh TEST (`Ctrl+Shift+R`) on `/`, `/cars/`, used PDP, `/about`.  
2. Rate header **3-second test** — target: «modern dealership» **without logo**.  
3. If impact **subtle** → recommend **T1 rollback** per charter.  
4. If **PASS** → authorize **W5-B** homepage showroom (separate task).

---

## Final verdict

| Layer | Verdict |
|-------|---------|
| OCPilot technical | **PASS WITH NOTES** |
| Operator visual HITL | **PENDING** |
| W5-B authorization | **NOT AUTHORIZED** until W5-A HITL |

**Commit / push / production:** **NOT AUTHORIZED**
