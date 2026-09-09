# ISEO-SU-FORM-CONTRACT-REGRESSION-01 — Evidence v1

**Task:** `ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01`  
**Lane:** ISEO-SU-SITE-OPS — FORM CONTRACT REGRESSION AUDIT + FIX 01  
**Date:** 2026-09-09  
**Handler:** `/page__FORM.php`  
**FINAL STATUS:** COMPLETE — ISEO-SU FORM CONTRACT REGRESSION AUDIT + FIX / ALL PROVEN PF_CONTACT-PF_PHONE DEFECTS CLOSED

---

## 1. Proven contract (from WEBINAR FORM FIX 01)

Handler `/page__FORM.php` (unchanged this wave):

| Slot | Contract |
|------|----------|
| `pf_contact` | contact **method** (hidden or `<select>`), not the phone string |
| `pf_phone` | actual visible contact / phone |
| Consent | `personal_data_consent` exact `"1"` |
| Honeypot | `contact_company_url` present empty |
| HMAC/timing | `iseo_ft` / `iseo_fs` / `iseo_fid` |
| Success | HTTP 200, body `true` |
| Business reject | HTTP 200, body `false` |

**Broken family (audit target):** visible tel `name="pf_contact"` AND no `name="pf_phone"` AND POST to `/page__FORM.php`.

**Minimal fix (same as webinar):**

```html
<input type="hidden" name="pf_contact" value="WhatsApp">
<input type="tel" id="pf_contact" name="pf_phone" placeholder="WhatsApp / Telegram" required>
```

Hidden method has **no** `id`. Visible tel keeps `id="pf_contact"`. Existing method value preserved (`WhatsApp` on this family). Handler and `js/common.js` **not** changed.

---

## 2. Live inventory (before)

Helper: `tools/_form-contract-regression-01-inventory.py`  
Machine: `evidence/form-contract-regression-01/live-inventory.json`

| Metric | Value |
|--------|--------|
| URLs scanned | 146 |
| Live `/page__FORM.php` surfaces | **137** |
| PROVEN CONTRACT DEFECT | **90** |
| Healthy `/page__FORM.php` | 47 |

Restaurant live: `https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html` — `#page__FORM_seo` — **BROKEN** before.

Healthy (not patched): homepage `#page__FORM`, footer, webinar (already fixed), calculator/other handlers, hubs `adv.html` / `development.html` / `serm.html` / `contacts.html` / `reviews.html` / `cases.html` / `services.html`.

Exact 90 URLs: `affected_urls` in `live-inventory.json`.

---

## 3. Source authorities

Helpers: `tools/_form-contract-regression-01-discover.py`, `tools/_form-contract-regression-01-walk-targeted.py`  
Machine: `live-authorities.json`, `live-authority-walk.json`

Do **not** re-run `tools/_form-contract-regression-01-walk.py` (hung; killed).

| Metric | Value |
|--------|--------|
| Hits | 93 |
| Proven inline authorities (OLD_CORE) | **18** remote files |
| Include-only pages (inherit SEO include) | **75** |

### GROUP A — shared WP include (fixed once)

| Item | Path |
|------|------|
| Live | `/home/n/nikel0rv/i-seo.su/public_html/wp-content/themes/iseoblog/template-parts/content-form-seo.php` |
| MARS | `production-source/theme/iseoblog/template-parts/content-form-seo.php` |
| Form id | `#page__FORM_seo` |
| Extra field | `cf_agree21` **preserved** |
| SAFE SHARED FIX | **YES** |

City pages (СПб, Казань, Екатеринбург, Новосибирск, Красноярск), niche pages (питомник, СМИ, ресторан, запчасти, интернет-провайдер, косметика, цветы), USA/UAE, and other SEO clones using this include were **not** independently patched. They inherit GROUP A.

### GROUP B — independent inline OLD_CORE (18 live files)

1. `blog.html` — `#page__FORM_info`. Consent checkbox **ABSENT** (WAVE 01 residual). This wave did **not** invent consent UI. Client JS still blocks UI submit without consent; HTTP field contract is the audit target.
2. `blog-article.html` — OLD_CORE + consent. **Not** in the 90 live inventory URLs. Patched as clone-spread prevention.
3–17. Fifteen live inline service pages:

- `services/adv/google-adwords.html`, `medijnaya-reklama.html`, `yandeks-direkt.html`
- `services/audit/analiz-konkurentov.html`
- `services/development/optimizaciya-pod-mobilnye-ustrojstva.html`, `soprovozhdenie-sajta.html`, `sozdanie-sajta.html`, `tekhnicheskaya-optimizaciya.html`, `tekhnicheskaya-podderzhka.html`
- `services/serm/email-marketing.html`, `reklama-u-blogerov.html`, `reklama-v-telegram.html`, `smm.html`, `targetirovannaya-reklama.html`, `upravlenie-reputaciej.html`

Arithmetic vs 90 live URLs: 75 include-only + 15 live inline ≈ 90. `blog-article.html` is extra disk authority. `content-form-seo.php` is the shared include.

No MARS copies of the 15 live inline service files were invented.

---

## 4. Restaurant page

| Item | Value |
|------|--------|
| URL | `https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html` |
| Source | shared `content-form-seo.php` (GROUP A) |
| BEFORE | **BROKEN** (`pf_contact` as visible tel; no `pf_phone`) |
| AFTER | **HEALTHY** (GET + HTTP POST accept + UI success body `true`) |

---

## 5. Backup

Root: `X:\AI MARS\local\sites\iseo-su-production\_form-contract-regression-01\`  
Helper: `tools/_form-contract-regression-01-backup-patch.py`  
Machine: `evidence/form-contract-regression-01/_backup-patch.json`  
Timestamp: `2026-09-09T11:04:19Z` (ended `11:04:51Z`)

18 remote files backed up with SHA-256 before; then patched. Shared include SHA-256:

| Path | SHA-256 before | SHA-256 after |
|------|----------------|---------------|
| live `content-form-seo.php` | `1d49be880913cb31c60afc34af08cfd6e63997fc29f2ff14bf80267953967150` | `b57a5690f13070e7754f22cbf3665b616f69b6e391dcc311d99266fa0de28a4e` |
| MARS `content-form-seo.php` | (patched to match live after) | `b57a5690f13070e7754f22cbf3665b616f69b6e391dcc311d99266fa0de28a4e` |
| MARS `blog.html` | | `7e3402c978d5f82086e06ed92150b1189e35cceb133be6d951c88943f9d1c984` (matches live) |
| MARS `blog-article.html` | | `95977b787880ca74111628307a3824016763511acab03648749503cda8f4b4a5` |

Live `blog-article.html` after is `12e49f122a388b2adfe1996046b0966f24b0eb53c5d3aa389698f68ac6f4bd25` — **not byte-identical** besides this patch. Contract aligned; unrelated bytes not force-aligned.

---

## 6. GET rescan after patch

Helper: `tools/_form-contract-regression-01-rescan-after.py`  
Machine: `live-inventory-after.json`

| Metric | Value |
|--------|--------|
| URLs scanned | 95 (90 previously affected + extras) |
| `broken_after` | **0** |
| Restaurant | **HEALTHY** |

`PF_CONTACT MISUSED AS VISIBLE PHONE AFTER: 0`  
`PF_PHONE MISSING AFTER: 0` on previously broken `/page__FORM.php` surfaces (GET confirmed).

---

## 7. HTTP POST validation

Do **not** re-run the full POST sequence. Rate limit ≈3/5 min / ≈10/hour.

Proven via live `.iseo-form-runtime/events.log` (`form=page`, 2026-09-09 UTC):

| ts (UTC) | class | result |
|----------|--------|--------|
| 09:47:52 / 09:47:57 / 09:48:01 | consent | reject |
| 09:53:15 | honeypot | reject |
| 09:53:20 / 09:53:30 / 10:24:26 | accept | mail |
| 11:16:29 / 11:16:34 / 11:16:38 | consent | reject |
| 11:21:53 | honeypot | reject |
| 11:21:57 / 11:25:20 / 11:29:34 | accept | mail |

Isolated `test_mode` used where needed, then restored **OFF**. Production recipient `nikel007i33@yandex.ru` was **not** used for repeated operator mail.

---

## 8. Live UI smoke

Helper: `tools/_form-contract-regression-01-ui-smoke.py` (retry exit 0, ~59s)  
Machine: `_validate.json` keys `ui_restaurant_retry`, `ui_*_retry`  
Viewports: 1440×900 and 390×844

| Surface | Result |
|---------|--------|
| Restaurant desktop submit | `success_ui` **true**; generic fail **false**; POST HTTP 200 body **`true`**; `has_pf_phone` true; consent=1 |
| Restaurant mobile | form present; `pf_phone`; hidden `pf_contact`; tel not named contact |
| Adv / SERM / develop | form present; contract healthy both viewports |
| Homepage (unaffected) | `home_ok` / `pf_phone` + select method (original healthy contract) |
| Webinar (unaffected) | screenshots + GET healthy |

Console: only site-wide CRM tracker `409` (pre-existing; unrelated).

**Nested AJAX path (document; JS not changed):** restaurant UI AJAX posted to relative `https://i-seo.su/services/seo/page__FORM.php` because `common.js` uses relative `'page__FORM.php'`. That nested URL returned `true` with `pf_phone`. Canonical HTTP POST to `/page__FORM.php` already proved the handler. Pre-existing thin service-tree delegate. Out of this task.

---

## 9. Security preservation

| Control | Status |
|---------|--------|
| HMAC | **ACTIVE** (secret in `.iseo-form-secrets.local.php`; committed config `hmac_secret => null` expected) |
| Honeypot | **ACTIVE** |
| Min-fill | **ACTIVE** |
| Rate limit | **ACTIVE** |
| Duplicate protection | **ACTIVE** |
| Consent server guard | **ACTIVE** (events.log `consent`/`reject`) |
| Recipient | `nikel007i33@yandex.ru` |
| `test_mode` final | **OFF** |

Handler `/page__FORM.php`, `iseo-form-security.php`, `common.js` **not** weakened.

---

## 10. SEO / content / design

Title, description, H1, canonical, robots, sitemap, menu, content, design: **NO** mutations this wave. Field-name contract only.

---

## 11. Production / source alignment

| Authority | Aligned? |
|-----------|----------|
| `content-form-seo.php` live ↔ MARS | **YES** (SHA match) |
| `blog.html` live ↔ MARS | **YES** (SHA match) |
| `blog-article.html` | contract aligned; **not** byte-identical |
| 15 inline service HTML | live-only; no invented MARS copies |

---

## 12. Helpers and machine evidence

| Path | Role |
|------|------|
| `tools/_form-contract-regression-01-inventory.py` | live GET inventory |
| `tools/_form-contract-regression-01-discover.py` | template discover |
| `tools/_form-contract-regression-01-walk-targeted.py` | targeted authority walk |
| `tools/_form-contract-regression-01-backup-patch.py` | backup + patch |
| `tools/_form-contract-regression-01-rescan-after.py` | GET after |
| `tools/_form-contract-regression-01-validate.py` | POST/config helper |
| `tools/_form-contract-regression-01-ui-smoke.py` | Playwright UI |
| `evidence/form-contract-regression-01/` | JSON + screenshots |
