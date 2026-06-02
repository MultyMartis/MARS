# Survivability Terminology Freeze (v1)

**Status:** **documented** — canonical vocabulary for MARS survivability layer (S1 baseline).  
**Not:** automated terminology enforcement, linter product, or governance expansion.

**Scope:** `projects/mars-survivability/` and cross-references from MARS ecosystem docs.  
**Supersedes:** ad-hoc phrasing in individual artefacts where conflict exists — update those artefacts on next touch, not retroactive mass edit.

---

## 1. Purpose

Freeze terminology after G0–G4 + D-01/D-02 to prevent semantic drift, runtime mythology, and duplicate definitions across GitGuard, validator, and governance docs.

---

## 2. Canonical terms

| Term | Definition | Notes |
|------|------------|-------|
| **survivability** | Ability of MARS (human-operated, documentation-first) to stay coherent across sessions: continuity, anti-drift, honest unknowns, recoverability without fake runtime | Broader governance sense: [governance/operational-survivability.md](../../../governance/operational-survivability.md). Lane B pack = operational execution layer. |
| **quarantine** | Isolation of suspect workspace/tree under `workspaces/_quarantine/` for human review before any promotion or merge | **Not** delete-in-place repair. Protocol: [workspace-quarantine-protocol-v1.md](../protocols/workspace-quarantine-protocol-v1.md) |
| **rollback** | Human-operated return to known-good state using git refs, snapshot copies, and documented steps | **Not** automatic reversion. Logs: `logs/rollback-history/` |
| **restore** | Human copy or checkout of files from snapshot or git to a target workspace (prefer new workspace) | Distinct from rollback planning docs |
| **snapshot** | Point-in-time copy of scope paths + `SNAPSHOT-MANIFEST.md` under `workspaces/_snapshots/` | Helper drafts manifest; **human** copies files |
| **drift** | Divergence between intent and reality: context drift (chat), registry drift (doc vs JSON), path drift, semantic drift | Detection = advisory (G4); correction = human |
| **validator** | `scoped-operation-validator-v1.mjs` — read-only CLI emitting ALLOW / DENY / NEED_HUMAN | Manual invoke; **no** shell interception in baseline |
| **helper** | Advisory script or doc assisting operator (snapshot-helper, scope-analyzer, diff/rollback advisors) | **No** autonomous execution |
| **observability** | Read-only signals after work (diff reports, integrity checks, drift linter) | **Not** control plane — [observability-philosophy-v1.md](observability-philosophy-v1.md) |
| **protected zone** | Path tier P0–P3 with CRITICAL/HIGH/MEDIUM labels — [protected-zones-registry-v1.md](../registries/protected-zones-registry-v1.md) | Validator JSON mirrors subset — manual sync |
| **operational halt** | Mandatory AGENT stop when FORBIDDEN op, incomplete snapshot, ambiguity, or incident — [operational-halt-protocol-v1.md](../protocols/operational-halt-protocol-v1.md) | Human-enforced |
| **scope lock** | Explicit ALLOWED / FORBIDDEN path list in task header — [safe-agent-task-template-v1.md](../templates/safe-agent-task-template-v1.md) | Required for AGENT writes |
| **advisory tooling** | GitGuard-aligned helpers + validator + observability — recommend, report, draft; operator executes | Correct phrase: "advisory tooling **recommended** X; operator did Y" |
| **human authority** | Operator is sole execution authority; AGENT bounded — [human-authority-protocol-v1.md](../protocols/human-authority-protocol-v1.md) | APPROVED: line required for MEDIUM+ mutations |

---

## 3. Risk class vocabulary (frozen)

Use **exact** labels from [agent-operation-risk-classes-v1.md](agent-operation-risk-classes-v1.md):

`SAFE` · `LOW RISK` · `MEDIUM RISK` · `HIGH RISK` · `CRITICAL` · `FORBIDDEN`

**Do not** mix with legacy R1–R4 labels in new docs except when citing [safe-execution-layer-v1.md](../protocols/safe-execution-layer-v1.md) git/FS tiers (R3 git destructive, R4 FS destructive) — prefer risk-class table for new material.

---

## 4. GitGuard vocabulary (frozen)

**GitGuard (MARS survivability context)** = **advisory survivability framework** combining validators, helpers, manifests, rollback guidance, and human authority.

| Say | Do not say |
|-----|------------|
| GitGuard advisory layer | GitGuard deployed / GitGuard blocked / GitGuard recovered |
| GitGuard-aligned tooling | GitGuard product / GitGuard runtime |
| Human-operated GitGuard evolution | GitGuard autonomous agent |
| Design contract for future pack | GitGuard is implemented (no `projects/gitguard/` pack) |

---

## 5. FORBIDDEN terminology

These phrases **must not** appear as claims about current MARS survivability capabilities:

| Forbidden term | Why |
|----------------|-----|
| **autonomous recovery** | No auto-restore; human-operated only |
| **self-healing** | No workspace rebuild without human |
| **self-repair** | No automatic manifest/snapshot repair |
| **orchestration runtime** | No multi-agent router in survivability layer |
| **intelligent cleanup** | No heuristic delete automation |
| **automatic healing** | Same as self-healing |
| **autonomous rollback** | Rollback is human-led with optional advisor docs |

**Allowed context:** listing these as **non-goals** or **forbidden claims** (as in this document).

---

## 6. SAFE UNKNOWN (frozen usage)

**SAFE UNKNOWN** = evidence missing; default is **deny / halt / NEED_HUMAN** — **not** "allowed because unknown".

Do not use SAFE UNKNOWN to imply implementation exists.

---

## 7. Phase labels (frozen)

| Label | Meaning |
|-------|---------|
| **G0–G4** | Delivered survivability layers (documented + human-operated tooling where noted) |
| **G5+** | Chartered future work — hooks (suggest-only), CLI rollback-map validator, scheduled snapshots |
| **D-01 / D-02** | Sandbox drill ids — evidence in `logs/survivability/` and `reports/` |
| **S1** | Stabilization checkpoint — baseline freeze, no feature expansion |

---

## 8. Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | S1 — terminology freeze v1 |

---

*End of Survivability Terminology Freeze v1.*
