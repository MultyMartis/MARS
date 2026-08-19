# BASELINE — FP-0002 Production Final (P18I)

**Baseline ID:** `FP-0002-PRODUCTION-FINAL-2026-08-20-P18I`  
**Established:** 2026-08-20  
**Domain:** https://shpigovsky.ru/  
**Core version:** `0.3.21-p18i`

---

## Runtime

| Item | Value |
|------|--------|
| Environment | **PRODUCTION** |
| Host | Beget — `/home/s/shpigovsky/shpigovsky.ru/public_html` |
| WordPress `home` / `siteurl` | `https://shpigovsky.ru` |
| Public site | HTTP 200 |

---

## Indexability

| Item | Value |
|------|--------|
| Indexing | **OPEN — HUMAN-APPROVED** |
| P18G guard | **ACTIVE** |
| `blog_public` | `1` |
| Robots | Globally permissive; sitemap in robots.txt |
| Sitemap | `https://shpigovsky.ru/wp-sitemap.xml` (200, 58 URLs) |

---

## Search consoles

| Service | P18I status |
|---------|-------------|
| Google Search Console | **AUTH BLOCKER** — operator submit |
| Yandex Webmaster | **AUTH BLOCKER** — operator submit |

---

## Mail / forms / privacy

| Item | Value |
|------|--------|
| SMTP | VERIFIED / ACTIVE |
| Forms | ACTIVE |
| Lead registry | ACTIVE (`fp02_form_leads`) |
| Lead retention (configured) | **0** (recommended **730**) |
| Cookie consent | ACTIVE |
| Yandex Metrika | CONSENT-GATED |
| Form goals | CONSENT-GATED |
| Cookie Policy | Factually current; legal sign-off non-blocking |

---

## Crawl summary (P18I final)

| Metric | Value |
|--------|------:|
| Crawl URLs | 107 |
| Sitemap URLs | 58 |
| HTTP 200 | 106 |
| Unresolved CRITICAL | 0 |
| Verdict | **CLEAN** |

---

## Redirects

Legacy 301 set: **7/7 PASS** (`/yoga`, `/about`, `/psy`, `/home`, `/policy`, `/neuro`, `/reviews`).

---

## Source parity

P18I deployed surfaces: theme `inc/template-tags.php`, `home-fallbacks.php`, `home-helpers.php`, `reusable-blocks-helpers.php`; plugin `shpigovsky-core.php`, `SystemDashboard.php` — **MATCH** after deploy.

---

## Dashboard

MetaCODE Dashboard: wave **P18I Final Launch Closeout**; maintenance posture.

---

## Non-blocking notes

- External legal sign-off (Cookie Policy)
- Apply lead retention 730 when operator accepts
- GSC / Yandex sitemap UI submission
- Editorial SEO refinements (missing meta descriptions on some pages)

---

## Evidence pack

`REPORTS/evidence/prod-p18i-final-launch-closeout/`

**Report:** `REPORTS/REPORT-FP-0002-PROD-P18I-FINAL-LAUNCH-CLOSEOUT.md`
