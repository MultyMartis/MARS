# HomeGateway v4.ai — surface material language v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** канон **материалов и поверхностей** — иерархия, стекло, границы, blur, тактические и фокусные surfaces.

**Не является:** CSS, component library, Figma components.

**Связанные:** [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md) (interaction states) · [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) · [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md)

---

## Material intent

Surfaces in HG read as **architectural instrument panels** in a calm cockpit — layered, readable, restrained. Materials support **spatial tri-focus**, not decorative card stacks.

---

## Surface taxonomy

| Surface class | Role | Typical zones | Layer (z) |
|---------------|------|---------------|-----------|
| **Primary surfaces** | Main structural panels — shell rails, `top_bar` base | `main_menu`, `info_area`, `top_bar` | surfaces (2) |
| **Secondary surfaces** | Block-screens at rest; standard work panels | `main_area` blocks | surfaces (2) |
| **Deep surfaces** | Canvas-adjacent; lower contrast inset regions | Background-adjacent strips, calm zones | surfaces (2), flatter |
| **Glass layers** | Semi-transparent operational panels | block-screens, overlays (partial) | surfaces / raised |
| **Overlay surfaces** | L3 panels above dimmed cockpit | project detail, confirms | overlays (4–5) |
| **Tactical surfaces** | Signal rows, level badges, rail chrome | `info_area` | surfaces; semantic tokens |
| **Focused surfaces** | Selected mode, active block, overlay target | selected nav, raised block | raised-surfaces (3) |

---

## Primary surfaces

| Aspect | Rule |
|--------|------|
| **Purpose** | Define cockpit skeleton — stable across modes |
| **Density** | Slightly denser than glass blocks — legible chrome |
| **Motion** | Minimal — shell static on mode switch |
| **Border** | Subtle `--hg-border`; no neon frame |

`top_bar` = **calm-control band** — primary surface, optional raised edge.

---

## Secondary surfaces (block-screens)

| Aspect | Rule |
|--------|------|
| **Default** | `--hg-surface-glass` + backdrop blur (graceful degrade) |
| **Feel** | Instrument on glass, not floating SaaS card |
| **Elevation** | Surface default; raised on hover/select |
| **Size** | S/M/L/XL per taxonomy — material consistent across sizes |

---

## Deep surfaces

| Aspect | Rule |
|--------|------|
| **Use** | Recess content that must not compete with P1 |
| **Contrast** | Lower than secondary; inset shadow optional |
| **Anti-pattern** | Deep surface that looks disabled without `disabled` state |

---

## Glass layers

### Glass should feel

| Quality | Expression |
|---------|------------|
| **Restrained** | Alpha 6–12% (dark draft); not invisible |
| **Architectural** | Clear edge, readable type on top |
| **Layered** | Stack readable: bg → glass → raised focus |

### Glass must NOT feel

| Anti-quality | Why |
|--------------|-----|
| **Apple clone** | Frosted white minimalism without cockpit depth |
| **Neon cyber glass** | Colored glass tint + glow borders |
| **Fantasy hologram** | Scanlines, rainbow refraction, fake depth parallax on every panel |

**Rule:** glass tints **neutral** — signal color on badges/edges, not full panel wash.

---

## Overlay surfaces

| Type | Material |
|------|----------|
| **Backdrop** | Dim + optional blur; preserves cockpit silhouette |
| **Panel** | Denser glass or opaque surface — **readable** over dim |
| **Sheet (rare)** | One step denser; max stack per depth charter |

Overlay material **separates** from canvas — border + shadow, not only opacity.

---

## Tactical surfaces

| Element | Material rule |
|---------|---------------|
| Signal row | Glass or flat row; semantic **badge/edge** only |
| Section header | Muted typography; sticky OVERDUE band restrained |
| Rail chrome | Primary surface; internal scroll fade masks |

CRITICAL row ≠ entire panel red flood — see [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md).

---

## Focused surfaces

| Context | Material |
|---------|----------|
| Selected nav | Accent left bar **or** accent border — one cue |
| Active block | Slightly denser glass + raised elevation |
| Keyboard focus | Focus ring `--hg-accent` — WCAG intent |
| Overlay-open | `main_area` dimmed 30–50%; legibility preserved |

---

## Texture philosophy

| Allowed | Forbidden |
|---------|-----------|
| Ultra-subtle noise/grain on background | Busy textures on block-screens |
| Static edge catch-light on glass | Skeuomorphic metal brushes |
| Matte operational finish | Leather, wood, gamer carbon fiber |

Texture lives primarily in **environment layer** ([background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md)).

---

## Border philosophy

| Rule | Detail |
|------|--------|
| Default | 1px `--hg-border` — low contrast |
| Hover | Brighten or accent mix — thin |
| Selected | Accent segment or left rail — **one** cue |
| Signal | Badge or edge segment — not full perimeter neon |
| Overlay | Full definition on panel; inactive regions unchanged border |

**Anti:** animated border crawl, rainbow borders, 3px gamer outlines.

---

## Translucency philosophy

| Layer | Translucency |
|-------|--------------|
| Background | Opaque environmental stack |
| Glass blocks | Alpha + blur; text always on opaque enough stack |
| Overlay panel | Higher opacity than canvas blocks |
| Tactical badge | Opaque for readability |

**Never** sacrifice body text contrast for «more glass».

---

## Blur philosophy

| Use | Rule |
|-----|------|
| block-screen glass | `backdrop-filter` with fallback solid |
| Overlay backdrop | Light blur optional — performance aware |
| Background | **No** heavy blur on full viewport behind everything |

Blur = **separation cue**, not aesthetic fog.

---

## Surface separation

```text
[ deep environment ]
    [ primary shell — nav | center | rail ]
        [ glass instruments — blocks ]
            [ raised — hover / selected ]
                [ overlay panel ]
```

Separation via: **tone step** + **border** + **elevation** — not only shadow.

---

## Material hierarchy (summary)

| Priority | Material loudness |
|----------|-------------------|
| P0 signal badge | Semantic color — small area |
| P1 active block | Standard glass + optional raise |
| P2 secondary block | Muted glass |
| P3 chrome / ambient | Primary/deep surfaces quiet |
| Environment | Lowest contrast |

Aligns with [information-priority-model-v0.1.md](information-priority-model-v0.1.md).

---

## Relationship to interaction states

Material **rests** in default; [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md) defines hover, critical, overlay-open transitions on top of this language.

---

## SAFE UNKNOWN

- Exact `--hg-glass-alpha` per theme — Phase 3 token freeze.
- backdrop-filter support policy for old browsers — degrade path Phase 4.
- Whether `info_area` uses denser primary vs glass — operator preference TBD.

---

*Last updated: 2026-05-24 — Surface material language.*
