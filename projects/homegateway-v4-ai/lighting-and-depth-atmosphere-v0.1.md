# HomeGateway v4.ai — lighting and depth atmosphere v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** канон **света и глубины** — как освещение направляет внимание и создаёт ощущение кокпита.

**Не является:** HDR rendering spec, Three.js scene, pixel-perfect mockups.

**Связанные:** [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) · [surface-material-language-v0.1.md](surface-material-language-v0.1.md) · [background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md)

---

## Lighting intent

Light in HG is **functional atmosphere** — it separates layers, elevates focus, and carries signal meaning. It is not decoration, bloom showcase, or cyberpunk neon.

> **Restrained lighting is critical** — over-lit interfaces destroy calm-control and glass legibility.

---

## How light guides attention

| Mechanism | Attention effect |
|-----------|------------------|
| **Brighter raised surface** | Hover / selected block draws foveal scan |
| **Accent edge catch** | Selected nav, focus ring |
| **Signal light** | Badge / segment — semantic only |
| **Environmental wash** | Peripheral orientation — P3 |
| **Overlay contrast** | Panel brighter than dimmed cockpit |

Light follows **P0–P3** — never all layers equally bright.

---

## How depth creates cockpit feeling

| Depth cue | Cockpit reading |
|-----------|-----------------|
| Environment recedes | Operator inside a volume |
| Glass instruments forward | Tools within reach |
| Raised focus nearest | Active work highlighted |
| Overlay above station | Temporary depth without losing shell memory |

Maps to z-stack ([depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md)):

```text
0 background          — darkest / most recessive
1 ambient-effects     — non-interactive light accents
2 surfaces            — instrument base
3 raised-surfaces     — active emphasis
4–5 overlays          — lit panel in dimmed room
6 tactical-alerts       — chip visibility, not flood
7 modal-priority      — brief focal peak
```

---

## Depth behavior (rules)

| Rule | Detail |
|------|--------|
| **Few named layers** | No ad-hoc z-index lighting |
| **One elevation focal** | Per viewport region max one strong glow |
| **Parallax subtle** | Depth planes optional; slow |
| **Dimming ≠ darkness** | overlay-open preserves legibility 30–50% |

---

## Surface illumination

| Surface type | Illumination |
|--------------|--------------|
| Primary shell | Soft top-down bias — slightly brighter top edge |
| Glass block | Edge catch-light static; interior even |
| Deep inset | Reduced ambient — recess |
| Tactical row | Row neutral; **badge** lit by signal token |
| `top_bar` | Calm uniform — not spotlight theater |

---

## Active-state lighting

| State | Light behavior |
|-------|----------------|
| hover | Border brighten + optional `--hg-elevation` |
| selected | Accent edge or left rail — single cue |
| focus (keyboard) | Accent ring — accessibility |
| critical row | Signal token on badge — **not** full panel bloom |
| overlay-open | Backdrop dim; panel normally lit |

**No** pulsing active-state loops.

---

## Overlay separation

| Element | Lighting |
|---------|----------|
| Backdrop | Multiply/dim cockpit — silhouette preserved |
| Panel | Full readability — opaque enough stack |
| Sheet (rare) | Slightly brighter than parent panel |

Operator must still sense **where** they are in tri-focus under dim.

---

## Tactical glow

| Allowed | Forbidden |
|---------|-----------|
| Micro-glow on CRITICAL badge | Whole-panel red glow |
| `--hg-elevation` on one raised block | Glow on every nav item |
| Global OVERDUE chip readable | Full-screen red alert layer |

**Tactical glow** = signal semantics + rare elevation — not RGB FX.

---

## Environmental lighting

| Type | Role |
|------|------|
| **Overhead wash** | Faint cool gradient top → darker bottom |
| **Structural accents** | Edge lines catching virtual light |
| **Corner falloff** | Volumetric depth |

Environmental light stays **layer 0–1** — never outshines P1 text.

---

## Light type taxonomy (canonical)

| Light type | Purpose | Typical carrier |
|------------|---------|-----------------|
| **Ambient light** | Room tone; orientation P3 | Background gradient, shell base |
| **Focus light** | Active work emphasis | Raised block, selected nav |
| **Signal light** | Semantic level visibility | INFO→OVERDUE tokens |
| **Critical-state light** | P0 emphasis — restrained | CRITICAL/OVERDUE badge, top chip |

### Ambient light

- Default state of cockpit — calm, even, low contrast motion.
- `system_status`, background hints.

### Focus light

- Draws eye to `main_area` active instrument or overlay panel.
- Earned by selection — not constant on all blocks.

### Signal light

- Color from semantic tokens only ([color-behavior-and-accent-philosophy-v0.1.md](color-behavior-and-accent-philosophy-v0.1.md)).
- Never used for decoration.

### Critical-state light

- Strongest signal illumination — still **bounded area**.
- No fullscreen bloom; no blink.

---

## Forbidden lighting patterns

| Pattern | Why forbidden |
|---------|---------------|
| **Bloom spam** | Legibility loss; demo aesthetic |
| **Neon glow everywhere** | Cyberpunk toy; fatigue |
| **Over-lit interfaces** | Flatten depth; anxiety |
| **Rim light on every card** | Dashboard equal emphasis |
| **Animated light sweeps** | Movie prop UI |

---

## Dark vs light lighting posture

| Theme | Lighting posture |
|-------|------------------|
| **Dark** | Volumetric; instruments lit in bay |
| **Light** | Flattened volume; stronger borders; softer shadows |

Both maintain **signal light** discipline.

---

## Relationship to motion charter

Ambient light motion (if any) follows [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md) — 60s+ or static.

Emotional layer: [motion-atmosphere-v0.1.md](motion-atmosphere-v0.1.md).

---

## SAFE UNKNOWN

- Exact shadow spread values — Phase 3 token freeze.
- Whether light theme uses stronger borders vs shadows — A/B at static MVP.
- HDR/wide-gamut displays — no special case v0.1.

---

*Last updated: 2026-05-24 — Lighting and depth atmosphere.*
