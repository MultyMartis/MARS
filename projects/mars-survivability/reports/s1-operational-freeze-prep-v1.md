# S1 Operational Freeze Prep (v1)

**Status:** Human-reviewed freeze assessment — documentation only  
**Date:** 2026-05-24  
**Purpose:** Classify survivability layer components before operational maintenance mode

---

## 1. Freeze intent

After G0–G4 + D-01/D-02 + S1 stabilization, **stop feature expansion**. Allowed work: consistency fixes, drill repetition, human-operated ops, chartered G5 experiments.

---

## 2. Stability classification

### Stable (baseline — maintain, do not redesign)

| Component | Rationale |
|-----------|-----------|
| contracts/destructive-operations-policy-v1.md | Incident-rooted; cross-referenced everywhere |
| contracts/agent-operation-risk-classes-v1.md | Canonical taxonomy |
| contracts/survivability-terminology-freeze-v1.md | S1 vocabulary lock |
| registries/enforcement-rules-registry-v1.md | G1 enforcement catalogue |
| registries/protected-zones-registry-v1.md | P0–P3 source of truth |
| registries/gitguard-system-entry-v1.md | Positioning anchor (post-S1 fix) |
| protocols/operational-halt-protocol-v1.md | Stop conditions |
| protocols/workspace-quarantine-protocol-v1.md | Quarantine-first (D-02 proven) |
| protocols/human-authority-protocol-v1.md | Operator supremacy |
| templates/safe-agent-task-template-v1.md | Scope lock standard |
| OPERATIONAL-INDEX.md + QUICKSTART.md | Navigation baseline |
| Infrastructure folders + READMEs | G0 layout |

### Experimental (proven in drill only — use with awareness)

| Component | Rationale |
|-----------|-----------|
| tools/validator/scoped-operation-validator-v1.mjs | D-01 validated; sandbox friction FP-01 |
| tools/helpers/*.mjs | Advisory; known label noise FP-S01 |
| tools/observability/*.mjs | D-01/D-02 used; Windows path edge FP-O01 |
| rollback-map-schema-v1.json + D-02 draft | First JSON draft; not production-incident proven |
| Drill workspaces in _quarantine/_snapshots | Retention policy SAFE UNKNOWN |

### Advisory only (never treat as enforcement)

| Component | Rationale |
|-----------|-----------|
| All G3 helpers and advisor docs | Recommend only; human executes |
| G4 observability outputs | Read-only signals |
| GitGuard advisory layer docs | Framework definition, not product |
| Validator ALLOW/DENY/NEED_HUMAN | Pre-check only — no shell hook |
| Scorecard v1 (2026-05-23) | Historical qualitative audit |

### Dangerous to evolve too early

| Area | Risk if rushed |
|------|----------------|
| Cursor hooks / beforeShellExecution | Silent block mythology; bypass fatigue |
| Automated snapshot copy | False confidence; partial mirror gaps |
| Registry JSON auto-sync | Hidden automation; drift masking |
| Production Triumph drill with AGENT | Production mutation risk |
| Autonomous rollback scripts | Amplifies incident class |
| Governance mass refactor linking survivability | Documentation gravity explosion |

### Must NOT be automated (S1 policy)

| Operation | Why human-only |
|-----------|----------------|
| Snapshot file copy | Partial mirror judgment (D-02 index.html case) |
| Restore / rollback execution | Irreversible; stress-sensitive |
| Quarantine promotion | Contamination spread risk |
| FORBIDDEN override | Requires APPROVED: + accountability |
| Governance/registry edits | CRITICAL zone |
| Commit / push | Operator decision per git-rules |
| Incident narrative closure | Human sign-off |

### Requires human-only discipline

| Discipline | Artefact |
|------------|----------|
| Scope lock every AGENT write | safe-agent-task-template |
| MEDIUM+ snapshot before mutation | enforcement-rules-registry |
| New chat on context drift | chat-context-drift-protocol |
| REPORT with SAFE UNKNOWN | AGENTS.md + recovery checklist |
| Drill in sandbox only | recovery-drill-protocol |
| No fix-on-top recovery | workspace-quarantine-protocol |

---

## 3. Maintenance mode rules (post-S1)

1. **No new large subsystems** without human charter.  
2. **Bug fixes** in tooling OK if behavior documented + drill note updated.  
3. **Doc changes** prefer QUICKSTART / OPERATIONAL-INDEX / terminology freeze alignment.  
4. **G5 experiments** require written charter referencing S1 checkpoint.  
5. **Scorecard** — do not update unless new full audit chartered.

---

## 4. Freeze boundaries vs governance Phase S3

| Layer | Role |
|-------|------|
| `governance/operational-survivability.md` | Phase S3 principles — frozen maintenance mode |
| `projects/mars-survivability/` | Lane B **operational pack** — S1 baseline frozen |

No duplication merge required — different altitude.

---

## 5. SAFE UNKNOWN

- Drill artifact retention duration  
- G5 hook experiment timeline  
- Operator formal sign-off on freeze

---

*End of S1 Operational Freeze Prep v1.*
