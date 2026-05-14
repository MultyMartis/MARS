# MARS — Operationalization maturity levels

**Status:** **documented** — governance-only, **Phase S6**. **Not** CMMI, **not** certification, **not** production SLA language.

**Purpose:** Lightweight **maturity** labels for helpers and interoperability paths—so evolution stays **explainable** and **honest**. **Explicitly avoids fake production framing:** these levels **do not** mean “GA,” “SOC2 ready,” or “deployed platform.”

---

## 1. Levels (conceptual)

| Level | Meaning | Typical evidence |
|-------|---------|------------------|
| **Documentation-only** | Described in prose/tables; no in-repo executable artifact required. | Governance sections, runbook steps. |
| **Governance-described** | Class, scope, risk, and boundaries stated in `governance/**` or linked project doc. | Helper classification row, interoperability note. |
| **Locally executable** | Script or command exists; operator runs on demand on a dev machine. | README command block, explicit flags. |
| **Operator-verified** | At least one human has run documented path and recorded outcome (e.g. REPORT, lifecycle note). | Task closeout, log entry—not automated attestation. |
| **Experimentally interoperable** | Narrow bridge/export/import tested under bounded scope; may depend on mocks or sandboxes. | Experimental label per [experimental-tooling-status.md](experimental-tooling-status.md). |
| **Operationally repeatable** | Same documented steps produce comparable artifacts when a human reruns them; still **not** “unattended product.” | Runbook + checklist; known limitations listed. |
| **External-system-dependent** | Requires named external service, credentials, or lane; behavior outside full repo control. | Cited boundary doc; no MARS-core over-claim. |
| **Runtime-scoped experimental** | Code may live under runtime-scoped trees for demos/tests—**does not** upgrade governance SoT—[execution-boundary-clarification.md](execution-boundary-clarification.md), [artifact-lifecycle-rules.md](artifact-lifecycle-rules.md). | Path + lifecycle label; honest status in AGENTS sense. |

---

## 2. Non-goals

- **No** level implies autonomous agents, orchestration, or hidden automation.  
- **No** level replaces human review for meaning, security, or registry truth.  
- Levels **do not** auto-promote when adjacent docs exist—promotion is **human** narrative.

---

## 3. Cross-references

- Controlled operationalization: [controlled-operationalization.md](controlled-operationalization.md).  
- Drift: [operationalization-drift-warnings.md](operationalization-drift-warnings.md).  
- Stabilization vs expansion: [stabilization-vs-expansion.md](stabilization-vs-expansion.md).

---

## 4. SAFE UNKNOWN

Default unknown paths to **documentation-only** or **governance-described** until executable evidence and operator verification exist.
