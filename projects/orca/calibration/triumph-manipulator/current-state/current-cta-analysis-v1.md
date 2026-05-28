# Current CTA Analysis v1 — zakaz

## ORCA blueprint CTA model

From `01-master-hot-general.md`:

| Role | Blueprint text |
|------|----------------|
| Primary | Узнать стоимость перевозки |
| Secondary | Позвонить сейчас |
| Strategy | Call + short form; messengers secondary |

Campaign instance `grp_fc12_zakaz` adds:

- `cta_semantics.primary_cta`: **call**
- `cta_phrase`: «Заказать по телефону»

## As-built CTA (v5 zakaz)

| Surface | Label | Mechanism |
|---------|-------|-----------|
| Hero form submit | Рассчитать стоимость | POST form → `data-form-endpoint="/backend/api/forms/send.php"` |
| Hero form call link | Позвонить | `tel:+79004658331` + desktop modal |
| Specs | Рассчитать стоимость | `#contacts` / modal callback |
| Cargo cards | Заказать перевозку > | `data-modal-open="modal-callback"` |
| Final contact | (footer partial) | Form + messengers MAX→TG→WA (per 5-ton handoff pattern) |

## Drift summary

| Item | Verdict |
|------|---------|
| Lexical: Узнать → Рассчитать | **Minor lexical drift** — same commercial intent |
| Form in hero vs blueprint “short form below” | **Productive** — form is primary visual CTA |
| Call vs form priority | **Ambiguous** — instance says call-first; hero **shows form first** on desktop |
| Messenger elevation in hero | **Pass** — not above phone/form in hero |

## CTA weight (visual)

| Element | Weight |
|---------|--------|
| Primary button (form) | High — filled primary in aside |
| Phone | Medium — outline in form footer |
| Cargo micro-CTAs | Medium-low — 6 competing entry points |
| Proof strip | Low — no click action |

## Risks (human reasoning)

1. **Six cargo buttons** may dilute single primary action for cold traffic.
2. **Consent checkbox** in hero form adds friction (required for compliance — acceptable if shortened on mobile).
3. **Call-first ads** (`ad_fc12_a1`) vs form-heavy hero — continuity tension for users expecting immediate dial prominence.

## Recommendation (calibration output)

Future pack should specify:

- `cta_primary_surface`: `hero_form` | `hero_call` | `split`
- `cta_label_locked`: exact Russian strings
- `cargo_card_cta`: optional / max count / mobile collapse rules
