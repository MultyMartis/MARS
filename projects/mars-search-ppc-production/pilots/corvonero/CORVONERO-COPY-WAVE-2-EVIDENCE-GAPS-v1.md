# CORVONERO Copy Wave 2 — Evidence Gaps v1

**Scope:** LP-02, LP-03, LP-04, LP-05  
**Checkpoint:** `2de6bafab4ca80f2e1bf641468f0b973c4c21282`  
**Status:** operator-review packet — **not** production approval  
**Generated:** 2026-06-29

---

## Cross-page facts affecting public copy

| Fact | Classification | LP impact | Draft handling |
|------|----------------|-----------|----------------|
| Центр автоматизации «Корво Неро» | CONFIRMED | all | Used in trust/footer blocks |
| Телефон +7 (383) 390-29-28 | CONFIRMED | all | Visible on every LP |
| ЮЛ и ИП, договор, безнал | CONFIRMED | all | FAQ and trust blocks |
| Удалённо по России | CONFIRMED | all | Work-format blocks |
| Выезд только Новосибирск | CONFIRMED | all | Work-format blocks |
| Рекламная география: НСО | CONFIRMED | all | Meta/H1 geo where relevant |
| Конфигурации УТ, УНФ, Розница, КА, БП | CONFIRMED | LP-02, LP-03, LP-05 | Configuration tables |
| Разовые задачи и абонентское сопровождение | CONFIRMED | LP-02 | Formats block without тарифов |
| Почасовая модель 3 000 ₽ / 2 ч мин. | CONFIRMED (LP-01 scope) | LP-01 only | **Not** auto-reused on LP-02–05 per Phase 6.2 evidence flags |
| Мессенджеры MAX, Telegram, WhatsApp | CONFIRMED (task boundary) | all | Contact block |
| Форма: имя необяз., телефон обяз. | CONFIRMED | all | Form blocks |
| Интеграция с сайтом, Битрикс, синхронизация | CONFIRMED (intake §6.3) | LP-04 | Generic integration scope |
| Маркировка, Честный знак, ТС ПИОТ (intake §6.1) | CONFIRMED (service list) | LP-05 | Service scope without legal advice |
| НДС | OPERATOR_DECISION_REQUIRED | all | Omitted from public copy |
| Тарифы абонентского сопровождения | OPERATOR_DECISION_REQUIRED | LP-02 | Formats described, prices omitted |
| Стоимость часа сопровождения | OPERATOR_DECISION_REQUIRED | LP-02 | Price-intent group served qualitatively |
| SLA / время ответа | SAFE_TO_OMIT | LP-02, LP-05 | Not mentioned |
| Партнёрский статус 1С | SAFE_TO_OMIT | all | Not mentioned |
| Кейсы и клиенты | CLIENT_EVIDENCE_REQUIRED | all | No invented cases |
| Портфolio интеграций | CLIENT_EVIDENCE_REQUIRED | LP-04 | Generic systems only |
| Опыт маркировки по отраслям | CLIENT_EVIDENCE_REQUIRED | LP-05 | Scenarios generic, no metrics |
| Гарантии совместимости после обновлений | CLIENT_EVIDENCE_REQUIRED | LP-03 | Not promised |
| Фиксированные сроки проектов | SAFE_TO_OMIT | LP-03, LP-04, LP-05 | Not mentioned |
| Список всех поддерживаемых API/протоколов | CLIENT_EVIDENCE_REQUIRED | LP-04 | Scope after audit of both systems |

---

## Per-page unresolved decisions (operator)

### LP-02 — Сопровождение

1. **OPERATOR_DECISION_REQUIRED:** публиковать ли почасовую ставку для разовых инцидентов сопровождения или оставить только «оценка после уточнения».
2. **OPERATOR_DECISION_REQUIRED:** как описывать абонентское сопровождение без тарифной сетки.
3. **OPERATOR_DECISION_REQUIRED:** включать ли НДС в коммерческие формулировки.

### LP-03 — Доработка

1. **OPERATOR_DECISION_REQUIRED:** указывать ли почасовую модель для мелких доработок или только смету по ТЗ.
2. **CLIENT_EVIDENCE_REQUIRED:** типовые примеры проектов для блока доверия (без выдуманных имён).

### LP-04 — Интеграции

1. **CLIENT_EVIDENCE_REQUIRED:** подтверждённый перечень внешних систем помимо сайта и Битрикс.
2. **OPERATOR_DECISION_REQUIRED:** модель ценообразования (проект vs почасовая) на публичной странице.

### LP-05 — Маркировка

1. **CLIENT_EVIDENCE_REQUIRED:** перечень отраслей/товарных групп с реальным опытом (intake list ≠ кейсы).
2. **OPERATOR_DECISION_REQUIRED:** глубина подраздела ТС ПИОТ vs общий блок маркировки.
3. **SAFE TO PROCEED:** без юридических консультаций и гарантий compliance — draft uses technical service scope only.

---

## Draft policy applied

- Gaps marked **SAFE_TO_OMIT** or **OPERATOR_DECISION_REQUIRED** do **not** block complete drafts.
- No internal governance wording in public copy.
- No invented tariffs, SLA, cases, or partner claims.
