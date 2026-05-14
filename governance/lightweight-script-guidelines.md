# MARS — Lightweight script guidelines

**Status:** **documented** — governance-only, **Phase S5**. **Not** a mandate to add scripts; **not** CI policy.

**Purpose:** Safe **expectations** for **small local scripts** so they stay **explicit**, **explainable**, and **non-orchestrating**.

---

## 1. Examples of acceptable intent

- Markdown **link** checks on a subtree.  
- **Phrase** or token scans (forbidden claims, drift cues).  
- **Grep** helpers that print paths for human review.  
- **Report formatting** (concatenate sections, normalize headings) from inputs the operator provides.  
- **Local exports** (inventory lists, CSV from static files).  
- **File inventory** scripts for audits.

These remain **manual**: someone runs the command and reads the output.

---

## 2. Principles

1. **Explicit invocation** — Command is run **on purpose** for that moment; no hidden scheduler.  
2. **No orchestration implication** — Script name or folder must not read like “the MARS control plane” unless a **real** product exists and is evidenced per [AGENTS.md](../AGENTS.md).  
3. **No hidden infrastructure** — Avoid “magic” global config dirs that change behavior without docs; prefer repo-relative paths and documented env vars.  
4. **No silent governance mutation** — Scripts must **not** rewrite `governance/**` meaning (claims, SoT, registry rows) **without** a tracked human decision (e.g. clear task scope + review). Read-only scans are safer.

---

## 3. Acceptable patterns

- **Exit non-zero** on detected issues **after** printing human-readable diagnostics.  
- **Dry-run** mode or `--print` before any write.  
- **Scope flags** (path, lane, project) so operators know what will be touched.  
- Output to **stdout** or a single obvious artifact path.

---

## 4. Unsafe patterns (for “governance helpers”)

- Writing to **multiple** unrelated subtrees in one run.  
- **Auto-commit** or **auto-push**.  
- **Retry until success** against network or VCS without caps and operator visibility.  
- **Polling** loops calling external APIs.  
- **Cron** or OS-level triggers checked into repo without a runbook that states owner and scope.

---

## 5. When scripts should stay **outside** core governance

If a script’s purpose is **product build**, **deploy**, or **runtime test** for a specific project lane, prefer that project’s folder and docs — not `governance/**` as a home for executable logic. Governance may **link** to runbooks; it should not accumulate **opaque** executable layers.

Cross-ref: [tooling-boundary-rules.md](tooling-boundary-rules.md), [tooling-escalation-warnings.md](tooling-escalation-warnings.md).