# MARS — Program registry summary (Sync Pack 2026-06)

**Status:** **CORE**  
**Authoritative table:** `registry/project-registry.md` — this file is a **Web-GPT distillate**; row changes happen only in the registry.

**Rule:** **Registry row ≠ deployed system.** Link `project_id`; do not duplicate full rows elsewhere as SoT.

---

## Registry role

| Field | Meaning |
|-------|---------|
| `project_id` | Stable introspection id |
| `status` | `planned` \| `active` \| `archived` |
| `phase` | Human-maintained lifecycle label |
| `related_entities` | Agent/card ids when registered |
| `last_updated` | ISO date of last review |

---

## Cross-cutting surfaces (not `project_id`)

| Surface | Role | Canonical entry |
|---------|------|-----------------|
| **GitGuard** | **REGISTERED** — Repository Survivability Layer | `projects/mars-survivability/registries/gitguard-system-entry-v1.md` |
| **IdeaBox** | Optional **Incubation Layer** — deferred ideas | `continuity/README.md` |
| **Incoming** | Ecosystem intake — hybrid Active Incoming (repo) + Historical Bulk (Storage after triage) | `incoming/README.md` |
| **Lifecycle Log** | Key Event History — governance milestones | `logs/lifecycle-log.md` |

**Lifecycle anchors (awareness pass):** `evt-2026-0022` (OPS registration), `evt-2026-0024` (ATLAS registration backfill).

---

## Factory execution cases (not `project_id`)

| Case | Workspace / path | Maturity note |
|------|------------------|---------------|
| **Triumph** | `workspaces/triumph-manipulator-landing/` | Reference case #1 — **canonical workspace v6** per `triumph-workspace-authority-map-v1.md` |
| **ISBD** | `workspaces/isbd-care-landing/` | Client delivery #2 — registered execution case |
| **BZPM** | `projects/website-factory/execution-cases/bzpm-catalog-redesign/` | Client delivery #3 — research phase complete |

**Registry:** `projects/mars-website-factory/execution-cases-registry-v1.md`

**Factory LOC-ZONE:** `workspaces/website-factory-operations/` — physical records plane (ROC-01 catalog). **Not** a `project_id`. FP-0001 enrolled; **FP-0002** (Shpigovsky.ru) visibility-only — ROC enrollment deferred.

---

## Active programs (sync snapshot)

| project_id | status | Posture | Canonical entry |
|------------|--------|---------|-----------------|
| `orca` | active | Human-supervised PPC toolkit; runtime **EXCLUDED** | `projects/orca/OPERATIONAL-INDEX.md` |
| `mars-website-factory` | planned | Strategic doc-first site methodology | `projects/mars-website-factory/OPERATIONAL-INDEX.md` |
| `metabot-seo-content-agent` | active | **Canonical** MetaBOT docs; execution **external** (n8n) | `projects/metabot-seo-content-agent/README.md` |
| `mig` | active | R1 groundtruth acquisition; v0.1 spine experimental | `projects/mig/OPERATIONAL-INDEX.md` |
| `ocpilot` | active | OpenCart/ocStore operational pack; bulk on storage layer | `projects/ocpilot/OPERATIONAL-INDEX.md` |
| `wpilot` | active | WordPress admin discipline; plugin source in-repo; prod bridge planned | `projects/wpilot/README.md` |
| `ear-runtime` | active | Engineering — R1 skeleton only; not live connector | `projects/ear-runtime/OPERATIONAL-INDEX.md` |
| `mars-survivability` | active | Survivability pack + GitGuard implementation locus | `projects/mars-survivability/OPERATIONAL-INDEX.md` |
| `homegateway-v4-ai` | planned | Personal Operational Cockpit — doc/draft | `projects/homegateway-v4-ai/OPERATIONAL-INDEX.md` |
| `atlas` | planned | Business Reality Registry — foundation + population docs; **not** runtime | `projects/atlas/OPERATIONAL-INDEX.md` |
| `ops` | planned | Business Operations Domain — WF-01/WF-02 pilots PARTIAL; **not** runtime | `projects/ops/OPERATIONAL-INDEX.md` |

---

## Planned / foundation / reference

| project_id | status | Note |
|------------|--------|------|
| `triumph-manipulator-landing` | planned | Factory reference + workspace lane — **not** Factory runtime |
| `nova` | planned | Mobile Application Factory foundation — implementation not started |
| `seo-content-agent` | planned | **Legacy** — do not extend; use `metabot-seo-content-agent` |
| `mars-core` | planned | Example row — placeholder |

---

## Cross-program relationships (intent, not APIs)

| Pair | Relationship |
|------|----------------|
| **MIG → ORCA** | MIG acquires reality; ORCA interprets — **human-only** handoff |
| **ORCA → Factory** | Optional strategy/semantic handoff when Factory lane selected |
| **Factory → WPilot** | Future WordPress bridge — documented boundary |
| **Factory ↔ ATLAS** | Factory consumers bind ORG/PRJ/WEB ids per `shared/contracts/atlas-context-binding-rule-v1.md` |
| **OPS → ATLAS** | OPS consumes business identity for reporting bindings — **does not** own ATLAS |
| **OCPilot ↔ WPilot** | CMS pilot **siblings** — not parent/child |
| **EAR Runtime → OCPilot** | Snapshots when chartered — consumers don't own acquisition |
| **MetaBOT** | External lane — MARS holds contracts only |
| **HomeGateway** | Surface layer — does not replace ORCA/WPilot/MetaBOT/governance |
| **GitGuard → mars-survivability** | Implementation under survivability pack — not separate `project_id` |

---

## Topology navigation (repo)

| Question | Surface |
|----------|---------|
| Entity placement | `governance/ecosystem-topology-index.md` |
| Bucket reality | `governance/mars-reality-index-v0.md` |
| Agent ids | `agents/registry.md` |
| Tool rows | `tools/registry.md` |
| Lifecycle events | `logs/lifecycle-log.md` (events ≠ implementation proof) |

---

*Reconcile against `registry/project-registry.md` after any registration change.*
