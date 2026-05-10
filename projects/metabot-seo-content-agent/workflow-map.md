# Workflow map — MetaBOT SEO Content Agent

**Status:** documentation — communication paths described at **workflow** level. **No** n8n JSON in this pack.

---

## Workflow set

| Workflow | Role |
|----------|------|
| **Intake** | Entry from Telegram (and possibly other triggers **SAFE UNKNOWN**); validation, normalization, handoff to processing. |
| **Worker** | Main content pipeline: chunking, generation, locks, QA/factcheck triggers, Sheets updates — **v13 stable**. |
| **Admin** | Operations: locks visibility, health-style probes, admin-only commands — **partial overlap** with Worker **SAFE UNKNOWN** without live graph. |
| **File Export** (future) | Export artifacts to files or external storage — **not** evidenced as implemented in this repository. |

---

## Communication paths (logical)

```
Telegram user
    │
    ▼
┌─────────────┐
│   Intake    │  ← commands, payloads, metadata (user_id, username, …)
└──────┬──────┘
       │  SAFE UNKNOWN: internal call pattern (sub-workflow, queue, HTTP)
       ▼
┌─────────────┐
│   Worker    │  ← OpenRouter, chunking, locks, seo_active_jobs, memory
└──────┬──────┘
       │
       ├──────────► Google Sheets (memory, seo_active_jobs, …)
       └──────────► OpenRouter (generation, QA, cleanup rewrite, …)

┌─────────────┐
│    Admin     │  ← may read Sheets, Telegram admin routes
└─────────────┘
       ▲
       │  SAFE UNKNOWN: whether Admin is always invoked via Intake or separate trigger
```

---

## External systems

| System | Direction | Notes |
|--------|-----------|--------|
| **Telegram** | Inbound commands / outbound replies | Bot API — credentials in n8n. |
| **OpenRouter** | Outbound API | Model calls from Worker (**SAFE UNKNOWN**: which nodes). |
| **Google Sheets** | Read/write | Rate limits affect `/health` and bulk operations — see [known-issues.md](known-issues.md). |

---

## SAFE UNKNOWN

- **Exact** handoff mechanism between Intake and Worker (named queue vs synchronous execute vs shared sheet row polling).
- Whether **Admin** is a separate Telegram bot, same bot with role check, or separate webhook — **not** documented in-repo.
- **Retry** and **dead-letter** behavior per workflow.
- **Future File Export Workflow** attachment point (post-Worker vs parallel).

---

*Related: [intake-workflow.md](intake-workflow.md), [worker-workflow.md](worker-workflow.md), [admin-workflow.md](admin-workflow.md), [integration-boundary.md](integration-boundary.md).*
