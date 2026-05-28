# Hero Drift Analysis v1

## Three hero generations (same route)

| Gen | File | Character |
|-----|------|-----------|
| **G0** | v4 `sections/screen-01-hero.html` | Generic index — **broken semantics** |
| **G1** | v4 `v5-ppc/zakaz/screen-01-hero.html` | PPC copy + form; qualification notice |
| **G2** | v5 `v5-ppc/zakaz/screen-01-hero.html` | `hero--v5` + lower band proof + cargo |

## G0 → G1 (ORCA alignment)

**Removed (destructive in G0):**

- `hero__rate` «от XXXX ₽/час»
- `hero__features` «Грузоподъёмность 5-10 тонн»
- `hero-proof` «Свой автопарк»

**Added (productive):**

- Locked 5 т specs list
- H1 «Аренда манипулятора в Краснодаре»
- Inline form

## G1 → G2 (Factory evolution)

| Change | Drift class | Notes |
|--------|-------------|-------|
| Wrapped proof + cargo in `hero__lower` | productive | Clear vertical rhythm |
| Cargo cards gain «Заказать перевозку >» | productive | Task CTAs |
| Removed `hero__notice` | **destructive** | See D1 |
| Proof labels simplified (no small print) | neutral | «От 30 минут» vs v4 «Подача от 30 минут по Краснодару» |
| Form endpoint attribute on v5 | neutral | Production wiring |
| Trust 4.9 ★ never implemented in G1/G2 hero | ambiguous | Blueprint never reached hero in implementation |

## ORCA blueprint hero intent vs G2

Blueprint says hero must NOT feel like «общая реклама услуги» — must show capability + fit.

| Blueprint test | G2 result |
|----------------|-----------|
| Capability visible <5 sec | **pass** — 5 bullets |
| Fit (use cases) | **pass** — cargo row |
| Uncertainty reduction | **partial** — no star rating in hero |
| Anti-junk | **partial** — no hero notice |

## Image / density drift

| Issue (G0) | G2 mitigation |
|------------|---------------|
| Image competition with headline | Bg pushed behind overlay |
| Visual clutter | Specs as compact list, not 6 feature lines |
| CTA buried below rate + features | Form column top-right |
| Semantic overload | Still high — 5+4+6 elements — mitigated by zoning |

## Calibration conclusion

Hero drift from ORCA is **net positive** for capability and CTA vs G0, with **two open gaps:**

1. Restore or relocate qualification line
2. Resolve trust strip semantics (reviews vs ops proof) per pack rule
