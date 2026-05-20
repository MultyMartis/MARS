# Overlay and popup behavior — wireframe v0.1

**Назначение:** Layer 3 patterns — types, triggers, stack rules, overlay vs full page.

**Upstream:** [navigation-hierarchy-v0.1.md](../navigation-hierarchy-v0.1.md)

---

## Overlay host

```text
#hg-overlay-host (fixed, z-index above canvas, below toast future)
  └── .hg-overlay-backdrop (dim 40–60%)
  └── .hg-overlay-panel (center | right | full)
```

Shell L1/L2 **not** covered by backdrop blur on nav (optional: dim only canvas).

---

## Overlay types

| type_id | Name | Trigger | Panel style | Content |
|---------|------|---------|-------------|---------|
| `ovl-quick-info` | Quick info | Icon ⓘ on block | Small center | 2–3 lines help, link |
| `ovl-project-detail` | Project detail | Client card click | **Right sheet** 40% width | Links, status, deadlines |
| `ovl-clipboard-reveal` | Clipboard reveal | Clipboard action | Small center | Template preview + Copy |
| `ovl-mars-detail` | MARS detail | MARS block | Medium center | Display-only links, lane text |
| `ovl-bot-detail` | Bot/system detail | Status block | Medium center | Last run, external link |
| `ovl-admin-stub` | Admin stub | Admin entry | Medium center | «Phase 5» message + back |
| `ovl-confirm` | Confirmation | Future risky action | Small center | Confirm / Cancel |

---

## Wireframe — right sheet (project detail)

```text
│ canvas (dimmed)                    │ PROJECT DETAIL          │
│                                    │ Client ACME             │
│                                    │ ─────────────────       │
│                                    │ Links · status          │
│                                    │ [Enter Focus]           │
│                                    │ [Close ×]               │
```

---

## Wireframe — center modal (confirm)

```text
│           ┌─────────────────────┐
│           │ Confirm action?     │
│           │ [Cancel] [Confirm]  │
│           └─────────────────────┘
│ canvas dimmed                      │
```

---

## When overlay vs full view

| Use overlay (L3) | Use full view (L2) |
|--------------------|---------------------|
| Project detail from Main | Systems Monitor |
| MARS/bot detail drill-down | Tactical Signals full list |
| Clipboard preview | Focus Workspace |
| Admin stub message | Settings (future page) |
| Confirm destructive (future) | Project list hub |
| Quick info tooltips | Login |

**Rule:** if operator stays > 2 min or needs filters → **L2 view**, not stacked overlays.

---

## Preventing overlay chaos

| Rule | Description |
|------|-------------|
| **Stack max** | 1 panel + 1 nested confirm; no third level |
| **Mode switch closes** | Changing L2 mode closes all overlays |
| **Home closes** | Home clears overlay host |
| **Same target replace** | Opening new project replaces panel content, no second sheet |
| **No overlay-on-overlay same width** | Replace, don't stack sheets |
| **Scroll lock** | `body` scroll locked when modal center; sheet scrolls internally |
| **Focus trap** | Tab cycles inside panel (Phase 4 a11y) |

---

## Overlay vs popup terminology

| Term in docs | HTML pattern |
|--------------|--------------|
| **Overlay** | Backdrop + panel (project, detail) |
| **Popup / modal** | Center confirm, small info |
| **Rail** | Not overlay — part of L2 layout |

---

## Behavior matrix

| From view | Action | Result |
|-----------|--------|--------|
| Main | Click client | `ovl-project-detail` |
| Main | MARS block | `ovl-mars-detail` |
| Systems | Click n8n | `ovl-bot-detail` |
| Focus | Task expand | inline or small `ovl-quick-info` |
| Any | Admin | `ovl-admin-stub` or stub page |
| Tactical | Row click | `ovl-project-detail` or filter project |

---

## Display-only guardrails

MARS and bot overlays:

- Text: «Display-only · sample data»
- Links: external `target="_blank"`
- **No** Run / Trigger / Deploy buttons

---

## HTML prototype hooks (future)

```html
<div id="hg-overlay-host" hidden>
  <motion not required>
  <div class="hg-overlay" data-hg-overlay-type="project-detail" role="dialog" aria-modal="true">
```

- `data-hg-open-overlay="project-detail"`
- `data-hg-close-overlay` on backdrop click (optional) and × button
- Event: `hg:overlay-open`, `hg:overlay-close` for JS stub

---

## Risks

| Risk | Mitigation |
|------|------------|
| Modal fatigue | Prefer right sheet for detail |
| Lost context | Dim canvas, keep nav visible |
| Mobile sheet height | Full-width sheet <1024px |

---

*Last updated: 2026-05-20.*
