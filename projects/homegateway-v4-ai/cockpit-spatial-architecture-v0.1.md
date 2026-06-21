# HomeGateway v4.ai — cockpit spatial architecture v0.1

**Статус:** **DRAFT** · **PLANNING** · **POST-PROTOTYPE** (operator review v0.1)  
**Назначение:** каноническая **пространственная** модель кокпита после Prototype v0.1 — зоны, tri-focus, философия cockpit environment.

**Не является:** HTML/CSS, routing, runtime, wireframe pixels.

**Supersedes (interpretation):** dashboard-grid reading of HG; «равная сетка карточек» как главная метафора.

**Связанные:** [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md) (legacy zone_id map) · [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) · [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md) · [viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md)

---

## Каноническое утверждение (post–Prototype v0.1)

> **HomeGateway v4.ai — spatial operational cockpit environment with layered tactical awareness.**  
> Не dashboard, не SaaS panel, не CRM, не admin UI, не коллекция страниц.

Оператор работает в **слоях** (shell → canvas → overlay → tactical periphery), а не «листает сайт».

---

## Почему HG — не dashboard

| Dashboard-мышление | Cockpit-реальность HG |
|--------------------|------------------------|
| Равноправные виджеты на одной странице | **Роли зон** — навигация / работа / тактика |
| Scroll всей страницы | **Viewport-first** — внутренние scroll-области ([viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md)) |
| «Обзор метрик» | **Операционная работа** + периферийная осведомлённость |
| Notification center справа | **info_area** — tactical awareness, не inbox ([tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md)) |
| Один layout на все задачи | **Multi-view** modes с общим shell ([multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md)) |

Dashboard перегружает внимание **равенством блоков**. Cockpit направляет внимание **пространственной иерархией**.

---

## Почему пространственная иерархия важна

1. **Периферийное зрение** — оператор видит CRITICAL/OVERDUE, не отрываясь от `main_area`.
2. **Стабильность якорей** — `top_bar`, `main_menu`, `info_area` не «прыгают» при смене mode (Layer 2).
3. **Когнитивная экономия** — левая колонка = «куда иду», центр = «что делаю», правая = «что требует внимания».
4. **Ambient workspace** — фон и атмосфера остаются спокойными; активность локализована в surfaces ([visual-language-direction-v0.1.md](visual-language-direction-v0.1.md)).

---

## Tri-focus model (canonical)

```text
┌──────────────────────────────────────────────────────────────────────── top_bar
│ logo · system_status · global context · theme · admin · user              │
├───┬──────────────────────────────────────────────────────────────┬────────┤
│ L │                         CENTER                                │ RIGHT  │
│ E │                    main_area                                  │ info   │
│ F │         active operational work · block-screens               │ _area  │
│ T │         project · clients · systems glance · focus content    │ tactical│
│   │                                                               │ aware. │
│ nav│ main_menu · favorites_used                                   │ rail   │
└───┴──────────────────────────────────────────────────────────────┴────────┘
         ▲                    ▲                                        ▲
    NAVIGATION          OPERATIONAL WORK                    PERIPHERAL INTELLIGENCE
```

| Focus | Zones | Operator question |
|-------|-------|-------------------|
| **LEFT** | `main_menu`, `favorites_used` | «Куда переключиться? Что открыть часто?» |
| **CENTER** | `main_area` | «Над чем работаю сейчас?» |
| **RIGHT** | `info_area` | «Что горит / что на горизонте без паники?» |

**Не tri-page:** три колонки — **один viewport**, одна сессия, shared `top_bar`.

---

## Zone catalog (canonical spatial IDs)

Зоны **персистентны** across operational modes; меняется **содержимое** `main_area` и плотность `info_area`, не исчезновение shell.

### `top_bar`

| Aspect | Definition |
|--------|------------|
| **Purpose** | Глобальный командный рубеж кокпита: идентичность, время/контекст (optional), глобальные chips, theme, admin entry, user stub |
| **Cognitive role** | Якорь «я в HG»; calm-control band |
| **Attention role** | Scan за < 2 s; **не** основная рабочая зона |
| **Interaction density** | Low — редкие клики |
| **Visibility** | Always visible; single global alert chip max ([cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md)) |
| **Spatial hierarchy** | Z-layer: raised surface above canvas ([depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md)) |
| **Desktop** | Full width; fixed height band |

**Legacy map:** `zone-top-command` (partial — см. `logo`, `system_status`).

---

### `logo`

| Aspect | Definition |
|--------|------------|
| **Purpose** | Brand / product identity; optional Home → `view-main-cockpit` |
| **Cognitive role** | Spatial anchor top-left |
| **Attention role** | Passive landmark |
| **Interaction density** | Minimal (click = home) |
| **Visibility** | Always in `top_bar` |
| **Spatial hierarchy** | Child of `top_bar`; не конкурирует с signals |
| **Desktop** | Fixed left segment of `top_bar` |

---

### `main_menu`

| Aspect | Definition |
|--------|------------|
| **Purpose** | Layer 2 **operational mode** switcher — Cockpit, Systems, Focus, Signals, Projects, Settings ([navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md)) |
| **Cognitive role** | «Режим станции», не SaaS sidebar с 15 равными пунктами |
| **Attention role** | Peripheral until mode change |
| **Interaction density** | Medium on switch; low while working |
| **Visibility** | Persistent left column (wide desktop); icon collapse (medium) |
| **Spatial hierarchy** | LEFT tri-focus; below `top_bar` |
| **Desktop** | Vertical rail; 5–7 modes, not client list as primary |

**Legacy map:** `zone-nav-left`.

**SAFE UNKNOWN:** clients in nav vs canvas-only — prefer canvas / Project view.

---

### `favorites_used`

| Aspect | Definition |
|--------|------------|
| **Purpose** | High-frequency destinations: links, quick resources, «used lately» — **не** полный каталог ссылок |
| **Cognitive role** | Muscle-memory shortcuts в навигационной колонке |
| **Attention role** | Secondary to `main_menu`; supports P1 operational ([information-priority-model-v0.1.md](information-priority-model-v0.1.md)) |
| **Interaction density** | Medium |
| **Visibility** | Persistent in left column or compact strip under menu |
| **Spatial hierarchy** | LEFT tri-focus; subordinate to `main_menu` |
| **Desktop** | Scroll **internal** if list long — не page scroll |

**Legacy map:** частично `hg-frequent-links` на canvas → **migrate tendency:** compact favorites left, full hub in `main_area`.

---

### `main_area`

| Aspect | Definition |
|--------|------------|
| **Purpose** | **Active operational work** — block-screens, project canvas, systems grid, tactical full list (mode-dependent) |
| **Cognitive role** | Primary task surface |
| **Attention role** | **Foveal** — majority of session time |
| **Interaction density** | High (mode-dependent) |
| **Visibility** | Always occupies center; may dim under overlay ([operational-focus-state-model-v0.1.md](operational-focus-state-model-v0.1.md)) |
| **Spatial hierarchy** | CENTER tri-focus; largest flex region |
| **Desktop** | Flex-grow; internal scroll regions only |

**Legacy map:** `zone-canvas-central`.

---

### `info_area`

| Aspect | Definition |
|--------|------------|
| **Purpose** | **Peripheral tactical awareness** — deadlines, overdue, watch items, ambient system hints |
| **Cognitive role** | «Периферийный радар»; не notification feed |
| **Attention role** | Peripheral scan; escalates via level tokens, not modal spam |
| **Interaction density** | Low–medium (row click → project / tactical view) |
| **Visibility** | Persistent right column (wide); collapsible / chip on Focus ([tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md)) |
| **Spatial hierarchy** | RIGHT tri-focus |
| **Desktop** | Fixed width rail; internal scroll + fade masks |

**Legacy map:** `zone-rail-right`.

**Not:** inbox, news column, Slack-style feed.

---

### `system_status`

| Aspect | Definition |
|--------|------------|
| **Purpose** | Ambient health: connection stub, last refresh mock, theme indicator, optional clock |
| **Cognitive role** | «Кокпит жив» — P3 ambient ([information-priority-model-v0.1.md](information-priority-model-v0.1.md)) |
| **Attention role** | Glance only; escalate only on true degradation (future integration) |
| **Interaction density** | Very low |
| **Visibility** | Embedded in `top_bar` (and optionally bottom strip echo) |
| **Spatial hierarchy** | Part of command band |
| **Desktop** | Top-right cluster near theme/admin |

**Legacy map:** `zone-status-indicators`.

---

## Additional shell elements (cross-zone)

| Element | Typical placement | Notes |
|---------|-------------------|-------|
| **Bottom quick strip** | Below `main_area` full width | `zone-strip-bottom` — actions, not alarms |
| **Overlay layer** | Above all shell | Layer 3 — project detail, confirms ([navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md)) |

---

## Calm-control philosophy

| Principle | Spatial expression |
|-----------|-------------------|
| **Calm chrome** | `top_bar`, inactive `main_menu` — low contrast motion |
| **Active work in center** | Density follows mode, not global max |
| **Tactical periphery** | `info_area` may be «hot» but restrained visually |
| **No panic layout** | CRITICAL ≠ full-screen red ([tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md)) |

---

## Ambient workspace feeling

- Background = **environmental depth**, not flat SaaS gray ([visual-language-direction-v0.1.md](visual-language-direction-v0.1.md)).
- Block-screens = **instruments on glass**, not cards in a grid.
- Operator ощущает **station**, не **browser tab with widgets**.

---

## Cockpit cognition

| Concept | Meaning in HG |
|---------|---------------|
| **Spatial memory** | «Сигналы всегда справа» снижает поиск |
| **Mode = posture** | Systems Monitor = scan; Focus = narrow ([operational-modes-v0.1.md](operational-modes-v0.1.md)) |
| **Progressive depth** | Summary in `main_area` → overlay → full mode |
| **Peripheral vigilance** | `info_area` без отвлечения от центра |

---

## Relationship to multi-view

Spatial shell **stable**; `main_area` composition swaps per `view-*`. См. [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md).

Default home: Hybrid (`view-main-cockpit`) — full tri-focus visible.

---

## Migration: legacy zone_id → spatial ID

| Legacy `zone_*` | Canonical spatial |
|-----------------|-------------------|
| `zone-top-command` | `top_bar` (+ children) |
| `zone-nav-left` | `main_menu` + `favorites_used` |
| `zone-canvas-central` | `main_area` |
| `zone-rail-right` | `info_area` |
| `zone-status-indicators` | `system_status` |
| `zone-strip-bottom` | bottom strip (unchanged id in docs until v0.2) |
| `zone-overlay` | overlay layer (L3) |

Старые wireframes остаются valid с этой картой соответствия.

---

## SAFE UNKNOWN

- Exact pixel widths for `info_area` — Phase 3–4.
- `favorites_used` left-only vs split with `main_area` link hub — operator preference TBD.
- Mobile tri-focus collapse order — wireframes TBD.

---

*Last updated: 2026-05-24 — Post–Prototype v0.1 spatial canon.*
