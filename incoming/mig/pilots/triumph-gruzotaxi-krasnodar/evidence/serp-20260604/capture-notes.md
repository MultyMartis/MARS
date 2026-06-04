# SERP capture notes — Pilot #1

**Date:** 2026-06-04  
**Query:** `грузотакси краснодар`  
**Captured at (UTC):** 2026-06-04T04:06:19.766Z (~07:06 MSK)

## Environment

| Field | Value |
|-------|-------|
| Search engine | Yandex — https://yandex.ru/search/touch/ |
| Region | Краснодар (`lr=35`, city/krai code on Yandex) |
| Device | Mobile — Playwright iPhone 13 emulation (390×844) |
| Browser | Chromium 131 via Playwright 1.60 |
| Language | ru-RU |
| Logged-in state | Not signed in (clean automated session) |
| Personalization | Unknown — automated headless session; no Yandex account |

## Capture method

Real Yandex mobile SERP loaded via Playwright; screenshots and HTML saved. No LLM-generated SERP data. Ad click targets on SERP use `yabs.yandex.ru` redirect URLs; display domains recorded from visible Path lines where shown.

## Evidence files

| File | Description |
|------|-------------|
| `serp-full-page.png` | Full scroll mobile SERP |
| `serp-full-viewport.png` | Initial viewport (top ads) |
| `serp-top-ads.png` | Top viewport — promo blocks |
| `serp-organic-block.png` | Scrolled — Avito / aggregators / organic |
| `serp-maps-organic.png` | Scrolled — maps link / Profi / lower organic |
| `serp-page.html` | Raw HTML at capture time |
| `capture-raw.json` | Machine extraction log |

## Anomalies

- No inline map carousel (local pack cards) observed on this SERP; Яндекс Карты appears as an organic link.
- Several promo blocks share `yabs.yandex.ru` hrefs; destination domains taken from visible Path text.
- Ad domain `krasnodar.gruzovichec.ru` (promo) differs from organic `krasnodar.gruzovichkof.ru`.
- Bottom promo «Разгрузка в Краснодаре. 850 ₽» — destination domain not visible in Path line; yabs href only.
