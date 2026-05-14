# Operational helper lessons learned (pilots 01–02)

**Status:** documentation — aligns with S7 [operational-lessons-and-postmortems.md](../governance/operational-lessons-and-postmortems.md). **Not** an incident ticket system, **not** automated learning.

**Scope:** Outcomes and risks observed from the design and intended use of `governance-scanner` and `registry-checker` (see each README). **SAFE UNKNOWN:** Quantitative frequency of runs and hits in production operator practice is **not** logged in-repo unless separately added.

---

## What worked

- **Explicit invocation** — `node …/script.js` with documented flags matches [human-execution-guarantees.md](../governance/human-execution-guarantees.md) and avoids “it just runs” mythology.  
- **Read-only, stdout-only** behavior — no hidden caches, no file mutation; reduces pseudo-runtime drift per [tooling-escalation-warnings.md](../governance/tooling-escalation-warnings.md).  
- **Transparent rules** — `forbidden-phrases.json` and `registry-rules.json` are inspectable; supports governance-first review.  
- **Bounded claims in READMEs** — “hints not verdicts” validates [experiment-evidence-rules.md](../governance/experiment-evidence-rules.md) posture: evidence is **operator output + context**, not proof of platform capability.  
- **Dry-run path (registry-checker)** — makes scan configuration visible without rule churn.

---

## What produced false positives (expect this)

- **Definitional / teaching prose** containing phrases the scanner flags (forbidden themes **named** in governance).  
- **Substring matching** without negation or citation detection.  
- **Registry heuristics** firing on examples, mirrors, or acceptable duplication of identifiers.  
- **Line-local rules** missing multi-line SoT cues or table structure.

**Lesson:** False positives are **acceptable** if labeled and triaged; they become **harmful** when outputs are treated as authoritative failures.

---

## What governance assumptions were validated

- **Governance truth stays primary** — helpers point **to** docs; they do not replace [registry-source-of-truth.md](../governance/registry-source-of-truth.md).  
- **Local success ≠ platform capability** — scripts prove **files + operator intent**, not MARS runtime or orchestration ([operational-experiments-overview.md](../governance/operational-experiments-overview.md)).  
- **Tooling boundaries matter** — narrow validators remain inside [tooling-boundary-rules.md](../governance/tooling-boundary-rules.md) when described honestly.

---

## What risks appeared (or could appear)

- **Enforcement mythology** — naming or social use that implies “the repo failed validation.”  
- **Mandatory coupling** — “you cannot merge without scanner green” without a **documented** human process — [validation-chain-semantics.md](../governance/validation-chain-semantics.md).  
- **Rule bloat** — large, opaque rule sets without ownership — [operationalization-drift-warnings.md](../governance/operationalization-drift-warnings.md).  
- **Lane bleed** — using helpers to assert **production** or **mars-runtime** truth beyond their scope.

---

## What should **not** happen next

- Background workers, file watchers, or scheduled scans **without** named owner and runbook — [tooling-escalation-warnings.md](../governance/tooling-escalation-warnings.md).  
- Auto-fix, auto-commit, or registry **rewrite** from helper output.  
- Silent chaining: scanner → ticket system → bot PR **without** human-readable trace for that chain.  
- Promoting either pilot to “MARS validation platform” or “governance engine” language.

---

## What would indicate **dangerous drift**

Overlap with [tooling-escalation-warnings.md](../governance/tooling-escalation-warnings.md) and [operationalization-drift-warnings.md](../governance/operationalization-drift-warnings.md):

- Hidden state (caches, local DBs) driving outcomes.  
- Implicit scheduling or “nightly governance scan” without governance narrative.  
- Invisible retries or cross-system coordination.  
- **Growing operational coupling** — unrelated lanes blocked by helper failures.  
- **Self-healing** or “auto-align registry to scanner” claims.

**If two or more signals appear:** pause expansion; stabilize documentation — [stabilization-vs-expansion.md](../governance/stabilization-vs-expansion.md).

---

## SAFE UNKNOWN

- How often operators run each pilot and **typical** false-positive rates — **unknown** without logs or habit surveys.  
- Whether any **operator-verified** runbooks exist outside this repo — **unknown**.

**Where to record evidence:** per [operational-lessons-and-postmortems.md](../governance/operational-lessons-and-postmortems.md) — `logs/`, task REPORT, or project `notes/`.
