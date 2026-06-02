# Rollback Advisor (v1)

**Status:** **documented** — human rollback guidance.  
**Not:** rollback engine, auto-restore, or git automation product.

**Related:** [snapshot-manifest-standard-v1.md](../../protocols/snapshot-manifest-standard-v1.md), [workspace-quarantine-protocol-v1.md](../../protocols/workspace-quarantine-protocol-v1.md), [snapshot-helper-v1.mjs](snapshot-helper-v1.mjs)

---

## 1. Purpose

Guide operators on **when** and **how** to roll back — and when **not** to — without executing rollback automatically.

---

## 2. What rollback advisor is

| Is | Is not |
|----|--------|
| Decision framework | `git reset --hard` runner |
| Restore ordering checklist | Snapshot copier |
| Quarantine-first philosophy | Self-healing recovery |

---

## 3. When rollback is recommended

| Situation | Rollback type |
|-----------|---------------|
| AGENT changed files outside scope lock | Selective restore from snapshot or `git checkout -- <path>` |
| Build broken after bounded edit | Restore `src/` from snapshot; regen dist |
| Wrong file mass-replaced | Snapshot selective copy — **not** repo-wide git clean |
| Pre-deploy regression found | Snapshot with Active retention tier |
| Incident freeze | Restore to Incident-linked snapshot; log in `logs/rollback-history/` |

**Prerequisites:**

- Snapshot exists with complete `SNAPSHOT-MANIFEST.md`, **or**  
- Changes are tracked and single-file `git checkout --` is sufficient.

---

## 4. When NOT to rollback (immediately)

| Situation | Preferred action |
|-----------|------------------|
| Unknown dirty state + unknown snapshot quality | Halt — assess; do not guess |
| Contaminated workspace (scope escape + more edits) | **Quarantine-first** — move to `_quarantine/` |
| Missing manifest / incomplete snapshot | **SAFE UNKNOWN** — do not trust copy |
| “Start fresh” / delete-recreate urge | **Forbidden** (F-10) — clone-first / quarantine |
| Governance/registry accidental edit | Human Lane B review — not blind revert |
| Triumph v4/v5 structural uncertainty | Quarantine + selective restore — no workspace delete |

---

## 5. Partial rollback risks

| Risk | Mitigation |
|------|------------|
| Restoring only HTML but not paired CSS/JS | Restore coherent subtree from snapshot |
| Mixing snapshot A files with live B files | One snapshot per restore operation |
| Partial `git checkout` leaving broken refs | List all coupled paths in manifest |
| Restoring `dist/` without `src/` | Prefer regen from restored `src/` |
| AGENT continues during restore | Stop AGENT first |

---

## 6. Contaminated workspace handling

**Contamination** = changes outside scope lock, cross-workspace touches, or unknown file set.

1. **Stop** AGENT.  
2. **Do not** add more fixes on top.  
3. Move workspace to `workspaces/_quarantine/<name>-<date>-<reason>/` (human copy/move).  
4. Compare quarantine tree vs last good snapshot (diff advisor).  
5. Plan **selective** promote from snapshot or `_recovery/` staging.  
6. Append narrative to `logs/incidents/` if operational impact.

---

## 7. Quarantine-first philosophy

```
Detect problem → Halt → Quarantine → Analyze diff → Selective restore → Verify → Promote
```

**Never:** delete production workspace and recreate as “recovery.”

---

## 8. Restore ordering (recommended)

1. Stop AGENT / close task.  
2. Record incident note (if applicable).  
3. Locate snapshot id from REPORT or `_snapshots/`.  
4. Read `SNAPSHOT-MANIFEST.md` restore instructions.  
5. Verify manifest git state vs current (branch drift OK if documented).  
6. Copy **from snapshot to production** — file-by-file or subtree — human operation.  
7. Run build/lint verification manually.  
8. `git diff` post-restore — confirm expected state.  
9. Append `logs/rollback-history/rollback-YYYYMMDD-<slug>.md`.  
10. New chat if context drift suspected.

---

## 9. Git vs snapshot rollback

| Method | Use when |
|--------|----------|
| `git checkout -- <tracked-path>` | Single known tracked file; clean scope |
| `git revert <commit>` | After commit; user requested commit already |
| Snapshot copy | Untracked assets, multi-file, dist bundles, workspace trees |
| **Avoid** `git reset --hard`, `git clean` | AGENT forbidden; human at keyboard only with warning |

---

## 10. Rollback importance (from snapshot-helper)

| Level | Meaning |
|-------|---------|
| low | Git revert likely enough |
| medium | Snapshot recommended; document restore path |
| high | Snapshot required; written plan before mutation |
| critical | Quarantine-ready; no AGENT mutation on recovery |

---

## 11. SAFE UNKNOWN

- Whether snapshot copy is byte-complete — operator verifies.  
- Cloud/off-repo backups — out of MARS survivability scope unless documented.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | G3 — rollback advisor v1 |

---

*End of Rollback Advisor v1.*
