# PPC Continuity Analysis v1 — drift lens

**Instance:** `triumph-s-tier-draft-v1.json` → `grp_fc12_zakaz`  
**Landing:** v5 zakaz hero + first screen

## Continuity matrix

| Dimension | Ad / ORCA | Landing | Survived? |
|-----------|-----------|---------|-----------|
| **Geo** | Краснодар (ads, keywords) | H1 span «в Краснодаре» + lead «по Краснодару и краю» | **yes** |
| **Capability** | Борт 5 т, стрела 3 т (desc, callouts) | Hero 5 bullets + specs block | **yes** |
| **Intent (аренда)** | ad_fc12_a2 H1 «Аренда манипулятора Краснодар» | H1 «Аренда манипулятора в Краснодаре» | **yes** |
| **Intent (заказать)** | ad_fc12_a1 H1 «Заказать манипулятор в Краснодаре» | H1 uses «Аренда» not «Заказать» | **no** (variant) |
| **Pricing frame** | «Цена по задаче», «Расчёт» | «Рассчитать стоимость», pricing factors section | **yes** |
| **Commercial CTA** | «Звонок и расчёт» callouts | Form + tel | **yes** |
| **Display path** | `zakaz-manip` | URL `/` — path not visible on page | neutral |
| **Trust** | Not in ad text | Reviews in §3 — not hero | **delayed** |
| **Qualification** | Negatives in campaign (купить, вакансии…) | Denied tasks section | **partial** (below fold) |

## Headline continuity detail

### Variant A2 (аренда) — **strong**

- Ad: `Аренда манипулятора Краснодар`
- H1: `Аренда манипулятора в Краснодаре`
- Yandex bold on «аренда манипулятора» — supported

### Variant A1 (заказать) — **weak**

- Ad: `Заказать манипулятор в Краснодаре`
- H1: no «заказать» token
- Mitigation options: dynamic headline test (out of scope), second LP, or H1 «Заказать и аренда…» (operator copy decision)

## Fastlinks continuity

Instance defines 8 fastlinks to capability/use-case URLs — **landing does not mirror** fastlink row in hero (expected — fastlinks are ad extensions, not page UI).

**Risk:** user expects fastlink-specific section on `/` — **low** if LP qualifies general intent first.

## Callouts vs hero proof

| Callout (ad) | Hero proof strip |
|--------------|------------------|
| Звонок и расчёт | Form + call — **aligned** |
| Борт 5 т | Spec bullet — **aligned** |

## Blocker check (5-ton rule analogy)

5-ton handoff: «Несовпадение с объявлением = блокер».

For master hot: **spec numbers pass**; **H1 token pass for аренда variant only**.

**Launch recommendation (calibration, not ads approval):**

- Do not treat group 12 as fully continuity-verified until H1 strategy covers **both** primary ads OR ads split by URL.

## Productive PPC-adjacent changes

- Description keywords «вызов», «расчёт» reflected in form microcopy
- «Без посредников» in lead — matches brand line in doctrine
