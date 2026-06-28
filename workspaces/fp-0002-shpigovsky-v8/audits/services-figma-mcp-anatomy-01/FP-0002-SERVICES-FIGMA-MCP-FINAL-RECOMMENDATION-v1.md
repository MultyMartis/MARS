# FP-0002 — Services Figma MCP Final Recommendation v1

**Date:** 2026-06-26  
**Authority:** `641295e1` · read-only audit complete

## Strategy gate

```text
HYBRID_RECONSTRUCTION
```

### Rationale

| Criterion | Evidence |
| --------- | -------- |
| Hero DOM conceptually wrong for target | CTA/breadcrumb/tab zone not in V1 |
| Breadcrumbs/submenu absent | `MISSING_COMPONENT` |
| Program layout differs | 2×2 grid vs home vertical |
| Category hubs partially close | Reuse data/hrefs; rebuild layout variants |
| Lower sections reliable | Founder, FAQ, form, footer |

`REPAIR_V1` rejected — would patch missing components onto wrong hero architecture.  
`BUILD_SERVICES_V2` full greenfield rejected — lower sections proven reusable.

## Website Factory lesson — NEW PAGE IMPLEMENTATION GATE

**Mandatory sequence:**

```text
1. PAGE ANATOMY AUDIT
2. COMPONENT BOUNDARY MAP
3. DESKTOP/MOBILE NODE MAPPING
4. DESIGN-TO-CONTENT/ASSET MAP
5. REUSE DECISION
6. IMPLEMENTATION
7. VISUAL DIFFERENTIAL QA
```

**Rule:** *Visual similarity does not prove component equivalence.*

### Previous process failure

Services V1 path: existing partials → reuse assumption → assembly → PNG chase.  
Correct path: **live target frame → anatomy → boundaries → reuse decision → build.**

### Governance

Recommendation documented here only. Central Website Factory governance **not updated** in this task.

## MCP status caveat

Live Figma MCP read on cloud file **blocked** (no `fileKey` in repo). Anatomy completed via offline `Spig_v1.2.fig` parse cross-checked with approved PNG. **Re-run MCP pass** when operator supplies cloud URL + share access.

## Exact next task

| Field | Value |
| ----- | ----- |
| Task | Services V2 — hero + breadcrumbs + subnav + program layout (block 1 only) |
| Strategy | `HYBRID_RECONSTRUCTION` |
| Source changes | New `uslugi-v2.html` + v2 partials only; V1 untouched |
| V1 fallback | Preserved |
| Home boundary | No home edits |
| Figma inputs | Cloud fileKey URL; MCP re-verify nodes `1:1310`, `1:4624` |
| Output | One block implementation + build pass + operator approval stop |

## Final verdict

```text
FP0002_SERVICES_FIGMA_MCP_AUDIT_COMPLETE_HYBRID_RECOMMENDED
```

With sub-status:

```text
LIVE MCP TARGET READ — BLOCKED (pending fileKey)
OFFLINE ANATOMY + V1 DIFFERENTIAL — COMPLETE
V2 IMPLEMENTATION — NOT_STARTED
```
