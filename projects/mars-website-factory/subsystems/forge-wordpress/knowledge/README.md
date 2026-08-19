# WP Forge production knowledge hub

**Status:** ACTIVE (2026-08-18)  
**Case that produced this pack:** FP-0002 Shpigovsky — production reference, not a second documentation tree.  
**Not:** runtime, orchestration, a shipped module library, or a claim that every FP-0002 module is a universal default.

Use this hub to answer: **how should we build, operate, migrate, and launch the next WordPress site?**

Do **not** reopen the full Shpigovsky chronology unless evidence is required.

---

## Start here

| Question | Canonical document |
|----------|-------------------|
| What should a new site receive from day 1? | [PRODUCTION-WEBSITE-BLUEPRINT-v1](../standards/FORGE-WORDPRESS-PRODUCTION-WEBSITE-BLUEPRINT-v1.md) |
| Concise next-project checklist | [NEW-SITE-STARTER-CHECKLIST](../templates/FORGE-WORDPRESS-NEW-SITE-STARTER-CHECKLIST-v1.md) |
| How do we turn a design into a WordPress editing model? | [CMS-ARCHITECTURE-STANDARD](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) |
| Page vs CPT vs Post vs taxonomy vs Options vs repeater | [CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) · [CONTENT-MODEL-CPT](../standards/FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) · [REPEATER-VS-ENTITY](../standards/FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md) |
| Figma → field schema before coding | [DESIGN-TO-CMS-WORKFLOW](../standards/FORGE-WORDPRESS-DESIGN-TO-CMS-WORKFLOW-v1.md) · [worksheet](../templates/FORGE-WORDPRESS-DESIGN-TO-CMS-MAPPING-WORKSHEET-v1.md) |
| Global phone/social ownership | [GLOBAL-SETTINGS-OWNERSHIP](../standards/FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md) · [SITE-SETTINGS-STANDARD](../standards/FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md) |
| Cookie/privacy controls for a small Russian production site | [COOKIE-CONSENT-AND-PRIVACY-CONTROLS](../standards/FORGE-WORDPRESS-COOKIE-CONSENT-AND-PRIVACY-CONTROLS-STANDARD-v1.md) · [FORMS-AND-SMTP](../standards/FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) |
| ACF fields, naming, JSON, CTA conditionals | [ACF-FIELD-MODELING](../standards/FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md) |
| Admin menus / tabs / list tables | [ADMIN-INFORMATION-ARCHITECTURE](../standards/FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md) · [ADMIN-UX-STANDARD](../standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) |
| Component empty states / data contracts | [COMPONENT-DATA-CONTRACT](../standards/FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-STANDARD-v1.md) |
| Internal links / relations | [RELATIONSHIP-MODELING](../standards/FORGE-WORDPRESS-RELATIONSHIP-MODELING-STANDARD-v1.md) |
| CMS modeling anti-patterns | [CMS-ANTI-PATTERNS](../standards/FORGE-WORDPRESS-CMS-ANTI-PATTERNS-v1.md) · [ANTI-PATTERN-REGISTRY](../standards/FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md) |
| What must not be repeated (ops + CMS) | [ANTI-PATTERN-REGISTRY](../standards/FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md) |
| Staging → production → final domain | [ENVIRONMENT-MIGRATION](../runbooks/FORGE-WORDPRESS-ENVIRONMENT-MIGRATION-STANDARD-v1.md) · [PRE-CUTOVER-AND-LAUNCH-SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) |
| Is the site actually done? | [DEFINITION-OF-DONE](../standards/FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md) |
| Is an Admin feature actually usable? | Same DoD discoverability sequence · [ADMIN-UX](../standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) §10.7 · AP-029 |
| How do we open/close search indexing? | [SEARCH-INDEXING-CONTROL](../standards/FORGE-WORDPRESS-SEARCH-INDEXING-CONTROL-STANDARD-v1.md) |
| Which modules exist | [MODULE-CATALOG](../registries/FORGE-WORDPRESS-MODULE-CATALOG-v1.md) |

---

## Classification used in this pack

| Code | Meaning |
|------|---------|
| **A** | Canonical pattern — reusable by default |
| **B** | Optional module — only when requirements call for it |
| **C** | Production operating standard |
| **D** | Migration / cutover standard |
| **E** | Admin UX standard |
| **F** | Frontend UX standard |
| **G** | Failure / anti-pattern — actively avoid |
| **H** | Real-device QA requirement |
| **I** | FP-0002 project-specific — do not generalize |
| **J** | Candidate — needs a second production case |

---

## Boundary

Do **not** copy as WP Forge defaults: clinical content, brand, phones, emails, social URLs, staff names, exact legacy redirects, medical taxonomy, client wording, credentials.

FP-0002 evidence lives under `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/`. This hub **absorbs lessons**; it does not replace project reports.

---

## Maps

- [FP-0002 → WP Forge assimilation index](FP-0002-KNOWLEDGE-ASSIMILATION-INDEX.md)
- [FP-0002 knowledge harvest map (35 areas)](FP-0002-KNOWLEDGE-HARVEST-MAP.md)
- [Knowledge-retrieval validation (ops Q1–Q3 + CMS Q1–Q10)](KNOWLEDGE-RETRIEVAL-VALIDATION.md)
- [Production maturity map](FORGE-WORDPRESS-PRODUCTION-MATURITY-MAP-v1.md)
- [Incident lessons](FORGE-WORDPRESS-PRODUCTION-INCIDENT-LESSONS-v1.md)
- [ADR pack](FORGE-WORDPRESS-ADR-PACK-v1.md)
- [Module extraction backlog](FORGE-WORDPRESS-MODULE-EXTRACTION-BACKLOG-v1.md)

CMS architecture templates live under [`templates/`](../templates/) (`CONTENT-ENTITY-MAP`, `FIELD-OWNERSHIP-MAP`, `PAGE-EDITABILITY-MAP`, `SITE-SETTINGS-MAP`, `RELATIONSHIP-MAP`, `COMPONENT-DATA-CONTRACT`, `ADMIN-INFORMATION-ARCHITECTURE`, `EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST`, `DESIGN-TO-CMS-MAPPING-WORKSHEET`, `CMS-MIGRATION-PLAN`).

*WP Forge knowledge hub — 2026-08-19 (P18E privacy/cookie-controls standard added on top of the prior P18C/P18D production knowledge pack). One production case. Second-project validation still required where marked J.*
