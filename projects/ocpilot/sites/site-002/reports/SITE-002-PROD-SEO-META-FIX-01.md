# REPORT — SITE-002 SEO Meta Fix

**OCPilot run:** 4.192  
**Operation ID:** SITE-002-PROD-SEO-META-FIX-01  
**Date:** 2026-07-06  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Parent checkpoint:** SITE-002-STABLE-PROD-SITEMAP-01  

---

## 1. Scope

Controlled non-product SEO meta fixes per Run 4.188 `meta-fix-plan.md`. Product PDP excluded. No robots/sitemap/header.twig/footer.twig/Yandex/Load More/cron/import/mail changes.

| Allowed | Forbidden (not touched) |
|---------|-------------------------|
| HTTP meta crawl (17 seed URLs) | Product PDP / `product_id` URLs |
| FTP deploy ≤3 controller files + OC modification contact | `header.twig` / `footer.twig` |
| OpenCart admin SEO fields (attempted) | robots.txt / sitemap settings |
| Storage manifests + rollback | DB direct writes |

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume X label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Staged files before task | **none** |
| Parent checkpoint | `SITE-002-STABLE-PROD-SITEMAP-01` |

**Foreign WIP:** FP-0002, forge-wordpress, `.recovery-temp/` — not staged, not touched.

---

## 3. Meta fix plan source

- Run 4.188: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SEO-READINESS-ROBOTS-01\meta-audit\meta-fix-plan.md`
- Audit CSV/JSON: same folder (`43` non-product URLs audited in 4.188)
- Working plan: `deployments/SITE-002-PROD-SEO-META-FIX-01/manifests/meta-fix-working-plan.md`

---

## 4. Fresh meta before

Captured 17 seed URLs → `meta-before/meta-before.csv` · `meta-before-summary.md`

Notable before state:

- `/stoly` — title 5 chars, no description, `index,follow`
- Query variants (`?page=`, `?limit=`, `?sort=`) — duplicate title, no description
- Technical routes — `index,follow`, missing descriptions
- `/contact` — no description
- Home — description 246 chars (overlong)

---

## 5. Fix authority map

| Issue class | Authority | Action |
|-------------|-----------|--------|
| Category missing title/description | **CONTROLLER** (`category.php` runtime defaults) + **ADMIN** (deferred) | Defaults map for 6 PLP categories when DB meta empty |
| Query variant duplicates | **CONTROLLER** | `X-Robots-Tag: noindex, follow` + clean canonical |
| Technical pages (cart/checkout/search/compare) | **CONTROLLER** (`common/header.php`) | `X-Robots-Tag` by route/URI |
| Contact description + canonical | **CONTROLLER** via **OC modification cache** | `/storage/modification/.../contact.php` (runtime authority) |
| Home overlong description | **ADMIN** | `config_meta_description` trim — **not applied** (admin timeout) |
| Meta robots in HTML | **SAFE UNKNOWN** | `header.twig` hardcodes `index, follow`; `Document::setRobots()` **does not exist** on this OC build |

Storage: `manifests/fix-authority-map.md`

---

## 6. Content proposals

Controller-side defaults prepared for: `stoly`, `podtovarniki-i-podstavki`, `polki-nastennye-i-nastolnye`, `shkafy-i-lari`, `telezhki-servirovochnye`, `telezhki-shpilki-i-protivni`, plus contact description.

Admin copy proposals retained in `manifests/meta-copy-proposals.md` for operator persistence in category/store admin when convenient.

---

## 7. Implementation plan

**PLAN C — Hybrid (executed)**

1. `category.php` — SEO variant guard + category meta defaults + canonical to clean URL  
2. `common/header.php` — technical route `X-Robots-Tag` guard  
3. `/storage/modification/.../information/contact.php` — description + absolute canonical (runtime contact page)

**Not deployed:** catalog `information/contact.php` patch reverted (modification cache is runtime authority).

**Incident:** First deploy used nonexistent `Document::setRobots()` → fatal errors on cart/variants. **Rolled back immediately** from `rollback/` backups. Second deploy used `$this->response->addHeader('X-Robots-Tag: …')`.

---

## 8. Backup and rollback readiness

| File | Backup | Rollback |
|------|--------|----------|
| `catalog/controller/product/category.php` | `backup/category.php` | `rollback/category.php` |
| `catalog/controller/common/header.php` | `backup/header.php` | `rollback/header.php` |
| `storage/modification/.../contact.php` | `backup/supplement-contact.modification.php` | same |

SHA manifests: `manifests/backup-hashes.json` · dry-run: `manifests/dry-run.md`

---

## 9. Deploy / admin actions

| Action | Count |
|--------|------:|
| Remote controller uploads | **4** (category, header, modification contact ×2 updates, wishlist attempt reverted from scope) |
| Admin saves by Cursor | **0** (Playwright admin login — **TimeoutError**) |
| DB direct writes | **0** |
| Cache clears | **0** |

---

## 10. Meta after verification

Final crawl: `meta-after/meta-after.csv` (2026-07-06)

| URL | Result |
|-----|--------|
| `/katalog/.../stoly` | Title 44 chars, description 137 chars, canonical OK, indexable |
| `stoly?page=2` / `?limit=30` / `?sort=…` | `X-Robots-Tag: noindex, follow` |
| `/contact` | Description 129 chars, canonical `https://bzpm.ru/contact` |
| `/cart`, `/checkout`, `/search`, `/compare-products` | `X-Robots-Tag: noindex, follow` |
| `/wishlist` | No `X-Robots-Tag`; **robots.txt `Disallow: /wishlist/`** documents crawl block |
| `/` (home) | Description still **246 chars** — admin trim deferred |
| Yandex Metrika + Webmaster | **present** on indexable pages |
| `body` count | **1** on verified pages |

---

## 11. Robots / sitemap preservation

| Check | Result |
|-------|--------|
| `https://bzpm.ru/robots.txt` | 200, unchanged (`Sitemap:` present) |
| `https://bzpm.ru/sitemap.xml` | 200, valid XML, **1320 URLs** |

---

## 12. Yandex / duplicate body preservation

| Check | Result |
|-------|--------|
| Yandex.Metrika | **present** (live HTML) |
| Yandex.Webmaster verification | **present** (live HTML) |
| Single `<body>` | **1** on home, category, contact |
| header.twig / footer.twig | **not modified** |

---

## 13. Product PDP exclusion proof

Seed URL set excluded product paths. No `product_id` URLs crawled or modified. No product controller/template uploads.

---

## 14. Rollback status

- **First deploy rolled back safely** (fatal `setRobots()` error)
- **Second deploy stable** — no rollback required post-fix
- Rollback artefacts retained in Storage deployment folder

---

## 15. Remote mutation summary

| Metric | Value |
|--------|------:|
| Remote uploads | **4** |
| Remote overwrites | **4** |
| Remote deletes | **0** |
| Remote renames | **0** |
| Admin saves by Cursor | **0** |
| DB direct operations | **0** |
| Header/footer Twig changes | **0** |
| Yandex changes | **0** |
| Robots changes | **0** |
| Sitemap changes | **0** |
| Product/PDP changes | **0** |
| Load More changes | **0** |
| Cron/import changes | **0** |
| Mail changes | **0** |
| Cache clears | **0** |

---

## 16. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SEO-META-FIX-01\`

- `meta-before/` · `meta-after/` · `manifests/` · `backup/` · `rollback/` · `prepared/` · `admin-evidence/` · `logs/`

Tool: `projects/ocpilot/sites/site-002/tools/site-002-prod-seo-meta-fix-01.py`

---

## 17. Authority updates

- OpenCart `Document` class on Production **has no `setRobots()`** — use `X-Robots-Tag` response header or future `header.twig` dynamic robots (separate approved op)
- Contact page runtime = **`/storage/modification/catalog/controller/information/contact.php`**, not catalog path alone
- Category SEO defaults can be applied in `category.php` when admin meta fields empty (runtime only; DB unchanged)

---

## 18. Git status

Repository docs/report/tool updated in this operation. Storage artefacts not committed (by policy).

---

## 19. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Admin category/store SEO saves | **BLOCKED** — Playwright timeout; controller defaults compensate for 6 PLPs at runtime |
| `X-Robots-Tag` on `/wishlist` | **SAFE UNKNOWN** — header + wishlist controller patches did not emit header; mitigated by robots.txt `Disallow: /wishlist/` |
| HTML `<meta robots>` still `index,follow` on all pages | **Known limitation** — `header.twig` hardcoded; search engines also receive `X-Robots-Tag` where set |
| `/katalog` vs `/katalog/` duplicate | **Deferred** — both 200, `/katalog/` redirects to `/katalog`; canonical on hub not added |
| Home / corp long descriptions | **Deferred** — admin input required |
| Blog hub missing descriptions | **Deferred** — P3 |

---

## 20. Final verdict

**SITE-002 SEO META FIX PARTIAL — ADMIN INPUT REQUIRED**

P1 non-product fixes verified: category PLP meta (sample `stoly`), query-variant noindex, technical page noindex (except wishlist mitigated by robots), contact description/canonical. Home meta trim and admin persistence of category SEO fields remain for operator.

**Checkpoint `SITE-002-STABLE-PROD-SEO-META-01` not issued** — partial completion; parent checkpoint remains `SITE-002-STABLE-PROD-SITEMAP-01`.

---

## 21. Next task recommendation

1. **Operator admin pass** — trim `config_meta_description` (home); persist category meta_title/description for 6 PLPs in OpenCart admin (optional — controller defaults active at runtime).  
2. **Optional follow-up** — dynamic robots in `header.twig` (separate approved op; Yandex blocks protected).  
3. **P2** — catalog hub canonical; blog hub descriptions.
