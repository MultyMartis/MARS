# HomeGateway Classification Review v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 1  
**Mode:** Read-only audit + classification recommendation (**not executed**)  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb`)  
**project_id:** `homegateway-v4-ai`

---

## Finding summary

| Dimension | Evidence-based determination |
|-----------|------------------------------|
| **Registry `status` column** | `planned` |
| **Registry narrative band** | **OPERATIONAL documentation** (doc-pack discipline — **not** deployed product) |
| **OPERATIONAL-INDEX** | **DRAFT · PLANNING · Phase 2 active** (Phase 1 foundation complete) |
| **Maturity map** | `planned / draft` — surface layer doc pack |
| **Workspace reality** | **UI prototype MVP v1** exists at `workspaces/homegateway-v4-ai/v1/` (Gulp static skeleton, 2026-05-25 init report) |
| **Recommended classification** | **Planned Program (documentation-first) + UI Prototype workspace** — **do not inflate** to operational product or MVP product |

---

## Audit surfaces

### 1. Registry (`registry/project-registry.md`)

| Field | Value |
|-------|-------|
| `project_id` | `homegateway-v4-ai` |
| `status` | `planned` |
| `phase` | **PLANNED / DRAFT** — documentation-first Personal Operational Cockpit; STATIC-FIRST target |
| `last_updated` | 2026-06-02 |
| Boundaries § | **OPERATIONAL documentation** — explicitly **not** deployed runtime, **not** control plane |

**Conflict (census D-004):** Table column `planned` vs boundary prose **OPERATIONAL** — prose means *operational documentation discipline*, not product maturity.

### 2. Maturity (`web-gpt-sources/mars-v2-stable-baseline-2026-06/08_SYSTEM_MATURITY_MAP.md`)

| Label | Notes |
|-------|-------|
| **HomeGateway** | `planned / draft` — surface layer doc pack |

Aligned with honest posture — no shipped runtime.

### 3. OPERATIONAL-INDEX (`projects/homegateway-v4-ai/OPERATIONAL-INDEX.md`)

| Signal | Evidence |
|--------|----------|
| Header status | **DRAFT · PLANNING · Phase 2 active** |
| Phase 1 | Exit criteria met ✓ (2026-05-20) |
| Phase 2 | Wireframe pack complete; **HTML files not started** (header note) — **superseded partially** by workspace MVP |
| Phase 4 static MVP | Documented as future gate |
| Workspace pointer | SAFE UNKNOWN table: `workspaces/homegateway-v4-ai/v1/` — MVP v1 skeleton **active** |
| Lane B activity | Large visual/spatial doc pack (2026-05-24+) — documentation expansion, not runtime |

### 4. Documentation pack (`projects/homegateway-v4-ai/README.md`)

| Claim | Evidence |
|-------|----------|
| Documentation-first | ✓ |
| STATIC-FIRST v0.1 | Mock login, cockpit layout — **planned** |
| Not runtime / not control plane | Repeated boundary blocks |
| Block-screen architecture | Concept + wireframes — doc stage |

### 5. Workspace (`workspaces/homegateway-v4-ai/`)

| Evidence | Finding |
|----------|---------|
| `projects/homegateway-v4-ai/reports/mvp-v1-initialization-report.md` | MVP v1 Gulp workspace initialized 2026-05-25; v0 prototype archived to `archive/v0/` |
| Build | `npm run build` verified at init |
| Scope | Static HTML/CSS/JS skeleton; `#main_area` empty tactical canvas |
| Tools | `projects/homegateway-v4-ai/tools/bootstrap-mvp-v1.ps1`, patch/verify scripts — **experimental draft** tooling |
| Backend / integrations | **Excluded** per README and roadmap |

**Maturity of workspace:** **UI Prototype / static frontend MVP skeleton** — not production cockpit, not deployed app.

---

## Classification options evaluated

| Example label | Fit? | Verdict |
|---------------|------|---------|
| **Concept** | Partial | Strong concept doc pack; but workspace exceeds pure concept |
| **Prototype** | Yes | Wireframe docs + v0 archived; v1 workspace skeleton |
| **UI Prototype** | **Best fit for workspace** | Gulp static shell without backend |
| **Planned Program** | **Best fit for `project_id`** | Registered planned program with phased roadmap |
| **MVP** | **Misleading if product sense** | "MVP v1" is internal workspace label — **not** shippable MVP product |
| **Operational (product)** | **No** | No runtime, no live integrations |
| **Active Program** | **No** | Registry `planned`; implementation gated |

---

## Inconsistencies (do not resolve in Wave 1)

1. **`planned` vs OPERATIONAL prose** — semantic overload of "OPERATIONAL" (documentation band vs product state).
2. **OPERATIONAL-INDEX "HTML not started"** vs MVP v1 workspace exists — index partially stale on workspace row.
3. **Git status WIP** — large uncommitted doc surface vs baseline — activity ≠ maturity inflation.
4. **Registry phase** does not mention UI prototype workspace — relationship implicit only in reports.

---

## Recommended classification

| Layer | Recommended label | Rationale |
|-------|-------------------|-----------|
| **Registry row** | **KEEP** `status: planned` | Correct lifecycle band |
| **Phase narrative** | **RECLASSIFY** prose to **PLANNED / DRAFT · OPERATIONAL DOC PACK** | Disambiguate from product "operational" |
| **Maturity map** | **KEEP** `planned / draft` | Honest |
| **Workspace** | **UI Prototype (static MVP skeleton)** | Evidence: init report + v1 tree |
| **Overall program state** | **Documentation-first planned program with experimental static UI prototype** | No runtime claims |

**Do not execute changes** — document-only recommendation.

---

## Proposed reclassification actions (Wave 2+ operator approval)

| ID | Action | Target |
|----|--------|--------|
| HG-R1 | **RECLASSIFY** | Registry boundaries § — clarify "OPERATIONAL documentation" ≠ `status: active` |
| HG-R2 | **RECLASSIFY** | OPERATIONAL-INDEX header — add workspace row: MVP v1 UI prototype active |
| HG-R3 | **KEEP** | `project_id` row; no promotion to `active` until phase evidence charter |
| HG-R4 | **INVESTIGATE** | Align roadmap Phase 4 gate vs existing v1 workspace scope |

---

## Resulting state (Wave 1)

- No edits to registry, OPERATIONAL-INDEX, or workspace.
- Classification recorded here for Wave 2 operator decisions.

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Deployment target / hosting | Not in-repo |
| Whether v1 workspace is operator canonical vs throwaway bootstrap | Operator preference |
| Lifecycle log entry for 2026-06-02 registry touch | **Missing** (see lifecycle-log review) |

---

*HomeGateway classification review v1 — Wave 1 evidence only.*
