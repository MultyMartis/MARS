# MIG — Operational Index

**Status:** **MIG Runtime MVP implemented** (`run-mig-session.js`, manifest v0.2); **v0.1 Session Spine** and Task File intake verified. Operational model: [contracts/mig-operational-runtime-architecture-v1.md](contracts/mig-operational-runtime-architecture-v1.md).  
**Not:** production n8n deployment, approval automation, or ORCA transport API.

**Domain root:** [README.md](README.md)

**Pre-pilot checkpoint (2026-06-01):** Freeze `pre-pilot-gruzotaxi-krasnodar-v1` — baseline before first real pilot (**грузотакси Краснодар / проект Триумф**). **Pilot #1 executed** — session `mig-20260604-61b585` (see `incoming/mig/completed/request-triumph-gruzotaxi-krasnodar-v1.outcome.json`). Archive: [archive/pre-pilot-gruzotaxi-krasnodar-v1/README.md](archive/pre-pilot-gruzotaxi-krasnodar-v1/README.md).

**MVP validation freeze (2026-06-05):** [reports/MIG-MVP-VALIDATION-FREEZE-v1.md](reports/MIG-MVP-VALIDATION-FREEZE-v1.md) — proven capabilities on **Грузотакси / Краснодар** (sessions `61b585`, `mqgt01`, `mlint01`, `gtrgt01`). Pilot evidence: [../../incoming/mig/pilots/triumph-gruzotaxi-krasnodar/](../../incoming/mig/pilots/triumph-gruzotaxi-krasnodar/).

---

## Core Run

| # | Topic | Document / path |
|---|--------|-----------------|
| 1 | **System Identity** | [README.md](README.md) |
| 2 | **Research Session (v0.1 spine)** | [system-overview.md](system-overview.md); [lib/session-spine/](lib/session-spine/) |
| 3 | **Local test** | [test/run-spine-test.ps1](test/run-spine-test.ps1) + [test/test-payload-fallback-v0.1.json](test/test-payload-fallback-v0.1.json) |
| 4 | **n8n workflow export** | [workflows/n8n/mig-research-session-v0.1.json](workflows/n8n/mig-research-session-v0.1.json) |
| 5 | **Environment** | [config/env.example](config/env.example) — `MIG_SESSION_ROOT`, `MIG_LIB_ROOT` |
| 6 | **Evidence Review** | [system-overview.md](system-overview.md); [boundaries.md](boundaries.md) |
| 7 | **Research Request (intake SoT)** | [contracts/mig-research-request-contract-v0.md](contracts/mig-research-request-contract-v0.md) |
| 8 | **Task File Adapter (intake)** | [contracts/mig-task-file-adapter-spec-v0.1.md](contracts/mig-task-file-adapter-spec-v0.1.md); drop zone [../../incoming/mig/README.md](../../incoming/mig/README.md); run [tools/run-task-file-adapter.ps1](tools/run-task-file-adapter.ps1); verify [tools/verify-adapter-runtime-or09.mjs](tools/verify-adapter-runtime-or09.mjs) |
| 9 | **Research Pack (output SoT)** | [contracts/mig-research-pack-contract-v0.md](contracts/mig-research-pack-contract-v0.md) |
| 10 | **Competitor Discovery (Phase 2 design)** | [contracts/mig-competitor-discovery-contract-v0.md](contracts/mig-competitor-discovery-contract-v0.md) |
| 10b | **Multi-Query Discovery (v0.3 design)** | [contracts/mig-multi-query-discovery-design-v0.md](contracts/mig-multi-query-discovery-design-v0.md) |
| 10c | **Website Acquisition (Phase 3 architecture)** | [contracts/mig-website-acquisition-architecture-v1.md](contracts/mig-website-acquisition-architecture-v1.md) |
| 10d | **Keyword Intelligence (architecture v1)** | [contracts/mig-keyword-intelligence-architecture-v1.md](contracts/mig-keyword-intelligence-architecture-v1.md) |
| 10e | **Landing Analysis (architecture v1)** | [contracts/mig-landing-analysis-architecture-v1.md](contracts/mig-landing-analysis-architecture-v1.md) |
| 10e2 | **Landing Analysis v2 (design)** | [contracts/mig-landing-analysis-v2.md](contracts/mig-landing-analysis-v2.md) · [REPORT](reports/REPORT-mig-landing-analysis-v2-design.md) · [families](contracts/mig-landing-observation-families-v2.md) · [offer](contracts/mig-landing-offer-model-v2.md) · [trust](contracts/mig-landing-trust-signals-model-v2.md) |
| 10f | **Deep Research (architecture v1)** | [contracts/mig-deep-research-architecture-v1.md](contracts/mig-deep-research-architecture-v1.md) |
| 10g | **Runtime Assembly (architecture v1)** | [contracts/mig-runtime-assembly-v1.md](contracts/mig-runtime-assembly-v1.md) — end-to-end session lifecycle |
| 10h | **Operational Runtime (architecture v1)** | [contracts/mig-operational-runtime-architecture-v1.md](contracts/mig-operational-runtime-architecture-v1.md) — MIG inside MARS: deployment, storage, operator workflow, n8n role, ORCA handoff |
| 10i | **Reality Acquisition Model (v1)** | [contracts/MIG-REALITY-ACQUISITION-MODEL-v1.md](contracts/MIG-REALITY-ACQUISITION-MODEL-v1.md) — R1–R4 trust stack, Human Review Mode, `evidence/review.md` |
| 11 | **MIG → ORCA Handoff** | [contracts/mig-orca-handoff-contract-v0.md](contracts/mig-orca-handoff-contract-v0.md) |
| 12 | **Reporting** | [reports/REPORT-TEMPLATE.md](reports/REPORT-TEMPLATE.md) |
| 12b | **MVP Validation Freeze (v1)** | [reports/MIG-MVP-VALIDATION-FREEZE-v1.md](reports/MIG-MVP-VALIDATION-FREEZE-v1.md) |
| 12c | **Phase 2 Keyword Surface Charter (v1)** | [reports/MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](reports/MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) |
| 13 | **Data Acquisition Architecture (v1)** | [reports/REPORT-mig-data-acquisition-architecture-v1.md](reports/REPORT-mig-data-acquisition-architecture-v1.md) |
| 14 | **Reality Acquisition Model (report)** | [reports/REPORT-mig-reality-acquisition-model-v1.md](reports/REPORT-mig-reality-acquisition-model-v1.md) |

---

## v0.1 capability snapshot

| Capability | Status |
|------------|--------|
| Task File intake (drop zone + adapter) | Implemented (human-invoked) |
| Intake validation | Implemented |
| Session manifest | Implemented |
| Normalized SERP (fallback/manual/provider stub) | Implemented |
| Draft research pack | Implemented |
| Live SERP provider | Not implemented |
| Competitor discovery (MVP) | Implemented (verify scripts) |
| Website acquisition (MVP) | Implemented (verify scripts) |
| Landing Analysis (structured pass) | **Implemented** (Pilot #1 session evidence); v2 operator model **design only**: [contracts/mig-landing-analysis-v2.md](contracts/mig-landing-analysis-v2.md) |
| Deep Research (synthesis pass) | Not implemented — architecture: [contracts/mig-deep-research-architecture-v1.md](contracts/mig-deep-research-architecture-v1.md) |
| Approval workflow | Not implemented |
| ORCA automation | Not implemented |

---

## Canonical boundaries

**MIG acquires reality. ORCA interprets reality.**

Ecosystem rule (Groundtruth Owner R1): [../../shared/contracts/groundtruth-ownership-rule-v1.md](../../shared/contracts/groundtruth-ownership-rule-v1.md)

Full matrix: [boundaries.md](boundaries.md)
