# HomeGateway v4.ai — environmental depth study v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** **ambient backgrounds** — spatial depth, environmental atmosphere, layered environment systems.

**Не является:** WebGL spec, video loops, committed image assets.

**Связанные:** [background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md) · [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) · [lighting-and-depth-atmosphere-v0.1.md](lighting-and-depth-atmosphere-v0.1.md)

---

## Canonical assertion (repeated)

> **Background is NOT wallpaper.**  
> **Background IS** atmospheric environmental layer.

The environment is the **room** the cockpit inhabits — P3, non-interactive, viewport-fixed.

---

## Environmental depth system (layers)

```text
Plane A — base tone (--hg-bg family)
Plane B — mid volumetric gradient / soft geometry
Plane C — faint light accents / grain (optional)
        ↓
Layer 2+ shell and instruments (P1–P2)
```

| Plane | Motion budget |
|-------|---------------|
| A–C | Static preferred; 60s+ drift max if any |
| Shell+ | Per motion charter |

---

## Explore

| Element | Guideline |
|---------|-----------|
| **Volumetric gradients** | Large soft steps — low contrast |
| **Subtle geometry** | Arcs, lines, grid hints — large scale |
| **Ambient fog** | Very soft — not obscuring UI |
| **Structural depth** | Suggests bay — not blueprint |
| **Faint environmental movement** | Ultra-slow optional — `pointer-events: none` |

---

## Forbidden

- Stars, galaxies, space vistas
- Spaceship windows, planet horizons
- Sci-fi landscapes, city skylines
- Wallpaper art, brand photography
- Matrix rain, hex spam, gamer RGB environments
- Fast parallax, video loops (v0.1)

---

## Relationship to viewport

[viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md): environment **does not scroll** with `main_area` content.

---

## Controlled image-generation prompts

---

### ED-01 — Layered environment stack (dark)

| Field | Content |
|-------|---------|
| **Purpose** | Three-plane dark environment |
| **Exploration goal** | Base + mid gradient + faint geometry |
| **Expected emotional result** | Depth without narrative |
| **Anti-pattern warnings** | No stars; no landscape |

**Prompt:**

```text
Abstract dark environmental background only three depth planes deep navy base soft mid gradient faint large geometry 3% opacity, atmospheric operational layer not wallpaper, no stars no spaceship window no city photo, 16:9
```

---

### ED-02 — Volumetric gradient (no geometry)

| Field | Content |
|-------|---------|
| **Purpose** | Pure tonal depth |
| **Exploration goal** | Gradient-only environment |
| **Expected emotional result** | Calm bay — minimal noise |
| **Anti-pattern warnings** | Not flat void; still stepped tones |

**Prompt:**

```text
Abstract volumetric dark navy charcoal gradient environment only, soft corner falloff, calm premium operational atmosphere, no objects no scenery no UI, 16:9
```

---

### ED-03 — Subtle structural geometry

| Field | Content |
|-------|---------|
| **Purpose** | Architectural hint discipline |
| **Exploration goal** | Large arcs/lines — low opacity |
| **Expected emotional result** | Intelligent space |
| **Anti-pattern warnings** | No honeycomb; no blueprint clutter |

**Prompt:**

```text
Abstract dark environment with very faint large-scale arc and line structural hints low opacity, cool blue-gray, operational cockpit bay not technical blueprint, no hex spam no matrix, 16:9
```

---

### ED-04 — Ambient fog layer

| Field | Content |
|-------|---------|
| **Purpose** | Soft fog between planes |
| **Exploration goal** | Gentle haze separating depth |
| **Expected emotional result** | Atmospheric separation |
| **Anti-pattern warnings** | Fog must not obscure UI zone |

**Prompt:**

```text
Abstract dark operational environment soft ambient fog between depth planes, very subtle haze, premium calm, no sci-fi planet fog, no horror mist, background layer only 16:9
```

---

### ED-05 — Static grain texture

| Field | Content |
|-------|---------|
| **Purpose** | Ultra-fine grain on environment |
| **Exploration goal** | Material richness without pattern noise |
| **Expected emotional result** | Premium finish |
| **Anti-pattern warnings** | No heavy TV static |

**Prompt:**

```text
Abstract dark navy environment with ultra subtle static film grain texture only, calm operational, no animated noise, no particles, 16:9
```

---

### ED-06 — Ultra-slow drift (implied still)

| Field | Content |
|-------|---------|
| **Purpose** | Test if still image suggests motion sickness |
| **Exploration goal** | Composition that could animate 60s+ period |
| **Expected emotional result** | Barely alive — not distracting |
| **Anti-pattern warnings** | Do not generate fast motion in tool |

**Prompt:**

```text
Abstract dark layered environment completely static composition suitable for imperceptibly slow parallax, calm premium, no stars no particles no speed lines, 16:9
```

---

### ED-07 — Light theme environmental depth

| Field | Content |
|-------|---------|
| **Purpose** | Layered light environment |
| **Exploration goal** | Cool white planes + faint geometry |
| **Expected emotional result** | Tactical daylight room |
| **Anti-pattern warnings** | No flat white void |

**Prompt:**

```text
Abstract light environmental background layered cool off-white planes faint geometry 2% opacity, tactical daylight atmosphere, not wallpaper not CRM, no warm beige, 16:9
```

---

### ED-08 — Anti-wallpaper negative probe

| Field | Content |
|-------|---------|
| **Purpose** | Reject narrative scenes |
| **Exploration goal** | Fail if space/landscape appears |
| **Expected emotional result** | Filter discipline |
| **Anti-pattern warnings** | Hard fail stars, planets, windows |

**Prompt:**

```text
Abstract operational cockpit environment layer ONLY, explicitly no wallpaper art, no space scene, no landscape, no spaceship interior window, volumetric tone and subtle geometry only, 16:9
```

---

### ED-09 — Environment behind glass (context)

| Field | Content |
|-------|---------|
| **Purpose** | See environment through glass hint |
| **Exploration goal** | Background visible at 5% through panel edge |
| **Expected emotional result** | Coherent stack |
| **Anti-pattern warnings** | Glass area tiny — environment doc focus |

**Prompt:**

```text
Abstract dark environment with edge of architectural glass panel showing faint background depth through translucency, layered operational atmosphere, no hologram, 16:9
```

---

### ED-10 — Focus mode environment dim

| Field | Content |
|-------|---------|
| **Purpose** | Environment recedes further in focus work |
| **Exploration goal** | Slightly darker/muted planes — center forward |
| **Expected emotional result** | Depth supports focus |
| **Anti-pattern warnings** | Not black hole center |

**Prompt:**

```text
Abstract dark environmental layers slightly muted darker than center work zone glow, calm depth recession, operational focus atmosphere, no void black center, 16:9
```

---

## Implementation note (non-binding)

CSS gradients + pseudo-elements preferred v0.1 — see [background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md).

---

## SAFE UNKNOWN

- Starfield micro-dots — default avoid
- Per-mode environment variants — likely unified first

---

*Last updated: 2026-05-24 — Environmental depth study.*
