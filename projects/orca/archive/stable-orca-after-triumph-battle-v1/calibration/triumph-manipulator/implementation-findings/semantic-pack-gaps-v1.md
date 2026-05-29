# Semantic Pack Gaps v1

**Reference pack:** `triumph-manipulyator-5-tonn-pack-v0.md`  
**Missing pack:** master hot / `zakaz` / `01-master-hot-general`

## Gaps (ORCA must add to packs)

| Gap | Impact | Proposed pack field |
|-----|--------|---------------------|
| No master hot pack | Factory infers from blueprint + cousin | `pack_type: master_hot` template |
| Hero layout contract | Only copy blocks, no zones | `hero_layout: v5_grid_form_right` |
| Trust hero mode | Blueprint text vs ops strip | `trust_hero_mode`, `trust_hero_copy[]` |
| Qualification placement | Lost in v5 | `qualification_line_required: true`, `placement: hero_lower` |
| Multi-ad H1 strategy | Continuity break | `h1_primary`, `h1_alt_ad_mapping[]` |
| Visual density budget | Overbuilt cargo row | `hero_interactive_max`, `cargo_cards[]` |
| CTA exact strings | Lexical drift | `cta_primary_label` 🔒 |
| CTA surface priority | call vs form | `cta_surface_priority[]` |
| Mobile critical markers | Not in pack | `mobile: { call_sticky: true, form_fold_safe: false }` |
| Image logic | Unspecified | `hero_bg_asset`, `hero_machine_image: none \| aside` |
| Proof weight levels | P0–P4 not encoded | `block_importance: { hero: P0, trust: P2 }` |
| Compactness tier | — | `compactness: dense` |
| Frontend implementation hints | Weak factory_notes | `factory_implementation_notes` per zone |
| Semantic importance | All sections equal in blueprint | `section_priority: P0–P4` |
| Shared partial warnings | B2B on master hot | `shared_partials: []` with review flag |

## Fields that worked in 5-ton pack (reuse)

- Positioning locks table
- PPC continuity table
- Per-section semantic locks 🔒
- `factory_notes` pointing to v4 partials (update to v5 paths)

## Pack authoring order (recommended)

1. Clone 5-ton pack structure
2. Replace route / group / ads from `grp_fc12_zakaz`
3. Insert hero v5 contract from [next-evolution/hero-v2-requirements.md](../next-evolution/hero-v2-requirements.md)
4. Operator review → `approved_for_factory`

## DOCX export

Pilot targets 5-ton pack only — master hot export **deferred** until pack exists.
