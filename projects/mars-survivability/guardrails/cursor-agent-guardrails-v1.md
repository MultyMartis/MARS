# Cursor Agent Guardrails (v1)

**Status:** **documented** — paste-friendly guardrails for operators and task prompts.  
**Implements:** [safe-execution-layer-v1.md](../protocols/safe-execution-layer-v1.md), [destructive-operations-policy-v1.md](../contracts/destructive-operations-policy-v1.md)

---

## 1. Session header (copy block)

```text
=== MARS AGENT GUARDRAILS v1 ===
Lane: [A|B]
Phase: [audit|implement|recovery]
Repo root: C:\AI MARS

SCOPE LOCK:
- Allowed root: <absolute path>
- Allowed ops: read, edit files under Allowed root
- Forbidden: recursive delete, git clean, git reset --hard, move top-level dirs
- Protected: governance/, registry/, agents/, web-gpt-sources/, other workspaces/

SNAPSHOT: [required|waived by human] — ID: ______

Do not infer cleanup authority. If path unclear → SAFE UNKNOWN and stop.
=== END GUARDRAILS ===
```

---

## 2. Pre-flight (agent self-check)

Before first write or shell command:

1. Restate **allowed root** in one sentence.  
2. Run location check (`pwd` / `Get-Location`).  
3. Confirm phase ≠ recovery-with-delete.  
4. If recovery: switch to **parity-first** rules — no delete-recreate.

---

## 3. Stop triggers (agent must halt)

- cwd outside scope lock  
- User message contains “delete all”, “clean repo”, “start fresh” without path list  
- Request touches P0 path ([protected-zones-registry-v1.md](../registries/protected-zones-registry-v1.md))  
- Contradiction between lane and path (Lane B editing `workspaces/*/src`)  
- Prior message was summary and scope lock missing  

**Output:** `SECURITY RISK` or `NEED HUMAN APPROVAL` + question.

---

## 4. Shell command deny list (agent)

Do not execute (substring match):

- `Remove-Item` + `-Recurse`  
- `rm -rf` / `rm -r`  
- `rd /s`  
- `git clean`  
- `git reset --hard`  
- `git push --force`  
- `del /s`  
- `rmdir /s`  

**Exception:** human typed `APPROVED:` line with exact command and paths in same turn.

---

## 5. Recovery guardrails

When user reports damage or incident:

1. **Stop** further agent mutations.  
2. **Read-only** audit: `git status`, list missing paths.  
3. Propose restore plan — **human executes** git/filesystem restore.  
4. No second-wave cleanup.

---

## 6. Multi-chat guardrails

- One AGENT chat per workspace mutation at a time.  
- Name chats: `LaneA-<workspace>-<phase>`.  
- Do not run “hygiene” in Lane B while Lane A builds.

---

## 7. REPORT footer (required for AGENT tasks)

```text
## Execution safety
- cwd: <path>
- scope lock honored: yes/no
- destructive ops: none | list
- protected zone touch: none | list
```

---

## 8. Mode selection guide

| Task | Mode |
|------|------|
| Architecture audit | ASK or AGENT read-only |
| Single-file fix | AGENT + scope lock |
| Mass delete recovery plan | ASK |
| Implement landing section | AGENT Lane A |
| Governance doc edit | AGENT Lane B |
| Post-incident filesystem | **Human** |

---

## 9. Links

- [cursor-operational-safety-rules-v1.md](cursor-operational-safety-rules-v1.md) (G0 operational rules)  
- [operational-halt-protocol-v1.md](../protocols/operational-halt-protocol-v1.md) (G1 halt + escalation)  
- [safe-prompt-pattern-library-v1.md](safe-prompt-pattern-library-v1.md) (G1 safe/unsafe prompts)  
- [cursor-agent-operational-risk-analysis-v1.md](../reports/cursor-agent-operational-risk-analysis-v1.md)  
- [website-factory-safe-production-rules-v1.md](../protocols/website-factory-safe-production-rules-v1.md)

---

*End of Cursor Agent Guardrails v1.*
