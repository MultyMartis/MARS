# MARS Survivability — Quickstart

**Status:** **documented** — practical operator guide.  
**Not:** governance waterfall, runtime product, or automated enforcement.

**Full index:** [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)  
**Lane:** B — use before AGENT tasks with filesystem or git impact.

---

## When to use this layer

- Cursor **AGENT** mode with shell or file writes  
- Recovery after agent mistake or context drift  
- Website Factory / workspace structural edits  
- Pre-deploy or pre-refactor freeze  
- Sandbox drills (D-01 style)

**Skip for:** pure ASK/read-only questions with no mutation intent.

---

## Pre-agent flow (2 minutes)

1. **Scope lock** — paste [templates/safe-agent-task-template-v1.md](templates/safe-agent-task-template-v1.md); list absolute ALLOWED paths.  
2. **Risk class** — [contracts/agent-operation-risk-classes-v1.md](contracts/agent-operation-risk-classes-v1.md): SAFE / LOW / MEDIUM / HIGH / CRITICAL / FORBIDDEN.  
3. **Protected zones** — if path hits P0/P1 → escalate minimum to HIGH; see [registries/protected-zones-registry-v1.md](registries/protected-zones-registry-v1.md).  
4. **Scope analyzer** (optional, recommended for multi-path):

```powershell
cd "C:\AI MARS\projects\mars-survivability\tools\helpers"
node scope-analyzer-v1.mjs --paths "path1,path2" --json
```

5. **FORBIDDEN match** → stop; output `SECURITY RISK` or `NEED HUMAN APPROVAL`.

---

## Snapshot flow (MEDIUM+ risk)

1. Run snapshot helper (draft only — **does not copy files**):

```powershell
cd "C:\AI MARS\projects\mars-survivability\tools\helpers"
node snapshot-helper-v1.mjs --workspace "workspaces/your-workspace" --risk MEDIUM --json
```

2. **Human** copies scope paths → `workspaces/_snapshots/<snap-id>/`.  
3. Complete `SNAPSHOT-MANIFEST.md` using [templates/snapshot-manifest-template.md](templates/snapshot-manifest-template.md).  
4. Put `SNAPSHOT_ID: <id>` in task header.  
5. Optional validation:

```powershell
cd "C:\AI MARS\projects\mars-survivability\tools\observability"
node snapshot-integrity-checker-v1.mjs --snapshot "workspaces/_snapshots/<snap-id>"
node manifest-cross-validator-v1.mjs --manifest "workspaces/_snapshots/<snap-id>/SNAPSHOT-MANIFEST.md" --scope "path1,path2"
```

**Rule:** incomplete snapshot = do not proceed.

---

## Validator flow (before shell)

```powershell
cd "C:\AI MARS\projects\mars-survivability\tools\validator"
node scoped-operation-validator-v1.mjs --command "your command here" --scope "allowed/path" --json
```

| Result | Action |
|--------|--------|
| **ALLOW** | Proceed only if risk class + scope lock still match |
| **DENY** | Halt — see [protocols/operational-halt-protocol-v1.md](protocols/operational-halt-protocol-v1.md) |
| **NEED_HUMAN** | Get `APPROVED:` line before AGENT runs command |

Record output per [tools/validator/validator-report-format-v1.md](tools/validator/validator-report-format-v1.md).

---

## Rollback flow (after incident)

1. **Stop** agent sessions.  
2. Read [tools/helpers/rollback-advisor-v1.md](tools/helpers/rollback-advisor-v1.md).  
3. Prefer **restore-to-new-workspace** — do not repair contaminated tree in place.  
4. Restore from snapshot dir and/or `git checkout <ref> -- <paths>`.  
5. Verify with diff helper:

```powershell
cd "C:\AI MARS\projects\mars-survivability\tools\observability"
node diff-report-helper-v1.mjs --stat-file "path\to\git-diff-stat.txt"
```

6. Append log → `logs/rollback-history/`.  
7. Contaminated source → `workspaces/_quarantine/` per [protocols/workspace-quarantine-protocol-v1.md](protocols/workspace-quarantine-protocol-v1.md).

**D-02 proved:** manual selective restore + hash compare in sandbox.

---

## Drill flow (sandbox only)

1. Read [protocols/recovery-drill-protocol-v1.md](protocols/recovery-drill-protocol-v1.md).  
2. Use `_sandbox/` or disposable drill workspace only.  
3. Run full stack: scope-analyzer → snapshot-helper → validator → observability tools.  
4. Log results → `logs/survivability/`.  
5. Write assessment → `reports/` (see D-01/D-02 examples).

---

## Emergency flow

| Trigger | Immediate action |
|---------|------------------|
| Recursive delete / git clean / reset --hard | **Halt** — [operational-halt-protocol-v1.md](protocols/operational-halt-protocol-v1.md) |
| Wrong workspace / summarization drift | **New chat** — [chat-context-drift-protocol-v1.md](protocols/chat-context-drift-protocol-v1.md) |
| Corrupted workspace | **Quarantine** — [workspace-quarantine-protocol-v1.md](protocols/workspace-quarantine-protocol-v1.md); no fix-on-top |
| Unknown file state | **SAFE UNKNOWN** — do not guess; list what would verify |
| Factory landing damage | [contracts/website-factory-enforcement-v1.md](contracts/website-factory-enforcement-v1.md) |

Post-incident: [templates/survivability-recovery-checklist-v1.md](templates/survivability-recovery-checklist-v1.md).

---

## What this layer does NOT do

- Block shell commands automatically (no hooks in baseline)  
- Copy snapshots or restore files for you  
- Run recovery loops as AGENT  
- Replace human `APPROVED:` authority  
- Certify production readiness

**GitGuard** = advisory framework + human-operated helpers — **not** autonomous recovery.

---

## Next reads (only if needed)

- Terminology: [contracts/survivability-terminology-freeze-v1.md](contracts/survivability-terminology-freeze-v1.md)  
- GitGuard boundaries: [registries/gitguard-system-entry-v1.md](registries/gitguard-system-entry-v1.md)  
- S1 baseline: [reports/s1-stabilization-checkpoint-v1.md](reports/s1-stabilization-checkpoint-v1.md)

---

*End of MARS Survivability Quickstart.*
