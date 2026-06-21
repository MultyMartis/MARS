# HomeGateway v4.ai — visual language direction v0.1

**Статус:** **DRAFT** · **PLANNING** · **POST-PROTOTYPE** (Phase 3 charter)  
**Назначение:** каноническое **визуальное направление** — tactical calm, premium aerospace, anti-patterns.

**Не является:** final Figma, pixel spec, font files.

**Связанные:** [visual-direction-exploration-pack-v0.1.md](visual-direction-exploration-pack-v0.1.md) (master pack) · [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md) · [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md) · [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md)

---

## Identity in one line

**Tactical calm · premium aerospace · ambient intelligence · layered operational environment.**

---

## What HG should feel like

| Quality | Expression |
|---------|------------|
| **Tactical calm** | Signals visible, atmosphere steady |
| **Premium aerospace** | Precision, depth, restrained accent — cockpit / mission control |
| **Ambient intelligence** | Environment suggests awareness, not chatbot mascot |
| **Layered** | Background → glass surfaces → raised focus |
| **Operational** | Readable 30+ min sessions |
| **Readable** | Contrast on glass; no illegible glow |
| **Atmospheric** | Subtle depth, not flat SaaS |
| **Restrained** | Motion and color earn attention |

---

## What HG must NOT become

| Forbidden direction | Why |
|---------------------|-----|
| **SaaS dashboard** | Generic cards, Inter-only sameness |
| **CRM** | Pipeline columns, deal stages |
| **Enterprise admin** | Gray tables dominating |
| **Cyberpunk toy** | Neon overload, illegible HUD |
| **RGB gamer UI** | Rainbow borders, pulsing everything |
| **Fantasy hologram** | Scanlines, fake 3D holograms, magic particles |
| **Noisy widget wall** | 20 equal widgets |
| **Movie fantasy UI** | Style over scan speed |

---

## Anti-SaaS · anti-cyberpunk · anti-gamer (summary)

```text
Prefer                          Avoid
────────────────────────────────────────────────────────
Spatial zones                   Equal card grid
Signal hierarchy                Vanity metrics
Glass + readable type           Pure transparency
One accent family               Full RGB spectrum
Calm dark default               Blinking alerts
Operator station                Team collaboration tropes
```

---

## Background philosophy

| Layer | Direction |
|-------|-----------|
| **Environmental depth** | Gradients, subtle starfield or grid — **low contrast** |
| **Atmospheric layers** | 2–3 depth planes, parallax optional ultra-slow |
| **Subtle geometry** | Lines, arcs, hex hints — not busy tessellation |
| **Ambient space** | Negative space is feature |
| **Restrained motion** | 60s+ periods or static ([motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md)) |

Background supports **calm-control** — never competes with P1 content ([information-priority-model-v0.1.md](information-priority-model-v0.1.md)).

---

## Surfaces (block-screens)

- **Glass** semantics via `--hg-surface-glass` — not invisible panels.
- **Borders** subtle — see [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md).
- **Glow** rare — elevation token only.
- Sci-fi inspiration **without** illegibility ([block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md)).

---

## Typography direction (draft)

| Level | Use |
|-------|-----|
| Display / zone titles | Compact, medium weight |
| Block titles | Semi-bold |
| Body | Regular, high legibility |
| Meta / dates | Muted secondary |

**Canonical family (Phase 3):** **Exo 2** — operational, aerospace-leaning, calm; see [typography-atmosphere-v0.1.md](typography-atmosphere-v0.1.md). Sci-fi display fonts forbidden for body.

---

## Color direction

Semantic tokens only — [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md).

| Role | Direction |
|------|-----------|
| Accent | Cyan / electric blue **restrained** |
| Background | Deep navy / charcoal (dark) |
| Signals | Distinct INFO→OVERDUE ladder |
| Danger | Separate from OVERDUE label confusion |

Light theme: desaturated signals, maintained contrast.

---

## Iconography

- Functional, consistent stroke weight.
- Signal icons duplicate color meaning.
- No cartoon mascots for MARS/bots.

---

## Reference mood (non-binding)

Mission control · modern aircraft MFD · premium tools UI — **not** game HUD, **not** Notion clone.

---

## Relationship to prototype v0.1

Operator review confirmed: **spatial cockpit** beats dashboard grid. Visual direction must **serve** tri-focus architecture ([cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md)).

---

## Visual Direction Exploration Pack (v0.1)

Full crystallization — Lane B:

| Doc | Topic |
|-----|-------|
| [visual-direction-exploration-pack-v0.1.md](visual-direction-exploration-pack-v0.1.md) | Master pack + pillars |
| [visual-dna-and-identity-v0.1.md](visual-dna-and-identity-v0.1.md) | Emotional DNA |
| [surface-material-language-v0.1.md](surface-material-language-v0.1.md) | Materials / glass |
| [background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md) | Environment layer |
| [lighting-and-depth-atmosphere-v0.1.md](lighting-and-depth-atmosphere-v0.1.md) | Light + depth |
| [color-behavior-and-accent-philosophy-v0.1.md](color-behavior-and-accent-philosophy-v0.1.md) | Operational color |
| [typography-atmosphere-v0.1.md](typography-atmosphere-v0.1.md) | Exo 2 atmosphere |
| [motion-atmosphere-v0.1.md](motion-atmosphere-v0.1.md) | Motion mood |
| [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md) | Visual dangers |
| [reference-analysis-and-visual-boundaries-v0.1.md](reference-analysis-and-visual-boundaries-v0.1.md) | Reference filter |

---

## SAFE UNKNOWN

- Reference board image assets — operator-curated; filter rules in reference doc.
- Logo / wordmark final — TBD.
- Illustration vs pure CSS atmosphere — implementation choice.

---

*Last updated: 2026-05-24 — Visual language direction; links Visual Direction Exploration Pack v0.1.*
