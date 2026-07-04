# Current operational state (v1)

**Status:** **documented** — canonical visibility snapshot.  
**Version:** v1 (operational state stabilization).  
**As-of discipline:** Re-verify with `git status` and lane charter on every session; this file is **not** live telemetry.  
**Authority:** [AGENTS.md](../AGENTS.md) / [.cursorrules](../.cursorrules) > this file; CURRENT Web-GPT sync pack: [web-gpt-sources/mars-current-x-drive-2026-06/](../web-gpt-sources/mars-current-x-drive-2026-06/) (X-drive current pack; chat synchronization distillate — **not** source of repo truth; repo governance wins on conflict). Historical packs (`mars-v2/`, `mars-v2-final/`, `mars-v2-stable-baseline-2026-06*`, numbered legacy topics) are **legacy / investigation only**.  
**Supersedes for SoT:** migration snapshot `web-gpt-sources/chat-migration/02-current-operational-state.md` (reference only).

---

## How to read this document

| Bucket | Meaning |
|--------|---------|
| **operational** | Used **today** in real **human-supervised** workflows. |
| **experimental** | Bounded in-tree probes; REPORT + lane isolation. |
| **conceptual** | Contracts and vocabulary; no shipped MARS product. |
| **future** | May exist later; **not** commitment language. |
| **excluded** | Do not treat as canonical MARS core or extend as SoT. |
| **historical** | Legacy import; reference with three-way split. |

**Anti-mythology pattern:** every major area states **what it is not**.

**Registry row ≠ deployed system** — catalogs document intent; they do not prove running services.

**Post–Cycle 8 posture (2026-05-19):** structural stabilization and survivability baseline **achieved**; governance baseline **frozen** in **maintenance mode**; primary effort is **operational-first** (ORCA, Factory, Triumph, external bridges). **Canonical ecosystem state:** [mars-operational-evolution-state-after-cycles-1-8-v0.md](mars-operational-evolution-state-after-cycles-1-8-v0.md). Task routing: [mars-operational-evolution-transition-index-v0.md](mars-operational-evolution-transition-index-v0.md).

---

## Operator infrastructure (physical)

| Layer | Path | Role |
|-------|------|------|
| **Active Brain** | `X:\AI MARS\` | This Git repository — governance, projects, workspaces, docs. |
| **Storage layer** | `X:\AI MARS STORAGE\` | Out-of-git bulk — **not** a second repo or governance root. |
| **Local runtime** | `X:\MARS-Localhost\` | Laragon, CMS, databases — **external** to Git; execution only. |

**Volume:** `X:` — label **AI WS**. **Authority:** [mars-x-drive-root-authority-v1.md](mars-x-drive-root-authority-v1.md), [mars-infrastructure-reality-v1.md](mars-infrastructure-reality-v1.md). **X-drive migration:** X0–X9 **COMPLETE** — [mars-x-drive-migration-closure-v1.md](mars-x-drive-migration-closure-v1.md). Remaining old-path families deferred per [mars-x-drive-deferred-path-register-v1.md](mars-x-drive-deferred-path-register-v1.md). Historical C/D/E paths in incident evidence are **not** current targets.

**Brain layers (organizational):** Visual Brain source `X:\AI MARS\docs\visualization\obsidian-canvas\`; Knowledge Center `X:\AI MARS STORAGE\MARS KNOWLEDGE CENTER\`; Cold Brain `X:\AI MARS STORAGE\ARCHIVE\` — operator layers, not autonomous memory services.

---

## Governance layer

| Bucket | What exists |
|--------|-------------|
| **operational** | `governance/**` maintained as human-readable control docs — **maintenance mode** post–Cycle 8 (freeze baseline, light hygiene); Phases S1–S7 and reality-audit semantics; [enforcement/](enforcement/README.md) checklists; parallel chat lanes ([parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md)); master build map as **roadmap documentation**. New governance waves require **explicit charter** — not default session work. |
| **conceptual** | Execution contracts (S4), operationalization semantics (S5–S6), experiment framework (S7) — **semantics**, not engines. |
| **future** | Automated governance validation, policy engine, certification product. |
| **excluded** | Treating governance markdown as runtime enforcement or CI substitute without explicit external setup. |

**What it is not:** autonomous policy engine; repo-wide auto-enforcer; proof that every stage in `master-build-map.md` is implemented.

---

## Execution model

| Bucket | What exists |
|--------|-------------|
| **operational** | Primary loop: **task/envelope → prompt (Web-GPT) → execute (Cursor/Codex on repo) → REPORT → validation (human meaning)** per [execution-model.md](execution-model.md); Web-GPT packaging via [mars-current-x-drive-2026-06/](../web-gpt-sources/mars-current-x-drive-2026-06/) (CURRENT sync pack — chat distillate; AGENTS / .cursorrules win on conflict). HITL for approvals, security stops, delivery. |
| **conceptual** | Task/workflow contracts under `workflows/`; execution phase vocabulary; task envelope standard. |
| **future** | Durable MARS task store; in-repo dispatcher; daemon enforcing full chain. |
| **excluded** | “MARS executes end-to-end without human initiation.” |

**What it is not:** orchestration engine; automatic multi-agent dispatch; Web-GPT as substitute for editor or git.

---

## Source-pack (`web-gpt-sources/`)

| Bucket | What exists |
|--------|-------------|
| **operational** | CURRENT Web-GPT sync pack: `web-gpt-sources/mars-current-x-drive-2026-06/` (X-drive current pack; chat synchronization distillate — **not** source of repo truth; repo governance / AGENTS / .cursorrules win on conflict). |
| **historical** | `mars-v2/`, `mars-v2-final/`, `mars-v2-stable-baseline-2026-06*`, numbered topic import (`01_system.md`, `02_architecture.md`, …) — **legacy / investigation only**. |
| **conceptual** | Terminology and architecture narrative inside packs — interpret via three-way split. |
| **excluded** | Treating pack paths like `02-core/...` as live repo roots (see [13_migration.md](../web-gpt-sources/13_migration.md)). |

**What it is not:** proof of implementation; current repository layout map without cross-check to root README.

---

## Website Factory

| Bucket | What exists |
|--------|-------------|
| **operational** | Documentation-first methodology under `projects/mars-website-factory/`: workflow v0, runbook, operator index, prompt/report standards, agent cards (documentation roles), human-driven stages with HITL. |
| **conceptual** | Seven-layer story, artifact bus vocabulary, validation **models** — semantics only. |
| **future** | Execution Bridge wire formats to Factory; optional deeper tool integration. |
| **excluded** | Autonomous AI factory; in-repo orchestration runtime; auto-deploy; monolithic bot. |

**What it is not:** MARS production runtime; replacement for MetaBOT SEO pack; proof that Triumph workspace output equals Factory engine.

**Reference case:** `projects/triumph-manipulator-landing/` and `workspaces/triumph-manipulator-landing-v2/` are **project delivery**, not Factory runtime evidence.

---

## Runtime boundary (`mars-runtime/`)

| Bucket | What exists |
|--------|-------------|
| **conceptual** | v0 contracts: execution bridge, queue, orchestrator, context, lifecycle, deployment models (`*-v0.md`). |
| **experimental** | Narrow R1 JavaScript: human-invoked `node` scripts, adapters (e.g. n8n webhook handoff), test runners — per [mars-runtime/README.md](../mars-runtime/README.md). |
| **boundary only** | R1 posture: **BOUNDARY ONLY / EXPERIMENTAL** — not production runtime. |
| **future** | Workers, schedulers, queues, worker pools, daemon host, fleet-wide operational runtime. |
| **excluded** | Claims of autonomous orchestration, deployed validator runtime, or control plane implementation without new evidence. |

**What it is not:** schedulers, queues, worker pools, or daemons **as shipped MARS** (no repo evidence); proof of MetaBOT or Factory automation.

**Do not imply without path proof:** production orchestrator, queue consumer, 24/7 MARS core, self-managing runtime.

---

## Helper tools (`tools/`)

| Bucket | What exists |
|--------|-------------|
| **operational** | Manual-assist scripts (e.g. registry-checker, governance-scanner, markdown-link-validator) run by operator; helper discipline docs. |
| **experimental** | Pilot utilities; local-only checks — not platform proof. |
| **conceptual** | Tool contracts and permission models under `tools/*.md`. |
| **future** | Tool layer product host integrated with MARS runtime. |
| **excluded** | Helpers as governance enforcers or hidden orchestration. |

**What it is not:** tooling platform; autonomous scanner governing commits; substitute for REPORT and human review.

---

## Operational chats

| Bucket | What exists |
|--------|-------------|
| **operational** | Multiple Cursor chats on **one** working copy; lane discipline (A production, B MARS core, Runtime explicit); session bootstrap with fresh `git status`; REPORT closeout per [AGENTS.md](../AGENTS.md). |
| **conceptual** | Migration pack under `web-gpt-sources/chat-migration/` — bootstrap sequences, not live state. |
| **future** | Chat memory isolation, automatic routing, cross-chat queues. |
| **excluded** | Assuming clean tree or lane from prior chat without verification. |

**What it is not:** multi-tenant runtime; automatic lane router; persisted orchestration state in MARS core.

---

## External systems

| Bucket | What exists |
|--------|-------------|
| **operational** | Documented integration boundaries: MetaBOT SEO Content Agent (`projects/metabot-seo-content-agent/`) as **external** n8n multi-workflow system; operator-configured webhooks for R1 experiments. |
| **boundary only** | Adapters under `mars-runtime/adapters/` — handoff sketches, not ownership of external SLAs. |
| **excluded** | Legacy `projects/seo-content-agent/` as canonical extension target. |
| **future** | Standardized bridge consumer across programs (SAFE UNKNOWN until adopted). |

**What it is not:** systems “inside” MARS core; automatic sync from external catalog to governance registries.

---

## Workspaces / projects

| Bucket | What exists |
|--------|-------------|
| **operational** | **Lane A:** `workspaces/*` implementation work (e.g. Triumph landing). **Lane B:** `projects/mars-website-factory/`, `governance/`, `agents/`, `registry/`. **Runtime lane:** `mars-runtime/*` only when chartered. **Search PPC:** `projects/mars-search-ppc-production/` — cross-system lifecycle authority (`mars-search-ppc-production` registry row). |
| **conceptual** | `registry/project-registry.md` rows — human-maintained classification. |
| **excluded** | `workspaces/**/dist/**` as source of truth; vendor trees (e.g. Font Awesome Pro under `shared/`) committed without license policy; `projects/seo-content-agent/` canonical work. |
| **historical** | Early SEO agent tree; old Web-GPT numbered topics. |

**What it is not:** registry row = deployed site or running factory stage.

---

## Infrastructure programmes (not all `project_id` rows)

| System | Bucket | Canonical entry |
|--------|--------|-----------------|
| **MARS Localhost Infrastructure (MLI)** | operational (enablement) | `projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md` — runtime `X:\MARS-Localhost\` |
| **Forge WordPress / AG-WP-001** | operational (foundation) | `projects/mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md` — Factory subsystem |
| **FOUNDRY** | operational (reference workspace) | `workspaces/website-factory-reference-v1/` — **not** separate `project_id` |
| **EAR Architecture** | conceptual (frozen) | `shared/external-access-runtime/OPERATIONAL-INDEX.md` — runtime engineering in `ear-runtime` |
| **GitGuard** | operational (advisory) | `projects/mars-survivability/registries/gitguard-system-entry-v1.md` — cross-cutting Survivability |

---

## Summary matrix

| Area | operational | experimental | conceptual | future | excluded / historical |
|------|-------------|--------------|------------|--------|------------------------|
| Governance docs | ✓ maintenance | — | ✓ contracts | auto-enforcement | fake runtime |
| Execution loop | ✓ human+Cursor | — | ✓ workflows | dispatcher | autonomous E2E |
| Source-pack | ✓ current X-drive pack | — | ✓ narratives | — | mars-v2 / legacy paths as live |
| Website Factory | ✓ methodology | — | ✓ layers/bus | bridge wire | AI factory runtime |
| mars-runtime | — | ✓ R1 only | ✓ contracts | full runtime | queues/daemons |
| tools/ | ✓ manual helpers | ✓ pilots | ✓ contracts | tool host | enforcers |
| Chats / lanes | ✓ discipline | — | migration docs | auto-route | memory product |
| External (MetaBOT) | ✓ docs + ops | R1 webhook | boundaries | standard bridge | legacy seo tree |
| Projects / workspaces | ✓ delivery | — | registry rows | — | dist/vendor/legacy |

---

## SAFE UNKNOWN (session-level)

Re-verify on each task — do not inherit from this file alone:

- Current `git status` and active lane.  
- Live parity between R1 adapter code and external workflows.  
- Whether untracked vendor assets may be committed.  
- Deployment URLs and secrets without operator paste.

---

## Related stabilization

- [mars-operational-evolution-state-after-cycles-1-8-v0.md](mars-operational-evolution-state-after-cycles-1-8-v0.md) — **canonical** post–Cycles 1–8 ecosystem posture  
- [mars-ecosystem-state-synchronization-review-v0.md](mars-ecosystem-state-synchronization-review-v0.md) — continuity / deprecated assumptions (sync pass)  
- [mars-reality-index-v0.md](mars-reality-index-v0.md) — **compact** bucket-oriented reality (Phase 2; prefer for fast orientation)  
- [canonical-terminology-registry.md](canonical-terminology-registry.md) — term-level rules  
- [runtime-registry-boundaries.md](runtime-registry-boundaries.md) — registry illusion prevention  

*Do not treat this document as superseding [AGENTS.md](../AGENTS.md) honesty rules.*
