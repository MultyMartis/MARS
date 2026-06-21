# HomeGateway v4.ai — Visual Direction Exploration Pack v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B — visual direction / cockpit atmosphere architecture  
**Назначение:** мастер-документ **кристаллизации визуального языка** HG — DNA, атмосфера, материалы, свет, цвет, типографика, motion, anti-patterns, границы референсов.

**Не является:** frontend-кодом, production UI, финальными mockup, Figma, design tokens implementation, runtime/orchestration.

**Связанные (spatial + interaction canon):** [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) · [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md) · [visual-language-direction-v0.1.md](visual-language-direction-v0.1.md) · [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md) · [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) · [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md)

---

## Pack scope (v0.1)

| # | Document | Role |
|---|----------|------|
| 1 | **This file** | Master visual direction — pillars, psychology, entry |
| 2 | [visual-dna-and-identity-v0.1.md](visual-dna-and-identity-v0.1.md) | Emotional DNA, operator-centric identity |
| 3 | [surface-material-language-v0.1.md](surface-material-language-v0.1.md) | Surfaces, glass, borders, hierarchy |
| 4 | [background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md) | Atmospheric environment — not wallpaper |
| 5 | [lighting-and-depth-atmosphere-v0.1.md](lighting-and-depth-atmosphere-v0.1.md) | Light types, depth, cockpit illumination |
| 6 | [color-behavior-and-accent-philosophy-v0.1.md](color-behavior-and-accent-philosophy-v0.1.md) | Operational color, accents, themes |
| 7 | [typography-atmosphere-v0.1.md](typography-atmosphere-v0.1.md) | Exo 2 operational typography atmosphere |
| 8 | [motion-atmosphere-v0.1.md](motion-atmosphere-v0.1.md) | Emotional motion layer (charter = timing) |
| 9 | [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md) | Visual danger doctrine |
| 10 | [reference-analysis-and-visual-boundaries-v0.1.md](reference-analysis-and-visual-boundaries-v0.1.md) | How to filter inspiration |

**Phase boundary:** visual language crystallization only. Token freeze and HTML remain Phase 3–4 ([roadmap-v0.1.md](roadmap-v0.1.md)).

---

## Canonical visual identity (one line)

> **Calm operational environment for a human operator managing a living AI/web ecosystem** — premium aerospace cockpit, restrained futuristic intelligence, layered atmospheric workspace.

**Not:** a flashy futuristic interface demo.

---

## Visual identity pillars

| Pillar | Meaning in HG |
|--------|----------------|
| **Tactical calm** | Signals visible; atmosphere steady; no alert theater |
| **Premium aerospace** | Precision, depth, restrained accent — mission control / MFD sensibility |
| **Restrained futuristic** | Technology-forward without sci-fi costume or gamer RGB |
| **Ambient intelligence** | Environment suggests awareness — not chatbot mascot or fake AI glow |
| **Layered operational depth** | Background → glass surfaces → raised focus → overlay ([depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md)) |
| **Atmospheric workspace** | Room-like station; negative space and depth are features |
| **Calm-control** | Chrome quiet; activity localized; long-session ergonomics |
| **Cockpit spatiality** | Tri-focus zones persist; vision uses periphery ([cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md)) |

---

## Why HG is not a dashboard

| Dashboard trap | HG cockpit answer |
|----------------|-------------------|
| Equal card grid | **Spatial roles** — nav / work / tactical periphery |
| Vanity metrics wall | **Operational work** in `main_area` |
| Scroll-the-page overview | **Viewport-first** station ([viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md)) |
| Notification center | **`info_area`** = tactical awareness, not inbox |
| Everything shouts | **P0–P3** attention discipline ([information-priority-model-v0.1.md](information-priority-model-v0.1.md)) |

Dashboard optimizes **comparison of widgets**. HG optimizes **operator posture in space**.

Post–Prototype v0.1: operator review confirmed **spatial cockpit** beats dashboard-grid reading.

---

## Why HG is not a «sci-fi toy»

| Sci-fi toy trap | HG restraint |
|-----------------|--------------|
| Neon HUD overload | Semantic signal colors only |
| Hologram clichés | Architectural glass, not fantasy projection |
| Starscape / ship window wallpaper | Environmental depth without literal scene |
| Bloom and glow spam | Rare elevation; one focal glow per region |
| Movie prop aesthetics | Scan speed and readability over style flex |

Sci-fi **inspiration** is allowed at the level of **precision and depth** — not costume UI.

---

## Why atmosphere matters

1. **Session length** — operator may sit 30+ minutes; flat SaaS gray fatigues; calm depth sustains focus.
2. **Peripheral cognition** — steady environment lets `info_area` escalate without global panic.
3. **Identity** — HG must feel like a **station**, not a browser tab with widgets.
4. **Trust** — restrained atmosphere signals **professional system**, not demo reel.

Atmosphere is **layer 0–1** of the stack — it must never compete with P1 content.

---

## Why restraint matters

| Restraint domain | Without restraint |
|------------------|-------------------|
| Color | Rainbow UI; signal meaning collapses |
| Glow | Fatigue; illegibility on glass |
| Motion | Gaming UI; broken calm-control |
| Glass | Apple clone or hologram fantasy |
| Typography | Decoration beats scan speed |

**Restraint increases clarity** — accent and motion **earn** attention ([color-behavior-and-accent-philosophy-v0.1.md](color-behavior-and-accent-philosophy-v0.1.md), [motion-atmosphere-v0.1.md](motion-atmosphere-v0.1.md)).

---

## Visual emotional target

| Target state | Operator should feel |
|------------|----------------------|
| **Confidence** | System is coherent; zones are predictable |
| **Calmness** | No ambient anxiety from UI chrome |
| **Control** | Work in center; risks at periphery |
| **Focus** | Foveal attention owned by `main_area` |
| **Awareness** | Tactical rail readable in < 3 s scan |
| **Intelligence** | Environment is capable, not theatrical |
| **Spatial orientation** | «Signals always right»; shell stable across modes |

**Forbidden emotional targets:** anxiety, overload, adrenaline, gamer hype, neon chaos — see [visual-dna-and-identity-v0.1.md](visual-dna-and-identity-v0.1.md).

---

## Operator psychology (intended)

| Need | Visual support |
|------|----------------|
| Situational awareness without panic | Calm tokens; persistent OVERDUE; no blink |
| Long-session readability | Contrast on glass; Exo 2 legibility |
| Peripheral vigilance | `info_area` visible; restrained CRITICAL |
| Mode posture | Shell static; content swap in center |
| Trust in persistence | Visual stability across theme toggle |

Aligns with [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md): *«Я вижу риски, но кокпит не кричит»*.

---

## Intended ambient feeling

```text
Dark default:  deep volumetric space · soft structural light · instruments on glass
Light alternate: tactical daylight · desaturated signals · maintained contrast
Both:          quiet chrome · localized activity · no wallpaper storytelling
```

**2K cockpit philosophy (draft):** design for **dense but readable** 2560×1440-class viewport — generous tri-focus, not mobile-blown SaaS cards. Exact breakpoints — Phase 4.

---

## Relationship to prior charters

| Charter | This pack extends |
|---------|-------------------|
| [visual-language-direction-v0.1.md](visual-language-direction-v0.1.md) | Summary identity → full exploration pack |
| [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md) | Interaction states → material language |
| [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md) | Timing tokens → emotional motion atmosphere |
| [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md) | Token groups → color behavior philosophy |

---

## Prototype v0.1 observations (non-binding)

| Observation | Visual consequence |
|-------------|-------------------|
| Spatial cockpit preferred over card grid | Surfaces as **instruments**, not equal widgets |
| Tri-focus readable on wide viewport | Preserve rail + center + nav proportions |
| Tactical rail must not feel like inbox | Typography + density calm; signal semantics |
| Theme toggle expected | Dark immersive primary; light tactical alternate |

**Не claim:** formal UX study; quantitative eye-tracking.

---

## Phase 3 exit criteria (visual direction draft)

- [ ] Pack v0.1 docs reviewed by operator
- [ ] Anti-pattern checklist accepted for static MVP
- [ ] Exo 2 direction confirmed for Phase 4
- [ ] Reference filter rules used before mood boards
- [ ] Token value freeze chartered (separate from this pack)

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Reference board image assets | Operator-curated; not scraped in-repo |
| Logo / wordmark final | TBD |
| Exact glass blur px | Phase 3–4 implementation |
| Illustration vs pure CSS atmosphere | Implementation choice |
| Empirical operator testing | Not conducted |

---

*Last updated: 2026-05-24 — Visual Direction Exploration Pack v0.1.*
