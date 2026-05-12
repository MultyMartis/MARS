# Operational template — Operator session (v0)

**Status:** **documentation-only** pattern for a **single supervised work session** (e.g. Cursor chat / local editor session). **Not** daemon session persistence, **not** multi-agent autonomous swarm.

**Normative references:** [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md), [reporting-standard-v0.md](reporting-standard-v0.md), [first-operational-runbook-v0.md](first-operational-runbook-v0.md), [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [`../../governance/execution-model.md`](../../governance/execution-model.md).

---

## 1. Session header

| Field | Value |
|-------|-------|
| Session goal (one sentence) | |
| Operator | |
| Related run step (R01–R15 if using reference sequence) | |
| Checkpoint alignment (C01–C08) | |

---

## 2. Session structure

Recommended flow (maps to “prompt → execute → report” legacy shorthand in [workflow-map.md](workflow-map.md)):

1. **Frame** — attach only necessary artifact paths; state non-goals.
2. **Plan** — micro-steps visible to supervisor.
3. **Execute** — filesystem edits / doc authoring in **AGENT** mode when allowed.
4. **Validate** — self-check against contracts + run **spot QA** if in scope.
5. **Report** — mandatory close-out per §3.

---

## 3. REPORT discipline

End each material session with a report whose **title** follows [reporting-standard-v0.md](reporting-standard-v0.md):

```text
# REPORT — <task/stage name>
```

Minimum body sections:

1. **Changed files** (paths)
2. **Summary** (what / why)
3. **Git status** awareness (what should / should not be committed)
4. **UNKNOWN / SECURITY RISK** if applicable (or explicit “none observed”)

**No** `git add .` unless project policy explicitly requires it — prefer **explicit paths** per [`../../web-gpt-sources/04-workflows__git-rules.md`](../../web-gpt-sources/04-workflows__git-rules.md) when cited by the operator pack.

---

## 4. Checkpoint behavior

- If session touches a **checkpoint boundary**, update checkpoint evidence table ([project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md)).
- Do **not** mark checkpoints “passed” without listed evidence.

---

## 5. Git discipline

- Default: **no commit** unless milestone policy says otherwise ([`../../AGENTS.md`](../../AGENTS.md) project rules).
- When committing: **explicit** `git add <path>` only; message reflects doc honesty.
- **Never** commit unrelated runtime experiments if session is doc-only.

---

## 6. Artifact tracking

- For each artifact touched: **version note**, **supersede** relationship if applicable ([artifact-state-model-v0.md](artifact-state-model-v0.md)).
- If **artifact bus** movement is narrative-only, say so — no fake transport logs.

---

## 7. SAFE UNKNOWN handling

When blocked by missing evidence:

1. Label **SAFE UNKNOWN** with what is missing and what would verify it ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)).
2. Do **not** fabricate numbers, approvals, or deploy URLs.
3. Escalate with **NEED HUMAN APPROVAL** when business/legal input is required ([orchestration-signals-v0.md](orchestration-signals-v0.md)).

---

## 8. Session outcome

- [ ] Goal met
- [ ] Partially met — carryover documented
- [ ] Blocked — reason + escalation

---

*Template v0 — Cursor-aligned supervised session hygiene.*
