# Human Authority Protocol (v1)

**Status:** **documented** — normative protocol fixing operator supremacy over agents and tooling.  
**Not:** legal contract, automated enforcement, or runtime policy engine.

**Lane:** B — applies to all MARS survivability and GitGuard advisory tooling.

---

## 1. Principle

**Operator authority is absolute.**  
Agents, validators, and helpers **advise**; they do **not** govern execution.

---

## 2. AGENT is bounded

| AGENT may | AGENT must not (default) |
|-----------|-------------------------|
| Read within scope lock | Recursive delete |
| Edit allowlisted paths | git clean / reset --hard |
| Run read-only git inspection | Force push |
| Report UNKNOWN / halt | Autonomous cleanup or recovery |
| Refuse FORBIDDEN ops | Expand scope without instruction |

Source: [destructive-operations-policy-v1.md](../contracts/destructive-operations-policy-v1.md), [AGENTS.md](../../../AGENTS.md)

---

## 3. Validator is advisory only

[scoped-operation-validator-v1.mjs](../tools/validator/scoped-operation-validator-v1.mjs) outputs **ALLOW**, **DENY**, or **NEED_HUMAN**.

- **DENY** = recommendation to stop — **not** system-enforced block.  
- Operator may override only with explicit documented approval and accepted risk.  
- Validator does not run automatically in AGENT loop (G3).

---

## 4. Helpers are advisory only

G3 tools ([snapshot-helper](../tools/helpers/snapshot-helper-v1.mjs), [scope-analyzer](../tools/helpers/scope-analyzer-v1.mjs), diff/rollback advisors):

- **Do not** write files (except operator saves reports manually).  
- **Do not** copy snapshots, run git, or restore trees.  
- **Do not** schedule background tasks or daemons.

---

## 5. Human confirms destructive operations

Destructive or irreversible-adjacent operations require:

1. Explicit user instruction naming paths.  
2. Scope lock in prompt.  
3. `APPROVED: <operation> @ <absolute paths>` for MEDIUM+ and mandatory human-confirm list in [enforcement-rules-registry-v1.md](../registries/enforcement-rules-registry-v1.md).  
4. Snapshot when risk class requires.

**“Fix it” / “clean up”** is **not** approval.

---

## 6. No autonomous cleanup

Forbidden for AGENT and **not** delegated to tooling:

- Repo-wide cleanup scripts unreviewed  
- Heuristic unused-file deletion  
- `git clean`, mass `Remove-Item -Recurse`  
- Workspace delete + recreate  

---

## 7. No autonomous recovery

Forbidden patterns:

- Self-healing workspace rebuild  
- Auto-rollback after failed AGENT run  
- Silent restore from snapshot  
- Fix-on-top of contaminated tree  

Recovery = **human-operated** quarantine → analyze → selective restore per [rollback-advisor-v1.md](../tools/helpers/rollback-advisor-v1.md).

---

## 8. No hidden execution

| Rule | Meaning |
|------|---------|
| No background daemons | Survivability tools are CLI/docs only |
| No Cursor Shell hooks (G3) | No intercept without charter |
| No fake runtime claims | Docs must say “human-operated” |
| Tool output visible | Operator runs helpers manually |
| REPORT honesty | List changed files; SAFE UNKNOWN when unsure |

---

## 9. Escalation

On conflict between tool advice and operator decision:

- **Operator wins** if written approval exists and risk accepted.  
- **Halt** if operator unsure — [operational-halt-protocol-v1.md](operational-halt-protocol-v1.md).  
- **New chat** on context drift — [chat-context-drift-protocol-v1.md](chat-context-drift-protocol-v1.md).

---

## 10. SAFE UNKNOWN

- Organizational RACI outside MARS repo — **UNKNOWN**.  
- External backup systems — not covered unless operator documents.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | G3 — human authority protocol v1 |

---

*End of Human Authority Protocol v1.*
