# Metadata Layout Rules v1

## Cover page (required fields)

| Field | Source |
|-------|--------|
| `project_id` | `project_ref` in frontmatter |
| `route_id` | `route_slug` |
| `export_version` | pilot constant `v1` |
| `generated_at` | ISO timestamp at export run |
| `exported_by` | `ORCA_EXPORTED_BY` env or default label |
| `pack_id` | frontmatter |
| `pack_version` | frontmatter |
| `canonical_url` | frontmatter |
| `locale` | frontmatter |
| `artifact_state` | frontmatter |
| `content_mode` | frontmatter |
| `semantic_lock` | frontmatter → display `ACTIVE (MODE 1)` when active |

## Table layout

Two-column: label (35%) | value (65%). Label column shaded `#F5F5F5`.

## Monospace fields

- `project_id` / `project_ref`
- `route_id` / `route_slug`
- `pack_id`
- `canonical_url`
- Factory workspace paths

## Title block

Centered:

- **ORCA Content Pack Export**
- Subtitle: *Operational specification — Website Factory handoff*
