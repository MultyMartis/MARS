# HomeGateway v4.ai — navigation hierarchy v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 2  
**Назначение:** layered navigation для multi-view cockpit — transitions, overlays, mode switching.

**Связанные:** [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) · [operational-modes-v0.1.md](operational-modes-v0.1.md) · [screen-map-v0.1.md](screen-map-v0.1.md)

---

## Design intent

Navigation HG v4.ai должна ощущаться как **cockpit mode switching** и **operational depth**, а не как **SaaS app sidebar** с бесконечными равноправными разделами.

**Предпочтительно:** spatial continuity, signal-oriented entry points, calm-control transitions.  
**Избегать:** generic enterprise left-rail с 12 одинаковыми пунктами, breadcrumb hell, modal stacking без иерархии.

Подробнее anti-patterns: [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md) § SaaS feeling analysis.

---

## Three-layer model

```text
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1 — Primary cockpit access                                │
│  Login → Cockpit shell · Home · Global command bar               │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│  LAYER 2 — Major operational modes (views)                       │
│  Main · Systems · Focus · Tactical · Project · Quick · Settings  │
│  Admin (future)                                                  │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│  LAYER 3 — Deep panels / overlays / detail screens               │
│  Project detail panel · Signal item expand · Confirm · Admin form │
└─────────────────────────────────────────────────────────────────┘
```

---

## Layer 1 — Primary cockpit access

| Element | Role | Persistence |
|---------|------|-------------|
| Login (mock v0.1) | Gate to cockpit | Session (mock) |
| **Home / Cockpit root** | Return to `view-main-cockpit` | Always available in top command |
| **Top command bar** (`zone-top-command`) | Global context, search stub, theme, admin entry, user | Persistent across Layer 2 |
| **Status indicators** (`zone-status-indicators`) | Ambient health | Persistent |

**Philosophy:** Layer 1 — **якорь идентичности** («я в HomeGateway cockpit»), не навигация по контенту.

---

## Layer 2 — Major operational modes

| mode_id | Label (draft UI) | Entry points (draft) |
|---------|------------------|----------------------|
| `view-main-cockpit` | Cockpit / Home | Default after login; Home control |
| `view-systems-monitor` | Systems | Left rail section; status alert deep link |
| `view-focus-workspace` | Focus | Project «focus» action; keyboard future |
| `view-tactical-signals` | Signals | Right rail header; overdue badge |
| `view-project` | Projects | Clients nav; project cards |
| `view-quick-actions` | Actions | Bottom strip expand; shortcut |
| `view-settings` | Settings | Top bar gear |
| `view-admin` | Admin | Admin entry (stub → future) |

### Mode switching philosophy

| Principle | Implementation hint (Phase 2+) |
|-----------|--------------------------------|
| **Intentional switch** | Mode change = deliberate operator action |
| **No hidden auto-routing** | Alerts highlight, не перехватывают view без confirm |
| **Visual continuity** | Shell zones stable; canvas content swaps |
| **State badge** | Active mode indicated in nav (not only URL) |
| **Last mode memory** | Optional Settings — SAFE UNKNOWN |

### Persistent vs temporary navigation

| Type | Examples | Behavior |
|------|----------|----------|
| **Persistent** | Top bar, primary mode switcher, bottom quick strip (optional) | Visible across Layer 2 |
| **Temporary** | Overlay project panel, signal detail, confirm dialog | Layer 3; dismiss returns to prior Layer 2 |
| **Contextual** | «Open in Focus» from Project card | Sets Focus context then switches mode |

---

## Layer 3 — Deep panels / overlays

| Pattern | Use when | Avoid when |
|---------|----------|------------|
| **Side panel** | Project detail, medium content | Full admin CRUD lists |
| **Center modal** | Confirm, short forms | Long scrolling content |
| **Full overlay** | Rare immersive detail | Default for every click |
| **Inline expand** | Single block-screen grow | Replacing entire view |

**Popup host:** `scr-popup-overlay` / `zone-overlay` — единый слой z-index above shell.

### Transition rules (draft)

1. **Overlay open:** dim canvas slightly; keep mode context visible at edge.
2. **Overlay close:** restore exact Layer 2 mode (no surprise mode change).
3. **Stack limit:** max 1 overlay + 1 nested confirm; no infinite stack.
4. **Escape / close:** consistent top-right or Esc (Phase 4).

---

## Navigation transitions map

```text
Login ──► Main Cockpit (L2)
              │
    ┌─────────┼─────────┬──────────┬──────────┐
    ▼         ▼         ▼          ▼          ▼
 Systems   Tactical   Project    Focus    Quick Actions
 Monitor   Signals     View     Workspace    Mode
    │         │         │          │
    └────┬────┴────┬────┴──────────┘
         ▼         ▼
    L3: detail   L3: overlay
    panel        (project, signal item)
```

**Cross-links (examples):**

- Tactical signal row → Project View (L2) or project overlay (L3).
- Systems Monitor MARS block → external MARS doc (new tab) — not in-app orchestration.
- Main client card → Project View.

---

## Zone ↔ navigation mapping

| Shell zone | Layer | Notes |
|------------|-------|-------|
| `zone-top-command` | 1 | Home, global actions |
| `zone-nav-left` | 2 | Primary mode switcher (draft) |
| `zone-canvas-central` | 2 content | Mode-specific block composition |
| `zone-rail-right` | 2 entry → 3 | Tactical shortcut; may mirror Tactical view |
| `zone-strip-bottom` | 1–2 | Quick Actions; persistent optional |
| `zone-overlay` | 3 | Popups |

**Phase 2 note:** `zone-nav-left` may list **modes** not **clients** — clients live in Project View / canvas cards. SAFE UNKNOWN until wireframes.

---

## Popup vs overlay vs full page

| Mechanism | Layer | Typical content |
|-----------|-------|-----------------|
| **Popup (modal)** | 3 | Confirm, short edit |
| **Overlay panel** | 3 | Project detail, expanded lead |
| **Full page / view swap** | 2 | Systems Monitor, Settings |
| **External tab** | — | MARS repo, WP-admin, n8n UI |

**Avoid:** turning every Layer 2 mode into a modal — modes need spatial room.

---

## Anti-SaaS navigation checklist

| Avoid | Prefer |
|-------|--------|
| 15 equal sidebar items | 5–7 modes + grouped modules |
| «Dashboard / Analytics / Reports / Team» | Cockpit / Signals / Systems / Projects |
| Hamburger hiding primary modes | Visible mode switcher on desktop |
| Breadcrumb for every block | Context header in canvas |
| Settings buried 3 levels | Top bar + dedicated Settings mode |

---

## Relationship to routing (future)

Phase 4 may implement:

- `/cockpit` → Main
- `/cockpit/systems` → Systems Monitor
- `/cockpit/project/:id` → Project View

**Phase 2:** navigation semantics first; URL scheme SAFE UNKNOWN ([screen-map-v0.1.md](screen-map-v0.1.md)).

---

## SAFE UNKNOWN

- Icon-only vs icon+label nav at medium breakpoints.
- Whether Focus is separate route or chrome flag on Project View.
- Keyboard shortcuts map — Phase 4+.
- Mobile: bottom tab bar vs collapsible mode drawer.

---

*Last updated: 2026-05-20 — Phase 2 navigation hierarchy.*
