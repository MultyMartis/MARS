# WPilot Lifecycle State

**Classification:** Lifecycle registration — project phase vocabulary.  
**Date:** 2026-06-19  
**Scope:** Documentation only.

---

## Purpose

Define canonical lifecycle states for WPilot and record the current state after RC5 finalization. This document complements registry `status` / `phase` fields in [registry/project-registry.md](../../registry/project-registry.md) without creating a shadow registry.

---

## Lifecycle states

| State | Meaning |
|-------|---------|
| **Concept** | Mission, boundaries, and policy direction documented; no runtime proof. |
| **Prototype** | Plugin source and early DEV experiments; partial or unproven REST paths. |
| **Proven Runtime** | End-to-end safety loop and connection runtime proven on DEV with evidence register. |
| **Reference Implementation** | Proven runtime frozen; used as canonical template and validation source for CMS Pilot family; development focus shifted away; maintenance-only unless chartered. |
| **Maintenance** | Active bugfix, security, documentation, and compatibility work under maintenance policy; no feature expansion. |
| **Retired** | No longer maintained or referenced as active baseline; superseded or archived. |

**Note:** Reference Implementation and Maintenance may overlap in practice. Reference Implementation describes **ecosystem role**; Maintenance describes **allowed change posture**. WPilot RC5 is **Reference Implementation** with **Maintenance**-gated changes.

---

## Current state

| Field | Value |
|-------|-------|
| **Current lifecycle state** | **Reference Implementation** |
| **Authority** | `WPILOT-RC5-PROVEN-CONNECTION-RUNTIME-2026-06-19` |
| **Commit** | `648632acbdd42703427fd76a0cb1fd8d88641dcc` |
| **Release candidate** | `v0.3.0-RC5` |
| **Effective date** | 2026-06-19 |

---

## Why Reference Implementation

WPilot reached **Reference Implementation** because:

1. **Runtime proven** — plugin REST safety loop and connection runtime verified on DEV with formal evidence ([WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md)).
2. **Authority registered** — canonical authority state and commit pin established ([WPILOT-AUTHORITY-STATE-RC5.md](WPILOT-AUTHORITY-STATE-RC5.md)).
3. **RC5 closed** — development sprints complete; Sprint 3 **HOLD**; freeze **ACTIVE** ([WPILOT-FINAL-STATE-RC5.md](WPILOT-FINAL-STATE-RC5.md)).
4. **Family pattern registered** — CMS Pilot Runtime Pattern v1 cites WPilot RC5 as proven reference ([CMS-PILOT-RUNTIME-PATTERN-v1.md](../shared/runtime-patterns/CMS-PILOT-RUNTIME-PATTERN-v1.md)).
5. **Ecosystem role shifted** — WPilot is the **first proven CMS Pilot runtime reference implementation** in MARS, not an active MVP development target.

Future CMS pilots (OCPilot, others) should compare against WPilot evidence and limits — not inherit WordPress proof automatically.

---

## State history (summary)

| Period | State | Notes |
|--------|-------|-------|
| Pre-2026-06 | Concept → Prototype | Phase 1 MVP docs; policy stack; early DEV work |
| 2026-06-19 (sprints) | Proven Runtime | Runtime Proof + Prototype Sprints; MILESTONE-001 |
| 2026-06-19 (RC5) | Proven Runtime + authority | Connection proof; authority registration; ecosystem sync |
| 2026-06-19 (finalization) | **Reference Implementation** | MILESTONE-002; maintenance policy; development focus closed |

---

## Transitions (normative)

| From | To | Requires |
|------|-----|----------|
| Concept | Prototype | Documented charter + initial implementation |
| Prototype | Proven Runtime | Completed DEV proof + evidence register update |
| Proven Runtime | Reference Implementation | Authority registration + freeze + finalization milestone |
| Reference Implementation | Maintenance (ongoing) | Default posture under [WPILOT-MAINTENANCE-POLICY-v1.md](WPILOT-MAINTENANCE-POLICY-v1.md) |
| Reference Implementation | Proven Runtime (re-expansion) | Explicit HITL charter unfreezing Sprint 3 or new capabilities |
| Any | Retired | Explicit operator decision; superseding baseline documented |

**Sprint 3** does not auto-start from Reference Implementation. Charter required.

---

## Related documents

| Document | Role |
|----------|------|
| [WPILOT-FINAL-STATE-RC5.md](WPILOT-FINAL-STATE-RC5.md) | Final state summary |
| [WPILOT-MAINTENANCE-POLICY-v1.md](WPILOT-MAINTENANCE-POLICY-v1.md) | Allowed changes |
| [milestones/WPILOT-MILESTONE-002-RC5-FINALIZATION.md](milestones/WPILOT-MILESTONE-002-RC5-FINALIZATION.md) | Closure milestone |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |

---

*WPilot Lifecycle State · Reference Implementation · 2026-06-19.*
