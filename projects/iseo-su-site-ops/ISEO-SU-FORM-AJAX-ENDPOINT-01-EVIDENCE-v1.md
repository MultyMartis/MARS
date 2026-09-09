# ISEO-SU FORM AJAX ENDPOINT 01 — EVIDENCE v1

**Task:** `ISEO-SU-SITE-OPS-FORM-AJAX-ENDPOINT-01`  
**Date:** 2026-09-09  
**Branch decision:** **B — DEFECT PROVEN**  
**Final status:** FORM AJAX ENDPOINT FIX 01 COMPLETE — RELATIVE ENDPOINT DEFECT CLOSED

Runtime truth is live production. Canonical editable JS mirror: `production-source/js/common.js`.

---

## 1. Decision gate

Playwright network capture **before any JS mutation** proved nested `/services/seo/*.html` pages POSTed to:

`https://i-seo.su/services/seo/page__FORM.php`

instead of canonical:

`https://i-seo.su/page__FORM.php`

Nested path exists (thin service-tree delegate) and returned HTTP 200 with honeypot body `false`, so the defect was silent.

**ROOT CAUSE:** jQuery `$.ajax({ url: 'page__FORM.php' })` in `#page__FORM_send_seo` resolves against the **document URL**, not the script URL. No `<base href>`. From `/services/seo/*.html` the browser posts to `/services/seo/page__FORM.php`.

WEBINAR lives at site root (`/webinar-seo-podryadchik.html`); relative `page__FORM.php` already resolved to `/page__FORM.php` there. Defect is **nested `/services/seo/` only**.

---

## 2. Live shared JS authority

| Field | Value |
|-------|-------|
| Canonical source | `X:\AI MARS\projects\iseo-su-site-ops\production-source\js\common.js` |
| Live URL | `https://i-seo.su/js/common.js` |
| Remote docroot | `/home/n/nikel0rv/i-seo.su/public_html/js/common.js` |
| SHA-256 before this task | `5CCE01E7B75BF7D06B8FCE9842B694D865D22EB60D1BF41685ED5EB3AE3176C5` (len 100751) |
| SHA-256 after one-string fix | `B6D1F7E941DECDC89A6B0C5EF7A209BA9FFAEEB01A25110B0CA31707C9F892D8` (len 100752) |
| Production backup | `X:\AI MARS\local\sites\iseo-su-production\_form-ajax-endpoint-01\common.js.before.2026-09-09T122208Z` |
| Backup timestamp UTC | 2026-09-09T12:22:11Z |

Git HEAD `common.js` (without uncommitted WAVE 01A) is a **different** byte stream (`c4ac6b92…`). WAVE 01A lines were already live before this task and remain **foreign WIP** (not staged here). Production/source alignment for this task = live HTTP hash == working-tree `production-source/js/common.js`.

---

## 3. PHASE 1 — static forensic (`page__FORM.php` in live-authoritative `common.js`)

After the proven one-string fix (SEO handler only):

| Line | Exact code | Kind | Form family | Live-authoritative |
|------|------------|------|-------------|--------------------|
| 1089 | `url: 'page__FORM.php'` | relative | `#page__FORM_send` homepage | YES — left relative (HOME `/` still resolves canonically) |
| 1193 | `url: '/page__FORM.php'` | root-relative | `#page__FORM_send_info` blog/info | YES — already root-relative |
| 1622 | `url: 'page__FORM.php'` | relative | `#page__FORM_send_cases` | YES — not this defect |
| 1688 | `url: 'page__FORM.php'` | relative | `#page__FORM_send_services` | YES — not this defect |
| **1775** | `url: '/page__FORM.php'` | **root-relative (FIXED)** | `#page__FORM_send_seo` / `#page__FORM_seo` | YES |
| 1964 | `url: 'page__FORM.php'` | relative | `#page__FORM_send_adv` | YES — not this defect |
| 2128 | `url: 'page__FORM.php'` | relative | `#page__FORM_send_audit` | YES — not this defect |
| 2293 | `url: 'page__FORM.php'` | relative | `#page__FORM_send_develop` | YES — not this defect |
| 2447 | `url: 'page__FORM.php'` | relative | `#page__FORM_send_serm` | YES — not this defect |

HTML `action="#"`; JS owns POST. Markup: `content-form-seo.php`, webinar HTML, nested SEO landings. Button `#page__FORM_send_seo`.

No speculative sweep of other families. Nearby trap `audit__FORM.php` not touched.

---

## 4. PHASE 2–3 — pre-fix network proof

Method: Playwright; honeypot filled (`contact_company_url=https://honeypot.invalid`) so POST fires; server REJECTS (`body: "false"`); **no production mail**. Honeypot rejects occur before `iseo_form_rate_check`. JSON: `evidence/form-ajax-endpoint-01/_network-probe.json`. Started 2026-09-09T12:19:26Z.

JS file on all pages: `https://i-seo.su/js/common.js`. `base_href`: null.

| Page | URL | Endpoint string | Resolved POST | HTTP |
|------|-----|-----------------|---------------|------|
| HOME | `https://i-seo.su/` | relative `page__FORM.php` (homepage family) | `https://i-seo.su/page__FORM.php` | 200 / `false` |
| WEBINAR | `https://i-seo.su/webinar-seo-podryadchik.html` | relative in SEO handler (pre-fix) | `https://i-seo.su/page__FORM.php` | 200 / `false` |
| RESTAURANT | `https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html` | relative in SEO handler | **`https://i-seo.su/services/seo/page__FORM.php`** | 200 / `false` |
| CITY | `https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html` | relative | **nested** | 200 / `false` |
| NICHE | `https://i-seo.su/services/seo/prodvizhenie-internet-magazina-kosmetiki.html` | relative | **nested** | 200 / `false` |
| USA | `https://i-seo.su/services/seo/prodvizhenie-v-ssha.html` | relative | **nested** | 200 / `false` |
| UAE | `https://i-seo.su/services/seo/prodvizhenie-v-oae.html` | relative | **nested** | 200 / `false` |

Pre-submit `new URL('page__FORM.php', location.href)` matched actual POST URL.

---

## 5. PHASE 5–8 — one-string fix + scoped deploy

Delta in `#page__FORM_send_seo` only:

```
url: 'page__FORM.php'
→
url: '/page__FORM.php'
```

Deploy 2026-09-09T12:22:08Z–12:22:13Z. Only `js/common.js`. No HTML/PHP/CSS/menu/sitemap. Remote/live hashes match local after. JSON: `evidence/form-ajax-endpoint-01/_backup-deploy.json`.

Relative `page__FORM.php` remaining in live JS: **7** (other families). Root-relative `/page__FORM.php`: **2** (info + SEO).

---

## 6. PHASE 9 — post-deploy network proof

JSON: `evidence/form-ajax-endpoint-01/_network-probe-after.json`. Started 2026-09-09T12:26:50Z.

**ALL seven pages POSTed to `https://i-seo.su/page__FORM.php`** (200 / honeypot `false`). No nested `/services/seo/page__FORM.php` requests.

Nested pages still theoretically resolve *relative* `page__FORM.php` to the nested path (`browser_pre_submit.resolved_relative`); actual POST uses root-relative (`network.url`).

---

## 7. PHASE 10 — functional regression

Isolated `test_mode` ON only for valid accepts; recipient `im.work@mail.ru`; restored **OFF**.

| Test | Result |
|------|--------|
| Honeypot UI (restaurant) | POST canonical `/page__FORM.php`, 200 body `false`, fail UI — **REJECT** |
| Consent UI | client `checkEmptyFields` blocked POST (no network) — **REJECT** |
| Consent server POST (no `personal_data_consent`) | 200 body `false`; events `class=consent` 12:28:08Z — **REJECT / GUARD ACTIVE** |
| Valid webinar | events `accept`/`mail` 12:28:18Z |
| Valid restaurant | events `accept`/`mail` 12:28:32Z |
| Valid city | events `accept`/`mail` 12:33:56Z |
| Valid niche | events `accept`/`mail` 12:34:11Z |
| Valid homepage | Playwright POST `https://i-seo.su/page__FORM.php` 200 body `true`, success UI; events `accept`/`mail` 12:37:34Z |

First regression run crashed on homepage fill (`#page__FORM #page__FORM #pf_phone` composed locator). Wave1/wave2 accepts already landed; homepage resumed once. **No re-mail of webinar/restaurant/city/niche.**

`cfg_final.test_mode`: `"false"`. `prod_has_nikel`: true. `prod_has_im_work`: false.

---

## 8. PHASE 11 — shared JS console

Representative pages (home, `/services/seo.html`, restaurant, webinar): form present; **two** console `409` resource errors per page. Same 409 noise existed in the **pre-fix** probe. Not introduced by the one-string change. Submit bindings intact; no double-mail signal in events for the resume home submit.

---

## 9. PHASE 12 — security hard check

| Control | State |
|---------|-------|
| Normal recipient | `nikel007i33@yandex.ru` |
| test_mode final | OFF |
| Test recipient in normal routing | NO |
| HMAC | ACTIVE (token HTTP 200; accepts require token; tracked config `hmac_secret_null` is expected — secret is production-local) |
| Honeypot | ACTIVE |
| Min-fill | ACTIVE |
| Rate limit | ACTIVE |
| Duplicate protection | ACTIVE |
| Consent server guard | ACTIVE |
| Handler PHP | UNCHANGED (not deployed) |

---

## 10. PHASE 13 — SEO / design

No HTML/CSS/PHP/sitemap/menu/content deploy. TITLE / DESCRIPTION / H1 / CANONICAL / ROBOTS / SITEMAP / MENU / DESIGN / CSS / form field contract **unchanged**.

---

## 11. Machine evidence (in-repo)

- `evidence/form-ajax-endpoint-01/_network-probe.json`
- `evidence/form-ajax-endpoint-01/_network-probe-after.json`
- `evidence/form-ajax-endpoint-01/_backup-deploy.json`
- `evidence/form-ajax-endpoint-01/_regression.json`
- `tools/_form-ajax-endpoint-01-network-probe.py`
- `tools/_form-ajax-endpoint-01-backup-deploy.py`
- `tools/_form-ajax-endpoint-01-regression.py`
- `tools/_form-ajax-endpoint-01-regression-resume.py`

Production backup is **out of git** under `X:\AI MARS\local\sites\iseo-su-production\_form-ajax-endpoint-01\`.
