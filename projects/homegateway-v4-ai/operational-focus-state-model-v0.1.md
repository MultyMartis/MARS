# HomeGateway v4.ai — operational focus state model v0.1

**Статус:** **DRAFT** · **PLANNING** · **POST-PROTOTYPE**  
**Назначение:** поведение кокпита при **сужении внимания** — overlay, project select, focus mode, critical, tactical expand.

**Связанные:** [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) · [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) · [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md)

---

## Core principle

**Focus states redistribute attention without amnesia.**  
Operator narrows work context; **P0 danger** and **spatial anchors** survive.

---

## Focus state catalog

| State | Trigger | Primary effect |
|-------|---------|----------------|
| **default** | Normal operation | Full tri-focus per mode |
| **overlay-open** | L3 panel/modal | Dim + freeze pointer on shell below |
| **project-selected** | Client/project card or list | Context binding; optional overlay |
| **focus-mode-active** | Focus Workspace mode or «focus this project» | Reduced peripheral chrome |
| **critical-state-active** | One or more P0 signals | Elevated chips/sections — no panic takeover |
| **tactical-panel-expanded** | Full Tactical view or expanded rail | Right column dominant for scan |

States may **combine** (e.g. overlay-open + project-selected).

---

## overlay-open

| Aspect | Behavior |
|--------|----------|
| **Dimming** | `main_area` + partial `info_area` @ 30–50% opacity |
| **Freezing** | No mode switch required; underlying mode **preserved** |
| **Peripheral reduction** | `main_menu` visible but de-emphasized |
| **Attention narrowing** | Overlay panel = foveal target |
| **Context preservation** | Close overlay → exact prior Layer 2 mode |

**Stack:** max 1 overlay + 1 confirm — [navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md).

Layer: [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) overlay 4–5.

---

## project-selected

| Aspect | Behavior |
|--------|----------|
| **Dimming** | None unless overlay opens |
| **Freezing** | Other projects visually muted in list (optional) |
| **Peripheral reduction** | Minimal on Main; stronger in Focus mode |
| **Attention narrowing** | Selected project block emphasized |
| **Context preservation** | Selection persists across overlay open/close |

**Default path:** card click → project detail **overlay** (L3), not forced mode change.

---

## focus-mode-active

| Aspect | Behavior |
|--------|----------|
| **Dimming** | Inactive blocks hidden or collapsed — not deleted |
| **Freezing** | `info_area` → compact chip or slim strip ([tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md)) |
| **Peripheral reduction** | `favorites_used` may collapse; `main_menu` icon-only |
| **Attention narrowing** | 2–4 large blocks in `main_area` |
| **Context preservation** | OVERDUE chip remains on `top_bar` (P0) |

Maps to `view-focus-workspace` / layout tendency C.

---

## critical-state-active

| Aspect | Behavior |
|--------|----------|
| **Dimming** | **No** full-screen red veil |
| **Freezing** | None — operator can still work |
| **Peripheral reduction** | INFO rows deprioritized in sort |
| **Attention narrowing** | P0 rows pinned; global chip shows count |
| **Context preservation** | Critical does not auto-switch mode |

**Sticky critical:** 1–2 rows max with strongest styling in `info_area` preview.

---

## tactical-panel-expanded

| Aspect | Behavior |
|--------|----------|
| **Dimming** | `main_area` may share width or full swap to Tactical view |
| **Freezing** | N/A — intentional scan mode |
| **Peripheral reduction** | Left nav slim |
| **Attention narrowing** | Signal lists dominate |
| **Context preservation** | «Back to Main» restores hybrid tri-focus |

Full view preferred over permanent expanded rail for monthly recurring waves.

---

## Dimming matrix (summary)

| State | main_area | info_area | top_bar | main_menu |
|-------|-----------|-----------|---------|-----------|
| overlay-open | dim | partial dim | active | de-emphasized |
| focus-mode | content reduced | compact | active | slim |
| critical-state | normal | P0 emphasis | chip | normal |
| tactical-expanded | secondary or hidden | dominant | active | slim |

---

## Freezing semantics

**Freeze** = no accidental interaction with dimmed layer, not **data freeze**.

| Frozen | Not frozen |
|--------|------------|
| Clicks on dimmed canvas | Live clock / theme |
| Mode switch (optional lock during confirm modal) | OVERDUE chip still visible |

---

## Context preservation rules

1. Closing overlay **never** changes Layer 2 mode silently.
2. Focus mode entry records **return target** (usually Main).
3. P0 signals **survive** all focus states except explicit «hide all» — **not** in v0.1.
4. Project selection ID preserved in overlay stack.

---

## Motion

Transitions use `base` token — [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md). No zoom-drama on focus enter.

---

## SAFE UNKNOWN

- Keyboard shortcut «Focus» — Phase 4+.
- Auto-enter Focus on CRITICAL — **rejected** (no hijack).

---

*Last updated: 2026-05-24 — Operational focus state model.*
