# Helper stabilization rules (anti-sprawl)

**Status:** governance-aligned operations documentation (S5–S6). **Not** a policy engine, **not** executable enforcement.

**Goal:** Keep operational helpers **narrow**, **explicit**, and **honest** — prevent uncontrolled growth and **platformization** myths.

**Related:** [tooling-boundary-rules.md](../governance/tooling-boundary-rules.md), [tooling-escalation-warnings.md](../governance/tooling-escalation-warnings.md), [operationalization-drift-warnings.md](../governance/operationalization-drift-warnings.md), [stabilization-vs-expansion.md](../governance/stabilization-vs-expansion.md).

---

## When helpers should **stay experimental**

- Output requires **human interpretation** for correctness (hints, heuristics, substring matches).  
- False positives are **material** and not fully catalogued.  
- No **dated** human verification record for the scenarios that matter.  
- Scope is still expanding faster than documentation — default to **experimental** per [experimental-isolation-rules.md](../governance/experimental-isolation-rules.md).

---

## When **stabilization** is justified (still not a “platform”)

Stabilization means **documentation + scope discipline**, not autonomous authority.

- **Clear owner** and README/runbook: inputs, outputs, known false positives, **non-goals**.  
- **Bounded roots** and flags; no surprise defaults that scan half the monorepo unintentionally.  
- **Human verification** for a **defined** checklist (e.g. “release hygiene triage”) recorded in REPORT or lifecycle notes — [operationalization-maturity-levels.md](../governance/operationalization-maturity-levels.md) **operator-verified** / **operationally repeatable** in the **narrow** sense only.  
- **Read-first** posture preserved; any future write path needs explicit flags and separate review — not part of current pilots.

Stabilization **does not** mean: CI mandatory, org-wide SLA, or “approved runtime.”

---

## When to **archive** helpers

- Superseded by a **simpler** path with no loss of honesty.  
- Rule set became unmaintained **or** misleading relative to governance.  
- Social misuse (treated as law) cannot be corrected with documentation — prefer **archive** or **freeze** over silent ambiguity.

Archiving is a **human** decision in task scope; this doc does not delete files.

---

## When helpers become **dangerous**

- They **mutate** governance, registry SoT, or production config **without** explicit human intent per change.  
- They run on **schedules** or triggers not visible in the same action (daemon semantics).  
- They become **mandatory gates** for unrelated work without governance agreement.  
- They accumulate **hidden coordination** (chained tools, opaque state).  
- Language drifts to **control plane**, **orchestrator-lite**, **self-healing**, **hands-off validation**.

---

## Warning signs of **pseudo-runtime** drift

See [tooling-escalation-warnings.md](../governance/tooling-escalation-warnings.md): retries/backoff “product” language, leader election, opaque caches, silent cross-system chains, growing coupling.

**Response:** Stop adding features; document actual behavior; reclassify; consider archive — [helper-maturity-review.md](helper-maturity-review.md).

---

## Anti-platformization rules (explicit)

| Forbidden pattern | Why |
|-------------------|-----|
| **Hidden execution** | Breaks traceability — [human-execution-guarantees.md](../governance/human-execution-guarantees.md). |
| **Automatic governance mutation** | SoT remains human-maintained — [registry-source-of-truth.md](../governance/registry-source-of-truth.md). |
| **Background scanning** | Daemon / monitoring semantics unless **separately** owned and documented — not current MARS helper posture. |
| **Invisible coordination** | Orchestration smell — [operationalization-drift-warnings.md](../governance/operationalization-drift-warnings.md). |
| **Silent synchronization** | Registry / doc “sync engines” are out of scope and misleading. |

---

## SAFE UNKNOWN

Whether a **future** helper meets these rules is **unknown** until reviewed against behavior and triggers — default new scripts to **experimental** and list them in [README.md](README.md) when they become pilots.
