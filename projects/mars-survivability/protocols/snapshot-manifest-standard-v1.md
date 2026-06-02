# Snapshot Manifest Standard (v1)

**Status:** **documented** — normative format for workspace snapshots under `workspaces/_snapshots/`.  
**Not:** automated snapshot tooling, enforced schema validator, or backup product.

**Template:** [../templates/snapshot-manifest-template.md](../templates/snapshot-manifest-template.md)  
**Storage:** [../../../workspaces/_snapshots/README.md](../../../workspaces/_snapshots/README.md)

---

## 1. Purpose

Every snapshot directory **must** contain a manifest file named `SNAPSHOT-MANIFEST.md` at its root. The manifest is the **human-operated** record that makes a snapshot restorable and auditable.

Without a complete manifest, a snapshot is **incomplete** — do not rely on it for recovery.

---

## 2. Required fields

| Field | Required | Format / rules |
|-------|----------|----------------|
| **snapshot id** | Yes | Unique string matching directory name: `snap-<YYYYMMDD>-<HHMMSS>-<workspace-slug>-<short-reason>` |
| **workspace** | Yes | Source workspace absolute path at snapshot time |
| **timestamp** | Yes | ISO-8601 UTC (e.g. `2026-05-24T14:30:22Z`) |
| **reason** | Yes | One-line operational reason (pre-refactor, pre-migration, incident freeze, drill, etc.) |
| **risk class** | Yes | One of: SAFE, LOW RISK, MEDIUM RISK, HIGH RISK, CRITICAL — per [agent-operation-risk-classes-v1.md](../contracts/agent-operation-risk-classes-v1.md) |
| **pre-operation state** | Yes | Brief factual state: git branch, dirty/clean, known issues, active task id |
| **restore instructions** | Yes | Step-by-step human restore path (selective copy targets, order, verification) |
| **forbidden operations after snapshot** | Yes | Explicit list of ops that must not run until restore verified or snapshot retired |
| **operator** | Yes | Human identifier (name or handle) who authorized snapshot |
| **git state** | Yes | `git status` summary, branch, HEAD short hash; note untracked if relevant |
| **SAFE UNKNOWN** | If applicable | Fields that could not be verified — **do not infer** |

---

## 3. Optional fields

| Field | When to include |
|-------|-----------------|
| **task / chat reference** | Cursor chat id, lane, task name |
| **scope lock excerpt** | Allowed paths from agent prompt |
| **file count / size estimate** | Large snapshots |
| **integrity checksum** | Future helper layer — mark SAFE UNKNOWN if not computed |
| **linked incident** | Path to `logs/incidents/` or survivability report |
| **retention tier** | Active / Reference / Incident-linked / Drill |

---

## 4. Naming and placement

```
workspaces/_snapshots/
  snap-20260524-143022-triumph-v4-pre-refactor/
    SNAPSHOT-MANIFEST.md
    <mirrored workspace tree>
```

- Manifest filename is fixed: `SNAPSHOT-MANIFEST.md` (uppercase).  
- Do not nest manifests outside snapshot root.  
- One manifest per snapshot directory.

---

## 5. Creation workflow (operator)

1. Identify risk class of planned operation — if MEDIUM RISK or higher → snapshot required.  
2. Create timestamped directory under `_snapshots/`.  
3. Copy workspace tree (or declared subtree) — **copy, not move**.  
4. Fill template from live `git status` and operator knowledge.  
5. Record snapshot id in active task REPORT.  
6. Optional: append one-line entry to `logs/survivability/`.

---

## 6. Validation before restore

Before using a snapshot for restore:

| Check | Pass criteria |
|-------|---------------|
| Manifest present | `SNAPSHOT-MANIFEST.md` exists and all required fields filled |
| snapshot id match | Directory name matches manifest `snapshot id` |
| workspace match | Target restore path matches or is documented successor |
| git state understood | Operator knows whether snapshot includes untracked files |
| SAFE UNKNOWN reviewed | Unknowns acknowledged; restore plan accounts for gaps |

If validation fails → **do not restore**; create new snapshot or use git recovery.

---

## 7. Agent rules

| Action | AGENT |
|--------|-------|
| Read manifest | Allowed (read-only audit) |
| Write manifest | Allowed only when task explicitly requires snapshot + scope includes `_snapshots/` |
| Delete snapshot | **FORBIDDEN** |
| Restore from snapshot | Human executes copy; AGENT assists read-only unless explicit scoped restore task |

---

## 8. Signals

| Signal | When |
|--------|------|
| **INCOMPLETE SNAPSHOT** | Manifest missing or required field empty |
| **NEED HUMAN APPROVAL** | Restore touches production workspace |
| **SAFE UNKNOWN** | git state, file completeness, or integrity not verified |

---

## 9. Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — G0 operationalization |

---

*End of Snapshot Manifest Standard v1.*
