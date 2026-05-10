# Full run pipeline (`/run`)

High-level narrative for the **`/run`** command as a **multi-step** production path — **not** a single LLM call.

---

## Intended stages (logical)

1. **Intake** receives `/run` and validates user / chat context.
2. **Task** and **`seo_active_jobs`** entries created or updated — [task-lifecycle.md](task-lifecycle.md).
3. **Lock** acquired — [lock-system.md](lock-system.md).
4. **Generation** phases execute (outline and/or text — **exact sequence SAFE UNKNOWN**; may involve **chunking**).
5. **Cleanup rewrite** may run for text output — [cleanup-rewrite-layer.md](cleanup-rewrite-layer.md).
6. **Strict QA** and **factcheck** are **not** automatically implied unless invoked with canonical commands — [seoqa-and-factcheck.md](seoqa-and-factcheck.md).
7. **Memory write** on successful milestones — [memory-and-task-reuse.md](memory-and-task-reuse.md).
8. **Lock** released; job row should move to **completed** — **known issue:** may stay **pending** — [known-issues.md](known-issues.md).

---

## Outputs

- **Telegram** messages (chunked if long).
- **Sheets** updates for jobs and memory — **SAFE UNKNOWN** whether full text is duplicated in Sheets.

---

## Operational notes

- **Worker v13 stable** is the reference implementation for this pipeline.
- Failures should land in **failed** state with user-visible error — **SAFE UNKNOWN** for all error codes.

---

## SAFE UNKNOWN

- Whether `/run` always includes outline step or can skip based on flags.
- Maximum runtime and cancellation (user `/cancel` **SAFE UNKNOWN**).

---

*See [workflow-map.md](workflow-map.md), [worker-workflow.md](worker-workflow.md).*
