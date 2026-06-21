# HomeGateway v4.ai — depth and z-layer system v0.1

**Статус:** **DRAFT** · **PLANNING** · **POST-PROTOTYPE**  
**Назначение:** предотвратить **z-index chaos** — каноническая глубина слоёв кокпита.

**Не является:** CSS file, stacking context implementation.

**Связанные:** [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md) · [operational-focus-state-model-v0.1.md](operational-focus-state-model-v0.1.md)

---

## Depth hierarchy philosophy

HG использует **мало слоёв, чётко именованных**. Глубина = **роль в операции**, не произвольное число.

**Rule:** новые UI-элементы получают слой из таблицы ниже — **не** ad-hoc `z-index: 9999`.

---

## Canonical layer stack (bottom → top)

| Order | Layer id | Description | Typical content |
|-------|----------|-------------|-----------------|
| 0 | **background** | Environmental canvas | `--hg-bg`, atmospheric gradients, subtle geometry |
| 1 | **ambient-effects** | Non-interactive atmosphere | Slow drift, grain, starfield **restrained** |
| 2 | **surfaces** | Shell + block-screens at rest | `main_area` blocks, rails, `top_bar` base |
| 3 | **raised-surfaces** | Hover, selected, elevated cards | Active block, nav selected |
| 4 | **overlays** | Dimmed backdrop + panels | Project detail, L3 panels |
| 5 | **sheets** | Higher sheets (drawer over panel) | Rare; max 1 nested |
| 6 | **tactical-alerts** | Global chips / sticky critical strip | `top_bar` OVERDUE chip — **not** modal |
| 7 | **modal-priority** | Confirm, destructive confirm | Short forms only |
| 8 | **future-notifications** | Reserved — toast/snackbar | **Not** v0.1; slot reserved |

```text
z (conceptual)
 8  future-notifications (reserved)
 7  modal-priority
 6  tactical-alerts (global chip)
 5  sheets
 4  overlays (backdrop + panel)
 3  raised-surfaces
 2  surfaces
 1  ambient-effects
 0  background
```

---

## Layer rules

| Rule | Detail |
|------|--------|
| **Single overlay stack** | Max 1 overlay + 1 confirm ([navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md)) |
| **info_area inside surfaces** | Rail is layer 2 unless expanded tactical sheet |
| **Signals not above modal** | CRITICAL row styling ≠ layer 7 |
| **Ambient never captures clicks** | layer 1 `pointer-events: none` |
| **Theme toggle** | layer 2–3, never above modal |

---

## Mapping to spatial zones

| Zone | Default layer |
|------|---------------|
| `background` / canvas env | 0–1 |
| `main_area` blocks | 2 (3 on hover) |
| `main_menu`, `info_area` | 2 |
| `top_bar` | 2–3 |
| `system_status` | 2 |
| Overlay host | 4–5 |
| Global overdue chip | 6 |

---

## Overlay vs sheet

| Type | Layer | When |
|------|-------|------|
| **Overlay backdrop** | 4 | Any L3 panel |
| **Overlay panel** | 4 (above own backdrop) | Project detail |
| **Sheet** | 5 | Only if panel stacks on another panel — avoid |

**Prefer:** mode switch (Layer 2) over sheet stack for large content.

---

## Tactical alerts layer

**Purpose:** persistent global indicators that must remain visible across overlay dim **except** true modal confirm.

| Element | Layer |
|---------|-------|
| OVERDUE count chip in `top_bar` | 6 |
| Sticky critical section header in `info_area` | 2–3 (semantic, not z-fight) |

**Not:** fullscreen red alert layer.

---

## Modal priority

| Content | Layer |
|---------|---------|
| Delete confirm | 7 |
| Short edit | 7 |
| Long admin CRUD | **full view** (Layer 2), not modal |

---

## Future notifications (reserved)

Slot 8 for optional toasts — **must not** preempt modal 7.

**v0.1:** no toast system; avoid implementing layer 8 early.

---

## Anti-patterns

| Anti-pattern | Fix |
|--------------|-----|
| Per-component z-index literals | Use layer tokens |
| `z-index: 99999` | Assign layer name |
| Signal row above modal | Keep rows in layer 2–3 |
| Multiple full-screen overlays | Stack limit 1+confirm |

---

## Draft token names (Phase 3–4 CSS)

```text
--hg-z-background: 0;
--hg-z-ambient: 10;
--hg-z-surface: 20;
--hg-z-raised: 30;
--hg-z-overlay: 40;
--hg-z-sheet: 50;
--hg-z-tactical: 60;
--hg-z-modal: 70;
--hg-z-toast: 80;  /* reserved */
```

Gaps (10) allow insertions without renumbering entire app.

---

## SAFE UNKNOWN

- Whether `info_area` expanded mode uses sheet layer 5 — likely yes on narrow breakpoints.
- Popover/tooltip layer — between raised and overlay (e.g. 35) TBD.

---

*Last updated: 2026-05-24 — Depth and z-layer system.*
