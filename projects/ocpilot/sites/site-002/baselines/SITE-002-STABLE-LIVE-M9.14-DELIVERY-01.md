# SITE-002 — Stable Live M9.14 Delivery Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-M9.14-DELIVERY-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/delivery  
**Registered at:** 2026-06-28  
**Mode:** Stable live checkpoint — `/delivery` page domain only

---

## 1. Authority state

**Checkpoint:** `SITE-002-STABLE-LIVE-M9.14-DELIVERY-01`

**Scope:** Corporate page `/delivery` only — does **not** supersede M9.13 About restored authority for `/about` or catalog UX baselines elsewhere.

**Parent authority (site-wide):** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` remains active for all non-delivery domains.

---

## 2. Live surface

| Item | Value |
|------|--------|
| **URL** | https://zpm.new-site.space/delivery |
| **Route** | `information/delivery` |
| **SEO keyword** | `delivery` → `information/delivery` (`oc_seo_url` id 1047) |
| **Controller** | `catalog/controller/information/delivery.php` |
| **Twig** | `catalog/view/theme/default/template/information/delivery.twig` |
| **CSS** | `assets/css/style.css` — append block `M9.14 — Delivery page` |
| **JS** | `assets/js/main.js` — append `M9.14 — Corp FAQ accordion` |
| **Copy authority** | [BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md](../copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md) |
| **Charter** | [SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md) |

---

## 3. Sections (live)

1. Hero — Pageintro H1 + Lead (Payment link)
2. Shipment points — 2 cards (Барнаул · МО Никольское 204)
3. Organization — BLOCK 01 + summary row
4. Receiving methods — BLOCK 03 H3 stack
5. Timeline — 7 steps SC-04
6. Packaging — BLOCK 05
7. Coverage — BLOCK 06
8. Outcomes — BLOCK 07 (7 rows)
9. Transport companies — TK table (supporting)
10. FAQ — 8-item accordion SC-08
11. CTA + form — Commercial Trust architecture SC-09/SC-10

**Forbidden (verified absent):** map · calculator · TK logos · Басовская address · mid-page submit

---

## 4. Rollback

| Priority | File | Backup |
|----------|------|--------|
| P1 | `delivery.twig` | `backups/delivery.twig.pre-m9.14-delivery.bak` |
| P2 | `delivery.php` | `backups/delivery.php.pre-m9.14-delivery.bak` |
| P3 | `style.css` | `backups/style.css.pre-m9.14-delivery.bak` |
| P4 | `main.js` | `backups/main.js.pre-m9.14-delivery.bak` |
| P5 | `oc_seo_url` | Pre-deploy query in `reports/m9.14-work/deploy-manifest.json` |

---

## 5. Evidence

| Artifact | Path |
|----------|------|
| Implementation report | [SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md](../reports/SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md) |
| Deploy manifest | [reports/m9.14-work/deploy-manifest.json](../reports/m9.14-work/deploy-manifest.json) |
| Preflight manifest | [reports/m9.14-work/preflight-manifest.json](../reports/m9.14-work/preflight-manifest.json) |
| QA HTML | [reports/m9.14-work/qa-delivery.html](../reports/m9.14-work/qa-delivery.html) |
| QA screenshots | [qa/m9.14-delivery-screenshots/](../qa/m9.14-delivery-screenshots/) |

---

## 6. Operator gates (unchanged)

| Gate | Status | Note |
|------|--------|------|
| B1 МО address | **OPEN** | Live uses copy v1.1 Никольское 204 |
| B6/B8 sign-off | **OPEN** | Implementation uses copy v1.1 |

---

*Checkpoint registration — documentation + deploy evidence. Recovery remains CLOSED.*
