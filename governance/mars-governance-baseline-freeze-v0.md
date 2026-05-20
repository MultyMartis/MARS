# MARS — Governance baseline freeze (post Cycles 1–8)

**Status:** **documented** — frozen baseline for controlled operational evolution.  
**Date:** 2026-05-19.  
**Effective:** After Cycle 8 global validation; governance enters **maintenance mode** (see [mars-lightweight-maintenance-mode-v0.md](mars-lightweight-maintenance-mode-v0.md)).

**Is:** a compact **freeze record** — what is stable, canonical, and accepted.  
**Is not:** a new governance wave, architecture redesign, runtime product, or enforcement framework.

**Cycles covered (human-operated passes):**

| Cycle | Scope | Primary artefacts |
|-------|--------|-------------------|
| **1** | Structural stabilization | [ecosystem-topology-index.md](ecosystem-topology-index.md), [mars-forge-transition-stabilization-v0.md](mars-forge-transition-stabilization-v0.md), [website-factory-compression-review-v0.md](website-factory-compression-review-v0.md) |
| **2** | Reality + lifecycle alignment | [mars-reality-index-v0.md](mars-reality-index-v0.md), [lifecycle-synchronization-review-v0.md](lifecycle-synchronization-review-v0.md), navigation compression |
| **3** | Survivability maintenance model | Tier 0–3 entry, onboarding paths A–E, [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md) |
| **4** | Editorial compression | [editorial-compression-pass-4-operator-fatigue-review-v0.md](editorial-compression-pass-4-operator-fatigue-review-v0.md) |
| **5** | Consistency pass | [mars-consistency-survivability-pass-5-review-v0.md](mars-consistency-survivability-pass-5-review-v0.md) |
| **6** | Ecosystem stress validation | [mars-ecosystem-stress-resilience-phase-6-review-v0.md](mars-ecosystem-stress-resilience-phase-6-review-v0.md) |
| **7** | Hardening + scaling projection | [mars-survivability-patterns-hardening-v0.md](mars-survivability-patterns-hardening-v0.md), scaling readiness |
| **8** | Global validation | [mars-global-ecosystem-validation-cycle-8-topology-v0.md](mars-global-ecosystem-validation-cycle-8-topology-v0.md) (+ critical nodes, human, session, growth) |

---

## 1. What is now considered stable

| Domain | Stable posture |
|--------|----------------|
| **Honesty chain** | [AGENTS.md](../AGENTS.md) → registries → pack OPERATIONAL-INDEX — **Pass** (Cycle 8) |
| **Tier 0–3 routing** | Entry model + pick-one Tier 1 — **operational** for human/Cursor work |
| **Topology ↔ reality ↔ registry** | Aligned for major entities; minor lag acceptable if lifecycle-caught |
| **Factory Core / Extended** | Core Run = session default; Extended = on-demand |
| **ORCA live-first** | OPERATIONAL-INDEX FAST PATH + STOP |
| **Forge overlay** | Pack exists; foundation-map wins over scattered re-derivation |
| **Runtime boundary** | `mars-runtime/` = R1 experimental only; no product runtime claimed |
| **Phases S1–S7 + reality audit** | **Semantics frozen** — extend only via explicit charter, not ambient sprawl |
| **MARS core role** | Documentation-first contracts + human-operated evolution — **not** shipped platform |

**Not stable (by design):** external runtimes (n8n, ad platforms), deployment proof, operator headcount, undocumented chat state.

---

## 2. Canonical governance patterns

| Pattern | Rule |
|---------|------|
| **Three-way split** | Documented vs planned vs legacy — always |
| **Registry precedence** | [registry-source-of-truth.md](registry-source-of-truth.md) over README prose |
| **Documentation-only enforcement** | [enforcement/](enforcement/README.md) — human discipline, **not** CI/policy engine |
| **Stabilize before expand** | [stabilization-vs-expansion.md](stabilization-vs-expansion.md) — default **stabilize** post-freeze |
| **Entropy control** | [documentation-entropy-rules.md](documentation-entropy-rules.md) — index row before new philosophy |
| **Execution contracts S4** | Envelope → execute → REPORT → validation (human meaning) |
| **No governance wave** | Post-freeze edits = **maintenance**, not new S-phase programmes without human charter |

---

## 3. Canonical survivability patterns

Formal catalogue: [mars-survivability-patterns-hardening-v0.md](mars-survivability-patterns-hardening-v0.md) (P1–P9).

**Frozen minimum:**

- **P1** Tier 0–3 routing  
- **P2** Factory Core / Extended  
- **P3** ORCA live-first INDEX  
- **P4** Foundation-map dedupe (Gulp ↔ Forge ↔ Factory)  
- **P5–P6** One Tier 1 router per session (topology **or** reality)  
- **P7** Forge transition notes authoritative  
- **P8** AGENTS precedence on status claims  
- **P9** Path A–E onboarding + STOP discipline  

**Pillars:** [operational-survivability.md](operational-survivability.md) — continuity, anti-drift, anti-overload, anti-fragmentation, anti-fake-runtime.

---

## 4. Canonical routing patterns

| Tier | Surface | Use |
|------|---------|-----|
| **0** | AGENTS.md | Honesty, scope, closeout |
| **1** (pick **one**) | topology **or** reality **or** governance README row **or** onboarding row | Placement / bucket / one concern |
| **2** | Pack OPERATIONAL-INDEX **Core Run** | Session SoT (Factory, ORCA) |
| **3** | Extended governance, Forge checklists, deep semantics | On-demand only |

**Lane paths:** [survivability-onboarding-strategy-v0.md](survivability-onboarding-strategy-v0.md) (A–E).  
**Anti-pattern:** breadth-first Tier 1 × 4 + full pack index — confirmed collapse trigger (Cycles 6–8).

---

## 5. Canonical anti-drift patterns

| Drift type | Control |
|------------|---------|
| **Runtime mythology** | [enforcement/forbidden-runtime-claims.md](enforcement/forbidden-runtime-claims.md), [runtime-registry-boundaries.md](runtime-registry-boundaries.md) |
| **Registry ≠ prose** | Minimal row + same-pass sync — [registry-entry-minimal-standard.md](registry-entry-minimal-standard.md) |
| **Terminology** | [canonical-terminology-registry.md](canonical-terminology-registry.md), [enforcement/terminology-boundaries.md](enforcement/terminology-boundaries.md) |
| **Chat-only SoT** | REPORT + lifecycle / continuity — [context-continuity-rules.md](context-continuity-rules.md) |
| **Legacy first-read** | web-gpt-sources subordinate to governance |
| **Production proof from reference cases** | Triumph / reference = methodology stress — **not** Factory engine proof |

---

## 6. Accepted scaling assumptions

From Cycle 8 + Phase 7 (frozen until disproven by evidence):

| Scale | Assumption |
|-------|------------|
| **+3 systems** | **Safe** if [mars-future-system-entry-discipline-v0.md](mars-future-system-entry-discipline-v0.md) checklist followed |
| **+5 systems** | **Marginal** — compression pass required |
| **+10 systems** | **Not safe** without maintenance programme + row caps |
| **+20 systems** | **Not safe** — flat indexes fail; grouped routers = **future architecture decision**, not freeze-scope |

**First collapse surfaces (ordered):** topology + reality indexes → governance/README → Factory Extended → ORCA doc-map → registry lag.

---

## 7. Freeze boundaries (what changes require charter)

| Allowed without wave | Requires explicit human charter |
|----------------------|----------------------------------|
| Registry row, link fix, banner | New Tier 1 router |
| OPERATIONAL-INDEX row (Core budget) | New S-phase programme doc series |
| One topology + one reality row | New meta-governance triad |
| REPORT / lifecycle line | Architecture redesign |
| Targeted validation artefact | Full Cycle 9-style global validation |

---

## 8. Authoritative index (post-freeze)

| Need | File |
|------|------|
| Operational evolution transition | This file + [mars-operational-evolution-transition-index-v0.md](mars-operational-evolution-transition-index-v0.md) |
| Maintenance mode | [mars-lightweight-maintenance-mode-v0.md](mars-lightweight-maintenance-mode-v0.md) |
| Production priority | [mars-operational-first-priority-v0.md](mars-operational-first-priority-v0.md) |
| New system entry | [mars-future-system-entry-discipline-v0.md](mars-future-system-entry-discipline-v0.md) |
| Validation cadence | [mars-future-validation-cadence-v0.md](mars-future-validation-cadence-v0.md) |

---

*Frozen baseline — human-operated; no runtime or enforcement product implied.*
