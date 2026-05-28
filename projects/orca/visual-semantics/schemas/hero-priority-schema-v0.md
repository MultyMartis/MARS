# Hero Priority Schema v0

## `hero_priority`

| Value | Meaning | Factory implementation |
|-------|---------|------------------------|
| `capability_first` | Specs before secondary messages | Spec list immediately under lead |
| `cta_first` | Form/call before long copy | Aside column top-aligned or stack form early on mobile |
| `qualification_first` | Anti-junk before cargo | `hero__notice` or notice above cargo |
| `balanced` | Explicit tradeoff | Document in `ambiguous` |

## `hero_layout_mode`

| Value | Meaning | Factory |
|-------|---------|---------|
| `grid_form_aside` | 2-col desktop + lower band | v5 `hero--v5` |
| `stacked` | Single column | Rare; small routes |
| `split_media` | Side image column | Use-case pages |
| `legacy_clutter` | **FORBIDDEN** | v4 index anti-pattern |

## Triumph zakaz

```yaml
hero_priority: capability_first
hero_layout_mode: grid_form_aside
```

## Mobile

When `hero_priority: cta_first` and `mobile_critical` includes `call`, apply `mobile_hero_cta_order` (vNext).
