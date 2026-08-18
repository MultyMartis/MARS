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
| ACF fields, naming, JSON, CTA conditionals | [ACF-FIELD-MODELING](../standards/FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md) |
| Admin menus / tabs / list tables | [ADMIN-INFORMATION-ARCHITECTURE](../standards/FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md) · [ADMIN-UX-STANDARD](../standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) |
| Component empty states / data contracts | [COMPONENT-DATA-CONTRACT](../standards/FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-STANDARD-v1.md) |
| Internal links / relations | [RELATIONSHIP-MODELING](../standards/FORGE-WORDPRESS-RELATIONSHIP-MODELING-STANDARD-v1.md) |
| CMS modeling anti-patterns | [CMS-ANTI-PATTERNS](../standards/FORGE-WORDPRESS-CMS-ANTI-PATTERNS-v1.md) · [ANTI-PATTERN-REGISTRY](../standards/FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md) |
| What must not be repeated (ops + CMS) | [ANTI-PATTERN-REGISTRY](../standards/FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md) |
| Staging → production → final domain | [ENVIRONMENT-MIGRATION](../runbooks/FORGE-WORDPRESS-ENVIRONMENT-MIGRATION-STANDARD-v1.md) · [PRE-CUTOVER-AND-LAUNCH-SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) |
| Is the site actually done? | [DEFINITION-OF-DONE](../standards/FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md) |
| Which modules exist | [MODULE-CATALOG](../registries/FORGE-WORDPRESS-MODULE-CATALOG-v1.md) |
| Theme vs plugin vs MU? | [CODE-OWNERSHIP-BOUNDARIES](../standards/FORGE-WORDPRESS-CODE-OWNERSHIP-BOUNDARIES-STANDARD-v1.md) |
| CSS / JS / component owners | [CSS-COMPONENT-ARCHITECTURE](../standards/FORGE-WORDPRESS-CSS-COMPONENT-ARCHITECTURE-STANDARD-v1.md) · [FRONTEND-INTERACTION](../standards/FORGE-WORDPRESS-FRONTEND-INTERACTION-OWNERSHIP-STANDARD-v1.md) |
| Design-system architecture (not brand) | [DESIGN-SYSTEM-FOUNDATION](../standards/FORGE-WORDPRESS-DESIGN-SYSTEM-FOUNDATION-v1.md) · [map template](../templates/FORGE-WORDPRESS-DESIGN-SYSTEM-MAP-TEMPLATE-v1.md) |
| Media / SVG / video | [MEDIA-ARCHITECTURE](../standards/FORGE-WORDPRESS-MEDIA-ARCHITECTURE-STANDARD-v1.md) |
| May we install another plugin? | [PLUGIN-GOVERNANCE](../standards/FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md) |
| Production WP/plugin update | [PRODUCTION-UPDATE-SOP](../runbooks/FORGE-WORDPRESS-PRODUCTION-UPDATE-SOP-v1.md) |
| What can the client editor do? | [CONTENT-OPERATIONS](../standards/FORGE-WORDPRESS-CONTENT-OPERATIONS-STANDARD-v1.md) · [CLIENT-HANDOFF](../templates/FORGE-WORDPRESS-CLIENT-HANDOFF-TEMPLATE-v1.md) |
| Frontend regression beyond screenshots | [REGRESSION-PACK](../standards/FORGE-WORDPRESS-REGRESSION-PACK-v1.md) · [FRONTEND-ACCEPTANCE](../standards/FORGE-WORDPRESS-FRONTEND-ACCEPTANCE-STANDARD-v1.md) |
| Retire a migration tool | [MODULE-LIFECYCLE](../standards/FORGE-WORDPRESS-MODULE-LIFECYCLE-STANDARD-v1.md) |
| What exists before site #2 pages? | [SECOND-SITE-BOOTSTRAP](../standards/FORGE-WORDPRESS-SECOND-SITE-BOOTSTRAP-v1.md) |
| Which modules are R1 extractable? | [EXTRACTION-ROADMAP](FORGE-WORDPRESS-REUSABLE-CODE-EXTRACTION-ROADMAP-v1.md) |

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
- [FP-0002 remaining knowledge gap map (engineering/ops wave)](FP-0002-REMAINING-KNOWLEDGE-GAP-MAP.md)
- [Knowledge-retrieval validation (ops + CMS + engineering Q1–Q12)](KNOWLEDGE-RETRIEVAL-VALIDATION.md)
- [Production maturity map](FORGE-WORDPRESS-PRODUCTION-MATURITY-MAP-v1.md)
- [Incident lessons](FORGE-WORDPRESS-PRODUCTION-INCIDENT-LESSONS-v1.md)
- [Incident response SOP](../runbooks/FORGE-WORDPRESS-INCIDENT-RESPONSE-SOP-v1.md)
- [Experience harvest loop](FORGE-WORDPRESS-EXPERIENCE-HARVEST-LOOP-v1.md)
- [ADR pack](FORGE-WORDPRESS-ADR-PACK-v1.md)
- [Reusable code extraction roadmap](FORGE-WORDPRESS-REUSABLE-CODE-EXTRACTION-ROADMAP-v1.md)
- [Second-project validation plan](FORGE-WORDPRESS-SECOND-PROJECT-VALIDATION-PLAN-v1.md)
- [Module extraction backlog (short historical table)](FORGE-WORDPRESS-MODULE-EXTRACTION-BACKLOG-v1.md)

CMS + engineering templates live under [`templates/`](../templates/) (entity/ownership maps, design-system map, component inventory, dependency register, client handoff, environment flags, temporary-tool register).

*WP Forge knowledge hub — 2026-08-18. One production case. CMS pack + engineering/operations assimilation the same day. Second-project validation still required where marked J.*
