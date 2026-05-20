# HomeGateway v4.ai — cognitive load and density notes v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 2  
**Назначение:** практические ориентиры по плотности, группировке, progressive disclosure и рискам перегрузки.

**Связанные:** [operational-modes-v0.1.md](operational-modes-v0.1.md) · [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) · [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md)

---

## Core principle

**Density is a mode property, not a global constant.**  
Main Cockpit (medium) and Systems Monitor (high) intentionally differ. Forcing one density everywhere causes either boredom or overload.

---

## Density scaling (draft targets)

| Mode | Target density | Max visible primary blocks (guideline) |
|------|----------------|----------------------------------------|
| Main Cockpit | medium | 6–9 block-screens on canvas |
| Systems Monitor | high | 8–12 compact status blocks |
| Focus Workspace | low–medium | 2–4 large blocks |
| Tactical Signals | medium–high | 1 dominant list + 2 supporting |
| Project View | medium | 4–7 grouped by category |
| Quick Actions | low | 4–8 actions |
| Settings | low | 3–6 controls |
| Admin (future) | medium lists | paginate; avoid infinite scroll tables |

**Block sizes:** [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) S/M/L — prefer **fewer L** on high-density views.

---

## Scan speed

| Goal | Tactic |
|------|--------|
| < 3 s morning scan | Signal rail + 2–3 hero blocks on Main |
| < 10 s systems check | Grid with consistent status glyph positions |
| Deep work | Focus mode hides non-project blocks |

**Grouping rules:**

1. **One visual group = one operational question** («какие дедлайны», «какие боты»).
2. **Align status indicators** — same corner in every block (e.g. top-right).
3. **Typography ladder** — 3 levels max per block-screen.

---

## Calm vs active zones

```text
┌────────────────────────────────────────────────────────────┐
│  CALM zones: top bar (except critical badge), settings,     │
│              focus canvas background, inactive nav           │
├────────────────────────────────────────────────────────────┤
│  ACTIVE zones: signal rail, tactical lists, overdue rows,  │
│                live attention indicators                     │
├────────────────────────────────────────────────────────────┤
│  NEUTRAL zones: client cards, link hubs, clipboard           │
└────────────────────────────────────────────────────────────┘
```

| Zone | Calm / Active | Notes |
|------|---------------|-------|
| `zone-rail-right` | Active | Motion restraint — no blinking |
| `zone-canvas-central` | Neutral–active | Depends on mode |
| `zone-top-command` | Calm | Single global alert max |
| `zone-strip-bottom` | Neutral | Actions, not alarms |

---

## Persistent alerts

| Rule | Rationale |
|------|-----------|
| **One global persistent strip** | Multiple strips → blindness |
| **Overdue survives mode switch** | Operator must not lose danger context in Focus |
| **Snooze is human action** | No auto-dismiss of critical (future) |
| **Differentiate overdue vs due-today** | [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md) |

In Focus mode: compress to **chip/badge**, not full rail.

---

## Hidden / deep information

| Surface | Depth |
|---------|-------|
| Client card on Main | Name, status, next deadline |
| Project overlay (L3) | Full links, notes, history (future) |
| MARS block | Summary + «open repo» external |
| Admin | Full CRUD — **never** on Main canvas v0.1 |

**Progressive disclosure:**

1. Summary on canvas.
2. Expand block inline (optional).
3. Overlay panel.
4. Full mode switch (Project / Systems).

---

## Progressive disclosure checklist

- [ ] New operator sees **readable** Main, not all modules at once.
- [ ] «Show more» for long link lists.
- [ ] Systems detail behind block click, not all rows expanded.
- [ ] Settings advanced prefs collapsed by default.

---

## Risks and mitigations

| Risk | Symptoms | Mitigation |
|------|----------|------------|
| **Cockpit chaos** | No focal point; every block animated | Mode-specific layouts; max block count |
| **Signal fatigue** | All items red/orange | Strict signal levels; calm defaults |
| **Dashboard overload** | 20 equal cards | Multi-view; move grids to Systems mode |
| **Notification blindness** | Ignored rail | Reduce noise; elevate only true critical |
| **Mode disorientation** | «Where am I?» | Clear active mode indicator Layer 2 |
| **Fantasy UI illegibility** | Glow over contrast | Phase 3 token discipline |

---

## Cognitive ergonomics by operator session length

| Session | Recommended modes | Density note |
|---------|-------------------|----------------|
| < 5 min | Main, Quick Actions | medium |
| 15–30 min | Project, Focus | low–medium |
| Check-in only | Tactical, Systems | high scan, short stay |
| Hours | Focus + occasional Main glance | lowest sustained load |

---

## Wireframe acceptance criteria (Phase 2)

1. Operator can name **current mode** without reading URL.
2. **Critical signal** visible from Main within one eye movement (rail or badge).
3. Focus mode has **≥30% less** visual elements than Main (rough count).
4. No view requires **horizontal scroll** on 1280px desktop (draft).

---

## SAFE UNKNOWN

- User-toggle density (compact/comfortable) — Settings future.
- Accessibility font scaling interaction with glass blocks — Phase 3–4.
- Empirical validation — no formal user testing yet.

---

*Last updated: 2026-05-20 — Phase 2 cognitive load notes.*
