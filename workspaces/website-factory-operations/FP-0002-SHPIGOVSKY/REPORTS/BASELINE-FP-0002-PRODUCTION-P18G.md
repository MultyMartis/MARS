# BASELINE — FP-0002 Production (P18G)

**Date:** 2026-08-20  
**Wave:** PROD-P18G Indexing Safety Guard  
**Core:** `0.3.17-p18g`

---

## Indexability (human-owned)

| Signal | Value |
|--------|-------|
| Human decision | **OPEN** (Olya / admin) |
| `blog_public` | **1** |
| Effective state | **OPEN** |
| Physical `robots.txt` | Present; **no global `Disallow: /`** (host-managed multi-agent rules) |
| Global meta robots | No sitewide `noindex` |
| X-Robots-Tag | None on sampled public pages |

---

## Safety systems (P18G)

| System | Status |
|--------|--------|
| `IndexingControl::request_state()` guard | ACTIVE — non-human close blocked |
| `pre_update_option_blog_public` guard | ACTIVE |
| `IndexingState` multi-surface model | ACTIVE |
| `IndexingAlerts` → WP administrators | ACTIVE (4 recipients) |
| `IndexingWatchdog` hourly | ACTIVE — alert only |

---

## Unchanged / preserved

- P18E cookie consent, Metrika consent-gating, form goal gating
- Olya editorial DB content
- SMTP VERIFIED / ACTIVE
- Form recipients (not used for indexing alerts)

---

## Source ↔ production

**8/8** plugin files MATCH (see `REPORTS/evidence/prod-p18g-indexing-safety/02-deploy-manifest.json`).

---

*Supersedes indexing sections of `BASELINE-FP-0002-PRODUCTION-P18D-FU01.md` for indexability truth only.*
