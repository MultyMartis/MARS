# DOCX export notes

## Style alignment

Follow `exporters/docx-pilot/STYLE-GUIDE-v1.md`:

- Operational tone, tables for locks
- Visual semantics bundle as YAML block in appendix
- 🔒 for semantic locks in rendered DOCX

## Section layout rules

| Pack folder | Template rules file |
|-------------|---------------------|
| content/* | `templates/section-layout-rules-v1.md` |
| APPROVALS | `templates/approval-layout-rules-v1.md` |
| semantic lock | `templates/semantic-lock-layout-rules-v1.md` |

## Master-hot specific

1. Render **visual semantics table** on cover or page 2
2. Include **continuity matrix** from `ppc/ad-alignment.md`
3. Include **drift tables** (allowed / forbidden) — client-facing risk control
4. Do **not** embed workspace file paths in client export without operator toggle (operator copy may use internal appendix)

## Filename proposal

`triumph-manipulyator-zakaz-pack-v1.docx`

## Validation

Use `exporters/docx-pilot/validation/export-checklist-v1.md` when pilot extended.
