# MARS — Long-session durability validation (Cycle 8)

**Status:** **documented** — Task D simulation of fatigue, switching, and orientation loss.  
**Date:** 2026-05-19.  
**Builds on:** Phase 6 operator overload test; Phase 7 operational hygiene hardening.

**Method:** Scenario walk-through of REPORT chains, lane switching, and overlap zones — **not** live operator telemetry.

---

## Simulated scenarios

| Scenario | Pressure | Durability finding |
|----------|----------|-------------------|
| **Long REPORT chains** (5+ tasks, same chat) | Context window + prior decisions | **Degrades** — no canonical REPORT index; continuity master-index empty |
| **Repeated context switching** (Factory → ORCA → governance) | Tier 1 re-pick; INDEX row re-derivation | **Med** — survivable with session header template (proposed Phase 6, not productized) |
| **Lane switching pressure** (Lane A/B) | Wrong pack edits | **Med** — parallel-cursor doc mitigates if read once |
| **Governance + ORCA overlap** | Dual vocabulary (validation, operational) | **Med** — REPORT must state validation class |
| **Factory + Forge overlap** | Three SoT surfaces | **Med–Strong** — foundation map hardened; fatigue opens overlay-as-SoT |
| **External-system overlap** (MetaBOT n8n + WPilot WP) | Execution truth outside repo | **Strong** boundaries — operator must not infer in-repo runtime |

---

## Fatigue degradation checklist

| Signal under fatigue | Observed risk | Mitigation (existing) |
|---------------------|---------------|------------------------|
| Skip Tier 0 honesty | Mythology claims in REPORT | AGENTS closeout |
| Open “just one more” doc | ORCA/Factory loops | STOP NOW, Extended STOP |
| Treat Extended as Core | Factory overload | INDEX header |
| Re-explain Tier model each prompt | Token + attention cost | Phase 7 patterns catalogue |
| Skip lifecycle on registry edit | Drift | registry-source-of-truth rule |
| Use chat memory as SoT | Silent drift | context-continuity-rules |

---

## Routing degradation under session fatigue

| Tier | Fatigue behavior | Resilience |
|------|------------------|------------|
| **Tier 0** | Usually retained | **Strong** |
| **Tier 1** | Often violated (read both indexes) | **Weak** under fatigue |
| **Tier 2** | Collapses to “search repo” | **Med** |
| **Tier 3** | Becomes default (catalog browsing) | **Weak** |

**Semantic drift accumulation:** **High** in long chats without REPORT promotion to lifecycle/continuity — chat is **not** governance SoT.

**Loss of operational orientation:** **High** after 3+ lane switches without pinned lane + INDEX row.

**Memory overload pressure:** **High** for governance-heavy + Factory Extended in same week.

---

## Durability verdict (Task D)

**Med–Strong** for single-lane, STOP-disciplined sessions (ORCA live, Factory Core).

**Weak** for multi-lane, multi-day threads without explicit continuity hygiene.

**Recommended operator habits (no new bureaucracy):**

1. Pin: `lane` + one Tier 1 router + one OPERATIONAL-INDEX row.  
2. End segment with REPORT; promote decisions to continuity or lifecycle when registry-affecting.  
3. Hard-stop at Tier 3 unless contract citation exists.  
4. Split chat when second major pack appears (ORCA + Factory same thread).

---

## Related (Cycle 8)

- [context-continuity-rules.md](context-continuity-rules.md)  
- [mars-operational-hygiene-hardening-v0.md](mars-operational-hygiene-hardening-v0.md)

---

*Cycle 8 Task D — session durability only.*
