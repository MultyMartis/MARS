# SERP capture notes — Multi-Query Groundtruth

**Date:** 2026-06-04  
**Pilot:** MIG Multi-Query Groundtruth (Триумф / Грузотакси / Краснодар)

## Environment

| Field | Value |
|-------|-------|
| Search engine | Yandex touch — `https://yandex.ru/search/touch/` |
| Region | Краснодар (`lr=35`) |
| Device | Playwright iPhone 13 emulation |
| Search string geo | Lowercase `краснодар` in URL (declared set uses «Краснодар») |
| Logged-in | No |

## Capture outcome

| Query ID | Status | Notes |
|----------|--------|-------|
| q01–q04 | captured | Browser OK after retries |
| q05–q07 | **failed** | Yandex SmartCaptcha — evidence in `captures/q05–q07/` |
| q08 | captured | |
| q09 | captured | Retry pass |
| q10 | captured | |
| q11 | captured | Retry pass |

**Executed:** 8 / 11 declared queries (`query_coverage: partial`).

## Evidence layout

```text
captures/<query_id>/
  capture-raw.json
  serp-full-viewport.png
  serp-full-page.png
  serp-page.html
serp_results/<query_id>.json   # normalized
serp_index.json                # in session folder after assembly
```

## Anomalies

- Batch capture triggers captcha after first query unless spaced (60–90s) and retried.
- Some queries (`газель` head terms) captcha-prone on this IP.
- yabs promo hrefs; domains inferred from Path line where needed.
