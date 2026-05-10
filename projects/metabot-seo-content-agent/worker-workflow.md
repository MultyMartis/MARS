# Worker workflow

**Reference version:** **v13 stable** (operations).  
**Evidence in this repo:** documentation only — **no** workflow JSON.

---

## Intended responsibilities

- **Content generation** pipeline: outline-related flows, full text, chunking for long outputs.
- **Lock** acquisition, enforcement, and **cleanup** so concurrent users/tasks do not corrupt state — see [lock-system.md](lock-system.md).
- **seo_active_jobs** lifecycle: pending → processing → completed / failed — see [task-lifecycle.md](task-lifecycle.md). **Note:** known inconsistency: lock may close while a row stays **pending** — [known-issues.md](known-issues.md).
- **Memory writes** after meaningful progress — [memory-and-task-reuse.md](memory-and-task-reuse.md).
- **Cleanup rewrite** layer for `/text` output — [cleanup-rewrite-layer.md](cleanup-rewrite-layer.md).
- **Strict QA** and **factcheck** **enforcement** when invoked with canonical flags — [seoqa-and-factcheck.md](seoqa-and-factcheck.md).
- Model calls via **OpenRouter** — **SAFE UNKNOWN**: prompts, models, and token limits.

---

## Non-responsibilities (boundary hints)

- **Admin-only** operational tasks may live in **Admin** workflow — overlap **SAFE UNKNOWN**.

---

## SAFE UNKNOWN

- Internal subgraphs for `/outline` vs `/text` vs `/run`.
- How **chunking** is parameterized (size, overlap, merge strategy).
- Exact **JavaScript** or **Code** nodes used for “runtime consistency” vs pure LLM steps.

---

*See [workflow-map.md](workflow-map.md), [full-run-pipeline.md](full-run-pipeline.md).*
