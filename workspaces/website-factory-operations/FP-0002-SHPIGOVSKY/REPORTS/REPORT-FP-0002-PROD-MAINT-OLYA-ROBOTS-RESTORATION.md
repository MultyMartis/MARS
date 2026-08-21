# REPORT — FP-0002 PROD-MAINT Olya Robots Restoration + SEO Safety Audit

**Date:** 2026-08-21  
**Status:** PASS  
**Core deployed:** `0.3.25-olya-robots`  
**Production:** https://shpigovsky.ru/  
**Indexing:** OPEN — HUMAN APPROVED (`blog_public=1`)  
**Evidence:** `REPORTS/evidence/prod-maint-olya-robots-restoration/`

---

## 1. Mission result

Restored Olya’s SEO `robots.txt` policy for production, separated it from human OPEN/CLOSED indexability, proved P18G close/open lifecycle cannot destroy that policy, and updated canonical source + Forge knowledge.

---

## 2. Olya source capture

**OLYA ROBOTS SOURCE CAPTURED EXACTLY BEFORE REVIEW**

| Field | Value |
|-------|--------|
| Source | P18G intake `01-pre-intake.json` → `robots_physical.body` (physical docroot file captured when Olya policy was live) |
| Evidence copy | `evidence/.../00-olya-robots-supplied-exact.txt` |
| SHA-256 | `b484afdc1b196dc930dc3bbf70d5cbddd8a4b6b65df43ea9da04c6416a237616` |
| Bytes / lines | 2748 / 138 |
| Encoding | UTF-8 BOM + CRLF |

No operator attachment was present in the live chat intake; the P18G physical capture is the proven Olya body matching the charter’s described directives.

---

## 3. Live before

**CURRENT LIVE ROBOTS OWNER AND PRECEDENCE PROVEN**

| Surface | Finding |
|---------|---------|
| HTTP `https://shpigovsky.ru/robots.txt` | 200, `text/plain`, SHA `ec64f8b8…`, generic MARS/WP-open body |
| Physical docroot | **Exists** `/home/s/shpigovsky/shpigovsky.ru/public_html/robots.txt` — same SHA as HTTP |
| WordPress virtual | Would match only if physical missing; physical was present |
| `IndexingControl::robots_body(true)` (pre-fix) | Identical generic template (`Disallow: /wp-admin/` + admin-ajax + Sitemap) |
| `blog_public` | 1 |

Owner: **physical file written by IndexingControl OPEN template** (not Olya SEO policy).

---

## 4. Root cause

**OLYA ROBOTS REPLACEMENT / SHADOWING ROOT CAUSE PROVEN**

1. Olya’s multi-agent SEO `robots.txt` existed physically (P18G intake SHA `b484afdc…`).
2. `IndexingControl::sync_robots_file(false)` on human/technical CLOSE overwrote it with global `Disallow: /`.
3. On OPEN, `robots_body(true)` wrote a **generic MARS open template**, not the prior SEO policy (`is_our_closed` path forced rewrite).
4. Result: OPEN indexing with a short non-Olya robots file — SEO policy destroyed.

“Preserve complex host-managed robots” only helped when OPEN *and* the file was still complex; after CLOSE the complex file was already gone.

---

## 5. Ownership model

**OPEN INDEXING PRESERVES OLYA SEO ROBOTS POLICY**  
**ONE DETERMINISTIC ROBOTS AUTHORITY ESTABLISHED**

| State | Authority |
|-------|-----------|
| OPEN | Canonical `shpigovsky-core/assets/robots-seo-policy.txt` → physical `/robots.txt` |
| CLOSED | Temporary global disallow; SEO body backed up to `robots.txt.fp02-seo-open.bak` |
| Recovery | OPEN always restores canonical SEO policy (not generic template) |

Runbook: `DOCS/OPERATIONS-INDEXING-ROBOTS-OWNERSHIP-v1.md`

---

## 6. Syntax audit

**OLYA ROBOTS SYNTAX AUDIT COMPLETE**

Authorities recorded in `16-official-rules-evidence.json` (Yandex Clean-param + Google robots.txt docs, 2026-08-21).

---

## 7. WordPress resource crawlability

**WORDPRESS RESOURCE CRAWLABILITY VERIFIED AGAINST OLYA RULES**

Live homepage inventory proved theme/plugin CSS/JS and uploads OK under Allow rules, but **theme `.webp` and font files** under `/wp-content/` were blocked by `Disallow: /wp-`. Minimal Allows added for `webp` / `woff` / `woff2` / `ttf`.

---

## 8. Tracking / Clean-param

**TRACKING-PARAMETER ROBOTS POLICY VALIDATED AGAINST CURRENT SITE**

- Yandex: removed `Disallow: *utm*=` / `*openstat=` (defeated Clean-param per official docs); kept explicit Clean-param list; removed ineffective `Clean-param: utm`.
- Google/Bing/*: kept Disallow utm/openstat (Clean-param unsupported).

---

## 9. Legal pages

| URL | HTTP | meta robots (live) | robots.txt | Classification | Olya decision |
|-----|------|--------------------|------------|----------------|---------------|
| `/privacy-policy/` | 200 | `max-image-preview:large` | Disallow | SAFE AS-IS (crawl blocked; SERP exclusion not guaranteed) | Preserved |
| `/user-agreement/` | 200 | same | Disallow | SAFE AS-IS | Preserved |
| `/consent-personal-data/` | 200 | same | Disallow | SAFE AS-IS | Preserved |
| `/cookie-files-policy/` | 200 | same | Disallow | SAFE AS-IS | Preserved |

Note: Disallow prevents crawlers from seeing page-level meta. No silent SEO/business change to legal indexing policy.

---

## 10. Sitemap

**OLYA ROBOTS SITEMAP DIRECTIVE VALID**

`https://shpigovsky.ru/wp-sitemap.xml` → HTTP 200, production host, no staging URLs (`01-sitemap-http.json`).

---

## 11. Olya → final diff

**EVERY DEVIATION FROM OLYA ROBOTS IS EXPLICITLY JUSTIFIED**

See `15-olya-to-final-diff.json`. Final SHA `2594093919d01f067bcd3776d50d973cfa20a1faf4a6d63fc23f21367d08529e`.

---

## 12. P18G lifecycle

**P18G CLOSE/OPEN LIFECYCLE DOES NOT DESTROY OLYA ROBOTS POLICY**

Isolated harness (`03-p18g-lifecycle-harness.json`): OPEN → CLOSE (backup) → OPEN restores identical SEO SHA; not generic MARS. **No production close performed.**

---

## 13. Read-only safety

**READ-ONLY ROBOTS VALIDATION CANNOT MUTATE ROBOTS POLICY**

- Watchdog: alert-only (no file writes).
- Forensics scripts: read-only.
- WPilot: `write_enabled=false` (site policy).
- Mutations only via explicit deploy / `IndexingControl` authorized state changes.

---

## 14. Live after

**LIVE ROBOTS MATCHES REVIEWED OLYA POLICY**

HTTP 200; SHA `2594093919…`; no global `Disallow: /`; Yandex group present; Sitemap correct (`05-live-robots-after.json`).

---

## 15. Rule matrix

**FINAL ROBOTS RULE MATRIX PASS** — `06-rule-matrix.json`

---

## 16. Resource rendering

**FINAL ROBOTS DOES NOT BLOCK ESSENTIAL PUBLIC RENDERING RESOURCES** — `09-resource-rendering.json`

---

## 17. Indexability

**GLOBAL INDEXING REMAINS OPEN AFTER OLYA ROBOTS RESTORATION**

`blog_public=1`, effective `OPEN`, homepage indexable, no global X-Robots noindex (`08-indexability-regression.json`, `14-dashboard-open-label.json`).

---

## 18. Guard / watchdog

- P18G guard: ACTIVE  
- Watchdog: ACTIVE (baseline effective OPEN)  
- Human decision: OPEN  
- Dashboard: **Индексация сайта: открыта**

---

## 19–20. Canonical recovery + parity

**OLYA ROBOTS POLICY HAS A CANONICAL RECOVERY SOURCE**  
**ROBOTS SOURCE / PRODUCTION PARITY PASS**

| Path | Role |
|------|------|
| `WORDPRESS/seo/OLYA-ROBOTS-REVIEWED-CANDIDATE.txt` | Review / docs copy |
| `WORDPRESS/plugins/shpigovsky-core/assets/robots-seo-policy.txt` | Runtime canonical |
| Production `/robots.txt` | Physical OPEN serving copy — SHA match |

---

## 21. Activity log

Logged: `seo_robots_restored` — «SEO robots.txt восстановлен / актуализирован» (not an indexing close/open event).

---

## 22. Current project state

**PRODUCTION / MAINTENANCE — STABLE**

---

## Acceptance

FP-0002 OLYA ROBOTS RESTORATION COMPLETE — THE OPERATOR-PROVIDED OLYA ROBOTS POLICY WAS CAPTURED AND AUDITED AGAINST CURRENT PRODUCTION AND OFFICIAL SEARCH-ENGINE RULES — ITS SEO INTENT WAS PRESERVED AND ONLY PROVEN TECHNICAL/SEO CONFLICTS WERE CORRECTED — THE ROOT CAUSE OF THE PREVIOUS REPLACEMENT/SHADOWING WAS IDENTIFIED AS FAR AS EVIDENCE ALLOWS — GLOBAL HUMAN-OWNED INDEXABILITY AND SEO ROBOTS POLICY NOW HAVE SEPARATE OWNERSHIP — OPEN INDEXING SERVES THE CANONICAL OLYA SEO POLICY — P18G CLOSE/OPEN SAFETY CANNOT DESTROY THAT POLICY — READ-ONLY PROBES CANNOT MUTATE ROBOTS — REQUIRED WORDPRESS RENDERING RESOURCES REMAIN CRAWLABLE — SITEMAP IS VALID — GLOBAL INDEXING REMAINS OPEN — THE FINAL ROBOTS POLICY HAS A CANONICAL RECOVERY SOURCE — SOURCE/PRODUCTION PARITY PASSES — CANONICAL REMOTE IS UPDATED — FP-0002 REMAINS PRODUCTION / MAINTENANCE — STABLE.
