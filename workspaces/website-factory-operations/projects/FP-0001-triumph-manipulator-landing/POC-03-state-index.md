# POC-03 — State Index

**Class:** POC-03  
**Record plane:** RT-G04 Persistence Substrate  
**LOC-HOME:** `projects/FP-0001-triumph-manipulator-landing/`  
**Created:** 2026-06-07  
**Wave:** 3 — populated via Playbook 04  

---

## Posture

| Field | Value |
|-------|-------|
| index_status | **populated** |
| active_state_category | **NEW_PROJECT** |
| lifecycle_segment | **LC-00** — intake |
| factory_track_status | **FACTORY_TRACK_CLOSED_PARTIAL** |
| invalid_active_flag | **no** |
| halt_flag | **no** |
| suspension_flag | **no** |
| write_authority | Playbook 04 only |

---

## Active state instance

| Field | Value |
|-------|-------|
| active_state_code | **NEW_PROJECT** |
| declared_by | Factory program operator |
| last_declaration_ref | [DEC-0002](POC-06-declarations/DEC-0002-closure-declaration-partial.md) |
| closure_record_ref | [POC-08-closure.md](POC-08-closure.md) |
| closure_declaration_ref | [DEC-0002](POC-06-declarations/DEC-0002-closure-declaration-partial.md) |

---

## State history

| Event | Date | State | Declaration ref |
|-------|------|-------|-----------------|
| Wave 2 scaffold | 2026-06-07 | NEW_PROJECT | *empty shell — orientation only* |
| LED-0001 | 2026-06-07 | NEW_PROJECT | [DEC-0001](POC-06-declarations/DEC-0001-lifecycle-interpretation-mvp-readiness.md) |
| LED-0002 | 2026-06-07 | NEW_PROJECT + FACTORY_TRACK_CLOSED_PARTIAL | [DEC-0002](POC-06-declarations/DEC-0002-closure-declaration-partial.md) |

---

## Manifest alignment note

MOC-04 partial endpoint **NEW_PROJECT** acknowledged per D-W3-01. Active state **not** progressed through LC-13 chain — partial closure at MVP demonstration boundary only.

---

*Authoritative active state. Last Playbook 04 act wins (INT-03). No fabricated progression history.*
