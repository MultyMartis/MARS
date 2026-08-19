# OPEN ITEMS — FP-0002 Production Maintenance

**Phase:** PRODUCTION / MAINTENANCE (post-P18I)  
**Updated:** 2026-08-20

Launch implementation tasks are **closed**. Only maintenance and operator follow-ups remain.

---

## Operator follow-ups (non-blocking)

| # | Item | Owner | Priority |
|---|------|-------|----------|
| 1 | Submit sitemap to **Google Search Console** (`https://shpigovsky.ru/wp-sitemap.xml`) | Operator | Medium |
| 2 | Submit sitemap to **Yandex Webmaster** | Operator | Medium |
| 3 | Final **legal sign-off** on Cookie Policy (factually current) | Operator / Legal | Low |
| 4 | Set `lead_retention_days=730` if accepted; align Privacy Policy wording | Operator | Low |
| 5 | Ongoing content, SEO, and feature work via Admin (normal production) | Editor / Operator | As needed |

---

## Closed (do not reopen as launch blockers)

- Indexing approval — **OPEN — human-approved**; P18G guard active
- SMTP verification — **done** (P18D-FU01)
- Privacy / cookie runtime — **done** (P18E)
- Pre-cutover / cutover / launch crawl — **done** (P18I)
- Sitemap technical validity — **done**

---

## Operational rules (maintenance)

1. **Editorial truth** = current production DB (Olya/Admin edits).
2. Technical waves start with **fresh intake** — do not restore old launch baselines over live content.
3. **Indexing is human-owned** — agents must not close without explicit command.
4. P18G guard remains active.
5. New features → new bounded waves with their own reports.

---

## References

- Final baseline: `REPORTS/BASELINE-FP-0002-PRODUCTION-FINAL.md`
- Closeout report: `REPORTS/REPORT-FP-0002-PROD-P18I-FINAL-LAUNCH-CLOSEOUT.md`
- Closeout charter summary: `REPORTS/FP-0002-FINAL-LAUNCH-CLOSEOUT-v1.md`
