# MIG Landing Observation Families v2

**Status:** design reference for [mig-landing-analysis-v2.md](mig-landing-analysis-v2.md)  
**Not:** runtime registry JSON (future: `config/landing-observation-families-v2.json`).

---

## Family index

| ID | Pack heading (RU) | Primary consumer question |
|----|-------------------|---------------------------|
| OFFERS | Ценностные обещания | Что обещает страница клиенту? |
| PRICING | Цены и тарифы | Какие цифры видны? |
| CTA | Действия | Как заказать / связаться? |
| TRUST | Доверие | Чем подкрепляют надёжность? |
| LEAD_CAPTURE | Захват лида | Какие формы и шаги? |
| SOCIAL_PROOF | Соцдоказательства | Отзывы, рейтинги, логотипы |
| CONTACT_MODEL | Контакты | Каналы связи |
| DELIVERY_PROMISE | Скорость и доступность | Подача, 24/7, срочность |
| SERVICE_COVERAGE | Охват услуг | Гео, типы перевозок, тоннаж |
| MARKETING_PATTERNS | Структура страницы | Как устроена витрина (без оценки качества) |

---

## Per-family specification

### OFFERS

- **Definition:** Market-facing promise strings excluding navigation section titles.
- **Evidence sources:** `/offers/*`, `/headings/*` (filtered), hero/card copy in `page.html`.
- **Confidence:** B = snapshot pointer; C = HTML-only; X = not found.
- **SAFE UNKNOWN:** `no_classified_offers_after_nav_filter`.
- **Pilot noise rule:** FAQ questions are not offers unless explicitly promotional.

### PRICING

- **Definition:** Monetary signals with or without currency marker.
- **Evidence sources:** `/pricing_signals/*`, pricing_block `content_summary`.
- **Confidence:** B = contains `₽` or `руб`; C = «стоимость» without number.
- **SAFE UNKNOWN:** `pricing_block_present_no_lines`.

### CTA

- **Definition:** Action element with visible label and optional target.
- **Evidence sources:** `/cta_elements/*`, `/forms/*`, `/contacts/phones`, messengers.
- **Confidence:** B = typed + href/tel; C = label only.
- **SAFE UNKNOWN:** `forms_without_labels`.

### TRUST

- **Definition:** Credibility-bearing verbatim lines (see trust model doc).
- **Evidence sources:** `/trust_signals_visible/*`, review blocks, legal footer.
- **Confidence:** B = subtype match + short line; C = long blob split pending.
- **SAFE UNKNOWN:** `trust_block_no_verbatim`.

### LEAD_CAPTURE

- **Definition:** Form structure and visible purpose heading.
- **Evidence sources:** `/forms/*`, adjacent headings.
- **Confidence:** B = ≥1 field; C = form count only.
- **SAFE UNKNOWN:** `lead_form_detected_fields_missing`.

### SOCIAL_PROOF

- **Definition:** External validation surfaces (platform ratings, review feeds, logos).
- **Evidence sources:** review blocks, trust lines with platform names.
- **Confidence:** B = platform + metric; C = «Reviews section visible».
- **SAFE UNKNOWN:** `reviews_block_no_text`.

### CONTACT_MODEL

- **Definition:** Enumerated channels (phone, email, messenger, app-only).
- **Evidence sources:** `/contacts`.
- **Confidence:** B = channel list complete in snapshot; C = partial.
- **SAFE UNKNOWN:** `contact_heading_only`.

### DELIVERY_PROMISE

- **Definition:** Time-bound or availability promises.
- **Evidence sources:** offers, headings, trust lines with time lexicon (`минут`, `24`, `круглосуточно`, `срочн`).
- **Confidence:** B = explicit duration; C = vague speed adjective.
- **SAFE UNKNOWN:** `no_delivery_promise_detected`.

### SERVICE_COVERAGE

- **Definition:** Geography and service taxonomy visible on page.
- **Evidence sources:** headings, service lists, meta_description.
- **Confidence:** B = city/region in verbatim body; C = title-only geo.
- **SAFE UNKNOWN:** `coverage_not_stated`.

### MARKETING_PATTERNS

- **Definition:** Composite structural tags (rules-only combinations).
- **Evidence sources:** block types, CTA mix, form count, app links.
- **Examples:** `app_first_order`, `phone_primary`, `dual_lead_form`, `faq_heavy`, `tariff_grid`.
- **Confidence:** B = ≥2 rules fired; C = 1 rule.
- **SAFE UNKNOWN:** never guess pattern without rule hit.

---

## Cross-family deduplication

| Situation | Resolution |
|-----------|------------|
| Same verbatim in OFFERS and DELIVERY_PROMISE | Prefer DELIVERY_PROMISE if time token present; else OFFERS |
| Price line in OFFERS and PRICING | PRICING only |
| Rating line in OFFERS and SOCIAL_PROOF | SOCIAL_PROOF / TRUST by subtype |
| Phone in CTA and CONTACT_MODEL | CONTACT_MODEL for channel list; CTA for clickable CTA row |

---

## Operator projection order (pack)

1. DELIVERY_PROMISE + SERVICE_COVERAGE (context)  
2. OFFERS (filtered)  
3. PRICING  
4. TRUST + SOCIAL_PROOF  
5. CTA + LEAD_CAPTURE + CONTACT_MODEL  
6. MARKETING_PATTERNS + blocks  

---

*Reference only — implementation deferred per Landing Analysis v2 scope.*
