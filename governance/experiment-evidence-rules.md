# MARS — Experiment evidence rules

**Status:** **documented** — governance-only, **Phase S7**. **Not** automated attestation, **not** a telemetry product.

**Purpose:** Define what counts as **operational evidence** during experiments so narratives stay tied to observable facts—without equating artifacts with platform proof.

---

## 1. Evidence states (ordered loosely by strength)

| State | Meaning | Typical artifacts |
|-------|---------|-------------------|
| **Described** | Prose or diagrams claim behavior; no required execution. | Design notes, governance text. |
| **Attempted** | Someone tried a step; outcome may be incomplete or ambiguous. | Chat log, partial log snippet. |
| **Locally executed** | Ran on one machine/environment; may depend on local secrets or state. | Command history, local stdout. |
| **Reproducible** | Another operator can repeat using **documented** steps and inputs; limits stated. | Runbook, fixture IDs, version pins. |
| **Operator-verified** | A human attests they observed the outcome and scope—**not** cryptographic proof. | REPORT section, signed-off checklist. |
| **Externally dependent** | Outcome relies on named third-party uptime, quotas, or config. | Boundary cite—[external-system-boundaries.md](external-system-boundaries.md). |
| **Partially observed** | Only part of the chain was witnessed; rest inferred or skipped. | Explicit “not observed” notes required. |
| **SAFE UNKNOWN** | Evidence missing for a claim or segment—must be labeled, not papered over. | Listed unknowns + what would verify. |

States **do not** auto-escalate: each promotion in narrative strength requires **human** judgment and often new artifacts—[experiment-to-pattern-transition.md](experiment-to-pattern-transition.md).

---

## 2. Common false equivalences (reject)

| False move | Clarification |
|------------|----------------|
| **Screenshots = system proof** | UI captures show one moment; they do not prove correctness, security, or repeatability. |
| **One successful run = stable capability** | Single paths hide edge cases; stabilization needs repeatability and stated limits—[operationalization-maturity-levels.md](operationalization-maturity-levels.md). |
| **Local scripts = platform feature** | Repository presence of a script **≠** productized runtime behavior—[experimental-tooling-status.md](experimental-tooling-status.md). |
| **Experimental runtime path = MARS runtime** | Scoped trees or demos **≠** core runtime claims—[execution-boundary-clarification.md](execution-boundary-clarification.md), [AGENTS.md](../AGENTS.md). |
| **Validation mention = automation exists** | See [validation-chain-semantics.md](validation-chain-semantics.md). |

---

## 3. Minimum evidence hygiene (lightweight)

For any experiment worth recording:

1. **Hypothesis** in one sentence (what was being tested).  
2. **Scope** (lanes, systems, files touched).  
3. **Steps** actually run (or explicit gaps).  
4. **Outcome** with evidence state labels from §1.  
5. **Limitations** and **SAFE UNKNOWN** where applicable.  

Optional but valuable: link to a **postmortem** skeleton—[operational-lessons-and-postmortems.md](operational-lessons-and-postmortems.md).

---

## 4. Alignment

- Maturity labels: [operationalization-maturity-levels.md](operationalization-maturity-levels.md).  
- Forbidden claim cues: [enforcement/forbidden-runtime-claims.md](enforcement/forbidden-runtime-claims.md).  
- Artifact honesty: [artifact-lifecycle-rules.md](artifact-lifecycle-rules.md).

---

## 5. SAFE UNKNOWN

Default missing segments of a chain to **SAFE UNKNOWN** rather than implied success. **Partially observed** without labeling is a governance defect, not a neutral omission.
