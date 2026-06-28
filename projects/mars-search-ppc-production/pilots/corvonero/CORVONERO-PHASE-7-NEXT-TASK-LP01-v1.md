# CORVONERO Phase 7 — Next Task LP-01 v1

**Prerequisite:** Phase 6.4 PASS — operator review of production content pack  
**Landing page:** LP-01  
**Builder:** Roman  
**Platform:** Tilda (`lk.corvonero.ru`)

---

## Task title

**Phase 7 — LP-01 Tilda build and operator staging review**

---

## Authorization

This next task authorizes:

- Tilda page build for `/programmist-1s` per handoff v1
- Staging preview for operator review
- Form wiring in Tilda (fields per spec)
- Click-to-call phone implementation

This next task does **not** authorize:

- Publish to production URL without operator sign-off
- Ad copy creation or campaign launch
- Minus-word deployment
- Commander / Yandex Direct import
- Modifications to corvonero.ru or unrelated LPs

---

## Operator inputs required before build start

| ID | Input | Owner |
|----|-------|-------|
| IMP-01 | Messenger URLs (MAX, Telegram, WhatsApp) | Operator / client |
| IMP-02 | Privacy consent legal text | Operator / client |
| IMP-03 | Tilda project access | Operator |
| IMP-05 | Published privacy policy URL | Operator |

Build may proceed with placeholders for IMP-01/02/05 if operator approves staging with visible TODO markers.

---

## Builder checklist

1. Read `CORVONERO-PHASE-6.4-LP01-TILDA-HANDOFF-v1.md`
2. Implement 15-block structure with Variant A first screen
3. Apply copy from `CORVONERO-PHASE-6.4-LP01-PRODUCTION-COPY-v1.md`
4. Configure form: Имя (optional), Телефон (required), submit «Заказать звонок»
5. Add CTAs: Обсудить задачу, Получить оценку, Заказать звонок
6. Phone `tel:+73833902928` in header, hero, contact, footer
7. FAQ accordion — 10 items from FAQ-v1
8. SEO per SEO-REQUIREMENTS-v1.json
9. Self-check against ACCEPTANCE-CRITERIA-v1 (26 items)
10. Share staging URL — **do not publish**

---

## Operator review gate

Operator must confirm:

- Copy accuracy (pricing, geo, configs)
- No prohibited claims
- Form and consent acceptable
- Messenger links correct (when provided)

Only then: publish + analytics wiring (Phase 7b or launch prep).

---

## Sequence note

LP-01 is P1 first in production sequence (LP-01 → LP-02 → LP-05 → LP-03 → LP-04 → LP-06 deferred).

---

## Stop condition

Stop after staging build and operator review request. Do not launch ads or publish without explicit operator publish authorization.
