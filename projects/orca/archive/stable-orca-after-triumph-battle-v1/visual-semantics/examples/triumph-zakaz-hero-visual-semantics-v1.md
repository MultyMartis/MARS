# Triumph Zakaz Hero — Visual Semantics v1 (canonical example)

**Route:** master hot · `grp_fc12_zakaz` · `/`  
**As-built partial:** `workspaces/triumph-manipulator-landing-v5/src/partials/sections/v5-ppc/zakaz/screen-01-hero.html`  
**Blueprint:** `projects/orca/ppc/triumph-manipulator/landing-pages/01-master-hot-general.md`  
**Status:** first canonical ORCA visual semantics example — describes **as-built G2** + calibration judgment

---

## Visual semantics bundle (as-built)

```yaml
visual_semantics:
  version: v0
  route_id: master_hot
  group_id: grp_fc12_zakaz
  canonical_url: https://manipulator-triumph.ru/
  fields:
    hero_priority: capability_first
    proof_priority: hero_strip
    cta_priority: form
    visual_density: high
    compactness_level: compact
    mobile_critical: [form_submit, capability_scan]
    trust_mode: operational_proof
    qualification_mode: tasks_section_only
    hero_layout_mode: grid_form_aside
    proof_visibility: prominent
    cta_weight: primary_dominant
    semantic_focus: [one_machine, use_case_fit]
    conversion_intent_weight: hot
    visual_noise_risk: high
    frontend_priority:
      - hero_main
      - hero_aside
      - hero_lower
      - specs
      - tasks
      - pricing_factors
      - trust_reviews
  drift_acceptance:
    productive:
      - inline_hero_form
      - compact_spec_list
      - v5_bg_overlay
      - cargo_cards_v5
      - hero_lower_zoning
      - fleet_fake_price_removed
      - operational_hero_proof
    destructive:
      - D1_qualification_hero_removed
      - D2_multi_ad_h1_unresolved
    ambiguous:
      - trust_social_deferred_to_section
      - call_first_vs_form_hero
```

---

## Hero structure

```text
.first-screen (hero-bg-final.jpg + overlay)
  └── .hero.hero--v5
        ├── .hero__main [1.06fr | 420px]
        │     ├── .hero__content
        │     │     H1: Аренда манипулятора в Краснодаре
        │     │     Lead: 5 т, край, без посредников
        │     │     Specs ×5 (борт, стрела, вылет, кузов, мин. заказ)
        │     └── .hero__aside
        │           Form H2: Рассчитать стоимость
        └── .hero__lower
              ├── .hero-proof--v5 (4 items)
              └── .hero__cargo-block (6 cards)
```

---

## Visual zones

| Zone | Role | Priority |
|------|------|----------|
| `hero__content` | Capability scan | P0 |
| `hero__aside` | Conversion (form) | P0 |
| `hero-proof--v5` | Ops trust | P1 in hero |
| `hero__cargo` | Task qualification | P1 in hero |

---

## CTA hierarchy

| CTA | Weight | Notes |
|-----|--------|-------|
| Form submit «Рассчитать…» | primary | red, aside column |
| Header tel | secondary | sticky — verify mobile |
| Cargo ×6 «Заказать перевозку» | secondary (noise risk) | outline/ghost recommended (H2-6) |
| Messengers | tertiary | footer/modal |

**Gap:** PPC instance call-first vs `cta_priority: form` — document under `ambiguous`.

---

## Proof mode

| Layer | Mode |
|-------|------|
| Hero strip | `operational_proof` — От 30 мин · Мин. заказ · Водители · Безнал |
| § Trust | `social_proof` — Яндекс + Авито (below fold) |

**Why ops above fold worked:** aligns with hot intent, callouts, dispatch speed; avoids v4 fleet signal.  
**Cost:** star rating not in first 5–10 sec — friction for social comparers.

---

## Semantic priorities

1. One machine — 5 т specs (not fleet)
2. Geo — Краснодар + край
3. Use-case fit — 6 cargo types
4. Price honesty — no fake hero rate; calc via form
5. Anti-junk — **weak in hero** (D1) — tasks section only

---

## Density level

`visual_density: high` — ~20+ distinct messages before scroll.  
Zoning makes this **productive** vs G0 **destructive** overload.

Redundancy: «мин. заказ 2 ч» in specs and proof.

---

## Mobile risks

| Risk | Severity |
|------|----------|
| Form after 5 specs on stack | high |
| call-first not mirrored in hero | medium |
| 6 cargo taps | medium |
| overflow | UNKNOWN |

Recommended pack vNext: `mobile_critical: [call, form_submit, qualification_line]`, `cargo_cards_max_mobile: 4`.

---

## Productive drift (keep)

- Inline form, compact specs, bg overlay, lower band, cargo cards, ops proof, fleet/price removal

---

## Destructive drift (fix before full approval)

- **D1:** qualification line absent in hero
- **D2:** A1 ad «Заказать» ≠ H1 «Аренда»

---

## Visual lock recommendations

| Lock | Recommendation |
|------|----------------|
| Qualification | Restore `hero__notice` in lower band above cargo |
| Trust | Move to `hybrid_proof` or document ops-only acceptance |
| H1 | Pack `primary_ad_variant` per ad set |
| Cargo | Cap 4 mobile; ghost style for micro-CTAs |
| Mobile | `mobile_hero_cta_order: [call, form]` |

---

## Factory hints

```yaml
factory_hints:
  data_page_type: ppc-zakaz-manip
  partial_paths:
    hero: v5-ppc/zakaz/screen-01-hero.html
    hero_scss: scss/sections/_v5-hero-extensions.scss
  build: gulp — see workspace README
```

---

## SAFE UNKNOWN

- Device QA results
- SLA truth for «30 минут»
- Conversion split call vs form
- Scroll depth to trust section
