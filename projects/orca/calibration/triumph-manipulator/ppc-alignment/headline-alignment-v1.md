# Headline Alignment v1

## Ads → H1 matrix

| ad_id | headline_1 | headline_2 | Landing H1 match? |
|-------|------------|------------|-------------------|
| ad_fc12_a1 | Заказать манипулятор в Краснодаре | Подача на объект | **partial** — geo OK, verb mismatch |
| ad_fc12_a2 | Аренда манипулятора Краснодар | Цена по задаче | **strong** — аренда + geo |

## Description alignment

| Ad text | Landing echo |
|---------|--------------|
| Борт 5 т, стрела 3 т | Hero bullets — **yes** |
| Расчёт / цена | Form «Рассчитать стоимость» — **yes** |
| Вызов | Not in H1; ops proof «От 30 мин» — **partial** |

## Title tag

`index.html` title: «Аренда манипулятора в Краснодаре | Триумф» — aligns with **A2**, not **A1**.

## Recommendations (ORCA — not implementation)

| Strategy | Description |
|----------|-------------|
| **A — A2 primary** | Launch A2 first; pause A1 until H1 adds «Заказать» variant LP |
| **B — Dual H1** | Not possible — one H1; use dynamic keyword insertion only in ads, not page |
| **C — Composite H1** | «Заказать и аренда манипулятора…» — operator copy review |
| **D — Split URL** | Separate LP per ad — heavy; likely overkill |

**Calibration preference:** document in pack `primary_ad_variant: ad_fc12_a2` OR fix H1 for A1.

## Yandex bold

Instance plans bold on «заказать манипулятор» for A1 — landing does not reinforce — **quality score risk hypothesis** (not measured).
