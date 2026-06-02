# MARS — Operational survivability

**Status:** **documented** — governance-only, Phase S3. **Not** runtime, **not** automation, **not** a substitute for [AGENTS.md](../AGENTS.md) honesty rules.

**Purpose:** Define what **operational survivability** means for MARS: how the repo and its operators stay coherent over time without pretending that tooling or “systems” replace human judgment.

---

## 1. Definition

**Operational survivability** is the ability of MARS (as a **human-operated**, **documentation-first**, **evolving governance** corpus) to:

- keep work **continuous** across sessions and people without inventing fake persistence;
- resist **drift** between claims, registries, and evidence;
- avoid **overload** of operators and contributors;
- limit **fragmentation** of workflows, lanes, and vocabulary;
- avoid **fake-runtime** narratives (see [enforcement/forbidden-runtime-claims.md](enforcement/forbidden-runtime-claims.md), [runtime-registry-boundaries.md](runtime-registry-boundaries.md)).

MARS is **not** asserted here as an autonomous product. It is a **governed documentation and design** space with **optional** narrow experimental code paths that must not silently redefine governance.

---

## 2. Pillars (minimal)

| Pillar | Meaning |
|--------|---------|
| **Continuity** | The next session can find **what was decided**, **what is unknown**, and **what lane** applies — via indexes, registries, lifecycle notes, and honest REPORT-style closeouts — without assuming chat memory or automated sync. |
| **Anti-drift** | Terminology, registry rows, and contracts stay aligned through **human** edits and precedence rules ([registry-source-of-truth.md](registry-source-of-truth.md)); contradictions are **visible**, not buried. |
| **Anti-overload** | Fewer mandatory reads, clearer optional/historical layers, and explicit “do not open yet” boundaries ([operator-load-management.md](operator-load-management.md), [onboarding-survivability.md](onboarding-survivability.md)). |
| **Anti-fragmentation** | Parallel work stays **lane-disciplined** ([parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md)); new docs prefer **merge or index** over sprawl ([documentation-entropy-rules.md](documentation-entropy-rules.md)). |
| **Anti-fake-runtime** | No documentation implies daemons, orchestrators, or repo-wide enforcement unless **proven** in-tree and qualified per [AGENTS.md](../AGENTS.md). |

---

## 3. Onboarding and operator survivability

- **Onboarding survivability:** a **small** canonical read order and explicit “optional / historical / governance-critical” labels — see [onboarding-survivability.md](onboarding-survivability.md).
- **Human operator survivability:** recognition of fatigue, lane overload, and prompt sprawl — see [operator-load-management.md](operator-load-management.md).

These are **patterns**, not tickets, not tooling.

---

## 4. Stabilization vs expansion

Runaway layering of architecture and parallel “future” stacks destroys survivability. Rules: [stabilization-vs-expansion.md](stabilization-vs-expansion.md).

---

## 5. Context continuity

Chat and editor sessions do **not** persist full reasoning. Rules for migration packages and **SAFE UNKNOWN**: [context-continuity-rules.md](context-continuity-rules.md).

Optional **filesystem-first** capture for ideas and light operational notes lives under `../continuity/` (**IdeaBox**) — **human-operated** only; it **does not** replace governance SoT, lifecycle logs, or REPORT discipline and introduces **no** automated persistence ([continuity/README.md](../continuity/README.md)).

---

## 6. Survivability Phase 3 (complexity-stage maintenance)

First lightweight **long-term survivability pass** (2026-05-19) — reviews and models only; **not** governance expansion or runtime implementation:

| Artefact | Role |
|----------|------|
| [survivability-architecture-weight-review-v0.md](survivability-architecture-weight-review-v0.md) | Cognitive-load / navigation-cost map |
| [survivability-onboarding-strategy-v0.md](survivability-onboarding-strategy-v0.md) | Shortest viable orientation paths (A–E) |
| [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md) | Tier 0–3 entry routing proposal |
| [survivability-documentation-fatigue-review-v0.md](survivability-documentation-fatigue-review-v0.md) | Prestige / taxonomy / checklist fatigue |
| [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md) | Human-operated anti-entropy triggers |
| [editorial-compression-pass-4-operator-fatigue-review-v0.md](editorial-compression-pass-4-operator-fatigue-review-v0.md) | First editorial compression pass — fatigue surfaces, dedupe map, hygiene |
| [mars-consistency-survivability-pass-5-review-v0.md](mars-consistency-survivability-pass-5-review-v0.md) | Post–Pass 4 routing, stale-reference, survivability-flow, semantic, and durability audit |
| [mars-ecosystem-stress-resilience-phase-6-review-v0.md](mars-ecosystem-stress-resilience-phase-6-review-v0.md) | First ecosystem-wide stress-test and resilience-validation (onboarding, routing, topology, operator overload, drift) |

---

## 7. Ecosystem hardening (Phase 7)

First **post-stress** hardening pass (2026-05-19) — pattern reinforcement, routing discipline, gravity review, hygiene, scaling projection — **not** architecture redesign, **not** governance expansion, **not** runtime:

| Artefact | Role |
|----------|------|
| [mars-survivability-patterns-hardening-v0.md](mars-survivability-patterns-hardening-v0.md) | Recommended survivability patterns (Tier 0–3, Core/Extended, ORCA live-first, indexes, Path A–E, AGENTS precedence) |
| [mars-document-gravity-hardening-review-v0.md](mars-document-gravity-hardening-review-v0.md) | Highest gravity zones, collapse clusters, compression targets (Factory, ORCA, Forge, governance, web-gpt-sources) |
| [mars-operational-hygiene-hardening-v0.md](mars-operational-hygiene-hardening-v0.md) | REPORT, lane, sync, onboarding, anti-drift habits — no process overload |
| [mars-scaling-readiness-review-v0.md](mars-scaling-readiness-review-v0.md) | +3 / +5 / +10 system absorption; what breaks first; maintenance needs |

---

## 8. Operational evolution transition (post–Cycle 8)

Governance moves from stabilization-heavy passes to **controlled operational evolution** — freeze baseline, maintenance mode, production-first priority:

| Artefact | Role |
|----------|------|
| [mars-operational-evolution-state-after-cycles-1-8-v0.md](mars-operational-evolution-state-after-cycles-1-8-v0.md) | **Canonical** ecosystem-state reference (post–Cycle 8) |
| [mars-operational-evolution-transition-index-v0.md](mars-operational-evolution-transition-index-v0.md) | Pick-one hub for transition docs |
| [mars-governance-baseline-freeze-v0.md](mars-governance-baseline-freeze-v0.md) | Frozen canonical patterns after Cycles 1–8 |
| [mars-lightweight-maintenance-mode-v0.md](mars-lightweight-maintenance-mode-v0.md) | Post-freeze hygiene triggers |
| [mars-operational-first-priority-v0.md](mars-operational-first-priority-v0.md) | ORCA / Factory / Triumph / external bridges primary |
| [mars-future-system-entry-discipline-v0.md](mars-future-system-entry-discipline-v0.md) | Minimal gate for new major systems |
| [mars-future-validation-cadence-v0.md](mars-future-validation-cadence-v0.md) | Rare targeted validation — not governance loops |

**Not:** another governance wave, runtime implementation, or architecture redesign.

---

## 9. Operational survivability pack (Lane B)

Incident-informed **human-operated** survivability contracts, protocols, helpers, and drills live under **`projects/mars-survivability/`** — **not** runtime enforcement.

| Entry | Role |
|-------|------|
| [projects/mars-survivability/OPERATIONAL-INDEX.md](../projects/mars-survivability/OPERATIONAL-INDEX.md) | **Start here** for G0–G4 ops, drills, validator, rollback |
| [projects/mars-survivability/QUICKSTART.md](../projects/mars-survivability/QUICKSTART.md) | Practical operator flows (pre-agent, snapshot, rollback, emergency) |
| [projects/mars-survivability/README.md](../projects/mars-survivability/README.md) | Domain purpose and structure |

This pack **extends** Phase S3 governance above; it does **not** replace [AGENTS.md](../AGENTS.md) or imply automated GitGuard deployment.

---

## 10. SAFE UNKNOWN

Anything not recorded in an authoritative file (governance, registry row, contract, lifecycle note with clear scope) is **not** guaranteed to survive the next session. If migration or handoff evidence is missing, state **SAFE UNKNOWN** and what would verify it — per [AGENTS.md](../AGENTS.md).
