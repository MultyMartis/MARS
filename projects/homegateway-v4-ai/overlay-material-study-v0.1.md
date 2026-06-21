# HomeGateway v4.ai — overlay material study v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** исследование **overlay surfaces** — architectural glass, translucency, border hierarchy, layered immersion.

**Не является:** overlay component spec, L3 panel HTML, backdrop-filter values.

**Связанные:** [surface-material-language-v0.1.md](surface-material-language-v0.1.md) · [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) · [operational-focus-state-model-v0.1.md](operational-focus-state-model-v0.1.md) · [wireframes/overlay-and-popup-behavior-v0.1.md](wireframes/overlay-and-popup-behavior-v0.1.md)

---

## Overlay material intent

Overlays are **temporary depth** above a dimmed cockpit — operator must still sense tri-focus shell.

| Quality | Target |
|---------|--------|
| **Premium** | Defined edges; readable stack |
| **Restrained** | Neutral glass tint; signal on badge only |
| **Operational** | Panel brighter than backdrop — scan speed |
| **Layered** | Backdrop dim → glass panel → rare sheet |

---

## Glass must feel

| Yes | No |
|-----|-----|
| Architectural instrument panel | Apple clone frosted minimalism |
| Neutral alpha + subtle edge light | Neon cyber glass tint |
| Readable type stack (implied) | Fantasy hologram scanlines |
| Separation via tone + border + elevation | Glow on entire panel perimeter |

Aligns with [surface-material-language-v0.1.md](surface-material-language-v0.1.md).

---

## Overlay immersion (atmospheric)

When overlay opens:

- Cockpit **silhouette preserved** (30–50% dim, not blackout)
- Panel feels **lit in a dimmed room**
- Environment does not compete with panel body
- No fullscreen bloom

---

## Border hierarchy (probe lens)

| Level | Border character |
|-------|------------------|
| Environment | None or ultra-subtle |
| Shell / rail | Low contrast 1px |
| Glass block | `--hg-border` calm |
| Overlay panel | Full definition — clearest border in view |
| Signal | Badge/segment only — not frame rainbow |

---

## Controlled image-generation prompts

---

### OM-01 — Architectural glass panel (neutral)

| Field | Content |
|-------|---------|
| **Purpose** | Baseline overlay panel material |
| **Exploration goal** | Neutral semi-transparent glass with clear edge |
| **Expected emotional result** | Premium instrument; trustworthy readability |
| **Anti-pattern warnings** | No hologram blue; no rainbow refraction |

**Prompt:**

```text
Single abstract architectural glass panel floating in dark calm operational environment, neutral gray-blue translucency, subtle static edge catch-light, premium restrained cockpit material, soft backdrop dim behind, no text, no neon, no Apple-style pure white blur only, no fantasy hologram scanlines, 16:9
```

---

### OM-02 — Dimmed cockpit backdrop

| Field | Content |
|-------|---------|
| **Purpose** | Backdrop atmosphere when overlay open |
| **Exploration goal** | 40% dimmed tri-focus silhouette still readable |
| **Expected emotional result** | Context preserved; focus on panel |
| **Anti-pattern warnings** | No blackout; no blur fog on entire world |

**Prompt:**

```text
Abstract widescreen cockpit environment dimmed to 40% brightness, soft uniform dim overlay, faint left center right spatial zones still visible, one brighter glass panel foreground, calm operational, no modal chaos, no neon, 16:9
```

---

### OM-03 — Layered glass stack

| Field | Content |
|-------|---------|
| **Purpose** | Two glass planes — depth without chaos |
| **Exploration goal** | Rear glass flatter; front glass slightly brighter |
| **Expected emotional result** | Layered intelligence; not clutter |
| **Anti-pattern warnings** | Max two planes in probe; no stack of five |

**Prompt:**

```text
Abstract operational UI material study, two layered architectural glass surfaces at different depth, rear flatter darker front slightly brighter with edge light, deep navy environment, restrained premium, no readable widgets, no cyberpunk, 16:9
```

---

### OM-04 — Overlay border definition

| Field | Content |
|-------|---------|
| **Purpose** | Border as separation cue |
| **Exploration goal** | Thin low-contrast border + slight elevation shadow |
| **Expected emotional result** | Panel «placed» in space |
| **Anti-pattern warnings** | No 3px gamer outline; no animated border |

**Prompt:**

```text
Close abstract study of premium glass overlay panel corner, thin desaturated border line, subtle elevation shadow on dark navy backdrop, architectural operational calm, no RGB border, no glowing perimeter, 16:9
```

---

### OM-05 — Translucency vs readability tension

| Field | Content |
|-------|---------|
| **Purpose** | Find upper bound of glass alpha |
| **Exploration goal** | Glass shows environment hint but remains «solid enough» |
| **Expected emotional result** | Layered; not invisible |
| **Anti-pattern warnings** | No illegible transparency; no frosted white void |

**Prompt:**

```text
Architectural glass operational panel medium translucency showing faint dark environment behind, still feels readable and solid, neutral blue-gray tint, premium cockpit, no text, no hologram effects, no SaaS card shadow only, 16:9
```

---

### OM-06 — Focus light on active panel

| Field | Content |
|-------|---------|
| **Purpose** | Active-state lighting on overlay material |
| **Exploration goal** | Single panel slightly brighter — focus light |
| **Expected emotional result** | Clear focal object |
| **Anti-pattern warnings** | One focal only; no bloom on all panels |

**Prompt:**

```text
Dark operational environment with one raised brighter glass panel focus light, other surfaces muted, restrained cyan accent edge segment only, calm premium aerospace, no pulsing glow, no neon flood, abstract 16:9
```

---

### OM-07 — Sheet layer (rare second overlay)

| Field | Content |
|-------|---------|
| **Purpose** | Denser sheet material above panel |
| **Exploration goal** | Slightly more opaque than parent glass |
| **Expected emotional result** | Serious confirmation layer — still calm |
| **Anti-pattern warnings** | No alert red fullscreen |

**Prompt:**

```text
Abstract two-step overlay material, softer glass layer behind denser more opaque sheet layer foreground, dark calm cockpit dim backdrop, operational premium restraint, no alarm red flood, no modal stack chaos, 16:9
```

---

### OM-08 — Tactical badge on glass (material)

| Field | Content |
|-------|---------|
| **Purpose** | Signal color on glass — bounded area |
| **Exploration goal** | Small amber/red badge on neutral glass row |
| **Expected emotional result** | Semantic light without row flood |
| **Anti-pattern warnings** | Badge <10% row; no full panel tint |

**Prompt:**

```text
Abstract glass tactical instrument row, neutral translucent surface, one small restrained amber status badge edge glow only, row body not colored, calm operational cockpit, no inbox UI, no neon frame, 16:9
```

---

### OM-09 — Anti-hologram negative probe

| Field | Content |
|-------|---------|
| **Purpose** | Confirm rejection of fantasy glass |
| **Exploration goal** | Tool must not add scanlines / rainbow |
| **Expected emotional result** | Fail if hologram clichés appear |
| **Anti-pattern warnings** | Hard fail on scanlines, wireframe mesh, AI brain |

**Prompt:**

```text
Premium architectural operational glass panel only, explicitly without hologram effects, without scanlines, without rainbow refraction, without wireframe mesh, without floating particles, dark calm navy environment, 16:9
```

---

### OM-10 — Overlay immersion full silhouette

| Field | Content |
|-------|---------|
| **Purpose** | End-to-end overlay mood |
| **Exploration goal** | Wide cockpit dim + centered glass overlay zone |
| **Expected emotional result** | «I am still in HG» — station continuity |
| **Anti-pattern warnings** | No new scene behind overlay; same bay |

**Prompt:**

```text
Widescreen abstract operational cockpit with dimmed environment preserving left navigation center work right tactical zones tone, large calm glass overlay panel in center-right work region, premium layered depth, no dashboard card grid, no cyberpunk, no SaaS white, 16:9
```

---

## SAFE UNKNOWN

- Exact blur radius — Phase 3–4 token freeze
- backdrop-filter degrade path — Phase 4

---

*Last updated: 2026-05-24 — Overlay material study.*
