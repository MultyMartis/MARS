# MARS — Operational hygiene hardening (Phase 7)

**Status:** **documented** — discipline reinforcement only.  
**Date:** 2026-05-19.  
**Builds on:** [operational-survivability.md](operational-survivability.md), [context-continuity-rules.md](context-continuity-rules.md), [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md).

**Is:** compact operator habits that **strengthen durability** after stress testing.  
**Is not:** process overload, ticketing, automation, or governance expansion.

---

## 1. Core hygiene habits (keep)

| Habit | Rule | Authoritative link |
|-------|------|-------------------|
| **REPORT discipline** | Non-trivial tasks end with `# REPORT — …`; changed files, summary, git status, SAFE UNKNOWN | [AGENTS.md](../AGENTS.md), [context-continuity-rules.md](context-continuity-rules.md) |
| **Lane discipline** | Declare production vs MARS-core lane; no Lane A/B doc mix without charter | [parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md) |
| **Topology sync** | New entity → **one row** in [ecosystem-topology-index.md](ecosystem-topology-index.md) | Not a new map |
| **Reality sync** | Same entity → **one row** in [mars-reality-index-v0.md](mars-reality-index-v0.md) | Pick-one with topology per session |
| **Registry sync** | New `agent_id` / `project_id` → minimal registry row in **same pass** as prose | [registry-entry-minimal-standard.md](registry-entry-minimal-standard.md) |
| **Lifecycle sync** | Stage claims ↔ `logs/lifecycle-log.md` in **one human pass** | [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md) |
| **Onboarding discipline** | Path A: 4 files + stop; lane path B–E when assigned | [onboarding-survivability.md](onboarding-survivability.md) |
| **Anti-drift habits** | Three-way split; no runtime claims without evidence; enforcement = human cues | [AGENTS.md](../AGENTS.md), [enforcement/README.md](enforcement/README.md) |
| **No chat-memory as SoT** | Decisions live in REPORT, lifecycle, continuity, or registry — not session recall alone | [context-continuity-rules.md](context-continuity-rules.md) |

---

## 2. Session header (recommended pin)

Paste at top of long or multi-switch sessions:

```text
Lane: [production | MARS-core]
Tier 1 router: [topology | reality | onboarding | governance-one-row]
Pack INDEX row: [one Core Run / FAST PATH concern]
STOP rule: [4-file | ORCA FAST PATH | Factory one-row]
```

**Effort:** trivial. **Target:** context-switch fatigue ([mars-ecosystem-stress-resilience-phase-6-review-v0.md](mars-ecosystem-stress-resilience-phase-6-review-v0.md) Task D).

---

## 3. Sync checkpoints (when to act)

| Situation | Minimum action |
|-----------|----------------|
| Added agent or project | Registry row + card if applicable + topology row |
| Changed operational status | Reality index row + pack README status line |
| Closed documentation milestone | lifecycle log + master-build-map in same pass |
| Major routing pass | Update banners only where wrong-turn proven — no new index |
| Parallel chats | Separate lane; no cross-pack edits without explicit scope |

---

## 4. What NOT to add (anti-bureaucracy)

- Standing review committees or mandatory weekly governance reads.  
- Automated “compliance” scripts presented as enforcement products.  
- New `*-discipline.md` for one-line fixes — edit authoritative file.  
- Duplicate REPORT indexes per chat — use [continuity/README.md](../continuity/README.md) when filesystem continuity is chosen.  
- Sixth Tier 1 router — retire or merge instead.

---

## 5. Failure modes (hygiene breaks)

| Break | Symptom | Recovery |
|-------|---------|----------|
| Skipped REPORT | Next session reinvents decisions | Write retrospective REPORT; lifecycle line if milestone |
| Registry without lifecycle | Claim vs evidence gap | Backfill minimal lifecycle event |
| Lane mix | Factory governance edited during ORCA live review | Re-scope session; pin lane header |
| README-only identity | Card/registry lag | registry-source-of-truth reconciliation |
| Chat-only decision | Silent drift | Promote to REPORT or continuity artifact |

---

## 6. Relation to survivability patterns

Operational hygiene **implements** [mars-survivability-patterns-hardening-v0.md](mars-survivability-patterns-hardening-v0.md) in daily work — patterns without hygiene still fail under volume.

---

## 7. SAFE UNKNOWN

No tool verifies hygiene automatically. Operator self-check and peer review only.
