# SITE-001 Brand Replacement Map v1

**Type:** W0 read-only discovery artefact — **no site modifications performed**  
**Date:** 2026-06-07  
**Site:** SITE-001 — Автосалон СИБКАР (Phase 1 target)  
**Environment:** **TEST** — `https://sibcar.new-site.space/`  
**Platform (operator-recorded):** ocStore / OpenCart **3.0.3.8 (rs.2)**  
**Discovery method:** Public HTTP read-only crawl (homepage, sitemap-linked pages, asset probes, `robots.txt`)  
**Companion:** [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md)

**Explicit exclusions observed:** No admin login; no DB/FTP/SSH access; no file writes; no backups created.

---

## Executive summary

Public storefront discovery confirms **pervasive legacy brand «АЦ / Автоцентр Хмельницкий»** across titles, meta, body copy, header/footer, contacts, and logo assets. **Transliterated Latin variants** (`Hmelnickiy`, `ac-hmelnickiy`, etc.) were **not found** in crawled public HTML.

**Critical gaps for W1:** `oc_setting` store keys were **not read from admin or database** — values below marked **INFERRED** from storefront unless noted. Active OpenCart **theme directory name** remains **SAFE UNKNOWN**. Write charter on access brief remains **NO**.

---

## 1. Theme discovery

| Item | Finding | Evidence | Confidence |
|------|---------|----------|------------|
| Active OC theme name (admin) | **SAFE UNKNOWN** | No `/catalog/view/theme/<name>/` paths in rendered HTML; requires admin → Extensions → Themes or filesystem | — |
| Storefront asset layout | **Custom root theme structure** (not default OC `catalog/view/theme/default/` in public HTML) | `/css/main.css`, `/css/media.css`, `css/normalize.css`, `/libs/*`, `/img/*`, `/favicon/*` on all scanned pages | **High** (public) |
| OpenCart core paths (backend) | Present per `robots.txt` | `/admin`, `/catalog`, `/system` disallowed | **High** |
| Custom theme paths (public) | `/css/`, `/img/`, `/favicon/`, `/libs/` | Repeated on homepage + 8 info/service pages | **High** |
| Logo paths (template refs) | `img/logo.svg`, `img/logo_white.svg`, `/img/logo_white.svg` | Homepage HTML `src`/`href` | **High** |
| Favicon paths | `/favicon/favicon.svg`, `/favicon/favicon-{16,32,64,96,144,192,256,384,512}x*.png`, `/favicon/apple-touch-icon-*.png` | Homepage HTML | **High** |
| Default OC logo path | `/image/catalog/logo.png` | HTTP 200 (2481 bytes) — likely **unused default**; storefront uses `/img/` | **Medium** |
| OG preview image | `/img/preview.jpg` | Referenced in `<meta property="og:image">`; HTTP probe **404** | **High** (broken ref) |
| Theme author meta | `MCA` | `<meta name="author" content="MCA">` on all pages | **High** |

**W1 note:** Store settings wave does **not** replace theme files; logo/favicon replacement is **W3**. Theme name discovery still required for W4+ language/template grep.

---

## 2. Store settings inventory

**Source limitation:** Admin → System → Settings → Store and `oc_setting` table were **not accessed**. Rows below map **expected OpenCart keys** to **observed storefront values** (INFERRED) or **SAFE UNKNOWN**.

| OC setting key (typical) | Observed / inferred old value | Replacement type | Risk | Notes |
|--------------------------|-------------------------------|------------------|------|-------|
| `config_name` | **INFERRED:** `АЦ Хмельницкий` (from titles, H1, footer patterns) | `brand_display_name` | **High** | Confirm in admin before W1 |
| `config_owner` | **SAFE UNKNOWN** | `legal_owner` | **Medium** | Target: signatory / ООО «СибКар» per operator pack |
| `config_address` | **INFERRED:** `Новосибирск, ул. Богдана Хмельницкого 101` | `physical_address` | **High** | Conflicts with Atlas legal address (ул. Доватора, 11) — **operator decision required** |
| `config_email` | **SAFE UNKNOWN** (not visible on public pages) | `contact_email` | **Medium** | Target attested: `info_sibcar@mail.ru` (EV-W1C-CC-01) |
| `config_telephone` | **INFERRED:** `+7 (383) 388-55-23` / `+73833885523` | `contact_phone` | **High** | Target phone **SAFE UNKNOWN** in Atlas |
| `config_meta_title` | `Купить авто с пробегом в Новосибирске — проверенные автомобили б/у \| АЦ Хмельницкий` | `seo_meta_title` | **High** | Contains brand suffix |
| `config_meta_description` | `Автоцентр Хмельницкий в Новосибирске предлагает надёжные автомобили с пробегом. Большой выбор, честные цены, оформление кредита, рассрочки и обмен по системе Trade-in.` | `seo_meta_description` | **High** | |
| `config_meta_keyword` | `АЦ Хмельницкий, автомобили с пробегом Новосибирск, купить б/у авто, Trade-in Новосибирск, автокредит` | `seo_meta_keyword` | **Medium** | |
| `config_country_id` / `config_zone_id` | **SAFE UNKNOWN** | `geo_settings` | **Low** | Likely RU / Novosibirsk region |
| Multi-store rows | **SAFE UNKNOWN** | `multi_store` | **Medium** | Not verified |

**Additional meta (non-standard keys possible):**

| Location | Old value | Replacement type | Risk |
|----------|-----------|------------------|------|
| `<meta name="author">` | `MCA` | `vendor_meta` | **Low** | May be theme-level, not `oc_setting` |
| `<meta name="yandex-verification">` | `69e51badedb26226` | `verification_token` | **High** | **Do not change** without operator/Yandex re-verification plan |
| `robots.txt` → `Host:` | `xn----7sbqmagfghm8fkh5f.xn--p1ai` | `legacy_domain_reference` | **High** | Punycode legacy production host — **out of W1**; needs DNS/SEO wave |
| `robots.txt` → `Sitemap:` | `https://xn----7sbqmagfghm8fkh5f.xn--p1ai/index.php?route=extension/feed/google_sitemap` | `legacy_sitemap_url` | **High** | Points off TEST hostname |

---

## 3. Information pages inventory

| Page role | SEO URL (TEST) | HTTP | Title (old brand highlighted) | Brand density | Notes |
|-----------|----------------|------|-------------------------------|---------------|-------|
| About company | `/about` | 200 | Об автосалоне **АЦ Хмельницкий** – продажа авто с пробегом… | High | Primary «О компании» |
| About (duplicate) | `/about_us` | 200 | **Вавилон** *(title)* — body still contains **АЦ Хмельницкий** | Medium | **Legacy orphan** — title mismatch; high leftover risk |
| Contacts | `/contact/` | 200 | Контакты **АЦ Хмельницкий** – автосалон… | High | H1: Контакты «**АЦ Хмельницкий**» |
| Privacy | `/privacy-policy` | 200 | …\| **АЦ Хмельницкий**, Новосибирск | High | Body: автосалон «**Хмельницкий**» |
| Delivery | — | — | **NOT FOUND** in sitemap (141 URLs scanned) | — | **SAFE UNKNOWN** / may not exist |
| Payment | — | — | **NOT FOUND** as standalone page | — | Credit terms under `/loan-terms` |
| Custom — autocredit | `/autocredit` | 200 | …\| **АЦ Хмельницкий** | High | Service landing |
| Custom — trade-in | `/tradein` | 200 | …\| **АЦ Хмельницкий** | High | Service landing |
| Custom — loan terms | `/loan-terms` | 200 | Условия автокредитования в **АЦ «Хмельницкий»**… | High | Payment/credit policy |

**Standard OC routes (`index.php?route=information/information&information_id=N`):** Not used in public SEO URLs; content appears routed through **custom SEO URLs** and/or custom controllers.

---

## 4. SEO inventory

### 4.1 Homepage

| Field | Old value |
|-------|-----------|
| `<title>` | Купить авто с пробегом в Новосибирске — проверенные автомобили б/у \| **АЦ Хмельницкий** |
| `<meta name="description">` | **Автоцентр Хмельницкий** в Новосибирске предлагает надёжные автомобили с пробегом… |
| `<meta name="keywords">` | **АЦ Хмельницкий**, автомобили с пробегом Новосибирск, купить б/у авто, Trade-in Новосибирск, автокредит |
| `<h1>` | **АЦ Хмельницкий** — авто с пробегом в Новосибирске |
| `<meta property="og:image">` | `/img/preview.jpg` (**404** at probe time) |

### 4.2 Manufacturer SEO

| Item | Status |
|------|--------|
| Manufacturer landing pages in sitemap | **None sampled** |
| `manufacturer_id` product URLs | Disallowed in `robots.txt` |
| Manufacturer meta fields | **SAFE UNKNOWN** — requires admin/catalog read |

### 4.3 Cross-page SEO patterns

- Brand suffix `| АЦ Хмельницкий` repeats on service pages (`/autocredit`, `/tradein`, etc.).
- Keywords on `/about` and `/contact/`: `автосалон, автоцентр Хмельницкий, ац Хмельницкий` (mixed case).
- JSON-LD structured data: **0 blocks** found on scanned pages.

---

## 5. Brand discovery matrix

Search terms from mission brief — public HTML crawl (homepage + 8 sitemap info/service pages, 2026-06-07):

| Search term | Found? | Occurrence notes |
|-------------|--------|------------------|
| Хмельницкий | **YES** | Dominant variant; titles, H1, body, privacy quoted form «Хмельницкий» |
| хмельницкий | **YES** | `/autocredit`, `/privacy-policy` (lowercase in body/meta) |
| Хмельницкого | **YES** | Street address «ул. Богдана **Хмельницкого** 101» — **geographic**; replacement policy needs operator rule |
| Автоцентр Хмельницкий | **YES** | Homepage meta description; `/about` keywords |
| Автосалон Хмельницкий | **PARTIAL** | Phrase «автосалон «**Хмельницкий**»» in privacy; not exact full phrase elsewhere |
| AC Хмельницкий | **NO** | Not in crawled HTML |
| АЦ Хмельницкий | **YES** | Primary short brand form |
| Hmelnickiy | **NO** | |
| hmelnickiy | **NO** | |
| Khmelnitskiy | **NO** | |
| khmelnitskiy | **NO** | |
| ac-hmelnickiy | **NO** in HTML | Possible in punycode domain / off-site refs only |
| ac_hmelnickiy | **NO** | |

### Additional discovered variants

| Variant | Context | Replacement type | Risk |
|---------|---------|------------------|------|
| `АЦ «Хмельницкий»` | `/loan-terms` title, body | `brand_display_name` | **High** |
| `ац Хмельницкий` | `/about`, `/contact/` keywords (lowercase «ац») | `brand_display_name` | **Medium** |
| `Автосалон «Хмельницкий»` | Privacy policy description | `brand_display_name` | **High** |
| `Автосалон №1 в Новосибирске` | Homepage marketing block | `marketing_claim` | **Medium** | May stay or be rewritten |
| `ул. Богдана Хмельницкого 101` | Header/footer/contacts all pages | `address_street` | **High** | **Not a brand string** — physical location; do not auto-replace with Доватора without operator |
| `xn----7sbqmagfghm8fkh5f.xn--p1ai` | `robots.txt` Host + Sitemap | `legacy_domain` | **High** | Likely legacy **.рф** production domain |
| Page title `Вавилон` | `/about_us` | `orphan_content` | **High** | Leftover unrelated brand |

---

## 6. Contacts discovery

| Contact type | Old value | Location(s) | Replacement type | Risk |
|--------------|-----------|-------------|------------------|------|
| Primary phone | `+7 (383) 388-55-23` | Header, footer, all scanned pages | `contact_phone` | **High** |
| Phone (normalized) | `+73833885523` | `tel:` / JSON attrs | `contact_phone` | **High** |
| WhatsApp | `https://wa.me/79539979910` | Header/footer link | `messenger_whatsapp` | **High** | **Different number** from main phone — confirm target |
| Email | **None found** on public pages | — | `contact_email` | **Medium** | Likely only in admin/mail settings |
| Physical address | `Новосибирск, ул. Богдана Хмельницкого 101` | Header, contacts, footer | `physical_address` | **High** |
| Hours | `Ежедневно c 9:00-21:00` | Header | `business_hours` | **Low** |
| Telegram / Viber / VK | **NOT FOUND** | — | — | — |
| Atlas target email (not on site) | — | — | `info_sibcar@mail.ru` | **Medium** | Attested target (EV-W1C-CC-01); not yet on storefront |
| Atlas legal address (not on site) | — | — | `630124, г. Новосибирск, ул. Доватора, 11` | **High** | Legal vs showroom address policy required |

---

## 7. Logo and favicon discovery

| Asset | Path | HTTP probe | Template reference | Replacement type | Risk |
|-------|------|------------|-------------------|------------------|------|
| Primary logo (color) | `/img/logo.svg` | 200, SVG 10890 B | `img/logo.svg` | `logo_file` | **High** | W3 — SVG may embed «Хмельницкий» text paths |
| Primary logo (white) | `/img/logo_white.svg` | 200, SVG 10673 B | `img/logo_white.svg`, `/img/logo_white.svg` | `logo_file` | **High** | Used in header/footer |
| Favicon master | `/favicon/favicon.svg` | 200, SVG 1463 B | `<link rel="icon">` variants | `favicon_file` | **High** | Full PNG size set under `/favicon/` |
| Apple touch icons | `/favicon/apple-touch-icon-*.png` | Referenced | `<link rel="apple-touch-icon">` | `favicon_file` | **Medium** |
| PNG favicons | `/favicon/favicon-*.png` | Referenced | Multiple sizes | `favicon_file` | **Medium** |
| Legacy root favicon | `/favicon.ico` | **404** | — | — | **Low** |
| OC default logo | `/image/catalog/logo.png` | 200 | Not referenced in crawled HTML | `orphan_asset` | **Low** | May still be set in admin `config_logo` |
| OG image | `/img/preview.jpg` | **404** | `og:image` meta | `social_preview` | **Medium** | Broken; may contain old branding |

**SVG text content:** Direct fetch of `/img/logo.svg` returned **HTTP 500** during probe — embedded brand text **SAFE UNKNOWN** until W3 asset review.

---

## 8. Brand Replacement Map (action table)

**Target strings (Phase 1 intent — not operator-approved pack):** display **СИБКАР** / **Автосалон СИБКАР**; legal **ООО «СибКар»**; email **info_sibcar@mail.ru**; address/phone per operator **Brand Replacement Pack v1** (pending).

| ID | Location | Old value | Replacement type | Wave | Risk |
|----|----------|-----------|------------------|------|------|
| BR-001 | `oc_setting` → `config_name` *(INFERRED)* | АЦ Хмельницкий | `brand_display_name` | **W1** | **High** |
| BR-002 | `oc_setting` → `config_meta_title` *(INFERRED)* | …\| АЦ Хмельницкий | `seo_meta_title` | **W1** | **High** |
| BR-003 | `oc_setting` → `config_meta_description` *(INFERRED)* | Автоцентр Хмельницкий в Новосибирске… | `seo_meta_description` | **W1** | **High** |
| BR-004 | `oc_setting` → `config_meta_keyword` *(INFERRED)* | АЦ Хмельницкий, … | `seo_meta_keyword` | **W1** | **Medium** |
| BR-005 | `oc_setting` → `config_address` *(INFERRED)* | Новосибирск, ул. Богдана Хмельницкого 101 | `physical_address` | **W1** | **High** |
| BR-006 | `oc_setting` → `config_telephone` *(INFERRED)* | +7 (383) 388-55-23 | `contact_phone` | **W1** | **High** |
| BR-007 | `oc_setting` → `config_email` | **SAFE UNKNOWN** | `contact_email` | **W1** | **Medium** |
| BR-008 | `oc_setting` → `config_owner` | **SAFE UNKNOWN** | `legal_owner` | **W1** | **Medium** |
| BR-009 | Homepage `<h1>` / body modules | АЦ Хмельницкий — авто с пробегом… | `page_content` | **W2** | **High** |
| BR-010 | `/about` — title, description, body | АЦ Хмельницкий / автоцентр Хмельницкий | `information_page` | **W2** | **High** |
| BR-011 | `/contact/` — title, H1, description | АЦ Хмельницкий | `information_page` | **W2** | **High** |
| BR-012 | `/privacy-policy` — title, description, body | АЦ Хмельницкий; «Хмельницкий» | `information_page` | **W2** | **High** |
| BR-013 | `/about_us` — title | Вавилон | `orphan_content` | **W2** | **High** |
| BR-014 | `/autocredit`, `/tradein`, `/loan-terms` | АЦ Хмельницкий | `custom_page` | **W2** | **High** |
| BR-015 | Header/footer template | img/logo.svg, logo_white.svg | `logo_file` | **W3** | **High** |
| BR-016 | `/favicon/*` | Branded favicon set | `favicon_file` | **W3** | **High** |
| BR-017 | `/image/catalog/logo.png` | Default OC logo (if `config_logo` points here) | `admin_logo_setting` | **W3** | **Medium** |
| BR-018 | `robots.txt` Host / Sitemap | xn----7sbqmagfghm8fkh5f.xn--p1ai | `legacy_domain` | **W5+** | **High** |
| BR-019 | `<meta name="yandex-verification">` | 69e51badedb26226 | `verification_token` | **Hold** | **High** |
| BR-020 | WhatsApp link | wa.me/79539979910 | `messenger_whatsapp` | **W1/W2** | **High** |
| BR-021 | Street name in address | ул. Богдана Хмельницкого | `address_street` | **Policy** | **High** | Operator: keep showroom vs replace |
| BR-022 | Mail / order templates | **SAFE UNKNOWN** | `email_template` | **W4+** | **Medium** |
| BR-023 | Extension module configs | **SAFE UNKNOWN** | `extension_config` | **W5** | **Medium** |
| BR-024 | `ocMod` / modification cache | **SAFE UNKNOWN** | `cached_strings` | **W6** | **High** |

---

## 9. W0 discovery gaps (SAFE UNKNOWN)

| Topic | Status | Verification path |
|-------|--------|-------------------|
| `oc_setting` exact values | **NOT CAPTURED** | Admin export or read-only SQL on TEST |
| Active theme directory name | **NOT CAPTURED** | Admin → Extensions → Themes |
| `config_logo` / `config_icon` admin paths | **NOT CAPTURED** | Admin settings |
| Admin store name vs storefront | **NOT COMPARED** | Admin screenshot |
| Delivery / Payment information pages | **NOT FOUND** | Admin information list + DB `oc_information_description` |
| DB-only brand strings | **NOT GREPPED** | SQL grep per review §Q4 |
| Theme/language PHP files | **NOT SCANNED** | FTP read-only or snapshot |
| Logo SVG embedded text | **NOT READ** (500 on fetch) | Filesystem or download in supervised session |
| Latin/transliterated brand in files | **NOT FOUND** (public HTML) | Full file grep still required |
| Product/category descriptions | **NOT SAMPLED** | Catalog grep |
| Email/SMTP sender name | **NOT CAPTURED** | Admin mail settings |

---

## 10. Operational signals (informational)

| Signal | Detail |
|--------|--------|
| PHP warning on homepage | `array_rand(): Second argument…` in `catalog/model/catalog/product.php:341` — **not W0 scope**; fix separately |
| Sitemap size | 141 URLs on TEST HTML sitemap |
| External integrations | Callibri (`cdn.callibri.ru`), SmartWidgets (`res.smartwidgets.ru`) — may inject brand-specific config **SAFE UNKNOWN** |

---

## 11. Decision — Can W1 Store Settings Replacement begin?

### Outcome: **NOT AUTHORIZED**

W0 public discovery **substantially advances** checklist items **C-03** (old-brand baseline — public layer) and **C-07** (partial discovery), but **W1 write prerequisites remain unsatisfied**:

| Gate | Status |
|------|--------|
| Write permission on TEST ([project-access-brief.md](../project-access-brief.md)) | **NO** |
| Brand Replacement Pack v1 approved (C-01) | **NOT SATISFIED** |
| Admin/`oc_setting` export — sanitized (C-08) | **NOT SATISFIED** — storefront inference only |
| Fresh backup before first write (C-08) | **NOT SATISFIED** — stale 2026-05-31 claim |
| Change Request + Rollback Plan (C-06) | **NOT SATISFIED** |
| Target phones/messengers confirmed (C-04) | **NOT SATISFIED** |
| Logo assets staged (C-03 assets) | **NOT SATISFIED** |
| Operator write approver on access brief (C-05) | **NOT SATISFIED** |

**Re-decision path:** Complete **C-01..C-11** in [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md) §6, including **admin store settings export** to confirm BR-001..BR-008, then issue decision **v1.1** as **AUTHORIZED WITH NOTES** for supervised W1 on TEST only.

**W1 may proceed when:** write charter **YES**, fresh backup recorded, Change Request bound, and `config_*` old values **confirmed in admin** against this map.

---

## 12. Related documents

| Document | Role |
|----------|------|
| [SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md](SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md) | Prior Phase 1 gate — NOT AUTHORIZED |
| [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md) | W0–W7 wave plan; checklist C-01..C-11 |
| [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](../../../atlas/population/ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | Target legal entity / email source |
| [RUN-5-FIRST-FINDINGS.md](RUN-5-FIRST-FINDINGS.md) | Pre-W0 evidence gaps |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-07 | **CREATED** — W0 read-only Brand Replacement Map from public TEST crawl |

*SITE-001 Brand Replacement Map v1 — discovery only; no site modifications.*
