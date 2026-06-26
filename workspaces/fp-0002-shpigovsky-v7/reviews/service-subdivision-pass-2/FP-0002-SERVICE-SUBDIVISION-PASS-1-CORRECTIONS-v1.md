# FP-0002 Service Subdivision Pass 1 Corrections v1

## Intro card markup

| Item | Before | After |
|------|--------|-------|
| Source | `service-subdivision-intro-v1.html` | same |
| Invalid pattern | `<span class="home-recovery-intro__card-icon">…<h3>…</h3></span>` | `<div class="home-recovery-intro__card-head"><span …icon…></span><h3>…</h3></div>` |
| `h3` inside `span` | 3 | 0 |
| Home output | unchanged | unchanged |

**Verdict:** `INTRO_MARKUP_VALID`
