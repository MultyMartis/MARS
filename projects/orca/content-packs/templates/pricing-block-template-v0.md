# Pricing Block Template v0

**Section ID:** `pricing` (06)  
**Use inside:** [landing-content-pack-template-v0.md](landing-content-pack-template-v0.md)

## Section contract

| Field | Guidance |
|-------|----------|
| section_purpose | Close «цена» intent without fake tariff table |
| ppc_continuity | Supports «…цена» queries with honest framing |
| semantic_locks | No invented hourly rate; min order preserved |

## Copy structure

| Block | Content |
|-------|---------|
| H2 | e.g. «Стоимость манипулятора …» |
| Lead | Exact price by task; no hidden fees after dispatch |
| Factors list | 4–6 bullets |
| Anchor line | Anti-dumping / anti–«lowest on internet» |

## Factors (bullets)

1. 
2. 
3. 
4. 
5. 
6. 

## CTA

| Role | Text |
|------|------|
| Primary | Рассчитать стоимость |
| Secondary | Уточнить подачу |

## SAFE UNKNOWN

| Field | Rule |
|-------|------|
| `hourly_rate_rub` | Do not publish until operator confirms |
| Promotional discounts | Not in pack without evidence |

## Semantic locks

- «Стоимость до выезда» principle
- Minimum order hours in factors if applicable

## Factory notes

- No `hero__rate` placeholder / no fake «от XXXX ₽/час»
- Light section acceptable; `#pricing` anchor
