# FP-0002 Service Subdivision — Asset Map v1

**Note:** runtime assets live under `src/img/` in workspace (may be gitignored); verify paths in workspace before new export.

| Block | Figma node | Existing runtime asset | Reuse/new export | Format |
|-------|------------|------------------------|------------------|--------|
| Hero | `1:da4` | `assets/img/content/services/services-hero.webp` (hub) | REUSE or subdivision export | webp |
| Program dir 01 | `1:e75` | `program-genotyping.webp` | REUSE_EXACT | webp |
| Program dir 02 | `1:e75` | `program-neuropsychology.webp` | REUSE_EXACT | webp |
| Program dir 03 | `1:e75` | `program-psychocorrection.webp` | REUSE_EXACT | webp |
| Program dir 04 | `1:e75` | `program-kinesiotherapy.webp` | REUSE_EXACT | webp |
| Center interior | `1:ec0` / `1:e9c` | `shpigovsky-interior-corridor.webp` | REUSE candidate | webp |
| Team group | `1:e9c` | `shpigovsky-staff-group.webp` | REUSE candidate | webp |
| Exterior | `1:ec0` | `shpigovsky-clinic-landscape.webp` | REUSE candidate | webp |
| Specialists | `1:efc` | `home-specialists/*.webp` | REUSE_WITH_CONTENT | webp |
| Founder portrait | `1:f21` | founder assets in home-founder-quote | REUSE | webp/svg |
| Comfort gallery | `1:f31` | home-comfort gallery set | REUSE_WITH_CONTENT | webp |
| Reviews avatars | `1:f63` | home-reviews assets | REUSE_WITH_CONTENT | webp |
| Info cards | nested | TBD frame read | NEW_EXPORT likely | webp |
| Hero subdivision-specific | `1:da4` | — | NEW_EXPORT if differs from hub | webp |

## Duplicate risk

- Program direction images already in runtime — **do not re-export**
- Hub hero may differ from subdivision hero — verify Figma fill before reuse

## Result

`ASSET_MAP_COMPLETE_PENDING_PASS1_HERO_VERIFY`
