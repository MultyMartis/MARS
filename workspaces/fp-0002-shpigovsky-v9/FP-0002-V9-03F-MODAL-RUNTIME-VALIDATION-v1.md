# FP-0002 V9-03F Modal Runtime Validation v1

**Tool:** `tools/v9-03f-modal-runtime-qa.py`  
**Preview:** `http://127.0.0.1:8796/`  
**Data:** `FP-0002-V9-03F-MODAL-RUNTIME-VALIDATION-DATA.json`

## Summary

Automated Playwright matrix confirms **major improvement** over V9-03E (no scroll-to-top jump). Close restoration is stable (marker delta typically ≤1px). Open deltas are typically ≤10px scrollY.

| Scenario | Scroll open Δ | Scroll close Δ | Marker close Δ | Overlay |
|----------|---------------|----------------|----------------|---------|
| Home footer | ≤18px | ≤6px | ≤1px | semitransparent ✓ |
| Home middle CTA | ≤2px | 0px | ≤6px | ✓ |
| O-Centre footer | ≤7px | ≤5px | ≤0.4px | ✓ |
| Alcohol Dependence | ≤7px | ≤5px | ≤0.4px | ✓ |
| Contacts footer | ≤7px | ≤4px | ≤0.2px | ✓ |
| Mobile ~390 footer | ≤10px | 0px | ≤4px | ✓ |

## Operator-critical checks (visual)

Automated marker deltas can fluctuate with reveal animation timing — **operator visual review is mandatory** for:

1. Home footer `Записаться` — no visible background movement
2. Home middle CTA — 3 cycles
3. O-Centre lower trigger — G6 absent
4. Alcohol Dependence lower CTA
5. Mobile ~380px footer + field focus

## Stale state

- `is-modal-scroll-locked` removed after close ✓
- No `pageShellEl.style.position` ✓

## Verdict

**AUTOMATED: PASS WITH OPERATOR VISUAL REVIEW REQUIRED**
