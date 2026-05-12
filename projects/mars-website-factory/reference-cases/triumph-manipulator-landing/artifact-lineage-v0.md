# Artifact lineage — Triumph Manipulator Landing (v0)

**Semantics SoT:** [artifact-lineage-semantics-v0.md](../../artifact-lineage-semantics-v0.md) (documentation vocabulary — **not** a running lineage service).

---

## 1. Forward chain (happy path)

```text
business-intake-v0.md
  → site-classification-v0.md
  → marketing-strategy-v0.md
  → seo-strategy-v0.md
  → information-architecture-v0.md
  → page-blueprint-v0.md
  → blueprint-qa-v0.md
  → design-handoff-v0.md
  → design-direction-v0.md
  → frontend-handoff-v0.md
  → frontend-production-plan-v0.md
  → frontend-qa-v0.md
  → validation-summary-v0.md
  → delivery-readiness-v0.md
  → hitl-review-summary-v0.md
  → reference-run-report-v0.md
```

---

## 2. Authority / supersede (v0 doc convention)

- **Upstream wins** until explicit revision: e.g. **IA** change supersedes **blueprint** row semantics for affected `section_order`.
- **QA artifacts** do not overwrite blueprint; they **reference** revision labels in prose (**no** formal revision ID in-repo).

---

## 3. Freeze propagation (example)

1. **Assume** blueprint batch **G3-frozen** (hypothetical).
2. **Design handoff** consumes frozen blueprint revision.
3. **Change:** `hero` **CTA_object** label change.
4. **Propagation:** Blueprint revision → design handoff **stale** → frontend handoff **stale** → delivery candidate **invalid** per [dependency-invalidation-v0.md](../../dependency-invalidation-v0.md) patterns.

---

## 4. Invalidation examples (specific)

| Trigger | Stale artifacts |
|---------|-----------------|
| Service area shrink | `geo_trust`, SEO meta, optional `LocalBusiness` snippet, **frontend** geo partial |
| Remove **cases** photo | `cases`, design crop specs, frontend lazy-load alt |
| Add **pricing** | `pricing` optional block, **faq**, **lead_form** microcopy, legal QA |

---

## 5. Orphan risk

- **design-direction-v0** without comps — not orphan of **process**, but **downstream** consumer should treat as **preliminary**.

---

*Artifact lineage v0 — reference execution only*
