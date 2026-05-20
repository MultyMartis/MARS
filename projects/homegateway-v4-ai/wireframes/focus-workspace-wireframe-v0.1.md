# Focus Workspace — wireframe v0.1

**view_id:** `view-focus-workspace`  
**Layout tendency:** **C — Tactical Focus Workspace**  
**Density (default):** **calm → standard** (2–4 large blocks)  
**Parent:** [wireframe-exploration-pack-v0.1.md](wireframe-exploration-pack-v0.1.md)

---

## Purpose

Active **single project** work session: links, tasks, materials — **low noise**, high concentration.

**Entry:** «Focus» on project card; or Project View → «Enter Focus».

---

## Layout zones

| Zone | Wireframe role |
|------|----------------|
| `zone-top-command` | Slim: project name breadcrumb, overdue chip, exit Focus |
| `zone-nav-left` | **Collapsed icons only** or hidden (breakpoint) |
| `zone-canvas-central` | 1× xl + 2× m blocks |
| `zone-rail-right` | **Hidden** — replaced by top chip |
| `zone-strip-bottom` | Project-scoped quick actions only |
| `zone-overlay` | Optional task detail |

---

## ASCII composition (calm)

```text
┌──────────────────────────────────────────────────────────────────────── zone-top-command
│ [← Main]  FOCUS · Client ACME · Project Website Redesign     [OVERDUE ×1] [theme]      │
├───┬────────────────────────────────────────────────────────────────────────────────────┤
│ ≡ │  ┌────────────────────────────────────────────────────────────────────────────┐  │
│   │  │ BLOCK:hg-project-detail bs-xl                                               │  │
│   │  │ Status · phase · next milestone · [sig:WARNING] deadline in 2d              │  │
│   │  └────────────────────────────────────────────────────────────────────────────┘  │
│   │  ┌─────────────────────────────┐ ┌─────────────────────────────┐                  │
│   │  │ PROJECT LINKS bs-m          │ │ CURRENT TASKS bs-m          │                  │
│   │  │ staging · WP · Figma · repo │ │ □ Review mockups            │                  │
│   │  │ admin/site links            │ │ □ Send handoff line         │                  │
│   │  └─────────────────────────────┘ └─────────────────────────────┘                  │
│   │  ┌────────────────────────────────────────────────────────────────────────────┐  │
│   │  │ MARS / PROJECT MATERIALS bs-m (display-only links)                          │  │
│   │  └────────────────────────────────────────────────────────────────────────────┘  │
├───┴────────────────────────────────────────────────────────────────────────────────────┤
│ [Open staging] [Copy handoff] [Exit Focus → Main]                                      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Must include (checklist)

- [x] Active client/project focus in header
- [x] Project links (staging, admin, Figma, repo)
- [x] Admin/site links in links block
- [x] Current tasks (sample checklist, non-persistent v0.1)
- [x] MARS/project materials (display-only links)
- [x] Low-noise layout (rails reduced)
- [x] Critical signal persistence (overdue chip)

---

## Hidden vs visible

| Hidden in Focus | Remains visible |
|-----------------|-----------------|
| Full client list | Active project only |
| Leads blocks | — |
| Full tactical rail | OVERDUE chip (+ optional CRITICAL tooltip) |
| Systems grid | — |
| Frequent links (global) | Project-scoped links only |
| Other clients’ deadlines | This project’s deadlines in xl block |

---

## Return to Main Cockpit

| Control | Behavior |
|---------|----------|
| `[← Main]` top-left | Layer 2 → `view-main-cockpit`; preserve last scroll **optional** |
| `Exit Focus` bottom strip | Same |
| Mode nav «Cockpit» | Same |
| Esc (future) | Exit Focus if no overlay open |

**Do not** auto-exit on overlay close.

---

## Project detail opening

| Gesture | Result |
|---------|--------|
| From Main: click client | Default: **overlay** project panel; button «Enter Focus» |
| From Focus: already in detail | Inline xl block, not second overlay |
| Expand task | Small L3 overlay or inline expand |

---

## Visible signals

| Rule | Implementation |
|------|----------------|
| Project-scoped only | Filter sample `data-hg-project-id` |
| Persistent OVERDUE | Top chip even in calm mode |
| No global WATCH spam | Hide INFO/WATCH not tied to project |
| WARNING on milestone | In xl block header |

---

## Density variants

| Level | Change |
|-------|--------|
| calm | xl + links only; tasks in overlay |
| standard | As ASCII |
| high | Add clipboard block — **discouraged** for Focus |

---

## Risks

| Risk | Mitigation |
|------|------------|
| Too empty | xl block rich enough; tasks block |
| Lost global urgency | Persistent overdue chip |
| Duplicate Project View | Focus = session chrome; Project View = structure hub |

---

*Last updated: 2026-05-20.*
