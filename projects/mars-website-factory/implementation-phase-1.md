# MARS Website Factory — implementation phase 1 (doc-first)

**Scope:** **Documentation and contracts only** — **no** code generation mandate, **no** new runtime.

## Proposed concrete deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | **Site Type Registry v0** | Markdown or structured table in this pack (or `registry/` if governance prefers) — initial `site_type_id` rows |
| 2 | **Block Registry v0** | Initial `block_id` set aligned with static HTML feasibility |
| 3 | **Website Factory workflow v0** | One **Task** / workflow narrative binding factory stages to `workflows/task-contract-v0.md` fields (`required_agents`, `hitl_gates`) |
| 4 | **Gulp Frontend Agent card** | Full card using `agents/agent-card-template.md` — I/O, validation, limitations |
| 5 | **Page Blueprint contract** | Schema for page-level block list, meta requirements, internal links |
| 6 | **Design artifact contract** | Minimum fields for handoff to frontend (tokens, breakpoints, component list) |
| 7 | **Frontend handoff contract** | What design must provide so **Gulp Frontend Agent** can implement without clarification loops |
| 8 | **QA checklist v0** | Single merged checklist covering Validator + specialist QA lanes ([qa-validation-model.md](qa-validation-model.md)) |

## Out of scope for phase 1

- Gulp project scaffolding in this repo.
- Figma plugins, n8n nodes, or Cursor extensions.
- Automated orchestration.

## Success criteria (documentation)

- Cross-links from `registry/project-registry.md` and `agents/registry.md` remain consistent.
- No **false** “production ready” language in phase 1 outputs.
