# Visual Density Observations v1

**Scope:** First two screens (hero + specs) — highest calibration impact.

## Density map (hero)

| Zone | Element count | Density |
|------|---------------|---------|
| Main grid | H1 + lead + 5 specs + form (5 fields) | **high** |
| Proof strip | 4 icons | medium |
| Cargo | 6 cards × 3 lines | **high** |

**Total hero sub-elements:** ~20+ distinct messages before scroll.

## What works

- Dark overlay **compresses** visual noise from photo
- `clamp()` type scales H1 without breakpoint explosion
- Spec list uses single-line items — scannable
- Form column **anchors** eye on desktop

## What strains

- Cargo grid adds **six** secondary CTAs — visual noise
- Proof strip duplicates themes (мин. заказ in specs AND proof)
- Red accent on H1 geo span + primary buttons — multiple red focal points

## Specs section density

- Large portrait image (1696×2528) + 5-row dl + CTA + microcopy
- **Effective** for «покажите машину» intent
- **Heavy** on mobile — image stacks above table

## Factory reports cross-ref

- `v5-production-hardening-audit-v1.md` — typography and `min-width: 0` fixes applied
- `v5-word-splitting-and-typography-fix-v1.md` — nbsp discipline reduces rag clutter

## Pack hints needed

| Field | Purpose |
|-------|---------|
| `hero_density_budget` | max interactive elements above fold |
| `cargo_cards_max` | e.g. 4 visible + «ещё» |
| `proof_strip_mode` | social | ops | hybrid (max 3 items) |
| `compactness_tier` | master_hot = dense \| use_case = medium |

## Productive density tradeoff

Master hot **must** qualify broad intent fast — some density is intentional. Destructive density = **competing CTAs without hierarchy** — cargo row borderline.
