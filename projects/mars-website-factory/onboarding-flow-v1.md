# Onboarding flow v1 (Wave 4)

**Status:** **documented** — **one path** for new operator, new workspace, new frontend task.  
**Supersedes for depth:** [frontend-operator-quickstart-v1.md](frontend-operator-quickstart-v1.md) remains valid; this file is the **ordered** Wave 4 path.

---

## Path A — New operator (first session)

| # | Read / do | Time |
|---|-----------|------|
| 1 | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) — Frontend & Forge row only | 2 min |
| 2 | This file — Path B steps 1–4 | 5 min |
| 3 | [foundation-adoption-charter-v1.md](foundation-adoption-charter-v1.md) — skim workflow | 5 min |
| 4 | [workspaces/website-factory-reference-v1/](../../workspaces/website-factory-reference-v1/) — `npm run build`, open `dist/index.html` | 10 min |
| 5 | [operational-examples/golden-report-examples-v1.md](operational-examples/golden-report-examples-v1.md) — Lite example | 5 min |
| 6 | [reference-workspace-qa-flow-v1.md](reference-workspace-qa-flow-v1.md) — one pass | 15 min |

**Do not read:** full governance catalog, Forge README checklist table.

---

## Path B — New client workspace

| # | Action | Doc |
|---|--------|-----|
| 1 | Charter: slug, path, `site_type_id`, block list | handoff |
| 1b | **Or** copy [workspaces/_template-client-v1/](../../workspaces/_template-client-v1/) wholesale, rename slug | template README |
| 2 | Copy `scss/foundations/` + `js/core/` from reference (if not using template) | [foundation-adoption-charter-v1.md](foundation-adoption-charter-v1.md) |
| 3 | Edit `_tokens.scss` brand only | [foundation-adoption-rules-v1.md](foundation-adoption-rules-v1.md) |
| 4 | Copy layout partials pattern (header/footer/modal) | reference `partials/layout/` |
| 4b | **Greenfield:** Production Standards Draft → DESIGN → FRONTEND MAPPING QA → Production Standards Approval → Shell → Visual Foundation → Design Calibration → Foundation QA **before** first commercial page | [production-standards-governance-v1.md](production-standards-governance-v1.md) · [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) · [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) · [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) · [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) · [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) |
| 4c | **Page closure:** after Home/inner page production — Design Completeness → Frontend Design QA Matrix → Pixel Fidelity → Production PASS | [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.2–§6 |
| 5 | Add first section: `hero` partial + scss | [golden-implementation-slice-v1.md](golden-implementation-slice-v1.md) |
| 6 | `npm run build` | REPORT evidence |
| 7 | QA + adoption validation | [operational-qa-entry-v1.md](operational-qa-entry-v1.md) → [adoption-validation-flow-v1.md](adoption-validation-flow-v1.md) |
| 8 | `# REPORT — <client> workspace bootstrap` | [reporting-standard-v0.md](reporting-standard-v0.md) |

---

## Path C — New frontend task (section slice)

| # | Action |
|---|--------|
| 1 | Confirm workspace path + `block_id` + Forge mode (Lite/Standard) |
| 2 | Read handoff + active design version only |
| 3 | Implement `src/partials/sections/` + `scss/sections/` |
| 4 | Build + compact QA |
| 5 | REPORT + freeze if Standard+ PASS |

**Replacement task:** add [section-swap-demo-flow-v1.md](section-swap-demo-flow-v1.md) before freeze.

**Extract to library:** [implementation-extraction-discipline-v1.md](implementation-extraction-discipline-v1.md).

---

## Minimal read order (all paths)

```text
OPERATIONAL-INDEX → onboarding-flow-v1 (this) → adoption charter → reference README → golden REPORT example
```

---

## First build flow

```powershell
cd workspaces/<your-workspace>
npm install
npm run build
# open dist/<page>.html
```

---

## First REPORT flow

Use [operational-examples/golden-report-examples-v1.md](operational-examples/golden-report-examples-v1.md) §1 (Lite) as template.

---

## First replacement flow

1. Read [section-replacement-contract-v1.md](section-replacement-contract-v1.md) §5 lifecycle.
2. Run [section-swap-demo-flow-v1.md](section-swap-demo-flow-v1.md) Demo A on reference.
3. REPORT §3 example format.

---

## Block library (reference)

**Canonical table:** [curated-library-index-v1.md](curated-library-index-v1.md) · **Tiers:** [block-quality-tiers-v1.md](block-quality-tiers-v1.md).

| block_id | Wave | Notes |
|----------|------|-------|
| hero, lead_form, cta_band | 3 | golden slice |
| social_proof, sticky_cta, contact_block | 4 | `social_proof` still experimental |
| faq | 5 | Triumph V2 extract |
| pricing, cases | 6 | Triumph V2 extracts |

*Wave 6 — onboarding points to curated library.*
