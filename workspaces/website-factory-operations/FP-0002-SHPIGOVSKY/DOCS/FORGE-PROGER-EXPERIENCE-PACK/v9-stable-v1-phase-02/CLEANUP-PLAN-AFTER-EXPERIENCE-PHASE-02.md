# Cleanup Plan — After Experience Pack Phase 02

**Status:** PLAN ONLY — execution requires a future explicit destructive charter  
**Prerequisite:** Phase 2 documentation reviewed; Stable v1 freeze intact  
**Policy:** [BACKUP-EVIDENCE-AND-CLEANUP-POLICY.md](./BACKUP-EVIDENCE-AND-CLEANUP-POLICY.md)  
**Inventory:** [CLEANUP-CANDIDATE-INVENTORY-PRE-PHASE.md](./CLEANUP-CANDIDATE-INVENTORY-PRE-PHASE.md)

---

## 1. Safe stages

| Stage | Action | Exit criteria |
|-------|--------|---------------|
| 1 | Verify documentation completeness | All Phase 2 files present; master index links OK; operator ACK |
| 2 | Re-verify Stable v1 freeze | Path exists; DB dump hash matches freeze docs; ROLLBACK.md present |
| 3 | Inventory + hash deletion candidates | Fresh size/hash list; diff vs Phase 2 inventory explained |
| 4 | Remove stale clean worktrees | Empty + superseded git-sync trees deleted; e63 only after remote verify |
| 5 | Remove obvious cache/log/temp | `debug.log` / regenerable temps; runtime smoke PASS |
| 6 | Remove superseded minor backups | Tiny E54–E62 checkpoints per allowlist; dry-run first |
| 7 | Consolidate evidence | Optional archive of unreferenced dumps; Git evidence retained |
| 8 | Verify runtime/source/DB after cleanup | Theme/plugin hash spot-check; key routes 200; DB tables intact |
| 9 | Create cleanup report | Paths deleted, sizes freed, hashes, stop events |
| 10 | Optional post-cleanup lightweight safety backup | Small manifest backup — **not** a replacement Stable freeze |
| 11 | **Do not alter** authoritative Stable v1 freeze | Freeze directory untouched |

Stages 4–7 require per-path allowlists. Never `Remove-Item -Recurse` on parent roots.

---

## 2. Safety gates (every destructive stage)

- [ ] Exact path allowlist (no globs that escape FP-0002 scope)
- [ ] Dry-run listing reviewed by operator
- [ ] Path validation on `X:` + `AI WS` volume
- [ ] Checkpoint/backup of metadata inventory CSV before delete
- [ ] Explicit operator approval for that stage
- [ ] Post-action audit (deleted list + remaining protected list)

---

## 3. Stop conditions (abort stage / escalate)

Stop immediately if any:

| Condition | Why |
|-----------|-----|
| Ambiguous ownership | Might delete foreign project |
| Missing replacement freeze | Would remove sole rollback |
| Unique evidence | Screenshot/report only lives there |
| Unknown operator asset | Incoming/original not promoted |
| Unverified DB dump | Cannot prove Stable DB still restorable |
| Source/runtime drift unexplained | Cleanup may hide product issues |
| Path outside exact FP-0002 scope | Boundary violation |
| Foreign project content | Monorepo / Storage collision |
| Hash mismatch on Stable freeze | Freeze integrity failure |
| Operator withdraws approval | Human gate |

---

## 4. Recommended first execution batch (future)

1. Empty worktrees `e38-e51`, `e58`  
2. Runtime `debug.log`  
3. Tiny intermediate backups (&lt;15 MB) from E54–E62 list marked DELETE_IN_CLEANUP_PHASE  
4. Stale large worktrees `e29*`, `push-divergence` after confirming no unique unpushed commits  

Defer: mid-size E59/E61 backups; pre-E54 mass delete; Stable/E58/E53/E63-pre; e63 worktree until remote re-check.

---

## 5. Forbidden in cleanup wave

- Deleting `v9-stable-v1-near-production-freeze-*`
- `git clean`, `git reset --hard`, force push
- `robocopy /MIR` or `/PURGE` against runtime/source
- Broad delete of `REPORTS/evidence` Git trees
- Demo content DB deletes (separate content charter)
- Any path under non-FP-0002 projects

---

## 6. Report template (for future cleanup report)

Must include: stage, allowlist, dry-run proof, operator approval ID/time, deleted paths+sizes, remaining protected freezes+hashes, runtime/source smoke, residual MANUAL_REVIEW list, disk freed.
