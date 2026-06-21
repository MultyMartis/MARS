# Landing State Summary v1 — Master Hot (zakaz)

**As-built source (canonical):** `workspaces/triumph-manipulator-landing-v6/`  
**Page:** `src/pages/index.html` → `dist/index.html` (zakaz master hot)  
**Date:** 2026-06-03 (Wave 1A alignment — calibration index retargeted from v5)

## Identity

| Field | Value |
|-------|--------|
| Human name | Аренда манипулятора в Краснодаре |
| `data-page-type` | `ppc-zakaz-manip` |
| Canonical URL | `https://manipulator-triumph.ru/` |
| PPC group | `grp_fc12_zakaz` |
| Blueprint | `01-master-hot-general` |
| Robots | `noindex,nofollow` (PPC default) |

## Section order (as-built)

1. **First screen** — bg image + overlay + header + hero (`v5-ppc/zakaz/screen-01-hero.html`)
2. **Specs** — `screen-02-specs.html` (`#specs`, machine showcase)
3. **Tasks** — `screen-02-tasks.html` (allowed / denied)
4. **Order steps** — `screen-02b-order-steps.html`
5. **Pricing factors** — `screen-02c-pricing-factors.html`
6. **Trust + reviews** — `v5-page01/screen-03-trust-reviews.html` (shared partial)
7. **B2B** — `v5-page01/screen-03b-b2b.html`
8. **Dark proof strip** — `v5-page01/dark-proof-strip.html`
9. **FAQ** — `v5-ppc/zakaz/screen-04-faq.html`
10. **Footer** — `v5-page01/landing-footer.html` (includes final contact / `#contacts`)

Matches hardening audit section order (`v5-production-hardening-audit-v1.md`).

## Hero structure (v5)

| Zone | Content |
|------|---------|
| Left column | H1, lead, 5 spec bullets |
| Right column | Inline form «Рассчитать стоимость» + call button |
| Lower band | `hero-proof--v5` (4 operational items) |
| Cargo row | 6 interactive cargo cards with micro-CTA «Заказать перевозку >» |

**Not in v5 zakaz hero (vs v4 zakaz partial):** `hero__notice` qualification paragraph.

## Positioning (as-built copy)

- **One machine** framing: 5 т / 3 т / 14 м / кузов / 2 ч мин. заказ
- **No** fleet «5–10 т» in hero (legacy v4 index removed)
- **No** fake «от XXXX ₽/час» in hero
- Lead mentions «манипулятором 5 т» — capability anchor on general page

## CTA map

| Location | Primary | Secondary |
|----------|---------|-----------|
| Hero form | Submit «Рассчитать стоимость» | `tel:+79004658331` |
| Specs block | «Рассчитать стоимость» → modal/callback | — |
| Cargo cards | Modal callback | — |
| Header | (v5-page01 header partial) | phone + CTA |

**Form handler:** v5 production audit flags `data-form-endpoint` on zakaz hero but also historical `mock` on some partials — **SAFE UNKNOWN** for live POST until operator confirms.

## Semantic lock status

| Source | Status |
|--------|--------|
| Dedicated zakaz handoff | **missing** |
| Blueprint `01-master-hot-general` | exists — doctrine-level |
| Content pack for master hot | **missing** (only 5-ton example pack) |
| MODE 1 lock | **partial** — locks inferred from blueprint + 5-ton cousin, not signed zakaz handoff |

## UNKNOWNs

- Production URL 200 / live parity with `dist/`
- Mobile CTA without-scroll (QA item 8 on 5-ton QA contract — applies by analogy)
- Which ad variant (Заказать vs Аренда) is primary at launch
- NAP / hours final lock
