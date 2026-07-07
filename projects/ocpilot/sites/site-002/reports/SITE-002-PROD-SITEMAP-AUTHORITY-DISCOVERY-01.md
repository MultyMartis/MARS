# REPORT — SITE-002 Sitemap Authority Discovery

**OCPilot run:** 4.214  
**Operation ID:** SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01  
**Date:** 2026-07-07  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Parent checkpoint:** SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01  
**Audit baseline before:** SITE-002-POST-1C-CATALOG-MONITOR-02  
**Mode:** Read-only sitemap authority discovery — **no Production mutation**

---

## 1. Scope

Read-only authority discovery for `https://bzpm.ru/sitemap.xml`. Goals:

1. Determine whether sitemap is automatic or manually maintained.
2. Identify exact controller/module/route authority.
3. Map data sources (products, categories, information, SEO URL, status filters).
4. Confirm physical file vs route/rewrite.
5. Assess cache/regeneration behavior.
6. Explain 1C import relationship.
7. Draft operational policy for MARS.

**Forbidden:** FTP upload, admin save, DB write, cache clear, sitemap/robots/meta edits, header/footer changes, cron/import trigger.

---

## 2. Operator question

> «Sitemap у нас автоматически формируется или нами непосредственно?»

**Direct answer:** Sitemap **формируется автоматически** встроенным OpenCart feed **Google Sitemap**. MARS **не** поддерживает `sitemap.xml` вручную в нормальной эксплуатации. Изменения URL отражают состояние каталога в БД (в т.ч. после ежедневного 1C import).

---

## 3. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` — **PASS** |
| Volume X label | `AI WS` — **PASS** |
| Branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD | `a8d825b0cbd6edd08707c0b20eab148544a6a111` |
| Staged files before task | **empty** — **PASS** |
| Foreign WIP | FP-0002 / forge-wordpress / `.recovery-temp` — **not staged, not touched** |

---

## 4. Public HTTP observation

### Sitemap

| Field | Value |
|-------|-------|
| URL | https://bzpm.ru/sitemap.xml |
| HTTP status | **200** |
| Final URL | https://bzpm.ru/sitemap.xml |
| Content-Type | `application/xml` |
| Valid XML | **yes** |
| URL count | **1377** |
| SHA-256 | `9c81305483d7fb79b829e562598e5a3a0eb74a29350fae142fa78f97c3eca6c1` |
| Byte length | 792539 |
| Products in sample | yes |
| Categories in sample | yes |
| Information pages | yes |
| Image sitemap entries | yes |

### Cache-bust probe

| Field | Value |
|-------|-------|
| URL | https://bzpm.ru/sitemap.xml?mars_readonly_probe=1 |
| HTTP status | **200** |
| Content equal to plain sitemap | **yes** (identical SHA-256) |
| Query ignored for routing | **yes** |

### Robots.txt

| Field | Value |
|-------|-------|
| HTTP status | **200** |
| Content-Type | `text/plain` |
| `Sitemap:` directive | `Sitemap: https://bzpm.ru/sitemap.xml` |

Storage: `deployments/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01/http/`

---

## 5. Physical file vs route check

| Question | Answer |
|----------|--------|
| Physical `/public_html/sitemap.xml` exists? | **NO** |
| Likely static/manual file? | **NO** |
| Likely route/feed? | **YES** |
| `.htaccess` rewrite involved? | **YES** |

**Exact rewrite rule (FTP read-only):**

```apache
RewriteRule ^sitemap.xml$ index.php?route=extension/feed/google_sitemap [L]
```

General SEO URL rewrite also present (`_route_` → `index.php`). No OC modification overlay for feed controller.

Storage: `deployments/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01/evidence/physical-vs-route-check.json`

---

## 6. Source/controller authority

| Path | Exists | Role |
|------|--------|------|
| `/public_html/catalog/controller/extension/feed/google_sitemap.php` | **yes** | **Catalog feed controller — sitemap XML generator** |
| `/public_html/admin/controller/extension/feed/google_sitemap.php` | yes | Admin settings (`feed_google_sitemap_status`) |
| `/public_html/catalog/controller/feed/google_sitemap.php` | no | Legacy route — not used |
| `/public_html/storage/modification/.../google_sitemap.php` | no | No modification overlay |

**Serving route:** `extension/feed/google_sitemap`  
**Public URL:** `https://bzpm.ru/sitemap.xml` (via `.htaccess`)  
**Feed URL:** `https://bzpm.ru/index.php?route=extension/feed/google_sitemap`

Catalog controller behavior (FTP-verified source):

- Checks `feed_google_sitemap_status` — if disabled, returns empty body.
- Builds XML in memory via `model_catalog_product->getProducts()`, recursive `getCategories()`, `getManufacturers()`, `getInformations()`.
- Emits `Content-Type: application/xml`.
- Does **not** write a physical file; does **not** use `$this->cache` in feed controller.

Storage: `deployments/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01/source-map/`

---

## 7. Data source map

### Products

| Field | Value |
|-------|-------|
| Source | `catalog/product::getProducts()` |
| Status filter | **yes** — `p.status = '1'`, `date_available <= NOW()`, `product_to_store` |
| URL pattern | `url->link('product/product', product_id=*)` → SEO alias |
| Images | yes (`image:image` when product has image) |
| lastmod | `product.date_modified` |
| changefreq / priority | weekly / 1.0 |
| 1C impact | **yes** — new/enabled products appear; disabled/removed drop |

### Categories

| Field | Value |
|-------|-------|
| Source | `catalog/category::getCategories()` recursive from parent 0 |
| Status filter | **yes** — `c.status = '1'` |
| URL pattern | `url->link('product/category', path=category_id)` → SEO alias |
| 1C impact | **yes** — new branches appear automatically |

### Information pages

| Field | Value |
|-------|-------|
| Source | `catalog/information::getInformations()` |
| Status filter | **yes** — `i.status = '1'` |
| Route | `information/information` via SEO rewrite |

### Manufacturers

| Field | Value |
|-------|-------|
| Source | `catalog/manufacturer::getManufacturers()` |
| In controller | **yes** |
| In live URL sample scan | no manufacturer URLs detected (may be empty set or unused public routes) |

### Blog / custom pages

| Field | Value |
|-------|-------|
| Included | **no** |
| Evidence | No blog logic in `google_sitemap.php`; only standard OpenCart feed directory entries (`google_sitemap`, `google_base`) |

### SEO URL

| Field | Value |
|-------|-------|
| Generation | `url->link()` + `catalog/controller/startup/seo_url.php` rewrite |
| SEO aliases | automatic from `oc_seo_url` when configured |

### Noindex / canonical

| Field | Value |
|-------|-------|
| Checked in feed | **no** |
| Implication | Sitemap inclusion is **catalog-state driven**; page-level robots/canonical must be audited separately |

Storage: `deployments/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01/module-map/`

---

## 8. Admin module state

Read-only inference (no admin login this run):

| Field | Value |
|-------|-------|
| `feed_google_sitemap_status` | **enabled** (inferred — live XML 1377 URLs) |
| Route | `extension/feed/google_sitemap` |
| Prior Run 4.191 admin evidence | `feed_google_sitemap_status=1` |
| Admin save this run | **0** |

Storage: `deployments/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01/admin-readonly/`

---

## 9. 1C import relationship

| Rule | Detail |
|------|--------|
| Daily 1C import | MARS wrapper via Beget cron 08:00 Moscow — **OPERATIONAL** (Run 4.194+) |
| Sitemap authority | Feed reads **current catalog DB** on each HTTP request |
| Manual sitemap edit by MARS | **not performed** |
| Manual regeneration required | **no** |
| Observed growth | 1320 (Run 4.206) → 1377 (Run 4.209+) — explained by catalog growth, not XML hand-edits |
| Category meta onboarding | Separate from sitemap inclusion; new enabled categories appear without manual sitemap work |

When 1C adds/enables products/categories with valid SEO routes, they **can appear automatically** on next sitemap fetch. When products are disabled or return 404, they **can disappear** (Run 4.209 removed test/operator URLs).

Storage: `deployments/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01/manifests/1c-sitemap-relationship.json`

---

## 10. Cache / regeneration behavior

| Aspect | Finding |
|--------|---------|
| Physical static file | **no** |
| Feed writes disk | **no** |
| OpenCart cache in feed controller | **no** |
| Generation mode | **live per HTTP request** |
| CDN/server cache | **SAFE UNKNOWN** — probe returned identical content; no cache headers analyzed in depth |
| Manual regeneration | **not required** |

Storage: `deployments/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01/manifests/sitemap-cache-behavior.json`

---

## 11. Sitemap authority policy

| Policy | Value |
|--------|-------|
| Authority | OpenCart/ocStore **Google Sitemap** feed (`extension/feed/google_sitemap`) |
| MARS manual XML edit | **prohibited** in normal operations |
| MARS monitor / delta audit | **allowed** |
| 1C-driven growth | **normal** — do not delete new URLs by default |
| New CATEGORY_PLP/HUB | onboard meta via **admin category SEO** |
| Problem URLs | fix at **source** (status, SEO URL, catalog data); not hand-edit XML |
| Physical upload | emergency + separate approval only |
| Post-1C monitor | use this authority model |

Storage: `deployments/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01/manifests/sitemap-authority-policy.md`

---

## 12. Direct answer

| Question | Answer |
|----------|--------|
| Automatically generated? | **YES** |
| Manually maintained by MARS? | **NO** |
| Physical file present? | **NO** |
| Generating controller | `/public_html/catalog/controller/extension/feed/google_sitemap.php` |
| Route | `extension/feed/google_sitemap` |
| Data sources | products, categories, manufacturers, information |
| 1C relationship | automatic reflection of catalog DB after import |
| Cache behavior | live per request (no static file, no feed-level cache) |
| Operational rule | monitor and audit; never manual XML edit in normal ops |

---

## 13. Remote mutation summary

| Action | Count |
|--------|------:|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| Remote renames | 0 |
| Admin saves | 0 |
| DB direct operations | 0 |
| Product DB changes | 0 |
| Product generator changes | 0 |
| Category meta changes | 0 |
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
| Physical sitemap edit | 0 |
| Manual sitemap generation | 0 |

---

## 14. Storage artefacts

Root: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01\`

| Folder | Contents |
|--------|----------|
| `http/` | sitemap + robots fetch, probe summary |
| `ftp-readonly/` | `.htaccess`, feed controller, models |
| `source-map/` | source file analysis |
| `module-map/` | data source map |
| `admin-readonly/` | feed state inference |
| `evidence/` | physical vs route |
| `manifests/` | operation.json, 1C relationship, cache, policy |
| `verification/` | authority verification summary |
| `logs/` | run log |

Tool: [site-002-prod-sitemap-authority-discovery-01.py](../tools/site-002-prod-sitemap-authority-discovery-01.py)

---

## 15. Authority updates

| Document | Update |
|----------|--------|
| `production-profile.md` | sitemap authority AUTO-GENERATED feed confirmed |
| `site-passport.md` | authority discovery Run 4.214 |
| `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | sitemap authority section expanded |
| `OPERATIONAL-INDEX.md` | Run 4.214 entry |
| `OCPILOT-STATE.md` | current focus → sitemap authority discovery |
| Audit baseline | `SITE-002-SITEMAP-AUTHORITY-DISCOVERY-01` issued |

---

## 16. Git status

Selective commit of report, baseline, tool, and scoped doc updates only. Storage artefacts remain outside git.

---

## 17. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| CDN/server-side HTTP cache TTL | **SAFE UNKNOWN** — identical probe hash; no edge cache headers fully characterized |
| Manufacturer URLs in sitemap | Controller includes them; live set may be empty/unused — **low operational impact** |
| Admin live re-read of `feed_google_sitemap_status` | Inferred from HTTP + Run 4.191; not re-logged this run |

No blockers to authority conclusion.

---

## 18. Final verdict

**SITE-002 SITEMAP AUTHORITY DISCOVERY COMPLETE — AUTO-GENERATED FEED CONFIRMED**

---

## 19. Next task recommendation

Continue **post-1C catalog onboarding monitor** after each daily import using established monitor tooling. Use this authority model:

- expect sitemap delta when catalog grows;
- onboard new CATEGORY_PLP meta via admin SEO;
- never hand-edit `sitemap.xml`;
- escalate problematic URLs to catalog/SEO source fixes.

Optional future: read-only manufacturer URL inventory if brand/manufacturer pages become SEO-relevant.
