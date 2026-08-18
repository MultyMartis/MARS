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
| Page vs CPT vs options | [CONTENT-MODEL-CPT-STANDARD](../standards/FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) |
| Admin / Site Settings / dashboard | [ADMIN-UX-STANDARD](../standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) · [SITE-SETTINGS-STANDARD](../standards/FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md) |
| What must not be repeated | [ANTI-PATTERN-REGISTRY](../standards/FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md) |
| Staging → production → final domain | [ENVIRONMENT-MIGRATION](../runbooks/FORGE-WORDPRESS-ENVIRONMENT-MIGRATION-STANDARD-v1.md) · [PRE-CUTOVER-AND-LAUNCH-SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) |
| Is the site actually done? | [DEFINITION-OF-DONE](../standards/FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md) |
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
- [Knowledge-retrieval validation (Q1–Q3)](KNOWLEDGE-RETRIEVAL-VALIDATION.md)
- [Production maturity map](FORGE-WORDPRESS-PRODUCTION-MATURITY-MAP-v1.md)
- [Incident lessons](FORGE-WORDPRESS-PRODUCTION-INCIDENT-LESSONS-v1.md)
- [ADR pack](FORGE-WORDPRESS-ADR-PACK-v1.md)
- [Module extraction backlog](FORGE-WORDPRESS-MODULE-EXTRACTION-BACKLOG-v1.md)

*WP Forge knowledge hub — 2026-08-18. One production case. Second-project validation still required where marked J.*
