# MARS Post-Cleanup Ecosystem State Snapshot — 2026-06

**Date:** 2026-06-03  
**Context:** Cleanup Program closeout after Wave 2B + Post-Cleanup Audit v1 (**PARTIAL PASS**)  
**Baseline anchor:** `45518bb` / `mars-v2-stable-baseline-2026-06` (publication); working tree includes post-cleanup alignment  
**SoT routers:** `registry/project-registry.md`, `governance/mars-reality-index-v0.md`, `governance/ecosystem-topology-index.md`

This file is a **point-in-time snapshot** for operators and Web-GPT — not registry SoT.

---

## Summary table

| System | Status (post-cleanup) | Canonical entry |
|--------|----------------------|-----------------|
| **GitGuard** | **REGISTERED** — Repository Survivability Layer; no `project_id`; implementation under mars-survivability | `projects/mars-survivability/registries/gitguard-system-entry-v1.md` |
| **IdeaBox** | **OPERATIONAL** — optional Incubation Layer; not a project row | `continuity/README.md` |
| **Incoming** | **OPERATIONAL** — hybrid Active Incoming (repo) + Historical Bulk (Storage after triage) | `incoming/README.md` |
| **Lifecycle log** | **OPERATIONAL** — Key Event History default; optional Tracking Mode; evt 0017–0021 backfilled | `logs/lifecycle-log.md` |
| **ISBD Care Landing** | **REGISTERED** — Website Factory execution case (not `project_id`) | `projects/mars-website-factory/execution-cases-registry-v1.md` |
| **HomeGateway v4.ai** | **PLANNED** — three-layer: registry `planned` + doc-pack discipline + UI prototype workspace | `projects/homegateway-v4-ai/OPERATIONAL-INDEX.md` |
| **Triumph authority** | **CANONICAL v6** — authority map; v1–v5 archive candidates on disk | `projects/triumph-manipulator-landing/triumph-workspace-authority-map-v1.md` |

---

## GitGuard

| Attribute | Value |
|-----------|--------|
| **Classification** | REGISTERED cross-cutting — Repository Survivability Layer |
| **`project_id`** | **None** (by design) |
| **`projects/gitguard/`** | **Does not exist** — avoids pack inflation |
| **Implementation** | `projects/mars-survivability/` — contracts, validator, human-invoked helpers |
| **Maturity** | Operational (human-supervised advisory); G3+ hooks / rollback JSON artefacts deferred |
| **Evidence** | Wave 2B `gitguard-registration-v1.md`; Wave 2A cross-link alignment |

**Not:** autonomous backup/checkpoint/rollback product, policy engine, or runtime orchestration.

---

## IdeaBox

| Attribute | Value |
|-----------|--------|
| **Path** | `continuity/` |
| **Role** | Optional **Incubation Layer** — deferred ideas; direct `projects/*` creation remains valid |
| **Registry** | Cross-cutting note in `registry/project-registry.md` — **no** `project_id` row |
| **Volume** | Low — substantive captures + protocols |
| **Residual** | Empty `continuity/registry/master-index.md` sections (optional population) |

**Not:** agent memory, orchestration, or governance auto-mutation.

---

## Incoming

| Attribute | Value |
|-----------|--------|
| **Policy** | Documented in `incoming/README.md` (Wave 2A create; Wave 2B hybrid alignment) |
| **Active Incoming** | Repo-root `incoming/` — e.g. `incoming/mig/` operational |
| **Historical Bulk** | Toward `C:\AI MARS STORAGE` / Cold Brain **after** operator triage — no Wave 2B folder moves |
| **Excluded from baseline checkpoint** | By design at `45518bb` |
| **Triage backlog** | `orca-triumph-raw-pack/`, `metabot/`, `website-factory-legal-cleanup/`, `mars-bridge/` stub — documented, not SoT corruption |

**Not:** Knowledge Center, runtime intake automation, or authoritative until promoted.

---

## Lifecycle

| Attribute | Value |
|-----------|--------|
| **SoT** | `logs/lifecycle-log.md` — append-only governance events |
| **Model** | Key Event History (default); optional Lifecycle Tracking Mode for long operations |
| **Distinct from** | `logs/cleanup/` (audit trail), `logs/releases/` (publication), routine task REPORTs |
| **Backfill** | evt **0017–0021** (Wave 2A) — approximate timestamps flagged |
| **Deferred** | Mandatory append on every registry edit (L-03); optional cleanup-milestone evt (L-01) |

**Not:** proof of implementation or automated enforcement.

---

## ISBD

| Attribute | Value |
|-----------|--------|
| **Classification** | Website Factory **execution case** `isbd-care-landing` — **not** `project_id` |
| **Workspace** | `workspaces/isbd-care-landing/` |
| **Registry** | `projects/mars-website-factory/execution-cases-registry-v1.md` + reference-case overview |
| **Census gap** | **Closed** (Wave 1A) |

**SAFE UNKNOWN:** production deployment / WP insertion — external hosting evidence.

---

## HomeGateway

| Attribute | Value |
|-----------|--------|
| **Registry `status`** | `planned` |
| **Layers** | (1) planned program row (2) operational **documentation pack** discipline (3) UI prototype `workspaces/homegateway-v4-ai/v1/` |
| **Product band** | Personal Operational Cockpit — STATIC-FIRST target; draft/planning |
| **Census conflict** | D-004 semantic overload — **mitigated** in registry boundaries + OPERATIONAL-INDEX |

**Not:** deployed product, MARS runtime, or control plane replacement.

---

## Triumph authority

| Attribute | Value |
|-----------|--------|
| **Canonical workspace** | `triumph-manipulator-landing-v6` |
| **Authority map** | `projects/triumph-manipulator-landing/triumph-workspace-authority-map-v1.md` |
| **`project_id`** | `triumph-manipulator-landing` (planned) |
| **ORCA calibration** | Retargeted to v6 (Wave 1A) |
| **On-disk sprawl** | v1–v5 remain — archive candidates; operator-gated moves deferred |
| **Factory relationship** | Reference + execution case linkage documented |

**Not:** proof that all workspace generations are production-deployed.

---

## Composite health (from audit)

Unweighted mean **7.7 / 10** across registry, classification, relationship, terminology, survivability, documentation consistency dimensions. See [MARS-POST-CLEANUP-AUDIT-v1.md](../cleanup/MARS-POST-CLEANUP-AUDIT-v1.md).

---

## Related closeout artefacts

| Artefact | Path |
|----------|------|
| Program closeout | `logs/cleanup/MARS-CLEANUP-PROGRAM-CLOSEOUT-2026-06.md` |
| Checkpoint recommendation | `logs/releases/post-cleanup-checkpoint-recommendation-2026-06.md` |
| Web-GPT refresh | `web-gpt-sources/REPORT-WEB-GPT-PACK-REFRESH-2026-06.md` |

---

*Post-cleanup ecosystem snapshot — 2026-06-03 — Lane B closeout.*
