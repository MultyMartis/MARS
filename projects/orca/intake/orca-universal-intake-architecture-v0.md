# ORCA Universal Intake Architecture v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — operational architecture and HITL workflow design only.

This document does **not** describe a runtime intake service, autonomous file processor, or deployed ingestion agent.

## Purpose

Define how chaotic incoming materials enter ORCA, become inventoried, classified, normalized, and distributed into project structure — under **human supervision** at every decision point.

## Boundary

| In scope | Out of scope |
|----------|--------------|
| Drop-zone contract, inventory, classification vocabulary | Autonomous intake bots |
| HITL normalization workflow | Production file watchers |
| Distribution rules into project tree | OCR/scraping pipelines as products |
| Link to manifest schema | Guaranteed auto-classification |

## Incoming Raw Packs

### Drop zone (repository-level)

Operators place unprocessed materials in:

```
incoming/orca/<project-id>-raw-pack/
```

**Example (validated precedent):**

```
C:\AI MARS\incoming\orca-triumph-raw-pack\
```

**Target naming (new projects):**

```
incoming/orca/<project-id>-raw-pack/
```

The raw pack is **immutable by convention** after first inventory pass — copies and normalized derivatives live under `projects/orca/projects/<project-id>/`, not by rewriting the drop zone.

### Accepted material types (non-exhaustive)

- Documents: PDF, DOCX, TXT, MD
- Spreadsheets: XLSX, CSV exports
- Images: screenshots, SERP captures, competitor UI
- URLs and link lists (as references, not live fetch claims)
- Commander / ad platform exports
- Competitor notes, landing copies, pricing notes
- Chat exports, operator memos, anything file-like

**SAFE UNKNOWN:** file type alone does not imply semantic category. Classification requires operator confirmation or explicit manifest entry.

## Intake Pipeline (HITL)

```mermaid
flowchart LR
  A[Raw pack drop] --> B[Inventory scan]
  B --> C[Manifest draft]
  C --> D[Operator classify]
  D --> E[Normalize copies]
  E --> F[Distribute to project tree]
  F --> G[Evidence + research layers]
```

### Stage 1 — Inventory

- Enumerate all files in raw pack (path, size, modified time, extension).
- Detect probable duplicates (hash or name+size heuristic — **operator confirms**).
- Flag `unknown_files` when type or role is unclear.
- Output: draft `inventory-manifest.json` per [inventory-manifest-schema-v0.md](inventory-manifest-schema-v0.md).

**No stage may claim "processed" without a manifest row.**

### Stage 2 — Classify

Operator assigns each item to manifest categories:

- `documents`, `screenshots`, `spreadsheets`, `urls`, `competitors`, `exports`, `unknown_files`, `duplicate_candidates`

Classification is **operational labeling**, not truth certification. See [evidence-classification-system-v0.md](../evidence/evidence-classification-system-v0.md).

### Stage 3 — Normalize

- Copy (never move/delete from raw pack without explicit operator instruction per MARS file rules) into `projects/orca/projects/<project-id>/normalized/` with stable naming.
- Preserve original filename in manifest `source_path` / `normalized_path` mapping.
- Convert human-readable extracts where useful (e.g. MD summary of a PDF) — **manual or assisted, always reviewed**.

### Stage 4 — Distribute

Route normalized items into project subfolders per [project-structure-contract-v0.md](../projects/project-structure-contract-v0.md):

| Material signal | Target folder |
|-----------------|---------------|
| Competitor pages, ads, offers | `competitors/` |
| SERP captures, snapshots | `serp/` |
| Keyword lists, exports | `keywords/` |
| Strategy memos | `strategy/` |
| Landing copy, briefs | `landing-briefs/` |
| Commander / sheet exports | `exports/` |
| Unresolved | stay in `raw-inventory/` + manifest `unknown_files` |

### Stage 5 — Downstream use

Normalized intelligence feeds:

- **Search** / **RSYA** / other modes — [orca-campaign-mode-architecture-v0.md](../campaign-modes/orca-campaign-mode-architecture-v0.md)
- **Research layer** — [orca-research-layer-v0.md](../research/orca-research-layer-v0.md)
- **Artifacts** — [orca-artifact-system-v0.md](../artifacts/orca-artifact-system-v0.md)
- **Website Factory handoff** — [orca-website-factory-semantic-lock-v0.md](../intelligence/orca-website-factory-semantic-lock-v0.md)

## Relationship to Existing Triumph Flow

`projects/orca/ppc/triumph-manipulator/` is a **legacy-normalized operational pack** ingested from `incoming/orca-triumph-raw-pack/`. It remains the active Search production path.

Universal intake v0 does **not** require migrating Triumph into `projects/orca/projects/` immediately. New projects should use the canonical project tree; Triumph migration is **SAFE UNKNOWN** until explicitly chartered.

## Operator Responsibilities

1. Create raw pack folder and drop materials.
2. Run or supervise inventory → manifest draft.
3. Confirm classifications and evidence grades.
4. Approve normalized paths before PPC / Factory work cites them as SoT.
5. Mark gaps **SAFE UNKNOWN** rather than inferring competitor strategy or performance.

## Anti-Patterns

- Treating raw pack files as approved campaign truth.
- Auto-moving or deleting incoming files without explicit instruction.
- Claiming "ORCA ingested" when only files exist without manifest + review.
- Skipping manifest for "small" drops — small packs still need traceability.

## Related Documents

- [inventory-manifest-schema-v0.md](inventory-manifest-schema-v0.md)
- [project-structure-contract-v0.md](../projects/project-structure-contract-v0.md)
- [orca-operational-principles-v0.md](../orca-operational-principles-v0.md)

## Version Note

v0 establishes intake **shape**. Automation helpers (scripts, CLI) may be added later as **human-invoked tools** only — not as autonomous intake runtime.
