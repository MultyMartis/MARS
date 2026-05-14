# MARS — Tooling boundary rules

**Status:** **documented** — governance-only, **Phase S5**. **Not** enforcement automation, **not** a policy engine.

**Purpose:** State **where tooling stops** and **runtime / orchestration** territory begins — in **documentation semantics** and **operator expectations**.

---

## 1. Distinctions (vocabulary)

| Term | Safe interpretation in MARS |
|------|-----------------------------|
| **Utility** | Small, **explicitly invoked** aid with **obvious** input/output; no standing authority over repo or external systems. |
| **Helper** | Same as utility; emphasizes **human** use during a task. |
| **Validator** | **Read-only** or **report-only** check; human interprets failures. Does **not** by itself prove “system validated” in a product sense. |
| **Adapter** | **Narrow** mapping of shapes or I/O; may wrap an API for a **demo** or **test**. **Not** ownership of the external system. |
| **Bridge** | **Handoff** concept (semantics ↔ runner) per [execution-model.md](execution-model.md). **Bridge description ≠ running bridge service** — [execution-boundary-clarification.md](execution-boundary-clarification.md). |
| **Orchestrator** | Coordinates **multiple** autonomous steps, schedules, or cross-system **implicit** chaining. **Out of scope** for “acceptable lightweight tooling” unless evidenced as **separate** product/runtime and labeled honestly per [AGENTS.md](../AGENTS.md). |
| **Runtime service** | Long-lived process that **executes** MARS-claimed workloads as a **product**. **Not** implied by helper scripts. |
| **Daemon** | Background process with **standing** execution. **Not** asserted for MARS core in governance docs without in-tree proof. |
| **Workflow engine** | Platform that **owns** branching, retries, credentials (e.g. external n8n). MARS docs may **reference**; MARS tooling must not **pretend** to be that engine. |
| **Background automation** | Triggers without a **human** decision at trigger time. **Red flag** for in-repo “governance helpers” unless clearly externalized and documented. |

---

## 2. Red flags (tooling drift)

Treat as **stop and clarify** signals:

- **Hidden state** — files, DBs, or caches that change meaning without a human-readable trail in committed artifacts.  
- **Autonomous retries** — loops that keep trying until success without operator opt-in.  
- **Background loops** — periodic jobs that mutate repo or call external systems silently.  
- **Implicit orchestration** — “run A then B then C” encoded only in opaque config with no human runbook.  
- **Silent execution** — side effects without console/log/artifact the operator sees.  
- **Cross-lane mutation** — scripts that edit **another** lane’s canonical outputs without explicit task scope.  
- **Self-triggered actions** — hooks that start work without a human starting that work for that moment.

These align with **anti-fake-runtime** posture and **HITL**: humans gate meaning and risky writes.

---

## 3. REPORT discipline

- Tooling may **suggest** REPORT sections or checklists; it **does not** satisfy REPORT by itself.  
- **SAFE UNKNOWN** remains the human’s responsibility when evidence is missing — tooling must not auto-fill claims.

---

## 4. Cross-references

- [operational-tooling-overview.md](operational-tooling-overview.md)  
- [lightweight-script-guidelines.md](lightweight-script-guidelines.md)  
- [adapter-and-bridge-boundaries.md](adapter-and-bridge-boundaries.md)  
- [tooling-escalation-warnings.md](tooling-escalation-warnings.md)  
- [enforcement/forbidden-runtime-claims.md](enforcement/forbidden-runtime-claims.md)
