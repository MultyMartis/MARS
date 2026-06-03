# Discoveries — MARS Ecosystem Integrity Census v1

**Date:** 2026-06-03  
**Pass:** Full-repo inventory (read-only)  
**Evidence commit context:** Post baseline `45518bb`; working tree may contain uncommitted WIP (git status not frozen for this pass)

---

## D-001 — Registered programs (project-registry SoT)

| project_id | status (registry) | Pack path |
|------------|-------------------|-----------|
| `mars-core` | planned (example) | — |
| `seo-content-agent` | planned (legacy) | `projects/seo-content-agent/` |
| `metabot-seo-content-agent` | active | `projects/metabot-seo-content-agent/` |
| `mars-website-factory` | planned (strategic) | `projects/mars-website-factory/` |
| `triumph-manipulator-landing` | planned | `projects/triumph-manipulator-landing/` |
| `orca` | active | `projects/orca/` |
| `mig` | active | `projects/mig/` |
| `ocpilot` | active | `projects/ocpilot/` |
| `ear-runtime` | active (engineering) | `projects/ear-runtime/` |
| `mars-survivability` | active | `projects/mars-survivability/` |
| `nova` | planned (foundation) | `projects/nova/` |
| `wpilot` | active | `projects/wpilot/` |
| `homegateway-v4-ai` | planned | `projects/homegateway-v4-ai/` |

---

## D-002 — Cross-cutting systems (no project_id)

| Entity | Path | Topology / registry note |
|--------|------|---------------------------|
| IdeaBox / Continuity | `continuity/` | Explicitly **not** a `project_id` row |
| MARS Core contract layers | root: `control-plane/`, `workflows/`, `interfaces/`, `security/`, `memory/`, `observability/`, `evaluation/`, `storage/`, `models/`, `integrations/` | Conceptual / doc-first per `AGENTS.md` |
| MARS Forge | `agents/mars-forge/` | Overlay; in `agents/registry.md` |
| Gulp Frontend Agent | `agents/frontend-gulp-agent/` | operational_doc_pack |
| GitGuard (concept) | `projects/mars-survivability/registries/gitguard-system-entry-v1.md` | **No** `projects/gitguard/`; entity-model example |
| Knowledge Center / Visual Brain | Out-of-git `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER`; git mirror `docs/visualization/obsidian-canvas/` | Operator navigation; not registry row |
| Cold Brain | `C:\AI MARS STORAGE\ARCHIVE` (per baseline infra doc) | Per-item SAFE UNKNOWN |
| MARS Bridge (stub) | `incoming/mars-bridge/mars-bridge-workflow.json` | `bridge_stub`; not registered |

---

## D-003 — Unregistered in project-registry (in-repo evidence)

| Entity | Evidence path | Gap type |
|--------|---------------|----------|
| **ISBD Care Landing** | `workspaces/isbd-care-landing/` (gulp workspace, nested `.git`, `PROJECT-STATUS.md`) | Workspace + client delivery; **no** `project_id`; canvas placeholder SAFE UNKNOWN |
| **MARS Bridge** | `incoming/mars-bridge/` | Contract/stub only; no program row |
| **Incoming drops** | `incoming/metabot/`, `incoming/mig/`, `incoming/orca-triumph-raw-pack/`, `incoming/website-factory-legal-cleanup/` | Operational intake; not programs |
| **ORCA nested container** | `projects/orca/projects/triumph-manipulator-krasnodar/` | ORCA-scoped case; overlaps naming with Factory `triumph-manipulator-landing` |
| **WPilot future agents** | Named in `projects/wpilot/README.md` (`wp-audit-agent`, etc.) | **Not** in `agents/registry.md` |
| **Integration Registry v0** | `integrations/integration-registry-v0.md` | Schema only; **no** populated integration rows observed |
| **Knowledge Center** | Baseline `06_KNOWLEDGE_CENTER.md` | Operator vault; not in git |

---

## D-004 — Classification conflicts

| Topic | Surface A | Surface B | Conflict |
|-------|-----------|-----------|----------|
| HomeGateway status | Registry table: `planned` | Registry narrative § boundaries: **OPERATIONAL** documentation | `status` column vs prose band |
| Website Factory maturity | Registry: `planned` | Maturity map / reality index: methodology **operational** | Program lifecycle vs operational methodology |
| GitGuard | Entity model: Program example | Reality index: conceptual name only; survivability maps tooling | Program vs design contract vs “not GitGuard product” |
| IdeaBox | Topology: operational discipline | Not in maturity map as row | Cross-cutting vs unmapped in program summary |
| Triumph | One `project_id` | Six workspace folders (`v2`–`v6` + base) | Execution case versioning vs single registry identity |
| seo-content-agent vs metabot | Both `project_id` rows | Legacy vs canonical external system | Duplicate product lineage (intentional legacy, drift risk) |

---

## D-005 — Duplicate entities (same responsibility, different names/locations)

| Cluster | Locations | Notes |
|---------|-----------|-------|
| SEO Content / MetaBOT | `projects/seo-content-agent/`, `projects/metabot-seo-content-agent/`, `mars-runtime/adapters/seo-content-agent-adapter.js`, `incoming/metabot/`, `incoming/mars-bridge/` | Canonical = metabot pack; legacy id retained |
| Triumph landing | `projects/triumph-manipulator-landing/`, `projects/mars-website-factory/reference-cases/`, `projects/orca/projects/triumph-manipulator-krasnodar/`, `workspaces/triumph-manipulator-landing*` (×6), `projects/orca/ppc/triumph-manipulator/` | Shared client theme; multiple authority surfaces |
| MIG workflow export | `projects/mig/workflows/n8n/`, `projects/mig/archive/pre-pilot-gruzotaxi-krasnodar-v1/mig-project/workflows/n8n/` | Archive copy of pilot spine |
| ORCA freeze archives | `projects/orca/freeze/`, `projects/orca/archive/stable-orca-after-triumph-battle-v1/` | Parallel stable snapshots |
| Registry checker / tool registry | `tools/registry.md`, `mars-runtime/runtime/tool-registry.js`, `governance/registry-architecture.md` | Different registry **kinds** (documented); mythology risk |
| Factory block registry | `projects/mars-website-factory/block-registry-v0.md`, `workspaces/website-factory-reference-v1/block-registry/` | Doc v0 vs reference workspace v1 tables |

---

## D-006 — Pilot / prototype / sandbox signals (sample)

| Path / pattern | Suggested class | Notes |
|----------------|-----------------|-------|
| `workspaces/_sandbox`, `_quarantine`, `_recovery`, `_tmp`, `_snapshots` | Experimental / ops hygiene | Not programs |
| `projects/orca/live-pilot/`, `live-pilots/`, `pilot-cases/` | Active operational pilots (ORCA) | Human-supervised |
| `projects/mig/archive/pre-pilot-gruzotaxi-krasnodar-v1/` | Historical | Pre-pilot archive |
| `projects/orca/content-packs/exporters/docx-pilot/` | Experimental | Docx export pilot |
| `projects/homegateway-v4-ai/tools/*mvp*`, `reports/mvp-v1-*` | Experimental / draft | MVP tooling in planned program pack |
| `incoming/*` | Experimental intake | Unreviewed until promoted |
| `archive/orca-lrl-foundation-v1/` | Historical | Archived foundation |
| `web-gpt-sources/` (numbered + chat-migration) | Historical import | Not live layout truth |

---

## D-007 — Orphaned / weak-link entities

| Entity | Issue |
|--------|-------|
| ISBD workspace | Implementation present; **no** registry, **no** Factory reference-case link in-repo |
| WPilot agent candidates | Documented roles; no agent cards |
| Website Factory agents (§4.1) | Cards exist for subset; most rows `planned`; no runtime |
| `mars-core` example row | Placeholder project_id |
| Lifecycle log | Last evt `0016` (2026-05-19); registry updates through 2026-06-02 **not** backfilled (`0017–0021` recommended in sync review) |
| `continuity/registry/master-index.md` | Empty sections — manual nav not populated |
| Integration registry | No concrete integration rows |
| HomeGateway | Large doc/WIP surface; registry `planned` vs heavy `OPERATIONAL-INDEX` activity in git status |

---

## D-008 — Relationship integrity (identified only)

| Relationship | Issue |
|--------------|-------|
| Registry → lifecycle | One-way freshness: registry ahead of lifecycle log |
| Factory → WPilot | Documented future bridge; no integration registry row |
| MIG → ORCA | Human-only handoff contract; no automation (correct) but easy to misread as pipeline |
| EAR Architecture (`shared/external-access-runtime/`) vs `ear-runtime` project | Frozen arch vs engineering project — docs stress split; drift risk on edits |
| MetaBOT execution | Live graphs external; `incoming/metabot/` JSON not proven synced to production |
| KC ↔ git | No auto-sync; canvas in git may lag operator KC |
| Triumph workspaces | No central version authority map in registry |

---

## D-009 — ISBD (dedicated)

| Field | Finding |
|-------|---------|
| **Name / id** | `isbd-care-landing` (workspace short id) |
| **Classification (observed)** | Website Factory **execution case** / client landing workspace — **not** registered as Program |
| **Ownership** | SAFE UNKNOWN — no owner field in registry; workspace README describes WP integration target |
| **Website Factory relationship** | Uses Gulp landing pattern (hero, sections, freeze archives); **no** `ISBD` string in `projects/mars-website-factory/` docs (grep 0) |
| **Registry status** | **Unregistered** |
| **Maturity status** | Active implementation in workspace (V2 polish per `PROJECT-STATUS.md`); excluded from baseline checkpoint workspaces WIP |
| **Topology** | Obsidian canvas node: SAFE UNKNOWN placeholder (`docs/visualization/obsidian-canvas/website-factory.canvas`) |
| **Inconsistency** | Substantial delivery artefact vs zero governance registration |

---

## D-010 — Archive candidates (identify only)

| Candidate | Rationale |
|-----------|-----------|
| `projects/seo-content-agent/` | Legacy; do-not-extend policy |
| `web-gpt-sources/chat-migration/` | Superseded by v1 operational state docs |
| `workspaces/triumph-manipulator-landing-v2`–`v4` (if v6 canonical) | Version sprawl; operator authority unclear |
| `projects/mig/archive/pre-pilot-gruzotaxi-krasnodar-v1/` | Pre-pilot complete |
| `projects/orca/archive/stable-orca-after-triumph-battle-v1/` | Stable snapshot duplicate of live tree areas |
| Duplicate ORCA ppc archive trees under `ppc/triumph-manipulator/archive/` | Freeze references |

---

*End of discoveries v1 — read-only census.*
