# REPORT — SITE-002 M9.15 PAYMENT IMPLEMENTATION

**Milestone:** M9.15 — Payment  
**Environment:** https://zpm.new-site.space/payment-methods  
**Branch:** `mars/canonical-post-recovery`  
**Date:** 2026-06-28  
**Checkpoint:** `SITE-002-STABLE-LIVE-M9.15-PAYMENT-01`

---

## 1. Safety preflight

| Check | Result |
|-------|--------|
| Repository | `C:\MARS Phenix\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `f2cec6cb` (matches expected) |
| Working tree | Unrelated modifications outside site-002 scope — **not touched** |
| Preflight manifest | [reports/m9.15-work/preflight-manifest.json](m9.15-work/preflight-manifest.json) |

**Authority note:** Dedicated file `SITE-002-M9.15-PAYMENT-IMPLEMENTATION-CHARTER-v1` was **not found in repo** at implementation time. Architecture followed: [BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md), [BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md](../copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md), M9.14 Delivery / Contacts / Commercial Trust patterns.

**Preflight note:** Remote `payment.php` and `payment.twig` existed (prior partial implementation); replaced by charter-aligned implementation. Prior M9.15 CSS block (`process-first redesign`) stripped and replaced.

---

## 2. Files modified

| Remote path | Action |
|-------------|--------|
| `catalog/controller/information/payment.php` | Replaced — meta, breadcrumbs, pageintro lead, bodyClass |
| `catalog/view/theme/default/template/information/payment.twig` | Replaced — 7-section page body |
| `assets/css/style.css` | Removed legacy M9.15 block; appended `zpm-payment-*` block (~7 KB) |
| `assets/js/main.js` | Replaced corp FAQ accordion block — added `[data-payment-faq]` |
| `oc_seo_url` keyword `payment-methods` | Confirmed `information/payment` (id 1045) |

---

## 3. Files created

| Path | Role |
|------|------|
| `reports/m9.15-work/payment.php` | Work copy controller |
| `reports/m9.15-work/payment.twig` | Work copy twig |
| `reports/m9.15-work/m9.15-payment-page.css` | CSS staging |
| `reports/m9.15-work/m9.15-corp-accordion.js` | JS staging (delivery + payment) |
| `reports/m9.15-work/m915-payment-deploy.py` | Deploy script |
| `reports/m9.15-work/m915-payment-screenshots.py` | Screenshot script |
| `reports/m9.15-work/deploy-manifest.json` | Post-deploy SHA256 |
| `reports/m9.15-work/preflight-manifest.json` | Pre-deploy SHA256 |
| `reports/m9.15-work/qa-payment.html` | Live HTML capture |
| `baselines/SITE-002-STABLE-LIVE-M9.15-PAYMENT-01.md` | Stable checkpoint |
| `qa/m9.15-payment-screenshots/*` | Viewport screenshots |
| `backups/payment.php.pre-m9.15-payment.bak` | Remote backup |
| `backups/payment.twig.pre-m9.15-payment.bak` | Remote backup |
| `backups/style.css.pre-m9.15-payment.bak` | Remote backup |
| `backups/main.js.pre-m9.15-payment.bak` | Remote backup |

---

## 4. Assets reused

| Pattern | Source |
|---------|--------|
| Commercial Trust CTA card | `zpm-commercial-trust__*` from M9.8.9 / Delivery |
| Contacts form | `zpm-form`, phone mask, email validate, consent |
| Pageintro shell | Delivery / Contacts internal pages |
| Corp timeline | `zpm-corp-timeline` from M9.14 Delivery CSS |
| Corp FAQ accordion | `zpm-corp-faq__*` from M9.14 Delivery CSS |
| Section titles | `section-title__like-h2`, `section-title__like-h3` |
| Decor logo | `/assets/img/decor-logo.svg` |

---

## 5. Deploy verification

| Item | Value |
|------|--------|
| Route | `information/payment` |
| Public URL | `/payment-methods` |
| Deploy script | `m915-payment-deploy.py` |
| Twig cache | Cleared (empty listing) |
| SEO patch | HTTP one-shot PHP patch — removed after run |

---

## 6. QA results

| Check | Result |
|-------|--------|
| HTTP 200 | PASS (desktop/tablet/mobile) |
| `zpm-payment-page` | PASS |
| Pageintro lead + Delivery link | PASS |
| 6 timeline steps | PASS |
| Step 6 «Подготовка к отгрузке» | PASS |
| Payment methods + table | PASS |
| 5 proof cards | PASS |
| Legal entity strip | PASS |
| 8 FAQ items | PASS |
| Company field required | PASS |
| CTA H2 exact match | PASS |
| Form title | PASS |
| No bank/QR widgets in main | PASS |
| No logistics/TK in main | PASS |
| Console errors | PASS (0) |
| Horizontal overflow | PASS (all viewports) |
| Meta title/description | PASS |

Full automated QA: [qa/m9.15-payment-screenshots/m9.15-payment-qa-results.json](../../qa/m9.15-payment-screenshots/m9.15-payment-qa-results.json)

---

## 7. Screenshots

| File |
|------|
| `qa/m9.15-payment-screenshots/m9.15-payment-desktop-1440-full.png` |
| `qa/m9.15-payment-screenshots/m9.15-payment-desktop-1440-timeline.png` |
| `qa/m9.15-payment-screenshots/m9.15-payment-tablet-1024-full.png` |
| `qa/m9.15-payment-screenshots/m9.15-payment-tablet-1024-timeline.png` |
| `qa/m9.15-payment-screenshots/m9.15-payment-mobile-390-full.png` |
| `qa/m9.15-payment-screenshots/m9.15-payment-mobile-390-timeline.png` |

---

## 8. Rollback

1. Restore `oc_seo_url` from `deploy-manifest.json` → `seo_url_patch_response.before`
2. Restore files from `backups/*.pre-m9.15-payment.bak`
3. Clear Twig template cache on TEST
4. Verify `/payment-methods` returns prior state

---

## 9. Stable checkpoint

**Registered:** `SITE-002-STABLE-LIVE-M9.15-PAYMENT-01`  
**Baseline doc:** [baselines/SITE-002-STABLE-LIVE-M9.15-PAYMENT-01.md](../baselines/SITE-002-STABLE-LIVE-M9.15-PAYMENT-01.md)

---

## 10. Risks

| Risk | Mitigation |
|------|------------|
| Form backend still `action="#"` (Contacts pattern) | No new backend — manager routing unchanged |
| Operator gates B6/B8 open | Copy/design from approved artefacts; HITL visual review recommended |
| Legacy payment page partially replaced | Backups in `backups/` + deploy manifest SHA256 |
| Global footer JS contains MO address in CITY_DATA | Out of scope — not rendered in payment `<main>` |

---

## 11. Operator review notes

- Visual HITL on TEST recommended: hero lead, 6-step timeline desktop grid, proof cards at 1310/1024/390.
- Step 6 intentionally stops at **Подготовка к отгрузке** with Delivery handoff — no shipment/logistics body on Payment page.
- BLOCK 03 (after-payment chain) and BLOCK 05 (audience matrix) omitted per task section list — copy pointers preserved in timeline step 6, FAQ, and CTA.
- Next in operator queue: **M9.17 Warranty**.

---

## Commit

**Message:** `feat(site-002): implement M9.15 Payment corporate page`  
**Push:** `mars/canonical-post-recovery` — YES (per task)
