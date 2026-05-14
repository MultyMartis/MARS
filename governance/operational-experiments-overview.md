# MARS — Operational experiments overview

**Status:** **documented** — governance-only, **Phase S7**. **Not** a runtime product, **not** orchestration, **not** autonomous experimentation.

**Purpose:** Define what **operational experimentation** means in MARS: controlled probes that gather **evidence** without rewriting governance truth or implying shipped platform capability.

---

## 1. Definition

**Operational experiments** are **narrow**, **human-initiated**, **bounded** activities that test a hypothesis about how work could run, integrate, or be described—under explicit **experimental** labeling. They are **controlled operational probes**, not proofs of a multi-agent platform, control plane, or production runtime.

---

## 2. What experiments are **not**

| Misread | Clarification |
|--------|----------------|
| **Platform proof** | A successful experiment does **not** establish MARS runtime, orchestration, or product-scale behavior. |
| **Governance mutation** | Experiments **do not** automatically change [registry-source-of-truth.md](registry-source-of-truth.md), capability narratives, or canonical terminology. |
| **Shipped capability** | Local success, screenshots, or one-off scripts **≠** stable capability—see [experiment-evidence-rules.md](experiment-evidence-rules.md). |
| **Hidden escalation** | No experiment authorizes silent background execution, undocumented triggers, or “it runs so it’s core” semantics—[human-execution-guarantees.md](human-execution-guarantees.md), [tooling-escalation-warnings.md](tooling-escalation-warnings.md). |

---

## 3. Core vocabulary (S7)

| Term | Meaning |
|------|---------|
| **Narrow pilot** | Small scope, clear entry/exit, explicit owner; may touch one lane or one integration surface. |
| **Local experiment** | Executed on an operator machine or sandbox; outcomes may not generalize. |
| **Operational sketch** | Lightweight description or stub of a flow—documentation or thin code—**not** a committed execution engine. |
| **Experimental helper** | Assistive utility under [experimental-tooling-status.md](experimental-tooling-status.md); remains non-canonical until a **human** stabilization path—[experiment-to-pattern-transition.md](experiment-to-pattern-transition.md). |
| **Evidence gathering** | Deliberate capture of logs, REPORT excerpts, repro steps, and limitations—feeds lessons, not mythology—[operational-lessons-and-postmortems.md](operational-lessons-and-postmortems.md). |

---

## 4. Alignment (S0–S6)

- **Narrow tooling pilot:** [`tools/governance-scanner/`](../tools/governance-scanner/) — human-invoked read-only markdown scan; **not** an experiment platform or orchestration proof.  
- **Registry drift hints (PILOT 02):** [`tools/registry-checker/`](../tools/registry-checker/) — local-only read-only scan; hints only; **not** sync, enforcement, or autonomous registry management.  
- **Survivability / anti-fake-runtime:** [operational-survivability.md](operational-survivability.md), [enforcement/forbidden-runtime-claims.md](enforcement/forbidden-runtime-claims.md).  
- **Operationalization without drift:** [controlled-operationalization.md](controlled-operationalization.md), [operationalization-maturity-levels.md](operationalization-maturity-levels.md).  
- **Classification and isolation:** [experiment-classification.md](experiment-classification.md), [experimental-isolation-rules.md](experimental-isolation-rules.md).

**Operational index / stabilization pass (tools):** [../tools/README.md](../tools/README.md), [../tools/helper-maturity-review.md](../tools/helper-maturity-review.md), [../tools/helper-stabilization-rules.md](../tools/helper-stabilization-rules.md).

---

## 5. SAFE UNKNOWN

Whether a given folder or script is an “operational experiment” vs stable helper is **SAFE UNKNOWN** until labeled, scoped, and reviewed—default to **experimental** when in doubt per [experimental-isolation-rules.md](experimental-isolation-rules.md).
