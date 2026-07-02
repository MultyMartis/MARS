# FP-0002 V9-03C — O-Centre Mobile Validation v1

**Route:** `/o-centre/`  
**Primary viewport:** ~380px  
**Secondary:** ~768px (tablet breakpoint where G6 previously appeared)

## Primary target (380px)

| Check | Expected | Automated |
|-------|----------|-----------|
| G6 block absent | Yes | PASS (dist HTML 0 G6 tokens) |
| No orphan close control | Yes | Structural — G6 was only `mobile-close` |
| No infrastructure-19/20 images | Yes | PASS |
| HTTP 200 | Yes | PASS |

## What changed on mobile

Previously at `max-width: 1024px`, G6 became `display: flex` with two stacked mobile-only images. That entire block is removed — G5 comfort gallery is now the final infrastructure group before the next section.

## Operator narrow review (required)

At **380px** scroll the infrastructure narrative:

1. Confirm former G6 images/control **completely gone**
2. Confirm **no empty vertical gap** between G5 and next section
3. Confirm scroll flow feels continuous

At **~768px** repeat quick check (old mobile-close activation zone).
