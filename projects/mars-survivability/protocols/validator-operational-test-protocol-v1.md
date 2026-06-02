# Validator Operational Test Protocol (v1)

**Status:** **documented** — human-operated procedure for safely testing the scoped operation validator.  
**Not:** CI pipeline, automated test runner, or production execution protocol.

**Tool:** [../tools/validator/scoped-operation-validator-v1.mjs](../tools/validator/scoped-operation-validator-v1.mjs)  
**Examples:** [../tools/validator/examples/](../tools/validator/examples/)

---

## 1. Purpose

Verify validator behavior against known safe and dangerous strings **without** executing dangerous commands on the MARS repository.

---

## 2. Principles

| Principle | Rule |
|-----------|------|
| **Sandbox-only** | Test using example `.txt` files and invented command strings — not live AGENT Shell |
| **No production execution** | Never run DENY-class commands “to see what happens” |
| **Deny-first** | Unexpected ALLOW on dangerous example = **test failure** |
| **Human override documented** | If operator intentionally proceeds after NEED_HUMAN, record approval in report |
| **No auto-run** | Validator is invoked manually per test case |

---

## 3. Preconditions

1. Node.js available on operator machine (LTS recommended).  
2. Working directory: `projects/mars-survivability/tools/validator/`.  
3. Registry present: `rules/validator-rules-registry-v1.json`.  
4. Read [validator-architecture-v1.md](../tools/validator/validator-architecture-v1.md) boundaries section.

---

## 4. Test procedure (manual)

### Step A — Safe cases

For each file in `examples/safe-example-*.txt`:

1. Extract `COMMAND`, `SCOPE`, `RISK_CLASS` from the example (comment lines only — **do not** run destructive COMMAND if it contains write/delete).  
2. Run:

```bash
node scoped-operation-validator-v1.mjs --command "<COMMAND>" --scope "<SCOPE>" --risk-class <CLASS>
```

3. Record decision; compare to `EXPECTED_DECISION` in example.  
4. If mismatch → file false positive/negative note under `reports/`.

**safe-example-02:** use exact command `git status` only.

### Step B — Dangerous cases

For each `examples/dangerous-example-*.txt`:

1. Pass **command text only** to validator — **do not execute** the command in Shell.  
2. Expect **DENY** (or **NEED_HUMAN** only where example allows).  
3. Confirm matched rules include expected IDs (e.g. FC-04 for git clean).

### Step C — JSON output spot-check

```bash
node scoped-operation-validator-v1.mjs --command "git clean -fdx" --json
```

Verify JSON includes all required fields per [validator-report-format-v1.md](../tools/validator/validator-report-format-v1.md).

### Step D — False positive review

Test legitimate commands your lane uses (read-only audit, single-file doc edit description):

- If **DENY** or **NEED_HUMAN** → document as false positive candidate.  
- Do **not** weaken registry without updating protected-zones alignment.  
- Prefer scope + risk-class clarity over registry dilution.

### Step E — False negative review

Test obfuscated variants (extra spaces, alternate quoting) **as strings only**:

- If **ALLOW** on obvious destructive intent → document as false negative.  
- Propose registry patch in separate chartered task.

---

## 5. Exit code mapping

| Exit code | Decision |
|-----------|----------|
| 0 | ALLOW |
| 1 | NEED_HUMAN |
| 2 | DENY |
| 3 | Usage or registry error |

Tests **do not** require exit code 0 for dangerous examples — exit code 2 is success for dangerous cases.

---

## 6. Human override rules

Validator **NEED_HUMAN** is not automatic approval. Operator may proceed only when:

1. Written `APPROVED: <operation> @ <absolute paths>` exists in task thread.  
2. Risk class and snapshot requirements satisfied per [agent-operation-risk-classes-v1.md](../contracts/agent-operation-risk-classes-v1.md).  
3. Override recorded in validation report `humanOverride` field.

**DENY** outcomes: override **discouraged** — redesign operation or escalate to Lane B charter.

---

## 7. What not to do

- Run validator in Cursor hooks or agent loop (G3+ only, human-chartered).  
- Execute dangerous-example commands on repo filesystem.  
- Treat ALLOW as permission without scope lock.  
- Commit test reports containing secrets or tokens.

---

## 8. Drill linkage

Optional: combine with [recovery-drill-protocol-v1.md](recovery-drill-protocol-v1.md) **tabletop** — operator validates a scripted recovery command list without execution.

---

## 9. SAFE UNKNOWN

- Full false positive/negative catalogue — **UNKNOWN** until first operator test log in `reports/`.  
- Cross-platform command coverage (bash vs PowerShell) — **partial** in v1 registry.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | G2 — operational test protocol v1 |

---

*End of Validator Operational Test Protocol v1.*
