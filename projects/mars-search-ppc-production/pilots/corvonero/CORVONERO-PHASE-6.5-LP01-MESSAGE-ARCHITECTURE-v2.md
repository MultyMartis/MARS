# CORVONERO Phase 6.5 — LP-01 Message Architecture v2

**Landing page:** LP-01  
**Campaign:** CA-01 (404 ACCEPT phrases) — **unchanged**  
**Default first-screen variant:** **A** (editorial copy v2)  
**Content authority:** CLOSED (Phase 6.4); editorial v2 applies to public copy only

---

## Architecture overview

Thirteen message layers in scroll order — **same structure as v1**. Each layer maps to one or more CA-01 ad groups and phrase intent families without keyword stuffing.

| # | Layer ID | H2 direction (RU) |
|---|----------|-------------------|
| 1 | first_screen | — (H1 zone) |
| 2 | audience | Услуги программиста 1С для компаний и ИП |
| 3 | service_scope | Что делает программист 1С |
| 4 | typical_tasks | Типовые задачи |
| 5 | configurations | Конфигурации 1С |
| 6 | work_format | Формат работы |
| 7 | pricing | Стоимость работ |
| 8 | process | Как мы работаем |
| 9 | trust | Почему обращаются в Корво Неро |
| 10 | faq | Частые вопросы |
| 11 | messengers_phone | Связаться с нами |
| 12 | lead_form | Оставить заявку |
| 13 | final_cta | Готовы обсудить задачу |

---

## Editorial v2 notes (cross-cutting)

1. **Governance language** — filtering intent (no training, no vacancies, no partner claims, no SLA) remains in acceptance criteria and internal compliance; **not** in visible page copy.
2. **First screen** — H1 shifts to task/scope proposition; Novosibirsk retained in meta, lead, work-format, and trust layers.
3. **Trust layer** — positive evidence-only framing; no disclaimers about absent cases or partner status.
4. **FAQ** — 9 customer-facing items; no partner question; no negative scope exclusions in answers.

---

## Layer specifications

### 1. First-screen commercial proposition

| Attribute | Specification |
|-----------|---------------|
| Purpose | Immediate message match for specialist-search and service-order traffic |
| Audience intent | Find and hire a 1C programmer for practical tasks |
| Required content | H1 — доработка, настройка, исправление ошибок; lead — разовые задачи, remote Russia, onsite Novosibirsk; primary CTA; phone above fold |
| Prohibited claims | Official partner; SLA; fixed project prices; license sales; unverified cases |
| Ad groups | ca-01-specialist-search (primary), ca-01-direct-service-order (secondary) |
| Phrase families | программист 1с, специалист 1с, доработка 1с, удалённо |
| CTA role | Primary: **Обсудить задачу**; Secondary: **Получить оценку** |

**v2 copy:** See PRODUCTION-COPY-v2 first screen.

### 2. Main audience

| Attribute | Specification |
|-----------|---------------|
| Purpose | Qualify B2B visitors naturally |
| Audience intent | Confirm services fit companies and IP needing external 1C specialist |
| Required content | Companies and IP; разовые и текущие задачи; external specialist without staff hire; config mention optional |
| Prohibited in public copy | Explicit training/vacancy filtering statements |
| Ad groups | ca-01-specialist-search |
| CTA role | Soft — scroll to services or **Обсудить задачу** |

### 3. Core service scope

| Attribute | Specification |
|-----------|---------------|
| Purpose | Match direct-service-order and task intent |
| Required content | Full approved scope list (8 bullets) |
| Prohibited claims | Training; licensing; 24/7 support |
| Ad groups | ca-01-direct-service-order, ca-01-specialist-search |
| CTA role | **Получить оценку** |

### 4. Typical tasks

| Attribute | Specification |
|-----------|---------------|
| Purpose | Cover task/result and problem intents without fake cases |
| Required content | Error fix, reports, integration, marking, post-update доработки failure — business language |
| v2 edit | Replace colloquial «поплыла логика» with formal wording |
| CTA role | **Обсудить задачу** |

### 5. Supported configurations

| Attribute | Specification |
|-----------|---------------|
| Required content | УТ, УНФ, Розница, КА, БП — explicit list |
| CTA role | **Получить оценку** |

### 6. Work format

| Attribute | Specification |
|-----------|---------------|
| Required content | Remote — по всей России; выезд — только Новосибирск |
| Removed from public copy | Campaign geo / advertising traffic notes |
| CTA role | **Заказать звонок** |

### 7. Pricing

| Attribute | Specification |
|-----------|---------------|
| Required content | от 3 000 ₽/час; минимальный заказ 2 часа; cost factors |
| Removed from public copy | Packages/subscriptions/discounts not published |
| CTA role | **Получить оценку** |

### 8. Work process

| Attribute | Specification |
|-----------|---------------|
| Required content | Five steps: обсуждаем → уточняем → согласовываем → выполняем → передаём |
| CTA role | **Заказать звонок** |

### 9. Trust without unsupported claims

| Attribute | Specification |
|-----------|---------------|
| Purpose | Credibility from confirmed evidence only — positive framing |
| Required content | Automation center positioning; разовые задачи; hourly model; contract/cashless; remote; Novosibirsk onsite; supported configs |
| Removed from public copy | Disclaimers about absent cases, partner status, certifications |
| CTA role | **Обсудить задачу** |

### 10. FAQ

| Attribute | Specification |
|-----------|---------------|
| Required content | 9 Q&A — see FAQ-v2 |
| Removed | Partner status question; training/license negatives; SLA-internal explanations |
| CTA role | Link to form |

### 11. Messenger and phone contact

| Attribute | Specification |
|-----------|---------------|
| Required content | Phone +7 (383) 390-29-28; MAX, Telegram, WhatsApp labels |
| Implementation inputs | Messenger URLs — not visible placeholder text on page |
| CTA role | Click-to-call; messenger links when provided at build |

### 12. Lead form

| Attribute | Specification |
|-----------|---------------|
| Required content | Имя (optional), Телефон (required); **Заказать звонок** submit |
| Supporting text v2 | Оставьте телефон — уточним задачу и сориентируем по стоимости. |
| Implementation inputs | Consent checkbox legal text — not in production copy draft |

### 13. Final CTA

| Attribute | Specification |
|-----------|---------------|
| Required content | Short recap + **Обсудить задачу** + phone |
| CTA role | **Обсудить задачу** primary |

---

## Cross-layer rules (unchanged from v1)

1. Single H1 on page — programmer 1C task proposition (v2 wording).
2. Geography: Novosibirsk in meta, lead, work-format, trust, FAQ; remote Russia explicit.
3. No phrase enumeration — natural Russian commercial copy.
4. All three approved CTAs appear at least once in defined roles.
5. Footer legal/privacy — implementation inputs only in v2 public copy draft.
