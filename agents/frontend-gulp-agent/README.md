# MARS — Frontend Gulp Agent (operational documentation pack)

This directory is the **MARS Frontend Gulp Agent operational documentation pack**: prompts, constraints, workflow, and QA/reporting discipline for **human- or Cursor-assisted** static frontend work aligned with the Website Factory.

**It is not** the gulp-starter repository, **not** MARS runtime code, and **not** a home for production page source. **It does not** ship runnable build tooling, dependencies, or `src/` trees for a live site.

**Execution target:** real HTML/SCSS/JS edits happen in an **external or local gulp-starter (or equivalent) project** that the operator opens separately. This pack only defines *how* to work there safely.

| Field | Value |
|--------|--------|
| **agent_id** | `gulp_frontend_agent` |
| **parent_system** | `mars_website_factory` |

**Related card:** [`../cards/gulp-frontend-agent-v0.md`](../cards/gulp-frontend-agent-v0.md)

**Related Website Factory docs:**

- [`../../projects/mars-website-factory/frontend-production-model.md`](../../projects/mars-website-factory/frontend-production-model.md)
- [`../../projects/mars-website-factory/frontend-handoff-contract-v0.md`](../../projects/mars-website-factory/frontend-handoff-contract-v0.md)
- [`../../projects/mars-website-factory/frontend-prompt-discipline-v0.md`](../../projects/mars-website-factory/frontend-prompt-discipline-v0.md)
- [`../../projects/mars-website-factory/first-operational-runbook-v0.md`](../../projects/mars-website-factory/first-operational-runbook-v0.md)
- [`../../projects/mars-website-factory/operator-session-template-v0.md`](../../projects/mars-website-factory/operator-session-template-v0.md)

**Pack index:** start with [`AGENT.md`](AGENT.md), then [`workflow.md`](workflow.md), [`constraints.md`](constraints.md), [`frontend-rules.md`](frontend-rules.md), [`handoff-rules.md`](handoff-rules.md), [`prompt-patterns.md`](prompt-patterns.md), [`qa-checklist.md`](qa-checklist.md), [`reporting.md`](reporting.md).

---

## SAFE UNKNOWN (normative)

- **Target project path** on disk is **project-specific** — confirm with the operator or ticket before editing.
- **gulp-starter (or stack) version** and **exact npm scripts** (`build`, `watch`, etc.) are **project-specific** — read the target repo’s `package.json` / README; do not assume script names.
- **Build commands** must be **verified in the target repo** each time the toolchain changes; this pack does not pin a dependency graph.

---

*Documentation only — no runtime enforcement.*
