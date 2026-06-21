# MIG — System Overview

**Status:** **documented** — R1 layer definition only.  
**Not:** implementation spec, tool catalog, or runtime architecture.

---

## R1 — Market Groundtruth Layer

| Dimension | Definition |
|-----------|------------|
| **Mission** | Capture and preserve **observable market reality** (SERP, competitors, local pack, reviews, trust, offers, CTAs) with explicit evidence grading and human approval before downstream use. |
| **Inputs** | Operator-defined **research scope** (region, date, queries), access to public/market surfaces humans can observe, and capture discipline (snapshots, notes, manifests). |
| **Outputs** | Normalized **observations**, **snapshots**, **evidence grades**, **SAFE UNKNOWN** markers, and **approved handoff packs** for ORCA (R2). |
| **Ownership** | **MIG** — acquisition, normalization, grading, review, approval, snapshot preservation, research session manifests. |
| **Consumers** | **ORCA** (primary) — interpretation, clustering, campaign architecture, PPC workflows. Website Factory and implementation layers consume **only** via downstream chains — not direct MIG scope. |
| **Non-goals** | Intent/semantic clustering; campaign architecture; LRL; PPC exports; Factory blueprints; content generation; CMS ops; runtime orchestration; automation; n8n. |

---

## MIG lifecycle (documentation-only)

No implementation details — human-operated phases:

```text
Capture → Normalize → Grade → Review → Approve → Handoff
```

| Phase | Intent |
|-------|--------|
| **Capture** | Record SERP, competitor, local pack, review, trust, offer, and CTA observations with snapshots where applicable. |
| **Normalize** | Structure observations into consistent session fields (scope, sources, dated notes) without semantic clustering. |
| **Grade** | Assign **evidence grade** per observation set; mark gaps as **SAFE UNKNOWN**. |
| **Review** | Human review of completeness, bias, and capture quality. |
| **Approve** | Explicit human sign-off (**Approved By**) before handoff. |
| **Handoff** | Deliver minimum pack per [contracts/mig-orca-handoff-contract-v0.md](contracts/mig-orca-handoff-contract-v0.md) — **human handoff only**. |

**Reality acquisition discipline:** Trust and capture-mode ordering (Human → Browser → Structured Search → Intelligence) is defined in [contracts/MIG-REALITY-ACQUISITION-MODEL-v1.md](contracts/MIG-REALITY-ACQUISITION-MODEL-v1.md), including **Human Review Mode** and the `evidence/review.md` package.

---

## Research Request (intake)

A **Research Request** is the canonical domain object for MIG intake — not a Telegram command, webhook body, or task file. Transport surfaces normalize into one request shape before session work begins. Full field, lifecycle, and adapter rules: [contracts/mig-research-request-contract-v0.md](contracts/mig-research-request-contract-v0.md).

```text
Research Request → Research Session → Research Pack → ORCA
```

---

## Research session (conceptual)

A **research session** is a bounded unit of groundtruth work:

- Declared **scope**, **region**, and **date**
- Listed **queries** and **evidence sources**
- Attached **snapshots** and **observations**
- Session-level **evidence grade** and **SAFE UNKNOWN** summary
- Optional approval gate before ORCA intake

Session reporting template: [reports/REPORT-TEMPLATE.md](reports/REPORT-TEMPLATE.md).

**Research Pack** (primary MIG output) — structure, lifecycle, evidence, and ORCA consumption rules: [contracts/mig-research-pack-contract-v0.md](contracts/mig-research-pack-contract-v0.md).

---

## Boundary reminder

| MIG | ORCA |
|-----|------|
| Acquires reality | Interprets reality |
| Snapshots & observations | Clusters, architecture, exports |
| Evidence grade at capture | Campaign and semantic decisions |

See [boundaries.md](boundaries.md).
