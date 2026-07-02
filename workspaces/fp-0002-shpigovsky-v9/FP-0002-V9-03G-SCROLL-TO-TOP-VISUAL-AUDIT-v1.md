# FP-0002 V9-03G Scroll-to-Top Visual Audit v1

**Phase:** V9-03G — pending operator visual approval

## Control specification

| Property | Desktop | Mobile (≤1024px) |
|----------|---------|------------------|
| Shape | Circle (`border-radius: var(--radius-full)`) | Same |
| Size | 48×48px | 44×44px |
| Position | fixed bottom-right | fixed bottom-right |
| Right offset | 15px (`--pad-gap-line`) | 10px (`--pad-gap-tight`) |
| Bottom offset | 15px + safe-area | 10px + safe-area |
| Background | `var(--color-surface)` | Same |
| Border | 1px `var(--color-border-subtle)` | Same |
| Icon | Inline SVG arrow up, 20px | 18px |
| Text label | none (icon only) | none |
| z-index | 900 | 900 |

## Interaction states

| State | Behavior |
|-------|----------|
| Default (hidden) | opacity 0, visibility hidden, pointer-events none |
| Visible | opacity 1, `.scroll-to-top--visible` |
| Hover / focus-visible | background + border → `--color-text-primary`; icon → inverse |
| Focus ring | 2px `--color-accent` outline, 2px offset |
| Active | opacity 0.92 |
| Hover lift | **none** (no translateY/scale) |

## Show/hide animation

- Opacity + visibility transition using `--motion-base` (0.3s)
- No vertical lift, bounce, or attention-seeking motion

## Design alignment

- Uses existing Shpigovsky palette and radius tokens
- Calm restrained floating control — not Triumph styling
- No external icon dependency

## Operator screenshot targets

1. Home at ~700–1000px scroll (desktop)
2. Long service page near footer (desktop)
3. Hover and focus-visible states
4. Mobile ~380px — corner position vs footer
5. Modal open — control remains behind overlay

**Preview:** http://127.0.0.1:8797/
