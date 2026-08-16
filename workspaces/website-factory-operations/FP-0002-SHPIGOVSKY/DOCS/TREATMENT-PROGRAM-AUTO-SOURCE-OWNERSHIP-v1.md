# Treatment Program — Auto-Source Ownership (v1)

**Wave:** V9-07A01  
**Status:** active local ownership model (post–Stable v1 correction)

## Canonical parent

- Page `#13` — `/o-centre/programma-lecheniya/`
- Published children are the only card content source.

## Per-card ownership

| Surface | Source |
|---------|--------|
| Title | Child page `post_title` (`get_the_title`) |
| URL | Child permalink (`get_permalink`) |
| Mini-description | ACF `treatment_program_short_description` on the child (`group_fp02_treatment_program_child`) |
| Order | `menu_order ASC`, then `ID ASC` |
| Marker / image assets | Non-content visual meta keyed by page ID in `shpigovsky_get_program_direction_visual_meta()` |

## Must not own card title/URL/description

- Hardcoded PHP slug/title maps
- `/o-centre/` repeater `about_program_items` (dormant / admin-hidden)
- Service repeater `programme_items` titles (dormant for frontend card rendering)

## Legitimate page-owned chrome

- O-centre: program heading / lead / intro texts
- Service sections: section program heading / lead / intros / foot labels

## Helper entrypoint

`WORDPRESS/theme/shpigovsky/inc/program-direction-helpers.php` → `shpigovsky_get_program_direction_items()`.
