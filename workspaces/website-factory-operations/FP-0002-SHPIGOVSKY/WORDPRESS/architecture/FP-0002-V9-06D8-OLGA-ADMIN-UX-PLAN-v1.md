# FP-0002 V9-06D8 Olga Admin UX Plan v1

**Date:** 2026-07-05  
**Audience:** Olga (content operator)  
**Evidence:** `validation/v9-06d8-content-seed-planning/olga-admin-ux-assessment.json`

---

## Goal

After D8 seed waves, Olga should edit routine copy in WP admin without developer help. Developer-controlled fields stay locked or hidden.

---

## Where Olga edits

| Location | Fields | Notes |
|---|---|---|
| **Настройки сайта** (Options) | phone, email, address, hours, social links, CTA labels | **Primary** for header/footer/contacts chrome |
| **Главная** (page 4) | hero slides, advantages, FAQ, CTA text | Repeaters — one section at a time |
| **Услуги** (page 5) | intro, FAQ | Do not change query mode |
| **Услуга** (service CPT) | lead, intro, signs, programme, stages, FAQ, CTA | Layout variant = developer |
| **Контакты** (page 20) | form intro, optional blocks | Phones: prefer Options |

---

## Classification summary

| Area | Current usability | Needed improvement | Classification | Before MVP |
|---|---|---|---|---:|
| Site Options | Empty; EN labels | D8-A seed; RU labels in D8-F | NEEDS_DEFAULT_SEED | yes |
| Home ACF | Partial seed | Repeater help text RU | NEEDS_LABEL_HELP_TEXT | no |
| Services Hub | Intro OK | Hide query_mode from editors | NEEDS_OPERATOR_DECISION | no |
| Service screen | 4 groups stacked | Group by section; lock variant | NEEDS_FIELD_GROUP_REORDER | no |
| Contacts | Overlap with Options | Document canonical phone source | NEEDS_LABEL_HELP_TEXT | yes |
| Media fields | Empty | Media library guide | NEEDS_OPERATOR_DECISION | no |
| Forms | Static only | Keep developer-only | DEVELOPER_ONLY | no |
| Legal IDs | Empty | Operator + legal review | NEEDS_OPERATOR_DECISION | no |

---

## Repeaters — guidance for Olga

1. **Hero slides (home):** max 5; each row = заголовок + текст + изображение.
2. **Advantages / FAQ:** add rows top-to-bottom; empty rows skipped on site.
3. **Signs / programme / stages (service):** match V9 section order; do not exceed max rows (enforced in admin).
4. **Social links (options):** label = «Telegram», URL = full `https://` link.

---

## Developer-only (do not expose to Olga routine edits)

- `service_layout_variant`
- `services_hub_query_mode`, `services_hub_show_placeholders`
- `manual_related_services`
- Form endpoint / API keys
- Menu structure, redirects, permalinks

---

## D8-F Admin UX Repair (optional source task)

**Not blocking D8-A.** Recommended before final handoff:

- Russian admin labels for English ACF JSON strings
- Field group `menu_order` by page section
- Instructions on Options vs page-level phone fields
- Optional ACF Extended features: **not approved**

---

## Result

**COMPLETE** — D8-F optional; seed waves can proceed with current ACF structure.
