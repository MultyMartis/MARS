# Frontend workspace — Triumph Manipulator Landing

## Recommended local path

**`C:\AI MARS\workspaces\triumph-manipulator-landing-v6\`** (active rollout base, 2026-05-28)

Historical: `workspaces/triumph-manipulator-landing-v5/` (mailer MVP freeze), `workspaces/triumph-manipulator-landing/` (V1 legacy).

This directory is the **local working area** for frontend implementation. It is intentionally **not** the MARS documentation pack under `projects/triumph-manipulator-landing/`.

**Canonical rules:** [`TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`](TRIUMPH-V6-CURRENT-FRONTEND-RULES.md)

## Intended use (later)

In this path, an operator may:

- Clone or copy a **gulp-starter** (or approved starter) when the project is ready for implementation.
- Author **source** files (templates, SCSS, JS), run **build**, and iterate with **Cursor**.
- Produce frontend output suitable for QA and HITL review.

## Rules

- **Do not** commit generated **`dist/`** (or equivalent build output) into the MARS repo.
- **Do not** commit client **assets** until reviewed and explicitly approved for version control.
- **Do not** hand-edit **`dist/`** — maintain **source-first** discipline only.
- Treat **[`agents/frontend-gulp-agent/`](../../agents/frontend-gulp-agent/)** as the **operational guide** for Gulp-oriented frontend work, reporting, and QA alignment.

## Related

- **Triumph V2 (current layout):** folder paths and where to edit — [V2-CANONICAL-STATE.md](V2-CANONICAL-STATE.md) (`workspaces/triumph-manipulator-landing-v2/`, design pack, `dist/`, shared icons).
- [frontend-agent-brief.md](frontend-agent-brief.md)
- [website-factory-runbook.md](website-factory-runbook.md)
