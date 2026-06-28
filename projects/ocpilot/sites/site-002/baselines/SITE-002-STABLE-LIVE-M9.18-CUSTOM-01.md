# SITE-002 — Stable Live M9.18 Custom Manufacturing Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/custom-equipment  
**Registered at:** 2026-06-28  
**Mode:** Stable live checkpoint — `/custom-equipment` page domain only

---

## 1. Authority state

**Checkpoint:** `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01`

**Scope:** Corporate page `/custom-equipment` only — does **not** supersede M9.13 About, M9.14 Delivery, M9.15 Payment, M9.17 Warranty, or M9.16 Dealers baselines elsewhere.

**Parent authority (site-wide):** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` remains active for all non-custom-manufacturing domains.

**Program note:** M9.18 is the **terminal** Corporate Pages Program implementation milestone on TEST. Corp implementation phase for M9.14–M9.18 is **complete** (About restoration separate) — pending operator gates B6/B8 for formal sign-off.

---

## 2. Live surface

| Item | Value |
|------|--------|
| **URL** | https://zpm.new-site.space/custom-equipment |
| **Route** | `information/custom_equipment` |
| **SEO keyword** | `custom-equipment` → `information/custom_equipment` (`oc_seo_url` id 1042; prior `information_id=14`) |
| **Legacy CMS** | OpenCart Information entry id **14** — **orphaned, not deleted** (rollback) |
| **Controller** | `catalog/controller/information/custom_equipment.php` |
| **Twig** | `catalog/view/theme/default/template/information/custom_equipment.twig` |
| **CSS** | `assets/css/style.css` — block `M9.18 — Custom Manufacturing page — manufacturer capability` |
| **JS** | `assets/js/main.js` — corp FAQ accordion extended for `[data-custom-faq]` |
| **Copy authority** | [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md](../copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md) |
| **Design authority** | [BZPM-M9.18-CUSTOM-MANUFACTURING-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.18-CUSTOM-MANUFACTURING-DESIGN-CHARTER-v1.md) |

---

## 3. Sections (live)

1. Hero — Pageintro H1 + Lead (manufacturer capability frame)
2. When custom needed — BLOCK 01 triggers + scope note
3. Task matrix — BLOCK 02 (7-row SC-07 table)
4. What we can make — BLOCK 03 scope groups + in/out table
5. OEM capability — BLOCK 04 (5× H3 + proof strip + production image)
6. Process timeline — BLOCK 05 (**8-step SC-04** — dominant) + approval gate badge
7. Requirements — BLOCK 06 (9-row checklist) + BLOCK 07 materials prose
8. Project outcomes — BLOCK 08 (5-row table — second emphasis)
9. FAQ — 8-item accordion SC-08 (`data-custom-faq`)
10. CTA + form — Commercial Trust architecture (charter field lock, **no upload**)

**Forbidden (verified absent in `<main>`):** calculator/configurator · file upload · price/lead badges · SKU grid · fake case gallery · tender wizard · mid-page primary submit · universal AISI table hero

**OQ-DC-C21 decision:** Approval gate badge on timeline — value chips **not** used.

**OQ-DC-C25 decision:** Production image reused from About — `/assets/img/about-page-img.jpg`.

---

## 4. Rollback

| Priority | File | Backup |
|----------|------|--------|
| P1 | `oc_seo_url` custom-equipment row | Pre-deploy in [deploy-manifest.json](../reports/m9.18-work/deploy-manifest.json) (`information_id=14`) |
| P2 | `custom_equipment.twig` | Remove remote file (was new) |
| P3 | `custom_equipment.php` | Remove remote file (was new) |
| P4 | `style.css` | `backups/style.css.pre-m9.18-custom.bak` |
| P5 | `main.js` | `backups/main.js.pre-m9.18-custom.bak` |

**Rollback order:** seo_url → remove custom_equipment.php/twig → restore style.css → restore main.js → clear OpenCart + twig cache.

---

## 5. Evidence

| Artifact | Path |
|----------|------|
| Implementation report | [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md](../reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md) |
| Implementation charter | [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md) |
| Deploy manifest | [reports/m9.18-work/deploy-manifest.json](../reports/m9.18-work/deploy-manifest.json) |
| Preflight manifest | [reports/m9.18-work/preflight-manifest.json](../reports/m9.18-work/preflight-manifest.json) |
| QA HTML | [reports/m9.18-work/qa-custom-equipment.html](../reports/m9.18-work/qa-custom-equipment.html) |
| QA screenshots | [qa/m9.18-custom-screenshots/](../qa/m9.18-custom-screenshots/) |

---

*Stable checkpoint — forward progress only. Corporate Pages Program implementation phase on TEST is complete pending operator B6/B8.*
