# REPORT — SITE-002 Category Lari Reparent Implementation

**Operation:** `SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01`  
**OCPilot run:** 4.235  
**Date:** 2026-07-09  
**Environment:** PRODUCTION controlled mutation — https://bzpm.ru/  
**Baseline before:** `SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01`  
**Checkpoint after:** `SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01`  
**Related discovery:** Run 4.234 — [SITE-002-PROD-CATEGORY-LARI-REPARENT-DISCOVERY-01.md](SITE-002-PROD-CATEGORY-LARI-REPARENT-DISCOVERY-01.md)

---

## 1. Scope

Controlled production reparent of category **Лари** (ID **88**) from direct child of **Нейтральное оборудование** (79) to child of **Шкафы и лари** (358), with URL canonicalization, scoped 301 redirects, entrypoint href fixes, and regression verification.

| Item | Value |
|------|-------|
| Old URL | `/katalog/nejtralnoe-oborudovanie/lari` |
| New URL | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari` |
| SEO keyword `lari` | **unchanged** |
| Product assignments | **unchanged** |
| 1C import run | **not executed** |

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace `X:\AI MARS` | PASS |
| Volume `X:` label `AI WS` | PASS |
| Branch `mars/canonical-post-recovery` | PASS |
| Staged files before task | empty — PASS |
| Foreign WIP | not staged / not touched |

---

## 3. 1C source gate

**Source:** `/public_html/1c_incoming/webdata/import0_1.xml` (FTP read-only)

**Verdict:** **PASS — PROCEED**

1C hierarchy confirms: `Нейтральное оборудование → Шкафы и лари → Лари`

Artefacts: `AI MARS STORAGE/.../SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01/one-c-source-check/`

---

## 4. Before public snapshot

Captured HTTP before mutation (artefacts `http-before/`). Key pre-mutation findings:

- Old `/lari` — 200, canonical flat path
- Nested `/shkafy-i-lari/lari` — resolved to flat `/lari` via `seo_pro` stale `category.seopath` cache
- Sitemap contained old flat lari tree (~1408 URLs per discovery)
- Homepage marketing tile **Лари** href pointed to flat path

---

## 5. DB backup and rollback plan

Backups captured under Storage `db-backup/` (not committed). Rollback SQL in repo:

- [site-002-category-lari-reparent-rollback.sql](../tools/site-002-category-lari-reparent-rollback.sql)

---

## 6. Mutation strategy selected

**Hybrid:**

1. Controlled DB migration (`parent_id` + `category_path` rebuild)
2. Scoped `.htaccess` 301 for old flat lari tree
3. Source patches for canonical URL generation (`seo_pro`, `seo_url`, `category_visibility`, `category.php`)
4. Scoped OpenCart cache purge (`category.seopath`, `seo_pro`, `cat-list-header`)

**Not used:** OpenCart admin bulk save, 1C import, monitor run.

---

## 7. Dry-run gates

All 18 gates passed before DB write (manifest `manifests/dry-run-gates.json` in Storage).

---

## 8. Applied DB/source changes

### DB (via SSH mysql)

- `oc_category`: ID **88** `parent_id` **79 → 358**
- `oc_category_path` rebuilt for **88**, **140**, **141**
- SEO keyword `lari` unchanged
- Product-to-category counts unchanged

### FTP uploads (5 files)

| File | Change |
|------|--------|
| `.htaccess` | 301 old flat lari → nested tree |
| `catalog/controller/startup/seo_url.php` | `category_path` normalize; rewrite uses canonical path |
| `catalog/controller/startup/seo_pro.php` | `getPathByCategory()` reads `oc_category_path` (not stale parent join cache) |
| `system/library/zpm/category_visibility.php` | `buildCategoryPathParam()`; homepage links `product/katalog` |
| `catalog/controller/product/category.php` | Canonical + hub hrefs via `buildCategoryPathParam()` + `product/katalog` |

### Cache (scoped)

Removed: `cache.category.seopath.*`, `cache.seo_pro.*`, `cache.cat-list-header.*`, `cache.product.seopath.*`

**Root cause note:** `seo_pro.php` `validate()` compared REQUEST_URI to `url->link()` canonical built from cached `category.seopath` with **old** flat path `79_88`, causing nested URLs to 301 → flat until cache purge.

---

## 9. DB after verification

| Check | Result |
|-------|--------|
| `88.parent_id` | **358** |
| path 88 | 79 → 358 → 88 |
| path 140 | 79 → 358 → 88 → 140 |
| path 141 | 79 → 358 → 88 → 141 |
| SEO `lari` keyword | unchanged |
| Product counts | unchanged |

---

## 10. Redirect verification

| URL | Status | Location |
|-----|--------|----------|
| `/.../lari` (old) | **301** | `/.../shkafy-i-lari/lari` |
| `/.../lari/skladskie-lari` (old) | **301** | `/.../shkafy-i-lari/lari/skladskie-lari` |
| `/.../lari/proizvodstvennye-lari` (old) | **301** | `/.../shkafy-i-lari/lari/proizvodstvennye-lari` |
| `/.../shkafy-i-lari/lari` (new) | **200** | — |

---

## 11. HTTP/canonical/breadcrumb verification

**Лари page** (`/shkafy-i-lari/lari`):

- Status: **200**
- Canonical: `https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari`
- H1: **Лари**
- Breadcrumbs: Главная → Каталог → Нейтральное оборудование → **Шкафы и лари** → Лари

Child categories: nested URLs **200** with correct hierarchy.

---

## 12. Sitemap verification

Dynamic sitemap (`/sitemap.xml`) after cache purge:

- **Contains** nested `/shkafy-i-lari/lari` category URLs (category + children + products)
- **No** old flat `/nejtralnoe-oborudovanie/lari` category URLs (`old_flat_count=0`)

---

## 13. Homepage/catalog/hub entrypoint verification

| Entrypoint | Лари behavior |
|------------|---------------|
| Homepage marketing tile (`zpm-cat-card`) | **Present**; href = nested `/shkafy-i-lari/lari` |
| Header megamenu (`zpm-catalog__tile`) | Шкафы и лари tile present; Лари not duplicated as top-level sibling in homepage cards |
| Neutral hub | Structural whitelist behavior unchanged; Лари marketing visibility per operator decision |
| Шкафы и лари hub | **200**; Лари accessible as child category |

---

## 14. Regression verification

| URL | Status | БЗПМ |
|-----|--------|------|
| `/` | 200 | 0 |
| `/katalog` | 200 | 0 |
| `/.../stoly` | 200 | 0 |
| `/sitemap.xml` | 200 | — |
| `/robots.txt` | 200 | — |
| `/llms.txt` | 200 | — |

No PHP 500 observed on probed paths.

---

## 15. Cache actions

Scoped purge only (see §8). No broad server cache clear.

---

## 16. Rollback status

**Not required.** Rollback bundle available in Storage `rollback/` + repo SQL rollback script.

---

## 17. Production mutation summary

| Metric | Count |
|--------|------:|
| Remote uploads | 5 |
| Remote overwrites | 5 |
| Remote deletes | 0 |
| FTP writes | 5 |
| Admin saves | 0 |
| DB SELECTs | multiple (read-only gates + verification) |
| DB direct writes | 1 parent update + category_path delete/insert (88/140/141) |
| Category parent changes | 1 (ID 88) |
| Category path changes | 3 categories (88, 140, 141) |
| SEO URL keyword changes | 0 |
| Redirect rules (.htaccess) | 2 |
| Product data changes | 0 |
| Product-to-category changes | 0 |
| Mail sends | 0 |
| Form submits | 0 |
| Cron/import runs | 0 |
| Monitor runs | 0 |
| Cache clears | 4 cache key families (scoped) |
| public БЗПМ introduced | **no** |

---

## 18. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01\`

Subfolders: `one-c-source-check/`, `http-before/`, `http-after/`, `db-backup/`, `db-after/`, `sql-applied/`, `ftp-source-before/`, `ftp-source-after/`, `verification/`, `rollback/`, `manifests/`, `logs/`

Checkpoint storage: `.../production/baselines/SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01/`

---

## 19. Authority updates

- [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) — Run 4.235
- [OCPILOT-STATE.md](../../OCPILOT-STATE.md)
- [production-profile.md](../production-profile.md)
- [site-passport.md](../site-passport.md)
- [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
- [tools/README.md](../tools/README.md)
- Baseline: [SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01.md](../baselines/SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01.md)

---

## 20. Git status

Docs/tools/report/checkpoint only staged (no Storage, no DB dumps).

---

## 21. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Post-1C import persistence of `parent_id=358` for category 88 | **PENDING** — next scheduled import should be observed; discovery indicates 1C does not update `parent_id` on existing categories, but operator verification after import is still required |
| `import0_1.xml` parent chain in future imports | assumed stable per gate; re-check if 1C structure changes |

---

## 22. Final verdict

**SITE-002 CATEGORY LARI REPARENT IMPLEMENTATION PARTIAL — POST-1C IMPORT VERIFICATION PENDING**

Production mutation verified stable: DB hierarchy, nested URLs 200, old URLs 301, canonical/breadcrumbs/sitemap/entrypoints correct. Checkpoint **`SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01`** issued. Full closure awaits post-1C import observation.

---

## 23. Next task recommendation

1. **SITE-002-PROD-POST-1C-LARI-REPARENT-VERIFICATION-01** — after next 1C cron import, read-only verify `parent_id`, `category_path`, sitemap, and HTTP canonical for category 88 subtree.
2. Optional: patch `katalog.php` megamenu href builder to use `buildCategoryPathParam()` (currently uses `path=_<id>` pattern; not blocking after cache rebuild).
