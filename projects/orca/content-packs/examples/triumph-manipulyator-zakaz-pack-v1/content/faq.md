# Section — FAQ

**section_id:** `faq`  
**partial:** `v5-ppc/zakaz/screen-04-faq.html`  
**anchor:** `#faq`  
**priority:** P2

## Purpose

Uncertainty reduction + **keyword reinforcement** («заказать», «цена», «край», безнал).

## Questions (as-built)

1. Как заказать манипулятор?
2. Какие параметры техники? — **5 т / 3 т / 14 м / кузов / 2 ч** 🔒
3. Как рассчитывается стоимость? — по задаче, до выезда
4. Работаете ли по краю? — Краснодар + край
5. Можно ли оплатить по безналу?
6. Что не перевозите? — echoes denied tasks

## Layout

- Split: FAQ list + embedded `contact-cta` (second `#contacts` anchor — verify HTML id uniqueness in QA)

## PPC continuity

| Keyword | FAQ support |
|---------|-------------|
| заказать | Q1 — **strong** |
| цена | Q3 — **strong** |
| край | Q4 — **strong** |
| кран-манипулятор | **weak** — no synonym in FAQ (optional vNext line) |

## Semantic locks

- Spec numbers in Q2 must match hero — **blocker** if drift

## Factory notes

- Route-specific partial (good) — unlike trust/B2B shared blocks
