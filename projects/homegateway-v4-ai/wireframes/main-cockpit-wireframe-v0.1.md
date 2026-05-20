# Main Cockpit — wireframe v0.1

**view_id:** `view-main-cockpit`  
**Layout tendency:** **D — Hybrid Operational Cockpit**  
**Density (default):** **standard** (6–9 blocks)  
**Parent:** [wireframe-exploration-pack-v0.1.md](wireframe-exploration-pack-v0.1.md)

---

## Purpose

Default **home** after login: balanced operational overview — clients, signals, systems glance, leads, quick access — without full monitoring grid or focus minimalism.

**Ideal session:** morning scan, return between tasks, «где я в целом».

---

## Layout zones

| Zone | Wireframe role |
|------|----------------|
| `zone-top-command` | Brand, Home, global overdue chip, theme, admin, user stub |
| `zone-nav-left` | Layer 2 mode switcher (Main **active**) |
| `zone-canvas-central` | Block-screen grid (primary) |
| `zone-rail-right` | Tactical signal preview (top 5–8 rows) |
| `zone-strip-bottom` | Quick actions + clipboard shortcuts |
| `zone-overlay` | Empty until L3 open |

---

## ASCII composition (desktop ~1280px, standard density)

```text
┌──────────────────────────────────────────────────────────────────────── zone-top-command
│ [HG v4.ai]  [Home●]              [sig:OVERDUE ×2]  [theme] [Admin] [user ▾]          │
├───┬─────────────────────────────────────────────────────────────────┬──────────────────┤
│ L │                         zone-canvas-central                      │ zone-rail-right  │
│ 2 │  ┌─────────────────────┐ ┌─────────────────────┐              │ TACTICAL PREVIEW │
│   │  │ BLOCK:hg-client-list│ │ BLOCK:hg-deadline-  │              │ ──────────────── │
│ n │  │ bs-m client-card    │ │ active bs-l signal  │              │ [sig:CRITICAL]   │
│ a │  │ 3 clients sample    │ │ list (top 3 rows)   │              │ Launch ACME site │
│ v │  └─────────────────────┘ └─────────────────────┘              │ [sig:OVERDUE]    │
│   │  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐  │ SEO report ···   │
│   │  │ hg-mars-     │ │ hg-bot-      │ │ hg-leads-polygon     │  │ [sig:WATCH]      │
│   │  │ monitor bs-s │ │ status bs-s  │ │ + metacode bs-m      │  │ [→ Open Signals] │
│   │  └──────────────┘ └──────────────┘ └──────────────────────┘  │                  │
│   │  ┌─────────────────────────────────────────────────────────┐ │                  │
│   │  │ BLOCK:hg-frequent-links bs-m link-hub                    │ │                  │
│   │  └─────────────────────────────────────────────────────────┘ │                  │
├───┴─────────────────────────────────────────────────────────────────┴──────────────────┤
│ zone-strip-bottom: [Quick: staging] [Copy brief] [Open MARS doc] [clipboard ▾]          │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Block-screen inventory

| module_id | size | type | Sample content |
|-----------|------|------|----------------|
| `hg-client-list` | bs-m | client-card | 3 clients, status dot, next deadline hint |
| `hg-deadline-active` | bs-l | signal-list | 3 rows visible; «view all» → Tactical |
| `hg-mars-monitor` | bs-s | status-row | Display-only: «MARS docs · lane OK» |
| `hg-bot-status` | bs-s | status-row | n8n OK, Telegram OK (sample) |
| `hg-leads-polygon` | bs-m | lead-feed | 1 new lead sample |
| `hg-leads-metacode` | (in bs-m or separate bs-s) | lead-feed | 0–1 sample |
| `hg-frequent-links` | bs-m | link-hub | 6 links grouped |
| `hg-quick-actions` | strip | action-strip | 3–4 primary actions |

**Recurring:** 1–2 rows inside deadline block or separate `hg-deadline-recurring` bs-s — wireframe choice: **inline in deadline block footer**.

---

## Visible signals

| Location | Signals shown |
|----------|---------------|
| Top command | Global OVERDUE count chip (persistent) |
| Right rail | CRITICAL, OVERDUE, WATCH (top N) |
| Client cards | Per-client worst level dot |
| MARS/bot blocks | INFO / WATCH only (no fake CRITICAL on systems) |
| Deadline block | Mixed levels; max 1 CRITICAL row styled |

**Not on Main canvas:** full Systems grid, full Tactical filters, admin forms.

---

## Always visible vs overlay

| Always visible (L2) | Opens in overlay (L3) |
|---------------------|------------------------|
| Shell all zones | Project detail (full links, notes stub) |
| Rail top 5–8 signals | Lead row expand |
| Mini MARS/bot status | MARS detail panel (links only) |
| Client names + worst signal | Clipboard template preview |
| Admin entry (top) | Admin stub panel (optional L3 vs stub page) |
| Theme toggle | Confirm dialogs (future) |

**Full view better than overlay:** Systems Monitor (mode switch), Tactical Signals full view, Settings.

---

## Density variants (this view)

| Level | Canvas change |
|-------|---------------|
| calm | Hide frequent-links; clients 2 only; rail → chip |
| standard | As ASCII above |
| high | Add recurring block; leads split; 4th client row |

---

## Navigation hooks

| Action | Target |
|--------|--------|
| `[→ Open Signals]` on rail | Tactical Signals view |
| Client card click | Project detail **overlay** (default) or Focus mode |
| MARS block click | MARS detail overlay (display-only) |
| Bot block click | Systems Monitor **or** bot detail overlay |
| Mode nav | [navigation-shell-wireframe-v0.1.md](navigation-shell-wireframe-v0.1.md) |

---

## Risks

| Risk | Mitigation |
|------|------------|
| Dashboard card farm | Varied block sizes (s/m/l); rail for urgency |
| Redundant deadline UI | Rail = preview; canvas block = summary only |
| SaaS sidebar | Mode labels = cockpit vocabulary |
| False live data | `data-hg-display-only="true"` on MARS/bot |

---

## HTML prototype notes (future)

- `data-hg-view="main-cockpit"`
- Canvas: CSS grid `repeat(auto-fill, minmax(280px, 1fr))` — **draft**, not final
- Rail: sticky; independent scroll from canvas

---

*Last updated: 2026-05-20.*
