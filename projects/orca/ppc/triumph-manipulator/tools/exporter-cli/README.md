# ORCA Exporter Prototype v0

**Status:** Local human-operated transport prototype · **NOT** production exporter.

**Fidelity phases:** Template introspection — [template-analysis-report.md](template-analysis-report.md) · Template-fill export — [template-fill-notes-v0.md](template-fill-notes-v0.md) · **Sheet1 ZIP patch** — [sheet1-patch-notes-v0.md](sheet1-patch-notes-v0.md) · **Template cleanup + new entity mode** — [template-cleanup-rules-v0.md](template-cleanup-rules-v0.md) · XLSX integrity — [xlsx-integrity-notes-v0.md](xlsx-integrity-notes-v0.md) · OOXML forensics — [ooxml-diff-report-v0.md](ooxml-diff-report-v0.md) · **NOT** import automation.

## Purpose

Minimal Node.js CLI that:

1. Loads validated `OrcaPpcDocument` JSON  
2. Loads paired `ValidationReport` JSON  
3. Runs **fail-closed** precheck (`export_allowed`, blocking errors, schema, search-only)  
4. Maps entities to logical Commander-oriented rows (deterministic, no semantic rewriting)  
5. Writes an XLSX **transport draft** (logical sheets **or** `--template-fill` into cloned Commander template)

Tests exporter architecture: validation-before-export handshake → dumb transport layer.

## What this is NOT

- **Not** a production exporter or Commander-fidelity implementation  
- **Not** Yandex Direct API integration, auto-upload, or campaign launcher  
- **Not** a service, daemon, watcher, scheduler, or orchestration system  
- **Not** autonomous export pipeline — **human-triggered** single `node export.js` run only  
- **Not** semantic AI, auto-fix, or validation replacement  

## Validation-before-export

Export **requires** a ValidationReport from [validation-cli](../validation-cli/README.md).

| Gate | Behavior |
|------|----------|
| Missing report | Block (`MISSING_VALIDATION_REPORT`) |
| `export_allowed !== true` | Block (`EXPORT_NOT_ALLOWED`) |
| `blocking_errors.length > 0` | Block (`BLOCKING_ERRORS_PRESENT`) |
| Invalid report schema | Block (`INVALID_REPORT_SCHEMA`) |
| Unsupported `schema_version` | Block |
| Document `search_only_scope !== true` | Block (`NON_SEARCH_SCOPE`) |
| `validation_status` failed/incomplete | Block |

See [export-blocking-rules-v1.md](../../exporter/export-blocking-rules-v1.md) and [export-preconditions-v1.md](../../exporter/export-preconditions-v1.md).

## Supported entities (v0 scope)

| Entity | Sheet |
|--------|--------|
| Campaigns | `campaigns` |
| Groups | `groups` |
| Keywords | `keywords` |
| Ads | `ads` |
| Fastlinks + callouts | `extensions` |

**Skipped in v0:** bid modifiers, geo IDs, retargeting, RSYA, campaign/group negatives, advanced Direct features.

## Prerequisites

- Node.js ≥ 18  
- `npm install` in this directory  

## How to run

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm install

node export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  ../../tools/validation-cli/output/validation-report.output.json
```

**Template-fill mode** (clone Commander template → write sheet **Тексты**):

```bash
node export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json \
  --template-fill
```

See [sample-template-fill-run.md](sample-template-fill-run.md). Optional: custom output path as third positional after flags.

**Sheet1 ZIP patch mode** (byte-preserving transport — **only** `sheet1.xml` modified):

```bash
node sheet1-patch-export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json
```

Output: `output/triumph-sheet1-patch-draft.xlsx`. See [sample-sheet1-patch-run.md](sample-sheet1-patch-run.md). **NOT** ExcelJS full rewrite · Commander compatibility **experimental**.

## Expected inputs

| Input | Source |
|-------|--------|
| PPC document | `schema/instances/*.json` — `orca-ppc-document-v1` |
| ValidationReport | `validation-cli` output or operator-approved copy |

`validated_document_id` must match document `project_id`.

## Expected outputs

| Output | Path |
|--------|------|
| Logical draft | `output/triumph-export-draft.xlsx` (default) |
| Template-fill draft | `output/triumph-commander-template-fill-draft.xlsx` (`--template-fill`) |
| Logical sheets | `_meta`, `campaigns`, `groups`, `keywords`, `ads`, `extensions` |
| Template-fill | Cloned template; data in **Тексты** from row 16 |

Logical column headers — optional translation via [commander-header-map-v0.json](commander-header-map-v0.json) when present. Workbook **layout** still differs from Commander template (five logical sheets vs single **Тексты** sheet). See [fidelity-notes-v0.md](fidelity-notes-v0.md).

## Commander template fidelity v0 (analysis only)

| Command | Output |
|---------|--------|
| `node template-reader.js` | `template-sheet-index-v0.json`, `commander-header-map-v0.json` |
| `npm run template:analyze` | Same |

| Doc | Role |
|-----|------|
| [template-analysis-report.md](template-analysis-report.md) | Human-readable workbook analysis |
| [fidelity-notes-v0.md](fidelity-notes-v0.md) | Current fidelity level + blockers |
| [sample-template-analysis.md](sample-template-analysis.md) | Operator runbook |

## Commander template-fill v0

| Command | Output |
|---------|--------|
| `node export.js … --template-fill` | Cloned template with ORCA rows in **Тексты** |
| `npm run export:template-fill` | Sample fixture run |

| Doc | Role |
|-----|------|
| [template-fill-notes-v0.md](template-fill-notes-v0.md) | Fidelity level, manual edits, **NOT production-safe** |
| [sample-template-fill-run.md](sample-template-fill-run.md) | Operator runbook + fail examples |

## XLSX integrity hardening v0

| Artifact | Role |
|----------|------|
| [xlsx-integrity-notes-v0.md](xlsx-integrity-notes-v0.md) | Root cause, safe-write discipline, recovery-mode context |
| [sample-integrity-run.md](sample-integrity-run.md) | Integrity success/fail console examples + operator checklist |
| `xlsx-integrity-check.js` | Post-save ExcelJS reopen validation (fail-closed on `--template-fill`) |

Template-fill export removes broad range clears, writes **exact mapped cells only** (row 16+), and aborts if reopen check fails.

## OOXML workbook forensics v0

| Command | Output |
|---------|--------|
| `node ooxml-forensics.js` | Structure indexes + console diff summary |
| `npm run forensics:ooxml` | Same (after template-fill output exists) |

| Doc | Role |
|-----|------|
| [ooxml-diff-report-v0.md](ooxml-diff-report-v0.md) | ZIP/worksheet diff findings |
| [ooxml-risk-analysis-v0.md](ooxml-risk-analysis-v0.md) | Root cause confidence + ExcelJS fidelity assessment |
| [sample-ooxml-analysis.md](sample-ooxml-analysis.md) | Operator runbook |

**Finding (v0):** ExcelJS full workbook `writeFile` rewrites all sheets; Excel recovery likely — see risk analysis. **NOT** fixed in forensics phase.

**NOT:** Direct API · auto-import · runtime · guaranteed Commander import.

## Commander template analysis v0

**NOT:** Direct API · auto-import · runtime (analysis artifacts only).

## Fail-closed philosophy

Any gate failure → **non-zero exit**, no partial workbook, explicit operator-readable block code and reason.

## Human review requirement

Even on success:

- Review XLSX against JSON source and Commander template  
- Import manually in Direct Commander  
- **Launch** remains human-only — exporter does not set or imply launch approval  

## Related docs

- [entity-to-commander-mapping-v1.md](../../exporter/entity-to-commander-mapping-v1.md)  
- [exporter-engine-overview-v1.md](../../exporter/exporter-engine-overview-v1.md)  
- [sample-run.md](sample-run.md)  
- [future-expansion-notes-v0.md](future-expansion-notes-v0.md)  
