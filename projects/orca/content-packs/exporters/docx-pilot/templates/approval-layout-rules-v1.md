# Approval Layout Rules v1

## Placement

Final section of DOCX (after Factory notes), preceded by page break.

## Gates rendered

| Gate | Source |
|------|--------|
| `approved_for_factory` | YAML frontmatter `approval_gates` |
| `approved_for_ads` | same |
| `approved_for_launch` | same |
| `approved_for_client_export` | same |

## Display format

- Table: gate name | YES — approved / NO — not approved / UNKNOWN
- Snapshot disclaimer: export does not modify gates
- Operator sign-off blank lines (name, date, notes)
- `export_id` + `generated_at` footer

## Human-only

No checkbox automation. No API callback. No gate promotion on export success.

## Pack-level table

If `## Operator sign-off` table exists in source MD, include as supplementary text before sign-off blank.
