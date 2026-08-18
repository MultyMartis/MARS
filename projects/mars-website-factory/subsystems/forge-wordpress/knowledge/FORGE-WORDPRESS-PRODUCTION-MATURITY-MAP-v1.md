# Forge WordPress — Production maturity map v1

**Date:** 2026-08-18  
**Rule:** One production case does **not** make a system universal.

| System | Maturity |
|--------|----------|
| i18n from day 1 | CANONICAL DEFAULT |
| Site Settings SoT | CANONICAL DEFAULT (shape); implementation PROVEN WITH CAVEATS |
| Native permalink UX | CANONICAL DEFAULT |
| Native sitemap extension | CANONICAL DEFAULT |
| SEO meta one owner | CANONICAL DEFAULT |
| Dashboard ops widget | CANONICAL DEFAULT |
| Exact-file deploy + drift intake | CANONICAL DEFAULT (ops) |
| Indexing after SMTP | CANONICAL DEFAULT (ops) |
| Webroot hygiene | CANONICAL DEFAULT (ops) |
| Physical-device QA for device-specific bugs | CANONICAL DEFAULT (QA) |
| Render-time typography | PRODUCTION PROVEN WITH CAVEATS |
| Standard WP navigation L2/mobile | PRODUCTION PROVEN WITH CAVEATS |
| Slider input matrix | PRODUCTION PROVEN WITH CAVEATS |
| Smart Search | PRODUCTION PROVEN WITH CAVEATS / NEEDS SECOND PROJECT |
| Activity Log | PRODUCTION PROVEN WITH CAVEATS / NEEDS SECOND PROJECT |
| DOCX importer | PRODUCTION PROVEN WITH CAVEATS / NEEDS SECOND PROJECT |
| Social type registry | PRODUCTION PROVEN WITH CAVEATS |
| Consultation AJAX forms | PRODUCTION PROVEN WITH CAVEATS (SMTP still a later gate on the reference case) |
| People/staff CPT | PRODUCTION PROVEN WITH CAVEATS (pattern); fields PROJECT-SPECIFIC |
| Reviews-as-options | NEEDS SECOND PROJECT VALIDATION |
| Decorative parallax | EXPERIMENTAL / PROJECT-SPECIFIC |
| Extracted shared `wp-forge-core` plugin | THEORY / BACKLOG — [EXTRACTION-ROADMAP](FORGE-WORDPRESS-REUSABLE-CODE-EXTRACTION-ROADMAP-v1.md); not extracted this wave |
| AG-WP-001 autonomous implementation | NOT PRODUCTION READY |
| Theme vs plugin vs MU survival test | CANONICAL DEFAULT (documented); implementation PROVEN ONCE |
| Design-system token architecture | CANONICAL DEFAULT (architecture); values PROJECT-SPECIFIC |
| CSS/JS one-owner | CANONICAL DEFAULT |
| Accessibility baseline (not WCAG cert) | CANONICAL DEFAULT |
| Media attachment-ID architecture | CANONICAL DEFAULT |
| Plugin one-owner collisions | CANONICAL DEFAULT |
| Client editor post-launch workflows | CANONICAL DEFAULT (custom roles = J) |
| Second-site bootstrap shell | CANONICAL DEFAULT (docs); code skeleton = SECOND-SITE VALIDATION when first copied |
| Experience harvest loop | CANONICAL DEFAULT (process) |

**Do not collapse:** DOCUMENTED STANDARD · IMPLEMENTED ON FP-0002 · PRODUCTION PROVEN ONCE · PRODUCTION PROVEN MULTIPLE TIMES · EXTRACTED REUSABLE MODULE · WP FORGE DEFAULT.

---

*Maturity map v1.1.*
