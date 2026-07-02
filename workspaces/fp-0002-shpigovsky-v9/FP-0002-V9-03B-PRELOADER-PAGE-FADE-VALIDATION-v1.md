# FP-0002 V9-03B — Preloader Page Fade Validation v1

## State model

| State | HTML classes | Page shell | Preloader |
|-------|--------------|------------|-----------|
| First visit loading | `is-preloader-active` | opacity 0 | opaque `#ffffff`, visible |
| Revealing | `is-page-revealing` | opacity 0→1 (~0.5s) | fading out |
| Ready | `is-page-ready` | opacity 1 | hidden, no pointer events |
| Same session | none of above on load | opacity 1 immediately | skipped |

## Test matrix

| Case | Expected | Automated |
|------|----------|-----------|
| A Fresh private session | White cover, fade to page | Structure + CSS proof |
| B Second page same session | No full preloader | sessionStorage gate in head |
| C Hard refresh same session | No full preloader | sessionStorage gate |
| D Cleared sessionStorage | Full flow returns | Manual |
| E Slow load | FAILSAFE_MS 3000 | JS present |
| F JavaScript disabled | No preloader, page visible | noscript + inline fail-safe |
| G sessionStorage unavailable | Page usable | try/catch fallbacks |
| H Reduced motion | Prompt clear, minimal fade | JS branch |
| I Nested routes | Same wrapper once | 31/31 `data-page-shell` |
| J Mobile 380px | Full viewport white | CSS `inset:0` fixed |

## Fail-safes

- Inline body-start timeout 3200ms
- JS `FAILSAFE_MS` 3000
- `revealPageImmediately()` when session already shown

## Operator re-check

Fresh private window required for case A.
