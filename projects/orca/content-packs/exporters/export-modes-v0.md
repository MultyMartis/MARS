# Export Modes v0

## Purpose

Vocabulary for `export_mode` in [export metadata](../schemas/export-metadata-schema-v0.md).

## Modes

| Mode | Audience | Pack state min | Gates typical |
|------|----------|----------------|---------------|
| `internal_draft` | Operator only | `draft` | none — watermark required |
| `internal_review` | Operator + reviewer | `reviewed` | none |
| `operational_markdown` | Git / Cursor ops | `approved` | optional |
| `approved_docx` | Sign-off artifact | `approved` | optional `approved_for_factory` |
| `factory_handoff_bundle` | Lane A Factory | `factory-ready` | `approved_for_factory` |
| `client_docx` | External client | `client-ready` | `approved_for_client_export` |
| `client_pdf` | External client | `client-ready` | `approved_for_client_export` (future) |

## Content mode interaction

| content_mode | Export constraint |
|--------------|-------------------|
| `MODE_1` | Exports must include `semantic_lock_snapshot: active` when pack approved |
| `MODE_2` | Exports must be labeled «DEMO / PLACEHOLDER» in header |

## Commander export (out of scope)

`commander_xlsx` is **not** a content-pack export mode — use exporter-cli.

## Boundary

Mode names only.
