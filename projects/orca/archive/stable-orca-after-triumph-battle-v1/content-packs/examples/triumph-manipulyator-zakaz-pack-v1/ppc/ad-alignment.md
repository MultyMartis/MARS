# PPC — Ad alignment

## Ads → landing matrix

| ad_id | headline_1 | headline_2 | description (core) | Landing match |
|-------|------------|------------|-------------------|---------------|
| `ad_fc12_a1` | Заказать манипулятор в Краснодаре | Подача на объект | Заказать… Борт 5 т, стрела 3 т. Звонок и расчёт | **partial** — specs yes, H1 verb no |
| `ad_fc12_a2` | Аренда манипулятора Краснодар | Цена по задаче | Аренда… Вызов и расчёт. Борт 5 т, стрела 3 т | **strong** |

## Description alignment

| Ad text | Landing echo |
|---------|--------------|
| Борт 5 т, стрела 3 т | Hero bullets + specs dl — **yes** |
| Расчёт / цена | Form + pricing section — **yes** |
| Вызов | Not in H1; «От 30 мин» proof — **partial** |
| Звонок и расчёт (callout) | Form + tel — **yes** |

## Title / meta (as-built)

- `<title>`: Аренда манипулятора в Краснодаре — aligns **A2**
- `meta description` leads with «Заказать» — **partial bridge to A1**

## Yandex bold (instance)

A1 plans bold on «заказать манипулятор» — landing H1 does not reinforce — **quality score risk hypothesis** (not measured).

## Pack recommendation

```yaml
primary_ad_variant: ad_fc12_a2
secondary_ad_variant: ad_fc12_a1
launch_strategy: A2 primary until H1 revision OR pause A1
```

## Strategies (ORCA — not implementation)

| ID | Description |
|----|-------------|
| A | Launch A2 first; pause A1 |
| B | Dynamic keyword in ads only — not page H1 |
| C | Composite H1 — operator copy review |
| D | Split URL — likely overkill |

**Calibration preference:** A or operator-approved C.
