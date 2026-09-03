# ISEO-SU FORM CONSENT WAVE 01A — CALC RESULT PATCH EVIDENCE v1

**Task:** `ISEO-SU-SITE-OPS-FORM-CONSENT-WAVE-01A-CALC-RESULT-FORM-PATCH`  
**Date:** 2026-09-03  
**Site:** `https://i-seo.su/`  
**Decision:** **PASS / COMPLETE — WAVE 1 FULLY RECONCILED**

---

## 1. Scope

WAVE 01A only: mandatory personal-data consent on the SEO/tariff **calculator result lead UI** that appears after «Рассчитать». No WAVE 2 / WAVE 3.

## 2. What WAVE 1 missed

WAVE 1 covered real `<form>` contact surfaces. It did **not** cover the calculator **result** lead block:

- Class family: `.tariff-calc-request` inside `.tariff-calc-output__request`
- Pre-patch: bare inputs **without** `name`; CTA was `<a href="#callback">`; soft note only; **no** consent checkbox
- Hidden until JS shows the result panel after «Рассчитать» — operator-visible gap on e.g. `/services/seo.html`

This was a **pseudo-lead UI**, not a classic form inventory entry.

## 3. Source authority

| Role | Path |
|------|------|
| Canonical project source | `projects/iseo-su-site-ops/production-source/theme/iseoblog/template-parts/tarif-calc.php` |
| Production remote | `/home/n/nikel0rv/i-seo.su/public_html/wp-content/themes/iseoblog/template-parts/tarif-calc.php` |
| Page template (include) | `page-tariffcalc.php` → `tarif-calc.php` for `/tariff-calc` |
| Service pages | Hybrid routes (e.g. `/services/seo.html`) expand PHP includes into HTTP body |

**UNCOVERED CALCULATOR RESULT FORMS before patch:** 1 source file (single authority).  
**After patch:** **0** — one file covers the entire form-family (no duplicated markup copies).

## 4. Analog pages / instances

| Surface | Calculator result form present |
|---------|--------------------------------|
| `https://i-seo.su/services/seo.html` | YES (live HTTP) |
| `https://i-seo.su/tariff-calc` | YES (live HTTP) |
| `https://i-seo.su/` | NO |
| `https://i-seo.su/glossary/` | NO |
| `https://i-seo.su/blog/` | NO |

**CALCULATOR RESULT FORM INSTANCES:** 1 markup authority (`tarif-calc.php`) → N pages that include it.  
Live verified instances with consent UI: **2** URLs above. Family coverage is template-based, not per-page HTML forks.

## 5. Fix applied

### Markup (`tarif-calc.php`)

- Converted request block to real `<form id="callback__FORM_tariff_calc">`
- Fields: `cf_name`, `cf_phone`, hidden `cf_contact=Телефон`, hidden `cf_site=не указан`
- Consent: `personal_data_consent` value `1`, not prechecked, link `/privacy-policy.html`
- Submit: `<button type="button" id="callback__FORM_tariff_calc_send">` (replaces `#callback` anchor)

### Client (`js/common.js`)

- Delegated click → `checkEmptyFields()` (WAVE 1 consent gate) → POST `/callback__FORM.php`

### CSS

- `.tariff-calc-request__agree` + `button.tariff-calc-request__btn` in `css/main.css` and theme `style.css`

### Server

- **No new server layer.** Posts use existing `callback__FORM.php` → `iseo_form_guard_request("callback")` (WAVE 1 consent authority).
- HMAC / secret / antispam / rate / honeypot / recipients unchanged.

## 6. Backup

Root: `X:\AI MARS\local\sites\iseo-su-production\_form-consent-wave-01a-calc-result-patch\`  
Stamp: `20260903T112856Z`  
SHA256 before (examples):

| Production path | sha256_before |
|-----------------|---------------|
| `…/template-parts/tarif-calc.php` | `c237fa520e8332da943f1d92c165df724633744a8a5d30b1e43d949faa95f673` |
| `…/js/common.js` | `f27626b2c0c21bd8876b0524788916e14eb994dc9113cb60372eea3eb0e964f2` |
| `…/css/main.css` | `de2037b4195dec88c95bb94cfcdd6810884d48898c6e3fe0e851b38df6f03463` |
| `…/themes/iseoblog/style.css` | `d998ef3ae85d6d4509e8879da84cbc964182ca8c15d2345722a63d2f85718b4d` |

Receipt: `tools/_wave01a_deploy_validate.json`

## 7. Deploy + alignment

Four files uploaded; source SHA256 == remote after. **PRODUCTION/SOURCE ALIGNED: YES**

## 8. Validation

### UI (HTTP)

Consent markers present on `/services/seo.html` and `/tariff-calc`; old soft note gone; privacy link present.

### Client

`checkEmptyFields()` requires consent=`1` before AJAX (same WAVE 1 contract).

### Server negatives (`callback__FORM.php`)

| Case | Result |
|------|--------|
| without consent | REJECTED (`false`) |
| consent=`0` | REJECTED |
| consent=`false` | REJECTED |
| malformed | REJECTED |
| Mail on negatives | **0** |

### Positive

- Temporary `test_mode` ON → POST with consent=`1` → body `true`
- Recipient expected: `im.work@mail.ru` (test_recipients only)
- `test_mode` restored **false**
- Receipt: `tools/_wave01a_positive_retry.json` (2026-09-03T11:40:12Z)
- Note: first positive attempt failed due to burst rate-limit (3/300s) after negatives on same `callback` bucket; retry after 320s cooldown **PASS**

### Routing final

| Check | Value |
|-------|-------|
| production_recipients | `nikel007i33@yandex.ru` only (count 1) |
| im.work in production_recipients | NO |
| im.work@nail.ru | NO |
| test_mode | OFF |

## 9. Hard-check summary

```
UNCOVERED CALCULATOR RESULT FORMS: 0
CONSENT UI ADDED: YES
CONSENT REQUIRED CLIENT-SIDE: YES
CONSENT REQUIRED SERVER-SIDE: YES
DIRECT POST WITHOUT CONSENT: REJECTED
DIRECT POST CONSENT=0: REJECTED
DIRECT POST CONSENT=false: REJECTED
DIRECT POST MALFORMED: REJECTED
MAIL SENT ON NEGATIVE TESTS: 0
POSITIVE TEST: PASS
TEST MODE FINAL: OFF
HMAC CHANGED: NO
ANTISPAM CHANGED: NO
FORM REGRESSION: NONE
```

## 10. Roadmap

WAVE 1 Form Consent → **COMPLETE / RECONCILED** (via 01A).  
WAVE 2 / WAVE 3 → **not started**.
