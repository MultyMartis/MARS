# REPORT — SITE-002 SEO Readiness and Robots

**OCPilot run:** 4.188  
**Operation ID:** SITE-002-PROD-SEO-READINESS-ROBOTS-01  
**Date:** 2026-07-06  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Parent checkpoint:** SITE-002-STABLE-PROD-LOAD-MORE-01  
**New checkpoint:** SITE-002-STABLE-PROD-SEO-ROBOTS-01

---

## 1. Scope

Controlled SEO readiness audit for **non-product** pages plus **single-file** `robots.txt` deploy.

| Allowed | Forbidden (not touched) |
|---------|-------------------------|
| HTTP crawl of public non-product URLs | Product PDP meta edits |
| FTP read-only (header/footer Twig, robots.txt) | DB writes / admin saves |
| Upload exactly `/public_html/robots.txt` | header.twig / footer.twig edits |
| Meta audit artefacts + fix plan | Cron / import / mail / Load More |
| OCPilot docs + checkpoint | Mass meta fixes |

**Product pages excluded** from meta audit scope. Category/listing, information, home, blog URLs included.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume X label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Staged files | **none** |
| Parent checkpoint | `SITE-002-STABLE-PROD-LOAD-MORE-01` |

**Foreign WIP:** FP-0002, forge-wordpress, `.recovery-temp/` — not staged, not touched.

---

## 3. Operator Twig analytics protection

Fresh FTP read-only download:

| File | Result |
|------|--------|
| `/public_html/catalog/view/theme/default/template/common/header.twig` | Downloaded — **no Yandex strings detected** |
| `/public_html/catalog/view/theme/default/template/common/footer.twig` | Downloaded — **no Yandex strings detected** |

| Field | Value |
|-------|-------|
| Metrika findings | **0** |
| Webmaster verification findings | **0** |
| Live HTML (homepage) Metrika | **not detected** |
| Live HTML Webmaster verification | **not detected** |
| Status | **SAFE UNKNOWN** |

Operator WIP for Yandex.Metrika / Yandex.Webmaster may be **pending deploy** or stored outside the inspected Twig paths. **No Twig files were modified, uploaded, or reformatted.**

Protection rule recorded: **DO NOT OVERWRITE / DO NOT REFORMAT** header/footer when operator codes are present.

Storage: `deployments/SITE-002-PROD-SEO-READINESS-ROBOTS-01/analytics-codes/`

---

## 4. Non-product URL inventory

| Metric | Value |
|--------|-------|
| URLs inventoried | **43** |
| Seed URLs | 19 |
| Homepage-discovered | 24 |
| Product PDP excluded | yes |

Minimum seed set audited including home, catalog hub, category `stoly` (+ page/limit/sort variants), corporate pages, contact, technical routes.

Storage: `crawl/non-product-url-inventory.csv` · `crawl/non-product-url-inventory.json`

---

## 5. Meta audit summary

| Classification | Count |
|----------------|-------|
| PASS | 12 |
| WARN | 14 |
| FAIL | 17 |
| SAFE UNKNOWN | 0 |

**Audited URLs:** 43 (non-product scope)

### Notable PASS pages

- Home-adjacent legal: `/privacy-policy`, `/user-agreement`, `/cookie-files-policy`
- Catalog hub/category samples: `/katalog/nejtralnoe-oborudovanie`, subcategories (моечные ванны, стеллажи, зonty)
- Blog articles (sample news URLs)
- `/our-certification`

### Common WARN/FAIL patterns

| Pattern | Examples | Recommended next step |
|---------|----------|----------------------|
| Missing meta description | Category PLPs (`stoly`, subcategories), blog hub | `SITE-002-PROD-SEO-META-FIX-01` |
| Duplicate title on pagination/sort/limit | `stoly`, `stoly?page=2`, `?limit=30`, `?sort=…` | Unique titles or `noindex` for faceted URLs |
| Description too long (>170) | Home, about, delivery, guarantee, dealers | Trim in admin/SEO layer |
| Short title (<20) | Blog hub `/blog`, `/blog/news` | Expand titles |
| Duplicate `/katalog` vs `/katalog/` | Both 200, same title/description | Canonical consolidation |
| Contact URL variants | `/contact`, `/index.php?route=information/contact` duplicate title | Pick canonical contact URL |
| Technical pages indexed | Cart, compare, wishlist — `index, follow` without description | Add `noindex` in meta-fix wave |

**No meta edits performed in this operation.**

Storage: `meta-audit/non-product-meta-audit.csv` · `meta-audit/non-product-meta-summary.md` · `meta-audit/meta-fix-plan.md`

---

## 6. Sitemap discovery

| URL | HTTP | Suitable for robots `Sitemap:` |
|-----|------|--------------------------------|
| https://bzpm.ru/sitemap.xml | 200 (empty body, `text/html`) | **NO** |
| https://bzpm.ru/index.php?route=extension/feed/google_sitemap | 200 (empty body) | **NO** |
| https://bzpm.ru/index.php?route=feed/google_sitemap | 404 | **NO** |
| https://bzpm.ru/sitemap_index.xml | 404 | **NO** |

**Result:** No valid XML sitemap discovered. Prepared `robots.txt` **omits** `Sitemap:` directive. Enable Google Sitemap extension / fix routing in a **separate approved operation**.

Storage: `sitemap/sitemap-discovery.md`

---

## 7. Current robots analysis

| Field | Value |
|-------|-------|
| Pre-deploy HTTP | 200 `text/plain` |
| Pre-deploy SHA-256 | `72ab7d21cdb7f66bf69fcc2cd21a2571bad402e38b626377516d7fd4f22ba723` |
| Pre-deploy size | ~2464 bytes |
| Blocks entire site | **NO** |
| Had Yandex `Clean-param: tracking` | **YES** |
| Missing explicit `/storage/`, `/image/` Allow | partial vs target design |

Legacy robots used OpenCart-style rules without trailing slashes on `/admin`, `/catalog`; lacked `/storage/` block and explicit `/image/` Allow.

Backup saved: `source/robots.txt`, `backup/robots.txt`, `rollback/robots.txt`

---

## 8. Robots design

Conservative OpenCart-aware robots:

- Allow public `/katalog/` pretty URLs and information pages
- Disallow admin, system, storage, account, cart, checkout, search, compare, wishlist
- Disallow faceted query params: `sort`, `order`, `limit`, `page`, `filter_name`, `tracking` (both `?` and `&`)
- Explicit **Allow** for `/catalog/view/`, `/catalog/view/theme/`, `/catalog/view/javascript/`, `/image/`
- **User-agent: Yandex** block retained with `Clean-param: tracking` (from prior production robots)
- No `Crawl-delay`, no `Host`, no secrets, no sitemap (none valid)

Storage: `robots/robots-design.md` · `robots/prepared-robots-preview.txt`

---

## 9. Robots deploy

| Gate | Result |
|------|--------|
| G1 target path | PASS |
| G2 backup recorded | PASS |
| G3 no full-site block | PASS |
| G4 public catalog not blocked | PASS |
| G5 rendering assets allowed | PASS |
| G6 sitemap omitted (none valid) | PASS |
| G7 no Twig in upload plan | PASS |
| G8 no meta/DB/admin changes | PASS |
| G9 analytics protection recorded | PASS (SAFE UNKNOWN documented) |
| G10 remote unchanged since backup | PASS |

| Field | Value |
|-------|-------|
| Remote target | `/public_html/robots.txt` |
| Uploads | **1** |
| Overwrites | **1** (robots.txt only) |
| Deletes | **0** |

---

## 10. Robots verification

| Check | Result |
|-------|--------|
| https://bzpm.ru/robots.txt HTTP | **200** |
| Content-Type | plain text |
| SHA-256 match prepared | **PASS** — `9fe056f7a2d84112ce053d20083537ef245d8bf083d41c0273058ccec701a9d8` |
| Full HTML page returned | **NO** |
| Secrets / Yandex tokens in file | **NO** |
| Cache clear | **not performed** |

---

## 11. Post-deploy SEO spot check

| URL | HTTP | Site break | Metrika in HTML | Webmaster verify |
|-----|------|------------|-----------------|------------------|
| https://bzpm.ru/ | 200 | none | not detected | not detected |
| https://bzpm.ru/katalog/nejtralnoe-oborudovanie | 200 | none | not detected | not detected |
| https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly | 200 | none | not detected | not detected |
| https://bzpm.ru/robots.txt | 200 | n/a | n/a | n/a |

Twig overwrite: **0**. Operator analytics codes touched: **0**.

---

## 12. Meta fix plan

Produced for all WARN/FAIL pages — see Storage `meta-audit/meta-fix-plan.md`.

**Proposed next operation:** `SITE-002-PROD-SEO-META-FIX-01` (operator approval required; no mass edits in this run).

Priority items:

1. Add unique meta descriptions to category PLPs missing them
2. Resolve duplicate titles on pagination/sort/limit variants for `stoly` and similar categories
3. Trim long descriptions on home and corporate pages
4. Add `noindex` to cart/checkout/account/search/compare/wishlist
5. Consolidate `/katalog` vs `/katalog/` canonical
6. Fix contact URL canonical (`/contact` vs `/contact-us` vs index.php route)

---

## 13. Remote mutation summary

| Category | Count |
|----------|-------|
| Remote uploads | **1** |
| Remote overwrites | **1** (robots.txt only) |
| Remote deletes | **0** |
| Remote renames | **0** |
| Twig/header/footer changes | **0** |
| Yandex.Metrika/Webmaster code touched | **0** |
| Product page changes | **0** |
| Meta changes | **0** |
| Database operations | **0** |
| Admin saves | **0** |
| Cron/import changes | **0** |
| Mail changes | **0** |
| Cache clears | **0** |

---

## 14. Storage artefacts

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SEO-READINESS-ROBOTS-01\
```

Subfolders: `source\`, `prepared\`, `backup\`, `rollback\`, `verification\`, `crawl\`, `meta-audit\`, `robots\`, `sitemap\`, `analytics-codes\`, `manifests\`, `logs\`

Checkpoint storage:

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-SEO-ROBOTS-01\
```

---

## 15. Authority updates

| Document | Updated |
|----------|---------|
| `projects/ocpilot/OPERATIONAL-INDEX.md` | Run 4.188 |
| `projects/ocpilot/OCPILOT-STATE.md` | SEO readiness state |
| `projects/ocpilot/sites/site-002/production-profile.md` | robots + SEO audit |
| `projects/ocpilot/sites/site-002/site-passport.md` | checkpoint |
| `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | SEO section |
| `projects/ocpilot/sites/site-002/baselines/SITE-002-STABLE-PROD-SEO-ROBOTS-01.md` | new checkpoint |
| `projects/ocpilot/sites/site-002/tools/site-002-prod-seo-readiness-robots-01.py` | operation tool |
| `projects/ocpilot/sites/site-002/tools/README.md` | tool index |

---

## 16. Git status

Selective commit of scoped OCPilot paths only. Storage artefacts **not** committed. Foreign WIP excluded.

---

## 17. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Yandex.Metrika in live Twig/HTML | **SAFE UNKNOWN** — not found at audit time; operator WIP may be unpublished |
| Yandex.Webmaster verification in live Twig/HTML | **SAFE UNKNOWN** |
| Valid XML sitemap | **NOT FOUND** — enable/fix in separate operation |
| Sitemap extension route empty response | **SAFE UNKNOWN** — may need admin module enable |

**Blockers for this operation:** none — robots deploy verified PASS.

---

## 18. Final verdict

**SITE-002 SEO READINESS PARTIAL — ROBOTS DEPLOYED / META AUDIT NEEDS OPERATOR REVIEW**

Robots.txt deployed and verified. Non-product meta audit complete with fix plan ready. Operator review required for WARN/FAIL meta items and Yandex analytics WIP confirmation.

---

## 19. Next task recommendation

1. **SITE-002-PROD-SEO-META-FIX-01** — approved scoped meta fixes (non-product; category descriptions; pagination titles/noindex; technical page noindex)
2. **SITE-002-PROD-SITEMAP-ENABLE-01** — enable/verify OpenCart Google Sitemap feed; add `Sitemap:` to robots after validation
3. **Operator HITL** — confirm Yandex.Metrika / Webmaster codes are deployed to live Twig; re-verify after operator publish

---

## Tooling

```bash
python projects/ocpilot/sites/site-002/tools/site-002-prod-seo-readiness-robots-01.py
python projects/ocpilot/sites/site-002/tools/site-002-prod-seo-readiness-robots-01.py --no-deploy
```

Rollback: upload `rollback/robots.txt` from Storage deployment folder to `/public_html/robots.txt`.
