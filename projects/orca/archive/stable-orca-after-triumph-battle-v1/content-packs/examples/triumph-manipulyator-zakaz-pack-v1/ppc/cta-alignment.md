# PPC — CTA alignment

## Instance vs as-built

| Source | Primary CTA semantics |
|--------|----------------------|
| `ad_fc12_a1` `cta_semantics` | `call` — «Заказать по телефону» |
| `ad_fc12_a2` | (description emphasizes вызов + расчёт) |
| Landing hero | `form` — «Рассчитать стоимость» |
| Order steps block | **Call first**, then form |

## CTA string locks 🔒

| Role | Label | Target |
|------|-------|--------|
| Primary (hero) | Рассчитать стоимость | form submit |
| Secondary | Позвонить | `tel:+79004658331` |
| Mid-page specs/pricing | Рассчитать стоимость | `#contacts` / modal |
| Order steps | Позвонить (primary button) | tel |

## Continuity assessment

| Dimension | Status |
|-----------|--------|
| «Расчёт» in ads → form | **strong** |
| «Звонок» in callout → tel surfaces | **strong** |
| call-first mobile doctrine vs form-first hero | **ambiguous** |

## Pack visual field

`cta_priority: form` — document tension in `visual-semantics/cta-priority.md`.

## Recommended vNext (calibration, not implementation)

```yaml
mobile_hero_cta_order: [call, form_submit]  # if operator confirms call-first
```

## Forbidden drift

- Replacing «Рассчитать стоимость» with «Узнать цену» without PPC review
- Removing tel from hero form
- Fake urgency CTAs («только сегодня»)
