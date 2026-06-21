# HomeGateway v4.ai — tactical rail atmosphere study v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** атмосфера **`info_area`** — peripheral awareness, tactical signal mood, compact density, signal calmness, severity readability.

**Не является:** signal data model, rail HTML, notification product.

**Связанные:** [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md) · [wireframes/tactical-signals-wireframe-v0.1.md](wireframes/tactical-signals-wireframe-v0.1.md) · [information-priority-model-v0.1.md](information-priority-model-v0.1.md)

---

## How tactical rail should FEEL

| Feeling | Description |
|---------|-------------|
| **Peripheral radar** | Scanned in <3 s; not foveal owner |
| **Calm vigilance** | Risks visible; cockpit does not scream |
| **Compact operational density** | Many rows; still breathable |
| **Severity readable** | Level obvious without red flood |
| **Not inbox** | No read/unread engagement pattern |

Canonical operator line: *«Я вижу риски, но кокпит не кричит»*.

---

## How attention should work

```text
Foveal:     main_area (work)
Peripheral: info_area (tactical ladder)
Escalation: badge / band — never fullscreen blink
Persistence: OVERDUE visible until resolved
```

| P-tier in rail | Visual loudness |
|----------------|-----------------|
| P0 CRITICAL/OVERDUE | Strong badge; neutral row body |
| P1–P2 rows | Standard glass |
| P3 chrome | Muted headers, scroll fades |

---

## How calmness is preserved

| Rule | Rationale |
|------|-----------|
| No blink / pulse loops | Alert fatigue |
| No every-row red | Semantic collapse |
| Sticky bands restrained | OVERDUE top — not banner wall |
| Typography disciplined | Exo 2 compact; no shouty display |
| Rail chrome quiet | Primary surface; signals on badges |

---

## Allowed / forbidden (rail atmosphere)

| Allowed | Forbidden |
|---------|-----------|
| Neutral rows + colored badge | Full-row rainbow |
| Glass or flat tactical surface | Inbox bubbles, avatar stacks |
| Internal scroll with fade masks | Feed infinite scroll metaphor |
| Semantic amber/red small areas | Neon perimeter frames |

---

## Controlled image-generation prompts

---

### TR-01 — Peripheral tactical column (abstract)

| Field | Content |
|-------|---------|
| **Purpose** | Rail as right-edge atmosphere |
| **Exploration goal** | Vertical zone — denser tone, still calm |
| **Expected emotional result** | Peripheral awareness without anxiety |
| **Anti-pattern warnings** | No inbox UI; no chat bubbles |

**Prompt:**

```text
Abstract widescreen dark operational cockpit, right peripheral vertical zone suggesting compact tactical awareness column, muted glass rows, calm premium, left and center softer, no notification app UI, no neon, no inbox metaphor, 16:9
```

---

### TR-02 — Signal calmness (mostly neutral rows)

| Field | Content |
|-------|---------|
| **Purpose** | Default rail mood — INFO/WATCH dominance |
| **Exploration goal** | 90% neutral rows, tiny cool muted badges |
| **Expected emotional result** | «Mostly fine» — steady state |
| **Anti-pattern warnings** | No wall of red |

**Prompt:**

```text
Abstract tactical signal column atmosphere, many neutral dark glass rows, occasional tiny cool blue-gray info badges only, calm operational vigilance, no red flood, no pulsing lights, premium aerospace restraint, 16:9
```

---

### TR-03 — Severity readability (one CRITICAL)

| Field | Content |
|-------|---------|
| **Purpose** | Single P0 emphasis discipline |
| **Exploration goal** | One row with strong small red badge — body neutral |
| **Expected emotional result** | Clear priority; no panic |
| **Anti-pattern warnings** | One critical only; no fullscreen alert |

**Prompt:**

```text
Abstract tactical rail study, vertical list of neutral glass rows, exactly one row with small restrained red critical badge edge, row background not red, calm cockpit, no alarm modal, no neon, 16:9
```

---

### TR-04 — OVERDUE persistent band mood

| Field | Content |
|-------|---------|
| **Purpose** | Sticky overdue atmosphere |
| **Exploration goal** | Top band slightly denser — persistent, not screaming |
| **Expected emotional result** | Serious continuity; operator trust |
| **Anti-pattern warnings** | No blink; no giant red header |

**Prompt:**

```text
Abstract right tactical column with subtle top band slightly denser tone suggesting persistent overdue section, restrained saturated red small labels only, calm professional, no banner alarm, no cyberpunk, 16:9
```

---

### TR-05 — Compact operational density

| Field | Content |
|-------|---------|
| **Purpose** | Many signals — without clutter chaos |
| **Exploration goal** | Tight vertical rhythm; readable separation |
| **Expected emotional result** | Dense but scannable |
| **Anti-pattern warnings** | No overlapping glow; no 3D explosion |

**Prompt:**

```text
Abstract compact tactical awareness column many thin neutral rows tight vertical rhythm, dark glass, premium operational density, readable separation lines, calm not chaotic, no gamer UI, no feed timeline, 16:9
```

---

### TR-06 — Rail chrome vs row body

| Field | Content |
|-------|---------|
| **Purpose** | Primary surface rail frame |
| **Exploration goal** | Rail container quieter than row content |
| **Expected emotional result** | Structure stable; data forward |
| **Anti-pattern warnings** | No decorative rail neon |

**Prompt:**

```text
Abstract dark cockpit right rail chrome frame subtle primary surface, interior glass rows slightly brighter, calm mission control, no RGB frame, no hologram, 16:9
```

---

### TR-07 — Scroll fade mask atmosphere

| Field | Content |
|-------|---------|
| **Purpose** | Internal scroll boundary feel |
| **Exploration goal** | Soft top/bottom fade — content continues |
| **Expected emotional result** | Contained periphery |
| **Anti-pattern warnings** | No harsh crop; no page scroll metaphor |

**Prompt:**

```text
Abstract vertical tactical list with soft gradient fade mask top and bottom edges, dark calm environment, premium operational, suggests internal scroll region, no page scroll, 16:9
```

---

### TR-08 — Anti-inbox negative probe

| Field | Content |
|-------|---------|
| **Purpose** | Reject notification-center aesthetic |
| **Exploration goal** | Must fail if tool produces inbox/chat |
| **Expected emotional result** | Evaluation discipline |
| **Anti-pattern warnings** | Hard fail on bubbles, avatars, unread dots |

**Prompt:**

```text
Operational tactical awareness column abstract, explicitly NOT notification center, NOT inbox, NOT chat app, NOT social feed, calm neutral glass rows small semantic badges only, dark premium cockpit, 16:9
```

---

### TR-09 — Morning scan clarity

| Field | Content |
|-------|---------|
| **Purpose** | <3 s scan emotional target |
| **Exploration goal** | High contrast badges on calm field |
| **Expected emotional result** | Instant level read |
| **Anti-pattern warnings** | Badge size disciplined; no shouty typography |

**Prompt:**

```text
Abstract tactical rail optimized for fast peripheral scan, high clarity small semantic color badges on neutral rows, dark calm background, aerospace operational, no decorative fonts, no neon chaos, 16:9
```

---

### TR-10 — Rail + dimmed center (focus preservation)

| Field | Content |
|-------|---------|
| **Purpose** | Rail visible while center is focus |
| **Exploration goal** | Center softer; rail steady — dual awareness |
| **Expected emotional result** | Work + vigilance coexist |
| **Anti-pattern warnings** | Rail must not overpower center glow |

**Prompt:**

```text
Abstract tri-focus cockpit dark atmosphere, center work zone slightly brighter calm, right tactical column steady peripheral tone, left navigation muted, layered operational calm, no dashboard grid, 16:9
```

---

## SAFE UNKNOWN

- Exact row height at 2K — Phase 4 implementation
- Rail width px — wireframe + prototype review

---

*Last updated: 2026-05-24 — Tactical rail atmosphere study.*
