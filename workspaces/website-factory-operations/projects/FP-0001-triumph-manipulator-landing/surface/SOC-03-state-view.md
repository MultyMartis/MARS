# SOC-03 — State View (Question #2)

**Class:** SOC-03  
**Record plane:** RT-G12 Tracking Surface  
**Question:** Where is it now?  
**Refreshed:** 2026-06-07 — Wave 3  

---

## Composed state view

| Field | Value | Authority |
|-------|-------|-----------|
| active_state_signal | **NEW_PROJECT** | POC-03 |
| lifecycle_segment | **LC-00** — intake | POC-03 |
| factory_track_status | **FACTORY_TRACK_CLOSED_PARTIAL** | POC-03 |
| halt_flag | **no** | POC-03 |
| suspension_flag | **no** | POC-03 |
| invalid_active_flag | **no** | POC-03 |
| closure_persisted | **yes** — partial | POC-08 |

---

## Read sources

| Source | Locator | Status |
|--------|---------|--------|
| POC-03 state index | [../POC-03-state-index.md](../POC-03-state-index.md) | populated |
| POC-08 closure | [../POC-08-closure.md](../POC-08-closure.md) | partial closure persisted |
| MOC-04 endpoint | [../manifest/MOC-04-endpoint.md](../manifest/MOC-04-endpoint.md) | partial endpoint NEW_PROJECT |

---

## Interpretation note

Active state remains **NEW_PROJECT** — Factory track closed partial per D-W3-01. **Not** `COMPLETE`. **Not** LC-13 terminal.

---

*Reflects POC-03 — does not invent Runtime state (SV-*).*
