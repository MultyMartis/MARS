# MARS Website Factory — QA and validation model

## Principles

1. **Validator Agent** is the **cross-cutting** MARS role for task-contract alignment, policy, and structural guardrails (`agents/registry.md`, `workflows/execution-flow.md` **validate** stage).
2. **Specialist QA agents** (frontend, design, SEO, conversion) provide **depth**; they do **not** replace security or human **HITL** where required.
3. **No** claim that automated QA **runs** in MARS today — **documentation-only** targets.

## QA lanes

| Lane | Focus | Primary owner (planned) |
|------|--------|-------------------------|
| **Structural / policy** | Task fit, secrets, forbidden paths, link integrity | **Validator Agent** |
| **Frontend** | Build, HTML semantics, responsive breakpoints, SCSS hygiene, JS scope | **Frontend QA Agent** |
| **Design** | Fidelity to approved spec, token compliance | **Design QA Agent** |
| **SEO** | Titles, meta, headings, internal links, thin content | **SEO QA Agent** |
| **Conversion** | CTA clarity, form UX, trust signals | **Conversion QA Agent** |

## Gates and outcomes

| Outcome | Meaning |
|---------|---------|
| **PASS** | Proceed to next stage or delivery. |
| **FAIL — fix** | Rework in current stage; may emit **STRUCTURE CHANGE** if blueprint wrong. |
| **NEED HUMAN APPROVAL** | Legal, brand, or high-risk commercial content. |
| **SAFE UNKNOWN** | Evidence missing — do not ship definitive claims (SEO facts, benchmarks). |

## Relation to evaluation layer

`evaluation/README.md` and `evaluation/evals-v0.md` describe **evals** and release gates at MARS level — **planned** integration; Website Factory should **reference** release-gate vocabulary rather than invent a parallel system.

## SAFE UNKNOWN

- Automated visual regression, Lighthouse CI, or a11y engines — **not** specified as in-repo for Factory v0.
- Whether **Validator** is one LLM call or a checklist tool — **implementation TBD**.
