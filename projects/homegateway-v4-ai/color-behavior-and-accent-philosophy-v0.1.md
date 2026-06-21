# HomeGateway v4.ai — color behavior and accent philosophy v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** канон **поведения цвета** — operational signals first, zones, accents, dark/light themes.

**Не является:** final hex values (see [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md) for token map).

**Связанные:** [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md) · [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md) · [information-priority-model-v0.1.md](information-priority-model-v0.1.md)

---

## Core principle

> **HG colors are operational signals first.**

Color communicates **state and priority** — not brand rainbow, not decoration, not gamer RGB.

**Restraint increases clarity:** muted chrome makes signal colors trustworthy.

---

## Color zones (spatial + semantic)

| Zone | Color behavior |
|------|----------------|
| **Neutral zones** | Shell chrome, borders, primary text — desaturated blue-gray family |
| **Ambient zones** | Background, P3 hints — lowest saturation |
| **Tactical zones** | `info_area` — signal ladder visible; row bodies neutral |
| **Signal-only colors** | INFO, WATCH, WARNING, CRITICAL, OVERDUE tokens |
| **Focus accents** | `--hg-accent` — nav selected, CTA, focus ring |
| **Critical accents** | CRITICAL/OVERDUE + `--hg-danger` (destructive) — bounded use |

---

## Neutral zones

| Element | Rule |
|---------|------|
| `top_bar`, rails | No signal colors except chips/badges |
| Block body text | `--hg-text-primary` / secondary |
| Borders | `--hg-border` — not accent-colored by default |

Neutrals carry **structure** — not emotion.

---

## Ambient zones

| Element | Rule |
|---------|------|
| `--hg-bg` | Deep navy/charcoal (dark) or cool gray (light) |
| Environmental geometry | 3–8% opacity accent or neutral |
| `system_status` | Muted; P3 |

P3 **never** uses CRITICAL red for decoration.

---

## Tactical zones

| Element | Rule |
|---------|------|
| Rail preview rows | Neutral row; colored badge/edge |
| Section headers | Muted uppercase labels |
| Sort bands | OVERDUE top — semantic header tint optional, restrained |

Full rainbow in rail = **failure**.

---

## Signal-only colors

Canonical ladder ([signal-system-draft-v0.1.md](signal-system-draft-v0.1.md)):

| Level | Color role |
|-------|------------|
| INFO | Cool muted — calm |
| WATCH | Distinct but low urgency |
| WARNING | Amber family — caution |
| CRITICAL | Strong — today/tomorrow |
| OVERDUE | Saturated red — persistent; distinct from WARNING |

**Rules:**

- Signal color on **badge, icon, label, edge segment** — not full block flood.
- Meaning duplicated: color + icon + text ([surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md)).
- Escalation monotonic — no skip to red for attention.

---

## Focus accents

| Use | Token |
|-----|-------|
| Active nav | `--hg-accent` |
| Primary CTA | `--hg-accent` |
| Focus ring | `--hg-accent` |
| Link hover | derived accent mix |

**Accent family (draft):** cyan / electric blue — **restrained**, single hue family.

### When accent is allowed

- Interactive affordance
- Selected state
- Primary action in block

### When accent is forbidden

- Decorative borders on every block
- Background gradients in accent hue
- Non-interactive labels

---

## Critical accents

| Use | Token |
|-----|-------|
| CRITICAL / due-today | `--hg-signal-critical` |
| OVERDUE | `--hg-signal-overdue` |
| Destructive confirm | `--hg-danger` — label clarity |

**Not** interchangeable without operator-visible label.

---

## When accent colors are allowed (summary)

| Allowed | Forbidden |
|---------|-----------|
| One accent family for UI chrome | Rainbow widget headers |
| Signal tokens on semantics | Random colorful charts |
| Theme toggle, selected nav | RGB cycling borders |
| Single global overdue chip | Multiple screaming banners |

---

## Where color should remain muted

| Region | Why |
|--------|-----|
| `main_area` default blocks | P1 work — not alarm wall |
| Background | P3 — atmosphere only |
| Inactive nav | Peripheral until selected |
| Focus mode periphery | Reduced contrast — not invisible |

---

## Dark / light theme behavior

| Theme | Posture |
|-------|---------|
| **Dark (primary)** | Immersive cockpit — deep bg, restrained accent glow, full signal saturation on badges |
| **Light (alternate)** | Tactical daylight — desaturated signals, stronger borders, maintained WCAG contrast |

Both themes: **semantic tokens only** — no hardcoded hex in components after freeze.

Toggle: calm cross-fade ([motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md)) — no spin.

---

## Forbidden color patterns

| Pattern | Why |
|---------|-----|
| **Rainbow UI** | Destroys signal semantics |
| **RGB gamer accents** | Wrong identity |
| **Uncontrolled gradients** | Dashboard marketing aesthetic |
| **Random colorful widgets** | Equal emphasis overload |
| **Color-only rows** | Accessibility failure |
| **Neon on neutral chrome** | Cyberpunk drift |

---

## Relationship to theme tokens

This philosophy **governs** [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md). Token freeze Phase 3 assigns concrete values — behavior rules here are normative.

---

## SAFE UNKNOWN

- Exact hex per signal level — illustrative in theme draft until review.
- Color-blind palettes — human verify Phase 3–4; icon+label mandatory now.
- Chart/data viz colors — defer until real data widgets.

---

*Last updated: 2026-05-24 — Color behavior and accent philosophy.*
