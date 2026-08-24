# ISEO-SU TECH SEO HIGH FIX STATUS v1

**Created:** 2026-08-24  
**Wave:** ISEO-SU-SITE-OPS-HIGH-FIX-WAVE-01  
**Evidence:** `ISEO-SU-HIGH-FIX-WAVE-01-EVIDENCE-v1.md`  
**Note:** Original audit CSV rows preserved; this file is the live post-fix status register for the two HIGH items.

| finding_id | severity | status | closed_by | notes |
|------------|----------|--------|-----------|-------|
| SM-CHILD-404 | HIGH | **CLOSED** | HIGH-FIX-WAVE-01 | Root `/sitemap.xml` now indexes only `sitemap-static.xml` + `wp-sitemap.xml` |
| IMG-BROKEN | HIGH | **CLOSED** | HIGH-FIX-WAVE-01 | Theme relative `img/` paths normalized to `/img/`; targeted recrawl PASS |

Remaining audit backlog (MEDIUM / LOW / REVIEW) stays open and is **out of scope** for this wave.
