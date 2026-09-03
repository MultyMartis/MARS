# ISEO-SU USA UAE PAGES WAVE 03 EVIDENCE v1

**Task ID:** `ISEO-SU-SITE-OPS-USA-UAE-PAGES-WAVE-03`  
**Date:** 2026-09-03  
**Class:** CURRENT / CANONICAL evidence for WAVE 3

---

## 1. Scope

Create two Direct-ready static SEO landings cloned from production `zarubezhnye.html`:

- `https://i-seo.su/services/seo/prodvizhenie-v-ssha.html`
- `https://i-seo.su/services/seo/prodvizhenie-v-oae.html`

Not in menu. Not in static sitemap. Normal indexability. Title suffix exactly `| INTLSEO`. WAVE 1 / 01A form consent inherited via PHP includes. Production mutation: **2 new HTML files only**.

---

## 2. Approved Decisions

| Decision | Resolution |
|----------|------------|
| Indexability | No `noindex`. `index, follow` inherited from source family. |
| Menu | Do not add. |
| Sitemap | Do not add to `sitemap-static.xml` / inventories. Do not regenerate. |
| Title suffix | `INTLSEO` (reject `itlseo`, `itlseo.su`, `i-seo.su` in title). |
| Topic block | Remove entire «Выберите тематику» on **new pages only**. |
| Recipient / HMAC | Unchanged: `nikel007i33@yandex.ru`; no HMAC/antispam edits. |

---

## 3. Source Page

| Field | Value |
|-------|-------|
| Live URL | `https://i-seo.su/services/seo/zarubezhnye.html` |
| Production path | `/home/n/nikel0rv/i-seo.su/public_html/services/seo/zarubezhnye.html` |
| Forensic SHA256 | `28e2d8a4bc781d1c8a077116c88337c8f20836be2deec0554842fa87f8fba671` |
| Bytes | 44159 |
| robots | `index, follow` |
| Canonical on source | **absent** (not fixed in this wave) |
| Topic section on source | **present** (must remain) |
| Consent in static HTML | via includes (`content-form-seo.php`, `content-calc-seo.php`, `tarif-calc.php`, popups) |
| Clone method | SFTP source with PHP includes — not live-rendered HTML |

MARS origin did **not** track `zarubezhnye.html`. Clone used production source. **`zarubezhnye.html` was not committed** (production-only existing page; this wave does not promote it).

---

## 4. Case Verification

Live HTTP 200 and identity needles **before** production write:

| Market | Label | URL | HTTP | Identity |
|--------|-------|-----|------|----------|
| USA | AAA Cab Limo | `https://i-seo.su/cases/aaa-limo.html` | 200 | aaa / limo / cab |
| USA | Dr. Nicole | `https://i-seo.su/cases/drnicole.html` | 200 | nicole / dallas / natural |
| UAE | iLuvMe | `https://i-seo.su/cases/iluve-me.html` | 200 | iluv / luvme / iluve |
| UAE | Yofleet | `https://i-seo.su/cases/youfleet.html` | 200 | fleet / yofleet / youfleet |

**CASE LINKS VALID: 4/4** · **STOP_CASE_MISMATCH: false**

Case images (existing production assets, no new uploads): `aaa-limo.png`, `drnicole.png`, `iluve-me.png`, `case_youfleet_title.png`.

---

## 5. USA Page Mapping

| Slot | Approved / live |
|------|-----------------|
| Title | `Заказать SEO-продвижение сайта компании в США \| INTLSEO` |
| Meta description | `Продвигаем сайты в США в топ Google. Работа с англоязычной семантикой, локальными справочниками и учетом конкуренции ниши. Бесплатный аудит и стратегия.` |
| H1 | `SEO-продвижение сайта в США` |
| Intro | Starts `США остаются крупнейшим и самым конкурентным рынком…` |
| Second H2 | `SEO продвижение сайта в США` |
| List | 4 items including outreach / GBP / Yelp / semantics |
| After list | AAA Cab Limo / Dallas Natural Doc narrative |
| Stages intro | Google only; English content |
| Cases | AAA Cab Limo (`aaacablimo.com`) · Dr. Nicole (`dallasnaturaldoc.com`) |
| Canonical | `https://i-seo.su/services/seo/prodvizhenie-v-ssha.html` |
| Source SHA256 | `b902adda9d99d825d967d609adc8070c481483ad3f09c34ca6fd2e222a802fb1` |
| Bytes | 42435 |

---

## 6. UAE Page Mapping

| Slot | Approved / live |
|------|-----------------|
| Title | `Заказать SEO-продвижение сайта компании в ОАЭ \| INTLSEO` |
| Meta description | `Продвигаем сайты в ОАЭ на арабском и английском языках. Учитываем конкуренцию Дубая и других эмиратов. Бесплатный аудит и понятная стратегия работы.` |
| H1 | `SEO-продвижение сайта в ОАЭ` |
| Intro | Starts `ОАЭ сочетают быстрорастущую экономику Персидского залива…` |
| Second H2 | `SEO продвижение сайта в ОАЭ` |
| List | 4 bilingual / GBP / reviews / localization items |
| After list | iLuvMe / Yofleet narrative |
| Stages intro | Arabic + English; Gulf / emirate specificity |
| Cases | iLuvMe (`iluvme.ae`) · Yofleet (`yofleet.com`, including `8 месяцев работы`) |
| Canonical | `https://i-seo.su/services/seo/prodvizhenie-v-oae.html` |
| Source SHA256 | `795670efeac3db0e78953f09ce9795f69196d87300fabf08b4bffc31fa4152ce` |
| Bytes | 42474 |

---

## 7. INTLSEO Branding

Both titles contain exactly `| INTLSEO`.  
No `itlseo`, `itlseo.su`, or `i-seo.su` in `<title>`.  
**INTLSEO BRANDING: PASS**

---

## 8. Topic Section Removal

Live HTML: heading «Выберите тематику» **absent**; `seo_subject` cards **absent**.  
Source `zarubezhnye.html` still has the section.  
**USA TOPIC SECTION PRESENT: NO** · **UAE TOPIC SECTION PRESENT: NO**

---

## 9. Form Consent Preservation

Live rendered pages: **10** `name="personal_data_consent"` fields each.  
Privacy link in WAVE 1 markup: `/privacy-policy.html` (absolute URL `https://i-seo.su/privacy-policy.html` is the documented canonical privacy page; relative href is the accepted include pattern).  
Calculator checkbox `personal_data_consent_calculator__FORM` present.  
Tariff-calc result `personal_data_consent_callback__FORM_tariff_calc` present.  
HMAC / recipient / handlers **not** modified.

**USA CONSENT COVERED: YES** · **UAE CONSENT COVERED: YES** · **CALCULATOR RESULT CONSENT COVERED: YES**

---

## 10. Indexability

- `meta robots`: `index, follow`
- no `noindex`
- self-canonical on both unique pages
- `robots.txt` does not `Disallow: /services/seo`
- **DIRECT-READY / NOT SITEMAP-PROMOTED**

---

## 11. Menu Exclusion

Theme `content-topbar.php` / `content-mobilemenu.php` unchanged.  
Homepage HTML does not contain `prodvizhenie-v-ssha` or `prodvizhenie-v-oae`.  
**USA IN MENU: NO** · **UAE IN MENU: NO**

---

## 12. Sitemap Exclusion

Allowlists not edited. Generator not run.  
Live `sitemap-static.xml`: **132** URLs; USA/UAE loc **absent**.  
**USA IN STATIC SITEMAP: NO** · **UAE IN STATIC SITEMAP: NO** · **SITEMAP CHANGED: NO**

---

## 13. Production Backup

Root: `X:\AI MARS\local\sites\iseo-su-production\_usa-uae-pages-wave-03\`

| Path | Role |
|------|------|
| `_forensic\zarubezhnye.html` | Source forensic |
| `backup-20260903T163937Z\prodvizhenie-v-ssha.html` | CREATE copy of USA page |
| `backup-20260903T163937Z\prodvizhenie-v-oae.html` | CREATE copy of UAE page |
| `_deploy_validate.json` | Deploy/validate log (privacy needle initially FAIL vs relative href; live revalidate PASS) |

Shared CSS/JS/forms/sitemap **not** backed up: **not mutated**.

---

## 14. Deployment

SFTP to `/home/n/nikel0rv/i-seo.su/public_html/services/seo/` — **2 HTML files**.  
No sitemap upload. No menu/theme upload.

---

## 15. Live Validation

Revalidate `tools/_wave03_live_validate.py` → `_wave03_live_validate.json`: **FINAL PASS**.

| URL | HTTP | Title | Canonical | Consent |
|-----|------|-------|-----------|---------|
| USA | 200 | exact INTLSEO title | self | 10 |
| UAE | 200 | exact INTLSEO title | self | 10 |

---

## 16. Direct Landing Readiness

Direct URL 200 without menu/sitemap discovery. First-screen H1 present. Forms/calculator includes present. CTA/forms inherit WAVE 1. Assets via existing relative `../../css` / `../../js`.  
**DIRECT LANDING READINESS: PASS**

Browser UI MCP not used; validation is HTTP + HTML parse.

---

## 17. Regression

Smoke 200: `/`, `zarubezhnye.html`, `b-regionakh.html`, `seo.html`, `/tariff-calc`, `sitemap-static.xml`.  
Source still has «Выберите тематику». Sitemap still 132.  
**FORM REGRESSION: NONE**

---

## 18. Production / Source Alignment

Canonical MARS files:

- `production-source/static-html/services/seo/prodvizhenie-v-ssha.html`
- `production-source/static-html/services/seo/prodvizhenie-v-oae.html`

**PRODUCTION/SOURCE ALIGNED: YES** (two new pages). Existing `zarubezhnye.html` remains production-authoritative and untracked in git by this wave.

---

## 19. Rollback

Delete the two remote HTML files; restore nothing else (menu/sitemap untouched). Local CREATE copies remain under `_usa-uae-pages-wave-03\`.

---

## 20. Final Decision

**COMPLETE** — WAVE 3 USA/UAE Direct-ready landings live; INTLSEO titles; no menu; no sitemap; consent preserved.
