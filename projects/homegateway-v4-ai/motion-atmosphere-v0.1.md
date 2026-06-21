# HomeGateway v4.ai — motion atmosphere v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** **эмоциональный слой** движения — как motion ощущается оператору; timing/easing остаются в [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md).

**Не является:** animation library, keyframe catalog, Framer spec.

**Связанные:** [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md) · [operational-focus-state-model-v0.1.md](operational-focus-state-model-v0.1.md) · [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md)

---

## Motion atmosphere (one line)

> **HG motion feels like a calm, intelligent station adjusting posture — not a game UI celebrating every click.**

---

## How motion should feel

| Quality | Operator reading |
|---------|------------------|
| **Restrained** | Motion noticed only when orienting |
| **Floating** | Soft deceleration; no hard snaps |
| **Calm** | No adrenaline pacing |
| **Intelligent** | Predictable directions (panel from right/center) |
| **Operational** | Supports task continuity |
| **Atmospheric** | Background may breathe ultra-slow |

---

## How motion must NOT feel

| Anti-quality | Symptom |
|--------------|---------|
| **Playful** | Bounce, elastic overshoot |
| **Flashy** | Flash transitions, spinners everywhere |
| **Gaming UI** | Scale punch, particle bursts on hover |
| **Hyperactive** | Cascaded fades, parallax on chrome |
| **Cartoony** | Spring physics, wiggle |

---

## Relationship to motion charter

| Layer | Document |
|-------|----------|
| **Timing, easing, tokens** | [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md) — fast/base/slow |
| **Emotional intent, mood** | This document |

Charter answers **how long**; atmosphere answers **how it feels**.

---

## Overlay motion mood

| Aspect | Mood |
|--------|------|
| Enter | Room dims; panel arrives with confidence — not drama |
| Exit | Faster leave than enter — respectful of time |
| Stack | Rare; no stacking carnival |

Operator retains **spatial memory** — shell still implied under dim.

---

## Hover mood

| Target | Mood |
|--------|------|
| Nav item | Quiet acknowledgment — background shift |
| Block-screen | Lift hint — not jump |
| Button | Solid state change |
| Link | Underline fade |

**No** scale > 1.02 on operational blocks. **No** ripple theatrics.

---

## Signal pulse philosophy

| Rule | Detail |
|------|--------|
| CRITICAL | **Steady** — no blink |
| OVERDUE | Persistent visibility — no pulse loop |
| New row insert | Prefer instant; optional fast fade |
| Global chip | Static count update |

Pulse loops = **alert fatigue** + gamer UI — forbidden.

---

## Ambient motion philosophy

| Allowed | Forbidden |
|---------|-----------|
| 60s+ gradient or parallax drift | Fast starfields |
| Static grain | Hologram scanlines |
| None (static env) | Flashing grids |

Ambient motion is **optional** and **first disabled** under `prefers-reduced-motion`.

---

## Mode transition mood

Shell **static** — only `main_area` content breathes.

| Transition | Mood |
|------------|------|
| Main → Systems | Calm swap — scan posture |
| Main → Focus | Periphery quiets — not zoom theater |
| → Tactical full | List emphasis — no alarm zoom |

Mode change = **posture shift**, not scene cut.

---

## Theme switch mood

Dark ↔ light: color cross-fade **base** — no spin, no flash.

Operator stays **in same station** — different lighting conditions.

---

## Scroll motion mood

| Element | Mood |
|---------|--------|
| Internal scroll | Native — honest |
| Fade masks | Static gradients |
| Chevron hint | OFF by default v0.1 |

No fake inertia, no rubber-band theater.

---

## Cognitive pairing

| Motion type | Supports |
|-------------|----------|
| Restrained overlay | calm-control |
| Static signals | tactical trust |
| Static shell on mode | spatial memory |
| Reduced motion path | accessibility respect |

---

## Anti-patterns (motion atmosphere)

| Pattern | Emotional damage |
|---------|------------------|
| Celebration on save | Playful — wrong product |
| Shake on error | Anxiety |
| Infinite loading shimmer everywhere | Hyperactive |
| Staggered list cascade | Dashboard demo |

Cross-ref: [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md).

---

## SAFE UNKNOWN

- Per-view motion profiles — likely unified first.
- Lottie icons — not planned v0.1.
- Sound/haptic — out of scope.

---

*Last updated: 2026-05-24 — Motion atmosphere.*
