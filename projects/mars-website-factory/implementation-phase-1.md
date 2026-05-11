# MARS Website Factory — implementation phase 1 (doc-first)

**Scope:** **Documentation and contracts only** — **no** code generation mandate, **no** new runtime.

## Proposed concrete deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | **Site Type Registry v0** | **Done (doc):** [site-type-registry-v0.md](site-type-registry-v0.md) — initial `site_type_id` rows and field glossary (Markdown in this pack). |
| 2 | **Block Registry v0** | **Done (doc):** [block-registry-v0.md](block-registry-v0.md) — initial `block_id` set, compatibility matrix, field glossary (Markdown); aligned with static HTML feasibility. |
| 3 | **Website Factory workflow v0** | One **Task** / workflow narrative binding factory stages to `workflows/task-contract-v0.md` fields (`required_agents`, `hitl_gates`) |
| 4 | **Gulp Frontend Agent card** | Full card using `agents/agent-card-template.md` — I/O, validation, limitations |
| 5 | **Page Blueprint contract** | **Done (doc):** [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md) — normalized page orchestration fields; human-readable (**no** strict JSON Schema in v0). |
| 6 | **Design artifact contract** | Minimum fields for handoff to frontend (tokens, breakpoints, component list) |
| 7 | **Frontend handoff contract** | What design must provide so **Gulp Frontend Agent** can implement without clarification loops |
| 8 | **QA checklist v0** | **Done (doc, blueprint slice):** [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md); broader lanes remain in [qa-validation-model.md](qa-validation-model.md). |

## Out of scope for phase 1

- Gulp project scaffolding in this repo.
- Figma plugins, n8n nodes, or Cursor extensions.
- Automated orchestration.

## Success criteria (documentation)

- Cross-links from `registry/project-registry.md` and `agents/registry.md` remain consistent.
- No **false** “production ready” language in phase 1 outputs.
