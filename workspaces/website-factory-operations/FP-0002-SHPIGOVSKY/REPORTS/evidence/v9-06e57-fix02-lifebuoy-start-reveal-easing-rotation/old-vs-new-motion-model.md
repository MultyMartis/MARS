# Old vs new motion model — V9-06E57-FIX02

## Root cause of FIX01 initial sluggishness

| Layer | FIX01 | Why it felt delayed |
|-------|-------|---------------------|
| X/Y/rotate easing | `easeInOutCubic` first half `4t³` | `de/dt(0) = 0` → dead zone at scroll start |
| Scale easing | Hermite `smoothstep` per half | `de/dt(0) = 0` → scale also waits |
| CSS / rAF / thresholds | passive scroll + rAF; no CSS transition on transform | **not** the lag source |

## Replacement model (FIX02)

| Layer | FIX02 | Initial response |
|-------|-------|------------------|
| X/Y/rotate | `easeOutCubic` = `1-(1-t)³` | `de/dt(0) = 3` — immediate |
| Scale | piecewise **linear** on raw `t` | constant non-zero slope from first pixels |
| Endpoints | scale `1.00 → 1.20 → 0.72` unchanged | preserved |

## Position / reveal envelope

| Param | FIX01 | FIX02 |
|-------|-------|-------|
| Long X start | −70% (~30% visible) | **−50% (~50% visible)** |
| Long X end | −30% (~70% visible) | **−20% (~80% visible)** |
| Short X start | −70% | **−50%** (coherent global start) |
| Short X end | −42% | **−38%** (milder; measured ~59% max) |
| Y arc | −12vh → 52vh / 28vh short | unchanged |
| Long rotate | −6° → +18° | **−7.2° → +21.6°** (×1.20) |
| Short rotate | −3° → +10° | **−3.6° → +12°** (×1.20) |

## Measured Home 1440×900

| progress | visible% | scale | rotate |
|----------|----------|-------|--------|
| 0% | **50.0** | 1.0000 | −7.200° |
| 2% | 52.9 | 1.0080 | −5.508° |
| 10% | 63.5 | 1.0400 | +0.606° |
| 50% | 69.3 | 1.2000 | +18.000° |
| ~98% | **81.1** | 0.7392 | +21.600° |

## Reduced motion

Freeze at effective `t = 0.28` **unchanged**. CSS `will-change: auto` under `prefers-reduced-motion` **unchanged**.
