# FP-0002 → WP Forge knowledge assimilation index

**Date:** 2026-08-18  
**Source case:** FP-0002 Shpigovsky production (P07–P17-FU02 plus earlier foundation where architecture changed)  
**Purpose:** Map each reusable lesson to a canonical WP Forge document. Agents should follow the **canonical** column, not the report archive.

**Project reports remain evidence.** They are not the operating brain.

---

## How to use

1. Identify the work type (new site / Admin / deploy / cutover / QA / security).
2. Open the canonical document in the table.
3. Open FP-0002 reports only when you need evidence, hashes, or a failure narrative.

---

## Lesson → canonical document

| FP-0002 lesson | Class | Canonical WP Forge document |
|----------------|-------|-----------------------------|
| Child Pages used for staff-like entities; later CPT `specialist` | A / G | [CONTENT-MODEL-CPT-STANDARD](../standards/FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) · [CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) |
| Preserve IDs/URLs when changing post type; hub page + CPT singles | A / D | same + [ENVIRONMENT-MIGRATION](../runbooks/FORGE-WORDPRESS-ENVIRONMENT-MIGRATION-STANDARD-v1.md) |
| Duplicate custom permalink UI vs native WP slug row | G | [ANTI-PATTERN-REGISTRY](../standards/FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md) AP-002 · CPT standard |
| Site Settings as one SoT for header/footer/mobile/contacts | A / E | [SITE-SETTINGS-STANDARD](../standards/FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md) · [GLOBAL-SETTINGS-OWNERSHIP](../standards/FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md) |
| Social: type + URL + visibility; registry icons; empty → no render | B / E / F | [SOCIAL-CONTACT-MODULE-SPEC](../standards/FORGE-WORDPRESS-SOCIAL-CONTACT-MODULE-SPEC-v1.md) |
| SEO meta, verification, analytics, advanced code; sitemap ≠ indexing | A / C | [SEO-AND-SITEMAP-STANDARD](../standards/FORGE-WORDPRESS-SEO-AND-SITEMAP-STANDARD-v1.md) |
| Extend native `wp-sitemap`; do not invent a Yandex page feed | A / G | same |
| Smart Search: one REST, groups, desktop+mobile, AbortController | B / F | [SMART-SEARCH-MODULE-SPEC](../standards/FORGE-WORDPRESS-SMART-SEARCH-MODULE-SPEC-v1.md) |
| Forms: nonce, anti-spam, AJAX, no `mail()`; persist lead before SMTP; Admin SMTP owner | A / C / D | [FORMS-AND-SMTP-STANDARD](../standards/FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) |
| DOCX → draft articles, images, no auto-publish | B | [DOCX-IMPORTER-MODULE-SPEC](../standards/FORGE-WORDPRESS-DOCX-IMPORTER-MODULE-SPEC-v1.md) |
| Article TOC from H2 only; reading time | A / B / F | [ARTICLE-SYSTEM notes in BLUEPRINT](../standards/FORGE-WORDPRESS-PRODUCTION-WEBSITE-BLUEPRINT-v1.md) §P8 |
| Broad DB typography rewrite vs render-time pipeline | G → A | [TYPOGRAPHY-PIPELINE-STANDARD](../standards/FORGE-WORDPRESS-TYPOGRAPHY-PIPELINE-STANDARD-v1.md) |
| Native WP menus; L2 dropdown + mobile accordion; parent navigable | A / F | [NAVIGATION-STANDARD](../standards/FORGE-WORDPRESS-NAVIGATION-STANDARD-v1.md) |
| Sliders: mouse/touch/trackpad; Hero exceptions; forceToAxis | A / F / H | [SLIDER-CAROUSEL-STANDARD](../standards/FORGE-WORDPRESS-SLIDER-CAROUSEL-STANDARD-v1.md) |
| iOS lifebuoy: emulation ≠ physical Safari; bounded fallback | G / H | [REAL-DEVICE-QA-STANDARD](../standards/FORGE-WORDPRESS-REAL-DEVICE-QA-STANDARD-v1.md) |
| Activity log dedicated table; no full content / secrets | B / E | [ACTIVITY-LOG-MODULE-SPEC](../standards/FORGE-WORDPRESS-ACTIVITY-LOG-MODULE-SPEC-v1.md) |
| Dashboard widget planned (no global notices) | A / E | [ADMIN-UX-STANDARD](../standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) §10.3 · [DEFINITION-OF-DONE](../standards/FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md) |
| Operator status UI must be updated in the same major production wave | C / E / G | same · AP-021 |
| Admin feature not done until discoverable in normal left-menu IA | E / G | [ADMIN-UX-STANDARD](../standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) §10.7 · [DoD](../standards/FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md) · AP-029 |
| Search indexing is explicit human approval; one SET SITE INDEXABILITY owner | D / E / G | [SEARCH-INDEXING-CONTROL](../standards/FORGE-WORDPRESS-SEARCH-INDEXING-CONTROL-STANDARD-v1.md) |
| Default technical SMTP sender `noreply@<domain>` | C | [FORMS-AND-SMTP-STANDARD](../standards/FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) §5 |
| i18n from day 1; no mixed hardcoded Admin strings | A / E | [I18N-STANDARD](../standards/FORGE-WORDPRESS-I18N-STANDARD-v1.md) |
| FS = runtime truth; DB = content truth; Git = code authority | C | [SOURCE-RUNTIME-AUTHORITY](../runbooks/FORGE-WORDPRESS-SOURCE-RUNTIME-AUTHORITY-STANDARD-v1.md) |
| Exact-file deploy + hash parity; no directory mirror | C | [PRODUCTION-DEPLOYMENT-SOP](../runbooks/FORGE-WORDPRESS-PRODUCTION-DEPLOYMENT-SOP-v1.md) |
| Exact-file rollback vs full files+DB backup gates | C | [BACKUP-ROLLBACK-STANDARD](../runbooks/FORGE-WORDPRESS-BACKUP-ROLLBACK-STANDARD-v1.md) |
| Dirty MARS monorepo; clean worktree checkpoint | C | [GIT-SOP](../runbooks/FORGE-WORDPRESS-GIT-SOP-v1.md) |
| `WP_ENVIRONMENT_TYPE=local`, `.test`, debug residue | D / G | [ENVIRONMENT-MIGRATION](../runbooks/FORGE-WORDPRESS-ENVIRONMENT-MIGRATION-STANDARD-v1.md) |
| Public `mars-runtime/` mutating GET | G | [PUBLIC-WEBROOT-HYGIENE-GATE](../standards/FORGE-WORDPRESS-PUBLIC-WEBROOT-HYGIENE-GATE-v1.md) |
| Legacy 301s: exact path, query preserve, no future-host hardcode pre-cutover | D | [REDIRECT-STANDARD](../runbooks/FORGE-WORDPRESS-REDIRECT-STANDARD-v1.md) |
| NS cutover must not move mail; inventory MX/SPF/DKIM first | D / G | [DNS-NS-CUTOVER-STANDARD](../runbooks/FORGE-WORDPRESS-DNS-NS-CUTOVER-STANDARD-v1.md) |
| Freeze → backup → NS → SSL → URLs → smoke → SMTP → indexing | D | [PRE-CUTOVER-AND-LAUNCH-SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) |
| Operator already changed NS/`home`/`siteurl` — intake, do not revert | C / D | [SOURCE-RUNTIME-AUTHORITY](../runbooks/FORGE-WORDPRESS-SOURCE-RUNTIME-AUTHORITY-STANDARD-v1.md) · Launch SOP |
| true_false false must not fall back to default; distinguish preview/autosave | A / G | [ACF-FIELD-MODELING](../standards/FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md) §6.1 · [EDITOR UX](../standards/FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md) §5.1 · AP-020 / AP-CMS-016 |
| Do not open indexing because the domain works | D / G | same § indexing gate |
| WPilot READ; `write_enabled=false`; version ≠ option | C | [WPILOT-PRODUCTION-STANDARD](../runbooks/FORGE-WORDPRESS-WPILOT-PRODUCTION-STANDARD-v1.md) |
| Clinical/brand/content/URLs of Shpigovsky | I | Do not copy — project LOC-ZONE only |
| Reviews as ACF options repeater, not CPT | J / I | [CONTENT-MODEL-CPT](../standards/FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) § when not to CPT · [REPEATER-VS-ENTITY](../standards/FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md) |
| Design/Admin fields modeled during implementation rather than as a CMS pack | G → A | [CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) P1b — do this **before** frontend WP coding |
| Duplicate phones / ACF-first without entity map | G | [CMS-ANTI-PATTERNS](../standards/FORGE-WORDPRESS-CMS-ANTI-PATTERNS-v1.md) AP-CMS-001–015 |
| Featured image as portrait SoT; empty ACF hidden; Local JSON in plugin | A / E | [ACF-FIELD-MODELING](../standards/FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md) · [EDITOR UX](../standards/FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md) |
| Decorative parallax / lifebuoy | J / I | [MODULE-CATALOG](../registries/FORGE-WORDPRESS-MODULE-CATALOG-v1.md) experimental |

---

## Wave evidence (minimum intake)

| Wave | Role in this pack | Report |
|------|-------------------|--------|
| P07 / FU01 | Admin/FE polish; demo/Lorem cleanup; access recovery | `REPORT-FP-0002-PROD-P07-*` |
| P08 | Mobile sliders; first typography (PARTIAL); specialists still Pages | `REPORT-FP-0002-PROD-P08-UI-CONTENT-SYSTEMS.md` |
| P09 / FU01 | Fancybox; Smart Search REST; mobile parity; CSS drift canonize | `REPORT-FP-0002-PROD-P09-*` |
| P10 | Native sitemap; SEO Admin; no Yandex invented feed; indexing closed | `REPORT-FP-0002-PROD-P10-*` |
| P11 | Specialists Page → CPT; URL/ID preservation; search/sitemap migrate | `REPORT-FP-0002-PROD-P11-SPECIALISTS-CPT-MIGRATION.md` |
| P12 | Custom slug UI (later failed); Activity Log; iOS transform repair insufficient | `REPORT-FP-0002-PROD-P12-*` |
| P13 | Dashboard, DOCX, SEO meta, nav L2, socials, TOC, trackpad, iOS FIX02 | `REPORT-FP-0002-PROD-P13-ADMIN-BLOG-SEO-NAV-IOS.md` |
| P13-FU01 | Native permalink owner; custom slug UI removed | `REPORT-FP-0002-PROD-P13-FU01-NATIVE-SLUG-UX.md` |
| P14 | Stabilization baseline; operator drift intake; full backup; Git checkpoint | `REPORT-FP-0002-PROD-P14-STABILIZATION.md` |
| P15 | Production env class; `.test` cleanup; mail suppress kept until SMTP | `REPORT-FP-0002-PROD-P15-ENVIRONMENT-CLEANUP.md` |
| P16 | Render-time typography owner; 0 DB rewrites | `REPORT-FP-0002-PROD-P16-TYPOGRAPHY.md` |
| P17 / CONT1 | Legacy 301s; DNS inventory; mail-zone preservation; NS not switched | `REPORT-FP-0002-PROD-P17-PRE-CUTOVER.md` |
| P17-FU02 | `mars-runtime` incident; webroot hygiene; freeze/NS runbooks; indexing still closed | `REPORT-FP-0002-PROD-P17-FU02-FINAL-PRE-CUTOVER-TAIL.md` |
| P18A | Operator live domain intake; legal DEMO banner owner; indexing still closed | `REPORT-FP-0002-PROD-P18A-LIVE-DOMAIN-LEGAL-STATE.md` |
| P18B | Dashboard reality sync; safe Admin indexing control; indexing remains CLOSED | `REPORT-FP-0002-PROD-P18B-DASHBOARD-INDEXING.md` |
| P18C | SMTP/forms Admin owner; lead persist-before-mail; Metrika goal after backend success; suppression remains ON | `REPORT-FP-0002-PROD-P18C-SMTP-FORMS-FOUNDATION.md` |
| P18C-FU01 | Menu discoverability: Почта и формы visible under ACF Site Settings parent | `REPORT-FP-0002-PROD-P18C-FU01-ADMIN-MENU.md` |
| P18G | Indexing safety guard; human OPEN preserved; non-human close blocked | `REPORT-FP-0002-PROD-P18G-INDEXING-SAFETY.md` |
| P18H | Privacy/retention decisions; browser-only consent; 730d lead retention recommend; launch-tail readiness | `REPORT-FP-0002-PROD-P18H-PRIVACY-RETENTION-DECISIONS.md` |
| PRIVACY-027–030 | Separate law vs product recommendation; no server consent log without necessity; consent lifetime as product policy; disclose sessionStorage attribution | `FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md` · P18H evidence |
| P18C-FU02 | Multi-recipient mail settings Add/Remove UX; SMTP secret preserved | `REPORT-FP-0002-PROD-P18C-FU02-MULTI-RECIPIENTS.md` |

Earlier V9 Admin-parity / ACF SoT / operator-CSS canon work remains valid foundation (Experience Pack Phase 1–2). It is **historical**; production operations above supersede it for launch.

---

## What stayed project-local

| Item | Why not canonical default |
|------|---------------------------|
| Medical service tree, alcohol/program copy | Client content (I) |
| Hub slug `specyalisty` spelling | Client URL contract (I) |
| Lifebuoy decorative asset | Visual brand (I/J) |
| Exact 7 legacy 301 paths | Client IA (I); **method** is reusable |
| Beget + REG.RU hosting pair | Provider-specific (I); **NS vs A-record** rule is reusable |

---

## Discoverability updates in this wave

| Surface | Change |
|---------|--------|
| This hub | New |
| Forge WordPress OPERATIONAL-INDEX | Production-knowledge routing |
| Contracts/standards register | FW-S-09+ and runbooks |
| Website Factory knowledge map | WP Forge production brain |
| Experience Pack INDEX | Points here (brain upgrade done) |

*Assimilation index v1 — 2026-08-18.*
