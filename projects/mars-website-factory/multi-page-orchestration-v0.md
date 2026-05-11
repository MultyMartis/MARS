# MARS Website Factory — Multi-Page Orchestration v0

**Status:** **documentation only** — **site-level production semantics** for multi-page static websites: structure, dependencies, QA scope, and invalidation **at the graph level**.  
**Not claimed:** crawlers, schedulers, link checkers running autonomously, or a hidden graph database maintained by MARS.

**Version:** v0.

**Related:** [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [seo-intent-model-v0.md](seo-intent-model-v0.md), [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md), [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md).

---

## 1. Multi-page website semantics

A **multi-page website** is a **set of pages** with **shared systems** (navigation, trust, CTAs, design system, frontend shell) and **cross-links**. Factory orchestration **documentation** treats the site as:

- A **graph** of pages (nodes) and **dependencies** (edges): parent/child, hub/spoke, service clusters.
- A **bundle** of blueprints + shared artifacts that **must change coherently** when upstream strategy or IA shifts.

**No** claim that an engine maintains this graph in real time — **human + runbook + signals** per [orchestration-signals-v0.md](orchestration-signals-v0.md).

---

## 2. Parent / child pages

**Parent** pages anchor **topic** or **service** families; **child** pages drill into variants (locations, SKUs, long-tail intents). **Semantics:**

- Child blueprints **inherit** objective class and **must** declare deviation rationale.
- URL depth and **breadcrumb** expectations flow from IA artifacts.

**Invalidation:** changing a parent’s **objective** or **CTA policy** may force child blueprint and frontend QA **re-run** for the subtree (**cluster invalidation**).

---

## 3. GEO trees

**GEO trees** group pages by **market / location** dimensions. **Risks:** duplicate local copy, conflicting NAP (name/address/phone) facts, **cannibalization** across locales.

**QA:** page-level uniqueness checks + **site-level** consistency of entity facts (**HITL** for legal accuracy).

---

## 4. SEO landing trees

**SEO landing trees** are hub pages supporting **intent clusters** (commercial investigation vs transactional). **Internal linking** must reflect the **declared** primary query per page (see §9).

**Invalidation:** hub strategy change **invalidates** spoke blueprints and internal link QA for the cluster.

---

## 5. Service clusters

**Service clusters** are sets of pages describing related offerings with **shared proof** (case studies), **shared pricing disclaimers**, and **shared CTAs**. Editing one page’s **trust block** may require **cluster-wide** QA for compliance consistency.

---

## 6. Reusable blocks

[Block registry](block-registry-v0.md) blocks may be **reused** across pages. **Shared section invalidation:** updating a **global** block definition invalidates every page instance unless the project uses **versioned** block snapshots (**SAFE UNKNOWN** whether versioning is tooling-enforced).

---

## 7. Shared trust systems

**Trust** semantics per [trust-semantics-v0.md](trust-semantics-v0.md) often appear on **many** pages (logos, certifications, reviews). A change to **trust sources** is **site-level** for QA impact even when triggered from one blueprint.

---

## 8. Shared CTA systems

[cta-semantics-v0.md](cta-semantics-v0.md) defines **primary / secondary** CTA discipline. **Site-level** CTA changes (phone number, form endpoint, promo) **invalidate** conversion QA for **all** pages using that CTA id.

---

## 9. Navigation dependencies

Navigation is a **first-class dependency graph**: menus, footers, mobile drawers reference **page ids**. **IA** is SoT for nav structure; **frontend** implements routes.

**Blocking:** shipping with **broken internal routes** or **orphan** pages flagged in IA is a **matrix blocking** issue unless explicitly waived with scope (“launch without section X”).

---

## 10. Internal linking semantics

Internal links carry **intent flow**: hub → spoke, related articles, service cross-sells. **Rules (v0):**

- Each link has a **purpose** (supporting evidence, conversion assist, legal cross-ref) documented at blueprint or content QA layer.
- **No** “link stuffing” without IA approval — escalation signal if detected in QA.

---

## 11. Cannibalization risks

**Cannibalization** = multiple pages competing for the **same** primary intent without clear **page role hierarchy** (see §12). **Detection** is **QA + human** judgment aided by strategy/SEO artifacts — **not** guaranteed by tooling in v0.

---

## 12. Page-role hierarchy

Assign each in-scope page a **role** (e.g. `home`, `pillar`, `landing`, `support`, `legal`, `local_landing`). **Hierarchy** constrains **objective** and **internal link** expectations:

- **Pillar** supports multiple **child** landings.
- **Legal** pages **must not** be used as **commercial** SEO landings without explicit risk acceptance.

---

## 13. Page lineage

**Page lineage** tracks blueprint → design → frontend → QA artifacts **per `page_id`**. **Supersede** of a blueprint version creates a **new lineage segment**; do not overwrite history in runbooks.

---

## 14. Page-level vs site-level QA

| Scope | Examples |
|--------|----------|
| **Page-level** | Blueprint checklist per page; visual QA per template; on-page accessibility. |
| **Site-level** | Nav graph integrity; global CTA/trust; duplicate title risk across cluster; robots/sitemap consistency (**SAFE UNKNOWN** hosting). |

**Both** may **block** delivery when production `project_type` applies.

---

## 15. Cluster invalidation

When a **cluster root** (GEO root, SEO hub, service parent) changes:

1. Identify **member pages** in the cluster (explicit list in IA/strategy artifacts — **no hidden state**).
2. Mark downstream blueprint/design/frontend/QA as **stale** for that member set.
3. Re-run **QA matrix** rows for **IA**, **Blueprint**, **Frontend**, **Delivery** as scope dictates.

**Automation:** **SAFE UNKNOWN** — any future link graph or CI must be evidenced per `AGENTS.md`; until then, **human-executed** checklists.

---

## 16. SAFE UNKNOWN (automation)

| Topic | Boundary |
|--------|----------|
| **Automated link graph** | May exist in some stacks — **not** claimed in-repo for Website Factory. |
| **Continuous orchestration** | **No** daemon reconciling page graph vs live site in MARS v0 documentation. |
| **Sitemap generators** | External tooling possible — treat outputs as **artifacts** subject to QA. |

---

## 17. Changelog

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-12 | Initial **Multi-Page Orchestration v0** — graph semantics, QA scopes, cluster invalidation, SAFE UNKNOWN automation. |
