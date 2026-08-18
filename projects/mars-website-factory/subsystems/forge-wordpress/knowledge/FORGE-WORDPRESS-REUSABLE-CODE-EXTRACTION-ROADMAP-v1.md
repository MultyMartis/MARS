# Forge WordPress — Reusable code extraction roadmap v1

**Date:** 2026-08-18  
**This wave:** knowledge only — **no** large FP-0002 code extraction.

**Supersedes as operating list:** [MODULE-EXTRACTION-BACKLOG](FORGE-WORDPRESS-MODULE-EXTRACTION-BACKLOG-v1.md) (kept as historical short table).

| Class | Meaning |
|-------|---------|
| **R1** | READY TO EXTRACT NOW (small, generic, parameterization obvious) — still **do not extract in this wave** |
| **R2** | EXTRACT AFTER SECOND-SITE VALIDATION |
| **R3** | CONCEPT ONLY |
| **R4** | DO NOT EXTRACT (project-specific) |

---

## Candidates (FP-0002)

| Candidate | Class | Notes |
|-----------|-------|-------|
| i18n bootstrap (text domain, POT path) | **R1** | Pattern + checklist; not a Composer package yet |
| Native sitemap helpers | **R1** | Tiny `wp_sitemaps_*` filters |
| TOC H2 + reading time | **R1** | Small theme/plugin functions; drop brand |
| Site Settings IA + helpers | **R2** | Keys must be generic; second site proves shape |
| Dashboard widget | **R2** | Fields via project meta |
| SEO meta + empty-safe integrations | **R2** | Collision with Yoast is a WAD |
| Typography pipeline | **R2** | Locale packs as config |
| Navigation helpers (L2/mobile) | **R2** | Walker + CSS contract |
| Smart Search | **R2** | Namespaces, CSS, REST |
| Activity Log | **R2** | Table name prefix |
| Social registry | **R2** | |
| Forms (consultation-like) | **R2** | Recipient from options only |
| DOCX importer | **R2** | Template file; draft-only |
| Module registry pattern | **R3** | Interface is a concept; implementation may stay per project |
| Native CPT permalink uniqueness data-layer | **R2** | UI-less |
| Slider attach helper | **R2** | |
| Specialist/service CPTs | **R4** fields / **R2** registration pattern only |
| Service layout governance / duplicate | **R4** / J |
| Lifebuoy parallax | **R4** |
| Reviews options repeater | **R3** / J |
| Clinical IA, brand CSS, exact slugs | **R4** |

**Do not** copy `FUTURE_RECIPIENT`, phones, or client emails into a shared package.

---

## `wp-forge-core` candidate (not production)

**AG-WP-001 remains NOT PRODUCTION READY** unless independent evidence changes that.

| Topic | Position |
|-------|----------|
| Candidate responsibilities | i18n loader, settings API helpers, SEO empty-safe output, sitemap filters, dashboard widget API, module enablement |
| Extension points | filters/actions; project plugin remains the composer of CPTs |
| Must remain project-owned | templates, brand tokens, CPT fields, redirects, clinical/content |
| Versioning | real plugin header; no fake versions |
| Migration path | copy-paste → must-use library → plugin **only after R2 evidence** |
| Maturity gate | second production site using extracted modules without fork-and-forget; tests; WAD |

Current state: **THEORY / BACKLOG**. Do not declare a shipped core.

---

*Roadmap v1.*
