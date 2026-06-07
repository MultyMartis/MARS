# POC-02 — Registry Binding Carrier (registry facet)

**Class:** POC-02 (registry facet)  
**Record plane:** RT-G04 substrate — content owned by RT-G05  
**Scope:** Portfolio (LOC-ZONE)  
**Created:** 2026-06-07  
**Wave:** 2 — Portfolio & Visibility Scaffold  

---

## Role

Binding carrier for Registry catalog content classes (ROC-*). **Carrier existence ≠ content authority.** Each ROC class has a **separate physical carrier** per COL-02 class separation.

**Manifest facet (POC-02(m)):** per-project at each LOC-HOME — distinct record class from this facet (ROC-RULE-03).

---

## Physical locus (D-W2-03)

| Field | Value |
|-------|-------|
| authorized_path | `workspaces/website-factory-operations/POC-02-registry-facet/` |
| declared_in | MOC-08 topology — `../../POC-02-registry-facet/` relative to manifest |
| df09_alignment | **confirmed** — portfolio-scope registry facet at zone root |

---

## Hosted registry content index

| Class | Carrier | Status |
|-------|---------|--------|
| ROC-01 | [ROC-01-catalog-aggregate.md](ROC-01-catalog-aggregate.md) | **present** |
| ROC-02 | [entries/FP-0001/ROC-02-catalog-entry.md](entries/FP-0001/ROC-02-catalog-entry.md) | **present** |
| ROC-03 | [entries/FP-0001/ROC-03-registry-entry-identity.md](entries/FP-0001/ROC-03-registry-entry-identity.md) | **present** |
| ROC-04 | [entries/FP-0001/ROC-04-logical-identity-reference.md](entries/FP-0001/ROC-04-logical-identity-reference.md) | **present** |
| ROC-05 | [entries/FP-0001/ROC-05-manifest-pointer.md](entries/FP-0001/ROC-05-manifest-pointer.md) | **present** |
| ROC-06 | [entries/FP-0001/ROC-06-distinction-summary.md](entries/FP-0001/ROC-06-distinction-summary.md) | **present** |
| ROC-07 | [entries/FP-0001/ROC-07-discoverability-status.md](entries/FP-0001/ROC-07-discoverability-status.md) | **present** |
| ROC-08 | — | **absent** (optional — omitted at Wave 2 per R-R7) |
| ROC-09 | [entries/FP-0001/ROC-09-enrollment-bind-metadata.md](entries/FP-0001/ROC-09-enrollment-bind-metadata.md) | **present** |
| ROC-10 | [entries/FP-0001/ROC-10-amendment-narrative.md](entries/FP-0001/ROC-10-amendment-narrative.md) | **present** |

---

## Separation discipline

- Registry facet **must not** embed live POC-04/POC-05 gate or handoff indexes (RA-05, INT-R06).
- Registry facet **must not** embed MOC-* minimum understanding bodies (REL-R12).
- ATLAS org legal facts **must not** appear in ROC-06 — refs only (ENROLL-ATLAS-01).

---

*POC-02 registry facet at portfolio scope. Per-project manifest facet is a separate locus at each LOC-HOME.*
