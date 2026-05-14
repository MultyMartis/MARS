# MARS — Controlled operationalization

**Status:** **documented** — governance-only, **Phase S6**. **Not** a production runtime, **not** orchestration, **not** autonomous execution.

**Purpose:** Define what **controlled operationalization** means in MARS: how **real** operational helpers and **semi-structured** interoperability may appear **without** collapsing into hidden-runtime drift.

---

## 1. Definition

**Controlled operationalization** is the **governance-first** allowance for **gradual**, **explainable** utility evolution: scripts, adapters, exporters, and similar aids that **assist humans** under **explicit** invocation and **documented** scope—while **preserving** S0–S5 boundaries (survivability, execution contracts, tooling limits, registry honesty).

**Operationalization ≠ autonomous runtime.** Introducing helpers or interoperability **does not** imply MARS owns scheduling, retries, multi-agent coordination, or product-grade execution services unless **separately** evidenced in-repo and described without exaggeration per [AGENTS.md](../AGENTS.md).

---

## 2. Pillars (S6 posture)

| Pillar | Meaning |
|--------|---------|
| **Governance-first** | Scope, maturity, and drift expectations are **read** before expanding helpers—[operationalization-maturity-levels.md](operationalization-maturity-levels.md), [operationalization-drift-warnings.md](operationalization-drift-warnings.md). |
| **Gradual utility evolution** | Add **narrow** capabilities with clear inputs/outputs; avoid “platform sprawl” in a single helper. |
| **Semi-structured interoperability** | Handoffs use **explicit** envelopes, exports, reports, and documented bridges—[interoperability-semantics.md](interoperability-semantics.md). |
| **Explicit / manual execution** | Default: human starts the run; visible initiation; no silent background chains—[human-execution-guarantees.md](human-execution-guarantees.md). |
| **Anti-hidden-runtime** | No undocumented state authority, no invisible retries, no pseudo-control-plane—[tooling-escalation-warnings.md](tooling-escalation-warnings.md). |

---

## 3. What S6 still does **not** introduce

S6 **does not** authorize: orchestration products, workflow engines, daemons, hidden automation, background scheduling as MARS core, or control-plane runtime **claims**. Helpers remain **assistive**; governance remains **human-maintained**.

---

## 4. Cross-references

- S5 tooling: [operational-tooling-overview.md](operational-tooling-overview.md), [tooling-boundary-rules.md](tooling-boundary-rules.md).  
- S4 execution: [execution-contracts-overview.md](execution-contracts-overview.md), [execution-boundary-clarification.md](execution-boundary-clarification.md).  
- Helper classes: [operational-helper-classification.md](operational-helper-classification.md).  
- Experimental pilots index + anti-sprawl rules: [../tools/README.md](../tools/README.md), [../tools/helper-stabilization-rules.md](../tools/helper-stabilization-rules.md).

---

## 5. SAFE UNKNOWN

Whether a **concrete** in-repo script is “controlled” vs drifting is **SAFE UNKNOWN** until behavior (triggers, state, side effects) is reviewed against [operational-helper-classification.md](operational-helper-classification.md) and [tooling-boundary-rules.md](tooling-boundary-rules.md).
