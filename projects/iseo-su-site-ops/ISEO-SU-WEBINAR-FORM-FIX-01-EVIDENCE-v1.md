# ISEO-SU-WEBINAR-FORM-FIX-01 — Evidence v1

**Task:** `ISEO-SU-SITE-OPS-WEBINAR-FORM-FIX-01`  
**Lane:** ISEO-SU-SITE-OPS — WEBINAR FORM FAILURE DIAGNOSIS + FIX 01  
**Date:** 2026-09-09  
**Live URL:** `https://i-seo.su/webinar-seo-podryadchik.html`  
**Handler:** `/page__FORM.php`  
**FINAL STATUS:** COMPLETE — WEBINAR REGISTRATION FORM FIXED / ROOT CAUSE PROVEN / SECURITY PRESERVED

---

## 1. Operator Reproduction

Operator submitted the live webinar form with:

- name filled;
- phone filled;
- message filled;
- consent checkbox checked.

Visible UI after submit:

> Не удалось отправить заявку. Проверьте заполнение формы и попробуйте ещё раз.

This wave reproduced the same generic failure against live production before mutation.

## 2. Live Network Reproduction

Do **not** guess from HTML only. Live request captured before the production HTML patch.

| Item | Value |
|------|--------|
| Form `action` | `#` (shared JS posts relative `page__FORM.php`) |
| Form `method` | `post` |
| JS submit handler | shared `js/common.js` (`#page__FORM_seo` / `#page__FORM_send_seo` family) |
| Request URL | `https://i-seo.su/page__FORM.php` |
| Request method | `POST` |
| Content type | `application/x-www-form-urlencoded` (XHR) |
| Visible tel `name` before fix | `pf_contact` |
| `pf_phone` before fix | **absent** |
| Consent field | `personal_data_consent=1` present in markup |
| Honeypot | `contact_company_url` empty (JS-injected) |
| HMAC/timing | `iseo_ft` / `iseo_fs` / `iseo_fid` from `/iseo-form-token.php` |
| HTTP status | **200** |
| Response body | `false` |
| Response content type | `text/plain; charset=utf-8` |
| JS parser | success only if `xhr.responseText.trim() === "true"`; otherwise generic failure UI |
| Console | no form-handler JS exception; unrelated CRM tracker `409` exists site-wide |

**FAILURE STAGE:** **E. HANDLER BUSINESS REJECTION**

Not A/B/C (request was sent). Not D (HTTP 200). Not G (body is `false`, not a success parse miss). Handler rejected the payload as `required` because `pf_phone` was empty.

## 3. Working Form Comparison

The webinar rebuild cloned visual markup from:

`https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html`

That source page uses the same **broken** `free_audit` SEO clone (`#page__FORM_seo`, tel named `pf_contact`, no `pf_phone`). It is **not** a proven working submit path. This wave did **not** expand to fix restaurant / `content-form-seo.php`.

**Working reference:** homepage `#page__FORM` family and the original webinar landing contract (`pf_name`, hidden `pf_contact` method, visible `pf_phone`).

| WORKING FORM FIELD | WEBINAR FORM FIELD (before) | MATCH? | REQUIRED BY HANDLER? | RESULT |
|--------------------|------------------------------|--------|----------------------|--------|
| `pf_name` | `pf_name` | YES | YES | OK |
| `pf_contact` (method: WhatsApp/Telegram/email) | visible tel `name="pf_contact"` | **NO** | YES as **method** | phone string stored as method; contact empty |
| `pf_phone` (actual contact) | **missing** | **NO** | **YES** | reject `required` |
| `pf_site` | `WEBINAR SEO CONTRACTOR 2026-09` | YES | marker | OK |
| `pf_comment` | `pf_comment` | YES | optional | OK |
| `personal_data_consent=1` | `personal_data_consent` value `1` | YES | YES exact `"1"` | OK if posted |
| `contact_company_url` | JS honeypot | YES | must be present empty | OK |
| `iseo_ft` / `iseo_fs` / `iseo_fid` | shared JS | YES | HMAC/timing | OK |
| form id `#page__FORM_seo` | `#page__FORM_seo` | YES | JS binding | OK |
| submit `#page__FORM_send_seo` | `#page__FORM_send_seo` | YES | JS binding | OK |

After fix, webinar matches the homepage/original-webinar **field contract** while keeping the existing visual clone (same IDs/classes).

## 4. Handler Contract

Canonical handler: `/page__FORM.php` (unchanged this wave).

| Slot | Contract |
|------|---------|
| REQUIRED FIELDS | `pf_name`; contact method via `pf_contact` (or typo alias `pf_ontact`); actual contact via `pf_phone`; consent `personal_data_consent` exact `"1"` |
| OPTIONAL FIELDS | `pf_comment`; page title/link markers |
| CONSENT FIELD | `personal_data_consent` must be exact `"1"` (client + server) |
| HONEYPOT FIELD | `contact_company_url` must be present and empty |
| HMAC/TIMING FIELDS | `iseo_ft`, `iseo_fs`, `iseo_fid`; min-fill ~3s |
| FORM TYPE / PF_SITE | `pf_site` is a marker string; webinar uses `WEBINAR SEO CONTRACTOR 2026-09` |
| SUCCESS RESPONSE | HTTP 200, body `true` (`accept`) |
| VALIDATION ERROR RESPONSE | HTTP 200, body `false` (classes include `required`, `consent`, …) |
| MAIL FAILURE RESPONSE | body `false` (mail class); not observed on isolated accept path |

HMAC secret is production-local (`.iseo-form-runtime/iseo-form-secrets.local.php`). **Not printed.** Committed config `hmac_secret => null` is expected.

## 5. Root Cause

**ROOT CAUSE:** Webinar markup (rebuild-01 clone of SEO `free_audit`) uses `pf_contact` as the visible phone field and omits `pf_phone`, while `/page__FORM.php` + the homepage `#page__FORM` family require `pf_contact` = contact method and `pf_phone` as the actual contact, so the handler rejects (`required`) with body `false` and shared JS shows the generic failure.

## 6. Fix

Smallest correct fix: restore the proven homepage/original-webinar field contract **in webinar markup only**.

```html
<input type="hidden" name="pf_contact" value="WhatsApp">
<input type="tel" id="pf_contact" name="pf_phone" placeholder="WhatsApp / Telegram" required>
```

- Hidden method has **no** `id`.
- Visible tel keeps `id="pf_contact"` (CSS does not target that id as a field name).
- Method value `WhatsApp` matches homepage option + `iseo_form_contact_ok` WhatsApp branch.
- Handler **not** changed.
- Shared JS **not** changed.
- Restaurant clone **not** changed.
- HMAC / honeypot / min-fill / rate limit / duplicate / consent **not** weakened.

Canonical source: `production-source/static-html/webinar-seo-podryadchik.html` (form snippet only).

**Date:** git origin source already had **10 сентября 2026** (`adbdbe42`). Production HTML was byte-patched on the tel-field core only; date-10 count unchanged. A local untracked leftover still had 3 сентября and was **not** deployed or committed.

## 7. Backup

Root: `X:\AI MARS\local\sites\iseo-su-production\_webinar-form-fix-01\`

| ABSOLUTE PATH | SHA-256 BEFORE | TIMESTAMP |
|---------------|----------------|-----------|
| `...\webinar-seo-podryadchik.html.before.20260909T094748Z` | `2434e990b08b6765fd0e475d203671f34acf77222447d03c48a43b49758c4382` | `2026-09-09T09:47:48Z` (13711 bytes) |
| `...\iseo-form-config.php.before.20260909T094748Z` | `d4e394f3a8dd725f526e6c195d290b6cb2ad46a8f27e1b8021d5769567d5ecb7` | `2026-09-09T09:47:48Z` |

Config backed up because isolated `test_mode` was toggled ON then restored OFF. Persistent production recipient block was not rewritten as the fix.

## 8. Deploy

| Item | Value |
|------|--------|
| Mode | exact HTML field patch (not full-file sync) |
| SHA-256 after | `f5e7d6029faeda9cabae7502a34ad716c6700f1eb309c188372205ab64b14331` (13776 bytes) |
| Live after | `has_pf_phone` true; hidden WhatsApp true; date **10 сентября 2026** true; date 3 false; H1 unchanged |
| Helper | `tools/_webinar-form-fix-01-backup-deploy-validate.py` |
| Machine evidence | `evidence/webinar-form-fix-01/_deploy_validate.json` |

## 9. Positive Validation

Isolated `test_mode` ON (then restored OFF):

| Check | Result |
|-------|--------|
| HTTP | 200 |
| Body | `true` |
| Event class | `accept` |
| Posted keys include | `pf_phone`, `pf_contact=WhatsApp`, `personal_data_consent=1`, empty honeypot, HMAC trio |
| Test recipient | `im.work@mail.ru` only while `test_mode` ON |
| Production recipient used | **NO** |
| Playwright desktop 1440×900 | success UI «Успешно! Сообщение отправлено»; generic fail **absent** |
| POST from UI | `https://i-seo.su/page__FORM.php` 200 `true`; `has_pf_phone` true; consent `1`; honeypot empty |
| Mobile 390×844 | form present; H1 unchanged; screenshot captured |
| Console | two `409` on `https://lpt-crm.online/track` — pre-existing CRM tracker, not the form |

**MAIL DELIVERY:** isolated PHP `mail()` path reached `accept` to `im.work@mail.ru`. Operator inbox visual not independently confirmed. Production mail to `nikel007i33@yandex.ru` was **not** sent.

**FUNCTIONAL FIX VERIFIED THROUGH SERVER ACCEPTANCE / MAIL DELIVERY PROOF REQUIRES OPERATOR-APPROVED TEST SEND**

Screenshots:

- `evidence/webinar-form-fix-01/screenshots/desktop-1440x900-after-submit-202609090947496.png`
- `evidence/webinar-form-fix-01/screenshots/mobile-390x844-202609090947496.png`

## 10. Negative Validation

Rate-limit pause **310s** between burst-3 consent rejects and honeypot POST.

| Test | HTTP | Body | Event class | Expected |
|------|------|------|-------------|----------|
| Missing consent | 200 | `false` | `consent` | REJECT |
| `consent=0` | 200 | `false` | `consent` | REJECT |
| Malformed consent (`yes`) | 200 | `false` | `consent` | REJECT |
| Honeypot filled | 200 | `false` | `honeypot` | REJECT / anti-spam |

Valid structurally correct webinar payload: **ACCEPT** (`accept`) — see §9.

## 11. Security Regression

Live config hard check after finish (PHP `array()` parse, not the deploy JSON regex that missed recipients):

| Control | Final |
|---------|--------|
| NORMAL RECIPIENT | `nikel007i33@yandex.ru` |
| TEST MODE FINAL | OFF (`false`) |
| TEST RECIPIENT IN NORMAL ROUTING | NO |
| `im.work@nail.ru` | ABSENT |
| HMAC | ACTIVE (production-local secret; file null is expected) |
| HONEYPOT | ACTIVE |
| MIN-FILL | ACTIVE |
| RATE LIMIT | ACTIVE (burst 3 / 300s; pause used) |
| DUPLICATE PROTECTION | ACTIVE |
| CONSENT SERVER GUARD | ACTIVE |

Deploy JSON `cfg_*.prod_has_nikel: false` is a **regex bug** (`[]` vs `array()`), not evidence that the recipient was wiped.

## 12. UI Regression

| Check | Result |
|-------|--------|
| Design / layout | unchanged (field names/hidden input only) |
| Title / description / H1 / canonical | unchanged on live |
| Date / time | live **10 сентября 2026**, **19:00 МСК** unchanged |
| Menu / sitemap | unchanged |
| Nikita image | unchanged |
| Homepage smoke | 200; `pf_phone` + `pf_contact` select present |
| Restaurant page smoke | 200; `#page__FORM_seo` present (still clone family; **not** submitted / **not** fixed this wave) |

## 13. Production / Source Alignment

| Surface | Form contract | Date copy |
|---------|---------------|-----------|
| Live production | `pf_phone` + hidden `pf_contact=WhatsApp` | **10 сентября 2026** |
| Canonical source HTML (origin + this wave) | same form snippet | **10 сентября 2026** (unchanged this wave) |

**PRODUCTION/SOURCE ALIGNED:** YES (form contract and date).

## 14. Final Decision

**COMPLETE — WEBINAR REGISTRATION FORM FIXED / ROOT CAUSE PROVEN / SECURITY PRESERVED**

Handler unchanged. Shared JS unchanged. Security baseline preserved. Isolated accept proven. Production mail send to `nikel007i33@yandex.ru` requires operator-approved test.
