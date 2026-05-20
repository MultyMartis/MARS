# Systems Monitor — wireframe v0.1

**view_id:** `view-systems-monitor`  
**Layout tendency:** **B — Modular Monitoring Grid**  
**Density (default):** **high** (8–12 compact blocks)  
**Parent:** [wireframe-exploration-pack-v0.1.md](wireframe-exploration-pack-v0.1.md)

---

## Purpose

Status-heavy scan: MARS, bots, n8n, workflows, uptime — **display-only** on v0.1. Operator answers «всё ли живо» за < 10 s.

---

## Layout zones

| Zone | Wireframe role |
|------|----------------|
| `zone-top-command` | Same shell; title context «Systems»; overdue chip persists |
| `zone-nav-left` | Systems **active** |
| `zone-canvas-central` | **Grid** of status blocks (primary) |
| `zone-rail-right` | **Collapsed** or incident-only strip |
| `zone-strip-bottom` | Reduced: «Back to Cockpit», refresh mock |
| `zone-overlay` | System detail panels |

---

## ASCII composition (high density)

```text
┌──────────────────────────────────────────────────────────────────────── zone-top-command
│ [HG] [Home]  SYSTEMS MONITOR                    [overdue chip] [theme] [Admin]        │
├───┬──────────────────────────────────────────────────────────────────────────────────┤
│ L2│  zone-canvas-central — GRID 3 columns (bs-s / bs-m status blocks)                │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                                 │
│   │  │ MARS        │ │ n8n         │ │ Telegram    │                                 │
│   │  │ [OK]        │ │ [WATCH]     │ │ [OK]        │                                 │
│   │  │ last: 2h    │ │ last: 15m   │ │ last: 1d    │                                 │
│   │  └─────────────┘ └─────────────┘ └─────────────┘                                 │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                                 │
│   │  │ Workflow A  │ │ Workflow B  │ │ Local store │                                 │
│   │  │ [degraded]  │ │ [offline]   │ │ [OK]        │                                 │
│   │  │ last: 5m    │ │ last: —     │ │ last: now   │                                 │
│   │  └─────────────┘ └─────────────┘ └─────────────┘                                 │
│   │  ┌──────────────────────────┐ ┌──────────────────────────┐                      │
│   │  │ INCIDENTS (bs-m)         │ │ ISSUE LOG (bs-m)         │                      │
│   │  │ [sig:WARNING] n8n queue  │ │ 2 open · 1 resolved      │                      │
│   │  └──────────────────────────┘ └──────────────────────────┘                      │
├───┴──────────────────────────────────────────────────────────────────────────────────┤
│ [← Main Cockpit]  [Refresh mock]                                                     │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Block inventory

| module_id | size | Content |
|-----------|------|---------|
| `hg-mars-monitor` | bs-s | Lane/pack summary; **display-only** label |
| `hg-bot-status` | bs-s | Per integration row |
| `hg-workflow-status` | bs-s | **NEW stub** workflow cards (sample) |
| `hg-system-health` | bs-s | Local storage / probe stub |
| `hg-incidents` | bs-m | Active warnings list |
| `hg-issue-log` | bs-m | Short log sample |

### Status glyph convention (wireframe)

| Glyph | Meaning | Sample |
|-------|---------|--------|
| `[OK]` | Healthy | Green token |
| `[WATCH]` | Attention | Accent outline |
| `[degraded]` | Partial | WARNING |
| `[offline]` | Unreachable | Muted + WARNING border |
| `last: Xm` | Last check timestamp | Static sample text |

**Degraded/offline examples required** — at least one each in grid (see ASCII).

---

## Avoiding SaaS / NOC overload

| Do | Don't |
|----|-------|
| Fixed 3-col grid of **compact** blocks | Full-width vanity charts |
| Consistent status corner (top-right) | Sparklines without labels |
| Group by system family | 20 equal «service cards» |
| Plain language labels | Datacenter jargon |
| `display-only` badge on MARS | Run / Restart buttons |
| Muted offline styling | Blinking red everything |

**Persistent signals:** only **incident strip** or top-bar chip if `[offline]` / `[degraded]` exists — not every OK row.

---

## Drill-down panels (L3)

| Click target | Overlay content |
|--------------|-----------------|
| MARS block | Links to repo, OPERATIONAL-INDEX; last export time (sample) |
| n8n block | Last run name, status text; link external n8n UI |
| Workflow card | Steps list stub; no execute |
| Incident row | Detail text + «acknowledge» stub (no backend) |

**Full page vs overlay:** stay on Systems view; overlay for detail. Switch to Main only via nav.

---

## Visible signals

| Signal type | Where |
|-------------|-------|
| System health | Per-block glyph |
| Incidents | INCIDENTS block + optional top chip |
| Deadlines | **Not** primary here — top overdue chip only |
| MARS operational | INFO/WATCH in MARS block only |

---

## Density variants

| Level | Change |
|-------|--------|
| calm | 2×2 grid only; hide issue log |
| standard | 6 core blocks |
| high | Full ASCII; incidents + log |

---

## Risks

| Risk | Mitigation |
|------|------------|
| Generic NOC dashboard | Cockpit chrome + compact blocks |
| False precision | Label «sample / mock» in HTML |
| Control plane drift | No action buttons except external links |

---

*Last updated: 2026-05-20.*
