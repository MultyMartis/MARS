# MIG Landing Offer Model v2

**Status:** design contract — **no runtime**.  
**Parent:** [mig-landing-analysis-v2.md](mig-landing-analysis-v2.md) · family `OFFERS`.

---

## 1. Canonical object

```json
{
  "observation_id": "mig-20260604-61b585-la003-obs002",
  "family": "OFFERS",
  "text": "В АВТОПАРКЕ БОЛЕЕ 50 МАШИН, ГОТОВЫХ К ВЫЕЗДУ ПРЯМО СЕЙЧАС!",
  "category": "fleet",
  "sub_type": "capacity_claim",
  "offer_surface": "hero",
  "block_id": "mig-20260604-61b585-la003-b002",
  "confidence": "B",
  "ambiguity": "none",
  "evidence": {
    "source": "website_snapshot",
    "snapshot_id": "mig-20260604-61b585-ws003",
    "snapshot_field": "/offers/1",
    "verbatim_text": "В АВТОПАРКЕ БОЛЕЕ 50 МАШИН, ГОТОВЫХ К ВЫЕЗДУ ПРЯМО СЕЙЧАС!",
    "capture_time": "2026-06-04T08:51:27.185Z"
  }
}
```

| Field | Required | Rules |
|-------|----------|-------|
| `observation_id` | Yes | Stable per landing |
| `family` | Yes | Always `OFFERS` |
| `text` | Yes | Verbatim; ≤500 chars per row (split long blobs in v2 extractor) |
| `category` | Yes | Enum §2; `unknown` if no rule match |
| `sub_type` | No | Finer grain (e.g. `discount_percent`, `fixed_price_claim`) |
| `offer_surface` | No | DOM role: heading, hero, card_title, list_item, button_label |
| `block_id` | No | Link to `visible_blocks[]` |
| `pricing_ref` | No | `pricing_id` when offer line is pure price |
| `confidence` | Yes | Evidence grade §3 |
| `ambiguity` | No | `none` \| `multi_interpretation` \| `high` |
| `evidence` | Yes | §1 |

---

## 2. Category enum (rules-only)

| `category` | Detection hints (RU/EN tokens) | Pilot example |
|------------|----------------------------------|---------------|
| `speed` | подача, минут, срочн, быстр, через N | «20 минут», «подача за 15 минут» |
| `price` | от N, ₽, руб, дешевле, % | «от 539 руб», «ниже на 20%» |
| `fleet` | машин, автопарк, газел, тонн, кузов | «более 50 машин» |
| `scope` | переезд, межгород, вывоз, грузчик | «квартирные переезды» |
| `quality` | опыт, профессион, аккурат | «обширным опытом» |
| `convenience` | приложение, без рации, онлайн | «мобильное приложение» |
| `b2b` | юридическ, ИП, договор | «Для юридических лиц» |
| `app_channel` | скачать, App Store, Google Play | «Скачать приложение» |
| `unknown` | No rule hit | Section titles misclassified in v1 |

**Forbidden:** LLM category assignment; «primary offer» flag.

---

## 3. Confidence rules

| Grade | Condition |
|-------|-----------|
| **A** | Operator `manual_annotation` only |
| **B** | `evidence.source = website_snapshot` + `snapshot_field` set |
| **C** | `page_html` only or heading heuristic without snapshot offer path |
| **X** | Text not reproducible from artifacts — must not emit as offer |

---

## 4. Nav-noise exclusion (v2)

Do **not** emit OFFERS for exact or normalized matches:

- Отзывы о нас  
- Вопросы и ответы  
- О компании / О Компании  
- Контакты …  
- Мы в социальных сетях  
- FAQ section labels without promotional clause  

Store exclusion in `_processing.excluded_offers[]` for audit.

---

## 5. SAFE UNKNOWN

Emit when:

- `offers[]` empty after acquisition and HTML re-scan finds no promo strings.  
- Only nav headings detected.

```json
{
  "family": "OFFERS",
  "status": "safe_unknown",
  "reason": "no_marketing_offer_strings_after_nav_filter",
  "confidence": "X"
}
```

---

## 6. v1 mapping

| v1 `offers[]` field | v2 |
|---------------------|-----|
| `offer_id` | `observation_id` |
| `text` | `text` |
| `offer_surface` | `offer_surface` |
| — | `category` (new) |
| `evidence` | `evidence` + required `snapshot_id` |

---

*Offer model v2 — design only.*
