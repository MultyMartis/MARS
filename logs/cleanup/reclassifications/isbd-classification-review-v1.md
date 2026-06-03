# ISBD Classification Review v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 1  
**Mode:** Read-only audit + reclassification recommendation (**not executed**)  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb` / `mars-v2-stable-baseline-2026-06`)  
**Upstream evidence:** [MARS-ECOSYSTEM-INTEGRITY-CENSUS-v1.md](../MARS-ECOSYSTEM-INTEGRITY-CENSUS-v1.md) D-009; census discoveries A-007, A-008, A-027

---

## Finding summary

| Field | Determination |
|-------|---------------|
| **Short id** | `isbd-care-landing` |
| **Actual classification** | **Website Factory execution case** + **client delivery workspace** |
| **Is NOT** | Program · System · Initiative · MARS `project_id` (today) |
| **Registry status today** | **Unregistered** |
| **Recommended band** | Execution locus under Factory production lane; optional cross-link to WPilot (WordPress integration target) |

---

## Audit surfaces

### 1. Registry (`registry/project-registry.md`)

| Check | Evidence | Result |
|-------|----------|--------|
| `project_id` row | Grep: no `isbd` / `ISBD` in registry | **Absent** |
| Intended registration model | Registry schema: `project_id` for programs only; IdeaBox explicitly excluded as cross-cutting | ISBD fits **execution locus**, not default program row |

### 2. Project references (`projects/`)

| Check | Evidence | Result |
|-------|----------|--------|
| Dedicated project pack | No `projects/isbd*` path | **None** |
| Website Factory docs | Grep `ISBD` under `projects/mars-website-factory/`: **0 matches** | No Factory reference-case or handoff doc |
| Triumph / ORCA / WPilot packs | No ISBD cross-refs found in grep pass | **Isolated** delivery workspace |

### 3. Execution case references (Factory vocabulary)

| Surface | Evidence | Result |
|---------|----------|--------|
| Reference Execution Case #1 | Triumph only — `projects/mars-website-factory/reference-cases/triumph-manipulator-landing/` | ISBD is **parallel pattern**, not documented case |
| Workflow map | `projects/mars-website-factory/workflow-map.md` — Triumph as reference execution case | Same Gulp landing lane; ISBD **undeclared sibling** |
| Master build map | C16 changelog cites Triumph reference case only | No ISBD milestone |

**Ecosystem vocabulary used (existing, not invented):**

- **Execution case** — Website Factory term (`reference execution case`, operational runbook chain)
- **Client delivery workspace** — census bucket C: execution loci under `workspaces/`
- **Unregistered entity** — census D-003

### 4. Website Factory references

| Surface | Evidence | Result |
|---------|----------|--------|
| Obsidian canvas | `docs/visualization/obsidian-canvas/website-factory.canvas` node `n-wf-isbd-note`: *"SAFE UNKNOWN — no ISBD execution case found in repo at export time"* | **Contradicts** live workspace |
| Canvas generator | `docs/visualization/obsidian-canvas/_generate_pack.py` — same placeholder text | Export-time gap, not absence of workspace |
| Factory OPERATIONAL-INDEX | No ISBD entry (grep) | **Gap** |

### 5. Workspace references (`workspaces/isbd-care-landing/`)

| Evidence file | Key facts |
|---------------|-----------|
| `README.md` | Promo landing *"Продукт для банков: интеллектуальная система заботы"*; short id `isbd-care-landing`; WP/The7/WPBakery integration target; no redesign/copy changes |
| `PROJECT-STATUS.md` | Semantic freeze complete; Gulp build verified; six content sections; content frozen (`docs/content-lock-v1.md`); V2 polish phase; stable checkpoints under `archive/` |
| Nested git | `workspaces/isbd-care-landing/.git` exists (**True** on 2026-06-03 shell check) | Monorepo boundary risk |
| Implementation pattern | Gulp, sections, freeze archives, host CSS preview — same lane as Triumph / Factory reference workspace | **Factory execution case posture** |

---

## Classification matrix (requested dimensions)

| Label | Applies? | Rationale |
|-------|----------|-----------|
| **Program** | **No** | No `project_id`; not a strategic MARS program pack |
| **System** | **No** | Static Gulp landing; no runtime, agent, or orchestration claims |
| **Initiative** | **No** | No governance initiative doc; bounded client landing delivery |
| **Execution Case** | **Yes** | Website Factory production-lane artifact chain (intake → build → freeze → WP handoff pending) |
| **Client Delivery Project** | **Yes** | Named client product landing with frozen content and WP insertion target |
| **Website Factory Output** | **Partial** | Output of Factory **methodology** (Gulp landing pattern); not registered as Factory reference case |

---

## Inconsistencies

1. **Canvas vs filesystem** — placeholder SAFE UNKNOWN while workspace is substantial and active.
2. **Registry silence** — largest unregistered delivery gap in census (D-003, D-009).
3. **Factory doc silence** — zero `ISBD` string in Factory pack despite parallel Triumph pattern.
4. **Nested `.git`** — survivability / backup scope ambiguity inside MARS monorepo.
5. **Baseline scope** — workspaces WIP excluded from stable baseline checkpoint; governance still should classify.

---

## Proposed reclassification (recommendation only)

| Action | Target | Resulting state (if approved in Wave 2+) |
|--------|--------|---------------------------------------------|
| **RECLASSIFY** | Topology + Visual Brain | Document ISBD as **Website Factory execution case #2 (client delivery)** linked from Factory OPERATIONAL-INDEX or a new `reference-cases/isbd-care-landing/` overview stub |
| **REGISTER** (operator choice) | **Option A — preferred:** execution-case registry row in Factory pack (not new `project_id`) | Traceable case id `isbd-care-landing`; canvas node updated |
| **REGISTER** (operator choice) | **Option B:** minimal `project_id` row | Only if operator treats ISBD as long-lived program — **not recommended** by this review (inflates registry) |
| **RECLASSIFY** | WPilot cross-link | Note WP insertion QA as **WPilot lane** follow-on (`README.md` already states WordPress target) |
| **INVESTIGATE** | Nested `.git` | Operator decides: absorb into monorepo or document external clone policy |

**Do not invent categories.** Use: execution case, client delivery workspace, execution locus, unregistered entity.

---

## Resulting state (today — Wave 1)

- **Classification documented** in this file.
- **No registry edit**, **no canvas edit**, **no filesystem change**.
- ISBD remains **de facto** Factory-pattern client delivery workspace with **zero governance registration**.

---

## SAFE UNKNOWN

| Topic | What would verify |
|-------|-------------------|
| Client / operator owner | External operator assignment |
| Production URL / WP live insertion | Hosting / WPilot deployment evidence |
| Relationship to MetaBOT / ORCA | None in-repo; assume **none** unless operator states |

---

*ISBD classification review v1 — Wave 1 evidence only.*
