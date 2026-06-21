# HomeGateway v4.ai — tactical darkness study v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** исследование **тактической темноты** — cockpit darkness, ambient depth, restrained lighting, volumetric atmosphere (dark default).

**Не является:** final dark theme tokens, CSS, generated images in-repo.

**Связанные:** [lighting-and-depth-atmosphere-v0.1.md](lighting-and-depth-atmosphere-v0.1.md) · [background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md) · [color-behavior-and-accent-philosophy-v0.1.md](color-behavior-and-accent-philosophy-v0.1.md)

---

## Darkness philosophy

Dark in HG is **immersive cockpit bay** — not void, not nightclub, not gamer cave.

| Principle | Meaning |
|-----------|---------|
| **Layered blacks** | Navy → charcoal steps; corners slightly deeper |
| **Volumetric atmosphere** | Soft falloff; overhead instrument wash |
| **Restrained tactical glow** | Signal badges only — not panel bloom |
| **Ambient depth** | 2–3 planes before glass instruments |
| **Calm-control** | Darkness supports focus; does not oppress |

Operator feeling: *night operations at a capable station* — not *sci-fi movie trailer*.

---

## Cockpit darkness vs pure black void

| Cockpit darkness | Pure void (forbidden) |
|------------------|------------------------|
| Readable glass edges | Lost panel boundaries |
| Environmental geometry at 3–8% | Nothing — #000 only |
| Subtle top-down light bias | Flat OLED crush |
| Peripheral rail still scannable | Rail disappears |

---

## Allowed

- Deep layered blacks (navy, blue-gray charcoal)
- Subtle gradients (low contrast)
- Atmospheric shadows (soft, large scale)
- Restrained tactical glow on **badges** only
- Static ultra-fine grain (optional)
- Faint structural lines / arcs at low opacity

---

## Forbidden

- Pure black void (#000 everywhere)
- RGB neon accents
- Cyberpunk overload (magenta+cyan chaos)
- Gamer darkness (RGB underglow, carbon textures)
- Starscape / space window
- Bloom on every panel
- Matrix rain / hex spam

---

## Controlled image-generation prompts

Use with external tools. Each probe: one question only.

---

### TD-01 — Volumetric cockpit bay (baseline)

| Field | Content |
|-------|---------|
| **Purpose** | Establish default dark environmental volume |
| **Exploration goal** | Layered navy-charcoal depth without narrative scene |
| **Expected emotional result** | Calm immersion; operator «inside» a station |
| **Anti-pattern warnings** | No stars, no ship windows, no pure #000 void, no neon |

**Prompt:**

```text
Widescreen abstract operational cockpit environment, deep layered navy and charcoal gradients, soft volumetric darkness with faint cool overhead light wash, subtle large-scale geometric hints at 4% opacity, calm premium aerospace atmosphere, no UI widgets, no stars, no neon, no cyberpunk, no text, cinematic restraint not movie overload, 16:9
```

---

### TD-02 — Corner falloff depth

| Field | Content |
|-------|---------|
| **Purpose** | Test peripheral depth cues (bay corners) |
| **Exploration goal** | Corners slightly darker than center — spatial enclosure |
| **Expected emotional result** | Grounded station; subtle spatial memory |
| **Anti-pattern warnings** | No vignette spotlight on center; no horror darkness |

**Prompt:**

```text
Abstract dark operational workspace atmosphere, gentle corner falloff darker than center, cool blue-gray volumetric shadows, minimal ambient geometry lines, calm mission-control mood, premium restrained, no characters, no space scenery, no RGB, no dashboard cards, 16:9
```

---

### TD-03 — Restrained tactical glow spot

| Field | Content |
|-------|---------|
| **Purpose** | Validate signal glow discipline in dark bay |
| **Exploration goal** | Single small amber or red accent glow in periphery only |
| **Expected emotional result** | Quiet alert — awareness without panic |
| **Anti-pattern warnings** | No full-screen red; no bloom spam; no pulsing |

**Prompt:**

```text
Dark calm cockpit bay background, deep navy layers, one very small restrained amber warning light accent in far periphery suggesting instrument edge, 95% of frame neutral dark atmosphere, architectural precision, no HUD text, no neon cyan magenta, no gamer RGB, no alert flood, 16:9
```

---

### TD-04 — Glass instrument silhouette (abstract)

| Field | Content |
|-------|---------|
| **Purpose** | Darkness behind architectural glass panels |
| **Exploration goal** | Dark environment + faint glass edge catch-light |
| **Expected emotional result** | Instruments forward; room recedes |
| **Anti-pattern warnings** | No hologram scanlines; no Apple frosted white minimalism only |

**Prompt:**

```text
Layered dark operational environment with abstract semi-transparent architectural glass panels, subtle static edge catch-light, deep navy background, restrained futuristic intelligence, premium cockpit materials, no fantasy hologram effects, no SaaS white cards, no readable UI text, 16:9
```

---

### TD-05 — Deep surface recess

| Field | Content |
|-------|---------|
| **Purpose** | Test inset / deep surface tonal step |
| **Exploration goal** | Lower contrast recessed plane behind brighter glass layer |
| **Expected emotional result** | Depth hierarchy without clutter |
| **Anti-pattern warnings** | No skeuomorphic metal; no busy texture |

**Prompt:**

```text
Abstract dark UI atmosphere study, two tonal planes deep inset recess behind slightly brighter glass layer, charcoal and navy, soft shadows, operational calm, minimal geometry, no widgets, no cyberpunk grid, no flat pure black, 16:9
```

---

### TD-06 — Ambient geometry discipline

| Field | Content |
|-------|---------|
| **Purpose** | Large-scale structural hints at low opacity |
| **Exploration goal** | Suggest architecture without blueprint clutter |
| **Expected emotional result** | Intelligent environment; not decoration |
| **Anti-pattern warnings** | No honeycomb spam; no matrix digits |

**Prompt:**

```text
Dark volumetric cockpit atmosphere, very faint large-scale arc and line geometry at 3% opacity, cool desaturated blue-gray, calm operational premium feel, environmental depth not wallpaper art, no tessellation spam, no sci-fi city, no neon, 16:9
```

---

### TD-07 — Top-down instrument wash

| Field | Content |
|-------|---------|
| **Purpose** | Overhead lighting logic from [lighting-and-depth-atmosphere-v0.1.md](lighting-and-depth-atmosphere-v0.1.md) |
| **Exploration goal** | Faint cool gradient top brighter → bottom darker |
| **Expected emotional result** | MFD / instrument bay readability metaphor |
| **Anti-pattern warnings** | No stage spotlight; no lens flare |

**Prompt:**

```text
Abstract dark mission control environment lighting, soft cool top-down ambient wash on deep navy charcoal volume, subtle premium aerospace, extremely restrained, no lens flare, no sun rays, no space background, no UI mockup, 16:9
```

---

### TD-08 — Dark calm vs cyberpunk (contrast probe)

| Field | Content |
|-------|---------|
| **Purpose** | Negative control — confirm filters reject cyber drift |
| **Exploration goal** | Same composition language but **must fail** evaluation if tool adds neon |
| **Expected emotional result** | N/A — use to test evaluation discipline |
| **Anti-pattern warnings** | If output has cyan-magenta neon → hard fail |

**Prompt (intentionally strict negatives):**

```text
Dark operational cockpit atmosphere ONLY, volumetric navy charcoal, calm premium, explicitly without cyberpunk, without neon cyan magenta, without hex grid, without glitch, without gamer RGB, without movie HUD, environmental abstract 16:9
```

---

### TD-09 — Session fatigue check (minimal motion static)

| Field | Content |
|-------|---------|
| **Purpose** | Static darkness for long-session calibration |
| **Exploration goal** | Zero narrative motion; ultra-stable grain |
| **Expected emotional result** | Boring in good way — sustainable 30+ min |
| **Anti-pattern warnings** | No particles; no starfield drift |

**Prompt:**

```text
Completely static abstract dark operational workspace environment, layered deep navy charcoal gradients only, ultra subtle film grain, no particles, no animation implied, no stars, calm professional station mood, 16:9
```

---

### TD-10 — Tri-focus silhouette in dark (abstract)

| Field | Content |
|-------|---------|
| **Purpose** | Darkness supporting left-center-right roles |
| **Exploration goal** | Three vertical zones of tonal calm — nav / work / rail |
| **Expected emotional result** | Spatial orientation without literal UI |
| **Anti-pattern warnings** | No equal three card columns; abstract tone only |

**Prompt:**

```text
Abstract widescreen dark cockpit spatial composition, three vertical tonal zones suggesting navigation left work center tactical right periphery, deep calm navy atmosphere, subtle glass hints center, peripheral slightly denser tone right, no literal dashboard cards, no neon, premium operational, 16:9
```

---

## Study exit notes

When ≥2 prompts pass evaluation, extract:

- Base tone family (navy vs charcoal bias)
- Gradient direction (top-down vs corner falloff)
- Maximum glow area (% of frame)
- Geometry opacity ceiling

Feed into theme token review — not direct hex from images.

---

## SAFE UNKNOWN

- OLED true black vs lifted black — operator display dependent
- Starfield micro-dots — borderline; default **avoid**

---

*Last updated: 2026-05-24 — Tactical darkness study.*
