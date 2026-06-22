# WEB-GPT Chat Synchronization Pack

**Purpose:** Source for **future chat synchronization prompts** — refresh program-specific Web-GPT or Cursor chats without inventing runtime or duplicating full packs.  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb`)  
**Global pack:** `mars-v2-stable-baseline-2026-06/` + `WEB-GPT-SOURCE-PACK-INDEX.md`

**Usage:** Copy the **Sync block** for one program into a new chat after uploading the minimum truth bundle (`01`, `02`, `10`). Re-verify `git status` and lane every session.

---

## Global sync preamble (all programs)

```text
MARS chat sync — Stable Baseline 2026-06.
Workspace: C:\AI MARS. Documentation-first — no MARS orchestrator claims.
Re-read git status; declare lane (A/B/Runtime).
SoT: pack OPERATIONAL-INDEX Core Run — not chat memory.
Governance: maintenance mode — operational-first.
UNKNOWN: state explicitly + verification step.
Close with # REPORT when deliverable required.
```

---

## ORCA

| Field | Value |
|-------|--------|
| **Registry** | `orca` (active) |
| **Canonical entry** | `projects/orca/OPERATIONAL-INDEX.md` — FAST PATH |
| **Lane** | Usually **A** (PPC delivery) or programme-specific |

**Synchronization targets:**

- Live PPC review framework and heuristics — human-supervised only  
- Freeze discipline under `projects/orca/freeze/` when task references frozen exports  
- MIG handoff: **human-only** per `projects/mig/contracts/mig-orca-handoff-contract-v0.md`  
- Optional Factory handoff when strategy/semantic outputs validated for site lane  
- **Exclude:** autonomous bidding, scheduling, validator daemon, MARS runtime ownership  
- **Canvas:** `docs/visualization/obsidian-canvas/orca.canvas` for orientation  

**Sync block:**

```text
Program: ORCA. Entry: projects/orca/OPERATIONAL-INDEX.md (FAST PATH).
Sync: current freeze refs, URL/registry integrity tasks, PPC review scope.
Not: runtime, auto-optimization, MIG auto-transport.
Report: paths under projects/orca/ and workspaces only if chartered.
```

---

## Website Factory

| Field | Value |
|-------|--------|
| **Registry** | `mars-website-factory` (planned/strategic) |
| **Canonical entry** | `projects/mars-website-factory/OPERATIONAL-INDEX.md` — Core Run |
| **Lane** | **B** (methodology) or **A** (reference workspace delivery) |

**Synchronization targets:**

- Workflow v0, prompt/report standards, agent cards as **documentation roles**  
- Reference case: Triumph — workspace is execution locus, not Factory engine proof  
- Frontend: Gulp foundation + optional MARS Forge overlay — not second SoT  
- WPilot: **future** WordPress bridge — boundary language only unless task charters bridge work  
- **Exclude:** autonomous site builder, in-repo deploy platform, runtime factory engine  
- **Canvas:** `docs/visualization/obsidian-canvas/website-factory.canvas`  

**Sync block:**

```text
Program: MARS Website Factory. Entry: projects/mars-website-factory/OPERATIONAL-INDEX.md (Core Run).
Sync: active stage/artifact for this run, HITL gates, QA severity if production QA task.
Not: shipped factory runtime, auto-deploy, Triumph workspace = engine proof.
```

---

## WPilot

| Field | Value |
|-------|--------|
| **Registry** | `wpilot` (active) |
| **Canonical entry** | `projects/wpilot/README.md`, `plugin-mvp/reconciliation-map-v0.md` |
| **Lane** | External Systems — ops docs **B**, implementation **A** only if chartered |

**Synchronization targets:**

- Phase 1 MVP documentation discipline  
- In-repo plugin source: `projects/wpilot/plugin/metacode-wpilot/` — DEV evidence only  
- Production bridge and live WordPress: **external** — SAFE UNKNOWN until operator confirms  
- Factory **Mode B** legacy compatibility references — not WPilot-owned by Factory runtime  
- **Exclude:** autonomous WP admin, MARS core runtime, deploy bot claims from repo alone  

**Sync block:**

```text
Program: WPilot. Entry: projects/wpilot/README.md + reconciliation-map-v0.md.
Sync: task mode (doc vs plugin vs bridge planning), external hosting boundary.
Not: production bridge ownership, autonomous CMS, MARS orchestration.
```

---

## OCPilot

| Field | Value |
|-------|--------|
| **Registry** | `ocpilot` (active) |
| **Canonical entry** | `projects/ocpilot/OPERATIONAL-INDEX.md` |
| **Lane** | External Systems — **B** for baseline/policy; bulk on `C:\AI MARS STORAGE\ocpilot\` |

**Synchronization targets:**

- Read-only audit, baseline passports, controlled-change discipline  
- Baseline bulk: external storage registry — **not** `baselines/**/files/**` in Web-GPT upload  
- EAR snapshots when chartered — consumer does not own acquisition mechanics  
- Sibling to WPilot — not child/parent relationship  
- **Exclude:** autonomous OpenCart admin, in-repo vendor bulk as pack material  

**Sync block:**

```text
Program: OCPilot. Entry: projects/ocpilot/OPERATIONAL-INDEX.md.
Sync: baseline id, passport path, storage registry row — not vendor file trees.
Not: WPilot child, MARS runtime, live site credentials in chat logs.
```

---

## MIG

| Field | Value |
|-------|--------|
| **Registry** | `mig` (active) |
| **Canonical entry** | `projects/mig/OPERATIONAL-INDEX.md` |
| **Lane** | **B** / acquisition charter; R1 tooling = Runtime only when explicit |

**Synchronization targets:**

- Session manifests, evidence grading, handoff packs — v0.1 spine only in-repo  
- **MIG acquires reality; ORCA interprets reality** — human handoff only  
- n8n export in-repo ≠ production deployment proof  
- **Exclude:** autonomous ORCA transport, full SERP/competitor pipeline as shipped  

**Sync block:**

```text
Program: MIG. Entry: projects/mig/OPERATIONAL-INDEX.md.
Sync: session id, evidence grade, handoff pack path for human ORCA transfer.
Not: auto handoff, production orchestration, campaign engine.
```

---

## MARS Search PPC Production

| Field | Value |
|-------|--------|
| **Registry** | `mars-search-ppc-production` (approved lifecycle) |
| **Canonical entry** | `projects/mars-search-ppc-production/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md` |
| **Lane** | **A** when executing search PPC lifecycle work |

**Synchronization targets:**

- Project PPC state manifest **required** before any search PPC chat work  
- Lifecycle validator: `projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs`  
- Opening block: `projects/mars-search-ppc-production/web-gpt/WEB-GPT-OPENING-STATUS-BLOCK-v1.md`  
- Full production corpus rule; human review is **not** default classification engine  
- Corvonero **FROZEN**; P0-I pilot **DIAGNOSTIC EVIDENCE** only  
- **Exclude:** duplicating all 23 stage contracts into chat; invented missing evidence  

**Sync block:**

```text
Program: MARS Search PPC Production. Entry: projects/mars-search-ppc-production/README.md.
Sync: project_id, manifest path, current SPPC stage, validator output, blockers.
Rules: BLOCKED — LIFECYCLE REQUIREMENT NOT MET when evidence missing; no stage skipping.
Not: Corvonero production resume, P0-I as production corpus, bulk manual phrase classification default.
Validator: node projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs <manifest>
```

---

## MetaBOT

| Field | Value |
|-------|--------|
| **Registry** | `metabot-seo-content-agent` (active) — **not** legacy `seo-content-agent` |
| **Canonical entry** | `projects/metabot-seo-content-agent/README.md` |
| **Lane** | External Systems — execution on **n8n** |

**Synchronization targets:**

- Intake / Worker / Admin workflow semantics from in-repo docs  
- Live graph truth: operator **n8n** instance — reconcile exports in `exports/` when pasted  
- R1 webhook adapter under `mars-runtime/` = experimental label only  
- **Exclude:** MARS-owned orchestration, duplicate legacy `projects/seo-content-agent/` extension  

**Sync block:**

```text
Program: MetaBOT (metabot-seo-content-agent). Entry: projects/metabot-seo-content-agent/README.md.
Sync: workflow name, export version if provided — live n8n is execution SoT.
Not: MARS core runtime, in-repo graph authority.
```

---

## HomeGateway

| Field | Value |
|-------|--------|
| **Registry** | `homegateway-v4-ai` (planned/draft) |
| **Canonical entry** | `projects/homegateway-v4-ai/OPERATIONAL-INDEX.md`, `roadmap-v0.1.md` |
| **Lane** | **B** — surface/cockpit planning unless MVP implementation chartered |

**Synchronization targets:**

- Personal Operational Cockpit — static-first, documentation-only at current evidence  
- Display-only signals / quick links — no replacement for ORCA, WPilot, MetaBOT, governance  
- Design/atmosphere WIP may be **outside** baseline checkpoint — re-verify paths  
- **Exclude:** MARS agent, n8n workflow, Telegram bot, deployed backend, control plane claims  

**Sync block:**

```text
Program: HomeGateway v4.ai. Entry: projects/homegateway-v4-ai/OPERATIONAL-INDEX.md.
Sync: roadmap phase, UI semantics doc in scope — not production integrations.
Not: MARS runtime, live n8n/Telegram ownership, autonomous cockpit.
```

---

## Cross-program sync checklist

Before closing a synchronized chat, confirm:

- [ ] Lane declared (A / B / Runtime)  
- [ ] `OPERATIONAL-INDEX` row cited for active program  
- [ ] No forbidden runtime claims ([`10_RUNTIME_BOUNDARY_RULES.md`](mars-v2-stable-baseline-2026-06/10_RUNTIME_BOUNDARY_RULES.md))  
- [ ] External systems marked external  
- [ ] REPORT if task required deliverable  

---

*Chat Sync Pack v1 — Stable Baseline 2026-06 — paste blocks; re-verify from repo each session.*
