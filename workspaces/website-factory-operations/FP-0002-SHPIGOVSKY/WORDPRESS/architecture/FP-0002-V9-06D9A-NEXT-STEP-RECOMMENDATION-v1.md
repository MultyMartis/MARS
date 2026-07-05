# FP-0002 V9-06D9A Next Step Recommendation v1

**Date:** 2026-07-05  
**Task:** V9-06D9-A Visual Parity Audit  
**Verdict:** FAIL — repair required

## Decision

Operator visual review confirmed significant parity gaps between static V9 and WordPress runtime. D9-A audit is **COMPLETE**. No repairs were performed.

## Recommended next action (exactly one)

**CREATE_V9_06D9C_HOME_HERO_PARITY_REPAIR_TASK**

### Rationale

- Primary operator concern: Home hero appears empty/light vs static photo hero.
- Root cause confirmed: `hero__media` absent because `home_hero_slides` image not seeded and `hero-main.png` not in runtime.
- Highest visual impact per screenshot evidence (static top ~568 KB vs runtime top ~27 KB).
- Bounded scope: single ACF field + one media asset + optional static fallback.

## Follow-on sequence (after D9-C)

1. **D9-B** — Inter font path repair (5 font 404s)
2. **D9-D** — missing Home section port (12 sections)
3. **D9-E** — density/vendor polish
4. **D9-F** — secondary page parity

## Do not precede with

- D8-F admin UX repair (optional, lower priority)
- Production deployment
- Unbounded template expansion without wave gates

## Evidence

- `validation/v9-06d9a-visual-parity-audit/final-verdict.json`
- `reports/FP-0002-V9-06D9A-VISUAL-PARITY-AUDIT-REPORT-v1.md`
