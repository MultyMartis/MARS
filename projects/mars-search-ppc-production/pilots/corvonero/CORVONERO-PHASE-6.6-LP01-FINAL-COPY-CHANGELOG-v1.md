# CORVONERO Phase 6.6 — LP-01 Final Copy Changelog v1

**Phase:** 6.6 — Final production copy v3  
**Date:** 2026-06-29  
**Input authority:** Phase 6.5 LP-01 artefacts (v2 unchanged)  
**Scope:** Operator-approved minor edits to public copy only — semantic architecture and campaign allocation unchanged

---

## Summary

Operator approved seven targeted edits to v2 public copy, plus three v2 handoff consistency fixes. v3 supersedes v2 for public copy and Tilda handoff. v1 and v2 artefacts preserved on disk.

---

## Operator decisions applied

| # | Area | v2 → v3 change |
|---|------|----------------|
| 1 | Trust block lead | «Корво Неро» помогает бизнесу настраивать, дорабатывать, обновлять и сопровождать 1С. |
| 2 | Trust configs bullet | «опыт работы с конфигурациями…» → «работаем с конфигурациями УТ, УНФ, Розница, КА и БП» |
| 3 | Work format | Positive remote/onsite wording; removed regional refusal language |
| 4 | FAQ onsite (faq-04) | Positive answer: выезд в пределах Новосибирска; другие города — удалённо |
| 5 | FAQ estimate (faq-09) | Simplified: phone sufficient for form; details clarified on first call |
| 6 | Final CTA | H2 «Обсудим вашу задачу в 1С»; new body; CTA unchanged |
| 7 | Contacts | Lead: «Позвоните нам или выберите удобный мессенджер.» |
| 8 | Footer | Visible legal line: ИП Никифоров Роман Вадимович |

---

## Consistency fixes (v2 handoff mismatches resolved)

| # | Issue | v3 resolution |
|---|-------|---------------|
| 1 | Final CTA H2 differed between production copy and handoff | Both use «Обсудим вашу задачу в 1С» |
| 2 | Pricing H2 in JSON was «Стоимость работ программиста 1С» | Public H2: «Стоимость работы программиста 1С» everywhere |
| 3 | Form success/error messages ambiguous authority | Marked as implementation text only in Tilda handoff v3 |

---

## Unchanged from v2

- H1 and first-screen lead
- Service scope, configurations, process
- Pricing facts: от 3 000 ₽ в час; minimum 2 hours
- Form fields: Имя optional, Телефон required
- CTA set: Обсудить задачу / Получить оценку / Заказать звонок
- CA-01 campaign allocation (404 phrases)
- 13 message layers
- 9 FAQ items (questions unchanged; 2 answers revised)
- Meta title and description
- Phone +7 (383) 390-29-28
- Messengers: MAX, Telegram, WhatsApp (labels only; URLs remain implementation input)
- No VAT, SLA, partner claims, license sales, fake cases

---

## Typography audit (v3)

| Check | Status |
|-------|--------|
| Cyrillic 1С (not Latin 1C) | Pass |
| Mixed-alphabet Russian words | None found |
| «Корво Неро» consistent | Pass |
| «Новосибирск» inflection | Pass (в Новосибирске / в пределах Новосибирска) |
| ₽ formatting | «3 000 ₽ в час» consistent |
| Doubled spaces | None |
| Visible implementation placeholders | None in public copy |

---

## Artefact lineage

| v2 (preserved) | v3 (new) |
|----------------|----------|
| PRODUCTION-COPY-v2 | FINAL-PRODUCTION-COPY-v3 |
| MESSAGE-ARCHITECTURE-v2 | FINAL-MESSAGE-ARCHITECTURE-v3 |
| FAQ-v2 | FINAL-FAQ-v3 |
| TILDA-HANDOFF-v2 | FINAL-TILDA-HANDOFF-v3 |
| — | FINAL-COPY-CHANGELOG-v1 |
| — | FINAL-COPY-APPROVAL-v1 |
| — | RESULT-v1 |

Not versioned in Phase 6.6: FIRST-SCREEN-VARIANTS-v1, FORM-CONTACT-SPEC-v1, ACCEPTANCE-CRITERIA-v1 (still valid internally).
