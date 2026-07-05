# FP-0002 V9-06D9Q Reviews Architecture Options Analysis v1

**Date:** 2026-07-06

Evidence: `validation/v9-06d9q-reviews-include-planning/reviews-architecture-options-analysis.json`

---

## Options comparison

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| **A** Static partial only | Simplest; matches today | No admin; not shared; poor long-term | Reject for implementation |
| **B** Home ACF repeater | Partially exists | Wrong ownership; Home UX clutter; operator rejected | **Reject** |
| **C** ACF Options shared | Central; matches site options pattern; shared include | No per-review URLs | **Recommended primary** |
| **D** Reviews CPT | Scalable archive | Overhead; overkill now | Defer future wave |
| **E** Hybrid | Options now + static fallback + future CPT slot | Slightly more helper code | **Recommended shape** |

---

## Recommendation

**Option E (Hybrid)** with **Option C (ACF Options)** as the immediate source-of-truth.

### Why not B (home_reviews_teaser)?

- Duplicates data if `/otzyvy/` also shows reviews.
- Pollutes Home #4 admin after D9-L…O UX repairs.
- Operator explicitly deferred reviews include away from Home ACF.

### Why not D (CPT) now?

- FP-0002 stage needs bounded MVP, not new post type lifecycle.
- Existing `group_fp02_page_reviews` already documents page-level repeater bounds — can merge into options or remain dormant.
- CPT remains valid escalation if operator later needs dozens of individually managed reviews with URLs.

### Why E over pure C?

- Preserves current static V9 frontend when options empty (demo-safe).
- Documents precedence: enabled → options → static → (future CPT).
- Allows `reviews_enabled` master hide without blank broken section.

---

## Safest for current FP-0002 stage

**Hybrid Options + shared include + static fallback** — implements shared reviews without Home admin coupling, without CPT cost, with production migration path via ACF JSON + options seed.
