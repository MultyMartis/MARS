# HomeGateway v4.ai — surface behavior system v0.1

**Статус:** **DRAFT** · **PLANNING** · **POST-PROTOTYPE**  
**Назначение:** канонические **interaction states** для block-screens, rails, controls — borders, glow, elevation, dimming.

**Не является:** CSS implementation, component library.

**Связанные:** [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md) · [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) · [visual-language-direction-v0.1.md](visual-language-direction-v0.1.md)

---

## Design intent

Surfaces должны ощущаться **операционными и премиальными**, не игровыми. Состояние читается через **иерархию**, не через RGB шоу.

---

## Canonical interaction states

| State | Meaning | Typical carrier |
|-------|---------|-----------------|
| **default** | Resting surface | block-screen, nav item |
| **hover** | Pointer exploration | clickable rows, buttons, nav |
| **active** | Currently pressed / engaged | button during click |
| **selected** | Current mode, tab, row in list | `main_menu` item, filter chip |
| **focus** | Keyboard focus ring | inputs, interactive controls |
| **disabled** | Unavailable action | future-gated controls |
| **stale** | Data older than trust threshold | status blocks (future integration) |
| **loading** | Await content | block-screen skeleton |
| **overlay-open** | Shell under modal/panel | `main_area` dimmed |
| **warning** | Elevated caution (semantic) | row/block with WARNING level |
| **critical** | Highest operational emphasis | CRITICAL/OVERDUE row — not full UI red |

---

## Border behavior

| State | Border rule |
|-------|-------------|
| default | `var(--hg-border)` — 1px subtle |
| hover | Slight brighten or accent mix — **no** thick neon frame |
| selected | Accent edge **or** left rail marker — one cue only |
| focus | Focus ring via `--hg-accent` — WCAG intent |
| warning/critical | Semantic signal token on **badge/edge segment**, not entire block flood |
| overlay-open | Unchanged on hidden layers; active overlay gets full border definition |

**Anti-pattern:** rainbow borders, animated border crawl.

---

## Glow behavior

| Allowed | Forbidden |
|---------|-----------|
| Restrained `--hg-elevation` on hover/select | Pulsing glow loops |
| Signal badge micro-glow at CRITICAL | Whole-panel red glow |
| Glass edge catch-light (static) | RGB cycle, «gamer FX» |

Glow = **emphasis**, not decoration. Max **one** elevated glow focal per viewport region.

---

## Elevation behavior

| Level | Use |
|-------|-----|
| **Flat inset** | Canvas background, calm zones |
| **Surface** | block-screen default |
| **Raised** | hover, selected block, `top_bar` |
| **Overlay** | panels, modals ([depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md)) |

Elevation via shadow + subtle z — **not** exaggerated Y-translate on every hover.

---

## Interaction transitions

| Transition | Timing token | Notes |
|------------|--------------|-------|
| hover in/out | `fast` | [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md) |
| selected change | `base` | Mode switch nav |
| overlay dim | `base` | Opacity on `main_area` |
| loading skeleton | `slow` pulse optional | Prefer static skeleton |
| warning/critical | **no** flash | Instant token apply |

---

## Dimming logic

| Context | What dims |
|---------|-----------|
| overlay-open | `main_area` + optionally `info_area` (partial) |
| focus mode | Peripheral rails reduce contrast — not invisible |
| critical global | **No** full-viewport dim except overlay |

Dim target: **30–50% opacity reduction** on inactive regions (draft), preserve legibility.

---

## Block-screen state matrix (summary)

| State | Background | Border | Signal badge |
|-------|------------|--------|--------------|
| default | `--hg-surface-glass` | `--hg-border` | per level |
| hover | +5% lift | accent hint | unchanged |
| selected | slightly denser glass | accent left bar | unchanged |
| loading | skeleton | muted border | hidden or placeholder |
| stale | desaturate 10% | dashed optional | WATCH default |
| warning row | — | — | WARNING token |
| critical row | — | — | CRITICAL/OVERDUE token |

---

## Anti-patterns (explicit)

| Anti-pattern | Why forbidden |
|--------------|---------------|
| Gamer FX | Undermines operational trust |
| Excessive glow | Fatigue, illegibility on glass |
| Neon overload | Cyberpunk toy, not aerospace calm |
| Aggressive animation | Breaks long-session ergonomics |
| Skeuomorphic knobs | Fantasy hologram UI |
| Equal emphasis everywhere | Dashboard feeling |

---

## Accessibility note

Signal meaning **never** color-only — duplicate with icon + text label ([theme-system-draft-v0.1.md](theme-system-draft-v0.1.md)).

---

## SAFE UNKNOWN

- Exact opacity values — Phase 3 token freeze.
- `stale` threshold minutes — integration Phase 7.

---

*Last updated: 2026-05-24 — Surface behavior system.*
