# RUNBOOK — FP-0002 PROD-P18 (MAINTENANCE STATE)

**Wave executed:** **P18I** — final launch closeout (2026-08-20)  
**Prior:** **P18H** privacy · **P18G** indexing safety · **P18E** cookie/consent · **P18D-FU01** SMTP closeout  
**Phase:** **PRODUCTION / MAINTENANCE** — launch implementation **closed**.

**Indexing is OPEN — human-approved (Olya/admin); do not close without explicit human command.**

---

## Current facts (P18I final baseline)

| Surface | Value |
|---------|--------|
| WordPress `home` / `siteurl` | `https://shpigovsky.ru` |
| Core | `0.3.21-p18i` |
| Baseline ID | `FP-0002-PRODUCTION-FINAL-2026-08-20-P18I` |
| SMTP | **VERIFIED / ACTIVE** |
| Forms / leads | **ACTIVE** |
| Cookie consent / Metrika | **ACTIVE / CONSENT-GATED** |
| Indexing | **OPEN** — **HUMAN-APPROVED**; P18G guard **ACTIVE** |
| Sitemap | `https://shpigovsky.ru/wp-sitemap.xml` (valid) |
| Final crawl | **CLEAN** (2026-08-19 UTC) |

**Do not revert** `home`/`siteurl` to `shpigovsky.beget.tech`.  
**Do not** run legacy launch scripts that close indexing.

---

## Maintenance operations

1. **Editor changes** via WordPress Admin are normal production truth.
2. **Technical waves** start with fresh production intake — never overwrite live editorial content from old baselines.
3. **Indexing** remains human-owned; P18G guard stays active.
4. **Backups** at meaningful milestones or before risky changes.
5. **New features** → new bounded waves with separate reports.

---

## Operator follow-ups (non-blocking)

1. Submit sitemap in **Google Search Console** and **Yandex Webmaster** (agent auth blocker in P18I).
2. Optional: Cookie Policy legal sign-off.
3. Optional: `lead_retention_days=730` + Privacy Policy alignment.

See `REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md`.

---

## Forbidden in maintenance (unless explicit new charter)

- Closing indexing without human command
- Global `Disallow: /` or mass noindex
- Restoring pre-cutover launch defaults over live DB
- Broad DB purge / migration without backup + charter

---

*Historical cutover steps remain in git history and P17–P18A reports; do not re-execute.*
