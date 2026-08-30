# I-SEO Report Hub — Platform Decision v0.1

**Status:** DECIDED (operator 2026-07-24)  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Implementation:** **NOT STARTED** — documentation decision only

**Supersedes (for runtime SoT):** WordPress-as-runtime assumptions in Product Charter v0.1 §4 and MVP Scope v0.1 WordPress framing — those docs remain historical; this decision is current platform authority.

**Related:** [Product Architecture Layer 02](I-SEO-REPORT-HUB-PRODUCT-ARCHITECTURE-LAYER-02-v0.1.md), [Implementation Options Decision Frame](I-SEO-REPORT-HUB-IMPLEMENTATION-OPTIONS-DECISION-FRAME-v0.1.md), [Platform Options](I-SEO-REPORT-HUB-PLATFORM-OPTIONS-v0.1.md), [PHP + MySQL MVP Technical Brief](I-SEO-REPORT-HUB-PHP-MYSQL-MVP-TECHNICAL-BRIEF-v0.1.md)

---

## 1. Decision

| Decision | Value |
|----------|-------|
| **Selected platform** | Custom **PHP + SQL/MySQL** (MySQL or MariaDB) application |
| **WordPress as runtime / source of truth** | **Rejected** |
| **Local dev/runtime candidate** | **Laragon** (available on operator machine) |
| **Static demo v0.4** | UX reference only — not implementation |
| **i-seo.su / WordPress** | Not product runtime; not DB SoT; not admin backend for reports |

Operator authority (2026-07-24): build **without WordPress**; own PHP + SQL/MySQL product; Laragon may be used for local development/runtime.

---

## 2. Reasoning

Report Hub is an **operational reporting system**, not a CMS page editor or PDF-only tool. Product Architecture Layer 02 requires:

| Need | Why custom PHP + MySQL fits |
|------|----------------------------|
| **Structured data model** | Clients, projects, sites, periods, blocks, KPI values map cleanly to relational tables |
| **Roles / permissions** | Fine-grained specialist assignment and review gates without WP capability friction |
| **Report lifecycle** | Explicit state machines for period / weekly / monthly / block |
| **Snapshots** | Draft vs published payload separation without CPT/meta awkwardness |
| **Evidence / files** | Controlled private storage with app-level ACL |
| **Future imports** | Topvisor and other APIs attach to app jobs without plugin coupling |
| **Clean product logic** | Specialist workspace and review queue designed for the domain, not wp-admin chrome |

WordPress on i-seo.su would add:

- plugin/theme update coupling;
- CPT/meta pressure for complex entities;
- specialist UX fighting wp-admin patterns;
- blurred SoT between marketing site and reporting product.

Therefore WordPress is **rejected as runtime and source of truth** for Report Hub MVP and forward product path.

---

## 3. What WordPress May Still Do

| Allowed residual role | Allowed? | Notes |
|----------------------|----------|-------|
| Visual style reference (i-seo.su / INTLSEO direction) | Yes | Demo and future UI may mirror brand look |
| Possible future public embedding / linking of published reports | Yes | Only if explicitly designed later; **not** required for MVP |
| Landing / marketing pages on i-seo.su | Yes | Marketing site remains separate concern |
| Database source of truth for reports | **No** | |
| Admin backend for Report Hub | **No** | |
| Required dependency for MVP | **No** | |

Historical WordPress architecture and data-model docs remain in the programme corpus as **legacy / Option A planning**, not current implementation authority.

---

## 4. Consequences

Choosing custom PHP + MySQL means Report Hub must own:

| Concern | Ownership |
|---------|-----------|
| Authentication / sessions | Own |
| Database schema | Own |
| File / evidence storage | Own |
| Report renderer (admin + client) | Own |
| Client token / controlled link | Own |
| Backup / export strategy | Own |
| Deployment plan | Own |

These are **planned** consequences — none are implemented in this task.

---

## 5. SAFE UNKNOWN

Exact values remain unverified until a future runtime confirmation charter:

| Item | Status |
|------|--------|
| Exact PHP version (Laragon / production) | **SAFE UNKNOWN** |
| Exact MySQL / MariaDB version | **SAFE UNKNOWN** |
| Laragon install path / vhost name | **SAFE UNKNOWN** |
| Final production hosting model | **SAFE UNKNOWN** |
| Final file storage path (local / production) | **SAFE UNKNOWN** |
| Final client access security model (token-only vs password vs later portal) | **SAFE UNKNOWN** (MVP default direction: unlisted token URL per Publishing model) |

---

## 6. Boundaries

- This document is a **platform decision**, not an implementation charter.
- No PHP code, SQL migrations, Laragon changes, or demo edits are authorized by this decision alone.
- Next product step: operator review of the PHP/MySQL MVP Technical Brief package, then scoped commit if approved.
