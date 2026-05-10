# Telegram commands — MetaBOT SEO Content Agent

**Status:** operations documentation — behavior is defined by **live n8n** + bot configuration. This file tracks the **intended** command surface.

**Convention:** Leading `/`. Arguments may include `from:task_id` and `--strict` where noted.

---

## User commands

### `/start`

- **Purpose:** Session entry; welcome / onboarding text.
- **SAFE UNKNOWN:** Exact copy and whether it writes state.

### `/help`

- **Purpose:** Short help and command pointers.

### `/examples`

- **Purpose:** Example prompts or command patterns for SEO operators.
- **SAFE UNKNOWN:** Whether implemented as static text or dynamic; parity with [seo-specialist-user-guide.md](seo-specialist-user-guide.md).

### `/outline`

- **Purpose:** Generate SEO outline / brief from user brief (and optional context).

### `/text`

- **Purpose:** Generate or refine **full text**, typically after outline; uses **cleanup rewrite** layer — [cleanup-rewrite-layer.md](cleanup-rewrite-layer.md).

### `/run`

- **Purpose:** End-to-end run combining pipeline stages (outline/text/QA steps as configured) — [full-run-pipeline.md](full-run-pipeline.md).  
- **Known issue:** lock vs `seo_active_jobs` **pending** inconsistency possible — [known-issues.md](known-issues.md).

### `/seoqa`

- **Purpose:** SEO quality review.  
- **Canonical strict usage:** `/seoqa --strict from:task_id` — [seoqa-and-factcheck.md](seoqa-and-factcheck.md).  
- **Note:** Requiring `--strict` on non-canonical invocations is **not** currently mandated for all paths.

### `/factcheck`

- **Purpose:** Fact-checking pass, **separated** from SEO QA — [seoqa-and-factcheck.md](seoqa-and-factcheck.md).  
- **Canonical strict usage:** `/factcheck --strict from:task_id`.

### `/locks`

- **Purpose:** Show or summarize active **locks** — [lock-system.md](lock-system.md).

### `/health`

- **Purpose:** System health probe; may hit **Google Sheets** heavily.  
- **Known issue:** rate limit message *“The service is receiving too many requests from you”* — [known-issues.md](known-issues.md).

### `/get task_id`

- **Purpose:** Retrieve artifact or status for a task.  
- **Known issue:** sometimes **does not respond** — [known-issues.md](known-issues.md).

---

## Admin commands

**SAFE UNKNOWN:** Exact names and permission model (Telegram user id allowlist, role flag in Sheets, etc.).

Documented **intent**:

- Inspect or clear **locks** at scale (beyond user `/locks`).
- Trigger or verify **cleanup** jobs.
- Possibly **replay** or **fail** stuck tasks — **not** confirmed in-repo.

See [admin-operations.md](admin-operations.md).

---

## Reuse syntax

- **`from:task_id`** (or equivalent parsing) ties a command to a prior task for reuse — [task-lifecycle.md](task-lifecycle.md), [memory-and-task-reuse.md](memory-and-task-reuse.md).

---

*Related pack (older spec): [`../seo-content-agent/telegram-commands.md`](../seo-content-agent/telegram-commands.md) — may differ; prefer operational truth from n8n.*
