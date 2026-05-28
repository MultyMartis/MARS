# DOCX Export Architecture v0

## Status

**PRE-IMPLEMENTATION** — primary approved export format design.

DOCX is the **canonical sign-off artifact** for landing content packs. Markdown remains operational; PDF is derived later from approved DOCX.

## Document structure

```
┌─────────────────────────────────────────────┐
│ Cover / metadata block                       │
│  pack_id, version, route, gates, MODE 1 lock │
├─────────────────────────────────────────────┤
│ PPC continuity summary                       │
├─────────────────────────────────────────────┤
│ SEO continuity summary                       │
├─────────────────────────────────────────────┤
│ Section 01 HERO … Section 10 FINAL CTA       │
│  (each: H2, copy, CTA highlight, locks)       │
├─────────────────────────────────────────────┤
│ Approval & export footer                     │
└─────────────────────────────────────────────┘
```

## Style map (Word styles)

| Element | Style name (proposed) | Formatting |
|---------|----------------------|------------|
| Document title | `ORCA Title` | 18pt bold; pack name |
| Pack metadata | `ORCA Meta` | 9pt; gray; key-value lines |
| Section H1 (export) | `ORCA H1` | 16pt bold; section number + title |
| Section H2 (in-section) | `ORCA H2` | 13pt bold; subheads |
| Body | `ORCA Body` | 11pt; 1.15 line spacing |
| Bullets | `ORCA Bullet` | hanging indent; • |
| CTA block | `ORCA CTA Block` | shaded box; primary + secondary labels |
| Semantic lock line | `ORCA Lock` | 🔒 prefix; 9pt italic |
| SAFE UNKNOWN | `ORCA Unknown` | ⚠ prefix; amber semantic (manual review) |
| Separator | `ORCA Divider` | horizontal rule between sections |
| Spec table | `ORCA Table` | 2-column label / value |

## Metadata block (first page)

Required fields:

- `pack_id`, `pack_version`, `project_ref`
- `canonical_url`, `route_slug`
- `artifact_state`, `content_mode`, `semantic_lock`
- `exported_at`, `exported_by` (human)
- `approval_gates_snapshot`
- PPC: `group_label`, `display_path`
- Export: `export_id`, `export_format: docx`

## Section rendering rules

1. Print `section_order` + `section_title` as `ORCA H1`
2. `section_purpose` as italic lead paragraph
3. `copy_blocks` in document order; locked blocks include `ORCA Lock` footnote
4. `cta` rendered as `ORCA CTA Block`
5. `proof_elements` as bullets or table rows
6. `safe_unknown` never stripped or auto-resolved

## PPC / route metadata table

| Column | Example |
|--------|---------|
| Group | `01 — Манипулятор 5 тонн` |
| Display path | `manip-5-tonn` |
| Primary intent | `манипулятор 5 тонн краснодар` |
| Ad H1 | (locked string) |

## Approval footer (last page)

| Field | Value |
|-------|--------|
| Approved for factory | yes/no |
| Approved for client export | yes/no |
| Operator sign-off line | blank field for handwritten/digital sign |
| Semantic lock | MODE 1 ACTIVE / INACTIVE |

## Export prerequisites

| State | DOCX type allowed |
|-------|-------------------|
| `draft` | Internal watermark «DRAFT — NOT APPROVED» |
| `approved` | Standard export |
| `client-ready` | No draft watermark; `approved_for_client_export` required |

## Future tooling notes

- Prefer deterministic template (OOXML) over free-form AI doc generation
- Round-trip: DOCX edits must flow back to pack Markdown SoT via human merge
- Store output under project `exports/docx/` when implemented — path **SAFE UNKNOWN** until charter

## Boundary

Formatting specification only — no DOCX generator in v0.
