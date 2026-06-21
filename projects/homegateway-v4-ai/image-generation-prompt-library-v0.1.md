# HomeGateway v4.ai — image generation prompt library v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** структурированная библиотека **атмосферных промптов** для внешних image-generation инструментов — controlled, HG-aligned, anti-cyberpunk / anti-SaaS / anti-gamer.

**Не является:** автоматическая генерация в MARS, production art pipeline, UI layout prompts.

**Связанные:** [visual-probe-methodology-v0.1.md](visual-probe-methodology-v0.1.md) · [visual-probe-evaluation-framework-v0.1.md](visual-probe-evaluation-framework-v0.1.md) · study docs (TD/OM/TR/MW/LT/ED series)

---

## How to use this library

| Step | Action |
|------|--------|
| 1 | Pick **category** below |
| 2 | Copy **base prompt** + optional **modifier** |
| 3 | Append **global negatives** (mandatory) |
| 4 | Generate externally; evaluate with framework |
| 5 | Log pass/fail — extract principle only |

**Never** use generic Midjourney keyword soup. Each prompt is **one atmospheric question**.

---

## Global negatives (append to every prompt)

```text
-- avoid: cyberpunk neon, RGB gamer, SaaS dashboard grid, CRM pipeline, enterprise admin tables, notification inbox, hologram scanlines, starscape, spaceship window, matrix rain, hex spam, pure black void, flat white void, blooming glow everywhere, pulsing lights, anime UI, Dribbble trendy dashboard, readable text labels, logos, watermarks
```

Short inline form for tools without `--avoid`:

```text
no neon cyberpunk, no RGB gamer, no SaaS dashboard grid, no CRM, no inbox UI, no hologram scanlines, no stars no space window, no matrix, no pure black void, no flat white void, no bloom spam, no pulsing lights
```

---

## Global positives (HG atmosphere anchor)

```text
calm operational cockpit environment, premium aerospace restraint, layered atmospheric depth, architectural glass instruments, spatial tri-focus suggestion, restrained futuristic intelligence, volumetric tone not wallpaper art, 16:9 widescreen station
```

---

## Category index

| Category | ID prefix | Study doc |
|----------|-----------|-----------|
| Darkness | TD-xx | [tactical-darkness-study-v0.1.md](tactical-darkness-study-v0.1.md) |
| Overlays | OM-xx | [overlay-material-study-v0.1.md](overlay-material-study-v0.1.md) |
| Tactical rail | TR-xx | [tactical-rail-atmosphere-study-v0.1.md](tactical-rail-atmosphere-study-v0.1.md) |
| Workspace | MW-xx | [main-workspace-atmosphere-study-v0.1.md](main-workspace-atmosphere-study-v0.1.md) |
| Background / depth | ED-xx | [environmental-depth-study-v0.1.md](environmental-depth-study-v0.1.md) |
| Light theme | LT-xx | [light-theme-tactical-environment-study-v0.1.md](light-theme-tactical-environment-study-v0.1.md) |
| Focus state | FS-xx | (this library) |
| Combined calibration | CAL-xx | (this library) |

Full prompt text for TD/OM/TR/MW/LT/ED: see study docs — this library adds **composable bases** + **cross-category** entries.

---

## Darkness — composable bases

| ID | Base prompt |
|----|-------------|
| **DARK-BASE-01** | Deep layered navy charcoal volumetric cockpit bay, soft cool top-down ambient wash, calm premium operational |
| **DARK-BASE-02** | Dark environment corner falloff spatial enclosure, blue-gray shadows, minimal large-scale geometry 4% opacity |
| **DARK-MOD-SIGNAL** | + one tiny restrained amber peripheral badge glow only |
| **DARK-MOD-GLASS** | + abstract architectural glass edge catch-light foreground |

**Canonical probes:** TD-01 … TD-10 in study doc.

---

## Overlays — composable bases

| ID | Base prompt |
|----|-------------|
| **OVR-BASE-01** | Neutral architectural glass panel, subtle border, dark calm environment backdrop dimmed |
| **OVR-BASE-02** | Two-layer glass stack rear flat front brighter, restrained depth |
| **OVR-MOD-DIM** | + widescreen cockpit silhouette 40% dim preserving three zones |
| **OVR-MOD-SHEET** | + denser opaque sheet layer above glass |

**Canonical probes:** OM-01 … OM-10.

---

## Tactical rail — composable bases

| ID | Base prompt |
|----|-------------|
| **RAIL-BASE-01** | Right peripheral tactical column, neutral glass rows, calm compact density |
| **RAIL-BASE-02** | Tactical list neutral rows, small semantic badges only, no row body flood color |
| **RAIL-MOD-CRIT** | + exactly one small red critical badge |
| **RAIL-MOD-OVERDUE** | + subtle top band slightly denser persistent overdue mood |

**Canonical probes:** TR-01 … TR-10.

---

## Workspace — composable bases

| ID | Base prompt |
|----|-------------|
| **WS-BASE-01** | Wide center operational canvas, asymmetric glass instruments, generous negative space |
| **WS-BASE-02** | Single raised active glass instrument, others muted, focus light |
| **WS-MOD-SYSTEMS** | + multiple small status instruments hierarchical calm |
| **WS-MOD-FOCUS** | + center bright periphery zones reduced contrast 30% |

**Canonical probes:** MW-01 … MW-10.

---

## Background / depth — composable bases

| ID | Base prompt |
|----|-------------|
| **ENV-BASE-01** | Environmental layer only, three depth planes, no UI, no scenery |
| **ENV-BASE-02** | Volumetric gradient only, soft falloff, no geometry |
| **ENV-MOD-GEO** | + faint large-scale arcs lines 3% opacity |
| **ENV-MOD-LIGHT** | Light theme cool off-white layered planes faint geometry 2% |

**Canonical probes:** ED-01 … ED-10.

---

## Light theme — composable bases

| ID | Base prompt |
|----|-------------|
| **LIGHT-BASE-01** | Tactical daylight cool layered off-white blue-gray, volumetric depth, not sterile SaaS |
| **LIGHT-BASE-02** | Light glass panels clear borders, desaturated environment |
| **LIGHT-MOD-SIGNAL** | + desaturated amber red small badges on neutral rows |
| **LIGHT-MOD-ANTI-CRM** | explicitly NOT CRM NOT pipeline NOT enterprise admin |

**Canonical probes:** LT-01 … LT-10.

---

## Focus state (library-only)

### FS-01 — Overlay-open focus

| Field | Content |
|-------|---------|
| **Purpose** | Atmosphere when L3 panel open |
| **Exploration goal** | Dim station + lit panel |
| **Expected emotional result** | Temporary depth; shell memory |
| **Anti-pattern warnings** | No blackout; no new scene |

**Prompt:**

```text
Abstract operational cockpit overlay-open atmosphere, dimmed tri-focus silhouette, brighter glass panel center-right, calm premium, global negatives, 16:9
```

### FS-02 — Critical without panic

| Field | Content |
|-------|---------|
| **Purpose** | P0 mood without adrenaline |
| **Exploration goal** | Small critical cues only |
| **Expected emotional result** | Alert calm |
| **Anti-pattern warnings** | No fullscreen red |

**Prompt:**

```text
Abstract dark cockpit calm atmosphere with two tiny critical red amber badges periphery only, neutral environment 98%, operational restraint, global negatives, 16:9
```

### FS-03 — Focus mode deep work

| Field | Content |
|-------|---------|
| **Purpose** | Mode C atmospheric posture |
| **Exploration goal** | Center dominant calm |
| **Expected emotional result** | Flow without isolation |
| **Anti-pattern warnings** | Periphery visible |

**Prompt:**

```text
Abstract focus deep work cockpit center workspace calm bright glass, left and right zones muted not removed, dark volumetric depth, global negatives, 16:9
```

---

## Combined calibration (library-only)

### CAL-01 — Full tri-focus dark (abstract)

**Prompt:**

```text
Ultra-wide abstract dark operational cockpit tri-focus composition left navigation center work right tactical awareness, layered volumetric navy environment, architectural glass hints, calm premium aerospace, global negatives, 21:9
```

### CAL-02 — Theme parity check (split mood — generate separately)

Generate **two** images in one session with same composition intent:

1. DARK-BASE-01 + global positives + negatives  
2. LIGHT-BASE-01 + global positives + negatives  

Compare: **same station identity**, different illumination.

### CAL-03 — Anti-pattern torture test

**Prompt:**

```text
Abstract operational cockpit atmosphere ONLY with global negatives repeated twice, calm restrained, if output adds neon dashboard stars inbox treat as hard fail, 16:9
```

---

## Prompt quality rules

| Rule | Rationale |
|------|-----------|
| One question per generation | Avoid muddy evaluation |
| Widescreen 16:9 or 21:9 | 2K station framing |
| Abstract — no readable UI text | Prevents fake UI approval |
| Always append global negatives | HG filter consistency |
| No «8k trending beautiful UI» | Keyword soup drift |
| Log ID (TD-03, etc.) | Traceability |

---

## Versioning

| Version | Change |
|---------|--------|
| v0.1 | Initial library; mirrors study docs |

Operator may fork prompts in session notes — repo canon remains these IDs.

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Tool-specific syntax | Adapt negatives to Midjourney / SD / etc. |
| Seed control | Operator discretion |

---

*Last updated: 2026-05-24 — Image generation prompt library.*
