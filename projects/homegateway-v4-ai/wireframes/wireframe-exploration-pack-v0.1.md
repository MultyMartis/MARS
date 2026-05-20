# HomeGateway v4.ai — Wireframe Exploration Pack v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 2 wireframes  
**Назначение:** единый пакет low-fidelity compositions для первого **HTML wireframe prototype**.

**Не является:** HTML/CSS, Figma, deployed app, backend design.

---

## Pack scope

| # | Deliverable | File | Mode / topic |
|---|-------------|------|--------------|
| 1 | Main Cockpit | [main-cockpit-wireframe-v0.1.md](main-cockpit-wireframe-v0.1.md) | D — Hybrid |
| 2 | Systems Monitor | [systems-monitor-wireframe-v0.1.md](systems-monitor-wireframe-v0.1.md) | B — Grid |
| 3 | Focus Workspace | [focus-workspace-wireframe-v0.1.md](focus-workspace-wireframe-v0.1.md) | C — Focus |
| 4 | Tactical Signals | [tactical-signals-wireframe-v0.1.md](tactical-signals-wireframe-v0.1.md) | View + rail hybrid |
| 5 | Navigation shell | [navigation-shell-wireframe-v0.1.md](navigation-shell-wireframe-v0.1.md) | L1/L2/L3 |
| 6 | Overlays | [overlay-and-popup-behavior-v0.1.md](overlay-and-popup-behavior-v0.1.md) | Layer 3 |
| 7 | Static readiness | [static-prototype-readiness-checklist-v0.1.md](static-prototype-readiness-checklist-v0.1.md) | Phase 4 prep |

**Out of pack v0.1 (defer):** Project View full wireframe, Settings mode, Admin CRUD screens — referenced from screen map only.

---

## HTML-first rationale

| Factor | Why HTML wireframe |
|--------|-------------------|
| Layering / z-index | Overlay stack hard to judge in static Figma |
| Signal density | Real scroll + font rendering |
| Hover / focus | Future keyboard nav validation |
| Theme tokens | Dark/light switch on real CSS variables |
| Responsive | Breakpoint behavior, rail collapse |
| MARS workflow | Aligns with Gulp/static frontend lane when workspace opens |

---

## View relationship map

```text
                    ┌─────────────────┐
                    │  Login (mock)   │
                    └────────┬────────┘
                             ▼
              ┌──────────────────────────────┐
              │   Navigation Shell (L1)       │
              │   top · nav · strip · overlay   │
              └──────────────┬───────────────┘
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
   Main Cockpit        Systems Monitor      Focus Workspace
   (default D)          (B grid)             (C minimal)
         │                   │                   │
         ├──── Tactical Signals (full or rail)──┤
         │                   │                   │
         └─────── L3 Overlays (project, detail) ─┘
```

**Cross-navigation:** см. [navigation-shell-wireframe-v0.1.md](navigation-shell-wireframe-v0.1.md).

---

## Shared wireframe conventions

### Block-screen placeholders

В ASCII: `[BLOCK:id size type]` — maps to [block-screen-taxonomy-v0.1.md](../block-screen-taxonomy-v0.1.md).

| Notation | Meaning |
|----------|---------|
| `bs-s` | Compact |
| `bs-m` | Standard |
| `bs-l` | Wide list |
| `bs-xl` | Hero / focus |

### Signal notation

`[sig:LEVEL]` — INFO, WATCH, WARNING, CRITICAL, OVERDUE per [signal-system-draft-v0.1.md](../signal-system-draft-v0.1.md).

### Zone notation

`zone-*` per [cockpit-layout-zones-v0.1.md](../cockpit-layout-zones-v0.1.md).

### Fidelity rules

- Grayscale / semantic labels OK in HTML later; pack uses text labels.
- No pixel-perfect spec — spacing tokens in Phase 3–4.
- Sample data names illustrative only.

---

## Density experiments (pack-level)

Три уровня для HTML prototype toggles (class or `data-hg-density`):

### Calm

| Attribute | Value |
|-----------|-------|
| **When** | Focus Workspace; Settings; operator fatigue |
| **Block count (canvas)** | 2–4 |
| **Signal visibility** | OVERDUE + CRITICAL only in persistent chip; rest in expand |
| **Risks** | Missed WATCH items |
| **Example** | Focus: 1× xl project + 1× m links + chip strip |

### Standard (default)

| Attribute | Value |
|-----------|-------|
| **When** | Main Cockpit; Project View; Tactical (medium) |
| **Block count** | 6–9 (Main), 4–7 (Project) |
| **Signal visibility** | Rail shows top 5–8 rows; levels all visible in Tactical |
| **Risks** | Drift to dashboard card farm |
| **Example** | Main wireframe composition (see main-cockpit doc) |

### High-density

| Attribute | Value |
|-----------|-------|
| **When** | Systems Monitor; Tactical full view |
| **Block count** | 8–12 compact (Systems) |
| **Signal visibility** | Status glyph grid; full deadline list |
| **Risks** | NOC/SaaS overload, scan fatigue |
| **Example** | Systems monitor 3×4 grid of `bs-s` status blocks |

**HTML prototype note:** implement as `data-hg-density="calm|standard|high"` on `<body>` or `main` for experimentation — not production feature flag claim.

---

## Anti-patterns (wireframe gate)

- [ ] No 12 equal hero cards on Main
- [ ] No full-page navigation for project detail (prefer L3 panel first)
- [ ] No hidden OVERDUE when entering Focus
- [ ] No «Run workflow» / orchestration buttons on MARS/bot blocks
- [ ] No CRM pipeline columns
- [ ] No illegible glow-only hierarchy

---

## Wireframe → HTML prototype mapping (preview)

| Wireframe artifact | Future HTML (workspace) |
|--------------------|-------------------------|
| Shell zones | `hg-shell`, `hg-zone--*` |
| Mode views | `hg-view` + `data-hg-view` |
| Block-screen | `.hg-block-screen` + `data-hg-module-id` |
| Overlay host | `#hg-overlay-host` |
| Sample data | `data/*.json` or inline `data-hg-*` |

Details: [static-prototype-readiness-checklist-v0.1.md](static-prototype-readiness-checklist-v0.1.md).

---

## Phase 2 exit (this pack)

| Criterion | State |
|-----------|-------|
| Main + Systems + Focus wireframes | ✓ docs |
| Tactical + shell + overlay specs | ✓ docs |
| Density experiment definitions | ✓ this doc |
| Static readiness checklist | ✓ doc |
| HTML files in repo | **not started** (by design) |

---

## SAFE UNKNOWN

- Exact grid columns at 1280 / 1440 / 1920px.
- Whether Tactical is separate HTML page or same document view-swap.
- Gulp vs plain npm scripts in workspace — align at workspace charter.

---

*Last updated: 2026-05-20 — Wireframe Exploration Pack v0.1.*
