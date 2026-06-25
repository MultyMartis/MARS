# MARS Phoenix — Branch integration decision v1

**Status:** **documented** — operator decision record; **integration not executed**.  
**Date:** 2026-06-25  
**Supersedes:** branch-integration section of [mars-phoenix-recovery-cutover-receipt-v1.md](mars-phoenix-recovery-cutover-receipt-v1.md) (status only).

---

## Git anchors (verified 2026-06-25)

| Field | Value |
|-------|-------|
| **Recovery branch** | `recovery/mars-phenix-2026-06-25` |
| **Recovery HEAD (local = remote)** | `de1a4d1bb1f417f5af0ae43a864dfeb321e503e6` |
| **Old forward branch (remote)** | `mars/post-cycle8-live-tests` @ `f78af433f8878f7523ae933ba9fb9986b18533f8` |
| **Old forward branch (local stale)** | `84b9a8c77dd9472bea6b23e6ec327ba3081c3615` — operator must not use legacy `C:\AI MARS` checkout as forward SHA authority |
| **Merge-base** | `84b9a8c77dd9472bea6b23e6ec327ba3081c3615` |
| **Recovery-only commits** | 2 (`eb2ca922` reconstruction, `de1a4d1` Phoenix paths + runtime pass 2) |
| **Forward-only commits (remote vs recovery)** | 23 linear commits after merge-base |
| **Cherry overlap** | **None** — recovery is a reconstruction squash; forward history is parallel post-parent |

---

## Default branch (remote metadata)

| Field | Value |
|-------|-------|
| **GitHub `HEAD branch`** | `main` (`219d609a` — NOVA Reality Root Recovery v1) |
| **Production coupling** | **SAFE UNKNOWN** — no in-repo CI/workflows bind deployment to `main` or forward branch |
| **Branch protection** | **SAFE UNKNOWN** — `gh` CLI unavailable in operator session; not inferred |

---

## Strategy comparison

| Strategy | Summary | Verdict |
|----------|---------|---------|
| **A — Keep `recovery/mars-phenix-2026-06-25` as permanent canonical** | Remote recovery confirmed; reconstruction receipts unambiguous | **Viable** — temporary branch name |
| **B — New permanent branch from recovery HEAD; keep recovery as immutable anchor** | Clean name; no merge; recovery branch frozen as evidence | **Recommended** |
| **C — Force old forward pointer to recovery state** | Rewrites `mars/post-cycle8-live-tests` history expectations | **Rejected** — high risk, requires explicit charter |
| **D — Ordinary merge old forward into recovery** | Would replay 23 commits against 1541-file reconstruction delta | **Rejected / deferred** — double-apply and deletion-hold risk |

---

## Why ordinary merge is rejected (deferred)

1. **Double application** — Recovery commit `eb2ca922` already consolidated ~23 forward commits plus backup dirty WIP, backup-only sources, Wave 4 semantic merges, and post-HEAD FP-0002 WIP.
2. **Deletion-hold** — Recovery intentionally retained 36 deletion-hold paths; forward merge may reintroduce destructive deletions.
3. **Backup dirty conflicts** — 211+ backup dirty paths in recovery vs linear forward history.
4. **Semantic merge integrity** — Wave 4 MLI/BZPM/OCPilot/ORCA merges are not replay-safe via git merge.
5. **Ancestry noise** — Merge would create misleading ancestry without adding authoritative state.
6. **Corvonero runtime drift** — Forward branch contains post-incident Corvonero/Orca tooling; recovery tree is the validated Phoenix authority.
7. **Legacy checkout hazard** — `C:\AI MARS` at `f78af433` with dirty WIP is evidence, not integration target.

---

## Recommended permanent canonical strategy

**Strategy B:**

1. Retain `recovery/mars-phenix-2026-06-25` @ `de1a4d1` (and subsequent recovery commits) as **`IMMUTABLE_RECOVERY_ANCHOR`**.
2. After operator approval, create a new permanent branch (e.g. `mars/canonical-post-recovery`) **from recovery HEAD** — **no merge** with `mars/post-cycle8-live-tests`.
3. Optionally update GitHub default branch **only** after operator charter — **not** part of this receipt.
4. Mark `mars/post-cycle8-live-tests` as **`LEGACY_FORWARD_LINE`** — read-only reference; do not delete without archival plan.

---

## Branch integration status

| Item | Status |
|------|--------|
| Merge / rebase / cherry-pick | **NOT EXECUTED** |
| Default branch change | **NOT EXECUTED** |
| Permanent canonical branch creation | **PENDING operator approval** |
| Recovery branch push authority | **CONFIRMED** |

---

## Explicit next operator decision

**Approve creation of a permanent canonical branch from verified recovery HEAD (`de1a4d1` or later), while retaining `recovery/mars-phenix-2026-06-25` as an immutable recovery anchor; defer any merge with `mars/post-cycle8-live-tests`.**

---

## Related

| Topic | Path |
|-------|------|
| Recovery cutover receipt | [mars-phoenix-recovery-cutover-receipt-v1.md](mars-phoenix-recovery-cutover-receipt-v1.md) |
| Control reports | `C:\MARS Phenix\_reconstruction-control\reports\` |
| Branch inventory | `C:\MARS Phenix\_reconstruction-control\manifests\branch-inventory.csv` |

---

*Branch integration decision v1 — plan only; no git integration performed.*
