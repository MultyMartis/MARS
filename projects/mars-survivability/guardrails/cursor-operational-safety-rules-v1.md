# Cursor Operational Safety Rules (v1)

**Status:** **documented** — operational guardrails for Cursor AGENT sessions on MARS.  
**Not:** IDE plugin, hook enforcement, or automated deny engine.

**Implements:** [destructive-operations-policy-v1.md](../contracts/destructive-operations-policy-v1.md), [agent-operation-risk-classes-v1.md](../contracts/agent-operation-risk-classes-v1.md)  
**Companion:** [cursor-agent-guardrails-v1.md](cursor-agent-guardrails-v1.md) (session header v1)  
**G1:** [operational-halt-protocol-v1.md](../protocols/operational-halt-protocol-v1.md), [enforcement-rules-registry-v1.md](../registries/enforcement-rules-registry-v1.md)

---

## 1. Absolute prohibitions (AGENT)

Agent **must refuse** these regardless of casual user phrasing:

| Rule | Description |
|------|-------------|
| **No delete-and-recreate** | Never delete workspace (or major subtree) and rebuild as recovery |
| **No rebuild-from-memory** | Never reconstruct implementation from chat context without snapshot/git/template source |
| **No broad cleanup** | No repo-wide or workspace-wide "cleanup", "hygiene", "fresh start" |
| **No recursive delete** | No `Remove-Item -Recurse`, `rm -rf`, `rd /s`, etc. |
| **No top-level rm** | No delete at `C:\AI MARS\` root or drive root |
| **No mass move** | No bulk move/rename across workspaces or top-level folders |
| **No agent recovery loops** | Stop after first failed fix — no delete→retry→delete cycles |
| **No workspace-wide replace without lock** | Mass search-replace requires path glob lock + dry-run review |
| **No git clean / git reset --hard** | FORBIDDEN for AGENT |
| **No git push --force** to main/master | FORBIDDEN unless explicit user request + warning |

---

## 2. Mandatory practices

| Rule | When |
|------|------|
| **Mandatory snapshot before risky ops** | MEDIUM RISK or higher — per [snapshot-manifest-standard-v1.md](../protocols/snapshot-manifest-standard-v1.md) |
| **Mandatory scope lock** | Every AGENT task — use [safe-agent-task-template-v1.md](../templates/safe-agent-task-template-v1.md) |
| **Mandatory new chat after drift** | Context drift, contradiction, or post-incident — fresh scope lock |
| **Mandatory REPORT footer** | Execution safety section in every AGENT task closeout |
| **Mandatory quarantine before deep recovery** | Broken/drifted workspace — [workspace-quarantine-protocol-v1.md](../protocols/workspace-quarantine-protocol-v1.md) |

---

## 3. AGENT forbidden cases (halt immediately)

Output `SECURITY RISK`, `NEED HUMAN APPROVAL`, or `SAFE UNKNOWN` and **stop**:

1. cwd outside scope lock **ALLOWED PATHS**  
2. Request touches CRITICAL zone without explicit allowlist entry  
3. User says "delete all", "clean repo", "start fresh" without path list  
4. Prior turn was summary-only and current turn lacks scope lock  
5. Recovery task proposes delete as first step  
6. Contradiction: Lane B task editing `workspaces/*/src` without exception  
7. Operation class = FORBIDDEN per [agent-operation-risk-classes-v1.md](../contracts/agent-operation-risk-classes-v1.md)  
8. Attempt to modify `workspaces/_snapshots/` without explicit task scope  
9. Second AGENT chat mutating same workspace without coordination  
10. Cannot verify path exists or is in scope  

---

## 4. Shell command deny list (substring)

Do not execute unless human same-turn `APPROVED:` + exact command:

- `Remove-Item` + `-Recurse`  
- `rm -rf` / `rm -r`  
- `rd /s` / `rmdir /s`  
- `git clean`  
- `git reset --hard`  
- `git push --force`  
- `del /s`  

**Exception:** scoped sandbox path under `workspaces/_sandbox/` with human approval.

---

## 5. Protected zone quick reference

| Tier | Paths | AGENT write |
|------|-------|-------------|
| **CRITICAL** | `governance/`, `registry/`, `agents/`, `web-gpt-sources/`, `workspaces/_snapshots/`, `projects/mars-survivability/` | Deny unless explicitly scoped |
| **HIGH** | `projects/`, `mars-runtime/`, `logs/` | Lane B + narrow scope |
| **MEDIUM** | `workspaces/` (production trees) | Lane A + one workspace scope lock |

Full registry: [protected-zones-registry-v1.md](../registries/protected-zones-registry-v1.md).

---

## 6. Recovery discipline

When user reports damage:

1. **Stop** mutations.  
2. Read-only: `git status`, list missing paths.  
3. Propose restore plan — human executes.  
4. No second-wave cleanup.  
5. Log to `logs/incidents/`.

---

## 7. Multi-chat rules

- One AGENT chat per workspace mutation at a time.  
- Name: `Lane<A|B>-<workspace|domain>-<phase>`.  
- No parallel "hygiene" in Lane B while Lane A builds.

---

## 8. Mode selection

| Situation | Mode |
|-----------|------|
| Architecture / survivability audit | ASK or AGENT read-only |
| Scoped implementation | AGENT + safe task template |
| Post-incident filesystem | **Human** |
| Mass delete recovery plan | ASK |
| FORBIDDEN op requested | Refuse in any mode |

---

## 9. Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — G0 operational safety rules |

---

*End of Cursor Operational Safety Rules v1.*
