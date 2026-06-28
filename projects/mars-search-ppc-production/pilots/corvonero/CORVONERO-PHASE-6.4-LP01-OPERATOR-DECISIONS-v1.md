# CORVONERO Phase 6.4 — LP-01 Operator Decisions Receipt v1

**Landing page:** LP-01 — Программист / специалист 1С  
**Campaign:** CA-01  
**Phrase coverage:** 404 ACCEPT  
**Decision authority:** Operator final decisions recorded 2026-06-29  
**Status:** **CLOSED** — content-strategy blockers cleared; implementation inputs only remain

---

## Receipt summary

| Metric | Value |
|--------|-------|
| Decisions closed | 18 |
| OPERATOR_CONFIRMED | 10 |
| OPERATOR_PROHIBITED | 6 |
| DEFERRED | 2 |
| REQUIRED_FOR_IMPLEMENTATION | 5 (implementation-only) |
| Content-strategy blockers remaining | **0** |

---

## Decision register

### Configurations (ODP-01)

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_CONFIRMED** |
| Approved list | УТ, УНФ, Розница, КА, БП |
| Prohibited | Adding configurations not in list; claiming «all 1C products» |

### Remote service scope (ODP-02)

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_CONFIRMED** |
| Service delivery | Remote service available **throughout Russia** |
| Campaign targeting | Initial advertising geography: **Novosibirsk + Novosibirsk Region only** |
| Rule | Do not confuse service-delivery geography with campaign targeting |

### On-site boundary (ODP-03)

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_CONFIRMED** |
| On-site visits | **Novosibirsk only** |
| Prohibited | On-site work throughout region or Russia |

### Pricing disclosure (ODP-06)

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_CONFIRMED** |
| Public wording | Стоимость работы — от 3 000 ₽ в час. Минимальный заказ — 2 часа. |
| Prohibited | Fixed project prices, subscription prices, discounts, package prices, emergency surcharges |

### VAT / NDS (ODP-05)

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_PROHIBITED** |
| Rule | Do not mention VAT / НДС on LP-01; do not infer tax status |

### Response time / SLA (ODP-07)

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_PROHIBITED** |
| Rule | Do not publish response-time or SLA promises |

### Cases and reviews (ODP-08)

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_PROHIBITED** |
| Rule | Do not use unverified cases, reviews or client names in LP-01 v1; do not fabricate generalized case metrics |

### Partner and certificates (ODP-09)

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_PROHIBITED** |
| Rule | Do not claim official 1C partnership, certification or badge status |

### Platform and builder (ODP-10)

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_CONFIRMED** |
| Platform | Tilda |
| Builder | Roman |
| Note | Handoff only — Tilda not modified in Phase 6.4 |

### Product and license sales (ODP-04)

| Field | Value |
|-------|-------|
| Classification | **DEFERRED** |
| Status | **HOLD** — no product resale or license-sale messaging on LP-01 |

### LP-06 deferral (ODP-11 / RD-03)

| Field | Value |
|-------|-------|
| Classification | **DEFERRED** |
| Rule | LP-06 not part of this task |

### Approved service scope

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_CONFIRMED** |
| Scope | доработка конфигураций 1С; исправление ошибок; настройка учёта и бизнес-процессов; отчёты, обработки, печатные формы; интеграции (сайты, Битрикс, внешние системы); маркировка и Честный знак; обновление и сопровождение баз; разовые и срочные задачи; удалённая работа; выезд по Новосибирску |
| Prohibited expansion | обучение; продажа лицензий; франчайзинг; официальный партнёр; гарантированные сроки реакции; круглосуточная поддержка; отраслевая экспертиза without evidence |

### Messengers

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_CONFIRMED** |
| Channels | MAX, Telegram, WhatsApp |
| Implementation | All three required on page; actual links **REQUIRED_FROM_OPERATOR_OR_CLIENT** |

### Form fields

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_CONFIRMED** |
| Fields | Имя, Телефон |
| Phone | Required |
| Name | Optional unless canonical form policy requires otherwise |
| Prohibited | Hidden mandatory company/email/comment fields |

### CTA set

| Field | Value |
|-------|-------|
| Classification | **OPERATOR_CONFIRMED** |
| Labels | Обсудить задачу; Получить оценку; Заказать звонок |
| Prohibited | Additional aggressive CTA wording |

---

## Implementation-only inputs (not content blockers)

| ID | Item | Status |
|----|------|--------|
| IMP-01 | Messenger URLs (MAX, Telegram, WhatsApp) | **REQUIRED_FROM_OPERATOR_OR_CLIENT** |
| IMP-02 | Privacy / consent legal text | **REQUIRED_FROM_OPERATOR_OR_CLIENT** |
| IMP-03 | Tilda project access for Roman | **REQUIRED_FOR_IMPLEMENTATION** |
| IMP-04 | Analytics / call-tracking IDs | **REQUIRED_FOR_IMPLEMENTATION** (launch prep) |
| IMP-05 | Published privacy policy URL on lk.corvonero.ru | **CURRENT_LINK_SAFE_UNKNOWN** |

---

## Superseded Phase 6.2 open items

All ODP-01..ODP-11 items affecting LP-01 content authority are **closed** by this receipt. Phase 6.2 `NEEDS_OPERATOR_CONFIRMATION` flags for LP-01 message evidence are resolved per classifications above.

---

## Authority references

- `CORVONERO-PHASE-6.2-OPERATOR-DECISION-PACKET-v3.*`
- `CORVONERO-PHASE-6.2-LP-01-PROGRAMMER-REQUIREMENTS-v1.*`
- ATLAS ORG-0009 / LE-0006 (brand and legal entity reference only)
- Operator decisions embedded in Phase 6.4 task charter (2026-06-29)
