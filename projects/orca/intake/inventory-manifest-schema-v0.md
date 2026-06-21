# Inventory Manifest Schema v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — contract for `inventory-manifest.json` at project intake.

Not a validator service. Not auto-generated without human review of classifications.

## Purpose

Provide a single machine-readable inventory of everything in a raw pack, how it was classified, where normalized copies live, and what remains unknown.

## File Location

Preferred:

```
projects/orca/projects/<project-id>/inventory-manifest.json
```

Acceptable alternate (legacy packs):

```
projects/orca/projects/<project-id>/raw-inventory/inventory-manifest.json
```

Document the chosen path in project `PROJECT.md`.

## Top-Level Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schema_version` | string | yes | `"inventory-manifest-v0"` |
| `project_id` | string | yes | Stable project slug |
| `raw_pack_path` | string | yes | Repo-relative path to incoming pack |
| `inventory_started_at` | string (ISO 8601) | yes | First scan timestamp |
| `inventory_completed_at` | string (ISO 8601) | no | When operator marked scan complete |
| `operator` | string | no | Who ran intake |
| `items` | array | yes | All inventoried entries |
| `summary` | object | yes | Counts by category |
| `safe_unknown` | array of strings | no | Explicit gaps |

## Item Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `item_id` | string | yes | Stable id, e.g. `inv-001` |
| `source_path` | string | yes | Path within raw pack |
| `category` | enum | yes | See categories below |
| `mime_or_ext` | string | no | `.pdf`, `image/png`, etc. |
| `size_bytes` | number | no | File size |
| `modified_at` | string | no | Source file mtime |
| `classification_confidence` | enum | no | `operator` \| `assisted` \| `unknown` |
| `evidence_grade` | enum | no | Links to evidence system — default `unverified` |
| `normalized_path` | string | no | After normalization |
| `distributed_to` | string | no | Project subfolder |
| `duplicate_of` | string | no | `item_id` if duplicate candidate confirmed |
| `notes` | string | no | Operator notes |
| `safe_unknown` | boolean | no | True if role still unclear |

## Categories (enum)

| Category | Use when |
|----------|----------|
| `documents` | PDF, DOCX, TXT, MD strategy/docs |
| `screenshots` | SERP, UI, ad captures |
| `spreadsheets` | XLSX, CSV, keyword sheets |
| `urls` | URL lists, bookmarks (files, not live crawl) |
| `competitors` | Competitor-specific materials |
| `exports` | Commander, analytics, platform dumps |
| `unknown_files` | Role not yet determined |
| `duplicate_candidates` | Probable duplicate — needs confirmation |

Items may not stay in `unknown_files` indefinitely without `safe_unknown` note at manifest level.

## Summary Object

```json
{
  "total_items": 0,
  "by_category": {
    "documents": 0,
    "screenshots": 0,
    "spreadsheets": 0,
    "urls": 0,
    "competitors": 0,
    "exports": 0,
    "unknown_files": 0,
    "duplicate_candidates": 0
  },
  "normalized_count": 0,
  "unresolved_unknown_count": 0
}
```

## Example (minimal)

```json
{
  "schema_version": "inventory-manifest-v0",
  "project_id": "triumph-manipulator",
  "raw_pack_path": "incoming/orca-triumph-raw-pack",
  "inventory_started_at": "2026-05-21T10:00:00+03:00",
  "operator": "human-operator",
  "items": [
    {
      "item_id": "inv-001",
      "source_path": "01 — Master PPC Landing Page.md",
      "category": "documents",
      "mime_or_ext": ".md",
      "classification_confidence": "operator",
      "evidence_grade": "operator-confirmed",
      "normalized_path": "projects/orca/projects/triumph-manipulator/normalized/2026-05-21-master-landing.md",
      "distributed_to": "landing-briefs"
    },
    {
      "item_id": "inv-002",
      "source_path": "Пример выгрузки кампании из Командера.xlsx",
      "category": "exports",
      "classification_confidence": "operator",
      "evidence_grade": "verified",
      "normalized_path": "projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/reference-template.xlsx",
      "distributed_to": "exports",
      "notes": "Legacy path — Triumph pack predates projects/ tree"
    }
  ],
  "summary": {
    "total_items": 2,
    "by_category": {
      "documents": 1,
      "screenshots": 0,
      "spreadsheets": 0,
      "urls": 0,
      "competitors": 0,
      "exports": 1,
      "unknown_files": 0,
      "duplicate_candidates": 0
    },
    "normalized_count": 2,
    "unresolved_unknown_count": 0
  },
  "safe_unknown": []
}
```

## HITL Rules

1. Manifest draft may be **assisted** (script listing files); categories require **operator** confirmation before downstream SoT use.
2. `duplicate_candidates` must resolve to merge, separate, or `duplicate_of` — no silent drops.
3. Changing `category` after distribution requires log entry in `logs/`.
4. Empty `items` array is invalid for a completed intake.

## Future JSON Schema

Formal JSON Schema file is **not** in v0. When added, it should live beside this doc as `inventory-manifest.schema.json` without claiming automated enforcement.

## Related Documents

- [orca-universal-intake-architecture-v0.md](orca-universal-intake-architecture-v0.md)
- [evidence-classification-system-v0.md](../evidence/evidence-classification-system-v0.md)
- [project-structure-contract-v0.md](../projects/project-structure-contract-v0.md)
