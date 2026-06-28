# CORVONERO Phase 6.6 — LP-01 Final Tilda Implementation Handoff v3

**Recipient:** Roman (builder)  
**Platform:** Tilda on `lk.corvonero.ru`  
**Page slug:** `/programmist-1s`  
**Status:** Final handoff package — **ready for Phase 7 build when authorized**  
**Supersedes for build copy:** `CORVONERO-PHASE-6.5-LP01-TILDA-HANDOFF-v2.md`

---

## Page structure (top to bottom)

| # | Block purpose | Tilda block type (conceptual) | Copy source |
|---|---------------|-------------------------------|-------------|
| 1 | Header + nav minimal | Header / menu strip | Phone +7 (383) 390-29-28; logo Корво Неро |
| 2 | First screen hero | Cover / hero with buttons | PRODUCTION-COPY-v3 first screen |
| 3 | Audience | Text block or cards | «Услуги программиста 1С для компаний и ИП» |
| 4 | Service scope | Cards or icon list | «Что делает программист 1С» |
| 5 | Typical tasks | Bullet list | «Типовые задачи» |
| 6 | Configurations | Table or tag grid | УТ, УНФ, Розница, КА, БП |
| 7 | Work format | Two-column or cards | Remote Russia + onsite Novosibirsk |
| 8 | Pricing | Highlight box | от 3 000 ₽ в час; min 2 hours |
| 9 | Process | Numbered steps | 5-step process |
| 10 | Trust | Text block | Final trust copy v3 |
| 11 | FAQ | Tilda FAQ / accordion | FAQ-v3 (9 items) |
| 12 | Contact + messengers | Contact block | Lead + phone + messenger labels |
| 13 | Lead form | Tilda form block | Имя + Телефон + consent |
| 14 | Final CTA | CTA strip | Обсудим вашу задачу в 1С |
| 15 | Footer | Footer | Brand + phone + legal line |

**Do not invent Tilda block IDs** — select equivalent blocks in project.

---

## Exact copy

Full Russian copy: `CORVONERO-PHASE-6.6-LP01-FINAL-PRODUCTION-COPY-v3.md`  
FAQ full text: `CORVONERO-PHASE-6.6-LP01-FINAL-FAQ-v3.md`

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

**Form heading:** Оставить заявку на услуги программиста 1С  
**Supporting text:** Оставьте телефон — уточним задачу и сориентируем по стоимости.  
**Submit button label:** Заказать звонок

---

## Form messages — implementation text only

> **Not public-copy authority.** Use at Tilda build; do not treat as separate customer-facing copy source.

**Success message (implementation):**  
«Спасибо! Мы получили заявку и перезвоним по указанному телефону.»

**Error message (implementation):**  
«Не удалось отправить заявку. Проверьте телефон или позвоните нам: +7 (383) 390-29-28.»

---

## CTA labels (use exactly)

- Обсудить задачу
- Получить оценку
- Заказать звонок

---

## Final CTA block

| Element | Copy |
|---------|------|
| **H2** | Обсудим вашу задачу в 1С |
| **Body** | Расскажите, что нужно исправить, настроить или доработать. Уточним детали и сориентируем по стоимости. |
| **Button** | Обсудить задачу |
| **Phone** | +7 (383) 390-29-28 |

---

## Contact block

| Element | Copy |
|---------|------|
| **H2** | Связаться с нами |
| **Lead** | Позвоните нам или выберите удобный мессенджер. |
| **Phone** | +7 (383) 390-29-28 |
| **Messengers** | MAX, Telegram, WhatsApp |

---

## Pricing block

| Element | Copy |
|---------|------|
| **H2** | Стоимость работы программиста 1С |
| **Rate** | от 3 000 ₽ в час |
| **Minimum** | Минимальный заказ — 2 часа |

---

## Phone

Display: **+7 (383) 390-29-28**  
Link: `tel:+73833902928`  
Locations: header, hero, contact block, final CTA, footer

---

## Messengers

| Channel | Public page | Implementation input |
|---------|-------------|----------------------|
| MAX | Label + icon | URL from operator/client |
| Telegram | Label + icon | URL/username from operator/client |
| WhatsApp | Label + icon | URL/phone binding from operator/client |

**Rules:**

- Show all three visually on the page.
- Do not display placeholder tokens as visible page text.
- Do not fabricate deep links until operator provides URLs.
- Until URLs provided: hide links or use non-visible builder notes — not fake working URLs.

---

## Footer

| Element | Copy |
|---------|------|
| Brand | Центр автоматизации «Корво Неро» |
| Phone | +7 (383) 390-29-28 |
| Legal entity (visible) | ИП Никифоров Роман Вадимович |

---

## Implementation inputs (not visible production copy)

| Item | Source | Notes |
|------|--------|-------|
| Messenger URLs | Operator/client | MAX, Telegram, WhatsApp |
| Privacy policy URL | Operator/client | Link in consent and footer |
| PD consent checkbox text | Operator/client | Legal wording |
| Full legal requisites | ATLAS LE-0006 + operator | For implementation verification; visible line above is minimum |
| OG image | Operator/client | Tilda page settings |
| Tilda project access | Operator | Builder Roman |
| Yandex Metrika goal IDs | Launch prep | See FORM-CONTACT-SPEC-v1 event names |
| Form success/error messages | This handoff — implementation text | See «Form messages — implementation text only» |

---

## SEO settings (Tilda)

| Setting | Value |
|---------|-------|
| Page URL | `/programmist-1s` |
| Title | Программист 1С в Новосибирске — услуги специалиста \| Корво Неро |
| Description | Per PRODUCTION-COPY-v3 meta |
| Canonical | Self URL |
| OG image | Implementation input — operator/client |

---

## Acceptance criteria (builder self-check)

See `CORVONERO-PHASE-6.4-LP01-ACCEPTANCE-CRITERIA-v1.md` — still valid. Additional v3 check: no governance placeholder text visible on staging; final CTA H2 matches production copy.

---

## Prohibited

- Publish without operator sign-off
- Mention VAT/NDS
- Partner 1C badges
- Fake messenger links
- Visible placeholder strings on production page
- Extra mandatory form fields
- `/products` links in hero or primary CTA path
- corvonero.ru as landing URL

---

## Dependencies before go-live

1. Messenger URLs from operator/client  
2. Privacy/consent legal text  
3. Operator review of staging URL  
4. Analytics IDs (launch prep)
