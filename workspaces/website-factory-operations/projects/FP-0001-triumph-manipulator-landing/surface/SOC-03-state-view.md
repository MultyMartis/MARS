# SOC-03 — State View (Question #2)

**Class:** SOC-03  
**Record plane:** RT-G12 Tracking Surface  
**Question:** Where is it now?  
**Created:** 2026-06-07  

---

## Composed state view

| Field | Value | Authority |
|-------|-------|-----------|
| active_state_signal | **NEW_PROJECT** | POC-03 *(empty shell — empty-allowed)* |
| lifecycle_segment | *not declared* | POC-03 — awaiting Playbook 04 |
| halt_flag | **no** | POC-03 — no halt declared |
| suspension_flag | **no** | POC-03 — no suspension declared |
| invalid_active_flag | **no** | POC-03 |

---

## Read sources

| Source | Locator | Status |
|--------|---------|--------|
| POC-03 state index | [../POC-03-state-index.md](../POC-03-state-index.md) | empty shell — NEW_PROJECT posture |
| MOC-04 endpoint orientation | [../manifest/MOC-04-endpoint.md](../manifest/MOC-04-endpoint.md) | intake NEW_PROJECT noted |

---

## Empty-allowed signal (W2-SCOPE-02)

At Wave 2 gate, POC-03 is an **empty shell**. Orientation category **NEW_PROJECT** is visible from scaffold posture — authoritative active state **awaits** Playbook 04 (Wave 3).

---

*Reflects POC-03 — does not invent Runtime state (SV-*).*
