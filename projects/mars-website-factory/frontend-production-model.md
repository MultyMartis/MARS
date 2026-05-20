# MARS Website Factory — frontend production model

## Role of Gulp Frontend Agent

The **Gulp Frontend Agent** is the **core production specialist** (documentation) for turning approved designs into **static frontend** artifacts. In MARS **Agent Registry** it is **`operational_doc_pack`**: a documentation-backed specialist pack (`agents/frontend-gulp-agent/`) — human + Cursor/Codex execution, **not** autonomous runtime, **not** proof of Gulp code in this repository (`agents/registry.md`). *Historical:* **legacy-bridge** label applied to the imported Web-GPT profile only.

Legacy **imported** profile (stack and rules) appears in **`web-gpt-sources/04_agents.md`** (Gulp Frontend Agent section): HTML, SCSS, JS; **Gulp**, **gulp-file-include**; optional jQuery and common libs; **source-first** — edit **`src`**, not manual **`dist`** edits. Normalized requirements for a page build are described in **[Frontend Handoff Contract v0](frontend-handoff-contract-v0.md)** (documentation only).

**Operational doc pack (MARS):** Cursor/human prompt patterns and guardrails for this role live under [`../../agents/frontend-gulp-agent/README.md`](../../agents/frontend-gulp-agent/README.md) — documentation only, **not** a bundled gulp-starter or runtime.

## gulp-starter architecture (target shape)

**SAFE UNKNOWN:** The repository does **not** contain a folder or artifact explicitly named `gulp-starter` at registration time. The **target** architecture below is **aligned** with the legacy profile and common static starter patterns:

| Concern | Target intent |
|---------|----------------|
| **Entry** | Gulp tasks for SCSS, HTML includes, assets, maybe lint |
| **Source tree** | `src/` (or equivalent) holds partials, section components, page entry HTML |
| **Output** | Build generates **`dist/`** (or agreed output); **never** hand-edit generated output |
| **Composition** | **Reusable sections/components** via includes/partials (`gulp-file-include` per legacy doc) |
| **Styles** | **Modular SCSS** — partials per component/section; shared tokens/variables |
| **Behavior** | **Data-attribute JS** — prefer scoped behavior hooks (e.g. `[data-component]`) over ad-hoc globals |
| **Globals** | **No unsafe global pollution** — avoid new `window.*` without explicit review; prefer modules or IIFEs as project policy dictates |
| **Responsive** | Mobile-first breakpoints per **Design System Rules**; **Frontend QA** checks key viewports |

## Outputs

- **HTML** pages assembled from includes.
- **CSS** compiled from SCSS.
- **JS** bundles or small entry scripts per project convention.

## Frontend QA

- Build must succeed.
- Markup sanity (headings, landmarks — **heuristic**).
- Responsive spot-checks.
- Link and asset path checks (**planned** depth).

## Honesty

- **Fully automated** page generation from design **without human supervision** is **not** claimed.
- **Human** Cursor sessions (or future runtime) remain the **execution** surface until implementation evidence exists (`governance/execution-model.md`).
