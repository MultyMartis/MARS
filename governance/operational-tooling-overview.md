# MARS — Operational tooling overview

**Status:** **documented** — governance-only, **Phase S5**. **Not** a tooling platform, **not** runtime, **not** orchestration.

**Purpose:** Define the **role** of **lightweight operational tooling** in MARS: what it may do for humans and governance, and what it must **not** become.

---

## 1. Role of operational tooling

Operational tooling **assists** **human-operated** governance and operations. It exists to:

- reduce repetitive **manual** checks (read-only scans, link checks, phrase scans);
- format or assemble **reports** the operator explicitly requested;
- export or inventory files for **review**;
- support **narrow** validation or demo paths that remain **explainable** and **invoked explicitly**.

Tooling **does not** replace human judgment, **does not** own execution truth, and **does not** silently change governance meaning.

---

## 2. What tooling is **not**

| Misuse | Clarification |
|--------|----------------|
| **Orchestration** | No implicit multi-step scheduling across systems or “always-on” coordination. |
| **Autonomous execution** | No unattended agents, daemons, or self-triggered work loops claimed as MARS product behavior. |
| **Hidden runtime** | No undocumented execution layer that mutates state, retries, or “heals” without human visibility. |

See [tooling-boundary-rules.md](tooling-boundary-rules.md) and [tooling-escalation-warnings.md](tooling-escalation-warnings.md).

---

## 3. Categories (vocabulary)

| Category | Typical behavior | Boundary |
|----------|-------------------|----------|
| **Helpers** | One-shot utilities (format, transform, summarize for paste) under explicit invocation. | Must not maintain hidden state between runs. |
| **Validators** | Check invariants, links, forbidden phrases, or registry shape **read-only**. | **Validation mention ≠ automated CI** unless separately evidenced — [validation-chain-semantics.md](validation-chain-semantics.md). |
| **Scanners** | Grep-style or inventory passes over the tree. | Output is for human triage; not a control plane. |
| **Exporters** | Produce artifacts (CSV, JSON snippets, markdown lists) from repo content. | Operator decides commit and lane. |
| **Report utilities** | Assemble **REPORT**-style sections or checklists from inputs. | Human still owns narrative and **SAFE UNKNOWN**. |
| **Local scripts** | Small CLI or shell scripts run **on demand**. | See [lightweight-script-guidelines.md](lightweight-script-guidelines.md). |
| **Adapters** | Narrow I/O or shape mapping toward a documented surface — often **experimental**. | **Adapter ≠ external system** — [adapter-and-bridge-boundaries.md](adapter-and-bridge-boundaries.md). |
| **Experimental utilities** | Demos, spikes, local-only aids. | **Experimental tooling ≠ MARS runtime capability** — [experimental-tooling-status.md](experimental-tooling-status.md). |

---

## 4. Alignment (S0–S4)

- **Pilot (experimental, local-only):** read-only markdown phrase scan for human triage — [`tools/governance-scanner/README.md`](../tools/governance-scanner/README.md) (**not** enforcement, **not** CI).  
- **Anti-fake-runtime:** [operational-survivability.md](operational-survivability.md), [enforcement/forbidden-runtime-claims.md](enforcement/forbidden-runtime-claims.md).  
- **Execution semantics:** [execution-contracts-overview.md](execution-contracts-overview.md), [execution-boundary-clarification.md](execution-boundary-clarification.md).  
- **Registry:** [runtime-registry-boundaries.md](runtime-registry-boundaries.md), [registry-source-of-truth.md](registry-source-of-truth.md).  
- **HITL / REPORT:** Human-in-the-loop remains primary; tooling supports explicit closeouts — [context-continuity-rules.md](context-continuity-rules.md).

---

## 5. SAFE UNKNOWN

Whether a **specific** script in the tree is “acceptable S5 tooling” vs drifting toward orchestration depends on its **behavior** (state, triggers, cross-lane writes). If undocumented, treat as **SAFE UNKNOWN** until reviewed against [tooling-boundary-rules.md](tooling-boundary-rules.md).
