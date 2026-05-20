# V2 — Responsive QA gate

**Purpose:** Layout behavior vs breakpoints and **no accidental breakage** when stacking.

## Preconditions

- Semantic QA completed or in-flight issues documented.
- Reference [responsive-rules.md](../implementation-pack/responsive-rules.md) + [spacing-system.md](../implementation-pack/spacing-system.md).

---

## Width matrix (spot-check)

Test at least: **1440**, **1200**, **1024**, **768**, **375**, **360** (or project standard device list).

| # | Check | Fail if |
|---|--------|---------|
| R1 | **No horizontal scroll** on body for standard widths | Persistent `overflow-x` on main document |
| R2 | **Container padding** follows ladder (72 / 32 / 16) unless mock-specific exception documented | Random per-section horizontal gutters |
| R3 | **Section `padding-block`** matches scale (96 / 72 / 56) or documented mock deviation | One-off 40px hacks breaking rhythm |
| R4 | **Hero CTAs + form** usable on mobile | CTA or submit clipped, overlapped unreadably, or tap target < design system minimum |
| R5 | **`03` cases** stack in **1→2→3** reading order | Order reverses without mock reason |
| R6 | **`04` cards** keep **01–08** order in stack | Cards reshuffled for “balance” |
| R7 | **`05` matrix** columns stack cleanly | Orphan icons, broken row pairing |
| R8 | **Footer** legal row readable, wraps | `overflow:hidden` clips legally significant lines |
| R9 | **Typography steps** use **px** only at breakpoints | `rem`/`clamp` on font-size |
| R10 | Images / media **scale** without distortion | Aspect broken, squashed logos |

---

## Outcome

- **PASS:** All dimensions behave; file exceptions in `drift-observations.md` if mock required tradeoff.  
- **FAIL:** Block freeze; fix layout before declaring section done.
