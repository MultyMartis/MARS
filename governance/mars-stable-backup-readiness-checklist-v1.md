# MARS Stable Backup Readiness Checklist v1

| Field | Value |
|-------|-------|
| **Status** | ACTIVE |
| **Scope** | MARS stable backup readiness before operator local full zip backup |
| **Current repo root** | `X:\AI MARS\` |
| **Current storage root** | `X:\AI MARS STORAGE\` |
| **Current local runtime root** | `X:\MARS-Localhost\` |
| **Branch** | `mars/canonical-post-recovery` |
| **Volume label** | AI WS |
| **Created from** | MASTER-16C |

---

## 1. Purpose

This checklist decides whether the current MARS state is safe to treat as a **stable recovery point** before the operator creates a **local full zip backup**.

It does **not**:

- run backups;
- clean files;
- delete WIP;
- replace Git, Storage, or Localhost backups.

MARS is documentation-first, human-supervised, and AI-assisted. MARS does **not** automatically create backups, enforce filesystem hygiene, or orchestrate archive creation. The operator performs the zip manually; this document only gates the **readiness decision**.

---

## 2. Backup layers

MARS recovery spans four distinct layers. Do not conflate them.

### 2.1 Git / Active Brain

- **Path:** `X:\AI MARS\`
- **Role:** tracked source of truth for committed governance, docs, and project code.
- **Requirements for stable backup declaration:**
  - `HEAD` aligned with `origin/mars/canonical-post-recovery` (or operator explicitly records intentional local-only commit state);
  - staged diff empty (`git diff --cached --name-only` → empty);
  - dirty working tree allowed **only if classified** at group level (see §5–§6).

Git alone does **not** capture untracked files, Storage contents, or Localhost runtime state.

### 2.2 Storage Layer

- **Path:** `X:\AI MARS STORAGE\`
- **Role:** evidence, archives, exports, large artifacts, project storage, incoming bulk material.
- **Not** fully represented by Git.
- Inclusion in operator zip must be **intentional** and noted in the backup manifest.

### 2.3 Local Runtime

- **Path:** `X:\MARS-Localhost\`
- **Role:** local CMS/runtime/DB state, dev servers, runtime caches.
- **Not** automatically represented by Git or Storage.
- May be large or volatile; operator may back up separately or with database export notes.

### 2.4 Operator full zip backup

- **Role:** manual local archive created by the operator (e.g. daily full zip).
- Should be made **only after** this readiness checklist is satisfied.
- Archive should include **explicitly chosen roots**; exclude transient trash **only by explicit operator choice**, not by silent agent cleanup.

**Deprecated / historical paths are not current backup authority:**

- `C:\AI MARS\`
- `C:\MARS Phenix\`
- `C:\AI MARS STORAGE\`
- `D:\MARS-Localhost\`
- `E:\MARS-Localhost\`

These may appear in recovery evidence; do **not** use them as default zip roots unless a separate destructive charter explicitly authorizes historical read-only capture.

---

## 3. Mandatory preflight before stable backup declaration

Run from `X:\AI MARS`:

```powershell
Get-Location
Get-Volume -DriveLetter X
Get-Volume -DriveLetter X | Select-Object DriveLetter,FileSystemLabel
git branch --show-current
git status --short
git diff --cached --name-only
git log --oneline origin/mars/canonical-post-recovery..HEAD
git rev-parse HEAD
git rev-parse origin/mars/canonical-post-recovery
git log -10 --oneline
```

### Expected (standard stable backup)

| Check | Expected |
|-------|----------|
| Workspace | `X:\AI MARS` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Staged diff | empty |
| `HEAD` vs `origin` | same SHA |
| Ahead list | empty |

**Exception:** If the operator intentionally keeps unpushed local commits, record that state explicitly in the backup manifest (§8) and use decision label `BACKUP_READY_WITH_KNOWN_WIP` or defer until push is complete.

---

## 4. Stable backup STOP conditions

Do **not** declare a stable backup if any of the following apply:

| STOP token / condition | Meaning |
|------------------------|---------|
| **STOP — X VOLUME IDENTITY OR WORKSPACE MISMATCH** | Wrong drive, volume label not `AI WS`, or workspace outside `X:\AI MARS` |
| **STOP — WRONG BRANCH** | Not on `mars/canonical-post-recovery` without explicit operator record |
| **STOP — EXISTING STAGED CHANGES PRESENT** | Staged diff not empty |
| **STOP — UNPUSHED COMMITS PRESENT** | Local commits ahead of origin unless explicitly recorded in manifest |
| **STOP — REMOTE/HEAD MISMATCH** | `HEAD` ≠ `origin/mars/canonical-post-recovery` without documented reason |
| Unknown destructive operations pending | Scheduled delete, mirror, purge, or migration not yet completed or chartered |
| Unresolved authority conflict | Competing path authority (e.g. old C:/D:/E: roots treated as active) |
| Storage or Localhost root unavailable | Planned inclusion but path missing, unmounted, or inaccessible |
| Foreign WIP not inventoried at high level | Large modified/untracked mass with no group-level summary |
| Active risky cleanup/migration in progress | Agent or operator mid-cleanup, mid-restore, or mid-migration |
| Agent-produced files not yet classified | Major lane just finished; outputs not grouped (held / include / exclude) |
| Operator unsure which roots are being zipped | Backup root list not explicit |

When any STOP condition applies, use decision label `BACKUP_NOT_READY_FIX_REQUIRED` or `BACKUP_NOT_READY_SAFE_UNKNOWN` (§11).

---

## 5. Foreign WIP handling

**Foreign WIP is allowed, but must be known.**

Stable backup does **not** require a clean working tree. It requires **classified awareness** of dirty and untracked state.

### High-level WIP groups

Classify at group level (not necessarily file-by-file):

| Group | Examples |
|-------|----------|
| Modified tracked files | In-progress commits not yet staged or pushed |
| Untracked project work | New lanes, pilots, evidence trees |
| Generated/runtime artifacts | `node_modules/`, build output, browser profiles, `__pycache__/` |
| Checkpoint/forensic evidence | Audit JSON, validation receipts, probe output |
| Backups / `.bak` / `.tmp` | Pre-migration snapshots, restore temp |
| Separate client lanes | Drive Avenue, FP-0002, OCPilot site work |
| Held residuals | Known excluded or held JSON, duplicate inventories |
| Safe unknown | Unreviewed paths — blocks `BACKUP_READY_STANDARD` |

### Rules

- **Do not** delete WIP for backup cleanliness.
- **Do not** run `git clean`, `git reset`, broad `git add`, or `Remove-Item` sweeps before backup.
- **Do not** stage broad WIP to “freeze” state unless a separate commit charter authorizes it.
- **Do not** include or exclude WIP silently — document inclusion in the operator zip plan and manifest.
- Preserve foreign WIP; backup captures what exists, not what “should” exist after cleanup.

---

## 6. What is backup-ready

**Backup-ready does not mean clean tree.**

**Backup-ready means:**

- current authority is clear (`X:\` roots, volume `AI WS`, canonical branch);
- latest **intended** Git commits are pushed (or deviation is recorded);
- staged diff is empty;
- dirty/untracked state is **known at group level** (§5);
- no active destructive operation is in progress;
- Storage and Localhost inclusion/exclusion is **intentional**;
- backup root list is **explicit** (§7);
- operator can restore with **known caveats** documented in manifest (§8).

A repo may be operationally dirty (modified + untracked foreign WIP) and still qualify as `BACKUP_READY_WITH_KNOWN_WIP` if all STOP conditions are clear and WIP groups are summarized.

---

## 7. Recommended operator backup roots

### Default roots (current authority)

| Root | Include when |
|------|--------------|
| `X:\AI MARS\` | Always (Active Brain / Git repo) |
| `X:\AI MARS STORAGE\` | When bulk evidence and archives must be recoverable with Brain |
| `X:\MARS-Localhost\` | When local CMS/runtime/DB state must be recoverable |

### Notes

- If Localhost is large or volatile, operator may back it up **separately** or pair zip with database export notes in the manifest.
- Do **not** default to old `C:\`, `D:\`, or `E:\` MARS roots.
- Exclusions (e.g. transient `_chrome-profile-tmp/`, portable node bundles) must be **listed explicitly** in the manifest, not assumed.

---

## 8. Minimal backup manifest

Create a small **human-readable note** next to the zip archive (manual today; automation optional in future). Do **not** implement manifest generation in this checklist wave.

### Recommended fields

```text
Date/time:
Archive filename:
Included roots:
Excluded roots (if any):
Repo HEAD (full SHA):
Origin HEAD (full SHA):
Branch:
Latest 5 commits (one line each):
Staged diff status: empty / not empty
High-level dirty/untracked summary:
  - modified tracked groups:
  - untracked groups:
Storage included: yes / no
Localhost included: yes / no
Known caveats:
Operator initials / confirmation:
```

The manifest is evidence that the operator knew **what** was captured and **what caveats** apply on restore.

---

## 9. Backup safety rules

- Backup is **not** cleanup.
- Backup is **not** migration.
- Backup is **not** `git commit`.
- Backup is **not** `git clean`.
- Do **not** delete files before backup unless a **separate destructive charter** explicitly authorizes deletion with dry-run and rollback plan.
- Do **not** overwrite old backups silently — use dated filenames or folders.
- Keep **at least one previous backup** when making a new stable backup.
- When possible, maintain **one off-disk / off-machine copy** later (see MASTER-16 finding F-013: off-disk redundancy may still be pending).

MARS does **not** provide an automatic backup engine. The operator owns archive creation, naming, retention, and off-disk copies.

---

## 10. Current known held groups after MASTER-16

The following are **examples / current known groups** as of MASTER-16 audit context. **Not exhaustive** — operator must refresh group summary at backup time.

### Search PPC / Corvonero held residuals

| Item | Notes |
|------|-------|
| 7 excluded V2 JSON | Corvonero campaign V2.x phrase authority variants held outside commit scope |
| Duplicate inventory reports | e.g. `REPORT-projects-projects-duplicate-tree-inventory-v1` |
| Drive Avenue separate lane | Distinct client/project lane — classify include/exclude explicitly |
| `.tools-test-output` | Generated test output under Search PPC |
| `.tools` checkpoint JSON | e.g. corvonero checkpoint / pre-export summaries |
| Node runtime bundles | e.g. `.tools/node-portable/`, `.tools/node-runtime/` |

### Foreign WIP outside Search PPC

| Item | Notes |
|------|-------|
| FP-0002 / Website Factory work | Modified tracked + validation receipts under `workspaces/`, `projects/mars-website-factory/` |
| OCPilot backups | `.bak` snapshots under `projects/ocpilot/sites/` |
| `.recovery-temp` / restore temp | Forensic/restore scratch — large untracked tree |
| Other untracked or modified project work | Additional lanes per `git status --short` at backup time |

Mark each group in the manifest as **included in zip**, **held outside zip**, or **known residual — restore caveat**.

---

## 11. Decision labels

Use exactly one primary label per readiness check:

| Label | When to use |
|-------|-------------|
| `BACKUP_READY_STANDARD` | All preflight checks pass; WIP classified; no unresolved STOP; intended roots clear |
| `BACKUP_READY_WITH_KNOWN_WIP` | Git/authority gates pass; significant dirty/untracked WIP documented; operator accepts restore caveats |
| `BACKUP_NOT_READY_FIX_REQUIRED` | STOP condition fixable (unpushed commits, staged diff, wrong branch, missing root, etc.) |
| `BACKUP_NOT_READY_SAFE_UNKNOWN` | Critical state unknown (unclassified WIP mass, authority conflict, unclear zip scope) |
| `BACKUP_DEFERRED_BY_OPERATOR` | Operator chooses to defer zip after review (maintenance window, disk space, etc.) |

---

## 12. Pre-backup report template

Copy and fill before creating the operator zip:

```markdown
# REPORT — MARS Stable Backup Readiness Check

## Result

## Git / Brain state

- Workspace:
- Volume label:
- Branch:
- HEAD:
- Origin HEAD:
- Ahead commits:
- Staged diff:
- High-level modified groups:

## Storage state

- Path accessible:
- Included in zip:
- Notes:

## Localhost state

- Path accessible:
- Included in zip:
- DB export notes (if any):

## Foreign WIP summary

-

## Included roots

-

## Excluded roots

-

## STOP conditions

- None / list:

## Decision

(one of: BACKUP_READY_STANDARD | BACKUP_READY_WITH_KNOWN_WIP | BACKUP_NOT_READY_* | BACKUP_DEFERRED_BY_OPERATOR)

## Operator backup note

- Archive filename:
- Manifest saved: yes / no
- Previous backup retained: yes / no
```

---

## 13. Relationship to other docs

| Document | Relationship |
|----------|--------------|
| [.cursorrules](../.cursorrules) | Filesystem denials, no cleanup-for-backup, foreign WIP preserve |
| [AGENTS.md](../AGENTS.md) | Session preflight, backup readiness mention, task closeout |
| [mars-normal-operations-resumption-checklist-v1.md](mars-normal-operations-resumption-checklist-v1.md) | Daily/session gates; complements but does not replace backup readiness |
| [mars-disaster-recovery-2026-06-24-closure-v1.md](mars-disaster-recovery-2026-06-24-closure-v1.md) | DR closure context; immutable recovery anchor |
| [mars-x-drive-root-authority-v1.md](mars-x-drive-root-authority-v1.md) | Canonical `X:\` root authority |
| [web-gpt-sources/mars-current-x-drive-2026-06/](../web-gpt-sources/mars-current-x-drive-2026-06/) | X-drive migration evidence pack |
| [projects/mars-survivability/guardrails/cursor-agent-guardrails-v1.md](../projects/mars-survivability/guardrails/cursor-agent-guardrails-v1.md) | Agent STOP tokens and session header |

This checklist addresses MASTER-16 finding **F-003** (no system-level backup readiness gate). It does not resolve **F-013** (off-disk redundancy) or **F-009** (untracked evidence in Git-only restore) by itself — it makes those caveats **visible** in the manifest.

---

## Revision history

| Version | Date | Notes |
|---------|------|-------|
| v1 | 2026-07-05 | Initial checklist — MASTER-16C |
