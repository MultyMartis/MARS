# ORCA Landing Content Pack System v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — semantic export layer for landing pages.

**Not:** HTML generator, Website Factory engine, Commander exporter, or autonomous content product.

## Definition

A **Landing Content Pack** is a structured, human-authored artifact that captures **marketing and operational semantics** for one landing route (or one capability/use-case surface), independent of frontend implementation.

| Property | Value |
|----------|--------|
| Primary audience | Human operator, strategist, Factory implementer |
| Secondary outputs | DOCX (approved), Markdown (operational), future PDF (client) |
| SoT for copy under MODE 1 | Approved content pack + handoff |
| Anti-pattern | Treating pack as final HTML or design spec |

## Layer position

```
┌─────────────────────────────────────────────────────────┐
│ ORCA Research / Strategy                                 │
│  (snapshots, intent tiers, competitor notes, PPC groups) │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│ Landing Content Pack  ← THIS SYSTEM                      │
│  (section contracts, copy, locks, gates)               │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────┐
│ DOCX export      │  │ Markdown export  │  │ Factory  │
│ (primary approve)│  │ (internal ops)   │  │ handoff  │
└──────────────────┘  └──────────────────┘  └──────────┘
```

## Input sources (allowed)

| Source type | Typical path / form | Pack usage |
|-------------|---------------------|------------|
| ORCA research | `research/`, session snapshots | Intent, SERP notes, evidence refs |
| Competitor analysis | research contracts, operator notes | Positioning deltas — not copied claims |
| SERP snapshots | `live-observations/`, research | Continuity checks — not auto-imported |
| PPC campaign groups | `ppc/*/schema/instances/*.json` | `ppc_group_ref`, ad continuity fields |
| Manually supplied files | `incoming/orca-*-raw-pack/` | Normalized into pack sections |
| AI-generated audits | operator-reviewed only | Findings → edits; never auto-approved |
| Normalized evidence | `evidence/` grading | Support claims; mark SAFE UNKNOWN if weak |
| Approved strategy artifacts | strategy docs with gates | Locks positioning and section order |

**Rule:** Inputs inform the pack; only **human-approved** pack states unlock Factory MODE 1 or client export.

## Output types

| Output | Role | v0 status |
|--------|------|-----------|
| **DOCX** | Primary **human-approved** export; sign-off artifact | Architecture documented; tooling future |
| **Markdown** | Internal diff, Git review, agent-assisted editing | Architecture documented |
| **PDF** | Future client-ready layer | Architecture stub only |
| **Website Factory handoff** | Implementation brief derived from pack | Template + workflow |
| **Client-ready bundle** | DOCX + metadata + redaction policy | Future; gate `approved_for_client_export` |

## Canonical page structure (10 sections)

Every capability or use-case landing pack uses this **ordered** section model:

| # | `section_id` | Title (canonical) |
|---|--------------|-------------------|
| 01 | `hero` | HERO |
| 02 | `specs` | SPECS |
| 03 | `allowed_tasks` | ALLOWED TASKS |
| 04 | `denied_tasks` | DENIED TASKS |
| 05 | `order_flow` | ORDER FLOW |
| 06 | `pricing` | PRICING |
| 07 | `trust` | TRUST |
| 08 | `b2b` | B2B |
| 09 | `faq` | FAQ |
| 10 | `final_cta` | FINAL CTA |

Sections may be **collapsed or omitted** only when operator documents rationale (e.g. B2B merged into trust on a thin use-case page). Default for Triumph capability pages: **all ten**.

Section field contract: [schemas/section-contract-schema-v0.md](schemas/section-contract-schema-v0.md).

## Content modes

| Mode | Condition | Website Factory |
|------|-----------|-----------------|
| **MODE 1** | Approved pack exists; `semantic_lock: active`; gate `approved_for_factory` | **Must not** rewrite approved copy — presentation only |
| **MODE 2** | No approved pack / exploratory build | Placeholder or demo copy allowed; **must not** ship to paid traffic |

See [semantic-lock-export-rules-v0.md](semantic-lock-export-rules-v0.md) and [../intelligence/orca-website-factory-semantic-lock-v0.md](../intelligence/orca-website-factory-semantic-lock-v0.md).

## Pack envelope (summary)

Full schema: [schemas/landing-content-pack-schema-v0.md](schemas/landing-content-pack-schema-v0.md).

Minimum pack identity fields:

- `pack_id`, `pack_version`, `project_ref`, `route_slug`, `canonical_url`
- `content_mode` (`MODE_1` | `MODE_2`)
- `artifact_state` (lifecycle)
- `approval_gates` (boolean flags — human-set only)
- `ppc_continuity` (group, headlines, display path)
- `sections[]` (section contracts)

## Relationship to other ORCA trees

| Tree | Relationship |
|------|----------------|
| `ppc/triumph-manipulator/landing-pages/` | Blueprint / doctrine source — may feed pack authoring |
| `ppc/.../handoff/*-handoff.md` | Production handoff — may mirror or derive from approved pack |
| `ppc/.../tools/exporter-cli/` | **Separate** — Commander XLSX; not content pack export |
| `projects/orca/projects/<id>/` | Per-project approvals and `PROJECT.md` gate summary |

## Boundary

Defines **what** a content pack is and **how** it relates to ORCA and Factory. Does not implement exporters, validators, or deployment.
