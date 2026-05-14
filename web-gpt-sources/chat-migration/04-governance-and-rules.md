# 04 — Governance and rules (migration v0)

---

## Registries

- **`registry/project-registry.md`** — project rows (`project_id`), lifecycle pointers.  
- **`agents/registry.md`** — agent catalog (documentation).  
- **`tools/registry.md`**, **`models/`** — planned tool/model registry docs.  
- **Website Factory:** `site-type-registry-v0.md`, `block-registry-v0.md` (under `projects/mars-website-factory/`).

## Dependency map

- **`governance/dependency-map.md`** — entity → entity relationships (**documentation**). Drives what must stay consistent when editing C16 entities (`website_factory_*`, etc.).

## Capability map

- **`governance/capability-map.md`** — **C15** (external multi-workflow knowledge), **C16** (Website Factory strategic planned), cross-refs to evidence paths.

## Stage 16

- **`governance/master-build-map.md` — Stage 16 — Pilot Project**  
- **Purpose:** end-to-end **documentation** validation across layers.  
- **Contains:** Website Factory pack, MetaBOT canonical pack, **legacy** `seo-content-agent` note, `mars-runtime` **SAFE UNKNOWN** for adapters.

## C16

- Shorthand for **Capability C16 — Website Factory (strategic planned)** in capability map changelog / §3 matrix.  
- **Not** a runtime release tag.

## Report discipline

- Task reports start with **`# REPORT — <task/stage name>`** (`AGENTS.md`).  
- Include changed files, summary, `git status`, **UNKNOWN** / **SECURITY RISK** when applicable.  
- **Parallel chat lane check** format in `governance/parallel-cursor-chat-work-mode-v0.md` when asked.

## Git safety

- No `git add .`, `git add -A`, `git commit -a`.  
- Explicit paths only; verify staged names before commit.  
- **No mixed-lane commits.**

## Lane separation

- **Lane A / B / Runtime** — see `02-current-operational-state.md` and `parallel-cursor-chat-work-mode-v0.md`.  
- Wrong-lane edits → **STOP**, **STRUCTURE CHANGE** / escalation, HITL.

## Approval semantics

- Documented under Website Factory **approval-semantics-v0.md** (gates, human approval markers). **Operational** in human sessions.

## Revision semantics

- **`revision-semantics-v0.md`** — who may revise what post-gate; ties to HITL.

## Invalidation semantics

- **`dependency-invalidation-v0.md`**, artifact routing invalidation shorthand — **conceptual** cascade rules for artifacts.

## Freeze semantics

- **Semantic freeze** / stage freeze concepts in semantic relationship + operator lane model — **authority** rules for operators, not automated enforcement.

## Escalation semantics

- **`orchestration-signals-v0.md`**, `system-signals-dictionary.md` — labels like **NEED HUMAN APPROVAL**, **STRUCTURE CHANGE**; used in prompts and REPORTs.

---

## Explicit anti-patterns

| Anti-pattern | Why forbidden |
|--------------|----------------|
| **`git add .`** | Cross-lane / secret / dist contamination |
| **Fake QA** | Claiming PASS / automated checks without evidence |
| **Fake runtime** | Saying orchestrator/scheduler “runs” MARS without code proof |
| **Hidden automation** | Implying background agents own repo or deploy |

---

## Canonical pointers

- `AGENTS.md` — non-negotiables.  
- `web-gpt-sources/04-workflows__git-rules.md` — checkpoint culture.  
- `governance/parallel-cursor-chat-work-mode-v0.md` — lane + git rules.
