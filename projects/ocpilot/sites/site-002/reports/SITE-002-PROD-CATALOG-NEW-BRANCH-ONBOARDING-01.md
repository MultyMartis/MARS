# REPORT — SITE-002 New Catalog Branch Onboarding

**Operation:** `SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-01`  
**OCPilot run:** 4.210  
**Date:** 2026-07-07  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Baseline before:** `SITE-002-STABLE-PROD-SEO-META-EDGE-01`  
**Audit baseline:** `SITE-002-SITEMAP-DELTA-AUDIT-01`  
**Checkpoint after:** `SITE-002-STABLE-PROD-CATALOG-NEW-BRANCH-01`

---

## 1. Scope

Controlled onboarding of new 1C-driven catalog branches surfaced after daily import and Run **4.209** sitemap delta audit. Goals:

1. Capture successful daily 1C import evidence.
2. Inventory new category/hub targets (not PDP).
3. Configure missing/weak category meta via exact OpenCart admin category SEO fields.
4. Preserve all new categories — **no delete/hide/noindex/redirect**.
5. Document ongoing 1C catalog growth onboarding policy.

**Forbidden:** category deletion/disable, noindex, sitemap removal, file upload, DB write, product generator change, llms/robots/sitemap/header/footer changes, cron/import trigger.

---

## 2. Operator clarification: onboard, do not delete

New categories from 1C import are **normal catalog growth** when HTTP 200, indexable, canonical sane, no test markers, no forbidden `БЗПМ`, and they have product fill or valid hub role.

This operation **onboards** them (category SEO meta, documentation, monitoring rule) — it does **not** treat sitemap growth as garbage or remove URLs.

---

## 3. Critical brand policy

| Rule | Value |
|------|-------|
| Correct public brand | **ЗПМ** |
| Forbidden in public content | **БЗПМ** |
| Domain | `bzpm.ru` (unchanged) |

All new meta copy uses **ЗПМ** only. No public **БЗПМ** introduced.

---

## 4. 1C import evidence

| Field | Value |
|-------|--------|
| Run ID | `mars-20260707-080008-[operator-provided]` |
| Operation | MARS parallel 1C import wrapper |
| Mode | run |
| Environment | PRODUCTION |
| Started | 2026-07-07T08:00:08+03:00 |
| Wrapper path | `/home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_import_wrapper.php` |
| Step 1 (catalog/products) | **PASS** — `import0_1.xml` |
| Step 2 (offers/prices/stocks) | **PASS** — `offers0_1.xml` |
| Final status | **SUCCESS** |
| Legacy policy | Sergey legacy import preserved; wrapper is parallel |
| Raw log file in workspace | **not found** — summary from operator charter + prior import pattern |

**Conclusion:** Daily 1C import is active and successful; new categories/products may appear normally; new catalog branches require onboarding, not deletion by default.

Storage: `import-evidence/1c-import-2026-07-07-summary.{md,json}`

---

## 5. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` — **PASS** |
| Volume | `X:` — label **AI WS** — **PASS** |
| Branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD (start) | `b10f91199d257df34e6982aa20f983583f1fff6c` |
| Staged files before task | **empty** — **PASS** |
| Foreign WIP | FP-0002 / `.recovery-temp` — **not staged, not touched** |

---

## 6. New branch target inventory

Built from Run **4.209** added URL list, current sitemap, and operator mentions (`konditerskiy-inventar`, `Лари`).

| Metric | Value |
|--------|-------|
| Total inventory rows | **64** |
| Category/hub crawl targets | **7** |
| PDP rows (out of scope) | **57** |
| New branch (1C) — primary | `konditerskiy-inventar` → `formy-konditerskie` |
| Lari branch | existing category + new PDPs; parent/subcategories reviewed |

**Included for onboarding (meta gap):**

| URL | Issue |
|-----|-------|
| `/konditerskiy-inventar` | missing description (Run 4.209 YELLOW) |
| `/formy-konditerskie` | missing description (Run 4.209 YELLOW) |
| `/lari` | weak description |
| `/lari/skladskie-lari` | weak description |
| `/lari/proizvodstvennye-lari` | weak description — **deferred** (authority) |

Storage: `inventory/new-branch-targets.{csv,json,md}`

---

## 7. Fresh live before

Crawled **7** category/hub URLs before mutation.

| URL | HTTP | Classification |
|-----|------|----------------|
| konditerskiy-inventar | 200 | CATEGORY_PLP_MISSING_DESCRIPTION |
| formy-konditerskie | 200 | CATEGORY_PLP_MISSING_DESCRIPTION |
| lari | 200 | CATEGORY_PLP_WEAK_DESCRIPTION |
| lari/skladskie-lari | 200 | CATEGORY_PLP_WEAK_DESCRIPTION |
| lari/proizvodstvennye-lari | 200 | CATEGORY_PLP_WEAK_DESCRIPTION |
| lari/lar-dlya-belya-… (sample) | 200 | PRODUCT_PDP_OUT_OF_SCOPE |

All targets: `page--category`, indexable, canonical sane, **0** forbidden `БЗПМ`.

Storage: `crawl-before/new-branch-before.{csv,json,md}`

---

## 8. Category authority map

| URL | category_id | Authority | Planned |
|-----|-------------|-----------|---------|
| konditerskiy-inventar | **360** | ADMIN_CATEGORY | ADMIN_SEO_SAVE |
| formy-konditerskie | **361** | ADMIN_CATEGORY | ADMIN_SEO_SAVE |
| lari | **88** | ADMIN_CATEGORY | ADMIN_SEO_SAVE |
| lari/skladskie-lari | **141** | ADMIN_CATEGORY | ADMIN_SEO_SAVE |
| lari/proizvodstvennye-lari | — | SAFE_UNKNOWN | DEFERRED |

Storage: `manifests/category-authority-map.{csv,json,md}`

---

## 9. Category meta copy final

| category_id | Name | Length | ЗПМ | БЗПМ |
|-------------|------|--------|-----|------|
| 360 | Кондитерский инвентарь | 133 | yes | no |
| 361 | Формы кондитерские | 132 | yes | no |
| 88 | Лари | 138 | yes | no |
| 141 | Складские | 138 | yes | no |

Copy for 360/361 matches operator-suggested text. Lari-related copy uses conservative ЗПМ template.

Storage: `copy/category-meta-copy-final.{csv,json,md}`

---

## 10. Implementation plan

- **Field changed:** `category_description[1][meta_description]` only
- **Title changes:** 0
- **Admin saves planned:** 4
- **File fallback:** 0
- **Delete/hide/noindex:** 0

Storage: `manifests/implementation-plan.md`, `manifests/admin-actions.json`

---

## 11. Before evidence / rollback values

Rollback captured for all **4** planned admin saves in `admin-evidence/category-seo-before.{csv,json,md}`.

---

## 12. Dry-run

| Gate | Result |
|------|--------|
| Forbidden БЗПМ in copy | **0** — PASS |
| PDP in admin targets | **0** — PASS |
| Delete/hide/noindex | **0** — PASS |
| File/DB/robots/sitemap/llms/header | **0** — PASS |

Storage: `manifests/dry-run.{md,json}`

---

## 13. Admin changes executed

| category_id | URL | Status | Verified |
|-------------|-----|--------|----------|
| 360 | konditerskiy-inventar | SAVED | yes |
| 361 | formy-konditerskie | SAVED | yes |
| 88 | lari | SAVED | yes |
| 141 | lari/skladskie-lari | SAVED | yes |

Storage: `admin-evidence/category-seo-after.json`

---

## 14. Live verification after

All **4** changed URLs: HTTP 200, `page--category`, meta description 120–165 chars, contains **ЗПМ**, **0** **БЗПМ**, title unchanged, canonical sane, sitemap membership unchanged (1377 URLs).

Storage: `crawl-after/new-branch-after.{csv,json,md}`, `verification/before-after-summary.{csv,json,md}`

---

## 15. Ongoing 1C catalog growth rule

Documented in `manifests/ongoing-1c-catalog-growth-rule.{md,json}`:

- Daily 1C import may add categories/products.
- Sitemap growth is not automatically a problem.
- New categories → **onboard** (meta, docs), not delete/close by default.
- Test/НЕ БРАТЬ SKUs → separate audit track.
- Post-import monitoring: category PLP/hub meta; PDP generator for true PDP only.
- Inventory types: PRODUCT_PDP, CATEGORY_PLP, CATEGORY_HUB, LEGACY_HUB, TECHNICAL.

---

## 16. Brand regression check

| Check | Result |
|-------|--------|
| New meta copy contains ЗПМ | **4/4** |
| New meta copy contains БЗПМ | **0** |
| Live pages after change — БЗПМ | **0** |

---

## 17. llms.txt preservation

| Check | Result |
|-------|--------|
| HTTP | 200 |
| UTF-8 BOM | present |
| БЗПМ | absent |

**llms.txt changes:** 0

---

## 18. Robots / sitemap preservation

| Check | Result |
|-------|--------|
| robots.txt | 200, `Sitemap:` present |
| sitemap.xml | 200, valid XML, **1377** URLs |
| Sitemap changes | **0** |

---

## 19. Yandex / duplicate body preservation

| Check | Result |
|-------|--------|
| Home HTTP 200 | yes |
| body_count | 1 |
| Yandex.Metrika | present |
| Yandex.Webmaster | present |
| /stoly Load More marker | present |

**Header/footer changes:** 0

---

## 20. Product PDP / generator exclusion proof

- **57** added PDP URLs inventoried as out of scope.
- **0** product/PDP admin saves.
- **0** `product.php` / generator changes.

---

## 21. Rollback status

Rollback values captured. **No rollback required** — all saves verified.

---

## 22. Remote mutation summary

| Action | Count |
|--------|-------|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| Remote renames | 0 |
| Admin saves (meta_description only) | **4** |
| DB direct operations | 0 |
| Product PDP changes | 0 |
| Product generator changes | 0 |
| Category structure changes | 0 |
| Category status changes | 0 |
| Category URL/slug changes | 0 |
| llms.txt changes | 0 |
| Header/footer changes | 0 |
| Yandex.Metrika/Webmaster changes | 0 |
| Robots changes | 0 |
| Sitemap changes | 0 |
| Cron/import runs | 0 |
| Mail changes | 0 |
| Cache clears | 0 |
| bzpm.ru domain changed | no |
| public БЗПМ introduced | no |
| delete/hide/noindex actions | 0 |

---

## 23. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-01\`

Checkpoint storage: `...\production\baselines\SITE-002-STABLE-PROD-CATALOG-NEW-BRANCH-01\`

---

## 24. Authority updates

| Doc | Updated |
|-----|---------|
| `OPERATIONAL-INDEX.md` | Run 4.210 |
| `OCPILOT-STATE.md` | evidence cutoff, SITE-002 focus |
| `production-profile.md` | checkpoint, onboarding policy |
| `site-passport.md` | checkpoint, new branch status |
| `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | 1C growth model, category IDs |
| `tools/README.md` | new tool entry |

---

## 25. Git status

Selective commit of repository docs/report/tool/baseline only. Storage artefacts not committed.

---

## 26. SAFE UNKNOWN / deferred

| URL | Reason |
|-----|--------|
| `/lari/proizvodstvennye-lari` | `category_id` not resolved safely (SAFE_UNKNOWN); weak meta remains; no guess save |

**Note:** Raw operator import log `mars_1c_import_2026-07-07_080008.txt` not found in workspace — summary from charter; step durations SAFE UNKNOWN.

---

## 27. Final verdict

**SITE-002 NEW CATALOG BRANCH ONBOARDING PARTIAL — DEFERRED SAFE UNKNOWN REMAINS**

Primary new 1C branch (`konditerskiy-inventar` / `formy-konditerskie`) onboarded with category meta. Lari parent/subcategory meta improved. One lari subcategory deferred pending safe `category_id` resolution.

---

## 28. Next task recommendation

1. Resolve `category_id` for `/lari/proizvodstvennye-lari` via read-only admin breadcrumb search or category tree export; apply distinct meta copy if weak description persists.
2. Add post-import monitoring hook: after daily 1C SUCCESS, diff sitemap for new CATEGORY_PLP with missing meta (reuse Run 4.209 classifier).
3. Keep PDP generator and category onboarding as separate tracks.

---

**Tool:** [site-002-prod-catalog-new-branch-onboarding-01.py](../tools/site-002-prod-catalog-new-branch-onboarding-01.py)  
**Related:** [SITE-002-PROD-SITEMAP-DELTA-AUDIT-01.md](SITE-002-PROD-SITEMAP-DELTA-AUDIT-01.md) (Run 4.209) · [OPERATIONAL-INDEX.md](../../../OPERATIONAL-INDEX.md) — Run 4.210
