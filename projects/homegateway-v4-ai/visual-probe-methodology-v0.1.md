# HomeGateway v4.ai — visual probe methodology v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** методология **атмосферных визуальных проб** — генерация, сравнение, фильтрация, оценка качества атмосферы.

**Не является:** design approval workflow, CI pipeline, automated scoring, production handoff.

**Связанные:** [atmospheric-visual-exploration-pack-v0.1.md](atmospheric-visual-exploration-pack-v0.1.md) · [visual-probe-evaluation-framework-v0.1.md](visual-probe-evaluation-framework-v0.1.md) · [image-generation-prompt-library-v0.1.md](image-generation-prompt-library-v0.1.md)

---

## Canonical definitions

### A probe is NOT

| Misuse | Why wrong |
|--------|-----------|
| **Final design** | Layout, tokens, components undecided |
| **UI approval** | Wireframes + operator sign-off required for Phase 4 |
| **Production screen** | No HTML/CSS claim from image |
| **Brand deliverable** | Marketing site out of scope |
| **Figma substitute** | Structure lives in wireframe docs |

### A probe IS

| Use | Description |
|-----|-------------|
| **Atmospheric experiment** | Tests one mood hypothesis |
| **Visual direction test** | Validates calm / premium / operational feel |
| **Material exploration** | Glass, darkness, depth, overlay character |
| **Mood validation** | Operator emotional calibration |

---

## Operator-feeling-first approach

Decisions start from **how the operator should feel**, not from tool impressiveness.

| Question (ask first) | Then |
|----------------------|------|
| Should this feel calm or alert? | Choose study doc + prompt tier |
| Which zone is in scope? | Rail-only vs full cockpit silhouette |
| What failure mode are we avoiding? | Tag anti-pattern from [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md) |
| Can I work 30 minutes in this mood? | Pass/fail via [visual-probe-evaluation-framework-v0.1.md](visual-probe-evaluation-framework-v0.1.md) |

**Feeling precedes aesthetics.** A beautiful image that fails operational calm is **fail**.

---

## Probe lifecycle (iteration loops)

```text
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  QUESTION   │────►│   GENERATE   │────►│  EVALUATE   │
│  (1 study)  │     │  (1–3 imgs)  │     │  framework  │
└─────────────┘     └──────────────┘     └──────┬──────┘
       ▲                                        │
       │         ┌──────────────┐                │
       └─────────│    REVISE    │◄─── FAIL ─────┘
                 │ prompt/scope │
                 └──────┬───────┘
                        │ PASS
                        ▼
                 ┌──────────────┐
                 │   EXTRACT    │
                 │  principle   │──► visual direction / theme notes
                 └──────────────┘
```

| Loop | Max recommended | Rule |
|------|-----------------|------|
| Single question | 3 generations | Avoid endless variation |
| Study category | 1 session | e.g. darkness only today |
| Full pack | Multiple sessions | Do not batch-approve all categories |

---

## Generating visual probes

| Step | Action |
|------|--------|
| 1 | Pick **one** study: darkness / overlay / rail / workspace / light / depth |
| 2 | Copy prompt from study or [image-generation-prompt-library-v0.1.md](image-generation-prompt-library-v0.1.md) |
| 3 | Add **negative constraints** from prompt (anti-SaaS, anti-cyberpunk, etc.) |
| 4 | Use **widescreen** aspect (~16:9) when tool allows — 2K station framing |
| 5 | Generate **outside** repo; store in operator board if desired |
| 6 | Never prompt «beautiful dashboard UI» — use atmospheric language |

### Prompt hygiene

| Do | Don't |
|----|-------|
| «calm operational cockpit bay, volumetric dark navy» | «futuristic UI design 8k trending» |
| «architectural glass panels, restrained cyan accent» | «neon cyberpunk HUD dashboard» |
| «peripheral tactical rail, muted signal badges» | «notification center inbox app» |
| «tactical daylight, layered cool whites» | «clean minimal SaaS CRM» |

---

## Comparing probes

Compare **within one study category** only — darkness A vs darkness B, not darkness vs light theme in same pass.

| Comparison axis | Notes |
|-----------------|-------|
| **Calm vs anxiety** | Gut check + framework questions |
| **Depth vs flat** | Enough layering without wallpaper |
| **Signal discipline** | Color only on semantics |
| **Spatial silhouette** | Tri-focus readable even if abstract |
| **Session fatigue** | 5-minute stare test |

Side-by-side: max **3** images. More → decision paralysis.

---

## Filtering probes

| Filter stage | Outcome |
|--------------|---------|
| **Hard fail** | Matches forbidden anti-pattern → discard, log tag |
| **Soft fail** | Close but one axis wrong → revise prompt |
| **Pass** | Extract 1–2 principles, not full composition clone |
| **Hold** | Interesting but out of scope → archive, do not merge |

**Never** promote probe to «approved UI» without wireframe + token review.

---

## Evaluating atmosphere quality

Use [visual-probe-evaluation-framework-v0.1.md](visual-probe-evaluation-framework-v0.1.md) — mandatory checklist per image.

Minimum bar for **pass**:

- Operational calm (not gamer, not cinematic overload)
- Enough depth (not void, not flat SaaS)
- Readable hierarchy suggestion (even in abstract probes)
- HG-aligned restraint (signal color bounded)
- No forbidden environment (stars, ship windows, matrix)

---

## Comparison criteria (summary table)

| Criterion | Pass indicator | Fail indicator |
|-----------|----------------|----------------|
| Operational | Station / instruments | Vanity dashboard |
| Calm | Steady atmosphere | Blink / pulse / chaos |
| Premium | Material quality | Cheap gradient spam |
| Spatial | Left-center-right roles | Equal card grid |
| Tactical | Peripheral awareness | Inbox / feed noise |
| Restraint | One accent family | RGB everywhere |
| Depth | Layered environment | Pure black void or white void |
| Light theme | Tactical clarity | Sterile CRM |

---

## Documentation discipline (human-operated)

Per probe cycle, operator notes (any format):

```text
Date:
Study:
Prompt ID:
Tool:
Pass/Fail:
Anti-pattern tags (if fail):
Extracted principle (if pass):
Next action:
```

No automated log in MARS v0.1.

---

## Relationship to reference analysis

Before external Pinterest/Dribbble references:

1. Classify via [reference-analysis-and-visual-boundaries-v0.1.md](reference-analysis-and-visual-boundaries-v0.1.md)
2. If reference is «dangerous class» — do not probe-copy; extract principle only
3. Probes **implement** HG filters — they do not replace them

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Team review process | Solo operator default |
| Probe versioning | Operator discretion |
| Quantitative metrics | Not used v0.1 |

---

*Last updated: 2026-05-24 — Visual probe methodology.*
