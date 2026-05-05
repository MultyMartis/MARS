# SEO Content Agent — Roadmap

**Status:** **plan** — sequencing and scope intent. Dates and resourcing are **SAFE UNKNOWN** unless recorded elsewhere.

**Fact vs plan:** Phases describe **intended** work. Completion of any phase is **not** asserted by this file alone.

---

## Phase 1 — Documentation and project registration

**Goal:** Register the project in MARS, document architecture, workflows, schemas, prompts, and QA.

**Outcomes (plan):**

- Authoritative `project_id` in `registry/project-registry.md`.
- This documentation pack under `projects/seo-content-agent/`.

**Dependencies:** None (documentation-only).

---

## Phase 2 — MVP `/outline` (without competitor parsing)

**Goal (plan):** **Documentation-level** design for `/outline`: workflows, schemas, prompts, and QA — so the behaviour is specified before any n8n graph is built.

**Fact:** Phase 2 **does not** assert that Telegram or n8n workflows exist; it asserts only that the **docs** in this folder describe the intended `/outline` behaviour.

**Scope (plan):**

- Task normalization from Telegram text (or structured payload) — **full** workflow description including **later** steps (Analyze Brief, optional sources module, Storage Adapter) in [workflows.md](workflows.md).
- Outline generation from the brief; **optional “sources” in MVP sense** = **text pasted into the Telegram message**, not URL fetching or competitor parsing.
- Human approval gate before any `/text` run (process **SAFE UNKNOWN** until tooling exists).

**Explicit non-goals for this phase:** Automated competitor scraping, SERP parsers, bulk URL ingestion (**planned** for Phase 5).

---

## Phase 2.1 — MVP `/outline` runtime (n8n + Telegram)

**Goal (plan):** **Executable** MVP spec for the **first** n8n implementation: Telegram **`/outline`** → OpenRouter (**Parse Task**, **Build Outline**, **QA Outline**) → structured SEO brief back in Telegram. Full detail: [runtime-mvp-outline.md](runtime-mvp-outline.md).

**Relationship to Phase 2:** Phase 2 is the **documentation umbrella** for `/outline`; Phase 2.1 is the **concrete orchestration + data-flow contract** for MVP-1 (subset of the full `/outline` story: **no** Storage Adapter, **no** URL/source pipeline).

**Status:** **plan** — technical execution spec in [runtime-mvp-outline.md](runtime-mvp-outline.md). **Fact:** No workflow JSON or deployed bot is implied by that file alone.

**Outcomes (plan):**

- Documented n8n node order and data flow (`task_raw` → … → `final_output`).
- [n8n-outline-workflow-spec.md](n8n-outline-workflow-spec.md) — implementation-ready build spec (per-node inputs/outputs, env vars, credentials, OpenRouter bodies, full prompts, Telegram format, test RU examples, manual QA checklist).
- Explicit MVP limitations (no storage, no `/text`, no publishing) and human review gate.

**Dependencies:** Phase 1 documentation; Phase 2 doc set for behaviour alignment; n8n + Telegram + OpenRouter available in target environment (**SAFE UNKNOWN:** who operates them).

---

## Phase 3 — MVP `/text` from approved outline

**Goal:** Generate full **SEO article draft** only from an **approved** outline (and the same fact boundary as Phase 2).

**Scope (plan):**

- Persist outline approval state (**SAFE UNKNOWN:** storage mechanism until implemented).
- Writer step bound to outline sections and allowed facts.
- Delivery back to Telegram (or link to stored artefact).

---

## Phase 4 — Fact check and SEO QA

**Goal:** Post-draft **factcheck** and **SEO QA** workflows with structured reports.

**Scope (plan):**

- `/factcheck` — compare draft claims to brief, sources, and explicit “company facts” corpus (**SAFE UNKNOWN:** where that corpus lives at runtime).
- `/seoqa` — structure, intent, cannibalization hints (manual), readability signals (**SAFE UNKNOWN:** which checks are automated vs human-only in v1).

---

## Phase 5 — Competitor / source analysis

**Goal:** Enrich outlines and QA with **external** source and competitor signals.

**Scope (plan):**

- Source analyzer module (see [architecture.md](architecture.md)).
- Policies for allowed sources, rate limits, and legal/compliance review (**SAFE UNKNOWN:** org-specific).

**Risk:** Web scraping and third-party ToS — **plan** requires governance review before implementation.

---

## Phase 6 — Freshness analysis

**Goal:** Optional `/freshness` workflow to flag stale claims, dates, statistics, and product facts.

**Scope (plan):**

- Compare content against dated source list or internal freshness registry.
- Output actionable “update suggestions”, not automatic rewrites without human approval.

---

## Phase 7 — Storage and reporting

**Goal:** Durable storage, audit trail, and light reporting for managers.

**Scope (plan):**

- Migrate from Sheets/files toward **PostgreSQL** (or equivalent) if volume and compliance require it.
- Run history, token/cost summaries (**align** with MARS model cost docs where applicable).

---

## Phase 8 — Production hardening

**Goal:** Reliability, security, observability, and access control suitable for internal production.

**Scope (plan):**

- Secrets management, RBAC on Telegram/n8n, rate limits, backoff, alerting.
- Regression evals on golden prompts (**SAFE UNKNOWN:** eval set location).

---

## Traceability

| Phase | Primary docs in this folder |
|------|-----------------------------|
| 1 | All files in `projects/seo-content-agent/` |
| 2 | [workflows.md](workflows.md), [prompts.md](prompts.md), [data-schema.md](data-schema.md) |
| 2.1 | [runtime-mvp-outline.md](runtime-mvp-outline.md), [n8n-outline-workflow-spec.md](n8n-outline-workflow-spec.md) |
| 3 | [workflows.md](workflows.md), [prompts.md](prompts.md), [data-schema.md](data-schema.md) |
| 4 | [workflows.md](workflows.md), [qa-checklist.md](qa-checklist.md) |
| 5–6 | [architecture.md](architecture.md), [workflows.md](workflows.md) |
| 7–8 | Cross-repo: MARS storage, observability, integrations docs |
