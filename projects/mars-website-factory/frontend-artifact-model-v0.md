# MARS Website Factory — Frontend artifact model v0

**Status:** **documentation only** — conceptual **static frontend** deliverables aligned with [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md) and [frontend-production-model.md](frontend-production-model.md). **Not** a claim that a repo contains a Gulp pipeline, **not** automated code generation.

**Related:** [design-handoff-contract-v0.md](design-handoff-contract-v0.md), [block-registry-v0.md](block-registry-v0.md), [agent-map.md](agent-map.md) (**Gulp Frontend Agent** — legacy-bridge / planned).

---

## Conceptual artifact categories

| Artifact kind | Role |
|---------------|------|
| **Section partials** | HTML include fragments per **`block_id`** / **section_map** row. |
| **Component groups** | Recurring UI groups (accordions, cards) shared across pages. |
| **SCSS modules** | Partial graph per block/page; tokens via shared entry. |
| **JS modules** | Scoped behaviors behind **`data-*`** hooks ([frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md)). |
| **Asset groups** | Images, fonts, icons referenced by handoff **asset_requirements**. |
| **Design tokens** | CSS variables or SCSS maps — **when** a design system exists ([registries.md](registries.md) Design System Rules). |
| **Responsive rules** | Breakpoint notes, mobile-first exceptions vs design baseline. |
| **Accessibility intent** | Documented focus order, landmarks, live regions — implementation still human-verified. |
| **Frontend QA outputs** | Reports tied to [qa-result-payloads-v0.md](qa-result-payloads-v0.md) concepts (build, spot viewports, link integrity). |

---

## Ties to Gulp Frontend Agent

The **Gulp Frontend Agent** is the **documented** specialist for static assembly; v0 maps artifacts above to **legacy-aligned** patterns (`src/`, partials, modular SCSS) from [frontend-production-model.md](frontend-production-model.md). **Human** execution remains the Phase 1 surface per `governance/execution-model.md`.

---

## Honesty boundary

- **No** claim that MARS ships an automated **design → code** pipeline.
- **No** claim that partials are generated from contracts without human authorship.
- Exact repo layout and task runners — **SAFE UNKNOWN** per project.

---

*Last updated: 2026-05-11.*
