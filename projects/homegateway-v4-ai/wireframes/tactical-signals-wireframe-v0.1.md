# Tactical Signals — wireframe v0.1

**view_id:** `view-tactical-signals`  
**Model:** **hybrid** — full view + right-rail preview on Main  
**Density (default):** **standard → high**  
**Parent:** [wireframe-exploration-pack-v0.1.md](wireframe-exploration-pack-v0.1.md)

---

## Purpose

Mission board for **deadlines, recurring reports, overdue** — urgency without panic UI.

**Entry points:**

- Main: `zone-rail-right` preview + `[→ Open Signals]`
- Mode nav: «Signals»
- Top overdue chip → Tactical filtered to OVERDUE

---

## Delivery model (canonical v0.1)

| Surface | Role |
|---------|------|
| **Rail preview** (on Main) | Top 5–8 rows; scan in < 3 s |
| **Full Tactical view** | Full list + filters + recurring section |
| **Overlay** (optional) | Single signal detail / snooze stub (future) |

**Not chosen:** rail-only forever (insufficient for monthly recurring wave).

---

## ASCII — full view

```text
┌──────────────────────────────────────────────────────────────────────── zone-top-command
│ [HG] [Home]  TACTICAL SIGNALS              [Filter ▾] [theme] [Admin]                │
├───┬──────────────────────────────────────────────────────────────────────────────────┤
│ L2│  FILTERS (horizontal chips):  [All] [Overdue] [Today] [Week] [Recurring]         │
│   │  Project: [▼ ACME]  Client: [▼ All]  Type: [▼ deadline|report|system]            │
│   │  ┌────────────────────────────────────────────────────────────────────────────┐  │
│   │  │ ACTIVE DEADLINES (bs-l signal-list)                                         │  │
│   │  │ [sig:OVERDUE]  ACME · Launch staging          due -3d   [open project]      │  │
│   │  │ [sig:CRITICAL] Beta · Client approval         TODAY     [open project]      │  │
│   │  │ [sig:WARNING]  Gamma · Content freeze         in 2d     ···               │  │
│   │  │ [sig:WATCH]    Delta · SEO check              in 5d     ···               │  │
│   │  │ [sig:INFO]     ···                                                          │  │
│   │  └────────────────────────────────────────────────────────────────────────────┘  │
│   │  ┌──────────────────────────────┐ ┌──────────────────────────────┐               │
│   │  │ RECURRING (bs-m)             │ │ UPCOMING (bs-m)              │               │
│   │  │ Monthly SEO report · ACME    │ │ Next 7 days grouped          │               │
│   │  │ Payment check · Beta         │ │                              │               │
│   │  └──────────────────────────────┘ └──────────────────────────────┘               │
├───┴──────────────────────────────────────────────────────────────────────────────────┤
│ [← Main Cockpit]                                                                     │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Signal display logic (INFO → OVERDUE)

Per [signal-system-draft-v0.1.md](../signal-system-draft-v0.1.md):

| Level | Visual priority | Sort weight | Panic? |
|-------|-----------------|-------------|--------|
| **OVERDUE** | Highest; persistent row styling | 1 | No blink; solid overdue token |
| **CRITICAL** | Strong; `due-today` badge | 2 | No full-screen red |
| **WARNING** | Warning token | 3 | — |
| **WATCH** | Outline accent | 4 | — |
| **INFO** | Muted; lower in list | 5 | — |

### State tags (orthogonal to level)

| State | Display |
|-------|---------|
| **due-today** | Badge «Today» + CRITICAL styling allowed |
| **upcoming** | «in Nd» muted text |
| **overdue** | Negative days; row never auto-hides |

**Default sort:** OVERDUE → CRITICAL → WARNING → WATCH → INFO; then by date proximity.

**Filters:** do not hide OVERDUE when filter=Today — OVERDUE always pinned section (top).

---

## Visual priority without panic UI

| Do | Don't |
|----|-------|
| Token-based color ([theme-system-draft-v0.1.md](../theme-system-draft-v0.1.md)) | Full viewport red background |
| One accent row per severity band | All rows CRITICAL red |
| Calm typography for INFO | Exclamation icons everywhere |
| Persistent OVERDUE section label | Auto-clear overdue from list |
| Count in top chip | Screaming modal on login |

---

## Persistent overdue behavior

| Rule | Wireframe / HTML intent |
|------|-------------------------|
| OVERDUE survives mode switch | Top chip on all views |
| OVERDUE visible when filter=Recurring | Pinned section |
| Row remains until manual resolve (future admin) | Sample: 2 overdue rows always |
| Rail preview always includes all OVERDUE | Then fill with CRITICAL/WATCH |

---

## Filters (draft)

| Filter | Effect |
|--------|--------|
| All | Full sorted list |
| Overdue | OVERDUE only (+ pinned anyway) |
| Today | CRITICAL + due-today + OVERDUE pinned |
| Week | WARNING+ within 7d |
| Recurring | `hg-deadline-recurring` content |
| Project / Client / Type | `data-hg-project-id`, `data-hg-client-id`, `data-hg-signal-type` |

---

## Rail preview (on Main)

```text
│ TACTICAL PREVIEW      │
│ ─────────────────     │
│ [OVERDUE] …           │
│ [CRITICAL] …          │
│ [WATCH] …             │
│ [→ Open Signals]      │
```

Max height: ~40vh scroll; **never** collapse OVERDUE rows.

---

## Overlay vs full view

| Content | Surface |
|---------|---------|
| Full lists + filters | Tactical view |
| Single deadline detail | L3 overlay optional |
| Open project | Overlay or Focus |

---

## Risks

| Risk | Mitigation |
|------|------------|
| Alarm fatigue | Sort + filter; calm INFO styling |
| Duplicate Main deadline block | Main = 3-row summary only |
| Notification blindness | Persistent chip + pinned OVERDUE |

---

*Last updated: 2026-05-20.*
