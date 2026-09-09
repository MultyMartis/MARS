# MARS Git Operation Registry Convention

**Status:** documented Storage-only convention — not implemented by this GO  
**Not:** a lock daemon, orchestration engine, Git hook, or in-repo registry product  
**Companion:** [MARS-GIT-OPERATION-DISCIPLINE.md](MARS-GIT-OPERATION-DISCIPLINE.md)

This GO documents the convention only. It must **not** create active registry entries.

---

## Purpose

Serialize promotions that intend to fast-forward `mars/canonical-post-recovery`.

Multiple clean worktrees may exist. Only one **active canonical promotion** should hold `LOCAL_COMMIT_CREATED` or `PUSH_PENDING` at a time, unless the operator explicitly preempts and records why.

The registry is a **file-based human/agent checklist**, not runtime enforcement.

---

## Location

Storage only (outside the git working tree, to avoid dirty-main noise):

```text
X:\AI MARS STORAGE\git-operations\active\
```

Optional later archive (not created by this GO):

```text
X:\AI MARS STORAGE\git-operations\history\
```

Do **not** put active lock files inside `X:\AI MARS`.

This path did not need to exist for the convention to be valid. Creating `active\` files is a future promotion GO’s job, not a docs GO’s job.

---

## File name

Each active Git promotion may create:

```text
<operation_id>.json
```

Example:

```text
X:\AI MARS STORAGE\git-operations\active\MARS-SITE-002-PAYMENT-DOCS-GIT-PROMOTION-01.json
```

One file per operation. Do not overwrite another operation’s file.

---

## Required fields

```json
{
  "operation_id": "MARS-EXAMPLE-GIT-PROMOTION-01",
  "subsystem": "SITE-002",
  "source_paths": [
    "projects/ocpilot/sites/site-002/payments/yookassa/"
  ],
  "exact_add_list": [
    "projects/ocpilot/sites/site-002/payments/yookassa/file.md"
  ],
  "clean_worktree": "X:\\AI MARS STORAGE\\git-sync-<id>\\repo",
  "base_remote_sha": "7aead1ea...",
  "expected_parent_sha": "7aead1ea...",
  "local_commit_sha": null,
  "push_authorized": false,
  "current_status": "PLANNED",
  "created_at": "2026-09-10T00:00:00+07:00",
  "updated_at": "2026-09-10T00:00:00+07:00",
  "operator": "human-or-agent-id",
  "notes": "push_forbidden | push_window_open | push_now"
}
```

| Field | Rule |
|-------|--------|
| `operation_id` | Matches the GO charter id |
| `subsystem` | One subsystem name |
| `source_paths` | Prefixes in scope |
| `exact_add_list` | Literal paths that may be staged |
| `clean_worktree` | Absolute path under an approved X: root |
| `base_remote_sha` | `ls-remote` SHA at start |
| `expected_parent_sha` | Required parent of the local commit |
| `local_commit_sha` | Null until `LOCAL_COMMIT_CREATED` |
| `push_authorized` | Boolean; details belong in `notes` (`push_now` / `push_window_open` / `push_forbidden`) |
| `current_status` | One status from the list below |
| `created_at` / `updated_at` | ISO-8601 |
| `operator` | Human or agent identifier |
| `notes` | Push window, preemption, or why status changed |

---

## Statuses

| Status | Meaning |
|--------|---------|
| `PLANNED` | Charter exists; worktree not proven created |
| `CLEAN_WORKTREE_CREATED` | Clean worktree exists at `base_remote_sha` |
| `LOCAL_COMMIT_CREATED` | Local SHA exists; not proven live tip |
| `PUSH_PENDING` | Local commit exists; push window open or follow-up push GO not finished |
| `CANONICAL_TIP_UPDATED` | Live `ls-remote` equals `local_commit_sha` |
| `CANONICAL_IN_HISTORY_NOT_TIP` | `local_commit_sha` is ancestor of live tip, not equal |
| `BLOCKED_REMOTE_ADVANCED_WITHOUT_COMMIT` | Live remote advanced and does not contain local commit. Report name: `PUSH_BLOCKED_REMOTE_ADVANCED_WITHOUT_COMMIT` |
| `CLOSED` | Operation finished; no further push from this file |
| `ABANDONED` | Operator cancelled; local SHA must not be pushed from this worktree |

Terminal success states that should move the file to history (future GO): `CANONICAL_TIP_UPDATED`, `CANONICAL_IN_HISTORY_NOT_TIP`, then `CLOSED`.

Blocked state `BLOCKED_REMOTE_ADVANCED_WITHOUT_COMMIT` is not success. Close or abandon this file and open a **new** operation id for cherry-pick/rebase in a new worktree.

---

## Lock / serialization rules

1. Create the JSON file **before** `git worktree add` / first canonical commit, when the promotion intends to FF origin.
2. While status is `LOCAL_COMMIT_CREATED` or `PUSH_PENDING`, another subsystem must not start a competing canonical FF unless the operator explicitly preempts.
3. Recheck remote immediately before push; then set `CANONICAL_TIP_UPDATED` or `CANONICAL_IN_HISTORY_NOT_TIP`.
4. After either of those two success states, set `CLOSED` and stop using this worktree for new unrelated work.
5. Stale registry files: **human review only**. Agents must not delete locks in passing tasks.
6. This is not a mutex implemented in Git. If two GOs race without a file, the **push decision table** is the last safety net (`ls-remote` before push).

---

## Interaction with the 2026-09-09 incident

If a registry file had existed from payment-docs local commit until after the first successful FF of `da7302a7`, a second deferred push of the same SHA would have been easier to classify.

After `da7302a7` was already on origin, an iSEO fast-forward on top is valid. The remaining requirement is reporting:

```text
CANONICAL_IN_HISTORY_NOT_TIP
```

not “push failed, therefore commit is missing.”

The registry would mainly prevent two **simultaneous** deferred pushes from racing on the same parent. It does not forbid a later unrelated subsystem commit **after** the previous operation is closed.

---

## What this convention forbids in a docs GO

- creating files under `git-operations\active\`
- implementing hooks or lock scripts
- claiming the registry is already an enforcement product
)
