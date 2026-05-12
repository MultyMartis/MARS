# MARS Website Factory — Semantic Inheritance v0

**Status:** **documentation only** — **inheritance of meaning** across site structure. **Not** CSS inheritance, **not** OOP runtime, **not** automatic field synchronization between files or databases.

**Version:** v0.

**Related:** [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md), [semantic-object-model-v0.md](semantic-object-model-v0.md), [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md), [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md).

---

## 1. Inheritance chain (conceptual)

```text
site
  → cluster
    → page
      → section
        → component
```

Each level may **define**, **inherit**, or **explicitly override** semantic objects. **Inheritance ≠ runtime propagation**: nothing in this repository applies child updates to parents or peers automatically.

---

## 2. Inheritance scope

| Level | Typical inherited defaults |
|-------|---------------------------|
| **Site** | Global `trust_object` policy, brand CTA tone, legal disclaimers, default `seo_intent` guardrails, root `navigation_entity`. |
| **Cluster** | Topic ownership, shared `service_entity` framing, internal linking rules, shared `geo_object` when cluster is regional. |
| **Page** | Page-level `conversion_goal`, `cta_object` primaries, page-specific `seo_intent`. |
| **Section** | Section payload fields from blueprint template; may inherit **block-level** defaults from [block-registry-v0.md](block-registry-v0.md). |
| **Component** | Smallest scope; inherits from section **unless** design contract allows local variant (must still be **traceable** in lineage). |

---

## 3. Override rules

1. **Explicit wins** — A child scope that **states** a semantic field **replaces** the inherited default for that field only.
2. **Narrowing allowed, widening risky** — Geo **narrowing** (child within parent area) is common; **widening** child geo beyond parent without IA update is **invalid** pattern.
3. **No silent override** — Overrides must appear in **Blueprint / IA / REPORT** text, not only in unreviewed Frontend edits.

---

## 4. Conflict resolution

| Situation | Resolution order (documentation) |
|-----------|-----------------------------------|
| Blueprint vs Design meaning | **Blueprint** (or upstream Strategy) wins until blueprint is revised. |
| Blueprint vs Frontend | **Blueprint + approved Design** win; Frontend bugfix without semantic change is OK per [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md). |
| Page vs cluster `seo_intent` | **Cluster topic ownership** wins unless page has **declared exception** approved in SEO QA / PM. |
| Two sections same page | Section payloads are **independent** unless explicitly linked (e.g. shared `proof_entity` reference). |

---

## 5. Inheritance freeze

When a scope is **frozen**, inherited values from ancestors **become fixed for that child snapshot** — changing the parent after child freeze does **not** auto-update the child ([semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md)). **Reconciliation** is a **manual / HITL** episode: reopen child, merge intent, re-run QA.

---

## 6. Shared systems (cross-cutting)

- **Shared trust systems** — Site-level proof library, testimonial policy; pages **reference** entries, do not fork silently.
- **Shared CTA systems** — Global primary phone, global lead form policy; pages choose **role**, not duplicate conflicting destinations.
- **Shared SEO intent** — Cannibalization rules live at cluster; pages declare **primary** vs **supporting** relative to cluster.
- **GEO inheritance** — Parent service area caps child claims unless IA expands.
- **Authority inheritance** — **Who may change** shared objects follows [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md); child owners cannot weaken site compliance defaults.

---

## 7. Explicit boundary

- **Inheritance** describes **defaulting and override policy in docs and prompts**.
- **Propagation** ([semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md)) describes **what should be reviewed** after a change.
- Neither implies **background synchronization** across repos, CMS, or design tools.

---

## 8. SAFE UNKNOWN

- Multi-tenant / franchise **partial overrides** — org-specific addendum required.
- **Versioned** inheritance when Strategy doc v2 coexists with Blueprint v1 — resolve per [revision-semantics-v0.md](revision-semantics-v0.md); exact matrix **TBD** per project.

---

*End of Semantic Inheritance v0.*
