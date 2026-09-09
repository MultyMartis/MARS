# MARS Git Push Decision Table

**Status:** documented process convention — human/agent operated  
**Not:** a script, hook, or automated pusher  
**Canonical ref to recheck:** `origin` `refs/heads/mars/canonical-post-recovery`  
**Companion:** [MARS-GIT-OPERATION-DISCIPLINE.md](MARS-GIT-OPERATION-DISCIPLINE.md)

Live remote must be read with:

```text
git ls-remote origin refs/heads/mars/canonical-post-recovery
```

Symbols:

- `L` = local commit SHA to land
- `R` = live remote SHA from `ls-remote`
- `P` = `expected_parent_sha` recorded in the charter / Storage registry

Preconditions before using the table: exact add list already committed; worktree is the charter clean worktree; push authorization is `push_now` (or an explicit follow-up push GO). If the worktree is stale or dirty, do not enter the table — status `WORKTREE_NOT_SAFE`.

---

## Decision table

| Remote state before push | Contains local commit? | Action | Status |
|---|---:|---|---|
| remote == expected parent | no | fast-forward push | `CANONICAL_TIP_UPDATED` |
| remote advanced and contains local commit | yes | do not push | `CANONICAL_IN_HISTORY_NOT_TIP` |
| remote advanced and does not contain local commit | no | stop, new rebase/cherry-pick charter | `PUSH_BLOCKED_REMOTE_ADVANCED_WITHOUT_COMMIT` |
| push would require force | n/a | stop | `FORCE_FORBIDDEN` |
| worktree stale or dirty | n/a | stop | `WORKTREE_NOT_SAFE` |

---

## Expanded matching rules

| Condition | Fast-forward? | Action | Status |
|-----------|---------------|--------|--------|
| `R == P` and `L^ == P` | YES | Fast-forward push `HEAD` → `mars/canonical-post-recovery` | `CANONICAL_TIP_UPDATED` if after-push `R' == L` |
| `R == L` | already tip | Do not push | `CANONICAL_TIP_UPDATED` |
| `L` is ancestor of `R` and `R != L` | NO (would rewind) | Do not push; do not force | `CANONICAL_IN_HISTORY_NOT_TIP` |
| `R` advanced, `L` is not ancestor of `R`, `R` is not ancestor of `L` | NO | STOP. New cherry-pick/rebase charter in a **new** clean worktree | `PUSH_BLOCKED_REMOTE_ADVANCED_WITHOUT_COMMIT` |
| `R != P` even if some other FF still looks possible | STOP first | Re-validate expected parent; do not assume | re-charter or continue only if new `P` is documented |
| Force required to place `L` at tip | NEVER | Stop | `FORCE_FORBIDDEN` |
| Worktree HEAD ≠ charter HEAD, dirty index, or foreign files staged | n/a | Stop | `WORKTREE_NOT_SAFE` |

---

## How to read “contains local commit”

“Contains” means `L` is an ancestor of live `R` (including `R == L`).

It does **not** mean:

- the subject of the tip commit matches the local work;
- dirty main has the files;
- a worktree still points at `L`.

If `L` is an ancestor of `R`, the landing job for `L` is done.

---

## Incident row (2026-09-09 / 2026-09-10)

Later SITE-002 push recheck:

| Symbol | SHA |
|--------|-----|
| `P` | `7aead1ea` (original expected parent) / after wave-1, live had already moved |
| `L` | `da7302a7` |
| `R` | `1f090c0e` |

`da7302a7` is the parent of `1f090c0e`. Remote advanced **and contains** the local commit.

| Action taken | Correct? | Status |
|--------------|----------|--------|
| Do not push | YES | `CANONICAL_IN_HISTORY_NOT_TIP` |

Pushing `da7302a7` onto a tip of `1f090c0e` would rewind canonical history. That is `FORCE_FORBIDDEN` if attempted with force, and a wrong push even without force.

No Git repair, force, rollback, or repeated push is required.

---

## Status meanings used by this table

| Status | Operator meaning |
|--------|------------------|
| `CANONICAL_TIP_UPDATED` | Local commit is the live tip. |
| `CANONICAL_IN_HISTORY_NOT_TIP` | Local commit is in canonical history; a later legitimate FF sits on top. |
| `PUSH_BLOCKED_REMOTE_ADVANCED_WITHOUT_COMMIT` | Local commit is **not** in the live line. Needs a new charter. |
| `FORCE_FORBIDDEN` | Do not rewind canonical. |
| `WORKTREE_NOT_SAFE` | Do not push from this tree. |

Related pre-push statuses (not table outcomes): `LOCAL_COMMIT_CREATED`, `PUSH_PENDING`. See the main discipline doc.

---

## What this table does not authorize

- force-push
- dirty-main push
- ad-hoc rebase in the current stale worktree
- treating `CANONICAL_IN_HISTORY_NOT_TIP` as a failed promotion
)
