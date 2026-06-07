# ROC-03 — Registry Entry Identity

**Class:** ROC-03  
**Record plane:** RT-G05 Registry  
**Catalog entry:** FP-0001 slot  
**Created:** 2026-06-07  

---

## Registry entry identifier (D-W2-04)

| Field | Value |
|-------|-------|
| registry_entry_id | **REG-0001** |
| catalog_slot_status | **bound** |
| assignment_authority | Factory program operator |
| assignment_date | 2026-06-07 |

---

## Distinction guard

| Entity | ID | Role |
|--------|-----|------|
| **Registry entry** (this record) | REG-0001 | Catalog index slot — Factory-owned |
| **Factory Project** (logical identity) | FP-0001 | Referenced via ROC-04 — **not** this ID |
| **ATLAS Project** (structural) | PRJ-0008 | MOC-12 ref only — **not** this ID |

---

*Registry entry ID is distinct from logical Factory Project identity (RA-03, RRDY-03).*
