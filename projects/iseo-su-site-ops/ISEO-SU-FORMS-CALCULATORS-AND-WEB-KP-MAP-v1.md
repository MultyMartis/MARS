# ISEO-SU FORMS, CALCULATORS, AND WEB-KP MAP v1

**Programme:** ISEO-SU-SITE-OPS  
**Date:** 2026-07-24 (structural); **security posture updated 2026-08-20**  
**Rule:** Structural map + current anti-spam posture. No customer proposal bodies, no recipient emails, no live form submits in audits.

**Security authority:** `ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md`. Shared libs: `iseo-form-security.php` / `iseo-form-config.php`. MARS mirror: `production-source/forms/`.

## Forms (structural)

| Route / surface | Purpose | Front-end | JS | Server handler | Mail | Validation | Thank-you | Spam | Shared risk |
|-----------------|---------|-----------|----|----------------|------|------------|-----------|------|-------------|
| Marketing pages / home | Callback | markup + popups | `js/common.js` | `callback__FORM.php` | `mail()` | server `iseo-form-security` + JS | in-page / JS | honeypot+token+rate+dup | root vs services copies |
| Marketing pages | Generic page form | markup | common.js | `page__FORM.php` | mail | server + JS | JS | honeypot+token+rate+dup | same |
| Audit CTAs | Audit request | markup | common.js | `audit__FORM.php` | mail | server + JS | JS | honeypot+token+rate+dup | same |
| Calculator | SEO calc lead | calc UI | common.js | `calc__FORM.php` | mail | server + JS | JS | honeypot+token+rate+dup | revenue-critical |
| Tariff cards | Tariff lead | `#tariffs_slider` etc. | common.js | `tariff_1..4__FORM.php` | mail | server + JS | JS | honeypot+token+rate+dup | revenue-critical |
| Bonuses | Bonus form | page | common.js | `bonus__FORM.php` | mail | server + JS | JS | honeypot+token+rate+dup | copies |
| Career | Career form | page | common.js | `career__FORM.php` | mail | server + JS | JS | honeypot+token+rate+dup | copies |
| Partners | Partners form | page | common.js | `partners__FORM.php` | mail | server + JS | JS | honeypot+token+rate+dup | copies |
| Reviews | Review form | page | common.js | `review__FORM.php` | mail | server + JS | JS | honeypot+token+rate+dup | copies |
| WP blog chrome | May expose same JS forms | theme | common.js enqueued | root handlers | mail | server + JS | JS | honeypot+token+rate+dup | theme+static dual |

**Do not** submit forms during audits unless under an explicit test charter with `test_mode`. SMTP vs host `mail()` delivery path remains SAFE UNKNOWN. Empty submissions must not mail (server authoritative).

## Calculator / tariffs

| Layer | Path / object | Role |
|-------|---------------|------|
| Public WP page | `/tariff-calc` (1734) | Shell + title |
| Template | `page-tariffcalc.php` | `get_header` + include `tarif-calc.php` |
| Logic/UI part | `template-parts/tarif-calc.php` | Reads ACF keys: `seo_rate`, `dev_rate`, `text_rate`, `tariffs`, `k_city`, `k_comp`, `k_niche`, `k_site`, `round_step`, `tarif_uplift_max`, `effect` |
| ACF | «Настройки калькулятора» (1761) | Primary calculator settings |
| ACF | «Настройки каналов и тарифов» (1742) | Channel stages / packages |
| Theme mirrors | `content-tarifs-*.php`, `content-calc-*.php` | Cards/popups on WP surfaces |
| Shared JS | `js/common.js` | Stages, posts, tariff slider |
| Handlers | `calc__FORM.php`, `tariff_*__FORM.php` | Lead mail |
| Homepage / static | embedded markup in `page-home.php` / HTML | Parallel UI surfaces |

**Request parameters:** structural POST field names only (see handlers). No live transactions in this audit.

## Web-KP / offers

| Item | Value |
|------|-------|
| Public listing | `/offers` (page 1377) |
| CPT | `offer` (Admin «Предложения») |
| Single template | `single-offer.php` |
| ACF group | «Предложения» (1382) |
| Field keys observed in template | `site`, `region`, `tariff`, `tariffs`, `discount`, `deadline`, `stages`, `ways`, `growth`, `audit_file` |
| Robots | Disallow `/offer/*`, `/blog/offer/*` |
| `/web-kp`, `/kp` | **404** — not public routes |
| Auth / privacy | Treat singles as private commercial documents |
| Naming | Operator term “web-KP” → **likely** this system; confirm nickname only |

---

*Forms / calculators / web-KP map v1 · security posture 2026-08-20 · no private content.*
