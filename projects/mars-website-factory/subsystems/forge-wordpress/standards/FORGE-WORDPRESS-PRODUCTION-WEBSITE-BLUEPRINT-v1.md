# Forge WordPress — Production Website Blueprint v1

**ID:** FW-S-09  
**Status:** ACTIVE — PRODUCTION PROVEN WITH CAVEATS (one live case: FP-0002)  
**Date:** 2026-08-18  
**Audience:** WP Forge programmers, operators, MetaBOT, Cursor, Web-GPT

**Honesty:** FP-0002 is **one** production reference. Items marked **J** need a second project before they become unconditional defaults.

This blueprint is the answer to: *we are starting a new WordPress site — what architecture and phases do we use?*

---

## 0. Day-1 foundation (install these concepts before coding)

| Foundation | Class | Notes |
|------------|-------|--------|
| Proper i18n (text domain, gettext, POT, project locale) | A | [I18N-STANDARD](FORGE-WORDPRESS-I18N-STANDARD-v1.md) |
| Content-model registry (Page / Post / CPT / options) | A | [CONTENT-MODEL-CPT](FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) |
| **CMS / editable architecture design (P1b pack)** | A | [CMS-ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) |
| Site Settings SoT | A | [SITE-SETTINGS-STANDARD](FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md) |
| System Dashboard widget (not global notices) | A | [ADMIN-UX](FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) |
| SEO meta owner (one) | A | [SEO-AND-SITEMAP](FORGE-WORDPRESS-SEO-AND-SITEMAP-STANDARD-v1.md) |
| Native sitemap extension | A | same |
| Native slug UX for public CPTs | A | CPT standard; AP-002 |
| Typography render-time owner | A | [TYPOGRAPHY](FORGE-WORDPRESS-TYPOGRAPHY-PIPELINE-STANDARD-v1.md) |
| Source / runtime identity | C | [AUTHORITY](../runbooks/FORGE-WORDPRESS-SOURCE-RUNTIME-AUTHORITY-STANDARD-v1.md) |
| Environment classification | C | [ENVIRONMENT](../runbooks/FORGE-WORDPRESS-ENVIRONMENT-MIGRATION-STANDARD-v1.md) |
| Deployment / rollback hooks (manifests, hashes) | C | [DEPLOY](../runbooks/FORGE-WORDPRESS-PRODUCTION-DEPLOYMENT-SOP-v1.md) |
| Standard navigation (native menus) | A | [NAVIGATION](FORGE-WORDPRESS-NAVIGATION-STANDARD-v1.md) |

Optional (select in P4): Smart Search, staff CPT, reviews, social registry, Activity Log, DOCX, reading time, auto TOC, consultation forms, decorative parallax, extra analytics.

---

## 1. Phases and gates

Map to existing FWP-01–12 where useful. Production reality after FP-0002 adds **connection → migrate → stabilize → cutover**.

### P0 Discovery

**Do:** business IA, locales, hosting, mail provider vs web host, existing domain/DNS/mail, indexing constraints, WPilot need.  
**Gate:** passport + production mode (`PIXEL_PERFECT` \| `TEMPLATE_ART`) declared.  
**Stop if:** undeclared mode; no hosting/DNS owner.

### P1 Content model

**Do:** Page vs Post vs CPT vs options vs repeater vs FE-only. Fill CPT decision matrix **before** first registration. Define URL map.  
**Gate:** CONTENT-MODEL signed. No “we will just use Pages and see”.  
**FP-0002:** specialists started as child Pages → CPT (P11). Do this decision in P1.

### P1b CMS / Editable Architecture Design

**Formal pre-frontend phase.** Frontend WordPress implementation must not begin with unresolved content ownership.

**Do:** Run the [DESIGN-TO-CMS workflow](FORGE-WORDPRESS-DESIGN-TO-CMS-WORKFLOW-v1.md). Produce the CMS pack:

- entity map · storage map · relationship map · Site Settings map · page field/editability map  
- reusable component data contracts · Admin IA · editor workflow plan  
- URL ownership · SEO ownership · migration assumptions  

Use templates listed in [CMS ARCHITECTURE §18](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md). Apply [REPEATER VS ENTITY](FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md). One owner per business value.

**Gate:** P1b pack signed (tabletop editor review at minimum). ACF groups are **not** started until entities/ownership are named.  
**Stop if:** dual owners for one value; 12 same-class cards with no CPT/repeater decision; internal CTAs planned as absolute URLs.

### P2 Admin model

**Do:** Site Settings IA; CPT list columns; hide junk metaboxes; i18n strings; Dashboard widget stub; dangerous screens Admin-only.  
**Gate:** ADMIN-UX-MAP; no raw Options/debug for editors.

### P3 Frontend architecture

**Do:** theme vs functionality plugin (R-TF-01/02); template map; asset owners; one transform owner; native menus. Consume **P1b contracts** — do not invent field ownership in templates.  
**Gate:** TEMPLATE-MAP + enqueue map + component contracts referenced.

### P4 Module selection

**Do:** pick CORE vs OPTIONAL from [MODULE-CATALOG](../registries/FORGE-WORDPRESS-MODULE-CATALOG-v1.md).  
**Gate:** written module list with maturity (do not silently enable experimental).

### P5 Local build

**Do:** MLI/local site; source under Git `WORDPRESS/`; ACF Local JSON.  
**Gate:** local HTTP smoke; no production credentials in repo.

### P6 Content / Admin integration

**Do:** ACF SoT; empty fields hide; no demo fallback on empty Admin data (AP-009).  
**Gate:** editor walkthrough; real wp-admin save test (not only PHP helpers).

### P7 Responsive / real-device QA

**Do:** Chrome/Firefox; Android Chrome; **physical iPhone Safari** for device-specific motion/scroll; trackpad if sliders.  
**Gate:** [REAL-DEVICE-QA](FORGE-WORDPRESS-REAL-DEVICE-QA-STANDARD-v1.md). Emulation is not iOS PASS.

### P8 SEO / forms / analytics

**Do:** meta + sitemap + forms handler; analytics fields empty-safe. SMTP **not** required locally if mail suppressed — but production sequencing is later.  
**Gate:** SEO owner unique; form nonce/CSRF; sitemap generates; indexing still closed on non-final hosts.

### P9 Production connection

**Do:** access matrix; WPilot READ; write_enabled=false; source/runtime hashes.  
**Gate:** [WPILOT](../runbooks/FORGE-WORDPRESS-WPILOT-PRODUCTION-STANDARD-v1.md); exact docroot (not placeholder jail).

### P10 Migration

**Do:** files+DB as chartered; classify environment; remove `.test`/localhost; do not leave runners in webroot.  
**Gate:** [ENVIRONMENT-MIGRATION](../runbooks/FORGE-WORDPRESS-ENVIRONMENT-MIGRATION-STANDARD-v1.md) checklist.

### P11 Stabilization

**Do:** intake operator drift; full backup; production baseline document; Git checkpoint via clean worktree.  
**Gate:** SOURCE ↔ PROD MATCH for product code; baseline named.

### P12 Pre-cutover

**Do:** webroot hygiene; users; redirects; DNS zone inventory; freeze runbook; cutover mutation plans exact.  
**Gate:** [PRE-CUTOVER SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) readiness matrix GO.

### P13 Cutover

**Do:** freeze → fresh full backup → NS or A-record as planned → verify DNS (including **mail**) → SSL → home/siteurl → URL migrate → smoke **indexing closed**.  
**Forbidden:** indexing open; SMTP skipped; future-host redirects before final domain works.

### P14 Post-launch

**Do:** SMTP → form delivery proof → robots/indexability → Webmaster/Search Console → sitemap submit → final crawl.  
**Gate:** [DEFINITION-OF-DONE](FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md).

---

## 2. Default technical architecture

```text
Functionality plugin  → CPT, ACF, settings, forms, SEO, i18n, logs, dashboard
Theme                 → templates, assets, chrome consumers of settings
MU-plugin (temporary) → mail suppress / env only when chartered; **retire after SMTP VERIFIED + operator activate**
WPilot                → operational READ; writes only with separate charter
```

**Permalink:** WordPress native UI.  
**Sitemap:** native `wp-sitemap.xml` extended.  
**Contacts/social:** one options SoT.  
**Typography:** one render-time HTML-aware owner.

---

## 3. Explicit non-goals of this blueprint

- Copying medical IA, brand, or copy from FP-0002
- Claiming AG-WP-001 is production-ready (still synthetic/read-only capability)
- Shipping an extracted shared plugin in this knowledge wave (see extraction backlog)

---

## 4. Required reading for a new site

1. This blueprint  
2. [CMS-ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) (P1b)  
3. [NEW-SITE-STARTER-CHECKLIST](../templates/FORGE-WORDPRESS-NEW-SITE-STARTER-CHECKLIST-v1.md)  
4. [ANTI-PATTERN-REGISTRY](FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md) · [CMS-ANTI-PATTERNS](FORGE-WORDPRESS-CMS-ANTI-PATTERNS-v1.md)  
5. [DEFINITION-OF-DONE](FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md)

*Blueprint v1.1 — FP-0002 production lessons integrated; P1b CMS/editable architecture is a formal pre-frontend phase. Second-case validation still required for optional modules marked J.*
