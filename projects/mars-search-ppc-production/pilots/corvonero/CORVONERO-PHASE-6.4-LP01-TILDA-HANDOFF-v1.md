# CORVONERO Phase 6.4 — LP-01 Tilda Implementation Handoff v1

**Recipient:** Roman (builder)  
**Platform:** Tilda on `lk.corvonero.ru`  
**Page slug:** `/programmist-1s`  
**Status:** Handoff package — **do not publish until operator review**

---

## Page structure (top to bottom)

| # | Block purpose | Tilda block type (conceptual) | Copy source |
|---|---------------|-------------------------------|-------------|
| 1 | Header + nav minimal | Header / menu strip | Phone +7 (383) 390-29-28; logo Корво Неро |
| 2 | First screen hero | Cover / hero with buttons | PRODUCTION-COPY first screen Variant A |
| 3 | Audience qualification | Text block or cards | «Для кого услуги…» |
| 4 | Service scope | Cards or icon list (4–8 items) | «Что делает программист 1С» |
| 5 | Typical tasks | Bullet list or accordion | «Типовые задачи» |
| 6 | Configurations | Table or tag grid | УТ, УНФ, Розница, КА, БП |
| 7 | Work format | Two-column or cards | Remote Russia + onsite Novosibirsk |
| 8 | Pricing | Highlight box | от 3 000 ₽/час; min 2 hours |
| 9 | Process | Numbered steps | 5-step process |
| 10 | Trust | Text block | Evidence-only trust copy |
| 11 | FAQ | Tilda FAQ / accordion | FAQ-v1 (10 items) |
| 12 | Contact + messengers | Contact block | Phone + MAX/TG/WA placeholders |
| 13 | Lead form | Tilda form block | Имя + Телефон + consent |
| 14 | Final CTA | CTA strip | Обсудить задачу + phone |
| 15 | Footer | Footer | Legal placeholder + privacy link |

**Do not invent Tilda block IDs** — select equivalent blocks in project.

---

## Exact copy

Full Russian copy: `CORVONERO-PHASE-6.4-LP01-PRODUCTION-COPY-v1.md`  
FAQ full text: `CORVONERO-PHASE-6.4-LP01-FAQ-v1.md`

---

## Desktop / mobile

| Requirement | Detail |
|-------------|--------|
| Desktop | Readable line length; CTA buttons visible without excessive scroll |
| Mobile ≤1024px | Stack columns; click-to-call phone in header or hero |
| Min width | 320px — form usable |
| Sticky CTA | Optional — phone or primary CTA |

---

## Form configuration

| Field | Label | Required |
|-------|-------|----------|
| name | Имя | No |
| phone | Телефон | Yes |

**Submit button label:** Заказать звонок  
**Consent:** Checkbox — text `REQUIRED_FROM_OPERATOR_OR_CLIENT`  
**Success / error messages:** See FORM-CONTACT-SPEC-v1

---

## CTA labels (use exactly)

- Обсудить задачу
- Получить оценку
- Заказать звонок

---

## Messenger placeholders

| Channel | Implementation |
|---------|----------------|
| MAX | Icon + label; href = `REQUIRED_FROM_OPERATOR_OR_CLIENT` |
| Telegram | Icon + label; href = `REQUIRED_FROM_OPERATOR_OR_CLIENT` |
| WhatsApp | Icon + label; href = `REQUIRED_FROM_OPERATOR_OR_CLIENT` |

---

## Phone

Display: **+7 (383) 390-29-28**  
Link: `tel:+73833902928`  
Locations: header, hero, contact block, footer

---

## Legal / privacy placeholders

| Item | Status |
|------|--------|
| Legal entity footer line | ИП Никифоров Роман Вадимович (ATLAS LE-0006) — full requisites `REQUIRED_FROM_OPERATOR_OR_CLIENT` |
| Privacy policy URL | `CURRENT_LINK_SAFE_UNKNOWN` |
| PD consent text | `REQUIRED_FROM_OPERATOR_OR_CLIENT` |

---

## Analytics placeholders

Wire at launch prep (not in this build unless IDs provided):

- Yandex Metrika goal IDs: `REQUIRED_FOR_IMPLEMENTATION`
- Recommended event names: see FORM-CONTACT-SPEC-v1

---

## SEO settings (Tilda)

| Setting | Value |
|---------|-------|
| Page URL | `/programmist-1s` |
| Title | Программист 1С в Новосибирске — услуги специалиста \| Корво Неро |
| Description | Per PRODUCTION-COPY meta |
| Canonical | Self URL |
| OG image | `REQUIRED_FROM_OPERATOR_OR_CLIENT` |

---

## Acceptance criteria (builder self-check)

See `CORVONERO-PHASE-6.4-LP01-ACCEPTANCE-CRITERIA-v1.md`

---

## Prohibited

- Publish without operator sign-off
- Mention VAT/NDS
- Partner 1C badges
- Fake messenger links
- Extra mandatory form fields
- `/products` links in hero or primary CTA path
- corvonero.ru as landing URL

---

## Dependencies before go-live

1. Messenger URLs from operator/client  
2. Privacy/consent legal text  
3. Operator review of staging URL  
4. Analytics IDs (launch prep)
