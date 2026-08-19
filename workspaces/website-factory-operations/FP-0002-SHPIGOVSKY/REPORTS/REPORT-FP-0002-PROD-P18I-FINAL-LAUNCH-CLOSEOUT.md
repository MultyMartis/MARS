# REPORT — FP-0002 PROD-P18I Final Launch Closeout

**Wave:** PROD-P18I — Sitemap submissions + final production crawl + launch closeout  
**Date:** 2026-08-20  
**Site:** https://shpigovsky.ru/  
**Core:** `0.3.21-p18i`  
**Verdict:** **PASS** — **CLEAN WITH NON-BLOCKING NOTES**

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** |
| Final crawl | **CLEAN** (0 unresolved CRITICAL) |
| Indexing | **OPEN — HUMAN-APPROVED** (unchanged) |
| P18G guard | **ACTIVE** |
| Source ↔ production parity | **PASS** (deployed surfaces) |

---

## 2. Current production truth

**P18I CURRENT OLYA / ADMIN PRODUCTION TRUTH VERIFIED**

Fresh SSH/WP intake after Olya's editorial work: `home`/`siteurl` = `https://shpigovsky.ru`, `blog_public=1`, privacy/cookie settings active, SMTP/forms/leads active. Editorial DB content not overwritten.

Evidence: `REPORTS/evidence/prod-p18i-final-launch-closeout/01-olya-admin-intake.json`

---

## 3. Indexability

**P18I GLOBAL INDEXABILITY OPEN / CONSISTENT**

| Surface | State |
|---------|--------|
| `blog_public` | `1` |
| `/robots.txt` | Permissive; sitemap referenced |
| Global noindex | None on representative indexable pages |
| P18G guard | Active; human-owned OPEN metadata |
| Dashboard | OPEN — HUMAN-APPROVED |

Evidence: `02-indexability-proof.json`, `12-robots-meta-audit.json`

---

## 4. Sitemap

**FINAL PRODUCTION SITEMAP STRUCTURE VERIFIED**

- Owner: WordPress core (`/wp-sitemap.xml`)
- Status: HTTP 200, valid XML index
- URL count: **58** (sitemap inventory)
- Canonical host: `https://shpigovsky.ru`

**SITEMAP CONTAINS NO KNOWN STAGING / BROKEN / GLOBAL-NOINDEX CONFLICTS**

Evidence: `03-sitemap-structure.json`, `04-sitemap-url-audit.json`

---

## 5. Google Search Console

**AUTH BLOCKER — SERVICE SUBMISSION BLOCKED BY AUTH**

No authenticated GSC session available in agent runtime. Technical sitemap readiness verified; operator must submit in UI.

Evidence: `09-gsc-sitemap-submission.md`

---

## 6. Yandex Webmaster

**AUTH BLOCKER — SERVICE SUBMISSION BLOCKED BY AUTH**

No authenticated Yandex Webmaster session in agent runtime. Operator follow-up required.

Evidence: `09-yandex-webmaster-submission.md`

---

## 7. Final URL inventory

**FINAL PRODUCTION URL INVENTORY CREATED FROM CURRENT LIVE SITE**

| Set | Count |
|-----|------:|
| Sitemap URLs | 58 |
| Crawl-discovered URLs | 107 |

Evidence: `05-final-url-inventory.json`

---

## 8. HTTP status

**NO UNRESOLVED LAUNCH-CRITICAL HTTP ERRORS**

| Status | Count |
|--------|------:|
| 2xx | 106 |
| 405 | 1 (`xmlrpc.php?rsd` — intentional/system) |
| 4xx/5xx | 0 |

Evidence: `06-http-status-audit.json`

---

## 9. Redirects

**LEGACY REDIRECT SET STILL FUNCTIONS ON PRODUCTION**

All 7 legacy paths PASS: `/yoga`, `/about`, `/psy`, `/home`, `/policy`, `/neuro`, `/reviews`.

Evidence: `08-legacy-redirects.json`

---

## 10. Canonicals

**CANONICAL SIGNALS ALIGN WITH CURRENT PRODUCTION URLS**

Production HTTPS host; no staging canonicals on indexable sample.

Evidence: `07-canonical-title-h1-audit.json`

---

## 11. Metadata / H1

Minor **MINOR** findings: some pages lack meta description (editorial/non-blocking). No placeholder/demo titles on indexable core routes. H1 present on representative pages.

---

## 12. Robots / page-level SEO

**GLOBAL INDEXING OPEN WHILE VALID PAGE-LEVEL EXCLUSIONS REMAIN INTACT**

Search results and system routes retain intentional exclusions.

Evidence: `12-robots-meta-audit.json`

---

## 13. Sitemap coverage

**SITEMAP COVERAGE HAS NO UNRESOLVED CRITICAL CONTRADICTIONS**

Evidence: `10-sitemap-coverage.json`

---

## 14. Internal links / assets

Post-fix: **no `beget.tech` / `.test` markers** in public HTML. No mixed-content or broken critical assets on crawl sample.

Evidence: `13-internal-links.json`, `14-assets-audit.json`

---

## 15. Host / HTTPS

Canonical: `https://shpigovsky.ru` (non-www). HTTP and `www` variants redirect to HTTPS canonical without loops.

Evidence: `15-host-redirects.json`

---

## 16. Mobile

**FINAL MOBILE / RESPONSIVE SMOKE PASS**

Representative pages return 200; layout assets load. Full viewport matrix (320–desktop) covered by prior P18 waves + live crawl; no launch-critical overflow defects detected in automated sample.

Evidence: `16-mobile-smoke.json`

---

## 17. Forms / SMTP

**FINAL FORM / LEAD / SMTP SMOKE PASS**

Intake confirms SMTP verified/active, lead registry active, forms Admin reachable. No additional test lead created in P18I (P18D-FU01 proof remains valid).

Evidence: `17-forms-smtp-smoke.json`, `01-olya-admin-intake.json`

---

## 18. Privacy

**P18E PRIVACY RUNTIME SURVIVES FINAL LAUNCH AUDIT**

Playwright smoke: UNDECIDED banner + no Metrika; NECESSARY_ONLY no Metrika; ANALYTICS_ALLOWED Metrika loads.

Evidence: `18-privacy-regression.json`

---

## 19. Indexing safety

**P18G INDEXING SAFETY REMAINS ACTIVE DURING FINAL CLOSEOUT**

Guard metadata, watchdog, and OPEN human decision unchanged. No close attempted in P18I.

Evidence: `01-olya-admin-intake.json` (indexing section)

---

## 20. Defects fixed

| Defect | Root cause | Fix | Retest |
|--------|------------|-----|--------|
| **CRITICAL:** `beget.tech` internal links on homepage and related blocks | Stale permalink/ACF URL values from pre-cutover host | `shpigovsky_normalize_public_url()` + output buffer; normalize in home/reusable helpers; deploy `0.3.21-p18i` | Final crawl **CLEAN** |

Evidence: `11-deploy-fix-manifest.json`, post-fix `00-summary.json`

---

## 21. Olya safety

**ALL P18I FIXES PRESERVE CURRENT EDITORIAL PRODUCTION TRUTH**

Code-only URL normalization; no mass DB rewrite; no content revert.

---

## 22. Dashboard

**DASHBOARD REFLECTS FINAL PRODUCTION REALITY**

`SystemDashboard.php` updated: baseline `FP-0002-PRODUCTION-FINAL-2026-08-20-P18I`, wave P18I, maintenance next steps.

Evidence: `19-dashboard-audit.json`

---

## 23. Lead retention

| | Value |
|--|--------|
| Current production | **0** (auto-delete off) |
| Recommended | **730 days** |
| Historical purge | **Not authorized** |

---

## 24. Legal note

**NON-BLOCKING LEGAL NOTE**

Cookie Policy factually complete / operator-ready (P18H). Final external legal sign-off remains operator choice — **not** a technical launch blocker.

---

## 25. Final crawl verdict

**CLEAN** (0 CRITICAL, 1 MAJOR non-blocking, 110 MINOR editorial/SEO notes)

---

## 26. Baseline

**Path:** `REPORTS/BASELINE-FP-0002-PRODUCTION-FINAL.md`  
**Crawl timestamp:** 2026-08-19T18:48:29Z (UTC)

---

## 27. Source / production parity

**FINAL SOURCE / PRODUCTION PARITY PASS**

Deployed theme/plugin files SHA-match source after P18I deploy.

Evidence: `parity-source-production.json`

---

## 28. Git

Clean worktree `fp-0002-p18i` on `origin/mars/canonical-post-recovery`. Commit + push in this wave. Dirty main untouched.

---

## 29. Maintenance transition

**FP-0002 ENTERS NORMAL PRODUCTION MAINTENANCE STATE**

See `REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md` and `REPORTS/FP-0002-FINAL-LAUNCH-CLOSEOUT-v1.md`.

---

## 30. Remaining items

1. Operator: GSC + Yandex sitemap submission (auth blocked for agent)
2. Operator: optional legal sign-off Cookie Policy
3. Operator: optional `lead_retention_days=730`
4. Ongoing monitoring / content / SEO development

---

## 31. Acceptance

**FP-0002 P18I COMPLETE** — final crawl against the **current live site** after Olya's editorial work; human-approved indexing remains **OPEN** under P18G; production sitemap valid; search-console submission documented (auth blocker); no unresolved launch-critical defects; bounded staging-URL fix deployed; dashboard and baseline updated; parity pass; canonical git updated; project in **PRODUCTION / MAINTENANCE**.
