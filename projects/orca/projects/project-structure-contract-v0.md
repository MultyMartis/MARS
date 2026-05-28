# ORCA Project Structure Contract v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — canonical folder contract for ORCA-managed PPC projects.

Not a database schema. Not a sync engine. Not proof that any given project is fully populated.

## Purpose

Separate **raw inputs**, **normalized intelligence**, and **approved artifacts** so operators and assisted workflows never confuse drafts with operational truth.

## Canonical Root

```
projects/orca/projects/<project-id>/
```

`<project-id>` — stable slug (e.g. `triumph-manipulator-krasnodar`, `acme-plumbing-spb`). Must match raw pack suffix where applicable: `incoming/orca/<project-id>-raw-pack/`.

## Folder Contract

| Path | Role | Mutability | Downstream use |
|------|------|------------|----------------|
| `raw-inventory/` | Indexed copies or pointers to raw pack items post-inventory | Append-only during intake | Traceability only — **not** SoT for ads |
| `normalized/` | Human-reviewed normalized files (renamed, extracted, cleaned) | Versioned by operator | Research, strategy, drafting inputs |
| `research/` | SERP notes, observation summaries, methodology outputs | Reviewed drafts → approved | Mode-specific campaign design |
| `competitors/` | Competitor ads, landings, offers, screenshots | Evidence-graded | Positioning, hooks, negatives |
| `serp/` | SERP snapshots, captures, snapshot contracts | Time-bound | Query architecture, ad patterns |
| `keywords/` | Keyword lists, clusters, negative candidates | Draft until approved | Search / RSYA packs |
| `strategy/` | Intent tiers, segment maps, commercial doctrine | Approved strategy docs | Campaign architecture |
| `landing-briefs/` | Page-level briefs, heroes, CTA rules | Approved briefs lock Factory | Website Factory handoff |
| `campaign-modes/` | Mode-specific packs (search, rsya, …) | Per-mode lifecycle | Export and validation targets |
| `artifacts/` | Deliverables (audits, exports, reports) | Status-driven | Client / operator delivery |
| `exports/` | Commander XLSX, sheet patches, transport outputs | Production-ready gate | Platform import (human) |
| `approvals/` | Sign-off records, checklists, HITL decisions | Append audit trail | Launch authority |
| `logs/` | Session logs, intake notes, run summaries | Operational diary | Postmortems, memory |

## Three-Layer Truth Model

```
┌─────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│  RAW INPUTS     │ ──► │ NORMALIZED           │ ──► │ APPROVED ARTIFACTS  │
│  (inventory)    │     │ INTELLIGENCE         │     │ (production gate)   │
└─────────────────┘     └──────────────────────┘     └─────────────────────┘
        │                          │                            │
   raw-inventory/            normalized/                  artifacts/
   incoming pack              research/                    exports/
                              competitors/                 approvals/
                              serp/ keywords/
                              strategy/ landing-briefs/
```

**Rule:** PPC export, Factory handoff, and Commander import may cite **approved** layer paths only unless explicitly marked draft in session.

## Per-Folder Minimum Expectations

### `raw-inventory/`

- Links to `inventory-manifest.json` (may live at project root or here — project README should state location).
- No semantic editing of source files in place.

### `normalized/`

- Stable filenames: `<date>-<category>-<short-slug>.<ext>`
- Each file should be mappable to a manifest `item_id`.

### `research/` / `competitors/` / `serp/`

- Observations follow [orca-research-layer-v0.md](../research/orca-research-layer-v0.md) and existing `research/serp-snapshot-contract-v1.md` where applicable.
- Evidence grades per [evidence-classification-system-v0.md](../evidence/evidence-classification-system-v0.md).

### `campaign-modes/`

Suggested internal layout:

```
campaign-modes/
  search/
  rsya/
  retarget/
  brand/
  local/
  experimental/
```

Only populate folders for modes actually in scope. Empty mode folder = **not active**, not failure.

### `artifacts/` / `exports/`

- Artifact types and statuses: [orca-artifact-system-v0.md](../artifacts/orca-artifact-system-v0.md).
- Transport exports (Commander XLSX) remain **dumb transport** — not campaign SoT (Triumph precedent).

### `approvals/`

Minimum approval record fields (markdown or YAML):

- `artifact_ref`, `approver`, `date`, `scope`, `notes`, `safe_unknown_gaps`

### `logs/`

- Intake session, validation run, export run, Factory handoff — human-readable summaries.

## Coexistence with `projects/orca/ppc/<pack>/`

Operational packs under `ppc/` (e.g. `triumph-manipulator`) remain valid **until migrated**.

| Aspect | `ppc/<pack>/` (legacy) | `projects/<project-id>/` (v0 canonical) |
|--------|------------------------|----------------------------------------|
| Status | Active Triumph production | Target for new multi-mode projects |
| Intake | Already normalized from raw pack | Full intake pipeline |
| Breaking change | **None required** by this contract | Opt-in per project |

## Project Root Files (recommended)

| File | Purpose |
|------|---------|
| `PROJECT.md` | Human summary: niche, geo, modes in scope, status |
| `inventory-manifest.json` | Intake inventory SoT |
| `OPERATIONAL-INDEX.md` | Operator navigation (optional but recommended) |

## SAFE UNKNOWN

- Whether all future ORCA projects migrate from `ppc/` to `projects/` — **not decided in v0**.
- Automated folder creation — **not claimed**; operator or explicit script invocation only.

## Related Documents

- [orca-universal-intake-architecture-v0.md](../intake/orca-universal-intake-architecture-v0.md)
- [inventory-manifest-schema-v0.md](../intake/inventory-manifest-schema-v0.md)
- [orca-artifact-system-v0.md](../artifacts/orca-artifact-system-v0.md)
