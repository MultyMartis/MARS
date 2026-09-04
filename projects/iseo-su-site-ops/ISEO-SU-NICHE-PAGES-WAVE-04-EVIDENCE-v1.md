# ISEO-SU NICHE PAGES WAVE 04 EVIDENCE v1

**Task ID:** `ISEO-SU-SITE-OPS-NICHE-PAGES-WAVE-04`  
**Date:** 2026-09-04  
**Class:** CURRENT / CANONICAL evidence for WAVE 4

---

## 1. Scope

Create seven static niche SEO landings under `/services/seo/`, cloned from production-current `prodvizhenie-avtomobilnogo-sajta.html` (post-consent PHP includes). Add seven niche links to `services/seo.html`. Add seven URLs to canonical static sitemap inventory; regenerate `sitemap-static.xml` (**132 → 139**). Self-canonical + indexable. Preserve form consent + calculator-result consent. Pitomnik-only case swap to Maltipoo Honey Club.

Production mutations: **7 new HTML** + updated `services/seo.html` + regenerated `sitemap-static.xml`.

---

## 2. Source Page

| Field | Value |
|-------|-------|
| Live URL | `https://i-seo.su/services/seo/prodvizhenie-avtomobilnogo-sajta.html` |
| MARS SoT | `production-source/static-html/services/seo/prodvizhenie-avtomobilnogo-sajta.html` |
| Clone method | Source HTML with PHP includes (not live-rendered HTML) |
| Consent | via `content-form-seo.php`, `content-seo-popups.php`, `tarif-calc.php` |
| Source canonical | absent on source → **new pages add self-canonical** |
| Source case | Drive Avenue (kept on 6/7 pages) |
| Forensic tool | `tools/_wave04_forensic_fetch.py` → `tools/_wave04_forensic_report.json` |

---

## 3. New URL Inventory

| # | URL |
|---|-----|
| 1 | `https://i-seo.su/services/seo/prodvizhenie-sajta-pitomnika.html` |
| 2 | `https://i-seo.su/services/seo/prodvizhenie-sajta-smi.html` |
| 3 | `https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html` |
| 4 | `https://i-seo.su/services/seo/prodvizhenie-internet-magazina-zapchastej.html` |
| 5 | `https://i-seo.su/services/seo/prodvizhenie-sajta-internet-provajdera.html` |
| 6 | `https://i-seo.su/services/seo/prodvizhenie-internet-magazina-kosmetiki.html` |
| 7 | `https://i-seo.su/services/seo/prodvizhenie-internet-magazina-czvetov.html` |

No Word soft-hyphen / NBSP artifacts in filenames.

---

## 4. Content Mapping

Per page, only: `<title>`, `meta description`, H1, first intro after H1, last breadcrumb. Unchanged: metrics, tariffs, stages, inclusions, calculator, promos, team, reviews, FAQ×4, free audit, other services, secondary automotive body H2s.

Title suffix: `| i-seo.su` (charter).

| File | Title | H1 |
|------|-------|----|
| pitomnika | Заказать SEO продвижение сайта питомника \| i-seo.su | SEO продвижение сайта питомника |
| smi | Заказать SEO продвижение сайта СМИ под ключ \| i-seo.su | SEO продвижение сайта СМИ |
| restorana | Заказать SEO продвижение сайта ресторана \| i-seo.su | SEO продвижение сайта ресторана |
| zapchastej | SEO продвижение интернет-магазина запчастей \| i-seo.su | SEO продвижение интернет-магазина запчастей |
| provajdera | SEO продвижение сайта интернет-провайдера \| i-seo.su | SEO продвижение сайта интернет-провайдера |
| kosmetiki | SEO продвижение интернет-магазина косметики \| i-seo.su | SEO продвижение интернет-магазина косметики |
| czvetov | Заказать SEO продвижение интернет-магазина цветов \| i-seo.su | SEO продвижение интернет-магазина цветов |

**CONTENT MAPPING EXACT: YES** (local QA + live 7/7)

---

## 5. Breadcrumb Mapping

Last breadcrumb level = full niche H1 string (not compact automotive source «автомобильного сайта»). Parents preserved.

**BREADCRUMB MAPPING EXACT: 7/7**

---

## 6. Pitomnik Case Verification

| Check | Result |
|-------|--------|
| URL | `https://i-seo.su/cases/maltipoo-honey-club.html` |
| HTTP | 200 |
| Identity | Maltipoo Honey Club |
| Case image | `img/cases/maltipoo-honey-club.png` HTTP 200 |
| STOP | not triggered |

---

## 7. Case Policy

| Page | Policy | Live |
|------|--------|------|
| Pitomnik | Replace Drive Avenue → Maltipoo Honey Club (metrics 120+ / 5,5% / 2300+ / 44+ / 67) | YES |
| Other 6 | Keep Drive Avenue from source | unchanged |

**PITOMNIK CASE REPLACED: YES** · **OTHER 6 CASE BLOCKS CHANGED: NO**

---

## 8. Form Consent Preservation

Live per page: `personal_data_consent` present (10 fields); privacy `https://i-seo.su/privacy-policy.html`; calculator-result consent present; HMAC/antispam/recipient unchanged (`nikel007i33@yandex.ru` only).

**FORM CONSENT COVERED: 7/7** · **CALCULATOR RESULT CONSENT COVERED: YES** · **FORM REGRESSION: NONE**

---

## 9. Services SEO Hub

| Field | Value |
|-------|-------|
| Page | `https://i-seo.su/services/seo.html` |
| Niche links before | **31** |
| Niche links after | **38** |
| New links | 7/7 |
| Hub labels | exact charter strings (capital **И** on shop items); markup uses `SEO&nbsp;продвижение…` like existing items |
| Targets | 7/7 HTTP 200 |

---

## 10. Canonical / Indexability

All 7: self-canonical exact URL; `robots` `index, follow`; no noindex; HTTP 200; canonical target 200. Global `robots.txt` unchanged.

**SELF-CANONICAL: 7/7** · **INDEXABLE: 7/7**

---

## 11. Sitemap Inventory

Updated both:

- `data/sitemaps/sitemap-static-urls-v1.txt`
- `data/sitemaps/public-canonical-static-routes-v1.txt`

Tool: `tools/_wave04_update_sitemap_inventory.py`

---

## 12. Sitemap Regeneration

| Step | Result |
|------|--------|
| Generator | `tools/generate-sitemap-static.py` |
| Output | `production-source/sitemaps/sitemap-static.xml` |
| Count before | **132** |
| Count after | **139** |
| Delta | +7 |

---

## 13. Completeness Validation

`tools/validate-sitemap-static-completeness.py`:

- `PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS = 0`
- New niche URLs 7/7 present once
- Duplicates 0
- Completeness **PASS**

---

## 14. Production Backup

Root: `X:\AI MARS\local\sites\iseo-su-production\_niche-pages-wave-04\`  
Stamp: `backup-20260904T042424Z`

| Item | Action |
|------|--------|
| 7 niche pages | CREATE (DEPLOYED-* copies post-upload) |
| `services/seo.html` | BEFORE + DEPLOYED |
| `sitemap-static.xml` | BEFORE + DEPLOYED |
| `manifest.json` | recorded |

---

## 15. Deployment

SFTP to Beget `public_html`. Deployed only:

- 7 niche HTML under `services/seo/`
- `services/seo.html`
- `sitemap-static.xml`

Checksum verify after upload: OK. Tool: `tools/_wave04_backup_deploy_validate.py` → `tools/_wave04_deploy_validate.json`

---

## 16. Live Validation

All 7 pages: HTTP 200; exact title/description/H1/intro/breadcrumb; case policy; self-canonical; indexable; forms/calc consent; CSS/JS OK. No automotive title/H1/breadcrumb leakage.

---

## 17. Hub Validation

Live hub HTTP 200; niche count 31→38; 7 new targets + labels; consent unaffected.

---

## 18. Sitemap Validation

Live `sitemap-static.xml` HTTP 200; 139 URLs; 7 new present once; duplicates 0. Root `sitemap.xml` HTTP 200; still references static + WP sitemaps.

---

## 19. Regression

Bounded smoke all HTTP 200: `/`, hub, automotive source, `b-regionakh`, USA, UAE, `/tariff-calc`, `/sitemap.xml`, `/sitemap-static.xml`.

---

## 20. Production / Source Alignment

Accepted production bytes match MARS SoT under `production-source/static-html/` and `production-source/sitemaps/`. No production-only hotfix tail.

---

## 21. Rollback

Restore from `_niche-pages-wave-04/backup-20260904T042424Z/`: delete 7 CREATEs; restore `seo.html` + `sitemap-static.xml` BEFORE copies; optionally restore inventory to pre-+7 and regenerate.

---

## 22. Final Decision

**COMPLETE — ISEO-SU NICHE PAGES WAVE 04 / 7 NEW SEO LANDINGS LIVE / SERVICES SEO HUB UPDATED / SITEMAP UPDATED**

| Hard check | Value |
|------------|-------|
| NICHE PAGES CREATED | 7 |
| NICHE PAGE HTTP 200 | 7/7 |
| CONTENT MAPPING EXACT | YES |
| BREADCRUMB MAPPING EXACT | 7/7 |
| PITOMNIK CASE VALID | YES |
| PITOMNIK CASE REPLACED | YES |
| OTHER 6 CASE BLOCKS CHANGED | NO |
| SELF-CANONICAL | 7/7 |
| INDEXABLE | 7/7 |
| SERVICES SEO HUB LINKS BEFORE | 31 |
| SERVICES SEO HUB LINKS AFTER | 38 |
| NEW NICHE HUB LINKS | 7/7 |
| NEW NICHE HUB TARGETS VALID | 7/7 |
| FORM CONSENT COVERED | 7/7 |
| CALCULATOR RESULT CONSENT COVERED | YES |
| FORM REGRESSION | NONE |
| STATIC SITEMAP URL COUNT BEFORE | 132 |
| STATIC SITEMAP URL COUNT AFTER | 139 |
| NEW NICHE URLS IN SITEMAP | 7/7 |
| SITEMAP DUPLICATES | 0 |
| SITEMAP 4XX | 0 |
| SITEMAP 5XX | 0 |
| STATIC/WP OVERLAP | 0 |
| COMPLETENESS VALIDATION | PASS |
| ROOT SITEMAP HEALTH | PASS |
| PRODUCTION/SOURCE ALIGNED | YES |
| UNAPPROVED CONTENT CHANGES | 0 |
| UNRELATED SEO CHANGES | 0 |
| PROJECT-OWNED UNCOMMITTED | 0 |
| FOREIGN WIP PRESERVED | YES |
| REMOTE SYNC | COMPLETE (`4e20c5bd` on `origin/mars/canonical-post-recovery`) |

Source SHA256 (SoT):

| File | SHA256 | Bytes |
|------|--------|-------|
| prodvizhenie-sajta-pitomnika.html | `452c90e82744372318082edeca8793d89f321528e7e446afd5c7de47f2dd2b12` | 41223 |
| prodvizhenie-sajta-smi.html | `971022ff27827c325285788e76201f92ae4460442e33357eb0d1a9b59c812cea` | 40844 |
| prodvizhenie-sajta-restorana.html | `7c48a8ea2060b770d102ff6f9d260c3d03f4af5880a3f59c8bb0893a832e639f` | 40706 |
| prodvizhenie-internet-magazina-zapchastej.html | `53b2b058b82ea157b79db28567aa379a20412b9f41e39060507dfb93aaa4a95f` | 40919 |
| prodvizhenie-sajta-internet-provajdera.html | `b6798868d65418e88b1ce79bafcfeacf3cd61ac1f40236ce498004a43d355f5a` | 40870 |
| prodvizhenie-internet-magazina-kosmetiki.html | `5813e1dc7e61548a780936facce092834631f76e7bffd36fcbc0024e00b41f81` | 40859 |
| prodvizhenie-internet-magazina-czvetov.html | `46c829b39a531c99da194db4677d8989bc49fe3cfba584cfc2944b5d09457d23` | 40797 |
| services/seo.html | `4498f61b3854b90436fb4ddf56126492ac45b144ad716226ae934e081f4a8fb2` | 42918 |
| sitemap-static.xml | `5fdbd0394ae882bef8bf60e123a06932853953d0b16b88047eab75d6b615e959` | 11852 |
