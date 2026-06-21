# Campaign Fidelity QA v1

**Date:** 2026-05-29  
**Export:** `triumph-sheet1-patch-launch-ready-v1.4.xlsx`  
**Template SoT:** `triumph-manipulator-commander-template-v1.xlsx`  
**Module:** `template-campaign-metadata-v1.4.js`

---

## Automated QA result

| Check | v1.3 | v1.4 |
|-------|------|------|
| campaign_type (R7C5) | PASS | **PASS** |
| placement search (R7C8) | PASS (inherited) | **PASS** (explicit patch) |
| currency RUB (R8C8) | PASS (inherited) | **PASS** (explicit patch) |
| campaign negatives (R9C5) | PASS | **PASS** |
| optimize_text 0 (R10C5) | PASS (inherited) | **PASS** (explicit patch) |
| promotion_url (R11C5) | **FAIL** (5-tonn.html) | **PASS** (root URL) |
| Metadata diff vs template | 1 cell | **0 cells** |

**Verdict:** **PASS**

---

## Field inventory

| Logical key | Column | Meaning | Template value | v1.3 export | v1.4 export |
|-------------|--------|---------|----------------|-------------|-------------|
| `campaigns.campaign_type` | R7C5 | Тип кампании | Единая перфоманс-кампания | same | same |
| `campaigns.placement` | R7C8 | Места показа | search | same | same |
| `campaigns.currency` | R8C8 | Валюта | RUB | same | same |
| `campaigns.campaign_negatives` | R9C5 | Минус-фразы на кампанию | 9 JSON negatives | same | same |
| `campaigns.optimize_text` | R10C5 | Оптимизация текста | 0 | same | same |
| `campaigns.promotion_url` | R11C5 | Объект продвижения | https://manipulator-triumph.ru/ | 5-tonn.html | **root URL** |

---

## v1.4 exporter changes

1. `buildCampaignMetadataPatches()` delegates to `buildTemplateFidelityMetadataPatches()` — no longer derives promotion URL from first group landing.  
2. `METADATA_CELL_MAP` extended with placement, currency, optimize_text (rows 7–10).  
3. All six metadata keys patched on every v1.4 export run.

---

## Strategy & budget (SAFE UNKNOWN)

| Setting | XLSX presence | Operator action |
|---------|---------------|-----------------|
| Ручное управление ставками | Implied: col 53 «Автоставка» = `-`; bids in col 54 | Confirm in Commander after import |
| Недельный / дневной бюджет | **Not in template** | Set manually in Direct UI |
| Стратегия (smart bidding) | **Out of scope** — Search manual template v1 | N/A |

---

## Human spot-check (required)

- [ ] Commander shows «Единая перфоманс-кампания» + Search placement  
- [ ] Promotion object = `https://manipulator-triumph.ru/`  
- [ ] Campaign minus list matches row 9  
- [ ] Budget / schedule set intentionally before launch  
