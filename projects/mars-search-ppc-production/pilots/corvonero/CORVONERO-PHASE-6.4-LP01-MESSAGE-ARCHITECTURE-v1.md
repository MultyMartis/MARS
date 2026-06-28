# CORVONERO Phase 6.4 — LP-01 Message Architecture v1

**Landing page:** LP-01  
**Campaign:** CA-01 (404 ACCEPT phrases)  
**Default first-screen variant:** **A** (specialist intent)  
**Content authority:** CLOSED

---

## Architecture overview

Thirteen message layers in scroll order. Each layer maps to one or more CA-01 ad groups and phrase intent families without keyword stuffing.

| # | Layer ID | H2 direction (RU) |
|---|----------|-------------------|
| 1 | first_screen | — (H1 zone) |
| 2 | audience | Для кого услуги программиста 1С |
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

## Layer specifications

### 1. First-screen commercial proposition

| Attribute | Specification |
|-----------|---------------|
| Purpose | Immediate message match for specialist-search and service-order traffic |
| Audience intent | Find and hire a 1C programmer / specialist in Novosibirsk context |
| Required content | H1 with programmer/specialist 1C; lead naming Корво Неро; Novosibirsk geo signal; primary CTA; phone above fold |
| Prohibited claims | Official partner; SLA; fixed project prices; license sales; unverified cases |
| Ad groups | ca-01-specialist-search (primary), ca-01-direct-service-order (secondary) |
| Phrase families | программист 1с, специалист 1с, 1с программист новосибирск, удалённо |
| CTA role | Primary: **Обсудить задачу**; Secondary: **Получить оценку** or phone |

### 2. Main audience

| Attribute | Specification |
|-----------|---------------|
| Purpose | Qualify B2B visitors; filter career/training intent |
| Audience intent | Confirm page is for businesses needing 1C specialist work |
| Required content | Decision-makers, бухгалтерия, IT; companies using 1C; not for обучение or employment |
| Prohibited claims | Job offers; courses; salary benchmarks |
| Ad groups | ca-01-specialist-search |
| Phrase families | бизнес, компания, для организации |
| CTA role | Soft — scroll to services or **Обсудить задачу** |

### 3. Core service scope

| Attribute | Specification |
|-----------|---------------|
| Purpose | Match direct-service-order and task intent |
| Audience intent | Understand what programmer engagement includes |
| Required content | Full approved scope list (10 items) |
| Prohibited claims | Training; licensing; franchising; 24/7 support |
| Ad groups | ca-01-direct-service-order, ca-01-specialist-search |
| Phrase families | услуги программиста 1с, доработка, интеграция, маркировка |
| CTA role | **Получить оценку** |

### 4. Typical tasks

| Attribute | Specification |
|-----------|---------------|
| Purpose | Cover task/result and problem intents without fake cases |
| Audience intent | «My 1C needs X done» |
| Required content | Error fix, report development, integration setup, marking, updates — as task bullets |
| Prohibited claims | Named clients; metrics; guaranteed timelines |
| Ad groups | ca-01-specialist-search |
| Phrase families | ошибка 1с, доработка, отчёт, интеграция, обновление |
| CTA role | **Обсудить задачу** |

### 5. Supported configurations

| Attribute | Specification |
|-----------|---------------|
| Purpose | Configuration-specific search match |
| Audience intent | «Programmer for UT / UNF / etc.» |
| Required content | УТ, УНФ, Розница, КА, БП — explicit list |
| Prohibited claims | «All 1C products»; ERP unless added by operator |
| Ad groups | ca-01-specialist-search |
| Phrase families | программист 1с ут, унф, розница, ка, бухгалтерия |
| CTA role | **Получить оценку** |

### 6. Work format

| Attribute | Specification |
|-----------|---------------|
| Purpose | Clarify remote vs on-site boundary |
| Audience intent | Remote work Russia-wide vs visit Novosibirsk |
| Required content | Remote — по всей России; выезд — только Новосибирск; campaign geo note internal only |
| Prohibited claims | On-site in NSO cities beyond Novosibirsk; office address if unknown |
| Ad groups | ca-01-specialist-search |
| Phrase families | удалённо, удаленная работа, новосибирск |
| CTA role | Phone or **Заказать звонок** |

### 7. Pricing

| Attribute | Specification |
|-----------|---------------|
| Purpose | Price-intent message match |
| Audience intent | Hourly cost, minimum order |
| Required content | от 3 000 ₽/час; минимальный заказ 2 часа; factors affecting cost |
| Prohibited claims | VAT; packages; subscriptions; discounts; fixed project quotes |
| Ad groups | ca-01-price-intent |
| Phrase families | стоимость часа, цена программиста, сколько стоит |
| CTA role | **Получить оценку** |

### 8. Work process

| Attribute | Specification |
|-----------|---------------|
| Purpose | Reduce friction for direct-order visitors |
| Audience intent | How engagement starts |
| Required content | Заявка → уточнение задачи → оценка → выполнение → сдача |
| Prohibited claims | Guaranteed response time; fixed delivery days |
| Ad groups | ca-01-direct-service-order |
| Phrase families | заказать, услуги, авито (competitive context — professional service) |
| CTA role | **Заказать звонок** |

### 9. Trust without unsupported claims

| Attribute | Specification |
|-----------|---------------|
| Purpose | Credibility from confirmed evidence only |
| Audience intent | Is this provider legitimate |
| Required content | Корво Неро — центр автоматизации 1С; опыт с внедрением и сопровождением; работа с типовыми конфигурациями |
| Prohibited claims | Partner badges; case studies; review quotes; client names |
| Ad groups | All CA-01 |
| Phrase families | — |
| CTA role | **Обсудить задачу** |

### 10. FAQ

| Attribute | Specification |
|-----------|---------------|
| Purpose | Long-tail intent and objection handling |
| Audience intent | Specific questions before contact |
| Required content | 8–10 Q&A from approved evidence (see FAQ artefact) |
| Prohibited claims | SLA; VAT; partner status; unverified pricing |
| Ad groups | ca-01-price-intent, ca-01-specialist-search |
| Phrase families | cost, remote, configurations, urgent |
| CTA role | Link to form |

### 11. Messenger and phone contact

| Attribute | Specification |
|-----------|---------------|
| Purpose | Multi-channel contact parity |
| Audience intent | Preferred channel contact |
| Required content | Phone +7 (383) 390-29-28; MAX, Telegram, WhatsApp icons/labels; links placeholder |
| Prohibited claims | Fake messenger URLs |
| Ad groups | All CA-01 |
| Phrase families | связаться, телефон |
| CTA role | Click-to-call; messenger deep links when provided |

### 12. Lead form

| Attribute | Specification |
|-----------|---------------|
| Purpose | Primary conversion |
| Audience intent | Request callback or estimate |
| Required content | Имя (optional), Телефон (required); consent checkbox; **Заказать звонок** submit |
| Prohibited claims | Extra mandatory fields |
| Ad groups | ca-01-direct-service-order, ca-01-price-intent |
| Phrase families | заказать звонок, заявка |
| CTA role | Submit = **Заказать звонок** |

### 13. Final CTA

| Attribute | Specification |
|-----------|---------------|
| Purpose | Last conversion opportunity |
| Audience intent | Ready to start |
| Required content | Short recap + **Обсудить задачу** + phone |
| Prohibited claims | Urgency manipulation; false scarcity |
| Ad groups | All CA-01 |
| Phrase families | — |
| CTA role | **Обсудить задачу** primary |

---

## Cross-layer rules

1. Single H1 on page — programmer/specialist 1C proposition.
2. Geography: Novosibirsk in H1/lead for campaign match; remote Russia in work-format only.
3. No phrase enumeration — natural Russian commercial copy.
4. All three approved CTAs appear at least once in defined roles.
5. Footer: legal entity reference from ATLAS LE-0006; privacy link placeholder.
