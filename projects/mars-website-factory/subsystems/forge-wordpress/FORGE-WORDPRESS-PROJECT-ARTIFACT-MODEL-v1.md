# Forge WordPress — Project Artifact Model v1

**Document type:** Artifact registry (templates deferred to FW-02)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01

**Rule:** FW-01 defines the model only — **artifact templates are FW-02 deliverables**.

---

## 1. Canonical project location

| Context | Path pattern |
|---------|--------------|
| **LOC-ZONE project root** | `workspaces/website-factory-operations/{FP-XXXX-SLUG}/` |
| **WordPress implementation docs** | `{project}/wordpress/` or `{project}/FORGE-WORDPRESS/` — **FW-02 standardizes** |
| **Subsystem methodology** | `projects/mars-website-factory/subsystems/forge-wordpress/` |

---

## 2. Artifact registry

| Artifact ID | Required | Owner | Creation stage | Approval stage | Reusable |
|-------------|----------|-------|----------------|----------------|----------|
| **PROJECT-INTAKE** | Required | Operator | FWP-01 | G1 | Project-specific |
| **FRONTEND-HANDOFF** | Required | Factory → Forge | FWP-01 | G1 | Project-specific |
| **FRONTEND-READINESS-REPORT** | Required | Forge Architect | FWP-02 | G2 | Project-specific |
| **WORDPRESS-ARCHITECTURE-DECISION** | Required | Forge Architect | FWP-03 | G3 | Project-specific |
| **CONTENT-MODEL** | Required | Content Modeler | FWP-04 | G4 | Project-specific |
| **EDITABLE-REGIONS-MAP** | Required | Admin UX Specialist | FWP-05 | G4 | Project-specific |
| **TEMPLATE-MAP** | Required | Theme Specialist | FWP-05 | G4 | Project-specific |
| **BLOCK-TO-WP-MAPPING** | Required | Forge Architect | FWP-05 | G4 | Project-specific |
| **ACF-SCHEMA** | Conditional | Content Modeler | FWP-04 | G4 | Project-specific (when ACF mode) |
| **CPT-TAXONOMY-MAP** | Required | Content Modeler | FWP-04 | G4 | Project-specific |
| **THEME-ARCHITECTURE** | Required | Theme Specialist | FWP-05 | G4 | Project-specific |
| **FUNCTIONALITY-BOUNDARY** | Required | Theme Specialist | FWP-05 | G4 | Project-specific |
| **PLUGIN-REGISTER** | Required | Forge Architect | FWP-05 | G4 | Project-specific |
| **ADMIN-UX-MAP** | Required | Admin UX Specialist | FWP-05 | G4 | Project-specific |
| **IMPLEMENTATION-SPEC** | Required | Forge Architect | FWP-06 | G5 | Project-specific |
| **VALIDATION-PLAN** | Required | WordPress Validator | FWP-06 | G5 | Project-specific |
| **VISUAL-QA-REPORT** | Required | Visual Parity Validator | FWP-09 | G8 | Project-specific |
| **RELEASE-MANIFEST** | Required | Forge Architect | FWP-10 | G9 | Project-specific |
| **WPILOT-HANDOFF** | Required | Handoff Reviewer | FWP-11 | G10 | Project-specific |
| **LESSONS-LEARNED** | Conditional | Operator | FWP-12 | — | Reusable patterns → subsystem register |

---

## 3. Conditional rules

| Condition | Additional artifacts |
|-----------|---------------------|
| ACF mode in WAD | `ACF-SCHEMA` required |
| Mode B hybrid | Hybrid manifest annex in `BLOCK-TO-WP-MAPPING` |
| Mode C legacy | Legacy audit artifact (FW-02 template) |
| Mode D charter | Charter-defined artifacts |
| Third-party plugins | `PLUGIN-REGISTER` entries with approval IDs |
| PIXEL_PERFECT upstream | `VISUAL-QA-REPORT` blocking at G8 |

---

## 4. Versioning and naming

| Rule | Definition |
|------|------------|
| **Filename pattern** | `{PROJECT}-{ARTIFACT-ID}-v{N}.md` or `.json` for schema |
| **Version bump** | Required on material spec change after G5 |
| **Git** | All artifacts committed — [R-VC-*](FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md) |

---

## 5. Artifact dependencies

```text
PROJECT-INTAKE + FRONTEND-HANDOFF
    → FRONTEND-READINESS-REPORT
        → WORDPRESS-ARCHITECTURE-DECISION
            → CONTENT-MODEL + THEME-ARCHITECTURE + ADMIN-UX-MAP (parallel)
                → IMPLEMENTATION-SPEC + VALIDATION-PLAN
                    → (implementation code artifacts — FW-05+)
                        → VISUAL-QA-REPORT + WV reports
                            → RELEASE-MANIFEST
                                → WPILOT-HANDOFF
                                    → LESSONS-LEARNED
```

---

## 6. FW-02 templates (not created in FW-01)

FW-02 will deliver blank templates for each required artifact — see [reports/FORGE-WORDPRESS-FW-02-CONTRACTS-AND-STANDARDS-INPUT-v1.md](reports/FORGE-WORDPRESS-FW-02-CONTRACTS-AND-STANDARDS-INPUT-v1.md).

---

## Related documents

- [FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md](FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md)
- [FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md](FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md)

---

*Artifact model v1 — registry only; templates deferred.*
