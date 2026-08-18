# Forge WordPress — Module Catalog v1

**ID:** FW-R-04  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**How to choose CPT vs repeater vs Options before registering modules:** [CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md). This catalog lists **modules**, not the modeling sequence.

Maturity: THEORY | IMPLEMENTED ONCE | PRODUCTION PROVEN | PRODUCTION PROVEN WITH CAVEATS | NEEDS SECOND PROJECT VALIDATION | CANONICAL DEFAULT

Source (reference, not a shared package yet):  
`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/plugins/shpigovsky-core/`  
Theme consumers: `.../WORDPRESS/theme/shpigovsky/`

Extraction status: [backlog](../knowledge/FORGE-WORDPRESS-MODULE-EXTRACTION-BACKLOG-v1.md).

---

## CORE (new sites should plan these on day 1)

| Module | Purpose | Deps | Admin | FE owner | Storage | API | Security | QA | Production | Maturity |
|--------|---------|------|-------|----------|---------|-----|----------|----|------------|----------|
| Site Settings | Globals SoT | ACF options | Options sections | theme helpers | options | — | caps | editor walkthrough | one SoT | **CANONICAL DEFAULT** (shape); implementation **PROVEN WITH CAVEATS** |
| Production Dashboard | Ops widget | — | Dashboard | — | options meta | — | no secrets | Admin only | not notices | **CANONICAL DEFAULT** |
| SEO Meta | Title/desc | ACF | entity + settings | `wp_head` | postmeta/options | — | esc_* | view-source | one owner | **CANONICAL DEFAULT** |
| Sitemap | Native extend | WP core | settings links | wp-sitemap | — | — | public types only | GET xml | ≠ indexing | **CANONICAL DEFAULT** |
| Native CPT permalink | Core slug UX | CPT public | core box | permalinks | `post_name` | — | uniqueness | save tests | AP-002 | **CANONICAL DEFAULT** |
| i18n | gettext | — | translated chrome | translated FE | po/mo | — | — | locale switch | from day 1 | **CANONICAL DEFAULT** |
| Typography | Render-time | — | none (or debug off) | filters | none | — | HTML-safe | NBSP/search | one owner | **PRODUCTION PROVEN WITH CAVEATS** |
| Standard navigation | WP menus | core | Menus | walker | nav_menu | — | — | keyboard | — | **CANONICAL DEFAULT** |

---

## OPTIONAL (requirements-driven)

| Module | Purpose | Maturity | Reuse class |
|--------|---------|----------|-------------|
| Smart Search | REST grouped suggest | PRODUCTION PROVEN WITH CAVEATS | B — extract later |
| Specialists / people CPT | Staff singles + hub | PRODUCTION PROVEN WITH CAVEATS | B — pattern A; fields I |
| Reviews | Social proof | NEEDS SECOND PROJECT VALIDATION | J — FP-0002 used options repeater |
| Social / Messengers | Type registry | PRODUCTION PROVEN WITH CAVEATS | B |
| Activity Log | Dedicated table | PRODUCTION PROVEN WITH CAVEATS | B |
| DOCX Publisher | Draft import | PRODUCTION PROVEN WITH CAVEATS | B |
| Reading Time | Auto WPM + override | PRODUCTION PROVEN | B |
| Auto TOC | H2 IDs + list | PRODUCTION PROVEN | B |
| Consultation Forms | AJAX lead + persist-before-mail | PRODUCTION PROVEN WITH CAVEATS (SMTP verification still a later gate) | B |
| SMTP Admin / PHPMailer owner | One Admin config + `phpmailer_init` | PRODUCTION PROVEN WITH CAVEATS | B |
| Form lead registry | Dedicated table + Заявки Admin | PRODUCTION PROVEN WITH CAVEATS | B |
| Decorative parallax | Brand motion | EXPERIMENTAL / PROJECT-SPECIFIC | I/J + **H** QA |
| Advanced analytics | GTM/Metrica/etc. | PRODUCTION PROVEN WITH CAVEATS | B — empty-safe fields |

---

## PROJECT-SPECIFIC (do not reuse as defaults)

| Item | Why |
|------|-----|
| Clinical service tree, layout roles «Раздел/Услуга/Заглушка» | Medical IA (I) |
| Lifebuoy asset | Brand (I) |
| Exact rewrite slugs | Client URLs (I) |
| Service duplicate / layout governance | Proven locally; **J** before CORE |

---

## Specs

- [Smart Search](../standards/FORGE-WORDPRESS-SMART-SEARCH-MODULE-SPEC-v1.md)
- [Activity Log](../standards/FORGE-WORDPRESS-ACTIVITY-LOG-MODULE-SPEC-v1.md)
- [DOCX](../standards/FORGE-WORDPRESS-DOCX-IMPORTER-MODULE-SPEC-v1.md)
- [Social](../standards/FORGE-WORDPRESS-SOCIAL-CONTACT-MODULE-SPEC-v1.md)

---

*Catalog v1.*
