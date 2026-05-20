# HomeGateway v4.ai — layout variants analysis v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 2  
**Назначение:** канонический reframe variants A/B/C/D как **operational cockpit mode tendencies**; SaaS feeling analysis; strengths/weaknesses.

**Supersedes (partially):** [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md) § «Layout variants (Phase 2 candidates)» — старые `layout-a`…`layout-d` как competing wireframes **заменены** этой моделью.

---

## Canonical reframe (Phase 2)

| variant_id | Name | Was (Phase 1 draft — deprecated) | Now (canonical) |
|------------|------|----------------------------------|-----------------|
| **A** | **Centralized Command Cockpit** | «Full zones as diagram» | Command-center overview; narrative + control focal point |
| **B** | **Modular Monitoring Grid** | «No left rail — tabs in top» | Status-heavy grid; systems/bots/MARS |
| **C** | **Tactical Focus Workspace** | «Signal rail bottom on mobile» | Low-noise concentration; project/task focus |
| **D** | **Hybrid Operational Cockpit** | «Hub-only one scroll» | Default home; balanced hybrid |

> **A/B/C/D — не взаимоисключающие финальные макеты.**  
> Это **tendencies** operational modes; реальный cockpit **комбинирует** зоны и плотность per [operational-modes-v0.1.md](operational-modes-v0.1.md).

---

## Variant A — Centralized Command Cockpit

| Aspect | Notes |
|--------|-------|
| **Strengths** | Clear focal hierarchy; operator «in command»; good for Project View and client overview |
| **Weaknesses** | Can feel busy if every block fights for center; risks «hero dashboard» |
| **Ideal use** | Project-centric work; client status at a glance |
| **Maps to modes** | Main Cockpit (partial), **Project View** (primary) |
| **Zone emphasis** | `zone-canvas-central` dominant; rails supportive |

---

## Variant B — Modular Monitoring Grid

| Aspect | Notes |
|--------|-------|
| **Strengths** | Fast scan of many systems; comparable status tiles; NOC-like clarity |
| **Weaknesses** | Generic monitoring dashboard vibe; table/card equality |
| **Ideal use** | Systems Monitor mode; morning health check |
| **Maps to modes** | **Systems Monitor** (primary) |
| **Zone emphasis** | Grid on canvas; optional reduced left nav |

---

## Variant C — Tactical Focus Workspace

| Aspect | Notes |
|--------|-------|
| **Strengths** | Low distraction; deep work; urgent signals when needed |
| **Weaknesses** | Hides global context; operator may miss peripheral systems |
| **Ideal use** | Focus Workspace; Tactical Signals (urgency list, not grid) |
| **Maps to modes** | **Focus Workspace**, **Tactical Signals** |
| **Zone emphasis** | Minimal rails; strong central column or list |

---

## Variant D — Hybrid Operational Cockpit

| Aspect | Notes |
|--------|-------|
| **Strengths** | Best daily driver; balances clients, signals, links; matches JTBD morning scan |
| **Weaknesses** | Hardest to tune — easy to slide into cluttered dashboard |
| **Ideal use** | **Default home** — Main Cockpit |
| **Maps to modes** | **Main Cockpit** (default) |
| **Zone emphasis** | Full shell per [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md) reference diagram |

---

## Combination patterns

| Pattern | Description |
|---------|-------------|
| **D + B slice** | Main Cockpit with compact systems row (not full Systems mode) |
| **D → C transition** | «Focus this project» collapses chrome to C tendency |
| **B standalone** | Full Systems Monitor without client narrative blocks |
| **A within D** | Project card expands to A-style command layout in overlay |
| **C + tactical rail** | Focus mode keeps slim overdue strip |

**Wireframe strategy:** prototype **D (home)** + **B (systems)** + **C (focus)** as three compositions; A emerges inside Project View.

---

## Default / home recommendation

| Decision (draft) | Rationale |
|------------------|-----------|
| **Default tendency: D** | Hybrid matches majority of [ux-discovery-notes-v0.1.md](ux-discovery-notes-v0.1.md) daily flows |
| **Home mode: Main Cockpit** | `view-main-cockpit` — see [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) |
| **Not default: B alone** | Too cold for primary entry; better as explicit mode |

---

## SaaS feeling analysis

### What to avoid

| Pattern | Why it hurts HG |
|---------|-----------------|
| Generic enterprise dashboard | Erases cockpit identity; looks like bought template |
| Boring productivity-app visuals | Flat grays, rounded cards, Inter-only sameness |
| Flat CRM aesthetics | Pipeline columns, «deals» language, avatar grids |
| Excessive table / admin-panel look | Spreadsheet dominance in operational views |
| Overload of equal cards | No signal hierarchy; everything screams equally |
| «Team management software» vibe | Multi-user tropes irrelevant to solo operator |
| Sidebar with 12+ same-weight items | SaaS navigation muscle memory, not cockpit |
| Fake charts / vanity metrics | Movie dashboard without operational truth |

### What to prefer

| Pattern | Why it fits HG |
|---------|----------------|
| **Cockpit atmosphere** | Operator-at-station metaphor; purposeful chrome |
| **Operational spatiality** | Zones have roles; canvas vs rail vs strip |
| **Signal-oriented hierarchy** | Urgency visible without chaos ([signal-system-draft-v0.1.md](signal-system-draft-v0.1.md)) |
| **Layered information** | Progressive disclosure; deep in L3 overlays |
| **Focus states** | Mode C reduces noise deliberately |
| **Tactical feeling** | Deadlines and recurring as mission board, not calendar widget |
| **Calm-control UX** | Readable under long sessions; dark/light tokens |
| **High-tech but readable surfaces** | Glass/block-screen aesthetic **without** illegible glow |

### Practical usability guardrail

> **Do not drift into movie fantasy UI.**  
> Glow, scanlines, holographic chrome — только если читаемость и contrast сохранены. Primary: **scan speed**, **overload prevention** ([cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md)).

---

## Responsive notes (variants × breakpoints)

| Breakpoint | D (home) | B (systems) | C (focus) |
|------------|----------|-------------|-----------|
| Wide | Full zones | Multi-column grid | Wide central column |
| Medium | Collapse nav icons | 2-col grid | Hide right rail |
| Narrow | Stack signal section | Single column status list | Full-width focus block |

**SAFE UNKNOWN:** exact breakpoints; mobile-first order — Phase 2 wireframes.

---

## Migration note (Phase 1 → 2)

If older docs reference:

- `layout-a` = full zones diagram only → **see Variant A + D**
- `layout-b` = no left rail → **deprecated as primary variant**; partial chrome collapse in C
- `layout-c` = mobile signal bottom → **responsive tactic**, not variant name
- `layout-d` = hub one scroll → **redefined as Hybrid Operational Cockpit (default)**

---

## SAFE UNKNOWN

- Whether wireframes label frames as A/B/C/D or as mode names — cosmetic.
- Glass intensity per variant — Phase 3 visual direction.

---

*Last updated: 2026-05-20 — Phase 2 layout variant reframe.*
