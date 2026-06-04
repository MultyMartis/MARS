# MIG Landing Trust Signals Model v2

**Status:** design only — **no runtime**.  
**Parent:** [mig-landing-analysis-v2.md](mig-landing-analysis-v2.md) · families `TRUST` + `SOCIAL_PROOF`.

---

## 1. Purpose

Pilot #1 stored credible lines but collapsed operator value to `trust_count` and mis-typed long copy as `statistics`. v2 separates **subtype**, **numeric extraction**, and **social proof platform**.

---

## 2. Trust observation object

```json
{
  "observation_id": "mig-20260604-61b585-la001-obs-tr02",
  "family": "TRUST",
  "sub_type": "rating_display",
  "text": "Рейтинг в Яндексе 5 129+ оценок",
  "platform": "yandex",
  "numeric_value": 5,
  "numeric_secondary": 129,
  "numeric_unit": "ratings_count",
  "confidence": "B",
  "evidence": {
    "source": "page_html",
    "snapshot_id": "mig-20260604-61b585-ws001",
    "verbatim_text": "Рейтинг в Яндексе 5 129+ оценок Рейтинг в Авито 4,8 222+ отзывов …"
  }
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `sub_type` | Yes | §3 enum |
| `platform` | No | `yandex` \| `avito` \| `google` \| `2gis` \| `unknown` \| null |
| `numeric_value` | No | Parsed if present — **not validated** |
| `numeric_secondary` | No | e.g. review count |
| `text` | Yes | Verbatim or shortest defensible substring |
| `confidence` | Yes | B/C/X |

---

## 3. Subtype enum

| `sub_type` | Definition | Pilot exemplar |
|------------|------------|----------------|
| `rating_display` | Star/score + optional count | Яндекс 5 · 129+ оценок |
| `review_snippet` | Quote or review-section descriptor | «избранные отзывы с Авито» |
| `client_logos` | Named clients or logo strip alt text | SAFE UNKNOWN unless alt captured |
| `experience_claim` | Years on market | «10 лет» (if visible) |
| `fleet_size` | Fleet / vehicle count | «более 50 единиц» |
| `completed_orders` | Order/volume count claim | only explicit counts |
| `guarantee` | Guarantee/warranty language | «гарантируем квалифицированный сервис» |
| `certificate` | License, ISO, membership | license numbers in footer |
| `legal_entity` | ИНН, ОГРН, legal name block | v1 `legal_entity` |
| `partner_badge` | Bank/partner logos | alt text required |
| `statistics` | **Deprecated for prose** — only standalone metrics (N клиентов, N заказов) | Do not tag paragraphs |

**v2 rule:** If line length > 200 chars and no metric pattern → split or reclassify as `MARKETING_PATTERNS` / exclude from TRUST.

---

## 4. SOCIAL_PROOF family overlap

| Signal | Family |
|--------|--------|
| Platform rating block | TRUST (`rating_display`) + tag `SOCIAL_PROOF` reference |
| «Reviews section visible» | SOCIAL_PROOF, confidence C |
| Client logo wall | SOCIAL_PROOF (`client_logos`) |

Pack may show one line under «Trust & social proof» merging both — artifacts keep separate `family` for querying.

---

## 5. Confidence rules

| Grade | When |
|-------|------|
| B | Subtype rule + platform name or number in verbatim |
| C | review block marker only |
| X | Widget not rendered in static capture |

**SAFE UNKNOWN:** `trust_region_detected_no_verbatim`.

---

## 6. Pilot #1 defects addressed

| Defect | v2 fix |
|--------|--------|
| Taxi Maxim marketing essay → `statistics` | Max length + prose exclusion |
| Triumph merged rating + delivery in one trust blob | Split observations per metric line |
| `trust_count: 7` hides structure | Index `families_present` + subtype counts |
| Gruzovichec «Reviews section visible» | Keep C-grade SOCIAL_PROOF row |

---

## 7. Prohibited

- Authenticity judgment («fake reviews»)  
- Trust score / strength index  
- Comparison vs other competitors  
- LLM summarization of reviews  

---

*Trust model v2 — design only.*
