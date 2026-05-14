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

---

## 6. SAFE UNKNOWN

Anything not recorded in an authoritative file (governance, registry row, contract, lifecycle note with clear scope) is **not** guaranteed to survive the next session. If migration or handoff evidence is missing, state **SAFE UNKNOWN** and what would verify it — per [AGENTS.md](../AGENTS.md).
