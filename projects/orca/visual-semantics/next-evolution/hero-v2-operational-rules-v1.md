# Hero v2 Operational Rules v1

**Source:** `calibration/.../next-evolution/hero-v2-requirements.md`  
**Status:** requirements only — not a build charter

## Retain from G2

- `first-screen` bg + overlay
- `hero__main` grid + `hero__aside` form
- 5 locked specs
- no fleet / no fake rate

## Required changes

| ID | Change | Priority | Visual semantics |
|----|--------|----------|------------------|
| H2-1 | Restore qualification line in `hero__lower` above cargo | P0 | `qualification_mode: hero_lower_band` |
| H2-2 | Pack-driven H1 per `primary_ad_variant` | P0 | fixes D2 |
| H2-3 | `trust_mode: hybrid_proof` — compact 4.9 + max 2 ops | P1 | |
| H2-4 | Cap cargo: 4 mobile / 6 desktop or 4 all | P1 | `cargo_cards_max_*` |
| H2-5 | `mobile_hero_cta_order: [call, form]` when call-first | P0 | `mobile_critical` |
| H2-6 | Single red primary — cargo ghost/outline | P2 | `cta_weight` |

## Acceptance

- [ ] A1 + A2 H1 strategy documented
- [ ] Qualification visible on 390px or sticky
- [ ] No placeholder form handler in production
- [ ] Pack fields match HTML
- [ ] `destructive` empty

## Do not

- Reintroduce v4 index hero
- Add hero hourly price
- Add second H1
