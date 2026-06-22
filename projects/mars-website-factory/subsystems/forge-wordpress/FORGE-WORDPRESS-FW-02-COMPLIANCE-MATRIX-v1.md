# Forge WordPress — FW-02 Compliance Matrix v1

**Document type:** Traceability matrix  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02

**Purpose:** Demonstrate FW-02 contracts, standards, templates, and validation cover FW-01 architecture without orphan requirements.

---

## Matrix

| Architecture layer | Lifecycle stage | Contract | Standard | Artifact / template | Validation | Human gate |
|-------------------|-----------------|----------|----------|---------------------|------------|------------|
| L1 Intake | FWP-01 | FW-C-01, FW-C-02 | — | FW-T-01, FW-T-02 | WV0 | G1 |
| L2 Frontend readiness | FWP-02 | FW-C-01 | — | FRONTEND-READINESS-REPORT | WV0 | G2 |
| L3 Implementation mode | FWP-03 | — | Modes doc (FW-01) | FW-T-03 | WV1 | G3 |
| L4 Content model | FWP-04 | — | FW-S-01, FW-S-02 | FW-T-04, FW-T-07, FW-T-08 | WV1 | G4 |
| L5 Theme / plugin boundary | FWP-05 | — | FW-S-03, FW-S-04 | FW-T-06, FUNCTIONALITY-BOUNDARY | WV1 | G4 |
| L6 ACF / fields | FWP-04–05 | — | FW-S-02 | FW-T-07 | WV1, WV3 | G4 |
| L7 Admin UX | FWP-05 | — | FW-S-05 | FW-T-05, FW-T-10 | WV7 | G4 |
| L8 Implementation | FWP-06–07 | B2 internal | FW-S-07 | IMPLEMENTATION-SPEC | WV2, WV3 | G5 |
| L9 Validation | FWP-08–09 | — | FW-S-08 | FW-T-11 | WV0–WV9 | G6–G8 |
| L10 Packaging / handoff | FWP-10–11 | FW-C-03 | FW-S-06 | FW-T-09, FW-T-12, FW-T-13 | WV4, WV9 | G9, G10 |

---

## Boundary coverage

| Boundary | Contract | WPilot alignment |
|----------|----------|------------------|
| B1 Factory → Forge | FW-C-01, FW-C-02 | — |
| B2 Internal | Artifact model (FW-01) | — |
| B3 Forge → WPilot | FW-C-03 | ChangeSet, Risk, Rollback, Target Registry |

---

## FW-01 rule traceability (sample)

| FW-01 rule | FW-02 home |
|------------|------------|
| R-TF-01–03 | FW-S-03, FW-S-04 |
| R-ACF-01–04 | FW-S-02 |
| R-UX-01–04 | FW-S-05 |
| R-VC-01–06 | FW-S-02, FW-S-07, FW-C-03 |
| R-ENV-01–05 | FW-C-02, FW-C-03 |
| WV0–WV9 | FW-S-08 |

---

## Orphan check

| Check | Status |
|-------|--------|
| All required artifacts have templates | ✓ FW-T-01–13 |
| All contracts linked in OPERATIONAL-INDEX | ✓ |
| All standards linked to WV layer | ✓ |
| No WordPress code in FW-02 | ✓ |
| Theme/plugin boundary consistent | ✓ FW-S-03 + FW-S-04 |
| ACF/content model consistent | ✓ FW-S-01 + FW-S-02 |
| WPilot separation explicit | ✓ FW-S-04, FW-C-03 |

---

## Related

- [registries/FORGE-WORDPRESS-CONTRACTS-AND-STANDARDS-REGISTER-v1.md](registries/FORGE-WORDPRESS-CONTRACTS-AND-STANDARDS-REGISTER-v1.md)
- [FORGE-WORDPRESS-ARCHITECTURE-v1.md](FORGE-WORDPRESS-ARCHITECTURE-v1.md)

---

*Compliance matrix v1 — FW-02 coverage proof.*
