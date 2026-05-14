# MARS — Reality vs mythology warnings

**Status:** **documented** — **human** pattern recognition aid. **Not** NLP classifiers, **not** automated claim detection products.

**Purpose:** Detect when MARS documentation or habits start **believing abstractions**—so audits can correct language and scope before mythology drives unsafe decisions.

---

## 1. Mythology (working definition)

**Mythology** is **narrative drift**: stories, maps, or titles that **sound** like running systems, guaranteed behaviors, or mature platforms **without** operational evidence proportional to the claim.

Mythology increases **destructive friction** ([operational-friction-semantics.md](operational-friction-semantics.md)) and erodes **status honesty** ([AGENTS.md](../AGENTS.md)).

---

## 2. Warning patterns (examples)

| Pattern | Typical failure mode |
|---------|----------------------|
| **Pilots described as capabilities** | “We have X” when only a **local pilot** or draft helper exists. |
| **Concepts named as systems** | Capitalized “Platform / Control Plane / Mesh” without in-repo execution proof. |
| **Assuming interoperability** | Implying automatic handoff where only **manual** export/envelope exists ([interoperability-semantics.md](interoperability-semantics.md)). |
| **Assuming runtime existence** | Registry rows, diagrams, or workflows treated as **running** MARS runtime. |
| **Assuming helper reliability** | Scripts treated as authoritative monitors or enforcers (S5 boundary breach). |
| **Governance inflation** | New normative layers without retiring overlaps—**prestige** documentation. |
| **Semantic prestige language** | Verbose capability speak that obscures **who** does **what** **today**. |
| **Architecture for architecture’s sake** | Maps nobody uses to decide or review work. |

---

## 3. Corrective actions (human)

- **Rename and narrow** — pilot, draft, experimental, governance-scoped; align to [operationalization-maturity-levels.md](operationalization-maturity-levels.md).
- **Add explicit boundaries** — link [execution-boundary-clarification.md](execution-boundary-clarification.md) and [registry-architecture.md](registry-architecture.md).
- **Demote to historical** or **merge** per [deprecation-and-pruning-semantics.md](deprecation-and-pruning-semantics.md).
- **Capture lesson** — short entry acceptable per [operational-lessons-and-postmortems.md](operational-lessons-and-postmortems.md).

---

## 4. Stabilization-before-expansion

When mythology signals appear, **pause expansion**:

- Stabilize **one** SoT path and index before adding new parallel docs ([stabilization-vs-expansion.md](stabilization-vs-expansion.md)).
- Prefer **evidence-first** language in experiments (S7) before pattern promotion.

---

## 5. SAFE UNKNOWN

Whether a given reader will misread a metaphor as a guarantee—**SAFE UNKNOWN**; still **worth** explicit disambiguation in high-risk areas (runtime, security, external integrations).
