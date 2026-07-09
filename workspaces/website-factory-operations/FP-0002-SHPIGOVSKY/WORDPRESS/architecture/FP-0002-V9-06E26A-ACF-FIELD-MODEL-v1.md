# FP-0002 V9-06E26A ACF Field Model v1

## Group

`group_fp02_page_institutional` — extended for `/o-centre/` hub (page ID 11 conditional).

## Preserved

- `hero_eyebrow`, `hero_title_override`, `hero_lead`, `hero_media`, `hero_cta_label`

## Added (hub-only)

| Prefix | Purpose |
|--------|---------|
| `about_narrative_*` | Who we are |
| `about_who_treat_*` | Who we treat + spectrum/cards repeaters |
| `about_approach_*` | Approach band |
| `about_program_*` | Program section + items repeater |

## Existing reused

- `infrastructure_g0_g5` — hub-only conditional; G0–G4 text; images via static V9 theme assets

## Admin UX

- Conditional logic: page `== 11` (`/o-centre/`)
- Empty fields fall back to static V9 authority in theme helpers

Evidence: `validation/v9-06e26a-about-page-wordpress-acf-port/acf-field-model-result.json`
