# Workflow — Frontend Gulp Agent (documentation pack)

Ordered flow for a **material** frontend implementation slice. Adjust step labels to match the operator session template when used inside a reference run.

**Lane discipline (one Cursor, multiple chats):** treat this workflow as **Lane A — production execution** per [`../../governance/parallel-cursor-chat-work-mode-v0.md`](../../governance/parallel-cursor-chat-work-mode-v0.md); avoid governance/registry commits in the same session unless explicitly re-scoped.

1. **Inspect frontend handoff** — Confirm `frontend_handoff_id`, `page_slug`, `section_map`, `partials_mapping`, `SCSS_mapping`, `JS_requirements`, `data_attribute_hooks`, `responsive_rules`, `QA_requirements`, `forbidden_patterns`, `HITL_required`, and `SAFE_UNKNOWN_notes` per [`frontend-handoff-contract-v0.md`](../../projects/mars-website-factory/frontend-handoff-contract-v0.md).
2. **Inspect target repo** — Open the **external/local** project; verify actual `src/` root, include syntax, SCSS entry pattern, JS bundling, and npm scripts (**SAFE UNKNOWN** until verified).
3. **Plan sections/components** — One prompt-friendly slice at a time (prefer one `block_id` / section per prompt per [`frontend-prompt-discipline-v0.md`](../../projects/mars-website-factory/frontend-prompt-discipline-v0.md)).
4. **Implement source files** — Edit only allowed paths under the project’s source tree; match handoff order and naming.
5. **Run build** — If the repo provides a build script and the prompt scope includes verification, run it and capture **honest** outcome (log excerpt or exit code).
6. **Run QA** — Apply [`qa-checklist.md`](qa-checklist.md); record pass/fail/partial with evidence.
7. **Report** — Emit a REPORT per [`reporting.md`](reporting.md) and factory [`reporting-standard-v0.md`](../../projects/mars-website-factory/reporting-standard-v0.md) §4.2.
8. **HITL review** — Pause when handoff **`HITL_required`** or findings demand sign-off (legal copy, a11y risk, structural change).
9. **Checkpoint** — Git commit / merge checkpoint **only** if policy and HITL approve; never silent commit or `git add .` (see [`constraints.md`](constraints.md)).

---

## SAFE UNKNOWN

Exact stage IDs, CI job names, and hosting URLs are **factory- and project-specific** — record unknowns explicitly in each REPORT.
