# MARS — Operationalization drift warnings

**Status:** **documented** — governance-only, **Phase S6**. **Not** automated monitoring, **not** alerts product.

**Purpose:** Define **signals** that MARS is drifting toward pseudo-runtime mythology, hidden orchestration, undocumented execution, governance bypass, automation creep, or invisible interoperability. Operators use this for **human** triage.

---

## 1. Drift vectors and red flags

| Drift vector | Red flags (examples) |
|--------------|----------------------|
| **Pseudo-runtime mythology** | “The helper runs MARS,” “orchestrator-lite,” “mini control plane,” “self-driving tasks.” |
| **Hidden orchestration** | Undocumented “run A then B” chains; cron without owner; “it always chains to n8n.” |
| **Undocumented execution** | Side effects not in README/runbook; “just run `npm test`” that also mutates registries. |
| **Governance bypass** | “Skip governance for speed,” “tool output overrides SoT,” edits to `governance/**` without task scope—[registry-source-of-truth.md](registry-source-of-truth.md). |
| **Automation creep** | Each helper adds a new trigger until no one knows full blast radius—[tooling-escalation-warnings.md](tooling-escalation-warnings.md). |
| **Invisible interoperability** | Silent cross-repo sync; invisible retries; “magic” mapping from ticket ID to file paths. |

---

## 2. Example wording to avoid (unless literally true and scoped)

- “Fully automated MARS pipeline” (implies product runtime).  
- “Hands-off validation” (collides with [validation-chain-semantics.md](validation-chain-semantics.md)).  
- “Self-healing registry” (implies autonomous governance).  
- “Background MARS worker” (daemon semantics).  
- “Interoperability layer handles coordination” (orchestration smell).

Prefer: **explicit**, **manual**, **operator-verified**, **experimental**, **read-only**, **dry-run**.

---

## 3. Stabilization recommendations

1. **Pause expansion** when two or more red-flag themes appear together—[stabilization-vs-expansion.md](stabilization-vs-expansion.md).  
2. **Document** current behavior: inputs, outputs, triggers, credentials, lanes touched—[lightweight-script-guidelines.md](lightweight-script-guidelines.md).  
3. **Reclassify** helper per [operational-helper-classification.md](operational-helper-classification.md); set maturity honestly—[operationalization-maturity-levels.md](operationalization-maturity-levels.md).  
4. **Narrow** scope or split into read-only vs write paths with explicit flags.  
5. **Record** human verification in REPORT or lifecycle notes—[context-continuity-rules.md](context-continuity-rules.md).

---

## 4. Pause-expansion signals (human)

Treat as “**stabilize before adding**” when:

- New helpers become **mandatory** for unrelated lanes.  
- Operators cannot reconstruct **who** ran **what** last week.  
- Language in docs **outruns** evidenced behavior—[enforcement/forbidden-runtime-claims.md](enforcement/forbidden-runtime-claims.md).

---

## 5. Cross-references

- Overview: [controlled-operationalization.md](controlled-operationalization.md).  
- Interop safety: [interoperability-semantics.md](interoperability-semantics.md).  
- HITL: [human-execution-guarantees.md](human-execution-guarantees.md).

---

## 6. SAFE UNKNOWN

This document **does not** evaluate the repo automatically. Specific drift is **SAFE UNKNOWN** until humans compare behavior to signals above.
