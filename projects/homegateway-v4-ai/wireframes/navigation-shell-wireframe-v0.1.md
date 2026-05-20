# Navigation shell — wireframe v0.1

**Назначение:** persistent **L1 shell** + **L2 mode switching** + hooks to **L3** — для HTML prototype.

**Upstream:** [navigation-hierarchy-v0.1.md](../navigation-hierarchy-v0.1.md) · [cockpit-layout-zones-v0.1.md](../cockpit-layout-zones-v0.1.md)

---

## Layer 1 — Access / shell (always on)

```text
┌─────────────────────────────────────────────────────────────┐
│ L1: zone-top-command                                         │
│  · Logo / product mark                                       │
│  · Home control (→ Main Cockpit)                             │
│  · Global overdue chip (persistent)                          │
│  · Theme switch (dark/light)                                 │
│  · Admin entry (stub)                                        │
│  · User menu stub                                            │
├────┬────────────────────────────────────────────────────────┤
│ L1 │ L2 mode nav (zone-nav-left)  │  VIEWPORT (swappable)    │
│    │                              │  + optional rails        │
├────┴────────────────────────────────────────────────────────┤
│ L1: zone-strip-bottom (optional per view)                    │
└─────────────────────────────────────────────────────────────┘
         L3: zone-overlay (covers viewport, not nav)
```

| Element | Layer | Persists across L2? |
|---------|-------|---------------------|
| Top command | 1 | Yes |
| Theme, Admin | 1 | Yes |
| Overdue chip | 1 | Yes |
| Mode nav | 2 chrome | Yes (labels update active) |
| Bottom strip | 1–2 | Configurable per view |
| Canvas content | 2 | Swaps |

---

## Layer 2 — Mode switcher (left rail)

### Mode list (draft labels)

| mode_id | Nav label (RU draft) | Icon hint |
|---------|----------------------|-----------|
| `view-main-cockpit` | Кокпит | home |
| `view-tactical-signals` | Сигналы | alert |
| `view-systems-monitor` | Системы | grid |
| `view-focus-workspace` | Фокус | focus |
| `view-project` | Проекты | folder |
| `view-quick-actions` | Действия | bolt |
| `view-settings` | Настройки | gear |

**Admin:** top bar only (not primary rail item) — [admin-entry notes](../admin-entry-and-future-crud-notes-v0.1.md).

### Current mode indicator

| Requirement | Wireframe |
|-------------|-----------|
| Active mode | Left border accent + label weight |
| Inactive | Muted |
| Focus mode active | Nav shows Focus highlighted; or «exit» in top bar only |
| View title | Top bar secondary text «SYSTEMS MONITOR» optional |

**HTML:** `data-hg-view` on `<main>` + `aria-current="page"` on active nav link.

---

## Layer 3 — Overlays / detail

See [overlay-and-popup-behavior-v0.1.md](overlay-and-popup-behavior-v0.1.md).

Shell **stays mounted**; overlay dims canvas, not mode nav (nav remains clickable to switch mode — closes overlay).

---

## Back / Home behavior

| Control | Action |
|---------|--------|
| **Home** (logo or label) | `view-main-cockpit`; close L3 |
| **← Main** (contextual) | Same from Systems / Tactical / Focus exit |
| Browser back (future) | Map to view stack if SPA; **SAFE UNKNOWN** |
| Admin stub | Separate stub route or overlay; Home returns to Main |

**Focus exception:** `Exit Focus` = Main, not previous arbitrary view.

---

## View switching (HTML prototype)

```text
Single index.html + view sections (display:none|.is-active)
  OR
Multi-page: cockpit.html, systems.html, … (simpler MPA wireframe)
```

**Pack recommendation:** start **single document, view-swap** for overlay z-index practice; split pages later if needed.

| Approach | Pros | Cons |
|----------|------|------|
| Single doc + JS view swap | Overlay stack, shared shell | Slightly more JS |
| MPA | Simple deploy | Overlay cross-page harder |

---

## Keyboard-friendly notes (future, not v0.1 impl)

| Key | Intended behavior |
|-----|-------------------|
| `1`–`5` | Jump modes (configurable) |
| `Esc` | Close top overlay; second Esc exit Focus |
| `?` | Shortcut help overlay |
| `/` | Focus search stub (top bar) |
| `g h` | Go home (vim-style optional) |

Document only — implement in static MVP Phase 4 selectively.

---

## Responsive shell (draft)

| Breakpoint | Nav | Rail |
|------------|-----|------|
| ≥1280px | Full labels | Right rail on Main |
| 1024–1279 | Icons + tooltip | Rail below canvas or drawer |
| <1024 | Bottom sheet mode picker | Rail → Tactical link only |

---

## Anti-SaaS nav checklist

- [ ] ≤ 7 primary mode items
- [ ] No «Analytics / Team / Billing»
- [ ] Home always one click
- [ ] Overdue never only inside submenu

---

*Last updated: 2026-05-20.*
