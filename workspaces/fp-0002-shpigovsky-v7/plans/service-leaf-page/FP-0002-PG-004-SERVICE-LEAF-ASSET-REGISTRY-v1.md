# FP-0002-PG-004 — Asset Registry v1

| Block | Visual description | Figma node | Existing runtime asset candidate | Decision |
| ----- | ------------------ | ---------- | -------------------------------- | -------- |
| hero | Man with whiskey glass — painterly hero | `1:1753` image 219 | `services-hero.webp` / new leaf hero | EXACT_EXPORT_REQUIRED |
| bordered-info | Lifebuoy decor behind bordered panel | `1:1789` image 13030403 | none exact | EXACT_EXPORT_REQUIRED |
| team-stats | Group staff photo in front of brick building | `1:1993` region | `shpigovsky-staff-group.webp` | REQUIRES_GROUP_INSPECTION |
| program-landscape | Clinic exterior lush green | `1:1954` region | `shpigovsky-clinic-landscape.webp` | REQUIRES_GROUP_INSPECTION |
| program cards ×4 | Genotyping / neuro / psycho / kinesio art | program section | `program-*.webp` set | EXACT_EXISTING_REUSE |
| corridor | Hallway with paintings | stages/approach region | `shpigovsky-interior-corridor.webp` | REQUIRES_GROUP_INSPECTION |
| specialists ×3 | Doctor portraits | `1:2029` | `home-specialists/*.webp` | EXACT_EXISTING_REUSE |
| founder | Sergey portrait + quote mark | `1:2066` | `founder-sergey-shpigovsky.png` | EXACT_EXISTING_REUSE |
| comfort gallery | 9 room/garden photos | `1:2082` | `home-comfort/*.webp` | REUSE_WITH_CONTENT |
| final-form bg | Dark blue + building faint | form region | `home-final-form-background.webp` | EXACT_EXISTING_REUSE |

- **Exact existing assets:** program card set, specialist portraits, founder, comfort set (verify order/count), final-form background
- **Exports required:** leaf hero, lifebuoy decor (if kept — see lifebuoy policy note in GROUP 1 plan)
- **Unresolved:** corridor vs team-stats photo boundary; exterior vs program transition crop
- **Duplicate risk:** reusing subdivision hero (`service-subdivision-hero.webp`) — WRONG subject; must not reuse without visual proof
- **Result:** COMPLETE for pass opening; export deferred to groups
