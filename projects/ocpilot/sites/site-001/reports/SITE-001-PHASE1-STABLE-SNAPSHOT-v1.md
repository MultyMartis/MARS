# SITE-001 — Phase 1 Stable Snapshot v1

**Type:** Stable checkpoint report — **read-only documentation**  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Platform:** ocStore **3.0.3.8 (rs.2)** · active theme **`auto`**

**Purpose:** Record the operationally stable Phase 1 state after W1A–W1F-A execution waves, prior to final audit closure and deferred remediation.

**Explicit exclusions (honored):** No site modifications. No FTP writes. No admin writes. No cache clears.

---

## Executive summary

Phase 1 brand replacement on TEST is **operationally successful** for scoped execution waves W1A through W1F-A. Operator visual QA confirms **СИБКАР** on homepage, used-car surfaces, header/footer, and replaced logos/favicon.

Phase 1 is **not fully closed** until final audit remediation of remaining **generated meta patterns** and **database-stored SEO fields** (notably new-car catalog root `/auto/` and new-car product `meta_title` values).

**Checkpoint verdict:** **STABLE WITH KNOWN RESIDUALS**

---

## Current visible state (operator + automated)

| Surface | Status | Evidence |
|---------|--------|----------|
| Homepage `/` | **СИБКАР** — title, H1, header, footer | W1A + W1B · operator QA · final audit HTTP 2026-06-09 |
| Used car category `/cars/bmw`, `/cars/hyundai` | **СИБКАР** — title, meta, H1 | W1F-A · final audit HTTP |
| New car manufacturer `/auto/haval`, `/auto/geely` | **СИБКАР** — title, meta, H1 | W1F-A · final audit HTTP |
| `/about`, `/contact/` | **СИБКАР** — controller meta + theme | W1B + W1C |
| Legal / service pages | **СИБКАР** — titles and body | W1F-B |
| Logos + favicon | **Replaced** — СИБКАР assets live | W1D · operator QA |
| New car catalog root `/auto/` | **LEGACY in title + meta** — `АЦ Хмельницкий` | Final audit HTTP 2026-06-09 |
| New car product detail pages | **LEGACY in browser title** *(operator-reported)* | Operator visual QA · code path analysis — automated product URL probe **empty** |

**Geographic exception preserved:** `ул. Богдана Хмельницкого 101` on all probed pages — **GEOGRAPHICAL_REFERENCE**, not brand failure.

---

## Waves completed

| Wave | Scope | Verdict | Date |
|------|-------|---------|------|
| **W1A** | Store Settings (admin) | **PASS WITH NOTES** | 2026-06-08 |
| **W1A Post-Audit** | Unicode / mixed-script check | **PASS** | 2026-06-08 |
| **W1B** | Theme branding (`auto`) | **PASS** | 2026-06-08 |
| **W1C** | Custom controllers `/about`, `/contact/` | **PASS** | 2026-06-08 |
| **W1D** | Logos + favicon | **PASS WITH NOTES** | 2026-06-08 |
| **W1F-C1** | YML generators + `robots.txt` | **PASS WITH NOTES** | 2026-06-08 |
| **W1F-B** | Legal / information pages (admin) | **PASS WITH NOTES** | 2026-06-08 |
| **W1F-A** | Product/category SEO controllers + templates | **PASS WITH NOTES** | 2026-06-08 |

**Not executed (deferred):**

| Wave | Scope | Status |
|------|-------|--------|
| **W1F-D** | SMTP — `config_mail_smtp_username`, `anketa.php` sender | **DEFERRED** |
| **W1F-E** | Admin `product_form.twig`, backup YML, orphan assets | **DEFERRED** |
| **W1G** *(proposed)* | DB product/category SEO bulk + new-car meta gap | **NOT AUTHORIZED** |

---

## What is clean

- Store settings brand fields (`config_name`, meta title/description/keyword, owner, email)
- Theme visible copy: header, footer, home, about/contact twigs
- Custom information controllers: `about.php`, `contact.php`
- Logo SVG set + favicon pack
- YML shop-level metadata + `robots.txt` Host/Sitemap (W1F-C1)
- Legal and service information pages (11 records)
- Used-car manufacturer category SEO (`/cars/*`) — controller-generated meta remediated
- New-car manufacturer category SEO (`/auto/{brand}`) — controller fallback remediated

---

## What remains known

| ID | Surface | Nature | Severity |
|----|---------|--------|----------|
| R-P1-01 | `/auto/` catalog root — `<title>` + meta description | **DB category meta** (`oc_category_description`, category_id **59**) — not controller fallback | **HIGH** |
| R-P1-02 | New car **product detail** browser titles | **DB product meta** (`oc_product_description.meta_title`) seeded by admin JS; category **59** uses DB meta without controller override | **HIGH** |
| R-P1-03 | `admin/view/template/catalog/product_form.twig` | JS SEO title template `\| АЦ Хмельницкий` — re-seeds legacy on edit | **MEDIUM** |
| R-P1-04 | `config_mail_smtp_username` | Legacy Cyrillic sender domain | **CRITICAL** *(mail identity)* |
| R-P1-05 | `catalog/controller/checkout/anketa.php:89` | Hardcoded punycode sender | **CRITICAL** *(mail identity)* |
| R-P1-06 | `catalog/controller/product/backup_yml/*.php` | Inactive backup YML copies | **LOW** |
| R-P1-07 | `productnew_Backup.twig` | Backup template — legacy at line 376 | **LOW** |
| R-P1-08 | Manufacturer custom SEO fields (`TitleNew`, `DescrNew`, etc.) | Per-manufacturer DB overrides — **SAFE UNKNOWN** if any retain legacy | **MEDIUM** |

---

## Operator QA references

| Check | Source | Result |
|-------|--------|--------|
| СИБКАР visible on homepage | Operator visual QA | **PASS** |
| СИБКАР on used car product page | Operator visual QA | **PASS** |
| СИБКАР in footer/header | Operator visual QA | **PASS** |
| Logos and favicon replaced | Operator visual QA | **PASS** |
| New car product page title still shows `АЦ Хмельницкий` | Operator visual QA | **FAIL** — drives final audit focus |

**Screenshots:** Not stored in repository. Operator session evidence only.

---

## Rollback status

| Tier | Status | Reference |
|------|--------|-----------|
| Pre-W1 operator backup (Beget) | **Available** — operator-confirmed 2026-06-08 | [SITE-001-W1-BACKUP-PROCEDURE-v1.md](SITE-001-W1-BACKUP-PROCEDURE-v1.md) |
| Per-wave FTP backups | **Available** — W1F-A, W1F-C1, W1F-B, W1D | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\` |
| Rollback plan | **Documented** | [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) |
| Independent restore drill | **SAFE UNKNOWN** | Not executed |

---

## Backup recommendation

Before any W1G / W1F-D / W1F-E remediation:

1. Execute fresh Beget file + DB backup per [SITE-001-W1-BACKUP-PROCEDURE-v1.md](SITE-001-W1-BACKUP-PROCEDURE-v1.md)
2. Export `oc_product_description` + `oc_category_description` for categories **59**, **60** before bulk SQL
3. Record backup manifest in external storage reports folder

---

## Readiness for next phase

| Gate | Status |
|------|--------|
| Phase 1 execution waves (W1A–W1F-A) | **DONE** on TEST |
| Final audit | **IN PROGRESS** — see [SITE-001-PHASE1-FINAL-AUDIT-v1.md](SITE-001-PHASE1-FINAL-AUDIT-v1.md) |
| Production deployment | **NOT AUTHORIZED** |
| Recommended next wave | **W1G** — DB SEO bulk + category 59 root + admin product form |
| OCPilot inspection rule | **CREATED** — [OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md](../../knowledge/OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md) |

**Closure statement:** Phase 1 is operationally successful but **not fully closed** until final audit remediation of remaining generated meta patterns and database-stored SEO fields.

---

## Evidence artefacts (local, not in git)

| Artefact | Path |
|----------|------|
| Final audit HTTP JSON | `.recovery-temp/site-001-phase1-final-audit-utf8.json` |
| W1F legacy sweep | `.recovery-temp/site-001-w1f-legacy-sweep.json` |
| W1F-A execution evidence | `.recovery-temp/site-001-w1f-a-result.json` |

*SITE-001 Phase 1 Stable Snapshot v1 — TEST only; documentation only; no commit.*
