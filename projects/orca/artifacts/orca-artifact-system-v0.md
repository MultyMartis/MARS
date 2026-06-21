# ORCA Artifact System v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — typed deliverables and lifecycle labels.

Not an artifact repository service. Not version control product. Files live in project tree per [project-structure-contract-v0.md](../projects/project-structure-contract-v0.md).

## Purpose

Name what ORCA produces, where it lives, how it progresses from draft to production-ready, and how it differs from raw intake files.

## Artifact vs Raw Input

| | Raw intake | Artifact |
|---|------------|----------|
| Source | Incoming pack | ORCA workflow output |
| Truth status | Never operational SoT alone | Status-gated |
| Location | `incoming/`, `raw-inventory/` | `artifacts/`, `exports/`, mode folders |
| Manifest | inventory item | artifact registry entry (optional v1) |

## Artifact Types

| Type | Typical format | Primary folder | Consumers |
|------|----------------|----------------|-----------|
| PDF audit | `.pdf` | `artifacts/audits/` | Operator, client review |
| DOCX strategy | `.docx` | `artifacts/strategy/` | Strategy sign-off |
| XLSX export | `.xlsx` | `exports/` | Commander import (human) |
| Keyword pack | `.xlsx`, `.csv`, `.md` | `keywords/`, `artifacts/` | Search / RSYA modes |
| Landing brief | `.md` | `landing-briefs/` | Website Factory MODE 1 |
| Competitor report | `.md`, `.pdf` | `competitors/`, `artifacts/` | Positioning, negatives |
| SERP review | `.md` + screenshots | `serp/`, `artifacts/` | Query architecture |
| Validation report | `.json`, `.md` | `artifacts/validation/` | Pre-export gate |
| Handoff package | `.md` | `artifacts/handoff/` or pack `handoff/` | Website Factory |
| Campaign structure doc | `.md` | `strategy/`, `campaign-modes/` | Architecture review |
| Operator checklist | `.md` | `approvals/`, `artifacts/` | Import / launch HITL |

Formats are indicative — operator may add types with `PROJECT.md` glossary.

## Lifecycle Statuses

```
draft → reviewed → approved → production-ready → archived
```

| Status | Meaning | May be cited as SoT? |
|--------|---------|----------------------|
| `draft` | Work in progress | No |
| `reviewed` | Human read; comments may remain | No — unless explicitly noted partial |
| `approved` | Operator sign-off for semantic content | Yes — for strategy and briefs |
| `production-ready` | Cleared for export import or Factory MODE 1 | Yes — for transport and build |
| `archived` | Superseded; kept for history | Traceability only |

**Promotion:** human only. AI-generated files default to `draft` with `ai-derived` evidence tag.

## Required Metadata (recommended front matter)

```yaml
artifact_id: art-2026-05-21-search-export-01
type: xlsx_export
status: production-ready
project_id: triumph-manipulator
mode: search
created_at: 2026-05-21
approved_by: operator
source_evidence: []
safe_unknown: []
supersedes: null
```

## Type-Specific Rules

### XLSX exports (Commander)

- **Transport only** — does not prove campaign performance or platform acceptance.
- Must pass validation CLI output reference when applicable (Triumph: `tools/validation-cli/`).
- `production-ready` requires import checklist completion (human).

### Landing briefs

- `approved` minimum before Factory MODE 1 semantic lock.
- Must link intent tier and CTA contract.

### PDF / DOCX audits

- Claims inside must map to evidence grades.
- UNKNOWN sections mandatory where data missing.

### Keyword packs

- Search: cluster ↔ intent ↔ landing route columns required in reviewed state.
- RSYA: must not reuse Search pack without mode relabel and validation.

## Storage Layout (within project)

```
artifacts/
  audits/
  strategy/
  validation/
  handoff/
  reports/
exports/
  commander/
  patches/
```

Legacy Triumph paths under `ppc/triumph-manipulator/` remain valid.

## Relationship to Approvals

Sign-off records in `approvals/` should reference `artifact_id` and final `status`.

## Anti-Patterns

- Marking `production-ready` because export script ran without human import check.
- Archiving without `supersedes` link — breaks audit trail.
- Using draft keyword pack in Commander import.

## SAFE UNKNOWN

- Central artifact registry JSON — **not in v0**; per-project files only.
- Automated status transitions — **not claimed**.

## Related Documents

- [project-structure-contract-v0.md](../projects/project-structure-contract-v0.md)
- [evidence-classification-system-v0.md](../evidence/evidence-classification-system-v0.md)
- [orca-website-factory-semantic-lock-v0.md](../intelligence/orca-website-factory-semantic-lock-v0.md)
- [orca-campaign-mode-architecture-v0.md](../campaign-modes/orca-campaign-mode-architecture-v0.md)
