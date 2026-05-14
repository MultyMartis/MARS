# MARS — Tooling escalation warnings

**Status:** **documented** — governance-only, **Phase S5**. **Not** monitoring, **not** alerts, **not** automated governance.

**Purpose:** List **signals** that lightweight tooling is **drifting** toward **dangerous** territory (pseudo-runtime, silent orchestration, hidden automation). Operators use this for **human** triage — no tooling product is implied.

---

## 1. Warning signals

| Signal | Why it matters |
|--------|----------------|
| **Too much hidden state** | Decisions live in caches, local DBs, or opaque files — not in committed, reviewable artifacts. |
| **Implicit scheduling** | “Runs every night” or cron without a named owner, scope, and runbook — overlaps **daemon** semantics. |
| **Undocumented automation** | Side effects not described in governance or project README — breaks HITL traceability. |
| **Growing operational coupling** | One script becomes mandatory for **all** lanes; failures block unrelated work. |
| **Runtime-like behavior** | Retries, backoff, leader election language in “helper” code — smells like a **service**. |
| **Silent cross-system coordination** | Chains calls across Slack, n8n, git, without a human-readable trace for that run. |
| **Invisible retries** | Network or API loops without explicit logging and caps — operator cannot reconstruct what happened. |
| **Self-healing claims** | Language that implies autonomous repair of governance or production — **red flag** unless proven and scoped. |
| **Pseudo-control-plane drift** | Scripts start **assigning** work, **mutating** registries, or **opening** tasks without human intent. |

---

## 2. Recommended human actions

1. **Stop** expanding the script; document current behavior honestly (inputs, outputs, side effects).  
2. **Classify** using [experimental-tooling-status.md](experimental-tooling-status.md).  
3. **Compare** to [tooling-boundary-rules.md](tooling-boundary-rules.md) and [lightweight-script-guidelines.md](lightweight-script-guidelines.md).  
4. **Prefer** read-only checks, dry-run, and explicit flags before any new write path.  
5. **Split** lanes: move product/build automation under the relevant **project** doc tree with a runbook; keep `governance/**` for **human** semantics.  
6. **Record** outcomes in a REPORT-style note when ambiguity is resolved — [context-continuity-rules.md](context-continuity-rules.md).

---

## 3. Stabilization-before-expansion

If two or more signals above appear together, treat as **governance debt** — favor **stabilization** (narrow scope, docs, delete dead paths) over **expansion** — [stabilization-vs-expansion.md](stabilization-vs-expansion.md).

---

## 4. SAFE UNKNOWN

This document **does not** score the repo automatically. Whether a **specific** path is escalating is **SAFE UNKNOWN** until a human reviews behavior and triggers.

**Related (operational helpers):** [../tools/helper-stabilization-rules.md](../tools/helper-stabilization-rules.md) — explicit anti-patterns (hidden execution, background scanning, pseudo-platformization).
