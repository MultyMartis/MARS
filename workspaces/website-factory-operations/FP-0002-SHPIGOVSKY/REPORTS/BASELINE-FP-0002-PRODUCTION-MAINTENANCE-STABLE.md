# BASELINE — FP-0002 Production Maintenance Stable

**Baseline ID:** `FP-0002-PRODUCTION-MAINTENANCE-STABLE-2026-08-24`  
**Established:** 2026-08-24  
**Supersedes for “current ops truth”:** post-anti-spam maintenance closeout (does **not** rewrite historical P18I baseline text)  
**Domain:** https://shpigovsky.ru/  
**Core version:** `0.3.25-olya-robots`

---

## Phase

| Item | Value |
|------|--------|
| Project | FP-0002 / Шпиговский |
| Phase | **PRODUCTION / MAINTENANCE — STABLE** |
| Launch tails | **NONE** (technical) |

---

## Runtime (read-only verified 2026-08-24)

| Item | Value |
|------|--------|
| Public HTTP | **200** |
| `home` / `siteurl` | `https://shpigovsky.ru` |
| Theme | Shpigovsky |
| Core plugin | `0.3.25-olya-robots` (current production status) |
| WPilot | installed; `write_enabled=false` |

---

## Indexability

| Item | Value |
|------|--------|
| Indexing | **OPEN — HUMAN-APPROVED** |
| `blog_public` | `1` |
| Discourage search engines | `false` |
| P18G guard | **ACTIVE** (deployed; not mutated this wave) |
| Watchdog | **ACTIVE** (deployed; not mutated this wave) |
| robots.txt | Olya-approved permissive policy + Sitemap |
| Sitemap | `https://shpigovsky.ru/wp-sitemap.xml` (HTTP 200) |

---

## Forms / mail / privacy / anti-spam

| Item | Value |
|------|--------|
| Forms | **ACTIVE** (public markup: honeypot + `fp02_fs`) |
| SMTP | **VERIFIED / ACTIVE** (unchanged this wave) |
| Native anti-spam | **ACTIVE** |
| External CAPTCHA | **NONE** |
| Privacy / consent | **ACTIVE** |
| Metrika | **CONSENT-GATED** |
| Russian form mail UX | **ACTIVE** |

---

## Git recovery

| Item | Value |
|------|--------|
| Canonical branch | `mars/canonical-post-recovery` |
| Authority | `origin/mars/canonical-post-recovery` |
| Pre-stabilization remote tip | `e0d297e6f95dfaca42c2b9ba6dde800178d4ca6b` |
| Anti-spam checkpoint (ancestor) | `0875b9d5c81f77b5a5f63ada7e6799eaf88c5cd2` |
| Stabilization recovery point | `0fbd25bdbd8ba3f77d6c0ab1e4881c9d159a35c3` |
| Stabilization commit | see `REPORT-FP-0002-PROD-MAINT-WORKSPACE-STABILIZATION.md` |
| Olya robots closeout commit (ancestor) | `76a23e3ae9976cb590e4493f6f25308cd981b101` |

---

## Non-blocking remaining

Operator GSC / Yandex sitemap submission; optional Cookie Policy legal sign-off; optional `lead_retention_days=730`; optional anti-spam tuning from real spam evidence; normal SEO/content/feature maintenance.

---

## References

- Stabilization report: `REPORT-FP-0002-PROD-MAINT-WORKSPACE-STABILIZATION.md`
- Historical launch baseline: `BASELINE-FP-0002-PRODUCTION-FINAL.md`
- Open items: `OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md`
