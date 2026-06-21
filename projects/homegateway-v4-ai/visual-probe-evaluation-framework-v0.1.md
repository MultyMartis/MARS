# HomeGateway v4.ai — visual probe evaluation framework v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** **оценка атмосферных проб** — pass/fail indicators, checklist questions, anti-pattern tagging.

**Не является:** automated ML scorer, design system linter, WCAG tool.

**Связанные:** [visual-probe-methodology-v0.1.md](visual-probe-methodology-v0.1.md) · [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md) · [reference-analysis-and-visual-boundaries-v0.1.md](reference-analysis-and-visual-boundaries-v0.1.md)

---

## Evaluation workflow

```text
1. View probe 5 minutes max (fatigue test)
2. Answer checklist (below)
3. Any HARD FAIL → reject probe
4. ≥2 SOFT FAIL → revise prompt or reject
5. PASS → extract 1–2 principles (not composition clone)
6. Log: ID, pass/fail, tags, notes
```

---

## Core checklist questions

Answer **Yes / No / N/A** per probe. **No** on operational/calm/spatial where applicable = fail that axis.

| # | Question | Pass if |
|---|----------|---------|
| Q1 | Does it feel **operational** (station/instruments)? | Yes — not marketing demo |
| Q2 | Does it feel **calm**? | Yes — no ambient anxiety |
| Q3 | Too **gamer**? | No — no RGB/carbon/pulse |
| Q4 | Too **cinematic**? | No — not movie prop overload |
| Q5 | Too **SaaS**? | No — not equal widget dashboard |
| Q6 | Too **empty**? | No — still has depth/layers |
| Q7 | Too **cyberpunk**? | No — no neon cyan-magenta chaos |
| Q8 | Too **sterile**? | No — not flat white/gray void |
| Q9 | Too **enterprise**? | No — not clerk table dominance |
| Q10 | Too much **glow**? | No — ≤1 focal glow region |
| Q11 | Enough **depth**? | Yes — 2+ tonal planes |
| Q12 | Enough **spatiality**? | Yes — tri-focus suggested or N/A for micro study |
| Q13 | Enough **readability** suggestion? | Yes — hierarchy even if abstract |
| Q14 | Background is **environment** not wallpaper? | Yes — no narrative scene |
| Q15 | Signal color **bounded**? | Yes — semantics small areas |
| Q16 | Would operator trust **30 min** session? | Yes — no eye fatigue |

---

## Pass / fail indicators

### HARD FAIL (automatic reject)

Any single match → **FAIL**, log tag:

| Tag | Detection |
|-----|-----------|
| `FAIL-CYBER` | Neon cyan+magenta, hex grid spam, glitch |
| `FAIL-GAMER` | RGB borders, carbon, pulsing lights |
| `FAIL-SAAS` | Equal colorful dashboard cards, KPI wall |
| `FAIL-CRM` | Pipeline/kanban/sales aesthetic (light probes) |
| `FAIL-INBOX` | Notification center, chat bubbles, unread dots |
| `FAIL-WALLPAPER` | Stars, space window, landscape, hero photo |
| `FAIL-HOLO` | Scanlines, hologram rainbow glass, wireframe mesh |
| `FAIL-VOID` | Pure #000 or flat #FFF entire frame |
| `FAIL-PANIC` | Full-screen red, blink implied, alarm theater |
| `FAIL-FAKE-AI` | Brain networks, matrix rain, AI mascot glow |

### SOFT FAIL (revise once; second time reject)

| Tag | Detection |
|-----|-----------|
| `SOFT-FLAT` | Depth planes unclear |
| `SOFT-GLOW` | Multiple glow regions |
| `SOFT-APPLE` | Only frosted white minimal — no cockpit depth |
| `SOFT-CINEMA` | Bloom heavy but not hard cyber |
| `SOFT-EMPTY` | Acceptable for micro crop — retry wider framing |
| `SOFT-SPATIAL` | Tri-focus unclear in full-cockpit probes only |

### PASS

| Criterion | Requirement |
|-----------|-------------|
| Zero HARD FAIL | Mandatory |
| ≤1 SOFT FAIL | Or zero |
| Q1, Q2, Q11, Q16 | All **Yes** |
| Operator gut | «Could live in this mood» |

**PASS does not mean** UI approved — only atmosphere direction viable.

---

## Scoring rubric (optional quick grade)

Human-operated 0–2 per axis; **minimum total 14/20** for pass (experimental).

| Axis | 0 | 1 | 2 |
|------|---|---|---|
| Operational calm | Anxiety | Neutral | Calm |
| Premium material | Cheap | OK | Premium |
| Depth | Flat/void | Weak | Layered |
| Restraint | Chaos | Mixed | Restrained |
| Spatiality | None | Weak | Clear tri-focus |
| Signal discipline | Flood | Mixed | Bounded |
| Light theme (if applicable) | CRM/SaaS | Mixed | Tactical daylight |
| Session sustainability | 5 min fatigue | OK | 30 min viable |

Skip light column for dark-only probes.

---

## Category-specific gates

| Study | Extra pass rule |
|-------|-----------------|
| [tactical-darkness-study-v0.1.md](tactical-darkness-study-v0.1.md) | Layered navy/charcoal — not void |
| [overlay-material-study-v0.1.md](overlay-material-study-v0.1.md) | Glass architectural — not hologram |
| [tactical-rail-atmosphere-study-v0.1.md](tactical-rail-atmosphere-study-v0.1.md) | Not inbox; peripheral calm |
| [main-workspace-atmosphere-study-v0.1.md](main-workspace-atmosphere-study-v0.1.md) | Not equal card grid |
| [light-theme-tactical-environment-study-v0.1.md](light-theme-tactical-environment-study-v0.1.md) | Not sterile SaaS/CRM |
| [environmental-depth-study-v0.1.md](environmental-depth-study-v0.1.md) | Not wallpaper scene |

---

## Comparison mode (A vs B)

When comparing two probes:

| Winner | Rule |
|--------|------|
| More calm at equal depth | Prefer |
| More depth at equal calm | Prefer |
| More spatial at equal material | Prefer for full-frame |
| Neither | Both fail — revise prompts |

Do not pick «cooler» if it fails Q16 fatigue.

---

## Extraction template (on PASS)

```text
Probe ID:
Principle 1: (e.g. corner falloff depth)
Principle 2: (e.g. badge-only signal glow)
Reject from image: (specific elements not to copy)
Maps to doc: (lighting / background / material / color)
Token implication: (qualitative only — no hex from image)
```

---

## Relationship to visual anti-patterns

| Anti-pattern doc entry | Evaluation tag |
|------------------------|----------------|
| SaaS dashboard drift | FAIL-SAAS |
| Enterprise admin drift | FAIL-CRM / SOFT-ENTERPRISE |
| Cyberpunk overload | FAIL-CYBER |
| RGB gamer UI | FAIL-GAMER |
| Fantasy hologram | FAIL-HOLO |
| Giant card-grid | FAIL-SAAS |
| Wallpaper background | FAIL-WALLPAPER |

Full catalog: [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md).

---

## Reporting (session)

Minimum log per session:

```text
Session date:
Tool:
Probes evaluated: (IDs)
Passed: 
Failed: (tags)
Principles extracted:
Open questions:
```

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Inter-rater reliability | Solo operator default |
| Automated vision classifiers | Not used — human judgment |

---

*Last updated: 2026-05-24 — Visual probe evaluation framework.*
