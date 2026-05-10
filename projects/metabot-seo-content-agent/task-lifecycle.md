# Task lifecycle

Describes **logical** task state for MetaBOT — **SAFE UNKNOWN** for exact column names and all transitions unless verified in Google Sheets schema.

---

## States (conceptual)

| State | Meaning |
|-------|---------|
| **Created** | Task id allocated; user or system initiated work. |
| **Locked** | A **lock** prevents conflicting operations — [lock-system.md](lock-system.md). |
| **Pending** | Waiting in `seo_active_jobs` (or equivalent) for worker pickup. |
| **Processing** | Worker actively generating / rewriting / validating. |
| **Completed** | Success path finished; outputs available (Telegram / Sheets / **SAFE UNKNOWN**). |
| **Failed** | Error path; user may retry or admin may intervene. |

---

## Typical flow

1. User issues `/outline`, `/text`, or `/run` (or strict QA commands with `from:`).
2. Intake/Worker creates or updates a **task** record and **`seo_active_jobs`** row.
3. **Locks** guard critical sections; **cleanup** removes stale locks when implemented.
4. On success, **memory write** may record summaries or reusable context — [memory-and-task-reuse.md](memory-and-task-reuse.md).
5. **Chunking** may split long generations; merge behavior **SAFE UNKNOWN** at node level.

---

## Reuse via `from:`

- Commands such as `/seoqa --strict from:task_id` and `/factcheck --strict from:task_id` **bind** to an existing task artifact.
- **SAFE UNKNOWN:** Whether all commands support `from:` or only a subset.

---

## Cleanup

- **Lock cleanup** — see [lock-system.md](lock-system.md).
- **Cleanup rewrite** for `/text` — editorial pass to remove low-quality phrasing — [cleanup-rewrite-layer.md](cleanup-rewrite-layer.md).
- **seo_active_jobs** row should eventually reflect terminal state; **known issue:** may remain **pending** when lock already closed — [known-issues.md](known-issues.md).

---

## SAFE UNKNOWN

- Exact **Sheets** schema (column headers, multiple tabs).
- Timeout values and automatic **failed** transitions.
- Whether **task_id** is globally unique or per-user.

---

*See [full-run-pipeline.md](full-run-pipeline.md), [storage-layer.md](storage-layer.md).*
