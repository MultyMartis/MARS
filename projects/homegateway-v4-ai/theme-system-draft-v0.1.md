# HomeGateway v4.ai — theme system draft v0.1

**Статус:** **DRAFT** · **PLANNING** · **STATIC-FIRST**

Семантические токены для **dark** и **light** темы с первого static MVP. High-tech cockpit aesthetic: glass surfaces, controlled glow, signal colors.

**Правило:** дизайн использует **semantic tokens**, не hardcoded colors. Dark и light — **first-class** с Phase 4 static build.

**Layout context:** [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md) · **Signals:** [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md)

---

## Режимы

| Mode | Token prefix (draft) |
|------|----------------------|
| Dark (default for cockpit) | `:root[data-theme="dark"]` |
| Light | `:root[data-theme="light"]` |

Переключатель — в `hg-settings` / shell header; persistence **SAFE UNKNOWN** (localStorage likely Phase 4).

---

## Token groups (semantic map)

| Group | Tokens | Назначение |
|-------|--------|------------|
| **background** | `--hg-bg` | Фон страницы / cockpit canvas |
| **surface** | `--hg-surface` | Плотные панели (rails, top bar) |
| **glass surface** | `--hg-surface-glass`, `--hg-glass-alpha` | Block-screen полупрозрачность |
| **text** | `--hg-text-primary` | Основной текст |
| **muted text** | `--hg-text-secondary` | Вторичный текст, hints |
| **accent** | `--hg-accent` | CTA, active nav, focus ring |
| **border** | `--hg-border` | Границы block-screen |
| **glow** | `--hg-elevation` | Свечение / emphasis |
| **signal colors** | `--hg-signal-info` … `--hg-signal-watch` … `--hg-signal-warning` | INFO, WATCH, WARNING |
| **critical colors** | `--hg-signal-critical` | CRITICAL, due-today |
| **overdue colors** | `--hg-signal-overdue` | OVERDUE persistent |
| **shadow/elevation** | `--hg-block-shadow` (derived) | Тень block-screen |
| **blur/transparency** | `--hg-glass-alpha`, backdrop-filter on glass | Blur stack |

Дополнительно:

| Token | Group |
|-------|-------|
| `--hg-danger` | destructive / error (не дублировать OVERDUE без label) |

### Производные (v0.1)

- `--hg-block-shadow` → fn(`--hg-elevation`)
- `--hg-link-hover` → mix accent + surface

---

## Dark theme (draft values — illustrative)

Значения **не нормативны** до visual direction (Phase 3); задают направление:

| Token | Role hint |
|-------|-----------|
| `--hg-bg` | deep navy / charcoal |
| `--hg-surface-glass` | white @ 6–12% alpha + blur |
| `--hg-accent` | cyan / electric blue restrained |
| `--hg-signal-overdue` | saturated red, distinct from WARNING |

---

## Light theme (draft)

| Token | Role hint |
|-------|-----------|
| `--hg-bg` | cool gray / off-white |
| `--hg-surface-glass` | dark @ 4–8% alpha or frosted white |
| `--hg-text-primary` | near-black |
| Signal colors | slightly desaturated vs dark for contrast |

---

## Block-screen styling rules

1. Background block-screen = `var(--hg-surface-glass)` + backdrop-filter (degrade gracefully).
2. Border = `var(--hg-border)`; glow only via `--hg-elevation`.
3. Signal badge = semantic signal token only.
4. **Запрет:** raw `#RRGGBB` в компонентных SCSS после token freeze.

---

## Accessibility intent (draft)

- Text on glass: minimum contrast target WCAG AA where feasible — **human verify** in Phase 3–4.
- Signal colors **не** единственный носитель смысла — дублировать icon/label.

---

## SAFE UNKNOWN

- CSS architecture (SCSS layers vs CSS modules) — Phase 4.
- Font stack — Phase 3 visual direction.
- Motion tokens — future; keep minimal v0.1.

---

*Last updated: 2026-05-20 — Phase 1 token groups expanded.*
