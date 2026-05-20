# HomeGateway v4.ai — cockpit layout zones v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 2 aligned

Возможные **зоны layout** cockpit shell. Зоны **персистентны** across operational modes; **canvas composition** меняется per mode.

**Phase 2:** layout variants A/B/C/D = **mode tendencies**, не competing finals — [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md).

---

## Принцип

HomeGateway Main Cockpit = **shell** (постоянные зоны) + **canvas** (композиция block-screens) + **overlay** (popups).

Зоны описывают **роли**, не пиксельную сетку.

---

## Zone catalog

| zone_id | Название | Роль | Типичное содержимое |
|---------|----------|------|---------------------|
| `zone-top-command` | **Top command bar** | Глобальный контекст, быстрый доступ | Logo/title, clock optional, global search stub, **admin entry**, user menu stub |
| `zone-nav-left` | **Left navigation / system rail** | Секции cockpit | Clients, Signals, MARS, Bots, Leads, Settings — icons + labels |
| `zone-canvas-central` | **Central cockpit canvas** | Основная композиция block-screens | Client cards, project panels, link hubs |
| `zone-rail-right` | **Right signal rail** | Срочность и alerts | Deadlines, overdue, due-today, recurring highlights |
| `zone-strip-bottom` | **Bottom quick action strip** | Частые действия | Quick actions, clipboard shortcuts |
| `zone-overlay` | **Popup / overlay layer** | Детали без смены страницы | Project detail panel, confirm dialogs, expanded lead |
| `zone-admin-access` | **Admin access point** | Вход в admin | Может жить в top bar **и** дублироваться в settings — **одна primary** |
| `zone-theme` | **Theme switch area** | Dark / light | Toggle в settings block или top bar |
| `zone-status-indicators` | **Status indicators** | Ambient health | Connection stub, last refresh mock, theme icon |

---

## Reference layout (non-binding)

```text
┌────────────────────────────────────────────────────────────────── zone-top-command
│  HG v4.ai          [status indicators]     [theme]  [admin entry]  [user]      │
├───┬──────────────────────────────────────────────────────────┬─────────────────┤
│   │                                                          │  zone-rail-right │
│ n │              zone-canvas-central                          │  · deadlines    │
│ a │         ┌──────────┐ ┌──────────┐ ┌──────────┐           │  · recurring    │
│ v │         │ block    │ │ block    │ │ block    │           │  · overdue      │
│   │         └──────────┘ └──────────┘ └──────────┘           │                 │
│ l │         ┌────────────────────┐ ┌──────────┐               │                 │
│ e │         │ block (project)  │ │ MARS disp│               │                 │
│ f │         └────────────────────┘ └──────────┘               │                 │
│ t │                                                          │                 │
├───┴──────────────────────────────────────────────────────────┴─────────────────┤
│                    zone-strip-bottom (quick actions · clipboard)                │
└────────────────────────────────────────────────────────────────────────────────┘
        ▲
        zone-overlay (full viewport, z-index above all)
```

---

## Zone ↔ screen relationships

| Zone | Related screens ([screen-map](screen-map-v0.1.md)) |
|------|-----------------------------------------------------|
| `zone-nav-left` | Switches hub vs `scr-mars-monitor`, etc. |
| `zone-canvas-central` | `scr-cockpit-main`, embedded `scr-project-detail` |
| `zone-rail-right` | `scr-signals-deadlines` content |
| `zone-overlay` | `scr-popup-overlay` |

---

## Layout variants → operational mode tendencies (canonical Phase 2)

**Полный анализ:** [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md)

| variant_id | Name | Mode tendency | Shell notes |
|------------|------|---------------|-------------|
| **A** | Centralized Command Cockpit | Project View, partial Main | Canvas-dominant |
| **B** | Modular Monitoring Grid | Systems Monitor | Grid canvas; rails optional slim |
| **C** | Tactical Focus Workspace | Focus, Tactical Signals | Minimal rails |
| **D** | Hybrid Operational Cockpit | **Main Cockpit (default)** | Reference diagram below |

> Старые определения `layout-a`…`layout-d` (competing wireframes) **deprecated** — не использовать.

**Reference diagram** ниже ≈ tendency **D** (default home), не единственный layout продукта.

---

## Responsive intent (draft)

| Breakpoint | Draft behavior |
|------------|----------------|
| Wide | All zones visible |
| Medium | Collapse left rail to icons |
| Narrow | Signal rail → stacked section; bottom strip sticky |

**SAFE UNKNOWN:** exact breakpoints.

---

## Theme + zones

- Top bar и rails: `var(--hg-surface)` или subtle glass.
- Canvas: `var(--hg-bg)` с block-screens на `var(--hg-surface-glass)`.
- Signal rail: допускается чуть выше contrast для signal tokens.

---

## Static MVP implication

Static build должен **продемонстрировать хотя бы один полный shell** с:

- top command bar (admin entry + theme),
- canvas с 3+ block-screens,
- signal rail или его эквивалент-секция,
- bottom strip или quick actions block,
- один popup mock.

Не обязательно все variants.

---

## SAFE UNKNOWN

- Fixed vs scrollable rails.
- Whether `zone-nav-left` lists clients or only sections.
- Pinning signal rail on scroll.

---

*Last updated: 2026-05-20 — Phase 2 variant reframe.*
