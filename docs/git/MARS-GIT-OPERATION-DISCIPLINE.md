# MARS Git Operation Discipline

**Status:** documented process convention — human/agent operated  
**Not:** Git hooks, lock daemon, orchestration product, or runtime enforcement  
**Canonical branch:** `mars/canonical-post-recovery` (`origin/mars/canonical-post-recovery`)  
**Repo root:** `X:\AI MARS`  
**Incident basis:** `MARS-GIT-STREAM-MIXING-INCIDENT-READONLY-01` (2026-09-10)

Related:

- [MARS-GIT-PUSH-DECISION-TABLE.md](MARS-GIT-PUSH-DECISION-TABLE.md)
- [MARS-GIT-OPERATION-REGISTRY-CONVENTION.md](MARS-GIT-OPERATION-REGISTRY-CONVENTION.md)
- Checkpoint culture: `web-gpt-sources/04-workflows__git-rules.md` (when a commit is even appropriate)

This document is the practical promotion rulebook. It does not authorize any Git mutation by itself.

---

## 1. Purpose

MARS uses **one canonical branch** and **many subsystem worktrees**. Sequential fast-forwards are normal. They are not history corruption.

Confusion happens when reports mix three different facts:

1. a local commit was created;
2. that commit is the current remote tip;
3. that commit is in canonical history but is no longer the tip.

This discipline exists so operators and agents always record **base SHA**, **expected parent**, **push authorization**, and a **named outcome status**.

Known-good linear example:

```text
7aead1ea  →  da7302a7  →  1f090c0e
```

`da7302a7` (SITE-002 payment docs) is in canonical history. `1f090c0e` is a legitimate later fast-forward (iSEO). No force, rewind, or Git repair is required.

---

## 2. When to use a clean worktree

Use a **new clean worktree** for any commit or push when:

- dirty main (`X:\AI MARS`) has foreign WIP, untracked residue, or a diverged `HEAD`;
- the promotion charter is subsystem-scoped;
- more than one Git Operation (GO) may touch the canonical branch.

Create the worktree from the **live remote SHA** (`git ls-remote`), never from dirty-main `HEAD`.

Preferred pattern:

```text
X:\AI MARS STORAGE\git-sync-<operation-id>\repo
```

Keep the worktree on `mars/canonical-post-recovery` (or detached at the recorded live SHA) with a **clean** status except the charter files.

Do **not** reuse an old worktree because it “looks close enough.”

---

## 3. Dirty main rules

Dirty main is the working brain. It is **not** a Git transport.

**Forbidden on dirty main** unless a separate explicit charter says otherwise:

- `git add` / `git commit` / `git push`
- `git pull` / `git fetch` / `git merge` / `git rebase`
- `git reset` / `git restore` / `git stash` / `git clean`
- `git checkout` / `git switch` to “catch up”
- using dirty-main `HEAD` as the canonical base SHA

Current incident fact: dirty main `HEAD` was diverged from origin. That remainder is **foreign WIP**. Leave it alone.

If a task only writes untracked docs/reports, still do not commit from dirty main.

---

## 4. One subsystem per commit

**One SHA = one subsystem path prefix.**

Allowed: a SITE-002 payment-docs commit that touches only SITE-002 payment docs.  
Allowed: an iSEO commit that touches only `projects/iseo-su-site-ops/`.  
Forbidden: one commit that mixes SITE-002 + iSEO, or docs + unrelated implementation, or two client programmes.

Branch-level adjacency (commit B on top of commit A from another subsystem) is **expected**. That is not mixed-commit contamination.

---

## 5. Exact add-list rule

Every promotion charter must contain an **exact add list** (literal paths).

Hard rules:

- Never `git add .`
- Never `git add -A`
- Never `git commit -a`
- Stage only the allowlisted paths
- Foreign WIP must not be staged, restored, cleaned, reset, moved, or deleted
- Commit and push are **separate waves** unless the same charter explicitly authorizes both

After staging, `git diff --cached --name-only` must equal the exact add list. If it does not, **STOP**.

---

## 6. Base SHA and expected parent

Every Git promotion charter must record:

| Field | Meaning |
|-------|---------|
| `base_remote_sha` | Live tip from `git ls-remote origin refs/heads/mars/canonical-post-recovery` at worktree/commit time |
| `expected_parent_sha` | Parent the local commit must have (`L^`) |
| `local_commit_sha` | SHA created in the clean worktree |

Rules:

- `expected_parent_sha` normally equals `base_remote_sha`
- Do not take the base from dirty-main `HEAD`
- Do not take the base from a stale worktree HEAD unless it **equals** live `ls-remote`
- Record full SHAs in the Storage registry file and in the GO report

---

## 7. Commit and push authorization

Treat commit and push as independently authorized.

Push authorization values:

| Value | Meaning |
|-------|---------|
| `push_forbidden` | Commit only. Do not push in this GO |
| `push_window_open` | Later GO may push, but must recheck remote first |
| `push_now` | This GO is authorized to push after recheck |

After a local commit:

- either push in the **same** GO that has `push_now`, or
- explicitly write `PUSH_PENDING` / `push_window_open`

Never leave “push later” implied.

If another subsystem needs a canonical fast-forward while a lock is `LOCAL_COMMIT_CREATED` or `PUSH_PENDING`, **STOP** unless the operator explicitly preempts and documents it.

---

## 8. Remote recheck before push

Immediately before push, re-read:

```text
git ls-remote origin refs/heads/mars/canonical-post-recovery
```

Compare live remote `R` with recorded `expected_parent_sha` `P` and local commit `L`.

Then apply [MARS-GIT-PUSH-DECISION-TABLE.md](MARS-GIT-PUSH-DECISION-TABLE.md).

Do not push from cached `origin/` refs alone if `ls-remote` is available. Do not fetch/pull dirty main to refresh the picture.

---

## 9. Push outcome statuses

Use these names in reports and registry files. Do not invent synonyms.

| Status | Meaning |
|--------|---------|
| `LOCAL_COMMIT_CREATED` | Local SHA exists in the clean worktree. It is not proven to be on origin. |
| `PUSH_PENDING` | Local commit exists; push is authorized later or still open; remote recheck not yet done or not yet acted on. |
| `CANONICAL_TIP_UPDATED` | Local commit was fast-forwarded (or already equals live tip). `ls-remote` == local SHA. |
| `CANONICAL_IN_HISTORY_NOT_TIP` | Local commit is an ancestor of live remote and is **not** equal to it. Landing succeeded. Do not push. |
| `PUSH_BLOCKED_REMOTE_ADVANCED_WITHOUT_COMMIT` | Live remote advanced and does **not** contain the local commit. Stop. New rebase/cherry-pick charter in a **new** clean worktree. |
| `FORCE_FORBIDDEN` | Placing the local SHA at the tip would require force/rewind. Stop. |
| `WORKTREE_NOT_SAFE` | Worktree is stale, dirty, or not the charter worktree. Stop. |

`CANONICAL_IN_HISTORY_NOT_TIP` is a **success of landing**, not a failed push. A later unrelated fast-forward on top is not a rollback.

---

## 10. Stale worktree rule

A worktree is **stale for new promotion** when its HEAD is not equal to live `ls-remote`.

Exceptions that are still not push-safe:

- HEAD equals a known ancestor (including a landed-but-not-tip SHA);
- HEAD equals a previous operation’s local commit;
- worktree has extra untracked reports or leftover files.

Do not reuse a stale worktree as the next canonical base. Create a new clean worktree from the live SHA.

The iSEO modal worktree that **equals** live tip may be kept, but must not be reused for unrelated work.

---

## 11. Cleanup rule

Cleanup is not part of commit or push.

Allowed only under a **separate destructive charter** after:

1. the commit is `CANONICAL_TIP_UPDATED` or `CANONICAL_IN_HISTORY_NOT_TIP`;
2. residues are archived to Storage;
3. exact path list, dry-run, and operator approval exist.

Forbidden in promotion/push/docs GOs:

- `git worktree remove` / prune
- `git clean`
- `Remove-Item -Recurse`
- deleting lock/registry files “in passing”
- closing someone else’s worktree because it is stale

Stale worktrees wait. They are not an emergency.

---

## 12. Forbidden operations

Without an explicit extra charter:

- force-push / `--force-with-lease` of `mars/canonical-post-recovery`
- rewind canonical to make an older SHA the tip
- push a SHA that would not fast-forward
- commit or push from dirty main
- mixed-subsystem commits
- ad-hoc rebase/cherry-pick inside a stale worktree
- `git add .` / `git add -A` / `git commit -a`
- fetching/pulling/resetting dirty main to “catch up”
- deleting, pruning, or moving worktrees during promotion
- treating a blocked rewind-push as “the earlier commit failed to land”
- implementing hooks, lock daemons, or Git automation in a docs GO

Disaster rewind is **not** defined here. It would need a separate human disaster charter.

---

## 13. Examples

### Example A — recent payment docs / iSEO line (canonical)

Facts from `MARS-GIT-STREAM-MIXING-INCIDENT-READONLY-01`:

| SHA | Role |
|-----|------|
| `7aead1ea` | Expected parent / then-live tip when payment docs worktree was created |
| `da7302a7` | SITE-002 YooKassa payment docs. Paths only under SITE-002 payment docs. Parent = `7aead1ea` |
| `1f090c0e` | iSEO homepage modal fix. Paths only under `projects/iseo-su-site-ops/`. Parent = `da7302a7` |

What happened:

1. Payment docs GO created local commit `da7302a7` → `LOCAL_COMMIT_CREATED`.
2. A later authorized wave fast-forwarded `7aead1ea..da7302a7` → payment docs **were** the tip (`CANONICAL_TIP_UPDATED`).
3. iSEO worktree started at then-tip `da7302a7`, committed `1f090c0e`, and fast-forwarded origin.
4. A later SITE-002 push recheck saw live tip `1f090c0e`. Pushing `da7302a7` would rewind. Correct action: **do not push**.

Correct final status for `da7302a7`:

```text
CANONICAL_IN_HISTORY_NOT_TIP
```

Correct actions: no push, no force, no rollback, no Git repair.

Wrong reading: “push blocked, therefore payment docs are missing.” They are not missing. They are the parent of the current tip.

### Example B — remote still equals expected parent

- Local commit `L` has parent `P`
- Live remote `R == P`
- Worktree clean and current

Action: fast-forward push.  
Status: `CANONICAL_TIP_UPDATED`.

### Example C — remote advanced without the local commit

- Local commit `L` is **not** an ancestor of live remote `R`
- `R` is not the expected parent

Action: **STOP**. New rebase/cherry-pick charter in a **new** clean worktree.  
Status: `PUSH_BLOCKED_REMOTE_ADVANCED_WITHOUT_COMMIT`.

Do not rebase in the stale worktree. Do not force.

### Example D — dirty main

Dirty main `HEAD` diverged (incident: `2bb511a9` vs origin `1f090c0e`).  
Action: do not commit/push/fetch/reset that tree. Use a clean worktree.  
Status if attempted: `WORKTREE_NOT_SAFE`.
)
