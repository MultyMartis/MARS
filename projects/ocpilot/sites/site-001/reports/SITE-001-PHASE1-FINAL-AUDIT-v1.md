# REPORT — SITE-001 Phase 1 Final Audit v1

**Type:** Final Phase 1 public + code-path audit — **read-only**  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Prior checkpoint:** [SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md](SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md)

**Explicit exclusions (honored):** No site modifications. No remediation performed.

**Evidence:** `.recovery-temp/site-001-phase1-final-audit-utf8.json` · prior wave reports W1A–W1F-A

---

## Executive summary

Automated HTTP audit of **14 core URLs** shows **12 CLEAN**, **1 FAIL** (`/auto/`), **1 operator-attested FAIL** (new car product detail — no product URLs discoverable in automated crawl).

Primary residual pattern: **SEO meta not fully controlled by admin store settings** — legacy brand persists in **database-stored category/product meta** and **admin JS SEO generators**, while controller hardcoded fallbacks for manufacturer pages were remediated in W1F-A.

**Geographic exception:** `ул. Богдана Хмельницкого` — **4–5 hits per page** — classified **GEOGRAPHICAL_REFERENCE**.

---

## 1. Public URL audit

### 1.1 Required URLs

| URL | HTTP | Title (excerpt) | Meta description | Legacy hits | Header/Footer СИБКАР | Verdict |
|-----|------|-----------------|------------------|-------------|----------------------|---------|
| `/` | 200 | `… \| СИБКАР` | Автосалон СИБКАР… | **0** | **YES** | **CLEAN** |
| `/about` | 200 | Об автосалоне **СИБКАР**… | СИБКАР – автосалон… | **0** | **YES** | **CLEAN** |
| `/contact/` | 200 | Контакты **СИБКАР**… | Контакты автосалона СИБКАР… | **0** | **YES** | **CLEAN** |
| `/privacy-policy` | 200 | …\| **СИБКАР**, Новосибирск | Политика… «СИБКАР» | **0** | **YES** | **CLEAN** |
| `/user-agreement` | 200 | …\| **СИБКАР**, Новосибирск | …автосалона «СИБКАР» | **0** | **YES** | **CLEAN** |
| `/autocredit` | 200 | …\| **СИБКАР** | СИБКАР – низкие ставки… | **0** | **YES** | **CLEAN** |
| `/tradein` | 200 | …\| **СИБКАР** | …в СИБКАР, Новосибирск | **0** | **YES** | **CLEAN** |
| `/loan-terms` | 200 | …в **СИБКАР**… | Автокредит в СИБКАР… | **0** | **YES** | **CLEAN** |
| `/cookie-files-policy` | 200 | …\| **СИБКАР**, Новосибирск | …«СИБКАР» | **0** | **YES** | **CLEAN** |
| `/cars/bmw` | 200 | …\| **СИБКАР** | …в СИБКАР… | **0** | **YES** | **CLEAN** |
| `/cars/hyundai` | 200 | …\| **СИБКАР** | …в СИБКАР… | **0** | **YES** | **CLEAN** |

### 1.2 New-car surfaces (extended probe)

| URL | HTTP | Title | Legacy hits | Verdict |
|-----|------|-------|-------------|---------|
| `/auto/` | 200 | Каталог новых автомобилей… **\| АЦ Хмельницкий** | `АЦ Хмельницкий` ×2 | **FAIL** |
| `/auto/haval` | 200 | …\| **СИБКАР** | **0** | **CLEAN** |
| `/auto/geely` | 200 | …\| **СИБКАР** | **0** | **CLEAN** |

### 1.3 Product detail pages

| Type | Automated discovery | Audit result |
|------|---------------------|--------------|
| Used car product | **0 URLs** found on `/`, `/cars/bmw`, `/cars/hyundai` | **NOT VERIFIED** — operator reports used car page **CLEAN** (visible body + branding) |
| New car product | **0 URLs** found on `/`, `/auto/haval`, `/auto/geely` | **OPERATOR FAIL** — browser title contains `АЦ Хмельницкий`; consistent with DB `meta_title` + admin JS pattern |

**Root cause (code analysis, not remediated):**

- Used cars (`category_id == 60`): `product.php` lines 304–305 **override** title/description with brand suffix — **remediated W1F-A** → `\| СИБКАР`
- New cars (`category_id == 59`): `product.php` lines 179–181 use **`$product_info['meta_title']` from database** — no controller brand override; admin `product_form.twig` JS seeds `\| АЦ Хмельницкий`

---

## 2. Per-URL field audit (core pages)

Legend: **C** = clean · **G** = geographical only · **L** = legacy hit

| URL | Title | Meta desc | Meta kw | H1 | Breadcrumbs | Body | Footer | Header |
|-----|-------|-----------|---------|-----|-------------|------|--------|--------|
| `/` | C | C | C | C | nav only | C | C | C |
| `/about` | C | C | C | C | nav only | C | C | C |
| `/contact/` | C | C | C | C | nav only | C | C | C |
| `/privacy-policy` | C | C | n/a | C | nav only | C | C | C |
| `/user-agreement` | C | C | n/a | C | nav only | C | C | C |
| `/autocredit` | C | C | n/a | C | nav only | C | C | C |
| `/tradein` | C | C | n/a | C | nav only | C | C | C |
| `/loan-terms` | C | C | n/a | C | nav only | C | C | C |
| `/cookie-files-policy` | C | C | n/a | C | nav only | C | C | C |
| `/cars/bmw` | C | C | n/a | C | nav only | C | C | C |
| `/cars/hyundai` | C | C | n/a | C | nav only | C | C | C |
| `/auto/` | **L** | **L** | n/a | C | nav only | C *(H1 clean)* | C | C |

**Breadcrumbs note:** Primary nav menu items (Главная, Новые авто, …) — no legacy brand suffix in crumbs.

---

## 3. Legacy search dictionary results

Search terms applied to full HTML of each probed URL.

| Term | Hits on audited pages | Notes |
|------|----------------------|-------|
| `АЦ Хмельницкий` | **`/auto/` only** (×2) | Title + meta description |
| `Автоцентр Хмельницкий` | **0** | — |
| `ООО «АЦ Хмельницкий»` | **0** | — |
| `АЦ «Хмельницкий»` | **0** | — |
| `Хмельницкий` *(brand)* | **`/auto/`** (×2, overlaps with above) + **geo** on all pages | Geo excluded |
| `ац-хмельницкий.рф` | **0** | — |
| `xn----7sbqmagfghm8fkh5f` | **0** | — |
| `Hmelnickiy` | **0** | — |
| `Khmelnitskiy` | **0** | — |
| `ул. Богдана Хмельницкого` | **4–5 per page** | **GEOGRAPHICAL_REFERENCE — IGNORE** |

---

## 4. Controller meta generator audit

See full table in §4.1. Method: read-only review of FTP-downloaded artefacts, wave execution backups, and W1F legacy sweep JSON (2026-06-08). Post-W1F-A/C1/B controller sources verified clean for **hardcoded** fallback strings; **DB-sourced** meta not re-scanned live.

### 4.1 Meta generator inventory

| File | Line | Pattern | Generated surface | Current risk | Recommended wave |
|------|------|---------|-------------------|--------------|------------------|
| `catalog/controller/product/product.php` | 179–181 | `$this->document->setTitle($product_info['meta_title'])` | New + used product pages *(DB passthrough)* | **HIGH** — DB values may contain legacy | **W1G** |
| `catalog/controller/product/product.php` | 304–305 | `setTitle` / `setDescription` with `\| СИБКАР` | Used product pages only (`category_id == 60`) | **LOW** — remediated W1F-A | — |
| `catalog/controller/product/category.php` | 143–161 | `setTitle` / `setDescription` / `heading_title` / `description` fallbacks | `/auto/{brand}`, `/cars/{brand}` when manufacturer set | **LOW** — remediated W1F-A | — |
| `catalog/controller/product/category.php` | 168–172 | `setTitle($category_info['meta_title'])` | `/auto/` root, category pages without manufacturer | **HIGH** — `/auto/` live legacy confirmed | **W1G** |
| `catalog/controller/information/about.php` | 8–10 | Hardcoded `setTitle` / `setDescription` / `setKeywords` | `/about` | **LOW** — remediated W1C | — |
| `catalog/controller/information/contact.php` | 8–10 | Hardcoded `setTitle` / `setDescription` / `setKeywords` | `/contact/` | **LOW** — remediated W1C | — |
| `catalog/controller/product/yml.php` | 55–57 | Hardcoded YML shop block | `/data/yandex-bu.xml` | **LOW** — remediated W1F-C1 | — |
| `catalog/controller/product/ymlnew.php` | 55–57 | Hardcoded YML shop block | `/data/yandex.xml` | **LOW** — remediated W1F-C1 | — |
| `catalog/controller/product/backup_yml/yml.php` | 55–57 | Backup YML shop block | Inactive | **LOW** | **W1F-E** |
| `catalog/controller/product/backup_yml/ymlnew.php` | 55–57 | Backup YML shop block | Inactive | **LOW** | **W1F-E** |
| `catalog/controller/checkout/anketa.php` | 89 | `$email_login = 'send@xn----7sbqmagfghm8fkh5f.xn--p1ai'` | Form mail sender | **CRITICAL** | **W1F-D** |
| `admin/view/template/catalog/product_form.twig` | 2202, 2211 | JS: `'… \| АЦ Хмельницкий'` meta title template | Admin product edit → DB `meta_title` | **HIGH** | **W1F-E** / **W1G** |
| `catalog/view/theme/auto/template/product/productnew.twig` | 405 | `{{ heading_title }} в наличии - СИБКАР` | New car product visible span | **LOW** — remediated W1F-A | — |
| `catalog/view/theme/auto/template/product/productnew_Backup.twig` | 376 | Legacy brand in backup template | Inactive unless switched | **LOW** | **W1F-E** |
| `catalog/view/theme/auto/template/product/category_backup.twig` | 486–542 | Review quotes | Inactive on live category render | **LOW** — remediated W1F-A | — |
| `oc_category_description` *(DB)* | category_id **59** | `meta_title`, `meta_description` | `/auto/` catalog root | **HIGH** — live confirmed | **W1G** |
| `oc_product_description` *(DB)* | new-car products | `meta_title`, `meta_description`, `meta_keyword` | `/auto/{brand}/{model}` product pages | **HIGH** — operator confirmed | **W1G** |
| `oc_manufacturer` *(DB)* | `TitleNew`, `DescrNew`, etc. | Per-brand SEO overrides | `/auto/{brand}` when set | **SAFE UNKNOWN** | **W1G** verify |

### 4.2 Key learning — asymmetric meta logic

Developer pattern on this site (associated in ATLAS with **ИП Дьяконов Сергей** — intake candidate, not fully populated):

```
Used cars (cat 60):  controller OVERRIDE → brand suffix in PHP
New cars (cat 59):   DB meta_title PASSTHROUGH → no override
Category root /auto/: DB category meta_title → no manufacturer fallback path
```

W1F-A fixed controller **fallback strings** but did not update **database SEO records** or **admin JS generators**.

---

## 5. Out-of-scope deferred items (inventory)

| Item | Wave | Severity |
|------|------|----------|
| `config_mail_smtp_username` = `send@ац-хмельницкий.рф` | W1F-D | CRITICAL |
| `anketa.php` punycode sender | W1F-D | CRITICAL |
| `backup_yml/` copies | W1F-E | LOW |
| Orphan `img/logo - hmel.svg` | W1F-E | LOW |
| C-04 WhatsApp URL hold | W1B | OPEN |
| C-10 Admin URL on access brief | All | OPEN |

---

## 6. Audit verdict

| Criterion | Result |
|-----------|--------|
| Core public pages (11 required URLs) | **PASS** — 11/11 CLEAN |
| New car catalog root `/auto/` | **FAIL** — legacy in title + meta |
| New car product detail HTTP | **NOT VERIFIED** — operator FAIL attested |
| Used car product detail HTTP | **NOT VERIFIED** — operator PASS attested |
| Controller hardcoded generators (scoped files) | **PASS** — W1F-A/C1/C remediated |
| DB + admin JS meta generators | **FAIL** — residual HIGH |
| Geographic exception handling | **PASS** |
| Production touched | **NO** |

**Overall final audit verdict:** **PASS WITH NOTES** — Phase 1 visually and structurally stable; **meta/SEO layer incomplete** for new-car surfaces.

---

## 7. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Live new/used product URL sample | Automated crawl returned **zero** product detail links — inventory may be JS-loaded or session-gated |
| Manufacturer custom SEO DB fields (`TitleNew`, etc.) | Not read live — **SAFE UNKNOWN** |
| `config_mail_smtp_hostname` current value | **SAFE UNKNOWN** |
| Full `catalog/language` exhaustive grep | Not completed in W1F sweep |
| Production environment | **Not scanned** |

*SITE-001 Phase 1 Final Audit v1 — TEST only; read-only; no commit.*
