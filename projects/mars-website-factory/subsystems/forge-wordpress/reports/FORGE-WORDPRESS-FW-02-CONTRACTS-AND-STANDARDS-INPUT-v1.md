# Forge WordPress — FW-02 Contracts and Standards Input v1

**Document type:** Next-stage input package  
**Version:** v1  
**Date:** 2026-06-22  
**Authorized use:** Input to **FW-02 — Contracts and Standards** only

---

## 1. Purpose

Enumerate documents FW-02 must create to operationalize FW-01 methodology into **contracts, standards, and templates**. FW-02 does **not** implement code or tooling.

---

## 2. Required FW-02 documents

### 2.1 Handoff and intake contracts

| # | Document | Source boundary |
|---|----------|-----------------|
| 1 | **Website Factory → Forge WordPress Handoff Contract** | B1 — [FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md](../FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md) |
| 2 | **WordPress Project Intake Contract** | FWP-01; artifact PROJECT-INTAKE |
| 3 | **Forge WordPress → WPilot Handoff Contract** | B3 — ecosystem position |

### 2.2 Architecture and modeling standards

| # | Document | FW-01 source |
|---|----------|--------------|
| 4 | **Content Modeling Standard** | L4; R-TF-02; CONTENT-MODEL artifact |
| 5 | **ACF Architecture Standard** | R-ACF-*; conditional ACF-SCHEMA |
| 6 | **Theme Architecture Standard** | L5; Mode A/B template rules |
| 7 | **Functionality Plugin Standard** | R-TF-*; FUNCTIONALITY-BOUNDARY |
| 8 | **Admin UX Standard** | R-UX-*; ADMIN-UX-MAP |

### 2.3 Governance and quality standards

| # | Document | FW-01 source |
|---|----------|--------------|
| 9 | **Plugin Governance Standard** | PLUGIN-REGISTER; WV4 |
| 10 | **Coding and Security Standard** | WV2/WV4; PHPCS; WP security handbook alignment |
| 11 | **Validation Standard** | WV0–WV9 operationalization; false-green rules |

### 2.4 Artifact templates

| # | Template set | Artifacts covered |
|---|--------------|-------------------|
| 12 | **Project artifact templates pack** | All required artifacts from [FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md](../FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md) |

Minimum templates:

- PROJECT-INTAKE
- FRONTEND-HANDOFF acknowledgment
- FRONTEND-READINESS-REPORT
- WORDPRESS-ARCHITECTURE-DECISION
- CONTENT-MODEL
- BLOCK-TO-WP-MAPPING
- EDITABLE-REGIONS-MAP
- IMPLEMENTATION-SPEC
- VALIDATION-PLAN
- VISUAL-QA-REPORT
- RELEASE-MANIFEST
- WPILOT-HANDOFF
- LESSONS-LEARNED

---

## 3. FW-02 sequencing (recommended)

```text
Pass 1: Handoff contracts (1–3) — unblocks intake semantics
Pass 2: Modeling standards (4–5) — unblocks WAD execution
Pass 3: Implementation standards (6–8, 9–10)
Pass 4: Validation standard (11)
Pass 5: Artifact templates (12)
```

---

## 4. Dependencies on external packs

| External | FW-02 need |
|----------|------------|
| [frontend-handoff-contract-v0.md](../../frontend-handoff-contract-v0.md) | Extend for WordPress-specific annex |
| [website-factory-validation-architecture-charter-v1.md](../../website-factory-validation-architecture-charter-v1.md) | VL/WV crosswalk in Validation Standard |
| [projects/wpilot/OPERATIONAL-INDEX.md](../../../wpilot/OPERATIONAL-INDEX.md) | B3 contract alignment review |

---

## 5. Explicit FW-02 exclusions

| Excluded | Stage |
|----------|-------|
| PHP/theme code | FW-05+ |
| Validation runner scripts | FW-03 |
| Agent registration | FW-05 charter |
| Local stack setup guide | FW-03 |

---

## 6. Success criteria for FW-02

| Criterion | Measure |
|-----------|---------|
| All contracts draft-complete | Human reviewable |
| Standards reference FW-01 rules by ID | Traceability |
| Templates cover all **required** artifacts | No orphan artifact IDs |
| OPERATIONAL-INDEX updated | Navigation |
| No implementation code | Git diff audit |

---

## Related

- [FORGE-WORDPRESS-FW-01-DECISION-RECORD-v1.md](FORGE-WORDPRESS-FW-01-DECISION-RECORD-v1.md)
- [../roadmap.md](../roadmap.md) — FW-02 **NEXT** after FW-01 complete

---

*FW-02 input v1 — not execution.*
