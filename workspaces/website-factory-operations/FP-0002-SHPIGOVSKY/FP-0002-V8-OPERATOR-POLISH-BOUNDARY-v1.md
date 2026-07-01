# FP-0002 V8 — Operator Polish Boundary v1

**Date:** 2026-07-01

---

## Current approved baseline

| Field | Value |
|-------|-------|
| Name | FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01 |
| Commit | `eb47ebb4066252373e02d9e1095403d0ce6b6b22` |
| Tag | `fp-0002-v8-operator-approved-frontend-stable-01` |
| Nature | Architecture and implementation baseline — **not** immutable final production site |

---

## Future manual polish is expected

The operator may later:

- Adjust spacing and typography manually  
- Correct minor content details  
- Refine images and captions  
- Collect small follow-up tasks for MARS  
- Add animation and interaction polish  

This is a **legitimate phase** — not uncontrolled drift.

---

## Authority after operator edits

| Rule | Detail |
|------|--------|
| Operator source edits | Become **canonical** for affected files |
| MARS responsibility | Inspect and **preserve** manual edits |
| Regeneration | MARS must **not** overwrite manually polished files without explicit authority |
| Documentation updates | Required only when polish changes **reusable architecture** — not every pixel tweak |

---

## Checkpoint discipline

| Step | Requirement |
|------|-------------|
| Before polish | Snapshot + record HEAD |
| After polish | Diff audit + clean build + operator review |
| Git | Selective checkpoint — not default for tiny tweaks unless operator requests |

---

## MARS follow-up tasks

After operator review, small tasks may be collected (e.g. fix broken link, add missing alt). Each task:

1. References specific file/block  
2. Does not broad-refactor unrelated areas  
3. Respects priority visual protocol for visual changes  

---

## Recommended workflow

```text
inspect approved baseline
  → snapshot (Storage + optional git tag)
  → operator manual polish in source
  → diff audit (human + optional script)
  → targeted MARS tasks for non-manual fixes
  → npm run build (clean)
  → visual review
  → stable checkpoint (if operator authorizes)
  → update docs only if architecture/rules changed
```

---

## Boundaries

| In scope for operator | Out of scope without charter |
|-----------------------|------------------------------|
| CSS value tweaks in `style.scss` | New page families |
| Copy in HTML partials | Component consolidation rewrites |
| Image swaps in `src/img/` | WordPress integration |
| Link fixes | Excel demo assembly (07C) |

---

## Relation to Phase 07C

Static client demo assembly (07C) uses approved baseline as **input**. Operator polish may occur **before or after** 07C — if before, 07C must rebuild from polished source.

---

*Operator polish boundary — FP-0002 V8.*
