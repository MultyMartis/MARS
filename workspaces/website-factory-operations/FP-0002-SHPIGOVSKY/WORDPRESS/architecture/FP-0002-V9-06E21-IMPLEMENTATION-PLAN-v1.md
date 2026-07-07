# FP-0002 V9-06E21 Implementation Plan

Evidence: `validation/v9-06e21-reusable-blocks-batch-2-fields/implementation-plan.json`

## Admin IA (post E21)

`Настройки сайта` direct children include Batch 1 + Batch 2:

- Общие настройки
- Повторяемые блоки (container)
- Финальная форма, Специалисты, CTA-блоки (Batch 1)
- **Шапка**, **Подвал**, **Герои**, **Комфорт / преимущества** (Batch 2)

Top-level **Отзывы** (`fp02-reviews`) unchanged.

## Fallback policy

Block option → existing general option → page-local field (heroes only) → theme asset → V9 static.
