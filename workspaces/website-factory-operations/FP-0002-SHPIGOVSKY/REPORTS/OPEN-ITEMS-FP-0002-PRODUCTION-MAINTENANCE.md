# OPEN ITEMS — FP-0002 Production Maintenance

**Phase:** PRODUCTION / MAINTENANCE (post native anti-spam v1)  
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
| 6 | Optional: tune anti-spam thresholds from real spam evidence (keep false-positive risk low) | Operator / Tech | Low |

---

## Closed (do not reopen as launch blockers)

- Indexing approval — **OPEN — human-approved**; P18G guard active; P18J synthetic QA separated from production incident stream
- SMTP verification — **done** (P18D-FU01)
- Privacy / cookie runtime — **done** (P18E)
- Pre-cutover / cutover / launch crawl — **done** (P18I)
- Sitemap technical validity — **done**
- Native form anti-spam v1 — **done** (honeypot + signed timing + rate + replay + heuristics; no external CAPTCHA)

---

## Operational rules (maintenance)

1. **Editorial truth** = current production DB (Olya/Admin edits).
2. Technical waves start with **fresh intake** — do not restore old launch baselines over live content.
3. **Indexing is human-owned** — agents must not close without explicit command.
4. P18G guard remains active; synthetic guard QA must use authorized QA context only (P18J).
5. New features → new bounded waves with their own reports.
6. Form spam controls stay **first-party** unless a new charter authorizes an external CAPTCHA provider.

---

## References

- Native anti-spam v1: `REPORTS/REPORT-FP-0002-PROD-MAINT-NATIVE-ANTISPAM-V1.md`
- Forms anti-spam runbook: `DOCS/OPERATIONS-FORMS-ANTISPAM-v1.md`
- P18J report: `REPORTS/REPORT-FP-0002-PROD-P18J-INDEXING-QA-NOISE-CLEANUP.md`
- Final baseline: `REPORTS/BASELINE-FP-0002-PRODUCTION-FINAL.md`
- Closeout report: `REPORTS/REPORT-FP-0002-PROD-P18I-FINAL-LAUNCH-CLOSEOUT.md`
- Closeout charter summary: `REPORTS/FP-0002-FINAL-LAUNCH-CLOSEOUT-v1.md`
