# MIG — Market Intelligence Groundtruth

**MIG** = **Market Intelligence Groundtruth** — the MARS **R1** research acquisition layer.

**Current status:** **MIG v0.1 Session Spine implemented and verified** (Node.js + n8n workflow export).  
**Not:** production runtime, automation platform, orchestration product, agents platform, or completed system.

**Lane:** B (Operational / Research Acquisition)  
**Registry:** `mig` — [registry/project-registry.md](../../registry/project-registry.md)

**Pre-pilot freeze (2026-06-01):** Checkpoint `pre-pilot-gruzotaxi-krasnodar-v1` created. First planned pilot: **грузотакси Краснодар** (проект **Триумф**). Pilot **not executed** yet.

---

## System identity

| | |
|--|--|
| **Name** | MIG (Market Intelligence Groundtruth) |
| **Layer** | **R1** — Market Groundtruth Research |
| **Role** | Acquire, normalize, grade, and preserve **market reality** for human review and handoff |
| **Mode** | Human-supervised research acquisition with a **narrow v0.1 runtime slice** |

**Canonical boundary:** *MIG acquires reality. ORCA interprets reality.*

---

## v0.1 capabilities (verified)

The v0.1 Session Spine provides:

- **Intake** — validate session payload via canonical [Research Request contract](contracts/mig-research-request-contract-v0.md) (v0.1 spine: legacy flat map)
- **Manifest** — create and finalize `session_manifest.json`
- **Normalized SERP** — fallback or manual/provider input → `serp_result.json`
- **Draft research pack** — generate `research_pack.draft.md`

**Runtime components (in-repo):**

| Path | Role |
|------|------|
| [lib/session-spine/](lib/session-spine/) | Node.js session spine (shared by CLI and n8n Code nodes) |
| [workflows/n8n/mig-research-session-v0.1.json](workflows/n8n/mig-research-session-v0.1.json) | n8n workflow export (webhook → spine → respond) |
| [schemas/](schemas/) | JSON schemas for manifest and SERP result |
| [test/](test/) | Test payloads and local spine runner |
| [sessions/](sessions/) | Runtime session output (gitignored contents) |
| [config/env.example](config/env.example) | Environment variable reference |

**Local verification:** `projects/mig/test/run-spine-test.ps1` (no n8n required).

---

## v0.1 limitations

- Single query per session (first seed query only)
- No live SERP provider integration
- No competitor capture
- No landing analysis
- No approval workflow
- No ORCA automation or handoff execution
- n8n runtime execution requires self-hosted n8n with filesystem access — **not proven as production deployment**

---

## Purpose (full vision)

MIG owns the **groundtruth acquisition** side of market research:

- SERP capture
- Competitor observation
- Local pack review
- Review capture
- Trust signal capture
- Offer capture
- CTA capture
- Evidence grading
- Snapshot preservation
- Research session manifests

MIG produces **evidence-grade observations** and **approved handoff packs** for downstream interpretation — not campaign or site decisions. Most of the above remains **planned** beyond v0.1.

---

## What MIG is

- Research acquisition system under MARS with a **documented v0.1 runtime slice**.
- Human-supervised capture → normalize → grade → review → approve → handoff lifecycle (full lifecycle **not** automated in v0.1).
- Owner of **market reality artifacts** (snapshots, observations, grades, session manifests).
- Upstream of **ORCA** (R2) for marketing intelligence analysis.

## What MIG is not

- **Not** a production automation platform or agent orchestrator.
- **Not** intent clustering, semantic clustering, LRL, or PPC export tooling.
- **Not** Website Factory blueprints, content generation, or CMS operations.
- **Not** a completed end-to-end research system.

---

## Ecosystem relationships

```text
MIG          → R1 Market Groundtruth (this pack)
ORCA         → R2 Marketing Intelligence Analysis
Website Factory → R3 Strategy + Site Production
WPilot / OCPilot → Implementation Layer (external CMS)
MetaBOT      → External n8n / Telegram cluster (separate from MIG spine)
mars-runtime → Future-integration contracts + narrow R1 experiments
```

| System | Relationship |
|--------|----------------|
| **ORCA** | **Primary consumer** of approved MIG handoffs. MIG **does not** interpret clusters, campaigns, or PPC architecture. See [contracts/mig-orca-handoff-contract-v0.md](contracts/mig-orca-handoff-contract-v0.md). |
| **Website Factory** | **Downstream** of ORCA/strategy — MIG **does not** own site blueprints, Factory semantics, or production contracts. |
| **MetaBOT** | **Separate external** n8n/Telegram execution lane. MIG v0.1 uses its **own** n8n workflow export; no MetaBOT dependency. |
| **WPilot / OCPilot** | **No direct handoff.** Implementation layer (external). |
| **mars-runtime** | **No execution dependency** for v0.1 spine. |

---

## Structure

| Path | Role |
|------|------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Minimal navigation — **start here** |
| [system-overview.md](system-overview.md) | R1 mission, inputs/outputs, lifecycle |
| [boundaries.md](boundaries.md) | Ownership matrix — **canonical boundaries** |
| [contracts/](contracts/) | Domain contracts — Research Request (intake SoT), Research Pack (output SoT), [Reality Acquisition Model](contracts/MIG-REALITY-ACQUISITION-MODEL-v1.md) (R1–R4 trust stack), Competitor Discovery (Phase 2), ORCA handoff |
| [reports/](reports/) | Session report templates |

---

## Operator rule (v0.1)

Before any research session: read [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) → [boundaries.md](boundaries.md).  
Run local spine test or n8n workflow with [test/test-payload-fallback-v0.1.json](test/test-payload-fallback-v0.1.json).  
Hand off to ORCA only via [contracts/mig-orca-handoff-contract-v0.md](contracts/mig-orca-handoff-contract-v0.md) after human **Approved By**.  
Report using [reports/REPORT-TEMPLATE.md](reports/REPORT-TEMPLATE.md).

Default: state **SAFE UNKNOWN** when evidence or scope is incomplete — do not infer downstream semantics.
