# Export Metadata Schema v0

## Purpose

When export tooling exists, each export run produces a **sidecar metadata** record (JSON or YAML) alongside DOCX/Markdown/PDF.

## `export_record` object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `export_id` | string | yes | UUID or `export-YYYYMMDD-NN` |
| `exported_at` | ISO datetime | yes | |
| `exported_by` | string | yes | Human operator identifier |
| `export_format` | enum | yes | `docx` \| `markdown` \| `pdf` |
| `export_mode` | enum | yes | See [exporters/export-modes-v0.md](../exporters/export-modes-v0.md) |
| `source_pack_id` | string | yes | |
| `source_pack_version` | string | yes | |
| `source_artifact_state` | string | yes | State at export time |
| `content_mode` | string | yes | `MODE_1` \| `MODE_2` |
| `semantic_lock_snapshot` | string | yes | `active` \| `inactive` |
| `approval_gates_snapshot` | object | yes | Copy of gates at export |
| `output_path` | string | yes | Relative path in repo or external store |
| `checksum` | string | optional | File hash when tooling supports |
| `notes` | string | optional | Operator comment |

## `approval_gates_snapshot`

```json
{
  "approved_for_factory": true,
  "approved_for_client_export": false,
  "approved_for_ads": false,
  "approved_for_launch": false
}
```

## `docx_formatting_profile` (DOCX only)

| Field | Description |
|-------|-------------|
| `profile_id` | e.g. `orca-landing-docx-v0` |
| `styles_version` | H1/H2/CTA block style set version |

## `redaction` (client export)

| Field | Description |
|-------|-------------|
| `client_visible` | bool |
| `redacted_fields[]` | Internal operator notes stripped |

## Anti-patterns

- Metadata generated without human `exported_by` (**invalid for approved export**)
- Gates snapshot differs from pack front-matter without explanation

## Boundary

Metadata contract only — no exporter implementation in v0.
