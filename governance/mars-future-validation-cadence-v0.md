# MARS — Future validation and testing cadence

**Status:** **documented** — post-freeze validation strategy.  
**Date:** 2026-05-19.  
**Context:** Cycle 8 completed global validation; baseline frozen.

**Is:** when to run **targeted** human-operated reviews.  
**Is not:** test infrastructure, CI governance product, endless validation loops, or Cycle 9 by default.

**Reference passes:** Cycle 8 suite ([mars-global-ecosystem-validation-cycle-8-topology-v0.md](mars-global-ecosystem-validation-cycle-8-topology-v0.md) et al.); Phase 6 stress; Phase 7 hardening.

---

## 1. Principles

1. **Rare, targeted, high-signal** — default = lane work + REPORT.  
2. **Validation ≠ implementation proof** — [validation-chain-semantics.md](validation-chain-semantics.md).  
3. **Stabilize findings** — compress/link; do not spawn new governance architecture.  
4. **One artefact per trigger** — 1–3 pages human-written, not a programme.

---

## 2. Lightweight validation (most common)

**When:**

- Single new major system entered ([mars-future-system-entry-discipline-v0.md](mars-future-system-entry-discipline-v0.md))  
- Registry/README contradiction reported  
- Broken routing after compression pass  
- New forbidden-runtime claim suspected  
- Per merge-worthy slice: links on touched paths  

**Scope:** Affected nodes only — one pack, one index pair, one registry table.

**Output:** REPORT section or ≤1 page note; fix in same pass.

**Cadence:** **Event-driven** — not scheduled.

---

## 3. Stress testing (occasional)

**When:**

- **+5** major systems accumulated since last stress review  
- Factory Extended row count materially exceeds Core budget  
- Operator overload signals across **multiple** lanes ([operator-load-management.md](operator-load-management.md))  
- Repeated Cycle 6-class failures (breadth-first onboarding, wrong ORCA entry, Forge checklist as default)

**Scope:** Re-run **patterns** from [mars-ecosystem-stress-resilience-phase-6-review-v0.md](mars-ecosystem-stress-resilience-phase-6-review-v0.md) — onboarding paths, overload hotspots, wrong-turn catalog — **not** new taxonomy.

**Output:** Short stress note; compression targets if failed.

**Cadence:** **At most** once per major expansion cluster — not quarterly by default.

---

## 4. Topology review

**When:**

- Second major system added in one quarter without index update  
- “Where does X live?” repeats for same X  
- External bridge changes role (MetaBOT, WPilot, n8n handoff)

**Scope:** [ecosystem-topology-index.md](ecosystem-topology-index.md) + [mars-reality-index-v0.md](mars-reality-index-v0.md) coherence — pick-one Tier 1 still teachable.

**Output:** Row fixes; optional 1-page topology note if structural ambiguity found.

**Not:** ontology redesign; grouped routers (deferred until +20 failure — Cycle 8).

---

## 5. Survivability review

**When:**

- Post-large Factory/Forge/ORCA expansion  
- Core/Extended boundary blur reported  
- Session durability failures (lane switch loses SoT) — see [mars-global-ecosystem-validation-cycle-8-session-durability-v0.md](mars-global-ecosystem-validation-cycle-8-session-durability-v0.md) triggers  
- Human survivability persona fails Path A–E in practice

**Scope:** Pattern catalogue P1–P9 spot-check ([mars-survivability-patterns-hardening-v0.md](mars-survivability-patterns-hardening-v0.md)).

**Output:** Banner/INDEX adjustments; no new checklists without failure mode.

---

## 6. When **NOT** to run giant validation cycles

| Situation | Instead |
|-----------|---------|
| Routine Factory page delivery | Lane QA + REPORT |
| Single governance typo | Direct edit |
| New Cursor/tool capability | Operational experiment if needed — [operational-experiments-overview.md](operational-experiments-overview.md) |
| Anxiety after successful Cycle 8 | Maintenance mode — [mars-lightweight-maintenance-mode-v0.md](mars-lightweight-maintenance-mode-v0.md) |
| Every new governance doc | Entropy rules — no Cycle repeat |
| Automated link crawl desire | **Out of scope** — human sample |
| “Validate everything” charter absent | **Refuse** — targeted scope only |

**Full Cycle 8-class global validation** requires **explicit human charter** and **multiple** of: critical-node failure, +10 scaling without maintenance, topology/reality/registry systemic drift, post-major architecture decision (grouped routers, new Tier 1).

---

## 7. Suggested cadence matrix (non-mandatory)

| Activity | Typical frequency | Owner |
|----------|-------------------|-------|
| Lightweight validation | Per event | Task operator |
| Registry/lifecycle sync | Per status change | Task operator |
| Compression pass | After large pack expansion | Lane owner |
| Stress spot-check | +5 systems or overload cluster | Human charter |
| Topology/survivability review | Combined with stress or entry gate | Human charter |
| Global validation (Cycle 8-class) | **Rare** — years or major crisis | Explicit charter |

**No calendar automation.**

---

## 8. Validation outputs (allowed)

- REPORT closeout  
- Short `*-review-v0.md` (1–3 pages)  
- Index/registry row updates in same pass  
- IdeaBox / continuity capture for follow-up  

**Disallowed as default output:** new S-phase series, enforcement framework, validation platform narrative.

---

## 9. Success criteria

- Findings produce **actionable diffs** (link, row, banner) in same or next chartered pass.  
- Validation count **decreases** as maintenance mode matures.  
- Operational lanes (ORCA, Factory, Triumph) absorb more session time than governance.

---

*Future validation — rare, targeted, human-operated.*
