# CORVONERO Phase 6.5 — LP-01 Tilda Implementation Handoff v2

**Recipient:** Roman (builder)  
**Platform:** Tilda on `lk.corvonero.ru`  
**Page slug:** `/programmist-1s`  
**Status:** Handoff package — **do not publish until operator review**  
**Supersedes for build copy:** `CORVONERO-PHASE-6.4-LP01-TILDA-HANDOFF-v1.md`

---

## Page structure (top to bottom)

| # | Block purpose | Tilda block type (conceptual) | Copy source |
|---|---------------|-------------------------------|-------------|
| 1 | Header + nav minimal | Header / menu strip | Phone +7 (383) 390-29-28; logo Корво Неро |
| 2 | First screen hero | Cover / hero with buttons | PRODUCTION-COPY-v2 first screen |
| 3 | Audience | Text block or cards | «Услуги программиста 1С для компаний и ИП» |
| 4 | Service scope | Cards or icon list | «Что делает программист 1С» |
| 5 | Typical tasks | Bullet list | «Типовые задачи» |
| 6 | Configurations | Table or tag grid | УТ, УНФ, Розница, КА, БП |
| 7 | Work format | Two-column or cards | Remote Russia + onsite Novosibirsk |
| 8 | Pricing | Highlight box | от 3 000 ₽/час; min 2 hours |
| 9 | Process | Numbered steps | 5-step process v2 |
| 10 | Trust | Text block | Evidence-only trust copy v2 |
| 11 | FAQ | Tilda FAQ / accordion | FAQ-v2 (9 items) |
| 12 | Contact + messengers | Contact block | Phone + messenger labels |
| 13 | Lead form | Tilda form block | Имя + Телефон + consent |
| 14 | Final CTA | CTA strip | Обсудить задачу + phone |
| 15 | Footer | Footer | Brand + phone + legal line when provided |

**Do not invent Tilda block IDs** — select equivalent blocks in project.

---

## Exact copy

Full Russian copy: `CORVONERO-PHASE-6.5-LP01-PRODUCTION-COPY-v2.md`  
FAQ full text: `CORVONERO-PHASE-6.5-LP01-FAQ-v2.md`

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

**Success message (implementation draft):**  
«Спасибо! Мы получили заявку и перезвоним по указанному телефону.»

**Error message (implementation draft):**  
«Не удалось отправить заявку. Проверьте телефон или позвоните нам: +7 (383) 390-29-28.»

---

## CTA labels (use exactly)

- Обсудить задачу
- Получить оценку
- Заказать звонок

---

## Phone

Display: **+7 (383) 390-29-28**  
Link: `tel:+73833902928`  
Locations: header, hero, contact block, footer

---

## Messengers

| Channel | Public page | Implementation input |
|---------|-------------|----------------------|
| MAX | Label + icon | URL from operator/client |
| Telegram | Label + icon | URL/username from operator/client |
| WhatsApp | Label + icon | URL/phone binding from operator/client |

**Rules:**

- Show all three visually on the page.
- Do not display placeholder tokens (`REQUIRED_FROM_OPERATOR_OR_CLIENT`) as visible page text.
- Do not fabricate deep links until operator provides URLs.
- Until URLs provided: hide links or use non-visible builder notes — not fake working URLs.

---

## Implementation inputs (not visible production copy)

| Item | Source | Notes |
|------|--------|-------|
| Messenger URLs | Operator/client | MAX, Telegram, WhatsApp |
| Privacy policy URL | Operator/client | Link in consent and footer |
| PD consent checkbox text | Operator/client | Legal wording |
| Legal entity footer line | ATLAS LE-0006 + operator | ИП Никифоров Роман Вадимович; full requisites if differ |
| OG image | Operator/client | Tilda page settings |
| Tilda project access | Operator | Builder Roman |
| Yandex Metrika goal IDs | Launch prep | See FORM-CONTACT-SPEC-v1 event names |

---

## SEO settings (Tilda)

| Setting | Value |
|---------|-------|
| Page URL | `/programmist-1s` |
| Title | Программист 1С в Новосибирске — услуги специалиста \| Корво Неро |
| Description | Per PRODUCTION-COPY-v2 meta |
| Canonical | Self URL |
| OG image | Implementation input — operator/client |

---

## Acceptance criteria (builder self-check)

See `CORVONERO-PHASE-6.4-LP01-ACCEPTANCE-CRITERIA-v1.md` — still valid. Additional v2 check: no governance placeholder text visible on staging.

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
