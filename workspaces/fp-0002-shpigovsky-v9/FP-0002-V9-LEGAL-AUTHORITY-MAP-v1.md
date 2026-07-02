# FP-0002 V9 — Legal Authority Map v1

**Phase:** V9-02  
**Date:** 2026-07-02

## CURRENT_CANONICAL_TEMPLATE

| Path | Title | Applicable pages | Reusable sections |
|------|-------|------------------|-------------------|
| `workspaces/website-factory-reference-v1/legal/privacy-policy-template.md` | Privacy Policy template | `/privacy-policy/` | definitions, purposes, rights, cookie reference, storage |
| `workspaces/website-factory-reference-v1/legal/consent-personal-data-template.md` | Consent PD template | `/consent-personal-data/` | data categories, purposes, withdrawal, policy acknowledgement |
| `workspaces/website-factory-reference-v1/legal/user-agreement-template.md` | User Agreement template | `/user-agreement/` | rights/obligations, liability, related docs |
| `workspaces/website-factory-reference-v1/legal/cookie-files-policy-template.md` | Cookie Policy template | `/cookie-files-policy/` | cookie categories, browser controls, tables |

## CURRENT_STANDARD

| Path | Classification | Use |
|------|----------------|-----|
| `workspaces/website-factory-reference-v1/legal/LEGAL-IMPLEMENTATION-RULES.md` | Footer Rule, Consent Rule, H1 canon | URL/H1/footer link discipline |
| `workspaces/website-factory-reference-v1/legal/LEGAL-PACK-ARCHITECTURE-v1.md` | Core Legal Pack L1–L4 | page family inventory |
| `workspaces/website-factory-reference-v1/page-architecture/LEGAL-PAGE-CONTRACT-v1.md` | Per-slot contracts | route/H1/footer invariants |
| `workspaces/website-factory-reference-v1/legal/LEGAL-VARIABLE-REGISTRY.md` | Variable registry | `{{company_name}}`, `{{domain}}`, etc. |
| `workspaces/website-factory-reference-v1/legal/LEGAL-GENERATION-CONTRACT-v1.md` | Production gate | unresolved placeholders = FAIL |

## APPROVED_EXAMPLE

| Path | Classification | Notes |
|------|----------------|-------|
| `workspaces/triumph-manipulator-landing-v6/src/partials/sections/legal/` | HTML structure reference | **Do not copy entity data** — different client |

## PROJECT_SPECIFIC_EXAMPLE

None verified for FP-0002 Shpigovsky legal entity.

## HISTORICAL / SUPERSEDED

| Path | Reason |
|------|--------|
| `workspaces/website-factory-reference-v1/snapshots/engine-readiness-audit-v1/legal/*` | Snapshot copy of canonical templates |

## UNSUITABLE

| Source | Reason |
|--------|--------|
| triumph-manipulator entity-specific content | Another project's legal operator |
| Random web legal texts | Not authorized by task |
| V8 one-line legal placeholders | Superseded in V9-02 |

## V9-02 implementation authority used

- MARS markdown templates for section structure and legal vocabulary
- triumph-manipulator HTML partial pattern for semantic markup only
- DEMO tokens where FP-0002 legal entity data is missing
