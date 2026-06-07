# POC-02 — Manifest Binding Carrier (manifest facet)

**Class:** POC-02 (manifest facet)  
**Record plane:** RT-G04 substrate — content owned by RT-G10  
**Scope:** Project (LOC-HOME)  
**Created:** 2026-06-07  

---

## Role

Binding carrier for Manifest content classes (MOC-*). **Carrier existence ≠ content authority.** Each MOC class has a **separate physical carrier** per COL-02 class separation.

**Registry facet (POC-02(r)):** not materialized — deferred to Wave 2 (RT-G05).

---

## Hosted manifest content index

| Class | Carrier | Status |
|-------|---------|--------|
| MOC-01 | [manifest/MOC-01-entry-anchor.md](manifest/MOC-01-entry-anchor.md) | **present** |
| MOC-02 | [manifest/MOC-02-identity.md](manifest/MOC-02-identity.md) | **present** |
| MOC-03 | [manifest/MOC-03-scope.md](manifest/MOC-03-scope.md) | **present** |
| MOC-04 | [manifest/MOC-04-endpoint.md](manifest/MOC-04-endpoint.md) | **present** |
| MOC-05 | [manifest/MOC-05-applicability.md](manifest/MOC-05-applicability.md) | **present** |
| MOC-06 | [manifest/MOC-06-classification.md](manifest/MOC-06-classification.md) | **present** |
| MOC-07 | — | **absent** (optional — pointer-only when present) |
| MOC-08 | [manifest/MOC-08-topology.md](manifest/MOC-08-topology.md) | **present** |
| MOC-09 | — | **absent** (optional — foundation pins not declared) |
| MOC-10 | [manifest/MOC-10-enrollment.md](manifest/MOC-10-enrollment.md) | **present** |
| MOC-11 | — | **absent** (no amendments yet) |
| MOC-12 | [manifest/MOC-12-external-refs.md](manifest/MOC-12-external-refs.md) | **present** |

---

## Separation discipline

- Manifest facet **must not** embed live POC-04/POC-05 gate or handoff indexes (MT-01).
- Tracking indexes POC-03…POC-07 **deferred** to Wave 2 — separate record classes when created.

---

*POC-02 manifest facet at project scope. Portfolio registry facet is a separate locus (Wave 2).*
