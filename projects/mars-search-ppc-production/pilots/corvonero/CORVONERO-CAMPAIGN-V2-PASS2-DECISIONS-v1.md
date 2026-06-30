# CORVONERO CAMPAIGN V2 PASS 2 — Phrase Decisions

Generated: 2026-06-30T11:13:36.000Z

## Summary
- **items_reviewed:** 33
- **high_confidence_auto_resolved:** 33
- **operator_decisions_required:** 0
- **recommended_reject:** 31
- **recommended_local_only:** 1
- **recommended_remote_only:** 0
- **recommended_include_both:** 1

## Decision table

| # | phrase | class | decision | target | confidence | operator? | reason |
|---|--------|-------|----------|--------|------------|-----------|--------|
| 1 | программист 1с москва | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «москва» — вне зоны LOCAL и нецелевой для REMOTE |
| 2 | программисты 1с спб | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «спб» — вне зоны LOCAL и нецелевой для REMOTE |
| 3 | 1с программист красноярск | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «красноярск» — вне зоны LOCAL и нецелевой для REMOTE |
| 4 | программисты 1с екатеринбург | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «екатеринбург» — вне зоны LOCAL и нецелевой для REMOTE |
| 5 | программист 1с нижний | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания |
| 6 | программист 1с нижний новгород | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания |
| 7 | 1с программисты ростов | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания |
| 8 | программист 1с санкт петербург | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «петербург» — вне зоны LOCAL и нецелевой для REMOTE |
| 9 | программисты 1с самара | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания |
| 10 | программисты 1с краснодар | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания |
| 11 | программисты 1с казань | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «казань» — вне зоны LOCAL и нецелевой для REMOTE |
| 12 | программисты 1с челябинск | CONFLICTING_OR_AMBIGUOUS | LOCAL_ONLY | CA-01-LOCAL | HIGH | False | Явный локальный маркер: «нск» |
| 13 | программист 1с ростов на дону | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания |
| 14 | программисты 1с воронеж | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания |
| 15 | программист 1с онлайн | CONFLICTING_OR_AMBIGUOUS | INCLUDE_BOTH | CA-01-LOCAL,CA-01-REMOTE | HIGH | False | «онлайн» описывает сервис/продукт, не режим доставки — дублировать в обе ветки |
| 16 | омск программисты 1с | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «омск» — вне зоны LOCAL и нецелевой для REMOTE |
| 17 | работа москва программист 1с | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «москва» — вне зоны LOCAL и нецелевой для REMOTE |
| 18 | программист 1с уфа | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания |
| 19 | программист 1с томск | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «омск» — вне зоны LOCAL и нецелевой для REMOTE |
| 20 | программист 1с пермь | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания |
| 21 | программист 1с барнаул | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «барнаул» — вне зоны LOCAL и нецелевой для REMOTE |
| 22 | программист 1с комендантский проспект спб | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «спб» — вне зоны LOCAL и нецелевой для REMOTE |
| 23 | маркировка в 1с с нуля | REJECT_CANDIDATE | REJECT | REMOTE_ONLY | HIGH | False | Обучение/курсы — не коммерческий сервис |
| 24 | сопровождение 1с екатеринбург | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-02-REMOTE | HIGH | False | Запрос с чужим городом «екатеринбург» — вне зоны LOCAL и нецелевой для REMOTE |
| 25 | центр сопровождения 1с екатеринбург | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-02-REMOTE | HIGH | False | Запрос с чужим городом «екатеринбург» — вне зоны LOCAL и нецелевой для REMOTE |
| 26 | асп сопровождение 1с екатеринбург | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-02-REMOTE | HIGH | False | Запрос с чужим городом «екатеринбург» — вне зоны LOCAL и нецелевой для REMOTE |
| 27 | асп центр сопровождения 1с екатеринбург | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-02-REMOTE | HIGH | False | Запрос с чужим городом «екатеринбург» — вне зоны LOCAL и нецелевой для REMOTE |
| 28 | сопровождение 1с зарплата | REJECT_CANDIDATE | REJECT | REMOTE_ONLY | HIGH | False | Зарплатный/кадровый интент — не услуга |
| 29 | сопровождение 1с зарплата и кадры | REJECT_CANDIDATE | REJECT | REMOTE_ONLY | HIGH | False | Зарплатный/кадровый интент — не услуга |
| 30 | 1с сопровождение москва | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-02-REMOTE | HIGH | False | Запрос с чужим городом «москва» — вне зоны LOCAL и нецелевой для REMOTE |
| 31 | сопровождение 1с ростов | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-02-REMOTE | HIGH | False | Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания |
| 32 | сопровождение и поддержка 1с в красноярске | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-02-REMOTE | HIGH | False | Запрос с чужим городом «красноярск» — вне зоны LOCAL и нецелевой для REMOTE |
| 33 | час программиста 1с в москве | CONFLICTING_OR_AMBIGUOUS | REJECT | CA-01-REMOTE | HIGH | False | Запрос с чужим городом «москве» — вне зоны LOCAL и нецелевой для REMOTE |
