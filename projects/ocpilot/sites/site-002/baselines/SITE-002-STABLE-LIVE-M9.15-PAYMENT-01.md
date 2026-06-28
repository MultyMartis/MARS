# SITE-002 — Stable Live M9.15 Payment Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-M9.15-PAYMENT-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/payment-methods  
**Registered at:** 2026-06-28  
**Mode:** Stable live checkpoint — `/payment-methods` page domain only

---

## 1. Authority state

**Checkpoint:** `SITE-002-STABLE-LIVE-M9.15-PAYMENT-01`

**Scope:** Corporate page `/payment-methods` only — does **not** supersede M9.14 Delivery or M9.13 About baselines elsewhere.

**Parent authority (site-wide):** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` remains active for all non-payment domains.

---

## 2. Live surface

| Item | Value |
|------|--------|
| **URL** | https://zpm.new-site.space/payment-methods |
| **Route** | `information/payment` |
| **SEO keyword** | `payment-methods` → `information/payment` (`oc_seo_url` id 1045) |
| **Controller** | `catalog/controller/information/payment.php` |
| **Twig** | `catalog/view/theme/default/template/information/payment.twig` |
| **CSS** | `assets/css/style.css` — block `M9.15 — Payment page — corporate settlement` |
| **JS** | `assets/js/main.js` — corp FAQ accordion extended for `[data-payment-faq]` |
| **Copy authority** | [BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md](../copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md) |
| **Design authority** | [BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md) |

---

## 3. Sections (live)

1. Hero — Pageintro H1 + Lead (Contacts / Delivery links)
2. Payment timeline — 6 steps SC-04 (step 6 = Подготовка к отгрузке → Delivery handoff)
3. Payment methods — BLOCK 02 (безнал primary + summary table)
4. Documents received — BLOCK 04 proof cards (5)
5. Legal company information — entity facts + Contacts link
6. FAQ — 8-item accordion SC-08
7. CTA + form — Commercial Trust architecture (company field required)

**Forbidden (verified absent in `<main>`):** bank widgets · payment logos · QR · Moscow warehouse detail · TK/logistics tables · delivery timeline duplication

---

## 4. Rollback

| Priority | File | Backup |
|----------|------|--------|
| P1 | `payment.twig` | `backups/payment.twig.pre-m9.15-payment.bak` |
| P2 | `payment.php` | `backups/payment.php.pre-m9.15-payment.bak` |
| P3 | `style.css` | `backups/style.css.pre-m9.15-payment.bak` |
| P4 | `main.js` | `backups/main.js.pre-m9.15-payment.bak` |
| P5 | `oc_seo_url` | Pre-deploy query in `reports/m9.15-work/deploy-manifest.json` |

---

## 5. Evidence

| Artifact | Path |
|----------|------|
| Implementation report | [SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md](../reports/SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md) |
| Deploy manifest | [reports/m9.15-work/deploy-manifest.json](../reports/m9.15-work/deploy-manifest.json) |
| Preflight manifest | [reports/m9.15-work/preflight-manifest.json](../reports/m9.15-work/preflight-manifest.json) |
| QA HTML | [reports/m9.15-work/qa-payment.html](../reports/m9.15-work/qa-payment.html) |
| QA screenshots | [qa/m9.15-payment-screenshots/](../qa/m9.15-payment-screenshots/) |

---

## 6. Operator gates (unchanged)

B6 Design Charter approval · B8 Copy sign-off · B1 МО address · B3 Dealers PLP — **not blocking** this page-domain checkpoint.
