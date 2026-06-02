# EAR Next Stage v1

**Type:** Transition recommendation — planning only  
**Date:** 2026-06-01  
**Prior stage:** EAR Architecture Program — **COMPLETE** (frozen)  
**Next stage:** EAR Runtime Program — **NOT STARTED**

---

## Primary objective shift

| Before freeze | After freeze |
|---------------|--------------|
| Architecture completeness, pilot charters, readiness assessments | **Runtime Engineering** — human-operated helpers implementing documented contracts |
| Default deliverable: markdown design | Default deliverable: **chartered** code/helpers **outside** architecture expansion |

Further architecture work is **exception**, not default (see [EAR-RUNTIME-BOUNDARY-v1.md](../../EAR-RUNTIME-BOUNDARY-v1.md)).

---

## Recommended next step (single)

**Authorize and draft: EAR Runtime v1 Engineering Charter**

| Charter element | Source material |
|-----------------|-----------------|
| Scope | [EAR-RUNTIME-BACKLOG-v1.md](../../EAR-RUNTIME-BACKLOG-v1.md) R1–R5 |
| Boundaries | [EAR-RUNTIME-BOUNDARY-v1.md](../../EAR-RUNTIME-BOUNDARY-v1.md) |
| Handoff | [EAR-RUNTIME-HANDOFF-v1.md](EAR-RUNTIME-HANDOFF-v1.md) |
| First reference pilot | PILOT-001 (no Execution until separately authorized) |
| Exclusions policy | [EAR-DEFAULT-EXCLUSIONS-v1.md](../../EAR-DEFAULT-EXCLUSIONS-v1.md) |

**Charter must state:** documentation-only phases are closed; implementation is in-scope **only** as named backlog items.

---

## Parallel operator track (not runtime code)

These remain **human-operated** and may proceed without runtime:

| Track | Action |
|-------|--------|
| PILOT-001 governance | Phase 7 Execution Preparation Review per [PHASE-6-DECISION-v1.md](../../pilots/PILOT-001-SITE-001-SFTP-READONLY/PHASE-6-DECISION-v1.md) |
| Sub-charter sign-off | Resolve §4 SAFE UNKNOWN bindings |
| Implementation Authorization | Sub-charter §10 — human sign-off |

**Execution Authorization** remains a **separate** gate after runtime helpers exist (or dry-run path defined in charter).

---

## What not to do next (default)

| Action | Why avoided |
|--------|-------------|
| New architecture phase (2F, 3B, etc.) without amendment | Freeze — architecture creep |
| Live SFTP under PILOT-001 without Execution Authorization | Governance violation |
| Claim EAR “runtime exists” when only docs exist | Status honesty |
| Merge OCPilot analysis into EAR acquisition | Layer violation |

---

## Success criteria for “Runtime Program started”

Runtime Program is **STARTED** when **all** are true:

1. Human-approved **EAR Runtime v1 Engineering Charter** exists (may live outside this folder).
2. Charter references frozen architecture version (`EAR-RUNTIME-TRANSITION-v1` / freeze date).
3. At least one backlog item (typically **R1**) is explicitly in-scope for implementation work.
4. OPERATIONAL-INDEX updated: Runtime Program status ≠ NOT STARTED.

Until then, status remains **NOT STARTED** per [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md).

---

## Longer horizon (not committed)

| Item | Program |
|------|---------|
| WordPress / WPilot Mode 2 | Future EAR roadmap (EAR-ROADMAP numbering) |
| Unified snapshot schema v2 | Post–Runtime v1 lessons |
| Additional pilots | Separate pilot charters |
| Mode 3 evaluation | Explicitly deferred — [EAR-NON-GOALS-v1.md](../../EAR-NON-GOALS-v1.md) |

---

## Entry checklist for charter author

- [ ] Read [EAR-STATE-SUMMARY-v1.md](EAR-STATE-SUMMARY-v1.md)
- [ ] Read [EAR-RUNTIME-HANDOFF-v1.md](EAR-RUNTIME-HANDOFF-v1.md)
- [ ] Read [EAR-RUNTIME-BACKLOG-v1.md](../../EAR-RUNTIME-BACKLOG-v1.md)
- [ ] Confirm PILOT-001 execution still **NOT AUTHORIZED**
- [ ] Confirm no secrets committed to MARS git
- [ ] Name artifact location for runtime code (repo vs external) — resolves U-08 from Phase 6
