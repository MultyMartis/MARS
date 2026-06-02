# OCPilot — Baseline Storage Migration Plan

**Run:** 3.7 — External Storage Architecture  
**Status:** documentation only — **migration not executed** in this run.

---

## Goal

Eventually move or recreate promoted baseline trees from repo-local paths:

```
C:\AI MARS\projects\ocpilot\baselines\<baseline-id>\files\
```

to external canonical storage:

```
C:\AI MARS STORAGE\ocpilot\baselines\<baseline-id>\files\
```

Canonical ZIP archives should likewise reside under:

```
C:\AI MARS STORAGE\ocpilot\baselines\
```

(or `incoming\` during quarantine, then `baselines\` after verification).

**Not in Run 3.7.** Run 3.5 grandfathered trees (~7608 files across two READY baselines) remain untouched.

---

## Scope (when migration runs)

| Baseline | Repo-local today | External target |
|----------|------------------|-----------------|
| `ocstore-3038-rs2` | `files/` (4055 files), ZIP in `incoming/baselines/` | `C:\AI MARS STORAGE\ocpilot\baselines\ocstore-3038-rs2\` |
| `ocstore-3039-rs1` | `files/` (3553 files), ZIP in `incoming/baselines/` | `C:\AI MARS STORAGE\ocpilot\baselines\ocstore-3039-rs1\` |

---

## Safe migration approach

Human-operated gates only. No automation claimed.

### Step 1 — Confirm current ZIP hashes

- Verify SHA256 of `opencart-3.0.3.8-rs.zip` and `opencart-3.0.3.9-rs.zip` against passport and manifest records.
- If hash mismatch, **stop** — re-acquire or reconcile before any move.

### Step 2 — Recreate promoted baseline tree in external storage from ZIP

- Extract canonical ZIP to `C:\AI MARS STORAGE\ocpilot\temp\` (scratch).
- Promote sanitized tree to `C:\AI MARS STORAGE\ocpilot\baselines\<baseline-id>\files\` using same rules as Run 3.5 ([baseline-promotion-strategy.md](baseline-promotion-strategy.md)).
- **Do not move** repo-local tree by rename alone — recreate from ZIP so external copy is provably canonical.

### Step 3 — Compare file counts and key manifests

- Compare file count: external `files/` vs repo-local `files/` vs manifest path counts.
- Spot-check critical paths (admin, catalog, system) listed in manifest.
- Record comparison note in `comparison-notes/` if any delta found.

### Step 4 — Update passports with external paths

- Add `external_zip_path` and `external_promoted_path` (or equivalent fields) to baseline passports.
- Record SHA256 and migration date in passport or version notes.

### Step 5 — Update readiness reports

- Amend or add readiness recheck documenting external storage as canonical bulk location.
- Confirm READY status still valid after migration.

### Step 6 — Remove repo-local promoted files (approval required)

- **Only after** operator explicit approval and Steps 1–5 pass.
- Remove `projects/ocpilot/baselines/<id>/files/` content — not before external copy verified.
- Optional: retain empty `files/` with README pointer to external path.

### Step 7 — Never delete canonical ZIP without operator approval

- Repo-local ZIP in `incoming/baselines/` may remain as working copy until operator confirms external canonical copy.
- External ZIP is canonical; deletion of any ZIP copy requires explicit operator decision.

---

## What Run 3.7 does not do

| Action | Run 3.7 |
|--------|---------|
| Move promoted `files/` trees | **No** |
| Move incoming ZIPs | **No** |
| Delete repo-local bulk | **No** |
| Update passports with external paths | **No** (optional operator follow-up) |
| Modify `.gitignore` | **No** |
| Git commit | **No** |

---

## Prerequisites before migration run

- [ ] External folder structure exists — **done** (Run 3.7)
- [ ] [external-storage-registry.md](external-storage-registry.md) approved
- [ ] Operator charter for migration run (separate from Run 3.7)
- [ ] Backup copy in `C:\AI MARS STORAGE\ocpilot\backups\` if operator requires

---

## Risks if migration skipped indefinitely

- Repo working tree remains large (~7600+ untracked files under `projects/ocpilot/`).
- First git commit must still exclude bulk per [git-storage-policy.md](git-storage-policy.md).
- Clone/copy of MARS repo carries local bulk unless `.gitignore` applied — policy documented, not enforced in Run 3.7.

---

## Related documents

| Doc | Role |
|-----|------|
| [external-storage-registry.md](external-storage-registry.md) | Target paths |
| [recommended-storage-model.md](recommended-storage-model.md) | Option D model |
| [run-3.5-readiness-recheck.md](run-3.5-readiness-recheck.md) | Current READY state |
| [storage-audit-run-3.6.md](storage-audit-run-3.6.md) | Size evidence |
