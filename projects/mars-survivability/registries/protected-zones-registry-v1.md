# Protected Zones Registry (v1)

**Status:** **documented** — human-maintained registry for safe-execution layer and future GitGuard.  
**Not:** enforced ACL.

**Policy:** [../contracts/destructive-operations-policy-v1.md](../contracts/destructive-operations-policy-v1.md)  
**Filesystem authority:** [../../../governance/mars-x-drive-root-authority-v1.md](../../../governance/mars-x-drive-root-authority-v1.md)

---

## 0. Canonical filesystem roots (X-drive — active)

**Volume:** `AI WS` / drive `X:`  
**Status:** active operational roots (X0–X1 cutover complete).

| Root | Role | Write authority | Destructive authority |
|------|------|-----------------|----------------------|
| `X:\AI MARS\` | Active Brain (Git, governance, projects, agents) | task-scoped | operator-approved only |
| `X:\AI MARS STORAGE\` | Storage (out-of-Git, backups, archives, bulk data) | task-scoped | operator-approved only |
| `X:\MARS-Localhost\` | Local runtime (Laragon, CMS, DB, logs) | task-scoped | operator-approved only |
| `X:\` | Volume root | **denied** | **denied** |

### Deprecated operational roots (write denied)

| Path | Status |
|------|--------|
| `C:\AI MARS\` | DEPRECATED OPERATIONAL ROOT — WRITE DENIED — HISTORICAL READ ONLY WHEN AUTHORIZED |
| `C:\MARS Phenix\` | DEPRECATED OPERATIONAL ROOT — WRITE DENIED — HISTORICAL READ ONLY WHEN AUTHORIZED |
| `C:\MARS Phenix\AI MARS\` | DEPRECATED OPERATIONAL ROOT — WRITE DENIED — HISTORICAL READ ONLY WHEN AUTHORIZED |
| `C:\AI MARS STORAGE\` | DEPRECATED OPERATIONAL ROOT — WRITE DENIED — HISTORICAL READ ONLY WHEN AUTHORIZED |
| `C:\MARS Phenix\AI MARS STORAGE\` | DEPRECATED OPERATIONAL ROOT — WRITE DENIED — HISTORICAL READ ONLY WHEN AUTHORIZED |
| `D:\MARS-Localhost\` | DEPRECATED OPERATIONAL ROOT — WRITE DENIED — HISTORICAL READ ONLY WHEN AUTHORIZED |
| `E:\MARS-Localhost\` | DEPRECATED OPERATIONAL ROOT — WRITE DENIED — HISTORICAL READ ONLY WHEN AUTHORIZED |

**Rule:** Do not register arbitrary whole-system paths. MARS boundary applies to MARS-controlled project, storage, and runtime data — not OS/AppData caches unless separately migrated.

---

## 1. Zone levels

| Level | Meaning | Agent delete | Agent write |
|-------|---------|--------------|-------------|
| **P0** | Ecosystem critical | **Deny** | Lane B + narrow task only |
| **P1** | System packs | **Deny** | Lane B or scoped project task |
| **P2** | Implementation SoT | **Deny** | Lane A with scope lock |
| **P3** | Regenerable / sandbox | Caution | Allowed with scope lock |
| **Q** | Quarantine / sandbox | Human-only delete | Disposable |

---

## 2. P0 — Ecosystem critical

| Path | Notes |
|------|-------|
| `governance/` | Governance SoT — freeze baseline |
| `registry/` | Project/tool registry |
| `AGENTS.md` | Root agent contract |
| `.cursorrules` | Cursor project rules |
| `web-gpt-sources/` | Legacy architecture pack |
| `security/` | Threat model, approval gates |
| `memory/` | Memory policies |

---

## 3. P1 — System packs (`projects/`)

| Path | Notes |
|------|-------|
| `projects/mars-website-factory/` | Factory governance |
| `projects/orca/` | ORCA operational pack |
| `projects/wpilot/` | WPilot |
| `projects/metabot-seo-content-agent/` | MetaBOT boundary |
| `projects/mars-survivability/` | This safety domain |
| `projects/homegateway-v4-ai/` | Registered operational doc |
| `projects/orca/ppc/triumph-manipulator/schema/` | Campaign schema SoT |

**Rule:** No agent bulk edits across `projects/` without Lane B task listing paths.

---

## 4. P1 — Agents and workflows

| Path | Notes |
|------|-------|
| `agents/` | Agent packs, checklists |
| `workflows/` | Workflow docs |
| `interfaces/` | Interface contracts |
| `control-plane/` | Documented architecture |
| `continuity/` | IdeaBox |

---

## 5. P2 — Workspaces (implementation)

| Path | Notes |
|------|-------|
| `workspaces/*/` | Client implementation trees |
| `workspaces/*/src/` | Primary implementation SoT |

**Exception:** Active task scope lock may allow writes under **one** `workspaces/<name>/` root.

**Triumph note:** v4/v5 workspaces are P2 — treat as production SoT; no agent delete-recreate.

---

## 6. P2 — Shared assets

| Path | Notes |
|------|-------|
| `shared/assets/` | Shared icon/libraries |
| `projects/triumph-manipulator-landing/design/` | Design authority |

---

## 7. P3 — Regenerable (caution)

| Path | Notes |
|------|-------|
| `**/node_modules/` | Regen via npm — task often forbids install |
| `**/dist/`, `**/build/`, `**/out/` | Regen via gulp — no hand-edit |
| `**/.cache/` | Disposable |
| `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/output/` | Export output |

**Rule:** Prefer regen over delete; snapshot if deploy-critical.

---

## 8. Q — Quarantine / sandbox / recovery

| Path | Status |
|------|--------|
| `workspaces/_sandbox/` | **Created** — disposable experiments (G0) |
| `workspaces/_snapshots/` | **Created** — point-in-time copies + manifests (G0) |
| `workspaces/_quarantine/` | **Created** — isolated broken/drifted workspaces (G0) |
| `workspaces/_recovery/` | **Created** — staged recovery trees (G0) |

Agent recursive delete **only** allowed under `_sandbox/` with snapshot (policy A-03).  
All other Q paths: **human-only delete**; agent write discouraged.

**Protocols:** [workspace-quarantine-protocol-v1.md](../protocols/workspace-quarantine-protocol-v1.md), [snapshot-manifest-standard-v1.md](../protocols/snapshot-manifest-standard-v1.md)

---

## 9. Operational risk tiers (G0 — maps to P0–P3)

Human-operated classification for scope-lock and agent prompts. **Does not replace** P0–P3 levels above — **extends** them for operational hardening.

### CRITICAL

| Path | P-level map | Required permissions |
|------|-------------|----------------------|
| `governance/` | P0 | Human confirmation; AGENT write **deny** default; Lane B + charter for bulk edits |
| `registry/` | P0 | Human confirmation; AGENT delete **deny** |
| `agents/` | P1 | Human confirmation; AGENT delete **deny** |
| `web-gpt-sources/` | P0 | Human confirmation; AGENT delete **deny** |
| `workspaces/_snapshots/` | Q (critical) | AGENT delete **deny**; write manifest only when task-scoped |
| `projects/mars-survivability/` | P1 | Human confirmation for structural changes; AGENT allowed for scoped Lane B tasks |

**Semantics:** Any write = minimum **HIGH RISK**; delete = **FORBIDDEN** for AGENT.

### HIGH

| Path | P-level map | Required permissions |
|------|-------------|----------------------|
| `projects/` | P1 | Lane B or scoped project task; no bulk cross-project edits |
| `mars-runtime/` | P1 (if present) | Lane B + explicit scope; SAFE UNKNOWN if path absent |
| `logs/` | P1-adjacent | Append-only discipline; AGENT may append survivability/incident logs when scoped |

**Semantics:** Writes = **LOW–MEDIUM RISK** with scope lock; cross-subtree = **HIGH RISK**.

### MEDIUM

| Path | P-level map | Required permissions |
|------|-------------|----------------------|
| `workspaces/` (production trees) | P2 | Lane A; **one** workspace per task scope lock; no delete-recreate |

**Exceptions (still MEDIUM path tier, higher op risk):**

- `workspaces/triumph-manipulator-landing-v4/`, `v5/` — treat edits as **MEDIUM RISK** minimum; snapshot before structural changes.
- `workspaces/_template-client-v1/` — template SoT; **LOW–MEDIUM RISK** writes.

**Semantics:** Production workspace mutation = scope lock mandatory; snapshot for MEDIUM RISK ops per [agent-operation-risk-classes-v1.md](../contracts/agent-operation-risk-classes-v1.md).

### Permission semantics summary

| Permission | Meaning |
|------------|---------|
| **Deny (agent delete)** | AGENT must not execute delete/recursive delete |
| **Deny (agent write) default** | Write only when ALLOWED PATHS lists exact subtree |
| **Human confirmation** | Operator acknowledges in task header before AGENT start |
| **Scope lock** | Mandatory allowlist in [safe-agent-task-template-v1.md](../templates/safe-agent-task-template-v1.md) |
| **Snapshot required** | MEDIUM RISK or higher on workspace paths |
| **Append-only** | logs/ — no rewrite of historical incident/rollback entries |

---

## 10. Tools directory

| Path | Level |
|------|-------|
| `tools/governance-scanner/` | P1 |
| `tools/markdown-link-validator/` | P1 |
| `tools/registry.md` | P0 via registry |

---

## 11. Change log

| Date | Change |
|------|--------|
| 2026-05-23 | v1 initial registry from audit |
| 2026-05-24 | G0 — Q zones created; CRITICAL/HIGH/MEDIUM tiers + permission semantics |
| 2026-06-29 | X0–X1 — canonical X-drive filesystem roots; deprecated C/D/E operational roots |

---

*End of Protected Zones Registry v1.*
