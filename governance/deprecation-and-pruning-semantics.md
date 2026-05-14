# MARS — Deprecation and pruning semantics

**Status:** **documented** — **human** labeling and editorial discipline. **Not** automated tombstoning, **not** archive products, **not** retention law.

**Purpose:** Normalize **cleanup and removal** as healthy behavior so governance and helpers do not accrete indefinitely.

Aligns with artifact labels in [artifact-lifecycle-rules.md](artifact-lifecycle-rules.md); extends the **why** and **signals** for audits.

---

## 1. Principles

- **Deprecation is healthy** — marks superseded material without pretending history never existed.
- **Unused docs may be archived** — posture = label + index + pointer, not necessarily file deletion (see AGENTS.md file-operation norms).
- **Failed experiments may stay historical** — evidence of learning; must not imply current capability.
- **Helper retirement is acceptable** — especially when noise > value or boundaries blur (S5/S6).
- **Governance simplification is allowed** — fewer normative sources beats more “coverage.”
- **Semantic pruning is healthy** — remove prestige duplication; merge overlapping rules.

---

## 2. Signal types (audit vocabulary)

| Signal | Meaning |
|--------|---------|
| **Archive signal** | Content still **valuable for history** but must not drive day-to-day SoT; trim active indexes; keep inbound links or redirects in prose. |
| **Merge signal** | Two artifacts differ trivially; **one** successor reduces load; prefer index-first merges when appropriate ([documentation-entropy-rules.md](documentation-entropy-rules.md)). |
| **Prune signal** | Content is **harmful**, **unused**, or **duplicate SoT**; remove redundant sections, delete only when policy and owners agree (no silent mass deletes). |
| **Historical but not active** | Explicit posture: readers should **not** execute against this file without a deliberate archaeology task; pair with replacement or scope banner. |

---

## 3. “Historical but not active”

Use clear prose (and lifecycle labels) to mean:

- **Not** current operational truth for execution, registry, or handoff.
- **May** still inform narrative, audits, or migration archaeology.
- **Must not** be indexed as primary without a stated reason.

This is **documentation semantics**, not a database state machine.

---

## 4. Relationship to experiments (S7)

- Failed experiments: prefer **historical** + short lesson pointer over silent deletion.
- Successful pattern promotion: deprecate **experiment-only** narratives that implied broader scope than evidence supports ([experiment-to-pattern-transition.md](experiment-to-pattern-transition.md)).

---

## 5. SAFE UNKNOWN

Whether your org uses git tags, folders, or filenames to encode lifecycle mechanically—**SAFE UNKNOWN**. Retention duration for archived chat exports—outside this doc’s scope ([context-continuity-rules.md](context-continuity-rules.md)).
