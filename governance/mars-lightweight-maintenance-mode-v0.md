# MARS — Lightweight maintenance mode (post-freeze)

**Status:** **documented** — operational hygiene after governance baseline freeze.  
**Date:** 2026-05-19.  
**Supersedes for daily ops:** ambient “stabilization programme” mindset — **not** the Phase 3 artefact set (those remain **reference**).

**Builds on:** [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md), [mars-governance-baseline-freeze-v0.md](mars-governance-baseline-freeze-v0.md).

**Is:** minimal triggers for human-operated upkeep.  
**Is not:** ticketing, calendars, committees, registry engines, or governance waves.

---

## 1. Mode definition

**Maintenance mode** = governance and survivability docs are **frozen baseline**; energy shifts to **operational systems** (see [mars-operational-first-priority-v0.md](mars-operational-first-priority-v0.md)).

Default action on friction: **compress, link, reconcile** — not **author new governance architecture**.

---

## 2. Periodic review (light touch)

| Item | When | Max effort |
|------|------|------------|
| **Registry ↔ prose ids** | After any new agent/project/tool id in work | One minimal row |
| **Broken links** on touched paths | Per merge-worthy slice | Fix only edited neighbourhood |
| **OPERATIONAL-INDEX Core Run** | Factory/ORCA lane active monthly+ | Spot-check ≤10 Core rows still true |
| **Operator load** | Fatigue signals | [operator-load-management.md](operator-load-management.md) — 15 min self-check |
| **governance/README** | Before adding a new governance file | Ask: **row instead of file?** |

**No standing review calendar** — triggers are **event-driven**.

---

## 3. Compression triggers

Run a **compression pass** (not a governance wave) when:

- Pack OPERATIONAL-INDEX or README grows without a **new operational failure mode**
- Duplicate triads (governance + taxonomy + model) for the same concern
- Checklist fatigue reported ([survivability-documentation-fatigue-review-v0.md](survivability-documentation-fatigue-review-v0.md))
- Factory Extended becomes the **default** read path
- Cycle 8 **+5** growth threshold approached ([mars-global-ecosystem-validation-cycle-8-future-growth-v0.md](mars-global-ecosystem-validation-cycle-8-future-growth-v0.md))

**Output:** index tiers, dedupe rows, banners — **1–2 page human note** or REPORT section.

---

## 4. Validation triggers

| Trigger | Validation type |
|---------|-----------------|
| New **major pack** or external bridge registered | Targeted topology + reality row check |
| Contradictory status claims across registry/README | Lightweight consistency spot-check |
| Post-large Factory/Forge/ORCA expansion | Lane-specific survivability spot-check |
| Operator reports “cannot find SoT in 10 min” | Onboarding path audit (Path A–E) |
| Mythology pressure in new docs | [reality-vs-mythology-warnings.md](reality-vs-mythology-warnings.md) triage |

**Do not** run full Cycle 8 global validation unless **multiple** critical-node failures or human charter.

Details: [mars-future-validation-cadence-v0.md](mars-future-validation-cadence-v0.md).

---

## 5. Registry sync triggers

Sync when:

- New `project_id`, agent id, or tool id used in prose **without** registry row
- Card or pack README claims **active** but registry says `planned`
- External system boundary changes ([external-system-boundaries.md](external-system-boundaries.md))

**Action:** one row per [registry-entry-minimal-standard.md](registry-entry-minimal-standard.md) — **same human pass** as the doc that introduced the id.

---

## 6. Lifecycle sync triggers

Sync when:

- `master-build-map.md` stage claim changes
- Milestone recorded in task charter but lifecycle log silent
- Status bucket changes (operational → experimental, etc.)

**Action:** update `logs/lifecycle-log.md` and/or map in **one pass** — [lifecycle-synchronization-review-v0.md](lifecycle-synchronization-review-v0.md) pattern.

---

## 7. Topology review triggers

Update [ecosystem-topology-index.md](ecosystem-topology-index.md) + [mars-reality-index-v0.md](mars-reality-index-v0.md) when:

- New **major system** enters ecosystem (charter + entry discipline)
- Repeated “where does X live?” without answer in indexes
- Lane assignment changes for ORCA, Factory, MetaBOT, WPilot, Triumph-class delivery

**Rule:** **one row each** — no new parallel map.

---

## 8. What does **NOT** trigger a governance wave

| Non-trigger | Instead |
|-------------|---------|
| Single broken link | Fix link |
| One new Factory governance doc | OPERATIONAL-INDEX row + link |
| Routine Factory/ORCA production task | Lane INDEX + REPORT |
| Cosmetic README drift | Edit authoritative file |
| “We should document philosophy of X” | Check entropy rules; link existing |
| Periodic anxiety about scale | Check +3 checklist; compress if +5 |
| Desire for automated enforcement | **Out of scope** — documentation discipline only |
| New Cursor feature / tool hype | [operationalization-drift-warnings.md](operationalization-drift-warnings.md) |

**Red flags for wave creep:** new doc titles with framework / engine / platform / ontology without implementation proof.

---

## 9. Escalation (human only)

| Situation | Action |
|-----------|--------|
| Conflicting SoT | SAFE UNKNOWN → [registry-source-of-truth.md](registry-source-of-truth.md) |
| Expansion vs stabilization dispute | **Stabilize** ([stabilization-vs-expansion.md](stabilization-vs-expansion.md)) |
| Prune / delete | Explicit user instruction + lifecycle note |
| Needs global re-validation | Charter + [mars-future-validation-cadence-v0.md](mars-future-validation-cadence-v0.md) |

---

## 10. Success / failure signals

**Success:** new operator reaches one authoritative file in &lt;10 min; Core Run row count grows slower than governance triads; registries match active ids.

**Failure (entropy returning):** parallel architecture initiatives; new taxonomies without failure mode; chat-only handoffs; experimental R1 described as product runtime.

---

*Maintenance mode — human-operated; production-first evolution.*
