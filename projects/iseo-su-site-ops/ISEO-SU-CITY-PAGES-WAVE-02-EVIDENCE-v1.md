# ISEO-SU CITY PAGES WAVE 02 EVIDENCE v1

**Task:** `ISEO-SU-SITE-OPS-CITY-PAGES-WAVE-02`  
**Date:** 2026-09-03  
**Site:** `https://i-seo.su/`  
**Decision:** **PASS / COMPLETE — WAVE 2 CITY PAGES ×5 LIVE**

---

## 1. Scope

WAVE 2 only:

- 5 static city SEO pages under `/services/seo/`
- Hub linking block on `b-regionakh.html`
- Self-canonical + indexable
- Static sitemap allowlist + regen + completeness
- Preserve WAVE 1 / 01A form consent baseline via PHP includes

**Not started:** WAVE 3 USA/UAE ×2.  
**Not touched:** SEO-review backlog (CANON-*, TITLE-*, etc.).

---

## 2. Source Hub

| Field | Value |
|-------|-------|
| Live URL | `https://i-seo.su/services/seo/b-regionakh.html` |
| Production path | `/home/n/nikel0rv/i-seo.su/public_html/services/seo/b-regionakh.html` |
| MARS source | `projects/iseo-su-site-ops/production-source/static-html/services/seo/b-regionakh.html` |
| Pre-wave SHA256 | `9ee158037097a3ba5029845fde34d29489abde0129b1827a6f0c712062392c23` |
| Post-wave SHA256 | `20374a198c7bbd72fb0028806d3b5aa21a02361b7cf3f1d857e55c527d29badd` |

---

## 3. Source Architecture

Hybrid static HTML + PHP `$template_parts` includes:

- `content-mobilemenu.php`, `content-topbar.php`
- `content-tarifs-seo.php`, `tarif-calc.php`, `content-calc-seo.php`
- `content-form-seo.php`, `content-footer.php`, `content-seo-popups.php`

Consent is **not** inlined in the HTML file; it is inherited from includes (WAVE 1 / 01A).  
Live city pages: **10** `personal_data_consent` fields; privacy links `/privacy-policy.html`; calculator result consent id `personal_data_consent_callback__FORM_tariff_calc` present.

Hub robots: `index, follow`. Hub had **no** canonical pre-wave (unchanged policy on hub). City pages add **self-canonical** only.

---

## 4. New URL Inventory

1. `https://i-seo.su/services/seo/prodvizhenie-v-sankt-peterburge.html`
2. `https://i-seo.su/services/seo/prodvizhenie-v-kazani.html`
3. `https://i-seo.su/services/seo/prodvizhenie-v-ekaterinburge.html`
4. `https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html`
5. `https://i-seo.su/services/seo/prodvizhenie-v-krasnoyarske.html`

---

## 5. Approved Content Mapping

Per city, only substituted:

- `<title>`, meta description, H1, intro after H1
- Main block title + text + 4 list items + after-list
- FAQ answer #4 only (question unchanged: «Насколько реально попасть на первую страницу поиска?»)

All other blocks (tariffs, stages, calculator, cases, team, forms, FAQ Q1–Q3, menu/footer) retained from hub clone.

**CONTENT MAPPING EXACT:** YES (live validation PASS 5/5)  
**UNAPPROVED CONTENT CHANGES:** 0

---

## 6. Page Creation

Built from hub via `tools/_wave02_build_city_pages.py` into `production-source/static-html/services/seo/`.

| File | Bytes | SHA256 |
|------|------:|--------|
| `prodvizhenie-v-sankt-peterburge.html` | 43901 | `d023d3d79cf5e8c494fc2d9f1fb261d223fe2762a9b2001280c323bbbd08605f` |
| `prodvizhenie-v-kazani.html` | 43679 | `318eb1950edaf6f5135be204513d3c4c96ab751fa3de54475cf161f9f194a756` |
| `prodvizhenie-v-ekaterinburge.html` | 43686 | `4bba37ebbc8f668bdc1d31877940bf53110cf6358eeae38b3f5c9fc160c8f4fb` |
| `prodvizhenie-v-novosibirske.html` | 43656 | `8c9e7ecc6a30570ca0d04f97f5cb3065221d22a0b9e661949bf1e3e404dd1ce1` |
| `prodvizhenie-v-krasnoyarske.html` | 43644 | `8f180a319e358d9d89dec396ee79016abe0e4c3f9737ee350c9dd1dfef7799a2` |

---

## 7. Canonical / Indexability

| Check | Result |
|-------|--------|
| Self-canonical 5/5 | YES |
| `robots` index,follow | YES |
| no noindex | YES |
| HTTP 200 | 5/5 |
| Conflicting canonical | NONE |

---

## 8. Hub Linking

Added block `id="city-seo-pages"` titled **«Выберите ваш город»** with links to all 5 city URLs.  
Live: HTTP 200, block visible, **5/5** links present.

---

## 9. City Backlinks

Each city main block includes contextual link to  
`https://i-seo.su/services/seo/b-regionakh.html`  
(**5/5** live).

---

## 10. Form Consent Preservation

| Check | Result |
|-------|--------|
| City pages consent fields | 10 per page (includes) |
| Privacy link | `/privacy-policy.html` (resolves to approved policy) |
| Calculator result consent | YES (`personal_data_consent_callback__FORM_tariff_calc`) |
| Server / HMAC / recipient | Unchanged |
| Form regression | NONE |

---

## 11. Sitemap Inventory

Updated both:

- `data/sitemaps/sitemap-static-urls-v1.txt`
- `data/sitemaps/public-canonical-static-routes-v1.txt`

**Before:** 127  
**After:** 132 (+5)

---

## 12. Sitemap Regeneration

Generator: `tools/generate-sitemap-static.py`  
Output: `production-source/sitemaps/sitemap-static.xml`  
SHA256: `cc2328b4f43b6ae48b6e9a42030cc8f1591d796378715fdb2f5d35f91edd7154`  
URL count: **132**

---

## 13. Completeness Validation

Validator: `tools/validate-sitemap-static-completeness.py`

```
PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS = 0
ALLOWLIST_COUNT=132
INVENTORY_COUNT=132
SITEMAP_LOC_COUNT=132
PASS
```

---

## 14. Production Backup

Root: `X:\AI MARS\local\sites\iseo-su-production\_city-pages-wave-02\`  
Backup stamp (deploy run): see `backup-*/manifest.json`

| Role | Path |
|------|------|
| MODIFY backup | `b-regionakh.html` (pre SHA `9ee15803…`) |
| MODIFY backup | `sitemap-static.xml` (pre SHA `7a387278…`) |
| CREATE rollback | delete only the 5 new city files |

---

## 15. Deployment

SFTP to `public_html`:

- 5 new city HTML files (CREATE)
- `services/seo/b-regionakh.html` (MODIFY)
- `sitemap-static.xml` (MODIFY)

Post-write verify: **byte match** for all uploads.

---

## 16. Live Page Validation

All 5 URLs: HTTP **200**; exact title/description/H1/intro/main/FAQ#4; self-canonical; indexable; hub backlink; consent covered.  
Evidence JSON: `tools/_wave02_deploy_validate.json`

---

## 17. Hub Validation

`b-regionakh.html`: 200; city block YES; links 5/5; consent retained.

---

## 18. Sitemap Validation

Live `sitemap-static.xml`: 200; valid XML; **132** locs; 5 city URLs once each; duplicates **0**.  
Root `sitemap.xml` still indexes `sitemap-static.xml` + `wp-sitemap.xml`.  
`robots.txt` still references root sitemap.

---

## 19. Regression

Smoke 200: `/`, `/services.html`, `/services/seo.html`, hub, `zarubezhnye.html`, `/tariff-calc`, `/blog/`, `/glossary/`, `/sitemap.xml`, `/sitemap-static.xml`.  
No Metrika / form architecture changes in this wave.

---

## 20. Production / Source Alignment

Source hashes match production for hub, 5 city pages, and `sitemap-static.xml` after deploy (**ALIGNED**).

---

## 21. SEO Content Residual

Texts remain SEO-team responsibility for Advego/Turgenev external checks if still required. No independent copy rewrite performed.

---

## 22. Rollback

1. Restore hub + sitemap from `_city-pages-wave-02/backup-*`
2. Delete only the 5 CREATE city paths
3. Revert allowlist inventories to 127 and regenerate, **or** restore prior `sitemap-static.xml`
4. Redeploy restored set

---

## 23. Final Decision

**PASS / COMPLETE** — WAVE 2 city pages live, hub linked, sitemap updated, completeness PASS.  
WAVE 3 remains **NEXT / OPEN DECISIONS** — not started.
