# Forge WordPress — Contracts and Standards Register v1

**Document type:** Subsystem local register  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02

**Note:** Local subsystem IDs only — **not** global MARS registry rows.

---

## Contracts

| ID | Document | Type | Status | Applies to | Authority |
|----|----------|------|--------|------------|-----------|
| FW-C-01 | [WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md](../contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md) | Contract | BASELINE v1 | B1; FWP-01; WV0 | Forge WordPress + Factory |
| FW-C-02 | [FORGE-WORDPRESS-PROJECT-INTAKE-CONTRACT-v1.md](../contracts/FORGE-WORDPRESS-PROJECT-INTAKE-CONTRACT-v1.md) | Contract | BASELINE v1 | FWP-01; G1 | Forge WordPress Operator |
| FW-C-03 | [FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md](../contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md) | Contract | BASELINE v1 | B3; FWP-11; G10; WV9 | Forge WordPress → WPilot |

---

## Standards

| ID | Document | Type | Status | Applies to | Authority |
|----|----------|------|--------|------------|-----------|
| FW-S-01 | [FORGE-WORDPRESS-CONTENT-MODELING-STANDARD-v1.md](../standards/FORGE-WORDPRESS-CONTENT-MODELING-STANDARD-v1.md) | Standard | BASELINE v1 | L4; FWP-04; WV1 | Content Modeler |
| FW-S-02 | [FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md](../standards/FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md) | Standard | BASELINE v1 | L4/L6; conditional ACF | Content Modeler |
| FW-S-03 | [FORGE-WORDPRESS-THEME-ARCHITECTURE-STANDARD-v1.md](../standards/FORGE-WORDPRESS-THEME-ARCHITECTURE-STANDARD-v1.md) | Standard | BASELINE v1 | L5; FWP-05; WV1 | Theme Specialist |
| FW-S-04 | [FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md](../standards/FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md) | Standard | BASELINE v1 | L5/L6; R-TF-*; WV1 | Theme Specialist |
| FW-S-05 | [FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md](../standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) | Standard | BASELINE v1 | L7; FWP-05; WV7 | Admin UX Specialist |
| FW-S-06 | [FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md](../standards/FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md) | Standard | BASELINE v1 | FWP-05; WV4 | Forge Architect |
| FW-S-07 | [FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md](../standards/FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md) | Standard | BASELINE v1 | L8; WV2; WV4 | WordPress Validator |
| FW-S-08 | [FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md](../standards/FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md) | Standard | BASELINE v1 | WV0–WV9; FWP-08–09 | WordPress Validator |

---

## Templates

| ID | Document | Type | Status | Artifact ID | Authority |
|----|----------|------|--------|-------------|-----------|
| FW-T-01 | [FORGE-WORDPRESS-PROJECT-INTAKE-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-PROJECT-INTAKE-TEMPLATE-v1.md) | Template | BASELINE v1 | PROJECT-INTAKE | Operator |
| FW-T-02 | [FORGE-WORDPRESS-FRONTEND-HANDOFF-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-FRONTEND-HANDOFF-TEMPLATE-v1.md) | Template | BASELINE v1 | FRONTEND-HANDOFF | Factory → Forge |
| FW-T-03 | [FORGE-WORDPRESS-ARCHITECTURE-DECISION-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-ARCHITECTURE-DECISION-TEMPLATE-v1.md) | Template | BASELINE v1 | WORDPRESS-ARCHITECTURE-DECISION | Forge Architect |
| FW-T-04 | [FORGE-WORDPRESS-CONTENT-MODEL-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-CONTENT-MODEL-TEMPLATE-v1.md) | Template | BASELINE v1 | CONTENT-MODEL | Content Modeler |
| FW-T-05 | [FORGE-WORDPRESS-EDITABLE-REGIONS-MAP-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-EDITABLE-REGIONS-MAP-TEMPLATE-v1.md) | Template | BASELINE v1 | EDITABLE-REGIONS-MAP | Admin UX Specialist |
| FW-T-06 | [FORGE-WORDPRESS-TEMPLATE-MAP-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-TEMPLATE-MAP-TEMPLATE-v1.md) | Template | BASELINE v1 | TEMPLATE-MAP | Theme Specialist |
| FW-T-07 | [FORGE-WORDPRESS-ACF-SCHEMA-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-ACF-SCHEMA-TEMPLATE-v1.md) | Template | BASELINE v1 | ACF-SCHEMA | Content Modeler |
| FW-T-08 | [FORGE-WORDPRESS-CPT-TAXONOMY-MAP-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-CPT-TAXONOMY-MAP-TEMPLATE-v1.md) | Template | BASELINE v1 | CPT-TAXONOMY-MAP | Content Modeler |
| FW-T-09 | [FORGE-WORDPRESS-PLUGIN-REGISTER-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-PLUGIN-REGISTER-TEMPLATE-v1.md) | Template | BASELINE v1 | PLUGIN-REGISTER | Forge Architect |
| FW-T-10 | [FORGE-WORDPRESS-ADMIN-UX-MAP-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-ADMIN-UX-MAP-TEMPLATE-v1.md) | Template | BASELINE v1 | ADMIN-UX-MAP | Admin UX Specialist |
| FW-T-11 | [FORGE-WORDPRESS-VALIDATION-REPORT-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-VALIDATION-REPORT-TEMPLATE-v1.md) | Template | BASELINE v1 | WV* reports | WordPress Validator |
| FW-T-12 | [FORGE-WORDPRESS-RELEASE-MANIFEST-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-RELEASE-MANIFEST-TEMPLATE-v1.md) | Template | BASELINE v1 | RELEASE-MANIFEST | Forge Architect |
| FW-T-13 | [FORGE-WORDPRESS-WPILOT-HANDOFF-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-WPILOT-HANDOFF-TEMPLATE-v1.md) | Template | BASELINE v1 | WPILOT-HANDOFF | Handoff Reviewer |

---

## FW-02 meta documents

| ID | Document | Type | Status |
|----|----------|------|--------|
| FW-M-01 | [FORGE-WORDPRESS-FW-02-COMPLIANCE-MATRIX-v1.md](../FORGE-WORDPRESS-FW-02-COMPLIANCE-MATRIX-v1.md) | Matrix | BASELINE v1 |
| FW-M-02 | [reports/FORGE-WORDPRESS-FW-03-TOOLING-AND-VALIDATION-DESIGN-INPUT-v1.md](../reports/FORGE-WORDPRESS-FW-03-TOOLING-AND-VALIDATION-DESIGN-INPUT-v1.md) | Input | v1 |

---

*Register v1 — subsystem local; updated FW-02 complete.*
