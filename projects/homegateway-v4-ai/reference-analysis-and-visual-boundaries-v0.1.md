# HomeGateway v4.ai — reference analysis and visual boundaries v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** **как фильтровать вдохновение** — useful vs dangerous reference classes; **не** scraping реальных референсов.

**Не является:** mood board archive, Pinterest collection, competitor teardown report.

**Связанные:** [visual-direction-exploration-pack-v0.1.md](visual-direction-exploration-pack-v0.1.md) · [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md)

---

## Purpose

HG visual direction will be influenced by external UI culture. Without filters, inspiration drifts toward **Dribbble demos**, **game HUDs**, or **SaaS templates**.

This document defines **what to borrow** and **what to reject** — before any reference board is assembled (operator-curated, Phase 3).

---

## Reference analysis method (human-operated)

| Step | Action |
|------|--------|
| 1 | Classify reference into **useful** or **dangerous** category below |
| 2 | If mixed — extract **principle** (light, depth, spacing) not **screenshot composition** |
| 3 | Map extracted principle to HG doc (material, light, color, spatial) |
| 4 | Run [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md) checklist |
| 5 | Log decision in session notes — no automated scraper |

**Not in scope:** automated reference scraping, trend reports, AI image gen boards.

---

## Useful inspiration classes

| Class | What to extract | HG mapping |
|-------|-----------------|------------|
| **Aerospace systems** | MFD density, label discipline, calm alert colors | Typography, signal ladder, tri-focus |
| **Premium automotive interfaces** | Material quality, night mode depth, touch targets | Glass restraint, dark theme |
| **Tactical monitoring systems** | Peripheral status, level semantics, no panic UI | `info_area`, P0 discipline |
| **Architectural lighting** | Volumetric depth, directional wash | [lighting-and-depth-atmosphere-v0.1.md](lighting-and-depth-atmosphere-v0.1.md) |
| **Cinematic environmental depth** | Layered atmosphere — **not** literal scene | [background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md) |
| **Restrained futuristic UI** | Precision geometry, muted palette, rare accent | Identity pillars |
| **Professional tools (IDE, DAW, NLE)** | Long-session chrome, panel hierarchy | Calm-control, viewport-first |
| **Mission control / NOC (restrained)** | Status walls with hierarchy — avoid full NOC chaos | Systems mode density caps |

### Extraction rules (useful)

- Borrow **relationships** (foreground/background, label/badge).
- Borrow **lighting logic**, not movie color grading.
- Borrow **spacing rhythm**, not exact component kit.
- Ask: *«Would an operator use this 30 minutes daily?»*

---

## Dangerous inspiration classes

| Class | Why dangerous | Typical trap |
|-------|---------------|--------------|
| **Gaming HUDs** | RGB, pulse, illegible chrome | Fortnite / sci-fi shooter UI |
| **Cyberpunk compilations** | Neon noise; no signal semantics | Pinterest «cyber UI» boards |
| **Dribbble glow spam** | Demo-first; no real data | Glass + gradient + no content |
| **Generic SaaS dashboards** | Card grid equality | Analytics template #47 |
| **«AI startup» aesthetics** | Purple mesh, sparkles, hype | Landing page as product |
| **Fantasy hologram interfaces** | Scanlines, wireframe spheres | Iron Man JARVIS cosplay |
| **Notion / Linear clone mood** | Wrong anti-SaaS target if copied wholesale | Flat minimal team app |
| **Crypto / Web3 dashboards** | Neon money aesthetic | Wrong trust model |
| **Movie UI stills** | Style over function | Blade Runner interfaces |

### Rejection rules (dangerous)

- If reference **impresses in 3 seconds** but **fails with 50 rows of deadlines** — reject.
- If reference needs **explanation text** on screenshot — reject for chrome.
- If reference **animates idle** — reject for HG chrome.
- If reference is **marketing hero** — not cockpit.

---

## HG filter questions (before adopting any reference)

| # | Question |
|---|----------|
| 1 | Does it reinforce **tri-focus spatial cockpit**? |
| 2 | Does color mean **operational state**? |
| 3 | Is motion **restrained** or entertainment? |
| 4 | Is glass **architectural** or hologram fantasy? |
| 5 | Would it survive **2K daily operations**? |
| 6 | Does it match **tactical calm** emotional target? |
| 7 | Which **anti-pattern** does it risk triggering? |

All seven should pass or reference is **principle-only** extraction.

---

## Structured analysis template (for operator mood boards)

When adding a reference image (external, not in-repo):

```text
Reference ID:     REF-YYYY-MM-NN (operator assigned)
Source class:     [aerospace | automotive | … | dangerous-*]
Verdict:          ADOPT PRINCIPLE | REJECT | MIXED
Principle extracted:
HG doc mapping:
Anti-pattern risk:
Notes:
```

**No** requirement to store images in MARS repo — operator local board acceptable.

---

## Boundaries: prototype v0.1

| Observation | Boundary |
|-------------|----------|
| Spatial layout preferred | Do not reintroduce dashboard refs |
| Wireframes ASCII | Visual pack informs Phase 4 HTML, not retroactive wireframe rewrites |
| Theme draft tokens | Philosophy here; hex freeze separate |

---

## Boundaries: MARS ecosystem

| Topic | Boundary |
|-------|----------|
| MARS orchestration UI | HG is operator cockpit — not governance catalog browser |
| Bot mascots | No cartoon agents in chrome |
| n8n / automation UIs | Status display only v0.1 — don't copy flow-editor aesthetic |

---

## Cross-reference map

| HG concern | Primary doc |
|------------|-------------|
| Identity | [visual-dna-and-identity-v0.1.md](visual-dna-and-identity-v0.1.md) |
| Materials | [surface-material-language-v0.1.md](surface-material-language-v0.1.md) |
| Environment | [background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md) |
| Light | [lighting-and-depth-atmosphere-v0.1.md](lighting-and-depth-atmosphere-v0.1.md) |
| Color | [color-behavior-and-accent-philosophy-v0.1.md](color-behavior-and-accent-philosophy-v0.1.md) |
| Type | [typography-atmosphere-v0.1.md](typography-atmosphere-v0.1.md) |
| Motion mood | [motion-atmosphere-v0.1.md](motion-atmosphere-v0.1.md) |
| Dangers | [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md) |

---

## SAFE UNKNOWN

- Operator reference board location and format — external.
- Licensed imagery for atmosphere — operator legal review.
- Whether to publish reference board in-repo — TBD; not required v0.1.

---

*Last updated: 2026-05-24 — Reference analysis and visual boundaries.*
