# REPORT — SITE-002 Brand ZPM Remediation

**Operation:** `SITE-002-PROD-BRAND-ZPM-REMEDIATION-01`  
**OCPilot run:** 4.205  
**Date:** 2026-07-07  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Baseline before:** `SITE-002-STABLE-PROD-LLMS-TXT-UTF8-01`  
**Baseline after:** `SITE-002-STABLE-PROD-BRAND-ZPM-01`

---

## 1. Scope

Controlled public brand remediation: replace Cyrillic public brand text **БЗПМ** with **ЗПМ** in llms.txt, controller meta literals, product meta generator output, and admin category SEO fields. Domain `bzpm.ru` and URLs unchanged. No header/footer, robots, sitemap, DB, import, or product data changes.

---

## 2. Critical brand policy

| Rule | Value |
|------|-------|
| Correct public Russian brand | **ЗПМ** |
| Forbidden in public content | **БЗПМ** |
| Domain (unchanged) | `bzpm.ru` — URL only, not a public Russian brand name |
| Internal shorthand | May remain in MARS operation IDs, folder names, historical reports only |

---

## 3. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` — label **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| Staged files before task | **none** |
| Foreign WIP | FP-0002 / `.recovery-temp` — **not staged** |

---

## 4. Public occurrence inventory before

Crawl: 47 URLs (19 core + 24 PDP + 4 extra PDP + 2 sanity).

| Metric | Value |
|--------|-------|
| URLs with public `БЗПМ` | **37** |
| Total `БЗПМ` count in bodies | **59** |
| llms.txt | 2 occurrences |
| Information pages | 6 controllers |
| katalog / blog | 3 controllers |
| Category PLP meta | 3 categories (331, 354, 358) |
| PDP generated meta | 24/24 sample |

**Storage:** `deployments/.../crawl-before/public-brand-occurrences-before.*`

---

## 5. Source authority map

| Authority | Remote path | `БЗПМ` count | Method |
|-----------|-------------|--------------|--------|
| LLMS_TXT | `/public_html/llms.txt` | 2 | FILE_PATCH + UTF-8 BOM |
| PRODUCT_META_GENERATOR | `/public_html/catalog/controller/product/product.php` | 2 | FILE_PATCH |
| PRODUCT_KATALOG_CONTROLLER | `/public_html/catalog/controller/product/katalog.php` | 1 | FILE_PATCH |
| BLOG_CONTROLLER | `/public_html/catalog/controller/blog/category.php` | 2 | FILE_PATCH |
| CUSTOM_CONTROLLER | `information/about.php` | 1 | FILE_PATCH |
| CUSTOM_CONTROLLER | `information/custom_equipment.php` | 1 | FILE_PATCH |
| CUSTOM_CONTROLLER | `information/dealers.php` | 1 | FILE_PATCH |
| CUSTOM_CONTROLLER | `information/delivery.php` | 1 | FILE_PATCH |
| CUSTOM_CONTROLLER | `information/guarantee.php` | 1 | FILE_PATCH |
| CUSTOM_CONTROLLER | `information/payment.php` | 1 | FILE_PATCH |
| ADMIN_CATEGORY_META | category_id=331, 354, 358 | 1 each | ADMIN_SEO_SAVE |

Categories 301, 322, 326 probed — no `БЗПМ` in SEO fields.

**Storage:** `manifests/source-authority-map.json`

---

## 6. Implementation plan

- 10 FTP file patches — literal `БЗПМ` → `ЗПМ` only
- 3 admin category SEO saves — meta_description only (title unchanged)
- 0 header/footer, robots, sitemap, DB, import changes

**Storage:** `manifests/implementation-plan.md`, `manifests/admin-actions.json`

---

## 7. Backup / rollback readiness

All 10 target files backed up to `backup/` and `rollback/` with SHA-256. Admin before values captured in `admin-evidence/category-brand-before.json`. Pre-upload SHA match verified for all files.

---

## 8. Dry-run

| Check | Result |
|-------|--------|
| Wrong brand before (files) | 14 literals |
| Wrong brand after (files) | 0 |
| `bzpm.ru` domain unchanged | **yes** (all files) |
| llms.txt UTF-8 BOM in prepared | **yes** |
| Header/footer in diff | **no** |

**Storage:** `manifests/dry-run.json`

---

## 9. File deploy / admin changes executed

### FTP uploads (10)

| Remote | SHA-256 (after) |
|--------|-----------------|
| `/public_html/llms.txt` | `2d200b546b46764fa3c422ad3dbd50c1b2a323609759431d9811b6122c8a54a7` |
| `.../product/product.php` | `6a476f6bd1decb82e7e7cd23ec528884d61445e49082045b72fcb60d1be04a86` |
| `.../product/katalog.php` | `2d12e18b524919055eca6c80d4476da3351f65941ed516b2d8681f34baa5e4b5` |
| `.../blog/category.php` | `c5121ffb098cb06336103aa24fab21c0692b2ff3d0d03d2dd14faf12dc252add` |
| 6× `information/*.php` | see `logs/ftp-uploads.json` |

### Admin saves (3)

| category_id | Name | Field changed |
|-------------|------|---------------|
| 331 | Полки настенные и настольные | meta_description |
| 354 | Тележки-шпильки и противни | meta_description |
| 358 | Шкафы и лари | meta_description |

**Storage:** `manifests/deploy-summary.json`

---

## 10. Public occurrence verification after

| Metric | Before | After |
|--------|--------|-------|
| URLs with public `БЗПМ` | 37 | **0** |
| Total body count | 59 | **0** |
| PDP sample (28) | all had `БЗПМ` in meta | **0** |
| HTTP errors | 0 | 0 |

**Storage:** `crawl-after/public-brand-occurrences-after.*`

---

## 11. llms.txt encoding preservation

| Check | Result |
|-------|--------|
| HTTP 200 | yes |
| UTF-8 BOM | **yes** (`ef bb bf`) |
| Readable Russian | yes |
| `БЗПМ` count | **0** |
| `ЗПМ` count | 2 |
| `bzpm.ru` URLs | 20 — unchanged |

---

## 12. Product meta generator brand verification

Sample PDP meta now uses **ЗПМ** in description and keywords (runtime generator in `product.php`). Generator logic unchanged except brand literal. 24/24 deep PDP sample CLEAN after deploy.

---

## 13. Robots / sitemap preservation

| Check | Result |
|-------|--------|
| robots.txt | HTTP 200 — unchanged |
| sitemap.xml | HTTP 200 — valid XML |
| URL count | **1320** |

---

## 14. Yandex / duplicate body preservation

| Check | Result |
|-------|--------|
| home body_count | **1** |
| Yandex.Metrika | present |
| Yandex.Webmaster | present |
| header.twig / footer.twig | **not modified** |

---

## 15. Domain URL preservation

`bzpm.ru` domain and all URL references unchanged in patched files and live crawl. Only Cyrillic **БЗПМ** replaced with **ЗПМ**.

---

## 16. Product data / DB exclusion proof

| Operation | Count |
|-----------|-------|
| DB direct writes | **0** |
| Product DB changes | **0** |
| Import script changes | **0** |
| Product template changes | **0** |

---

## 17. Rollback status

Rollback **not required**. Rollback artefacts ready in Storage `rollback/` for all 10 files and admin before values in `admin-evidence/category-brand-before.json`.

---

## 18. Remote mutation summary

| Operation | Count |
|-----------|-------|
| Remote uploads | **10** |
| Remote overwrites | **10** |
| Remote deletes | **0** |
| Remote renames | **0** |
| Admin saves | **3** exact SEO fields |
| DB direct operations | **0** |
| Import script changes | **0** |
| Product DB changes | **0** |
| Product template changes | **0** |
| Header/footer changes | **0** |
| Yandex.Metrika/Webmaster changes | **0** |
| Robots changes | **0** |
| Sitemap changes | **0** |
| Cron/import changes | **0** |
| Mail changes | **0** |
| Cache clears | **0** |
| llms.txt changed | **yes** |
| llms.txt UTF-8 BOM preserved | **yes** |
| bzpm.ru domain changed | **no** |

---

## 19. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-BRAND-ZPM-REMEDIATION-01\`

Subfolders: `source/`, `prepared/`, `backup/`, `rollback/`, `verification/`, `crawl-before/`, `crawl-after/`, `admin-evidence/`, `manifests/`, `logs/`

---

## 20. Authority updates

Updated: `production-profile.md`, `site-passport.md`, `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`, `OCPILOT-STATE.md`, `OPERATIONAL-INDEX.md`, `tools/README.md`

---

## 21. Git status

Selective commit planned for operation report, checkpoint, tool script, and scoped doc updates only. Storage artefacts excluded from Git.

---

## 22. SAFE UNKNOWN / blockers

None for targeted crawl scope. Full-site exhaustive crawl outside sample not performed — **final meta inventory** recommended as next task for any remaining edge pages.

---

## 23. Final verdict

**SITE-002 BRAND ZPM REMEDIATION COMPLETE — PUBLIC БЗПМ REMOVED**

---

## 24. Next task recommendation

**Final meta inventory** — full public meta audit across all indexable routes to confirm no residual wrong-brand text outside sampled URLs; optional home page visible copy review if operator reports legacy body text.
