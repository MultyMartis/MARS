# REPORT — SITE-001 W1F Legacy Sweep

**Type:** Full legacy-brand inventory — **read-only**  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Authorization context:** W1 Write Charter — inventory wave per [SITE-001-W1-EXECUTION-PACK-v1.md](SITE-001-W1-EXECUTION-PACK-v1.md) §3.6 W1F  
**Prior waves:** W1A **PASS** · W1B **PASS** · W1C **PASS** · W1D **PASS**

**Binding inputs:**

| Document | Role |
|----------|------|
| [SITE-001-W1A-EXECUTION-v1.md](SITE-001-W1A-EXECUTION-v1.md) | Store settings baseline; SMTP exclusion note |
| [SITE-001-W1A-POST-AUDIT-v1.md](SITE-001-W1A-POST-AUDIT-v1.md) | Unicode audit — no mixed-script defect |
| [SITE-001-W1B-EXECUTION-v1.md](SITE-001-W1B-EXECUTION-v1.md) | Theme text replacements |
| [SITE-001-W1C-EXECUTION-v1.md](SITE-001-W1C-EXECUTION-v1.md) | Controller meta replacements |
| [SITE-001-W1D-EXECUTION-v1.md](SITE-001-W1D-EXECUTION-v1.md) | Logo/favicon swap; prior grep artefact |
| [SITE-001-BRAND-REPLACEMENT-MAP-v1.md](SITE-001-BRAND-REPLACEMENT-MAP-v1.md) | W0 discovery dictionary |
| [SITE-001-W1-EXECUTION-PACK-v1.md](SITE-001-W1-EXECUTION-PACK-v1.md) | Wave plan W1F-A..E |

**Explicit exclusions (honored):** No replacements. No FTP writes. No admin writes. No cache clears. **Production not touched.**

**Evidence artefact (local, not in git):** `.recovery-temp/site-001-w1f-legacy-sweep.json` · `.recovery-temp/site-001-w1f-extract.json`

---

## Executive summary

Post-W1A/B/C/D targeted inventory confirms **substantial remaining legacy brand exposure** outside the completed waves. **Homepage, `/about`, `/contact/` are CLEAN** (W1A/B/C effective). Highest residual risk clusters:

1. **YML / export feeds** — shop `<name>`, `<company>`, `<url>` still legacy in controllers **and** live XML at `/data/yandex-bu.xml`, `/data/yandex.xml`.
2. **SMTP / mail identity** — `config_mail_smtp_username` unchanged per W1A; hardcoded punycode sender in `anketa.php`.
3. **Legal / service information pages** — pervasive legacy in admin-sourced HTML (privacy, user-agreement, loan-terms, autocredit, tradein).
4. **Product-layer SEO** — `product.php`, `category.php`, `productnew.twig`, admin `product_form.twig` inject «АЦ Хмельницкий» into titles/meta.
5. **SEO infrastructure** — `robots.txt` Host + Sitemap still point to legacy punycode production domain.

**Latin transliterations** (`Hmelnickiy`, `Khmelnitskiy`, `ac-hmelnickiy`, `ac_hmelnickiy`): **not found** in scanned surfaces.

**Geographic exception:** `ул. Богдана Хмельницкого` / `улица Богдана Хмельницкого, 101` — **5 hits**, classified **GEOGRAPHICAL_REFERENCE** — excluded from replacement list.

---

## Scan scope and methods

| Surface | Method | Coverage |
|---------|--------|----------|
| `catalog/` | FTP read-only — controllers, theme `auto`, targeted templates | **Partial-deep** — high-risk paths + W1D-known files |
| `admin/` | FTP read-only — `product_form.twig`; admin login for settings/information | **Partial** — template grep OK; **admin session failed** this run (see UNKNOWN) |
| `system/` | FTP list (depth-limited) | **Shallow** — no legacy hits in scanned `system/` PHP configs |
| `image/` | FTP flat listing `image/catalog/` | Filename inventory only |
| `img/` | FTP flat listing | Orphan filename check |
| `robots.txt` | FTP + HTTP | **Full** |
| Live HTTP | Public pages, YML routes, XML exports | **Full** for listed URLs |
| Feeds / YML | Controller source + `/data/yandex*.xml` | **Full** for active exports |
| Language files | Not exhaustively scanned (FTP throughput) | **SAFE UNKNOWN** for undiscovered lang keys |
| Full-tree grep | ~1300 text files enumerated; download aborted (FTP latency) | Deferred — targeted scan used instead |

**Scan limitation (documented):** Full recursive download of all `catalog/language` + `admin/language` text files exceeded practical FTP throughput in this session. Residual risk in un-scanned language PHP files is **LOW** (standard OC lang files rarely contain brand strings; W1C lang scan of `contact.php` was clean).

---

## Special rule — GEOGRAPHICAL_REFERENCE

The following are **not branding** and are **excluded** from the replacement inventory:

| File | Line | Text | Classification |
|------|------|------|----------------|
| `catalog/view/theme/auto/template/common/header.twig` | 46 | `Новосибирск, ул. Богдана Хмельницкого 101` | GEOGRAPHICAL_REFERENCE |
| `catalog/view/theme/auto/template/common/footer.twig` | 10 | `Новосибирск, ул. Богдана Хмельницкого 101` | GEOGRAPHICAL_REFERENCE |
| `catalog/view/theme/auto/template/information/contact.twig` | 27 | `Новосибирск, ул. Богдана Хмельницкого 101` | GEOGRAPHICAL_REFERENCE |
| `admin:oc_setting/config_address` | — | `Новосибирск, улица Богдана Хмельницкого, 101` *(W1A confirmed)* | GEOGRAPHICAL_REFERENCE |

---

## robots.txt verification

| Directive | Value found | Status |
|-----------|-------------|--------|
| **Host** | `xn----7sbqmagfghm8fkh5f.xn--p1ai` | **LEGACY** |
| **Sitemap** | `https://xn----7sbqmagfghm8fkh5f.xn--p1ai/index.php?route=extension/feed/google_sitemap` | **LEGACY** — off-TEST hostname |

---

## SMTP verification

| Setting / identity | Source | Value | Status |
|--------------------|--------|-------|--------|
| `config_email` | W1A execution report (2026-06-08) | `demo@sibcar.local` | **UPDATED** — no legacy |
| `config_mail_smtp_username` | W1A execution report — **explicitly unchanged** | `send@ац-хмельницкий.рф` | **LEGACY — CRITICAL** |
| `config_mail_smtp_hostname` | W1A execution report | SAFE UNKNOWN *(not in W1A diff)* | **UNKNOWN** |
| Hardcoded sender | `catalog/controller/checkout/anketa.php:89` | `send@xn----7sbqmagfghm8fkh5f.xn--p1ai` | **LEGACY — CRITICAL** |
| Admin live read-back | This session | Login token **not obtained** | **SAFE UNKNOWN** — use W1A report as proxy |

---

## YML / export verification

| Export | Generator | Live URL | Legacy fields |
|--------|-----------|----------|---------------|
| Used stock YML | `catalog/controller/product/yml.php` → `data/yandex-bu.xml` | `/data/yandex-bu.xml` | `<name>АЦ «Хмельницкий»</name>`, `<company>ООО «АЦ Хмельницкий»</company>`, `<url>https://ац-хмельницкий.рф/</url>` |
| New stock YML | `catalog/controller/product/ymlnew.php` → `data/yandex.xml` | `/data/yandex.xml` | Same legacy shop block |
| Backup generators | `catalog/controller/product/backup_yml/yml.php`, `ymlnew.php` | Not active routes | Same strings — **inactive copies** |
| Google sitemap | `extension/feed/google_sitemap` | HTTP probe | **No brand strings** in response body |
| Per-offer URLs in YML | Live XML | `https://sibcar.new-site.space/...` | **TEST hostname** — shop-level metadata only is legacy |

---

## Admin product form verification

| File | Line | Text (legacy fragment) | Notes |
|------|------|------------------------|-------|
| `admin/view/template/catalog/product_form.twig` | 2202 | Comment example: `… \| АЦ Хмельницкий` | Admin UI hint / JS comment |
| `admin/view/template/catalog/product_form.twig` | 2211 | `name = '… \| АЦ Хмельницкий'` | JS template for auto-generated product SEO title |

---

## Orphan assets

| File | Location | Severity | Notes |
|------|----------|----------|-------|
| `img/logo - hmel.svg` | FTP `img/` | LOW | Legacy filename; **not referenced** in active templates (W1D confirmed) |
| `image/catalog/logo_balck.png` | FTP `image/catalog/` | LOW | Admin `config_logo` only; not in storefront HTML (W1D) |

---

## Legacy inventory table

*Consolidated rows — duplicate term matches on same line merged. Geographic references excluded.*

| File | Line/Location | Text | Category | Surface | Severity | Recommended Wave |
|------|---------------|------|----------|---------|----------|------------------|
| `robots.txt` | Host | `xn----7sbqmagfghm8fkh5f.xn--p1ai` | SEO | PUBLIC | HIGH | W1F-C |
| `robots.txt` | Sitemap | `https://xn----7sbqmagfghm8fkh5f.xn--p1ai/index.php?route=extension/feed/google_sitemap` | SEO | PUBLIC | HIGH | W1F-C |
| `catalog/controller/product/yml.php` | 55–57 | `<name>АЦ «Хмельницкий»</name>` · `<company>ООО «АЦ Хмельницкий»</company>` · `<url>https://ац-хмельницкий.рф/</url>` | YML | EXPORT | CRITICAL | W1F-C |
| `catalog/controller/product/ymlnew.php` | 55–57 | Same shop block as `yml.php` | YML | EXPORT | CRITICAL | W1F-C |
| `data/yandex-bu.xml` | `<shop>` block | Live XML mirrors controller legacy `name` / `company` / `url` | YML | EXPORT | CRITICAL | W1F-C |
| `data/yandex.xml` | `<shop>` block | Live XML mirrors controller legacy `name` / `company` / `url` | YML | EXPORT | CRITICAL | W1F-C |
| `catalog/controller/product/backup_yml/yml.php` | 55–57 | Backup copy — same legacy shop strings | YML | INTERNAL | LOW | W1F-E |
| `catalog/controller/product/backup_yml/ymlnew.php` | 55–57 | Backup copy — same legacy shop strings | YML | INTERNAL | LOW | W1F-E |
| `catalog/controller/product/product.php` | 304–305 | `setTitle` / `setDescription` suffix `\| АЦ Хмельницкий` | SEO | PUBLIC | HIGH | W1F-A |
| `catalog/controller/product/category.php` | 143–156 | `setTitle`, `setDescription`, `heading_title` — «АЦ Хмельницкий» | SEO | PUBLIC | HIGH | W1F-A |
| `catalog/view/theme/auto/template/product/productnew.twig` | 405 | `{{ heading_title }} в наличии - АЦ Хмельницкий` | BRAND | PUBLIC | HIGH | W1F-A |
| `catalog/view/theme/auto/template/product/category_backup.twig` | 486–542 (×5) | Review quote: «Автосалон Ац Хмельницкий» | BRAND | PUBLIC | HIGH | W1F-A |
| `admin/view/template/catalog/product_form.twig` | 2202, 2211 | JS SEO title template `\| АЦ Хмельницкий` | ADMIN | ADMIN | MEDIUM | W1F-E |
| `catalog/controller/checkout/anketa.php` | 89 | `$email_login = 'send@xn----7sbqmagfghm8fkh5f.xn--p1ai'` | SMTP | INTERNAL | CRITICAL | W1F-D |
| `admin:oc_setting/config_mail_smtp_username` | W1A report | `send@ац-хмельницкий.рф` | SMTP | ADMIN | CRITICAL | W1F-D |
| `HTTP:/privacy-policy` | `<title>` + body | `\| АЦ Хмельницкий` · `ац-хмельницкий.рф` (×4 body refs) | LEGAL | PUBLIC | HIGH | W1F-B |
| `HTTP:/user-agreement` | `<title>` + body | `\| АЦ Хмельницкий` · `ац-хмельницкий.рф` (×7 body refs) | LEGAL | PUBLIC | HIGH | W1F-B |
| `HTTP:/loan-terms` | `<title>`, meta | `АЦ «Хмельницкий»` | LEGAL | PUBLIC | HIGH | W1F-B |
| `HTTP:/autocredit` | `<title>`, body, H2 | `АЦ Хмельницкий` · `ац-хмельницкий.рф` · `«АЦ Хмельницкий»` | BRAND | PUBLIC | HIGH | W1F-B |
| `HTTP:/tradein` | `<title>`, body, H2 | `АЦ Хмельницкий` · `«АЦ Хмельницкий»` | BRAND | PUBLIC | HIGH | W1F-B |
| `HTTP:/about_us` | `<title>` | `Вавилон` | HISTORICAL | PUBLIC | LOW | W1F-B |
| `img/logo - hmel.svg` | filename | `logo - hmel.svg` | ORPHAN | INTERNAL | LOW | W1F-E |
| `image/catalog/logo_balck.png` | filename *(W1D)* | Legacy admin logo asset | ORPHAN | ADMIN | LOW | W1F-E |

### Surfaces verified CLEAN (no legacy brand in probe)

| URL | Wave that fixed | Probe result |
|-----|-----------------|--------------|
| `/` | W1A + W1B | **CLEAN** |
| `/about` | W1B + W1C | **CLEAN** |
| `/contact/` | W1B + W1C | **CLEAN** |

---

## Legacy Inventory Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 6 |
| HIGH | 12 |
| MEDIUM | 1 |
| LOW | 4 |
| IGNORE (GEOGRAPHICAL_REFERENCE) | 4 |

*Counts = consolidated inventory rows above, not raw regex match multiplicity (raw FTP+HTTP term matches: 91; deduplicated meaningful locations: 23 + 4 geo).*

---

## Remaining Legacy Risk Assessment

| Risk ID | Description | Severity | Likelihood | Impact |
|---------|-------------|----------|------------|--------|
| R-W1F-01 | YML feeds advertise legacy legal entity + legacy domain to aggregators | **CRITICAL** | **Certain** (live XML confirmed) | Wrong brand/company in Yandex/Market listings |
| R-W1F-02 | SMTP username + anketa hardcoded sender use legacy domains | **CRITICAL** | **High** | Mail delivery failure or wrong sender identity on forms |
| R-W1F-03 | Legal pages (privacy, user-agreement) reference `ац-хмельницкий.рф` and «АЦ Хмельницкий» | **HIGH** | **Certain** | Compliance / consumer-facing legal mismatch |
| R-W1F-04 | Product/category SEO templates append legacy brand to every vehicle page | **HIGH** | **Certain** | SERP titles/descriptions show old brand at scale |
| R-W1F-05 | `robots.txt` Host/Sitemap off-domain | **HIGH** | **Certain** | SEO crawlers directed to legacy production host |
| R-W1F-06 | Service landings (autocredit, tradein, loan-terms) still legacy | **HIGH** | **Certain** | Marketing pages inconsistent with W1A/B/C |
| R-W1F-07 | Admin product form JS seeds legacy SEO pattern | **MEDIUM** | **High** | New/edited products inherit legacy titles |
| R-W1F-08 | Orphan legacy logo files on disk | **LOW** | **Low** | No public reference today; clutter / accidental reuse risk |
| R-W1F-09 | Un-scanned language/module files | **LOW** | **Unknown** | Requires extended grep when FTP throughput allows |

**Overall W1F verdict:** **FAIL** — legacy dictionary hits remain on **EXPORT**, **SMTP**, **LEGAL**, and **product SEO** surfaces. W1A/B/C/D objectives met for their scoped slices; **Phase 1 TEST is not complete** until W1F remediation waves execute.

---

## Recommended Execution Order

| Wave | Scope | Priority | Rationale |
|------|-------|----------|-----------|
| **W1F-C** | Exports / YML + `robots.txt` Host/Sitemap | **1 — Immediate** | External aggregator exposure; SEO infra |
| **W1F-D** | SMTP — `config_mail_smtp_username`, `anketa.php` sender | **2 — Immediate** | Mail identity / deliverability |
| **W1F-B** | Legal / service information pages (admin Catalog → Information) | **3 — High** | Compliance-facing copy |
| **W1F-A** | Public product SEO — `product.php`, `category.php`, `productnew.twig`, `category_backup.twig` | **4 — High** | High-volume SERP surfaces |
| **W1F-E** | Admin cleanup — `product_form.twig`, backup YML copies, orphan assets | **5 — Medium** | Prevents reintroduction; disk hygiene |

**Post-remediation:** Re-run W1F inventory (this document's methodology) → expect **0 CRITICAL/HIGH** hits outside GEOGRAPHICAL_REFERENCE and intentional HOLD items per execution pack.

---

## UNKNOWN / limitations

| Item | Status |
|------|--------|
| Admin live read-back (settings + information forms) | **SAFE UNKNOWN** — admin session token not obtained this run; HTTP + W1A report used |
| `config_mail_smtp_hostname` current value | **SAFE UNKNOWN** — not captured live |
| Full `catalog/language` + `admin/language` exhaustive grep | **Not completed** — FTP throughput |
| `system/storage` modification caches | **Not scanned** — expected compiled copies; clear after remediation |
| Latin slug variants (`auto-center-hmelnickiy`, etc.) | **Not found** in scanned set |
| Production environment | **Not scanned** — TEST only per charter |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **CREATED** — SITE-001 W1F full legacy sweep inventory report (read-only) |

*SITE-001 W1F Legacy Sweep v1 — TEST only; no modifications; no commit; no push.*
