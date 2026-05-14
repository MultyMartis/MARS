# MARS — Human execution guarantees (HITL integrity)

**Status:** **documented** — governance-only, **Phase S6**. **Not** automated compliance, **not** runtime enforcement.

**Purpose:** Preserve **human-in-the-loop (HITL)** integrity while MARS allows **controlled operationalization**: explicit initiation, visible effects, owned narrative, and **no** silent machinery.

**Alignment:** [AGENTS.md](../AGENTS.md), [execution-contracts-overview.md](execution-contracts-overview.md), [tooling-boundary-rules.md](tooling-boundary-rules.md), [context-continuity-rules.md](context-continuity-rules.md), [operational-survivability.md](operational-survivability.md).

---

## 1. Guarantees (normative for MARS *discourse*, not code enforcement)

| Guarantee | Meaning |
|-----------|---------|
| **Explicit execution** | Work runs because a human (or human-directed agent session) **started** it for **that** scope—not because an undocumented timer or hook decided. |
| **Visible initiation** | Triggers are knowable: command line, chat instruction, documented runbook step—not “something fixed it overnight” without trace. |
| **Human review** | Meaningful governance, security, and scope decisions stay with humans; helpers **assist**, they **do not** certify truth. |
| **REPORT expectations** | Task closeouts remain human-owned per project rules; tooling may suggest sections, not replace disclosure—[tooling-boundary-rules.md](tooling-boundary-rules.md). |
| **Explicit ownership** | **Who** accepted outputs, **which** lane, **what** was excluded—stated in chat or REPORT, not inferred. |
| **No silent execution** | Side effects without operator-visible logs/artifacts/console are **out of band** for acceptable S5/S6 helpers. |
| **No invisible retries** | Bounded, logged retries only under explicit operator opt-in and caps—[tooling-escalation-warnings.md](tooling-escalation-warnings.md). |
| **No hidden state mutation** | No undisclosed files/DBs/env that change governance or production meaning—[operational-survivability.md](operational-survivability.md). |

---

## 2. Relationship to interoperability

Handoffs use **explicit** exports, envelopes, and imports—[interoperability-semantics.md](interoperability-semantics.md). **Invisible ownership transfer** breaks HITL and is **disallowed** as a *claimed* MARS pattern.

---

## 3. Survivability note

HITL integrity reduces **operator overload** and **documentation entropy**: fewer “magic” paths to memorize—[operator-load-management.md](operator-load-management.md), [documentation-entropy-rules.md](documentation-entropy-rules.md).

---

## 4. SAFE UNKNOWN

If initiation, retries, or state paths are **undocumented**, assume **HITL is not guaranteed** for that path until clarified—work proceeds only with explicit human acknowledgment of risk.
