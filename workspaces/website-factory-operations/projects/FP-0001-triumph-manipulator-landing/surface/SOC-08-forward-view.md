# SOC-08 — Forward View (Question #7)

**Class:** SOC-08  
**Record plane:** RT-G12 Tracking Surface  
**Question:** What should happen next?  
**Created:** 2026-06-07  

---

## Composed forward eligibility (derived — does not execute)

| Field | Value |
|-------|-------|
| next_eligible_action | **first Playbook 04 declaration cycle** |
| blocked_with_cause | **no** — no open blockers in empty indexes |
| transition_execution | **forbidden here** — Surface enables declare decision only (OA-01) |
| recommended_operator_path | Wave 3 — Playbook 04 population when separately authorized |

---

## Derivation chain

```text
  SOC-04 (no blockers) + MOC-04 (factory_terminal_closure) + POC-03 (NEW_PROJECT)
       → first declaration eligible when operator chooses Wave 3 entry
```

---

## Read sources

| Source | Role |
|--------|------|
| [SOC-04-blocking-view.md](SOC-04-blocking-view.md) | Eligibility input |
| [../manifest/MOC-04-endpoint.md](../manifest/MOC-04-endpoint.md) | Endpoint context |
| [../POC-03-state-index.md](../POC-03-state-index.md) | Active posture |

---

*Derived forward view — does not execute transitions or declare on behalf of operator.*
