# Operational QA entry v1 (Wave 5)

**Status:** **single operational surface** — consolidates Wave 3–5 QA without a governance catalog.

**Replaces as default entry:** opening multiple QA docs separately. Underlying checklists remain valid; this file routes only.

---

## When to use

| Situation | Start here → then |
|-----------|---------------------|
| Reference or client workspace after build | § **Compact pass** below |
| Foundation / lifecycle slice | § **Foundation Lite** |
| Adoption bootstrap | § **Adoption validation** |
| Visual slice / swap / migration | § **Visual regression** |
| REPORT shape | § **REPORT examples** |

---

## Compact pass (~15 min)

**Source:** [reference-workspace-qa-flow-v1.md](reference-workspace-qa-flow-v1.md) (unchanged checklist).

```text
npm run build → open dist → 375 / 768 / desktop → modal → form → sticky (if any) → overflow/z-index spot
```

REPORT line:

```text
Verification: operational QA entry v1 → reference-workspace-qa-flow v1 — PASS | partial | SAFE UNKNOWN
```

---

## Foundation Lite

**When:** touching `foundations/`, `js/core/`, or `data-module`.

**Source:** [agents/mars-forge/foundation-lite-checklist.md](../../agents/mars-forge/foundation-lite-checklist.md)

Skip if copy-only with no hooks.

---

## Adoption validation

**When:** new client workspace, post-migration, or first freeze candidate.

**Source:** [adoption-validation-flow-v1.md](adoption-validation-flow-v1.md)

---

## Visual regression

**When:** section replacement, token/visual change, migration checkpoint.

**Source:** [visual-regression-workflow-v1.md](visual-regression-workflow-v1.md)

**Not:** automated diff tooling.

---

## Production hardening

**When:** before freeze or after modal/sticky/form work.

**Source:** [production-hardening-rules-v1.md](production-hardening-rules-v1.md)

---

## REPORT examples

**Source:** [operational-examples/golden-report-examples-v1.md](operational-examples/golden-report-examples-v1.md)

Lite / Standard / extraction / swap formats.

---

## Do not default-read

- Full [agents/mars-forge/qa-checklist.md](../../agents/mars-forge/qa-checklist.md) — Extended only  
- [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md) — blueprinting tasks only  
- Governance drift taxonomies — Tier 3

*Wave 5 — one QA entry surface.*
