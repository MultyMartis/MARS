# HomeGateway v4.ai — desktop viewport shell rule v0.1

**Статус:** **DRAFT** · **IMPLEMENTATION CONSTRAINT** · desktop only  
**Назначение:** каноническая **геометрия desktop shell** для MVP v1 и последующих static/HTML итераций.

**Не является:** mobile/tablet layout spec, visual redesign charter, animation rule.

**Связанные:** [viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md) · [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) · [typography-atmosphere-v0.1.md](typography-atmosphere-v0.1.md)

---

## Canonical assertion

> **HomeGateway desktop UI is a centered operational device shell — not a stretched fullscreen web dashboard.**

Оператор видит **кокпит как объект в viewport**, а не SaaS-страницу на всю ширину браузера.

---

## Desktop target viewport

| Parameter | Value |
|-----------|-------|
| Design target | **2560 × 1440** |
| Shell role | Primary desktop operational station |
| Page scroll at target | **Forbidden** — shell fits inside viewport |

На целевом разрешении **нет** document-level vertical scroll. Внутренние scroll-области допустимы позже ([viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md)).

---

## Operational wrapper (device shell)

Внутри viewport размещается **центрированный operational wrapper**:

| Parameter | Value |
|-----------|-------|
| Width | **1920px** max (`width: 100%` при меньшем viewport) |
| Height | **auto** |
| Min-height | **900px** |
| Max-height | **1080px** |
| Horizontal alignment | **center** |
| Vertical alignment | **center** |

Wrapper — **единый device shell**. В нём живут все base blocks:

- `top_bar`
- `logo`
- `favorites_used`
- `main_menu`
- `main_area`
- `info_area`
- `system_status`

Зелёный прямоугольник на operator schema (`hg_shem-v1.png`) — **только пояснительная разметка**. **Не** рендерить как UI-элемент и **не** использовать его цвет как palette token.

---

## What HG desktop is / is not

| HG desktop **is** | HG desktop **is not** |
|-------------------|------------------------|
| Centered operational device | Full-width dashboard |
| Cockpit shell / command workstation | Stretched SaaS admin page |
| Spatial interface object | Browser admin panel on 100vw |

---

## `#main_area` rule

`#main_area` остаётся **пустой операционной зоной** в MVP v1 skeleton:

- placeholder label допустим;
- контент подключается позже;
- **не** заполнять demo-widgets в scope viewport fix.

---

## Mobile / tablet

**Это правило только для desktop.**

| Now | Later |
|-----|-------|
| Desktop-first shell architecture | Dedicated mobile/tablet layout TBD |
| Basic responsive survival (fit without break) | No mobile optimization in this rule |
| Preserve centered shell intent where possible | Separate human charter required |

**Не** проектировать mobile layout в рамках этого документа.

---

## Implementation reference (MVP v1)

**Workspace:** `workspaces/homegateway-v4-ai/v1/`

Expected CSS intent:

- `html`, `body` — full viewport height, no page overflow at 2560×1440;
- outer stage — flex/grid centering;
- `.hg-device-shell` (or equivalent) — max-width 1920px, min-height 900px, max-height 1080px;
- inner `.hg-app` — fills shell, internal grid unchanged.

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Exact shell border / shadow treatment | Visual direction — not part of geometry rule |
| Tablet breakpoint handoff | Undefined until mobile charter |
| Login / pre-cockpit pages | May differ; outside cockpit shell |

---

*Last updated: 2026-05-25 — MVP v1 desktop shell geometry constraint.*
