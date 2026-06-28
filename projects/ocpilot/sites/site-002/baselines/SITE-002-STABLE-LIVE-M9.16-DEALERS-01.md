# SITE-002 — Stable Live M9.16 Dealers Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-M9.16-DEALERS-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/dealers  
**Registered at:** 2026-06-28  
**Mode:** Stable live checkpoint — `/dealers` page domain only

---

## 1. Authority state

**Checkpoint:** `SITE-002-STABLE-LIVE-M9.16-DEALERS-01`

**Scope:** Corporate page `/dealers` only — does **not** supersede M9.13 About, M9.14 Delivery, M9.15 Payment, or M9.17 Warranty baselines elsewhere.

**Parent authority (site-wide):** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` remains active for all non-dealers domains.

**B3:** **OPEN** — PLP `blockdealersform.twig` reconciliation is **out of scope** for this checkpoint.

---

## 2. Live surface

| Item | Value |
|------|--------|
| **URL** | https://zpm.new-site.space/dealers |
| **Route** | `information/dealers` |
| **SEO keyword** | `dealers` → `information/dealers` (`oc_seo_url` id 1049; prior `information_id=10`) |
| **Controller** | `catalog/controller/information/dealers.php` |
| **Twig** | `catalog/view/theme/default/template/information/dealers.twig` |
| **CSS** | `assets/css/style.css` — block `M9.16 — Dealers page — manufacturer partnership` |
| **JS** | `assets/js/main.js` — corp FAQ accordion extended for `[data-dealers-faq]` |
| **Copy authority** | [BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md](../copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md) |
| **Design authority** | [BZPM-M9.16-DEALERS-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.16-DEALERS-DESIGN-CHARTER-v1.md) |

---

## 3. Sections (live)

1. Hero — Pageintro H1 + Lead (manufacturer partnership frame)
2. Partner matrix — BLOCK 01 (SC-13, 5 partner types)
3. OEM proof — BLOCK 02 (5× H3 + channel note)
4. OEM trust row — MICRO (manufacturer · ИНН · Барнаул · About)
5. Partner outcomes — BLOCK 03 (6-row table)
6. Cooperation process — BLOCK 04 (5-step SC-04 timeline)
7. Supply chain + cross-links — BLOCK 05 (4-node chain + 3-row table)
8. FAQ — 8-item accordion SC-08 (`data-dealers-faq`)
9. CTA + form — Commercial Trust architecture (`company` + `city` required, `dialog=7`)

**Forbidden (verified absent in `<main>`):** discount badges · territory map · franchise tiers · form-as-hero · СНГ geography · website field · ИНН field · mid-page primary submit

**OQ-DC-DE04 decision:** OEM trust row after BLOCK 02 — optional trust strip **not** duplicated.

---

## 4. Rollback

| Priority | File | Backup |
|----------|------|--------|
| P1 | `oc_seo_url` dealers row | Pre-deploy in [deploy-manifest.json](../reports/m9.16-work/deploy-manifest.json) (`information_id=10`) |
| P2 | `dealers.twig` | Remove remote file (was new) |
| P3 | `dealers.php` | Remove remote file (was new) |
| P4 | `style.css` | `backups/style.css.pre-m9.16-dealers.bak` |
| P5 | `main.js` | `backups/main.js.pre-m9.16-dealers.bak` |

**Rollback order:** seo_url → remove dealers.php/twig → restore style.css → restore main.js → clear OpenCart + twig cache.

**PLP rollback:** Not in M9.16 scope — `blockdealersform.twig` unchanged by design.

---

## 5. Evidence

| Artifact | Path |
|----------|------|
| Implementation report | [SITE-002-M9.16-DEALERS-IMPLEMENTATION.md](../reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION.md) |
| Implementation charter | [SITE-002-M9.16-DEALERS-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION-CHARTER-v1.md) |
| Deploy manifest | [reports/m9.16-work/deploy-manifest.json](../reports/m9.16-work/deploy-manifest.json) |
| Preflight manifest | [reports/m9.16-work/preflight-manifest.json](../reports/m9.16-work/preflight-manifest.json) |
| QA HTML | [reports/m9.16-work/qa-dealers.html](../reports/m9.16-work/qa-dealers.html) |
| QA screenshots | [qa/m9.16-dealers-screenshots/](../qa/m9.16-dealers-screenshots/) |

---

*Stable checkpoint — forward progress only. B3 PLP reconciliation remains a separate governed task.*
