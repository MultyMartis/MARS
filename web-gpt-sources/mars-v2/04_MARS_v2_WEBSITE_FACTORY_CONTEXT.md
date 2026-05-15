# MARS v2 — Website Factory context

**Status:** **OPERATIONAL** methodology · **PLANNED** full automation

**project_id:** `mars-website-factory`

---

## Purpose

**MARS Website Factory** is a **documentation-first operational methodology** for **multi-agent, contract-driven** marketing-site production: intake → strategy → IA → blueprints → design → frontend → QA → HITL → delivery.

It extends MARS task/workflow/Validator concepts into a **factory story** — primarily through **markdown contracts, registries, runbooks, and prompt discipline**.

---

## Classification (explicit)

| Statement | Status |
|-----------|--------|
| Documentation-first methodology | **CORE** |
| Strategic planned direction in MARS ecosystem | **CORE** |
| Shipped in-repo orchestration engine | **EXCLUDED** — not evidenced |
| Autonomous AI design/dev studio | **EXCLUDED** |
| Single bot or monolithic agent | **EXCLUDED** |
| Replacement for MetaBOT SEO pack | **EXCLUDED** — separate external system |

**MARS is NOT** Website Factory runtime. Factory **does not** make MARS a production runtime.

---

## Operating reality (Phase 1)

```
Human operator + Cursor/Codex + prompts/runbooks/contracts + REPORT + explicit git
```

- Workflows and stage models are **targets** and **semantics**.
- **prompt → execute → report** = **OPERATIONAL** pattern, not a scheduler.
- Frontend center: documented **Gulp / static** profile (`frontend-production-model.md`, agent packs).

---

## Layers (summary)

| Layer | Role |
|-------|------|
| Strategy / SEO / marketing | Intent models, site-type registry |
| IA / blueprints | Page blueprint contract, block registry |
| Design | Handoff contract; **no** proven auto-Figma pipeline |
| Frontend | Handoff + Gulp discipline; source-first, no `dist/` edits |
| QA / validation | Gates, checklists, Validator **role** — human-operated meaning |
| Delivery | Lifecycle semantics; export packages — not auto-deploy |
| Cross-cutting | Artifact bus / semantic graph vocabulary — **documentation only**, not queues or graph DB |

**Seven target layers** detailed in `layer-map.md` (REPO-ONLY).

---

## Workflow (summary)

Canonical stages in `website-factory-workflow-v0.md` and `first-operational-runbook-v0.md`:

- Human-driven progression with **HITL** checkpoints.
- Artifact immutability, approval inheritance, revision/regeneration semantics.
- QA gating blocks delivery on documented rules — **human** waiver/override.

**Orchestration signals** = vocabulary aligned with system signals dictionary — **not** event bus.

---

## Frontend / design / validation roles

| Concern | Pack entry (in repo) |
|---------|----------------------|
| Cursor execution | `cursor-execution-standard-v0.md` |
| Frontend prompts | `frontend-prompt-discipline-v0.md` |
| Reporting | `reporting-standard-v0.md` |
| QA prompts | `qa-prompt-rules-v0.md` |
| Validation semantics | `validation-runtime-overview-v0.md` — **not** validator engine |
| Honesty boundary | `safe-unknown-boundary.md` |

---

## Reference case exclusion (Triumph)

| Path | Role |
|------|------|
| `projects/triumph-manipulator-landing/` | Project **documentation** pack |
| `projects/mars-website-factory/reference-cases/triumph-manipulator-landing/` | **Simulated** documentation-first run — **not** built-site proof |
| `workspaces/triumph-manipulator-landing-v2/` | **Project workspace** — **not** MARS core; `src/**` **EXCLUDED** from Web-GPT packs |

Do **not** promote Triumph delivery assets as MARS core or Factory runtime evidence.

---

## SAFE UNKNOWN (factory-specific)

- gulp-starter template inside vs outside MARS repo.
- Wire formats for future Execution Bridge handoff to Factory.
- Automatic Figma / n8n / Cursor integration — **future**, **optional**, unspecified.

---

## Canonical repo entry points

1. `projects/mars-website-factory/README.md` — pack index  
2. `projects/mars-website-factory/OPERATIONAL-INDEX.md` — short operator map  
3. `projects/mars-website-factory/system-overview.md` — vision and boundaries  

*This file is a Web-GPT distillate; do not treat it as superseding governance or pack README.*
