# HomeGateway v4.ai — viewport and scroll philosophy v0.1

**Статус:** **DRAFT** · **PLANNING** · **POST-PROTOTYPE**  
**Назначение:** канон **viewport-first cockpit** — no page scroll, internal regions, accessibility.

**Связанные:** [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) · [desktop-viewport-shell-rule-v0.1.md](desktop-viewport-shell-rule-v0.1.md) · [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md)

---

## Canonical assertion

> **HG behaves like an operational environment, not a scrolling website.**

The **viewport is the station window**. Content moves **inside** instruments, not by dragging the entire room.

---

## Viewport-first cockpit

| Principle | Implementation intent |
|-----------|----------------------|
| Shell fills **100vh** (desktop) | `top_bar` + tri-focus columns + optional bottom strip |
| No **document body** scroll for main shell | `overflow: hidden` on cockpit root |
| Resize reflow | Internal regions flex; layout reserved ([loading-and-empty-state-philosophy-v0.1.md](loading-and-empty-state-philosophy-v0.1.md)) |

---

## No page scroll

| Allowed | Forbidden |
|---------|-----------|
| Scroll inside `main_area` block lists | Scroll entire HG page to find footer |
| Scroll inside `info_area` rail | Long SaaS landing-style page |
| Scroll inside overlay panel content | Double scrollbars (body + panel) without intent |

**Exception:** Login (pre-cockpit) may be simple page — outside cockpit shell.

---

## Internal scroll areas

| Region | Scroll owner |
|--------|--------------|
| `main_area` | Primary canvas lists, grids |
| `info_area` | Tactical preview rows |
| `favorites_used` | Long favorites list |
| Overlay panel | Project detail links |
| Tactical full view | Deadline tables |

Each region: `overflow-y: auto` + fade masks at edges.

---

## Hidden scrollbars

| Approach | Rationale |
|----------|-----------|
| Scrollbar visually minimal or hidden | Preserves cockpit aesthetic |
| **Scroll still works** | Wheel, touchpad, keyboard |

**Critical:** hiding scrollbar ≠ disabling scroll.

---

## Fade masks

| Location | Purpose |
|----------|---------|
| Top/bottom of `info_area` | Hint more content |
| `main_area` tall lists | Same |
| Optional horizontal | Wide link hubs |

Static CSS gradients — see [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md) (no mandatory animation).

---

## Scroll indicators

| Type | Role |
|------|------|
| Fade mask | Primary indicator |
| Subtle chevron | **Optional** supplement — OFF default v0.1 |
| Shadow edge | Alternative to gradient |

**Buttons do NOT replace native scrolling** — they **supplement** accessibility and discoverability.

| Supplement control | Behavior |
|--------------------|----------|
| «Scroll down» affordance | Calls `element.scrollBy()` on **target region** |
| Keyboard Page Down | Native focus on scroll container |

Never the only way to scroll.

---

## Wheel / touchpad preservation

| Rule | Detail |
|------|--------|
| Wheel over `main_area` | Scrolls `main_area` under pointer |
| Wheel over `info_area` | Scrolls rail |
| No wheel hijack to page | |
| Nested scroll | Prefer deepest focused region; avoid scroll chaining to body |

---

## Keyboard accessibility

| Key | Target |
|-----|--------|
| Tab | Focusable controls in logical order |
| Arrow keys | Optional list navigation in signals |
| Space / Enter | Activate focused row |
| Escape | Close overlay ([navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md)) |

Scroll containers need `tabindex="0"` when keyboard scroll required.

**WCAG:** hidden scrollbar must not block keyboard access to off-screen content.

---

## Why not a website?

| Website pattern | HG cockpit pattern |
|-----------------|-------------------|
| Infinite vertical marketing scroll | Fixed viewport station |
| Footer with links | `favorites_used` + modes |
| Page title + long article | Block-screens + overlays |
| Browser back as main nav | `main_menu` mode switch |

---

## Responsive notes (draft)

| Breakpoint | Scroll behavior |
|------------|-----------------|
| Wide | Tri-focus, internal scroll per column |
| Medium | Collapse rails; `main_area` primary scroll |
| Narrow | Stack zones; still no full-page scroll if possible |

**SAFE UNKNOWN:** exact breakpoints.

---

## Anti-patterns

| Anti-pattern | Why |
|--------------|-----|
| Scroll jacking entire cockpit | Disorienting |
| Only button scroll | Fails power users + a11y |
| Visible ugly scrollbar on glass | Breaks aesthetic — use thin/hidden |
| 200vh canvas on Main | Dashboard relapse |

---

## SAFE UNKNOWN

- Mobile browser address bar 100vh issues — Phase 4 implementation detail.
- Horizontal scroll on Systems grid — allowed inside `main_area` only if needed.

---

*Last updated: 2026-05-24 — Viewport and scroll philosophy.*
