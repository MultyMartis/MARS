# REPORT — ISEO-SU-SITE-OPS-RECIPIENT-REMOVE-AND-TECH-SEO-AUDIT-01

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-RECIPIENT-REMOVE-AND-TECH-SEO-AUDIT-01  
**Date:** 2026-08-21  
**Final status:** COMPLETE — OPERATOR FORM RECIPIENT REMOVED / ISEO-SU TECH-SEO AUDIT COMPLETE / FIX PLAN READY

---

## 1. Execution Summary

Removed operator mailbox `im.work@mail.ru` from production `production_recipients`, kept original `nikel007i33@yandex.ru`, left `test_mode` OFF, aligned MARS canonical source, sent **0** mail, then completed a conservative read-only tech/SEO crawl of `https://i-seo.su/` (1033 URLs) with SEO-facing + internal evidence artefacts. **No audit remediations applied.**

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `AI WS` (X:) |
| Branch | `mars/canonical-post-recovery` |
| HEAD at start | `5ab46f5e…` (ahead of origin; foreign unpushed history present) |
| Origin tip (task note) | `507bf19c…` verified as remote tip at start |
| Staged | empty |
| Foreign WIP | preserved (not staged) |

## 3. Recipient State Before

Production `iseo-form-config.php` SHA `dea5b3482feb914f…`:

- `test_mode`: false  
- recipients: `nikel007i33@yandex.ru`, `im.work@mail.ru`  
- typo `im.work@nail.ru`: absent  
- 12/12 handlers on shared send; no hardcoded operator To  

## 4. Recipient Mutation

| Step | Detail |
|------|--------|
| Backup | `local/sites/iseo-su-production/_recipient-remove-01/backups/remove-20260821T055420Z/` |
| Source first | `production-source/forms/iseo-form-config.php` |
| Upload | SFTP put exact source |
| After SHA | `1aa4d09b091e1c3e…` ≡ source |
| Security surface | unchanged |

## 5. Recipient State After

- FINAL FORM RECIPIENTS: `nikel007i33@yandex.ru` only  
- `im.work@mail.ru` ACTIVE: **NO**  
- `im.work@nail.ru` ACTIVE: **NO**  
- TEST MODE: **OFF**  
- `test_recipients` still lists operator for future controlled tests only (unused)

## 6. Production / Source Alignment

**YES** — production SHA ≡ `production-source/forms/iseo-form-config.php`.

## 7. Crawl Scope

Full public discovery via seeds + both sitemap indexes + internal links (static, services, cases, blog, WP, glossary, offers, tariff-calc, linked sibling routes).

## 8. Crawl Method

Python GET/HEAD crawler @ ~1.4 rps, concurrency 2, ~998 s, UA `MARS-ISEO-TechSEO-Audit/1.0`. No POST/forms.

## 9. URL Counts

| Metric | Count |
|--------|------:|
| TOTAL URLS CRAWLED | 1033 |
| INDEXABLE URLS | 643 |
| 4XX | 0 |
| 5XX | 0 |
| REDIRECTS | 136 |
| BROKEN INTERNAL LINKS | 0 |

## 10. Technical Findings Summary

**CONFIRMED HIGH (2):** Yoast child sitemaps 404; blog relative image 404s (96 sampled).  
HTTP document health strong. Mobile/Playwright lab **LIMITED**.

## 11. SEO Findings Summary

Duplicate titles/metas, canonical gaps, sitemap/indexability mismatches, crawler orphans — predominantly **REVIEW NEEDED** for SEO judgment; not auto-assigned as SEO implementation work.

## 12. Confirmed Issues

1. `SM-CHILD-404` — `post|page|category-sitemap.xml` = 404 via `/sitemap.xml`  
2. `IMG-BROKEN` — relative `img/` under `/blog/YYYY/` and `/blog/author/`  

## 13. Expected Behavior

Dual sitemap architecture; `/offer/*` robots disallow; glossary ownership via wp-sitemap.

## 14. Review Needed

Canonical strategy, title dedupe for blog archives, meta gaps, orphans, OG, alt-text policy.

## 15. SEO-Team Report

`reports/ISEO-SU-TECH-SEO-AUDIT-FOR-SEO-TEAM-v1.md` — Russian, no secrets, visibility-only framing.

## 16. Raw Evidence

- `ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md`  
- `audits/tech-seo/ISEO-SU-TECH-SEO-FINDINGS-v1.csv`  
- `audits/tech-seo/ISEO-SU-TECH-SEO-URL-INVENTORY-v1.csv`  
- Storage raw: `X:\AI MARS STORAGE\iseo-su-site-ops\tech-seo-audit-01\`  
- Recipient evidence: `ISEO-SU-FORM-OPERATOR-RECIPIENT-REMOVAL-EVIDENCE-v1.md`

## 17. Production Mutations

**Only** `iseo-form-config.php` recipient list (operator removed). No anti-spam/security/template/JS/CSS/DB changes. Audit: **zero** mutations.

## 18. Files Created or Updated

**Created:** operator removal evidence; tech SEO evidence; findings/inventory CSV; SEO team report; this REPORT.  
**Updated:** `production-source/forms/iseo-form-config.php`; current-state / baseline / OPERATIONAL-INDEX / artifact register.

## 19. Git Persistence

Local commit f1e0ce31 on diverged dirty main; remote sync commit 3befa11c on origin/mars/canonical-post-recovery (cherry-pick FF). No force push. No foreign WIP staged.

## 20. Open Blockers

None for this charter. Mobile lab incomplete (environment). Post-crawl TLS timeouts noted — no outage declared.

## 21. Recommended Next Fix Wave

1. Repair `/sitemap.xml` children or stop advertising 404 sitemaps  
2. Fix blog relative image paths to root-absolute `/img/`  
3. Prioritize REVIEW backlog with SEO (canonicals/titles) in separate tasks  

## 22. Stop Condition

Met: recipient removal + alignment + read-only audit + validated findings + SEO report + evidence + scoped git persistence. **Audit fixes not implemented.**

---

## FINAL HARD CHECK

```
FINAL FORM RECIPIENTS: nikel007i33@yandex.ru only
im.work@mail.ru ACTIVE: NO
im.work@nail.ru ACTIVE: NO
TEST MODE: OFF
MAIL SENT DURING TASK: 0
FORM SECURITY CHANGED: NO
PRODUCTION/SOURCE RECIPIENTS ALIGNED: YES

TOTAL URLS CRAWLED: 1033
INDEXABLE URLS: 643
CRITICAL FINDINGS: 0
HIGH FINDINGS: 2
MEDIUM FINDINGS: 6
LOW FINDINGS: 8
REVIEW FINDINGS: 14

4XX: 0
5XX: 0
BROKEN INTERNAL LINKS: 0
REDIRECT CHAINS (>=2): 0
CANONICAL ISSUES: 279 (mostly REVIEW)
INDEXABILITY ISSUES: 54
SITEMAP ISSUES: child 404 x3 + dual-arch INFO
TITLE ISSUES: 0 missing; duplicates REVIEW
META DESCRIPTION ISSUES: 23 missing REVIEW
H1 ISSUES: 5 (tool/hub REVIEW)
IMAGE ISSUES: 96 broken confirmed (HIGH)
STRUCTURED DATA ISSUES: 0 syntax
MOBILE TECH ISSUES: LIMITED

SEO TEAM REPORT CREATED: YES
AUDIT FIXES APPLIED: NO
OPEN BLOCKERS: none for charter
REMOTE SYNC: YES — origin tip 3befa11c via clean worktree cherry-pick (no force)
```
