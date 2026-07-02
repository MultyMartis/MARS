# FP-0002 V8 — Next Wave Recommendation v1

**Date:** 2026-06-28
**Status:** NEXT IMPLEMENTATION — **NOT AUTHORIZED**

## Recommended order

1. **CF-011** — dark CTA wrapper consolidation (**P1**)
2. **CF-012** — program modifier consolidation (**P1**)
3. **CF-010** — clinic landscape neutralization (**P2**)
4. Final consolidation readiness review
5. O-Centre reimplementation on neutral shared components

## Notes

- CF-011 charter should include remediation of pre-existing broken `aria-labelledby` on `service-subdivision-first-cta-v1.html` (`service-subdivision-start-heading` missing).
- CF-010 and CF-012 must remain separate prompts (different CSS/HTML families, different risk).
- Do not start O-Centre until shared-component consolidation waves are operator-chartered and complete.

## Current gate

- CF-003–CF-009 shared families: **COMPLETE**
- Duplicate-ID repair on Home: **COMPLETE**
- Page-wide DOM gate: **BLOCKED** (pre-existing subdivision ARIA — document only)
