# HomeGateway v4.ai — motion and transition charter v0.1

**Статус:** **DRAFT** · **PLANNING** · **POST-PROTOTYPE**  
**Назначение:** каноническая **философия движения** — timing, easing, переходы modes/overlays/scroll.

**Не является:** animation library, Framer implementation.

**Связанные:** [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md) · [operational-focus-state-model-v0.1.md](operational-focus-state-model-v0.1.md) · [viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md)

---

## Why motion in HG

Motion supports **orientation** and **calm continuity**, not entertainment.

| Motion should feel | Motion must NOT feel |
|--------------------|----------------------|
| Restrained | Flashy |
| Premium | Playful / bouncy |
| Operational | Gaming UI |
| Atmospheric | Cartoony easing |

---

## Global timing philosophy

**Rule:** если движение заметно больше 400 ms без причины — слишком медленно для UI; если < 80 ms без opacity — слишком резко для overlay.

Предпочтение: **короткие, предсказуемые** переходы; длинные только для overlay enter/exit.

---

## Canonical duration tokens

| Token | Duration (draft) | Use |
|-------|------------------|-----|
| **fast** | 120–160 ms | hover, chip toggle, focus ring |
| **base** | 200–280 ms | mode content swap fade, overlay dim, nav selected |
| **slow** | 320–400 ms | overlay panel slide, large surface reveal |

**v0.1 static prototype:** CSS variables only; values illustrative until Phase 3 freeze.

Suggested CSS custom properties (future):

```text
--hg-motion-fast:  150ms;
--hg-motion-base:  240ms;
--hg-motion-slow:  360ms;
```

---

## Easing philosophy

**Recommended curve:** ease-out for enter, ease-in for exit; **avoid** elastic/bounce.

| Token | Curve (draft) | Feel |
|-------|---------------|------|
| **standard** | `cubic-bezier(0.22, 1, 0.36, 1)` | Smooth deceleration — premium |
| **exit** | `cubic-bezier(0.4, 0, 1, 1)` | Quick leave |
| **linear** | `linear` | Scroll fade masks only |

**Anti-pattern:** `spring(1, 80, 10, 0)` style overshoot.

---

## Cockpit calmness rules

1. **No infinite loops** except ambient background (ultra-subtle, optional).
2. **No blink** on signals — CRITICAL is steady state.
3. **One motion at a time** per region — не cascade 5 fades.
4. **Respect reduced motion** — `prefers-reduced-motion: reduce` → instant or opacity-only.

---

## Fade rules

| Scenario | Motion |
|----------|--------|
| Mode switch (`main_area` content) | Cross-fade `base` or instant if reduced motion |
| Overlay backdrop | Opacity `base` |
| Signal row insert | Prefer instant; optional fade `fast` |
| Theme switch dark/light | Colors `base`; no spin |

---

## Overlay motion

| Element | Enter | Exit |
|---------|-------|------|
| Backdrop dim | opacity `base` | opacity `fast` |
| Side panel | translate 12–16px + opacity `slow` | reverse `base` |
| Center modal | scale 0.98→1 + opacity `base` | opacity `fast` |

Panel never slides from random angles; **consistent right or center** per [wireframes/overlay-and-popup-behavior-v0.1.md](wireframes/overlay-and-popup-behavior-v0.1.md).

---

## Mode transitions

Shell zones (`top_bar`, `main_menu`, `info_area`) **static** — only `main_area` content animates.

| Transition | Motion |
|------------|--------|
| Main → Systems | Content fade/swap `base` |
| Main → Focus | Optional rail collapse **without** dramatic zoom |
| Any → Tactical | List emphasis — no «alarm zoom» |

---

## Scroll indicators & masks

| Element | Motion |
|---------|--------|
| Top/bottom fade mask | Static gradient — no animation |
| Scroll hint chevron | Opacity pulse **optional** `slow` — OFF by default v0.1 |
| Internal scroll | Native behavior — no fake inertia |

See [viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md).

---

## Hover transitions

| Target | Property | Token |
|--------|----------|-------|
| Nav item | background, border | `fast` |
| Block-screen | border, shadow | `fast` |
| Button | background | `fast` |
| Link | underline opacity | `fast` |

No scale-up > 1.02 on operational blocks.

---

## Ambient background motion (optional Phase 3+)

| Allowed | Forbidden |
|---------|-----------|
| Slow parallax drift 60s+ period | Fast starfields |
| Subtle gradient shift | Hologram scanlines |
| Static noise texture | Flashing grids |

---

## Relationship to theme

Motion tokens **orthogonal** to color tokens — both semantic ([theme-system-draft-v0.1.md](theme-system-draft-v0.1.md)).

---

## SAFE UNKNOWN

- Per-view motion profiles — likely unified charter first.
- Lottie / video backgrounds — **not** planned v0.1.

---

*Last updated: 2026-05-24 — Motion and transition charter.*
