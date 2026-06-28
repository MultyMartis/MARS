# SITE-002 — Stable Live M9.17 Warranty Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-M9.17-WARRANTY-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/guarantee  
**Registered at:** 2026-06-28  
**Mode:** Stable live checkpoint — `/guarantee` page domain only

---

## 1. Authority state

**Checkpoint:** `SITE-002-STABLE-LIVE-M9.17-WARRANTY-01`

**Scope:** Corporate page `/guarantee` only — does **not** supersede M9.14 Delivery, M9.15 Payment, or M9.13 About baselines elsewhere.

**Parent authority (site-wide):** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` remains active for all non-warranty domains.

---

## 2. Live surface

| Item | Value |
|------|--------|
| **URL** | https://zpm.new-site.space/guarantee |
| **Route** | `information/guarantee` |
| **SEO keyword** | `guarantee` → `information/guarantee` (`oc_seo_url` id 1048; prior `information_id=11`) |
| **Controller** | `catalog/controller/information/guarantee.php` |
| **Twig** | `catalog/view/theme/default/template/information/guarantee.twig` |
| **CSS** | `assets/css/style.css` — block `M9.17 — Warranty page — manufacturer service reassurance` |
| **JS** | `assets/js/main.js` — corp FAQ accordion extended for `[data-warranty-faq]` |
| **Copy authority** | [BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md](../copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md) |
| **Design authority** | [BZPM-M9.17-WARRANTY-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.17-WARRANTY-DESIGN-CHARTER-v1.md) |

---

## 3. Sections (live)

1. Hero — Pageintro H1 + Lead (About + Delivery links)
2. Warranty principles + coverage — BLOCK 01 (5-row outcome table + 4-label summary row)
3. Document checklist — BLOCK 02 (6 rows SC-06)
4. Claim procedure — BLOCK 03 (5-step SC-04 timeline — page spine)
5. Verification cases — BLOCK 04 (7 calm bullets — subordinate weight)
6. Service outcomes — BLOCK 05 (6 outcome rows)
7. FAQ — 8-item accordion SC-08 (`data-warranty-faq`)
8. CTA + form — Commercial Trust architecture (`equipment_model` + `comment` required)

**Forbidden (verified absent in `<main>`):** term badge · ASC map · red exclusion alerts · warranty certificate hero · photo upload · mid-page primary submit · TK tables · payment bodies

**OQ-DC-W03 decision:** Summary row only — trust strip **not** duplicated above fold.

---

## 4. Rollback

| Priority | File | Backup |
|----------|------|--------|
| P1 | `oc_seo_url` guarantee row | Pre-deploy in [deploy-manifest.json](../reports/m9.17-work/deploy-manifest.json) (`information_id=11`) |
| P2 | `guarantee.twig` | Remove remote file (was new) |
| P3 | `guarantee.php` | Remove remote file (was new) |
| P4 | `style.css` | `backups/style.css.pre-m9.17-warranty.bak` |
| P5 | `main.js` | `backups/main.js.pre-m9.17-warranty.bak` |

**Rollback order:** seo_url → remove guarantee.php/twig → restore style.css → restore main.js → clear twig cache.

---

## 5. Evidence

| Artifact | Path |
|----------|------|
| Implementation report | [SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md](../reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md) |
| Implementation charter | [SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md) |
| Deploy manifest | [reports/m9.17-work/deploy-manifest.json](../reports/m9.17-work/deploy-manifest.json) |
| Preflight manifest | [reports/m9.17-work/preflight-manifest.json](../reports/m9.17-work/preflight-manifest.json) |
| QA HTML | [reports/m9.17-work/qa-guarantee.html](../reports/m9.17-work/qa-guarantee.html) |
| QA screenshots | [qa/m9.17-warranty-screenshots/](../qa/m9.17-warranty-screenshots/) |

---

## 6. Operator gates (unchanged)

B6 Design Charter approval · B8 Copy sign-off · B2 warranty term (OQ-W01) · B1/B3 — **not blocking** this page-domain checkpoint unless operator requests term badge sync.
