# ISEO-SU TECH SEO RE-AUDIT 02 — Evidence v1

**Task ID:** `ISEO-SU-SITE-OPS-FULL-SITE-TECH-SEO-REAUDIT-02`  
**Mode:** READ-ONLY  
**Production:** `https://i-seo.su/`  
**Crawl timestamp (contour):** `20260904-163451`  
**Evidence root (Storage):** `X:\AI MARS STORAGE\iseo-su-site-ops\tech-seo-reaudit-02\20260904-163451\`  
**Prior audit baseline:** Tech SEO Audit 01 / SEO Review Pack 01 (2026-08-21 contour under `tech-seo-audit-01`)

---

## 1. Preflight (recorded)

| Check | Value |
|-------|--------|
| CWD | `X:\AI MARS` |
| Volume | `X:` / label **`AI WS`** |
| Branch | `mars/canonical-post-recovery` |
| HEAD (at crawl start) | `0cd709b96ee9cb36f2893de9d6bc73b5b26f3b86` |
| Origin tip (at crawl start) | `adbdbe4258dccb376bf452ba2effcbc6a787a47f` |
| Staged | empty |
| Dirty tree | large foreign WIP (~1300+ paths) — **untouched** |
| Production / source mutations | **0** |
| Menu / navigation mutations | **0** |

Later session tip may advance due to unrelated report-hub commits; audit artifacts are docs-only.

---

## 2. Crawl methodology

- Fresh BFS / link-following crawl of `https://i-seo.su/` (not reuse of audit-01 raw pages).
- Seed: home + sitemaps (`/sitemap.xml`, `/sitemap-static.xml`, `/wp-sitemap.xml` children) + known new-page allowlist.
- Script: `crawl_iseo_tech_seo-reaudit02.py` (stored under contour).
- Analyzer: `analyze_reaudit02.py` → `analysis-stats.json`, `findings-raw.json`, project FINDINGS CSV.
- HTTP note: crawler stores **final** status after redirects; 3xx counted via `redirect_chain` / final≠request (~9).

### Key raw artifacts

| File | Role |
|------|------|
| `pages.json` / `pages-full.json` | Page entities (~1053) |
| `crawl-summary.json` | Crawl rollup |
| `inlinks.json` | Internal link graph |
| `image-status.json` / `asset-status.json` | Asset HTTP |
| `sitemap-meta.json` / `robots.txt` | Sitemap + robots snapshot |
| `new-pages-probe.json` | 14 landings + webinar |
| `form-security-probe.json` | Handlers / config signals |
| `menu-nav-probe.json` | Nav visibility |
| `local-form-layout-probe.json` | First-screen / 100vh |
| `sitemap-completeness-local.txt` | Local validator output |

---

## 3. Locked counts (analyzer)

| Metric | Value |
|--------|------:|
| TOTAL CRAWLED URLS | 1053 |
| HTML 200 | 705 |
| 3XX (via chain) | 9 |
| Page-level 4XX | 0 |
| Page-level 5XX | 0 |
| INDEXABLE | 650 |
| NOINDEX | 55 |
| Broken internal href pairs | 0 |
| Link-to-redirect pairs | 0 |
| Broken images (unique) | 1 (`/img/logo.svg` 404) |
| Broken CSS | 6 (blog-author relative path quirk) |
| Broken JS | 0 |
| Low-height overlap regression (live 14) | 0 |

Canonical (all HTML / indexable nuance):

| Signal | All HTML | Indexable-only (narrative) |
|--------|---------:|---------------------------:|
| CANON-MISSING | 206 | ~156 |
| CANON-MISMATCH | 120 | ~120 |
| CANON-TO-REDIR / TO-ERR | 0 / 0 | 0 / 0 |

Titles / meta / H1:

| Signal | Value |
|--------|------:|
| TITLE missing | 0 |
| TITLE-DUP groups | 10 (~152 URLs in families) |
| TITLE-LONG (>70) | 25 |
| META-MISSING | 23 |
| META-DUP groups | 2 |
| H1-MISSING | 5 (indexable core: report-hub family) |
| MULTIPLE H1 | 0 |

Sitemap / indexability:

| Signal | Value |
|--------|------:|
| Static sitemap URL count (public) | **139** |
| Local completeness `PUBLIC − STATIC` | **0 / PASS** |
| Static/WP overlap | 0 (expected architecture) |
| Sitemap URL 4xx/5xx | 0 |
| SM-NONINDEX | ~54 |
| Indexable not in sitemap (excl. intentional policy trio) | ~142 |
| POLICY-NO-SITEMAP (USA / UAE / Webinar) | 3 — **INTENTIONAL** |

---

## 4. New page contour (live)

All **14** SEO landings + webinar: HTTP **200**, indexable, consent on lead forms **OK**, safe first-screen class present, no stale `height:100vh` pilot body class on live.

| Family | Count | Sitemap | Typical inlinks | Menu |
|--------|------:|---------|-----------------|------|
| City | 5 | YES | ~5 (hub + peers) | NO |
| Niche | 7 | YES | ~1 (from `/services/seo.html`) | NO |
| USA / UAE | 2 | NO | 0 | NO |
| Webinar | 1 | NO | 0 | NO |

**Webinar live:** date **10 сентября 2026**, **19:00 МСК**; old-date occurrences on live HTML: **0**.

---

## 5. Forms / security (read-only)

| Check | Result |
|-------|--------|
| Root handlers | **12** |
| Consent guard (shared) | present |
| HMAC | active (security path) |
| `test_mode` (tracked `production-source/forms/iseo-form-config.php`) | **OFF / false** |
| Normal recipient | **nikel007i33@yandex.ru** only |
| `im.work@nail.ru` | absent |
| `im.work@mail.ru` | test_recipients path only — not normal routing |
| Hidden CC/BCC | 0 |
| Live lead uncovered consent | **0** |
| Crawl “uncovered” forms (5) | **false positives for consent policy**: offers/glossary **search** UIs + `varvara-new.php` tool — not PII lead forms |

---

## 6. False-positive exclusions

1. **Menu absence** for city/niche/USA/UAE/webinar → `OPERATOR/SEO DECISION`, not implementation defect.
2. **USA / UAE / Webinar** not in sitemap → `INTENTIONAL / OPERATOR POLICY`.
3. Search forms without `personal_data_consent` → not counted as uncovered lead consent failures.
4. Decorative `alt=""` → not auto-defect; content-image missing alt → REVIEW/LOW.
5. Shared commercial blocks on city/niche templates → **EXPECTED TEMPLATE REUSE**, not SEO-risk body clone unless title/H1/body uniqueness collapses (not observed as CRITICAL).
6. Crawler final-200 after redirect → do not treat as page-level 3xx histogram on status field alone.

---

## 7. Comparison vs Audit 01 (high level)

| Topic | Prior | Current | Delta |
|-------|-------|---------|-------|
| SM-CHILD-404 | open | **CLOSED** | IMPROVED |
| Static sitemap completeness 139 | fixed | **PASS** | CLOSED |
| LINK-TO-REDIR | 129 | **0** | CLOSED |
| Mass blog relative IMG 404 | open | largely closed; residual logo.svg | IMPROVED |
| CANON-MISSING (indexable) | 162 | ~156 | IMPROVED |
| CANON-MISMATCH | ~117 | ~120 | SAME / slight WORSE |
| META-MISSING | 23 | 23 | SAME |
| Low-height overlap | known then fixed | **0 regression** | CLOSED live |
| New city/niche/USA/UAE/webinar | n/a | live + audited | NEW CONTOUR |

---

## 8. Finding IDs (CSV)

Path: `audits/tech-seo/ISEO-SU-TECH-SEO-REAUDIT-02-FINDINGS.csv`  
Rows: **359** (sampled/capped per family where noted).  
IDs: `CANON-MISMATCH`, `CANON-MISSING`, `CSS-BROKEN`, `H1-MISSING`, `IMG-ALT`, `IMG-BROKEN`, `IMG-HUGE`, `LAYOUT-LOWHEIGHT`, `MENU-NAV-DECISION`, `META-DUP`, `META-MISSING`, `OG-MISSING`, `ORPHAN-CRAWLER`, `POLICY-NO-SITEMAP`, `SM-NONINDEX`, `TITLE-DUP`, `TITLE-LONG`.

---

## 9. Mutations

| Layer | Count |
|-------|------:|
| Production | 0 |
| Source implementation | 0 |
| DB | 0 |
| Sitemap / menu | 0 |
| Audit docs created | yes (this wave) |

---

*Evidence v1 · ISEO-SU-SITE-OPS-FULL-SITE-TECH-SEO-REAUDIT-02 · read-only.*
