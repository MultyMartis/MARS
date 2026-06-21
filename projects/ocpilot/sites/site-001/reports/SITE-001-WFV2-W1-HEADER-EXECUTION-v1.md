# SITE-001 WF-V2-W1 Hybrid Header Execution v1

**Type:** Execution report — WF V2 Wave 1 Hybrid Header  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-WFV2-W1-2026-06-10  
**Backup:** `pre-wfv2-w1-header-20260610-0216`

---

## Summary

WF-V2-W1 deployed to TEST: **hybrid header system** — light contact rail + dark primary band + light promo strip. Phone/WhatsApp **removed** from primary band CTA cluster. Original logo restored (`img/logo.svg`, no invert filter). WF-V2-W1 CSS block appended (~320 lines main + ~90 lines media). **8/8** verification URLs **PASS**. Interaction audit **11/11 PASS**. W5-C Used PDP markers **preserved**. No PHP/JS/DB/product.twig changes.

---

## Pre-write artefacts

| Artefact | Status |
|----------|--------|
| [SITE-001-WFV2-W1-HEADER-WRITE-CHARTER-v1.md](SITE-001-WFV2-W1-HEADER-WRITE-CHARTER-v1.md) | **ACTIVE** |
| [SITE-001-WFV2-W1-HEADER-CHANGE-REQUEST-v1.md](SITE-001-WFV2-W1-HEADER-CHANGE-REQUEST-v1.md) | CR-SITE-001-WFV2-W1-2026-06-10 |
| [SITE-001-WFV2-W1-HEADER-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W1-HEADER-ROLLBACK-PLAN-v1.md) | **CREATED** |
| Backup `pre-wfv2-w1-header-20260610-0216` | **DONE** — manifest present |

---

## HITL decision applied

| Option | Status |
|--------|--------|
| Pure light header (spec `02`) | **NOT implemented** |
| Current graphite W5-A header | **NOT retained** |
| **Hybrid** (light rail + dark band + light promo) | **IMPLEMENTED** |

---

## Files modified (TEST FTP)

| File | Pre bytes | Post bytes | Delta |
|------|-----------|------------|-------|
| `header.twig` | 12,750 | 12,443 | Hybrid shell; phone/WA removed from CTA cluster; `wfv2-header` hooks |
| `css/main.css` | 173,031 | 183,183 | +WF-V2-W1 block (~320 lines) |
| `css/media.css` | 44,591 | 47,129 | +WF-V2-W1 responsive block |

**Not modified:** `product.twig`, `footer.twig`, PHP, JS, DB

**Working copy:** `.recovery-temp/site-001-wfv2-w1-work/`  
**Result JSON:** `.recovery-temp/site-001-wfv2-w1-result.json`

---

## Twig changes

| Zone | Change |
|------|--------|
| `<header>` | Added `wfv2-header wfv2-header--hybrid` |
| Contact rail | Restructured as flat info line with `wfv2-contact-rail__*` hooks; thin separators |
| Primary band logo | `img/logo.svg` (original brand asset) |
| CTA cluster | **Callback only** — removed `.w5a-cta--secondary.phone_btn` and `.w5a-cta--supportive.whatsapp_btn` |
| Nav / offcanvas | **Unchanged** — all menu links, «Услуги», «Ещё», mobile offcanvas preserved |

---

## CSS changes (WF-V2-W1 block)

| Zone | Target |
|------|--------|
| Contact rail | `#F7F8FA` bg · `#6B7280` text · thin `#E5E7EB` dividers · no capsules/cards |
| Primary band | `#1A2332` flat dark · centered white nav · single red CTA `#E60000` |
| Logo | `filter: none` — original logo visible |
| Promo strip | `#F3F4F6` light neutral · no dark inset · marquee fade masks removed |
| Dropdowns | Flat panel · minimal shadow · hover/focus preserved |
| Header | `position: static` — no sticky |

---

## Verification matrix

| URL | HTTP | Markers | Result |
|-----|------|---------|--------|
| `/` | 200 | All present; no `w5a-cta--secondary/supportive` | **PASS** |
| `/about` | 200 | All present | **PASS** |
| `/contact/` | 200 | All present + form | **PASS** |
| `/cars/` | 200 | All present | **PASS** |
| `/cars/bmw/` | 200 | All present | **PASS** |
| `/auto/` | 200 | All present | **PASS** |
| `/auto/haval/` | 200 | All present | **PASS** |
| `/audi-a1-2012-s-probegom-149-000-km-799` | 200 | W5-C preserved | **PASS** |

**CSS live:** `main.css` 183,183 bytes · `WF-V2-W1` marker **YES** · W5-C marker **YES**

---

## Interaction audit

| Check | Result |
|-------|--------|
| Logo src `logo.svg` | **PASS** |
| Logo no invert filter | **PASS** (`filter: none`) |
| Phone in contact rail | **PASS** |
| Phone NOT in primary band | **PASS** |
| WhatsApp NOT in primary band | **PASS** |
| Callback in primary band | **PASS** |
| «Услуги» dropdown hover | **PASS** (opacity 1) |
| «Ещё» dropdown hover | **PASS** (opacity 1) |
| No sticky header | **PASS** (`position: static`) |
| Promo no overlap | **PASS** (promo bg `rgb(243, 244, 246)`) |
| Mobile offcanvas | **PASS** |

**Overall automated:** **PASS**

---

## Screenshots

**Path:** `projects/ocpilot/sites/site-001/qa/wfv2-w1-header-screenshots/`

| Phase | Desktop | Mobile |
|-------|---------|--------|
| Before | homepage, used_pdp, used_catalog, about | homepage, used_pdp, used_catalog, about |
| After | homepage, used_pdp, used_catalog, about | homepage, used_pdp, used_catalog, about |

---

## Cache operations

| Action | Status |
|--------|--------|
| cache_system | 200 |
| cache_modification | 200 |
| cache_image | 200 |
| modification_refresh | 200 |

---

## Rollback

T1: Restore from `pre-wfv2-w1-header-20260610-0216` → [SITE-001-WFV2-W1-HEADER-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W1-HEADER-ROLLBACK-PLAN-v1.md)

---

## Authorization

| Action | Status |
|--------|--------|
| Commit | **NOT AUTHORIZED** |
| Push | **NOT AUTHORIZED** |
| Production | **NOT AUTHORIZED** |

**Next gate:** Operator 3-second visual HITL vs concept mock `01` → accept WF-V2-W1 or T1 rollback.
