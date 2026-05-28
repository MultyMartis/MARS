# Website Factory Visual Contract v0

**Parties:** ORCA (visual semantic intent) → Website Factory (implementation)  
**Bridge:** This contract + section handoff paths — **not** CSS, **not** design tokens

## Factory MUST receive

| Input | Minimum content |
|-------|-----------------|
| Visual semantics bundle | All 15 canonical fields — [schemas/visual-semantics-schema-v0.md](../schemas/visual-semantics-schema-v0.md) |
| `drift_acceptance` | productive listed; destructive empty for build |
| `factory_hints.partial_paths` | Per-section HTML partial paths |
| `data_page_type` | e.g. `ppc-zakaz-manip` |
| Trust + qualification | Explicit `trust_mode`, `qualification_mode` |

## Factory MUST implement

| Requirement | Source field |
|-------------|--------------|
| Hero zoning | `hero_layout_mode` — main / aside / lower |
| Trust mode | `trust_mode` — no silent substitution |
| Compactness | `compactness_level` — list vs paragraph |
| CTA dominance | `cta_weight: primary_dominant` |
| Mobile priority | `mobile_critical` + order hints when provided |
| Proof hierarchy | `proof_priority`, `proof_visibility` |
| Density budget | refuse `overloaded` without override |
| Critical semantics | MODE 1 locks (one machine, no fake hero price) |
| Visual anchors | specs as scannable lines; specs § image when pack says |
| Implementation hints | `factory_hints` object — breakpoints, sticky, caps |

## Factory MUST NOT

- Invent star ratings or review counts
- Reintroduce v4 index hero patterns (`legacy_clutter`)
- Add hero hourly «от … ₽» without approved pricing lock
- Auto-pick `trust_mode` when pack is silent
- Treat blueprint markdown alone as complete handoff

## Factory MAY (productive drift)

When listed in `drift_acceptance.productive`:

- Inline hero form
- v5 bg + overlay
- Cargo cards with secondary CTA style per `cta_weight` rules
- Operational proof strip

## Feedback loop

```text
Factory reports (workspaces/.../reports/)
    → calibration
    → visual-semantics updates
    → next pack/handoff
```

Reports are **not** auto-ingested — human promotes findings.

## Triumph zakaz reference

[examples/triumph-zakaz-hero-visual-semantics-v1.md](../examples/triumph-zakaz-hero-visual-semantics-v1.md)

## SAFE UNKNOWN

CI enforcement of this contract — **not in repo** (validation-cli = PPC export only).
