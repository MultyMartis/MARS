# Section — Contacts / forms

**section_id:** `contacts`  
**anchors:** `#contacts` (FAQ aside + final CTA)  
**priority:** P0 (conversion surface)

## Surfaces (as-built)

| Surface | Location | Primary action |
|---------|----------|----------------|
| Hero inline form | `screen-01-hero.html` | Рассчитать стоимость |
| FAQ embedded CTA | `screen-04-faq.html` | Form + tel + messengers |
| Final contact | `final-contact-cta.html` | Duplicate conversion block |

## Copy locks 🔒

- Phone: `+7 (900) 465-83-31` / `tel:+79004658331`
- Form success: «Спасибо! Заявка принята — скоро перезвоним…»
- Form microcopy: тип груза · адрес подачи · возможность работы · ориентировочная стоимость

## H2 variants

| Block | H2 |
|-------|-----|
| Final / FAQ aside | Нужно заказать манипулятор? |

**PPC note:** «Заказать» appears here and in meta description — partial mitigation for ad A1 H1 mismatch.

## Messengers

- WhatsApp: live `wa.me` link in partial
- MAX / Telegram: `data-link-todo` placeholders — **SAFE UNKNOWN** until operator URLs set

## Factory notes

- `data-form-id`: `zakaz-hero-quote`, `zakaz-contact-quote`
- `data-page-type`: `ppc-zakaz-manip`
- Consent checkbox required — legal partials linked

## CTA continuity

- Aligns with ad callout «Звонок и расчёт»
- Order steps section inverts priority: **call first**, then form — intentional mid-page pattern
