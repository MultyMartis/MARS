# HomeGateway v4.ai — Atmospheric Visual Exploration Pack v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B — atmospheric visual exploration  
**Назначение:** мастер-документ **атмосферных визуальных исследований** — controlled probes, mood discovery, material feeling, operator emotional calibration.

**Не является:** final UI, production mockups, Figma, frontend implementation, design token implementation, automated image generation, runtime product.

**Связанные (visual direction canon):** [visual-direction-exploration-pack-v0.1.md](visual-direction-exploration-pack-v0.1.md) · [visual-dna-and-identity-v0.1.md](visual-dna-and-identity-v0.1.md) · [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md)

---

## Pack scope (v0.1)

| # | Document | Role |
|---|----------|------|
| 1 | **This file** | Master atmospheric exploration — purpose, philosophy, index |
| 2 | [visual-probe-methodology-v0.1.md](visual-probe-methodology-v0.1.md) | How to generate, compare, filter probes |
| 3 | [tactical-darkness-study-v0.1.md](tactical-darkness-study-v0.1.md) | Cockpit darkness, ambient depth |
| 4 | [overlay-material-study-v0.1.md](overlay-material-study-v0.1.md) | Glass, overlays, layered immersion |
| 5 | [tactical-rail-atmosphere-study-v0.1.md](tactical-rail-atmosphere-study-v0.1.md) | `info_area` mood, peripheral calm |
| 6 | [main-workspace-atmosphere-study-v0.1.md](main-workspace-atmosphere-study-v0.1.md) | `main_area` focus environment |
| 7 | [light-theme-tactical-environment-study-v0.1.md](light-theme-tactical-environment-study-v0.1.md) | Operational light theme without SaaS |
| 8 | [environmental-depth-study-v0.1.md](environmental-depth-study-v0.1.md) | Background as atmospheric layer |
| 9 | [image-generation-prompt-library-v0.1.md](image-generation-prompt-library-v0.1.md) | Structured prompt library (no auto-gen) |
| 10 | [visual-probe-evaluation-framework-v0.1.md](visual-probe-evaluation-framework-v0.1.md) | Pass/fail atmosphere evaluation |

**Phase boundary:** atmospheric research only. Token freeze, HTML, curated reference boards remain separate ([roadmap-v0.1.md](roadmap-v0.1.md)).

---

## What this pack is

**VISUAL ATMOSPHERE RESEARCH** — discovering how HomeGateway should *feel* before any production screen is approved.

| Creates | Does not create |
|---------|-----------------|
| Controlled atmospheric visual probes (methodology + prompts) | Final UI |
| Visual exploration methodology | Production mockups |
| Material and cockpit mood studies | Frontend implementation |
| Tactical environment experiments | Polished interface system |
| Image-generation-ready exploration prompts | Figma files or auto-generated images in-repo |

---

## Why atmosphere matters

Architecture ([cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md)), tri-focus, and signal doctrine define **where** attention goes. Atmosphere defines **how it feels** to sit in that structure for 30+ minutes.

| Without atmosphere research | With atmosphere research |
|-----------------------------|--------------------------|
| Correct zones, wrong emotional tone | Spatial + emotional coherence |
| Flat SaaS or accidental cyberpunk | Intentional operational ambiance |
| Operator fatigue from chrome | Calm-control sustained in session |
| Reference drift at implementation | Pre-filtered mood vocabulary |

> **HG background is NOT wallpaper.**  
> **HG background IS** atmospheric environmental layer — see [background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md).

Atmosphere is **layer 0–1** of the stack — it must never compete with P1 content ([information-priority-model-v0.1.md](information-priority-model-v0.1.md)).

---

## Why architecture alone is not enough

| Architecture answers | Atmosphere answers |
|----------------------|-------------------|
| Zone roles (nav / work / tactical) | Material feeling in each zone |
| P0–P3 attention tiers | Whether depth feels premium or cheap |
| Viewport-first, no page scroll | Whether the room feels like a station |
| Signal ladder semantics | Whether darkness feels calm or gamer |

A spatially correct cockpit can still read as **enterprise admin**, **Dribbble demo**, or **cyberpunk toy** if atmosphere is uncontrolled. This pack prevents that drift **before** Phase 4 HTML.

---

## Why HG must feel emotionally coherent

The operator manages a **living AI/web ecosystem** — clients, projects, deadlines, integrations (display-only in static MVP). Emotional incoherence breaks trust:

| Incoherence symptom | Operator impact |
|---------------------|-----------------|
| Neon periphery + gray center | «System is panicking but work area is bored» |
| Hologram glass + CRM tables | Identity collapse — fantasy + clerk |
| Cinematic background + flat widgets | Wallpaper competes with judgment |
| Gamer rail + aerospace center | Peripheral anxiety |

Coherence means: **one station, one mood family, localized escalation only**.

Canonical one-liner (unchanged from visual direction):

> **Calm operational environment for a human operator managing a living AI/web ecosystem.**

**Not:** a flashy futuristic interface demo.

---

## Controlled visual probes

A **visual probe** is a deliberate, non-final atmospheric experiment — typically an image-generation output or curated reference — tested against HG doctrine.

| Probe property | Rule |
|----------------|------|
| **Scoped** | One atmosphere question per probe (e.g. rail calmness, not full app) |
| **Non-binding** | Probe pass ≠ UI approval |
| **Comparable** | Same aspect ratio / 2K-class framing when possible |
| **Documented** | Purpose, goal, expected feeling, anti-pattern warnings |
| **Filtered** | [visual-probe-evaluation-framework-v0.1.md](visual-probe-evaluation-framework-v0.1.md) before promotion |

Probes explore **mood and material** — not layout pixel specs. Wireframes remain authoritative for structure ([wireframes/README.md](wireframes/README.md)).

---

## Iterative atmosphere exploration

```text
1. Define atmosphere question (study doc)
2. Select 1–3 prompts from library or study
3. Generate externally (operator-controlled tool)
4. Evaluate with framework — pass / fail / revise
5. Log decision in session notes (human-operated)
6. Extract principle → visual direction pack (not screenshot clone)
7. Repeat until operator calibration stable
```

**No** automated generation in MARS repo. **No** claiming «final look» from a single lucky image.

---

## Non-final visual studies

All outputs of this lane are **studies**:

| Study type | Example doc |
|------------|-------------|
| Darkness philosophy | [tactical-darkness-study-v0.1.md](tactical-darkness-study-v0.1.md) |
| Overlay glass mood | [overlay-material-study-v0.1.md](overlay-material-study-v0.1.md) |
| Zone-specific atmosphere | rail / workspace / light / depth studies |
| Prompt inventory | [image-generation-prompt-library-v0.1.md](image-generation-prompt-library-v0.1.md) |

Studies inform Phase 3 token freeze and Phase 4 static MVP — they do not replace [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md) or wireframes.

---

## Operator emotional calibration

| Calibration target | Probe validates |
|--------------------|-----------------|
| Long-session calm | No fatigue in 5-minute review |
| Peripheral trust | Rail readable without anxiety |
| Focus ownership | Center feels like «my work» |
| Premium operational | Precision, not luxury marketing |
| Spatial memory | Tri-focus silhouette preserved in probes |

Operator review is **human-operated** — no UX lab, no eye-tracking claimed ([visual-direction-exploration-pack-v0.1.md](visual-direction-exploration-pack-v0.1.md) SAFE UNKNOWN).

---

## HG should feel (target atmosphere)

| Quality | Meaning |
|---------|---------|
| **Calm** | Steady chrome; escalation earned |
| **Intelligent** | Capable depth; no fake AI theater |
| **Premium** | Material precision under load |
| **Operational** | Readable instruments, not vanity metrics |
| **Spatial** | Tri-focus; room-like station |
| **Layered** | Background → glass → focus → overlay |
| **Atmospheric** | Environmental depth without narrative wallpaper |
| **Focused** | `main_area` owns foveal attention |

---

## HG must NOT feel (forbidden atmosphere)

| Forbidden | Typical failure mode |
|-----------|----------------------|
| **Flashy** | Demo reel aesthetics |
| **Gamer** | RGB, pulse, neon frames |
| **Aggressive** | Adrenaline UI, blink, red floods |
| **Hyperactive** | Fast ambient motion, particle spam |
| **Cinematic overload** | Movie prop HUD, bloom everywhere |
| **Startup-SaaS** | Inter-gray cards, equal widget grid |

See [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md) for detection and mitigation.

---

## Relationship to Visual Direction Exploration Pack

| Prior pack (v0.1) | This pack (v0.1) extends |
|-------------------|--------------------------|
| DNA, materials, light, color philosophy | **Executable exploration** via probes + prompts |
| Doctrine and rules | **Empirical mood tests** (operator-run) |
| Anti-patterns catalog | **Per-probe evaluation** framework |

Read visual direction pack first; use atmospheric pack when **generating or judging** mood images.

---

## 2K cockpit and viewport-first (probe framing)

| Constraint | Probe implication |
|------------|-------------------|
| **2K-class viewport** (~2560×1440) | Wide tri-focus; dense but readable — not mobile card stack |
| **Viewport-first** | Environment fixed; no «scrolling poster» composition |
| **Exo 2** | Probes may omit type detail; implementation uses [typography-atmosphere-v0.1.md](typography-atmosphere-v0.1.md) |

Probes should suggest **widescreen station** — not phone mockup or Pinterest square.

---

## Phase exit criteria (atmospheric exploration draft)

- [ ] Methodology + evaluation framework reviewed
- [ ] At least one probe cycle per study category (operator-run, external tool)
- [ ] Failed probes logged with anti-pattern tag
- [ ] Principles extracted to token/theme review (separate session)
- [ ] No claim of final UI from probes alone

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Image tool choice | Operator selects (Midjourney, SD, etc.) — not in-repo |
| Probe asset storage | Curated board location TBD — not committed in v0.1 |
| Empirical operator testing | Not conducted |
| Light vs dark primary preference | Dark immersive primary; light alternate — validate with probes |

---

*Last updated: 2026-05-24 — Atmospheric Visual Exploration Pack v0.1 (Lane B).*
