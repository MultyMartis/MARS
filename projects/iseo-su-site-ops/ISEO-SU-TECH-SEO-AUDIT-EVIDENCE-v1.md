# ISEO-SU TECH SEO AUDIT EVIDENCE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-RECIPIENT-REMOVE-AND-TECH-SEO-AUDIT-01  
**Date:** 2026-08-21  
**Site:** `https://i-seo.su/`  
**Mode:** READ-ONLY crawl after recipient correction (GET/HEAD only; no form POST; no WP/admin/DB mutation)

---

## 1. Audit Scope

Publicly reachable surfaces discovered via seeds + sitemaps + internal links, including:

- static marketing pages (`.html`)
- `/services/**`, `/cases/**`
- WordPress pages / blog archive / posts
- `/offers`, `/tariff-calc`
- `/glossary/` archive + published singles
- Report Hub sibling routes when linked
- sitemap/robots endpoints

**Out of scope mutations:** form POSTs, calculator lead submits, admin, DB, file writes (except local evidence artefacts).

## 2. Crawl Method

| Item | Value |
|------|-------|
| Crawler | Custom Python (`requests` + BeautifulSoup) |
| User-Agent | `MARS-ISEO-TechSEO-Audit/1.0 (+read-only; contact site-ops)` |
| Seeds | Known routes + `/sitemap.xml` + `/wp-sitemap.xml` + `/sitemap-static.xml` |
| Discovery | Sitemap locs + same-host internal `<a href>` BFS |
| Follow-up | Bounded outlink status check (up to 400 missing targets) |
| Images | HEAD/GET sample ≤250 unique on-host image URLs |

## 3. Crawl Safety

| Control | Value |
|---------|-------|
| Target rate | **~1.4 req/s** |
| Concurrency | **2** |
| Aggressive brute paths | **NO** |
| Form POST | **0** |
| Mail sent | **0** |
| Production mutations during crawl | **0** |

Elapsed ≈ **998 s**. After the wave, intermittent TLS/read timeouts were observed on opportunistic follow-up samples — crawl rate was already conservative; further hammering stopped.

## 4. URL Inventory

| Metric | Count |
|--------|------:|
| TOTAL URLS CRAWLED | **1033** |
| HTML-like docs analyzed | **696** |
| INDEXABLE (meta/robots heuristic, 200) | **643** |
| Sitemap-discovered URL set | **486** |
| HTTP 200 | **1032** |
| HTTP 0 / fetch fail | **1** |
| HTTP 4xx (crawled page set) | **0** |
| HTTP 5xx (crawled page set) | **0** |

Machine inventory: `projects/iseo-su-site-ops/audits/tech-seo/ISEO-SU-TECH-SEO-URL-INVENTORY-v1.csv`  
Raw crawl: `X:\AI MARS STORAGE\iseo-su-site-ops\tech-seo-audit-01\`

Page-type mix (crawled): GLOSSARY_SINGLE 184, BLOG_POST 167, BLOG_ARCHIVE 126, SERVICE 79, CASE 38, OFFER 35, STATIC 28, plus WP_PAGE/OTHER/tool routes.

## 5. HTTP Findings

- **No 4xx/5xx** among successfully classified crawled document URLs in the main inventory.
- **1** fetch failure (`http_status=0`) — transient/network class; not treated as site outage.
- Soft-404 heuristic: no strong confirmed soft-404 set after review thresholds.

## 6. Redirect Findings

| Metric | Count |
|--------|------:|
| URLs with redirect history | **136** |
| Chains ≥2 hops | **0** |
| Internal links pointing at redirecting URLs | **129** (REVIEW) |

No redirect loops detected in crawl graph.

## 7. Indexability

- `noindex` / non-indexable heuristic set includes offer/private-like surfaces and some WP entities.
- **52** sitemap-listed URLs classified non-indexable (REVIEW — often intentional for offers/tags/users).
- **197** indexable crawled URLs absent from discovered sitemap union (REVIEW — dual-sitemap architecture; not auto-merge).

## 8. Canonicals

| Signal | Count | Class |
|--------|------:|-------|
| Missing canonical on content-like 200 | **162** | REVIEW NEEDED |
| Canonical/self mismatch / unresolved | **117** | REVIEW NEEDED |
| Canonical→non-200 / redirect | **0** confirmed in refined set | — |

Static `.html` templates frequently lack `rel=canonical` — may be historical template design rather than acute breakage.

## 9. Sitemap / Robots

### robots.txt

Fetched OK. Notable Disallow: `/offer/*`, `/blog/offer/*`, `/wp-`, search/tag/author/feed patterns. Used as **audit signal only**.

### Sitemap architecture (actual)

1. **`/sitemap.xml`** — Yoast-styled index referencing:
   - `sitemap-static.xml` (**200**)
   - `post-sitemap.xml` (**404**)
   - `page-sitemap.xml` (**404**)
   - `category-sitemap.xml` (**404**)
2. **`/wp-sitemap.xml`** — WordPress core index (**200**), includes posts/pages/offer/glossary/taxonomies/users.
3. Dual public indexes coexist.

**CONFIRMED HIGH:** Yoast-styled children `post|page|category-sitemap.xml` return **404** while still advertised by `/sitemap.xml`.

## 10. Titles

- Missing `<title>` on HTML 200: **0**
- Duplicate title groups: **10** (≈**161** URL involvements)
- Largest cluster: blog archive title repeated across ~**119** URLs (pagination/category — REVIEW)
- Long titles (>~70): **24** (REVIEW)

## 11. Meta Descriptions

- Missing on indexable 200: **23** (REVIEW / often LOW)
- Duplicate meta groups: **2** (≈**137** URL involvements — REVIEW; may include template defaults)

## 12. H1

- Missing H1: **5** — `varvara-new.php` + Report Hub `client-report` query variants (sibling/tool; REVIEW / LOW for marketing priority)
- Multiple H1: **0** in crawl set
- Empty H1: **0** material set

## 13. Internal Linking

- Broken internal link targets (4xx/5xx): **0** in crawled graph
- Links-to-redirects: **129** (LOW / REVIEW)
- Crawler-level orphans (0 inlinks but seen via sitemap/crawl): **57** (REVIEW — not GSC truth)

## 14. Images

Sampled ≤250 on-host images.

| Signal | Count | Class |
|--------|------:|-------|
| Broken (404) in sample | **96** | **CONFIRMED HIGH** |
| Of which `/blog/20YY/.../img/` relative resolve | **62** | root cause pattern |
| `/blog/author/.../img/` relative | **31** | same class |
| Huge (>1.5MB) | **2** | REVIEW |
| Pages with many empty/missing alt | large | REVIEW — decorative empties likely |

**Root cause direction:** relative `img/…` on blog posts resolves against `/blog/YYYY/` or author paths instead of site-root `/img/`.

## 15. Structured Data

- JSON-LD syntax errors in crawl parse: **0**
- Schema richness varies by template; no speculative rich-result claims.

## 16. Social Meta

- Missing key OG tags on important templates: **97** URLs (LOW / REVIEW)
- Secondary priority unless template corruption (not observed as systemic blank titles).

## 17. Frontend / JS

Playwright Chromium sample **failed** in this environment (launch/navigation errors/timeouts). No reliable console-error inventory from headed automation this run.

## 18. Mobile

**LIMITED.** Overflow checks at 320/360/390/414 **not completed** (Playwright failure). Prior programme knowledge: glossary-scoped overflow CSS already shipped; not re-validated visually here.

## 19. Performance Lab Sample

Opportunistic HTML GET weights deferred after post-crawl TLS timeouts (avoid further load). Label: **LAB incomplete / not field CWV**.

## 20. Confirmed Issues

1. **SM-CHILD-404 (HIGH)** — `/sitemap.xml` children `post|page|category-sitemap.xml` = 404  
2. **IMG-BROKEN (HIGH)** — relative blog image paths → 404 under `/blog/YYYY/img/` and `/blog/author/...`

## 21. Expected Behavior

- Dual sitemap indexes (`/sitemap.xml` + `/wp-sitemap.xml`) as architecture (INFO) — do not auto-duplicate glossary into custom static sitemap.
- `/offer/*` disallowed in robots — intentional commercial privacy posture.
- Operator mailbox retained only in unused `test_recipients` while `test_mode=false`.

## 22. Review Needed

Canonical gaps/mismatches, duplicate blog titles, missing metas, orphans, links-to-redirects, OG gaps, alt-text volume, sitemap indexable mismatches — require SEO/product judgment before implementation waves.

## 23. Raw Artifact Index

| Artifact | Location |
|----------|----------|
| Crawl raw | `X:\AI MARS STORAGE\iseo-su-site-ops\tech-seo-audit-01\` |
| URL inventory CSV | `projects/iseo-su-site-ops/audits/tech-seo/ISEO-SU-TECH-SEO-URL-INVENTORY-v1.csv` |
| Findings CSV | `projects/iseo-su-site-ops/audits/tech-seo/ISEO-SU-TECH-SEO-FINDINGS-v1.csv` |
| SEO-facing report | `projects/iseo-su-site-ops/reports/ISEO-SU-TECH-SEO-AUDIT-FOR-SEO-TEAM-v1.md` |
| Recipient removal evidence | `ISEO-SU-FORM-OPERATOR-RECIPIENT-REMOVAL-EVIDENCE-v1.md` |

## 24. Final Technical Verdict

Recipient routing corrected and aligned. Site HTTP surface of crawled URLs is largely healthy (**0** page-level 4xx/5xx). Two **HIGH** confirmed technical defects require Site Ops fix waves: broken Yoast child sitemaps advertised by `/sitemap.xml`, and blog relative image 404 pattern. Remaining items are mostly REVIEW/LOW for prioritization with SEO — **no audit remediations applied in this task**.
