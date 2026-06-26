# FP-0002 Services V2 — Detail Link Home Pattern Reuse v1

## Home reference

| Item | Value |
|------|-------|
| Text selector | `.home-rehabilitation-program__all-text` |
| Link selector | `.home-rehabilitation-program__all-link` |
| Icon selector | `.home-rehabilitation-program__all-icon` |
| Icon | `<i class="fas fa-play"></i>` |
| Typography | 15px / `--line-height-nav` / `--font-weight-button` / uppercase |
| Color | `--color-text-primary` → `--color-accent` on hover/focus |
| Gap | `--pad-gap-line` |

## Services implementation

| Item | Value |
|------|-------|
| Anchor | `.services-category-section-v2__service-link.home-rehabilitation-program__all-link` |
| Label | `узнать больше` (mockup runtime label preserved) |
| Icon | Same Home `fa-play` pattern |
| Custom V2 link SCSS | Removed |
| New tokens | 0 |

## Probe (post-build)

| Metric | Value |
|--------|------:|
| Detail links | 14 |
| Home-pattern dual-class links | 14 |
| `fa-play` icons | 14 |
| `external-link.svg` in service links | 0 |

## Verdict

`HOME_REHABILITATION_PATTERN_REUSED`
