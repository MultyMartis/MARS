# Operational QA entry v1 (Wave 5)

**Status:** **single operational surface** — consolidates Wave 3–5 QA without a governance catalog.

**Replaces as default entry:** opening multiple QA docs separately. Underlying checklists remain valid; this file routes only.

**Production mode router (2026-06-17):** Read passport `production_mode` **before** any QA pass. **Undeclared mode** → **STOP**. Charter: [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md).

**Validation Architecture (2026-06-17):** Ordered layer chain VL0→VL6, signals, evidence bundles, false-green rules — [website-factory-validation-architecture-charter-v1.md](website-factory-validation-architecture-charter-v1.md). **Not a runtime** — human operator follows layer map before claiming VERIFIED or PRODUCTION PASS.

---

## Production Mode QA Router

**Not a runtime** — human operator selects branch from passport SoT.

| `production_mode` | QA branch | Primary gates | VERIFIED requires |
|-------------------|-----------|---------------|-------------------|
| `PIXEL_PERFECT` | **Pixel-perfect QA** | Source Discovery visual SSOT · Mapping QA · PF-* · render/text diff · Operator Visual side-by-side | Mode checklist + diff evidence — **not** build alone |
| `TEMPLATE_ART` | **Template-art QA** | Blueprint QA · content contract · semantic Design QA Matrix · block `block_id` provenance | Semantic + responsive + enforcement; PF-* **N/A** (waived with charter ref) |
| `UNDECLARED` / `UNKNOWN` / `CONFLICT` | **None** | — | **STOP** — declare mode first |

**Artifact lifecycle** (distinct from gate Layer A): **BUILT** → **VERIFIED** → **PRODUCTION PASS** — [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §1.1 · lifecycle boundaries VL4/VL5/VL6 — [website-factory-validation-architecture-charter-v1.md](website-factory-validation-architecture-charter-v1.md) §3, §6.

**REPORT header (when production QA):**

```text
Production mode: PIXEL_PERFECT | TEMPLATE_ART
Artifact lifecycle: BUILT | VERIFIED | (pending PRODUCTION PASS)
```

---

## When to use

| Situation | Start here → then |
|-----------|---------------------|
| Reference or client workspace after build | § **Compact pass** below |
| Foundation / lifecycle slice | § **Foundation Lite** |
| Adoption bootstrap | § **Adoption validation** |
| Visual slice / swap / migration | § **Visual regression** |
| REPORT shape | § **REPORT examples** |
| **Frontend Production Sign-off** | § **Production PASS authority** below |

---

## Production PASS authority

When closing a **full Frontend Production Sign-off** (page/slice Production PASS, not compact operational pass), use **[frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md)** for gate verdict vocabulary and **PRODUCTION VERDICT** rollup.

Compact pass (§ below) remains the default after build — it is **not** Production PASS authority.

---

## Compact pass (~15 min)

**Checklist body:** [reference-workspace-qa-flow-v1.md](reference-workspace-qa-flow-v1.md).

**Russian commercial landings (mandatory):** [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) — all preset widths + typography checks. Authority: [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md).

```text
npm run build → open dist → RU preset widths (if RU commercial) → modal → form → sticky (if any) → overflow/z-index spot → supplementary 375/768/desktop (reference flow)
```

REPORT lines:

```text
Verification: operational QA entry v1 → reference-workspace-qa-flow v1 — PASS | partial | SAFE UNKNOWN
```

For **Russian commercial landings**, also:

```text
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial (list) | FAIL | SAFE UNKNOWN (widths not tested)
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

*Wave 5 — one QA entry surface; RU typography stabilized 2026-05-24.*
