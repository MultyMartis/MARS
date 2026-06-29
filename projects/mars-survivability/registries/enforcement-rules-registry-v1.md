# Enforcement Rules Registry (v1)

**Status:** **documented** — human-operated enforcement catalogue for MARS survivability.  
**Not:** runtime policy engine, automated deny product, or Cursor hook implementation.

**Implements:** [destructive-operations-policy-v1.md](../contracts/destructive-operations-policy-v1.md), [agent-operation-risk-classes-v1.md](../contracts/agent-operation-risk-classes-v1.md)  
**Halt protocol:** [operational-halt-protocol-v1.md](../protocols/operational-halt-protocol-v1.md)  
**Protected zones:** [protected-zones-registry-v1.md](protected-zones-registry-v1.md)

---

## 1. FORBIDDEN operations registry

Canonical FORBIDDEN list for AGENT. Source of truth: [destructive-operations-policy-v1.md](../contracts/destructive-operations-policy-v1.md) §3 + [agent-operation-risk-classes-v1.md](../contracts/agent-operation-risk-classes-v1.md) §8.

| ID | Operation | Agent | Human |
|----|-----------|-------|-------|
| F-01 | Recursive directory delete | **Deny** | Snapshot + explicit approval |
| F-02 | Delete at volume/canonical root (`X:\`, `X:\AI MARS\`, `X:\AI MARS STORAGE\`, `X:\MARS-Localhost\`) | **Deny** | Discouraged |
| F-03 | Wildcard mass delete | **Deny** | Path list + approval |
| F-04 | Move/rename top-level ecosystem folders | **Deny** | Charter required |
| F-05 | `git clean` (any flags) | **Deny** | At keyboard only |
| F-06 | `git reset --hard` | **Deny** | At keyboard only |
| F-07 | `git push --force` to main/master | **Deny** | Explicit request + warning |
| F-08 | Mass search-replace without path glob lock | **Deny** | Dry-run review first |
| F-09 | Auto-generated cleanup scripts unreviewed | **Deny** | Review script body |
| F-10 | Workspace delete + recreate as recovery | **Deny** | Quarantine + clone-first |
| F-11 | Recursive delete outside `_sandbox/` | **Deny** | Sandbox only |
| F-12 | Heuristic "unused file" deletion | **Deny** | Inventory manifest |
| F-13 | Delete build outputs when task forbids | **Deny** | Regen pipeline |
| F-14 | Governance/registry prune without charter | **Deny** | Lane B charter |

**Default interpretation:** uncertain operation → **FORBIDDEN** → halt per [operational-halt-protocol-v1.md](../protocols/operational-halt-protocol-v1.md).

---

## 2. Mandatory snapshot operations

Snapshot **required** before first mutation when risk class is MEDIUM RISK or higher.

| Trigger | Snapshot location | Manifest |
|---------|-------------------|----------|
| MEDIUM+ workspace structural edit | `workspaces/_snapshots/` | `SNAPSHOT-MANIFEST.md` |
| Pre-refactor multi-file change | Same | Required fields per standard |
| Pre-migration / handoff freeze | Same | Reference freeze noted |
| Incident freeze | Same | Link to `logs/incidents/` |
| Drill (sandbox) | `_snapshots/` or sandbox copy | Retention tier **Drill** |
| Deploy-critical dist bundle | `_snapshots/` | If dist non-reproducible |

**Standard:** [snapshot-manifest-standard-v1.md](../protocols/snapshot-manifest-standard-v1.md)  
**Incomplete snapshot:** do not proceed — halt with `INCOMPLETE SNAPSHOT`.

---

## 3. Mandatory human-confirm operations

Operator must reply `APPROVED: <operation> @ <absolute paths>` **before** AGENT executes:

| # | Operation |
|---|-----------|
| 1 | First delete or move in session |
| 2 | Any git command beyond status/diff/log |
| 3 | Shell command outside scope lock |
| 4 | Any write to CRITICAL zone path |
| 5 | Recovery mode entry ("rebuild", "reset", "start over") |
| 6 | Commit or push |
| 7 | Quarantine move (production paths) |
| 8 | Promotion from `_recovery/` to production |
| 9 | Mass search-replace (even with glob lock) |
| 10 | Snapshot waive for MEDIUM+ operation |

---

## 4. AGENT forbidden contexts

AGENT **must refuse or switch to read-only** in these contexts:

| Context | Required mode |
|---------|---------------|
| Post-incident filesystem repair | Human shell / ASK plan only |
| Recovery without quarantine manifest | ASK — halt mutations |
| Missing scope lock after summarization | HALT — request new task block |
| Lane B editing `workspaces/*/src` without exception | HALT |
| Parallel AGENT on same workspace | HALT — coordinate or stop |
| `_snapshots/` delete or tree mutation | HALT — human only |
| Governance bulk edit without charter | HALT |
| "Fix it" / "clean up" without path list | HALT |
| Multiple candidate workspaces unnamed | HALT — ask anchor |
| FORBIDDEN op in user message | HALT — refuse |

---

## 5. Workspace isolation rules

| Rule | Detail |
|------|--------|
| **One workspace per AGENT task** | Scope lock lists exactly one production workspace root for Lane A |
| **No cross-workspace edits** | Exception: Lane B doc paths only |
| **Infra zones separate** | `_snapshots/`, `_quarantine/`, `_recovery/`, `_sandbox/` — not interchangeable |
| **Quarantine before deep recovery** | Contaminated tree → `_quarantine/` — no fix-on-top |
| **Sandbox ≠ quarantine** | Production contamination never goes to `_sandbox/` |
| **Recovery staging** | Verified restore → `_recovery/` → human promote |
| **Triumph v4/v5** | P2 production SoT — no delete-recreate; snapshot before structural change |

---

## 6. Path-scope requirements

Every AGENT task **must** include:

| Field | Rule |
|-------|------|
| **TARGET FOLDER** | Narrowest absolute root — not whole repo for mutations |
| **ALLOWED PATHS** | Explicit allowlist; absolute paths only |
| **FORBIDDEN PATHS** | CRITICAL zones + unlisted workspaces |
| **RISK CLASS** | From agent-operation-risk-classes |
| **SCOPE LOCK block** | Verbatim from [safe-agent-task-template-v1.md](../templates/safe-agent-task-template-v1.md) |

**Violation:** cwd outside ALLOWED PATHS → immediate halt.  
**Expansion:** user adds scope without updating block → `NEED HUMAN APPROVAL`.

---

## 7. Chat drift detection triggers

Agent or operator should treat as **drift signal**:

| Trigger | Action |
|---------|--------|
| Summarization event in long session | Re-anchor scope lock; consider new chat |
| Task goal changed without new scope lock | HALT |
| Lane label contradicts paths touched | HALT |
| Model references wrong workspace name/version | HALT — verify path |
| Prior turn was summary-only | Mandatory scope lock restatement |
| Multi-project paths in one response plan | HALT — split tasks |
| Recovery narrative without SoT pointer | HALT |
| "While we're at it" scope expansion | HALT |

**Protocol:** [chat-context-drift-protocol-v1.md](../protocols/chat-context-drift-protocol-v1.md)

---

## 8. Emergency halt triggers

Immediate **STOP** — no further mutations until human resolves:

| Trigger | Signal |
|---------|--------|
| Scope drift detected | `SECURITY RISK` |
| Path uncertainty | `SAFE UNKNOWN` |
| Multiple candidate workspaces | Ask human to name anchor |
| Unexpected delete proposal | Refuse + list FORBIDDEN ID |
| Rebuild-from-memory proposed | Refuse — require snapshot/git/SoT |
| Missing snapshot for MEDIUM+ | `INCOMPLETE SNAPSHOT` |
| Missing SoT for Factory recovery | `SAFE UNKNOWN` |
| Recovery ambiguity | ASK-only |
| Conflicting instructions | Ask clarification — do not guess |
| Unknown filesystem state | Read-only audit only |
| Recursive operation proposed | Refuse F-01/F-11 |
| Workspace-wide replace | Refuse F-08 |
| Cleanup / wipe / fresh language | Refuse — see safe-prompt library |

**Escalation:** [operational-halt-protocol-v1.md](../protocols/operational-halt-protocol-v1.md)

---

## 9. Unsafe prompt patterns

Canonical catalogue: [safe-prompt-pattern-library-v1.md](../guardrails/safe-prompt-pattern-library-v1.md)

**High-risk phrases (agent must not interpret as authorization):**

- "clean repo" / "clean everything" / "clean up"
- "start fresh" / "start from scratch"
- "wipe" / "wipe dist"
- "recreate project" / "recreate workspace"
- "delete old versions"
- "remove broken files"
- "mass refactor" without scope
- "fix the mess" without path list

---

## 10. Recovery-only ASK-mode situations

AGENT **must not mutate filesystem** — ASK or human-only:

| Situation | Mode |
|-----------|------|
| Post-incident damage assessment | ASK read-only plan |
| Mass delete recovery planning | ASK |
| Quarantine move (production) | Human executes |
| Production restore copy | Human executes |
| Integrity sign-off after restore | Human |
| Rollback map drafting | ASK or read-only AGENT |
| Conflicting git + filesystem state | ASK |
| Unknown extent of contamination | ASK |
| Second-wave "cleanup" after failed fix | **Forbidden** — halt |

---

## 11. Enforcement maturity

| Layer | Status |
|-------|--------|
| Documentation registry (this file) | **v1 present** |
| Operator paste discipline | **Human-operated** |
| Cursor hooks / GitGuard validator | **SAFE UNKNOWN** — see [gitguard-system-entry-v1.md](gitguard-system-entry-v1.md) |

---

## 12. Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — G1 enforcement registry |

---

*End of Enforcement Rules Registry v1.*
