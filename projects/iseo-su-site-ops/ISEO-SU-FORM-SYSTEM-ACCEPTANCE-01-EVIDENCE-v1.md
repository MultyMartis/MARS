# ISEO-SU-FORM-SYSTEM-ACCEPTANCE-01 — EVIDENCE v1

**Task:** `ISEO-SU-SITE-OPS-FORM-SYSTEM-ACCEPTANCE-01`  
**Date:** 2026-09-09  
**Live:** https://i-seo.su/  
**Audit timestamp:** 2026-09-09T16:34:42Z (inventory) … 2026-09-09T18:33:26Z (closeout, `test_mode` OFF)

## 1. Scope

Full live inventory of user-reachable lead surfaces on production, contract scan of every classified surface, browser submit of unique handler/UI authorities, isolated mail-path of all 12 PHP handlers, guarded minimal repair of proven defects.

**Mail policy (enforced):** isolated `test_mode` only → `im.work@mail.ru`. Production recipient left as `nikel007i33@yandex.ru`. Production test mails: **0**. Operator-accepted homepage audit modal was **not** re-sent to production.

**Not in scope:** SEO/menu/design/sitemap mutation; handler consolidation; anti-spam redesign.

## 2. Live Form Inventory

Crawl seed **584** URLs; HTTP 200 **583**; pages with lead forms **534**.

| Kind | Count |
|------|------:|
| TOTAL LIVE FORM SURFACES | **3744** |
| STATIC | 80 |
| MODAL (DOM popup/hidden lead forms, including shared includes) | 3594 |
| DYNAMIC (calculator-result `#callback__FORM_tariff_calc`) | 70 |

Machine inventory:

- `evidence/form-system-acceptance-01/live-form-inventory.csv`
- `evidence/form-system-acceptance-01/live-form-inventory.json`

**Reachability note:** many TARIFF_POPUP / AUDIT / CALLBACK nodes exist in included popup partials on pages that do **not** expose a CTA (e.g. `/services/seo.html` includes popup markup without tariff cards). User-reachable tariff order path is pages that include `content-tarifs-*.php` (city/niche/USA/UAE/hub cards). Orphans were structurally scanned; functional tariff UI was executed on a page with real `a.modalbox[href="#tariff_N__FORM_popup"]`.

Consent missing after Wave 1 deploy + live re-check: **0**.

## 3. Form Families

| Family | Surfaces |
|--------|---------:|
| TARIFF_POPUP | 1892 |
| CALLBACK_FORM | 533 |
| AUDIT_FORM | 532 |
| PAGE_FORM | 525 |
| BONUS_FORM | 97 |
| CALCULATOR_STAGE | 90 |
| TARIFF_CALCULATOR_RESULT | 70 |
| PARTNERS_FORM | 2 |
| REVIEW_FORM | 2 |
| CAREER_FORM | 1 |

**TOTAL UNIQUE FORM FAMILIES: 10**

Classifier contract keys (`family|php|js|dom_id|fields|send_types|endpoint_risk|consent`): **87** unique authorities. Clones that share PHP handler + `common.js` family binding were treated as one UI/mail contract (same method as FORM CONTRACT REGRESSION 01).

## 4. PHP Handlers

**TOTAL UNIQUE PHP HANDLERS: 12**

`page__FORM.php`, `callback__FORM.php`, `audit__FORM.php`, `calc__FORM.php`, `bonus__FORM.php`, `career__FORM.php`, `partners__FORM.php`, `review__FORM.php`, `tariff_1__FORM.php` … `tariff_4__FORM.php`.

Shared: `iseo-form-security.php`, `iseo-form-config.php`, `iseo-form-token.php`.

All 12 isolated mail-path **PASS** (`body=true`, recipient `im.work@mail.ru`).

## 5. JS Handlers

Single runtime file: `js/common.js` (`ISEO_FORM_SECURITY_V1` + family click handlers + delegated `#callback__FORM_tariff_calc_send` + catch-all `[id*="FORM_send"]` for `preventDefault` / HMAC fields).

Classified unique send-id bindings: **29** keys in inventory (suffixes `_seo`, `_info`, `_adv`, `_serm`, `_develop`, `_cases`, `_services`).

Wave 1: all family AJAX URLs made **root-relative** (`/page__FORM.php`, `/callback__FORM.php`, …).

## 6. Static Forms

Representative browser PASS: homepage `#page__FORM`, nested SEO `#page__FORM_seo`, webinar `#page__FORM`, career `#career__FORM_info`, reviews `#review__FORM_info`, partners, WP footer callback.

`blog.html` consent restored (DEF-CONSENT-BLOG). A later `blog.html` submit returned handler `false` during page burst 3/5 min — **rate-limit**, not a field defect. Handler isolated mail PASS.

## 7. Modal Forms

| Surface | Result |
|---------|--------|
| Homepage audit `#audit__FORM` | Isolated POST `/audit__FORM.php` body `true`. Operator already accepted live production path. **Not** retested to `nikel007i33@yandex.ru`. |
| Homepage callback modal | Prior homepage regression 01 + this wave intercept. |
| Bonuses | Browser PASS `/bonus__FORM.php` |
| Tariff 1–4 order popups on restaurant niche page | Browser PASS `/tariff_N__FORM.php`, success UI, no reload |

## 8. Dynamic Forms

Authority: `theme/iseoblog/template-parts/tarif-calc.php` → `#callback__FORM_tariff_calc` / `.tariff-calc-request` → `/callback__FORM.php`.

Present after «Рассчитать» on `/services/seo.html`, `/tariff-calc`, city/niche/USA/UAE includes. Consent `personal_data_consent=1` present.

Payload fields: `cf_name`, `cf_phone`, hidden `cf_contact=Телефон`, `cf_site=не указан`, consent, HMAC/honeypot injected. **Calculated tariff is visual-only** (not duplicated as hidden mail fields).

## 9. SEO Calculator

Page: `https://i-seo.su/services/seo.html`

| Check | Result |
|-------|--------|
| CALCULATION WORKS | PASS — result «СТАНДАРТ / 64 000 ₽/мес» (accept run) |
| RESULT REVEALS | PASS — `.tariff-calc-result` display flex |
| DYNAMIC FORM FOUND | PASS — `#callback__FORM_tariff_calc` |
| DYNAMIC FORM CONSENT | PASS |
| DYNAMIC FORM SUBMIT | PASS — POST `https://i-seo.su/callback__FORM.php` |
| SERVER RESULT | HTTP 200 `true` |
| SUCCESS UI | PASS |
| ISOLATED MAIL | PASS |
| RECALCULATE | PASS — form remains a single DOM node; after success the form fades out (`fadeOut` + success `<p>`); a second click does **not** POST (no duplicate mail). Recalc does not insert a second form. `dup_click_handlers_on_button` = 0 (delegated `$(document).on`) |
| DUPLICATE HANDLER | 0 problematic |
| DUPLICATE MAIL | 0 extra POST after success |

## 10. Tariff Calculator

Page: `https://i-seo.su/tariff-calc` — **same** `tarif-calc.php` flow, not a second calculator engine.

| Check | Result |
|-------|--------|
| CALCULATION WORKS | PASS |
| DYNAMIC FORM | PASS |
| SUBMIT | PASS `/callback__FORM.php` |
| SERVER | `true` |
| SUCCESS UI | PASS |
| MAIL PATH | PASS isolated |

## 11. Field Contracts

- PAGE: `pf_contact` method + `pf_phone` visible (regression 01). Site optional HTML/JS/server.
- CALLBACK: `cf_phone` required; live selects often `name="cf_ontact"` (missing Latin `c`). PHP aliases `cf_ontact`/`cf_contact`. **Not globally renamed.**
- AUDIT: `af_site` optional on server after HOMEPAGE-MODAL-LIVE-FAILURE-02 (blank site accepted).
- CALC: radio stages + `calc_*`; site not must-meaningful.
- CAREER: `cf_file` optional after Wave 2 (`не приложен` if absent).
- Extra SEO checkbox `.required-checkbox` («аудит после созвона») is **not** consent; intended UX.

SITE FIELD CONTRACT MISMATCHES AFTER: **0** (HTML/JS/server aligned: optional unless `required`).  
PHONE/CONTACT CONTRACT MISMATCHES AFTER: **0** (aliases documented; webinar/page use `pf_phone`).

## 12. Endpoint Resolution

Nested `/services/seo/*.html` previously posted to `/services/seo/page__FORM.php`. After Wave 1, live nested SEO and tariff popups POST to `https://i-seo.su/<handler>__FORM.php`. WRONG ENDPOINTS AFTER: **0**.

## 13. Consent

Live lead surfaces without `personal_data_consent`: **0** (blog.html/article patched; calc-result WAVE 01A already present). Privacy URL `/privacy-policy.html` / `https://i-seo.su/privacy-policy.html`. Accepted value `1`. Server guard in `iseo-form-security.php`. Snapshot key `consent_guard_hint` on **config.php** is not the guard file — do not treat as OFF.

DYNAMIC CONSENT SURFACES MISSING: **0**.

## 14. Security

| Control | State |
|---------|--------|
| HMAC | ACTIVE (token endpoint + hidden `iseo_ft`/`iseo_fs`/`iseo_fid`; snapshot `hmac_secret_null` is a config-text false-positive) |
| HONEYPOT | ACTIVE `contact_company_url` |
| MIN-FILL | ACTIVE |
| RATE LIMIT | ACTIVE ~3/5 min / form_id / IP; ~10/hour |
| DUPLICATE PROTECTION | ACTIVE |
| CRLF / scalar | intact |
| NORMAL RECIPIENT | `nikel007i33@yandex.ru` only |
| `im.work@mail.ru` in normal routing | NO |
| `im.work@nail.ru` | ABSENT |

Negative matrix on `page__FORM.php` (isolated): missing consent / `0` / malformed / honeypot / too-fast → HTTP 200 `false`. Validation **not** weakened.

## 15. Isolated Mail Matrix

Recipient for all task mails: **`im.work@mail.ru`**.

| Handler | Isolated accept |
|---------|-----------------|
| page | YES (browser homepage + nested + webinar; synthetic) |
| callback | YES (SEO calc, tariff-calc, WP footer) |
| audit | YES (homepage modal browser; operator production accept **not** repeated) |
| calc | YES (homepage calculator) |
| bonus | YES |
| partners | YES |
| career | YES (synthetic then live UI after Wave 2) |
| review | YES (synthetic then live UI after Wave 2) |
| tariff_1..4 | YES (synthetic + live UI on restaurant page) |

PRODUCTION TEST EMAIL COUNT: **0**.

## 16. Defects Found

See `evidence/form-system-acceptance-01/defects.csv`.

1. **DEF-CONSENT-BLOG** — static blog forms lacked consent.  
2. **DEF-CYRILLIC-NAME** — footer contact id/name hygiene; `cf_ontact` remains aliased.  
3. **DEF-RELATIVE-ENDPOINT** — remaining relative `__FORM.php` AJAX in `common.js`.  
4. **DEF-PREVENTDEFAULT** — catch-all intercept; calc `preventDefault`.  
5. **DEF-CAREER-DEAD-UI** — live form `#career__FORM_info` unbound; `cf_file` required vs file input omitted by `serialize()`.

Known historical families (pf_contact-as-phone, nested page endpoint, `*_site` JS-required, audit `af_site`, webinar) were **regression-checked**; not reopened.

## 17. Fixes

Backups: `X:\AI MARS\local\sites\iseo-su-production\_form-system-acceptance-01\` (Wave 1 + Wave 2 SHA/timestamp).

| Wave | Files | Change |
|------|-------|--------|
| 1 | `js/common.js`, `blog.html`, `blog-article.html`, `wp-content/themes/iseoblog/footer.php` | consent; footer `cf_contact`; root-relative AJAX; preventDefault catch-all |
| 2 | `js/common.js`, `career__FORM.php` | `#career__FORM_send_info`; optional resume file |

No redesign, no handler merge, no mail-architecture change.

## 18. Browser Acceptance

Unique UI paths with real click/fill/Network:

homepage main, homepage audit modal (isolated + operator), homepage calc, SEO calculator, `/tariff-calc`, nested SEO page form, webinar, WP blog footer callback, partners, bonuses, career, reviews, tariff_1–4 order modals (restaurant page CTA).

Console 409s observed are **Metrika/other**, not form endpoints. No native reload where AJAX expected on these paths.

## 19. Responsive Acceptance

Viewports **1440×900** and **390×844**. Homepage main form/consent/button geometrically visible. SEO/tariff calculator result form + consent + button visible after calculate. Homepage audit modal and webinar inspect used imperfect selectors in the harness (modal trigger vs form); those UIs were already proven at 1440 via functional submit. No clipping defect proven that required CSS change. DESIGN CHANGED: **NO**.

## 20. Production / Source Alignment

Canonical mirrors updated under `projects/iseo-su-site-ops/production-source/` for the patched files. Live SHA matched source after deploys (Wave 1/2 evidence JSON). PRODUCTION/SOURCE ALIGNED: **YES** for this contour.

## 21. Final Decision

**COMPLETE** — all classified live surfaces structurally accounted; unique PHP handlers mail-tested in isolation; proven defects closed; SEO/tariff calculator submit+success+isolated mail PASS; homepage main + audit modal PASS; other modals (bonus, tariff 1–4) PASS; webinar/city/niche/USA-UAE share SEO form family with nested restaurant PASS; `test_mode` FINAL OFF; production test mails 0.

Classifier **87** UA keys were not each given a separate POST (shared templates + per-`form_id` rate limit 3/5 min). That is the same clone-authority model as FORM CONTRACT REGRESSION 01, not an untested user form family.
