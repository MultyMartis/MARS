# Service-to-Cluster Inventory — Корво Неро v1

**Source:** Operator intake + MIG `keyword_registry.json` + `demand_surface.json`  
**Stage:** 2A

---

## Inventory map

| # | Operator service direction | MIG cluster(s) | Evidence grade | Campaign | Ad groups | Status |
|---|---------------------------|----------------|----------------|----------|-----------|--------|
| 1 | программист 1С | A_broad_commercial | B partial | CORV-C01 | G01-01, G01-02 | IN SCOPE |
| 2 | услуги программиста 1С | A_broad_commercial | B | CORV-C01 | G01-01 | IN SCOPE |
| 3 | настройка 1С | A_broad_commercial | B semantic | CORV-C01 | G01-03 | IN SCOPE |
| 4 | внедрение 1С | A_broad_commercial | B semantic | CORV-C01 | G01-04 | IN SCOPE |
| 5 | сопровождение 1С | A_support | B r1q02 | CORV-C01 | G01-05 | IN SCOPE |
| 6 | обслуживание 1С | A_support | B semantic | CORV-C01 | G01-06 | IN SCOPE |
| 7 | разовые работы | A_broad_commercial | intake | CORV-C01 | G01-08 | IN SCOPE |
| 8 | абонентское сопровождение | A_support | B semantic | CORV-C01 | G01-07 | IN SCOPE |
| 9 | доработка 1С | A_modification | B r1q03 | CORV-C02 | G02-01 | IN SCOPE |
| 10 | доработка конфигурации | A_modification | B | CORV-C02 | G02-02 | IN SCOPE |
| 11 | доработка существующей базы | A_modification | B | CORV-C02 | G02-03 | IN SCOPE |
| 12 | обновление доработанной 1С | A_support | intake+semantic | CORV-C02 | G02-04 | IN SCOPE |
| 13 | перенос и сохранение доработок | A_modification | semantic | CORV-C02 | G02-05 | IN SCOPE |
| 14 | исправление доработок после обновления | A_modification | semantic | CORV-C02 | G02-06 | IN SCOPE |
| 15 | настройка отчёта | B_reports, A_modification | B r1q04 | CORV-C03 | G03-01 | IN SCOPE |
| 16 | доработка отчёта | B_reports | B r1q04 | CORV-C03 | G03-01 | IN SCOPE |
| 17 | создание отчёта | B_forms adjacency | semantic | CORV-C03 | G03-02 | IN SCOPE |
| 18 | печатная форма | B_forms | B semantic | CORV-C03 | G03-03 | IN SCOPE |
| 19 | доработка печатной формы | B_forms | B seed | CORV-C03 | G03-04 | IN SCOPE |
| 20 | внешние отчёты и обработки | B_forms | B | CORV-C03 | G03-05 | IN SCOPE |
| 21 | РМК | B_rmk | weak seed | CORV-C03 | G03-06 | IN SCOPE (Tier 3) |
| 22 | доработка РМК | B_rmk | weak/no-result seed | CORV-C03 | G03-06 | IN SCOPE (Tier 3) |
| 23 | настройка рабочего места кассира | B_rmk, C_integrations | semantic adjacency | CORV-C03 | G03-06 | IN SCOPE |
| 24 | расчёт себестоимости | Wordstat adjacency | intake | CORV-C04 | G04-01 | IN SCOPE |
| 25 | настройка расчёта себестоимости | Wordstat adjacency | intake | CORV-C04 | G04-01 | IN SCOPE |
| 26 | планирование закупок | Wordstat adjacency | intake | CORV-C04 | G04-02 | IN SCOPE |
| 27 | платёжный календарь | Wordstat adjacency | intake | CORV-C04 | G04-03 | IN SCOPE |
| 28 | интеграция 1С с сайтом | C_integrations | B r1q05 | CORV-C05 | G05-01 | IN SCOPE |
| 29 | обмен 1С с сайтом | C_integrations | B | CORV-C05 | G05-01 | IN SCOPE |
| 30 | интеграция 1С Битрикс | C_integrations | C r1q06 | CORV-C05 | G05-02 | IN SCOPE |
| 31 | интеграция 1С с кассой | C_integrations | C semantic | CORV-C05 | G05-03 | IN SCOPE |
| 32 | подключение кассы к 1С | C_integrations | semantic | CORV-C05 | G05-03 | IN SCOPE |
| 33 | синхронизация 1С | C_integrations | B seed | CORV-C05 | G05-04 | IN SCOPE |
| 34 | настройка обмена | C_integrations | B | CORV-C05 | G05-05 | IN SCOPE |
| 35 | перенос данных | C_integrations | semantic | CORV-C05 | G05-06 | IN SCOPE |
| 36 | подключение маркировки | D_labeling | C/B mixed | CORV-C06 | G06-01 | IN SCOPE |
| 37 | настройка маркировки | D_labeling | B semantic | CORV-C06 | G06-02 | IN SCOPE |
| 38 | внедрение маркировки | D_labeling | semantic | CORV-C06 | G06-01 | IN SCOPE |
| 39 | Честный знак | D_labeling | B r1q08 | CORV-C06 | G06-03 | IN SCOPE |
| 40 | устранение ошибок маркировки | D_labeling | semantic | CORV-C06 | G06-04 | IN SCOPE |
| 41–52 | product marking categories | E_product_labeling, D_ts_piot | B/C | CORV-C06 | G06-05 … G06-13 | IN SCOPE |
| 53 | программа 1С не работает | A_urgent | B r1q10 | CORV-C07 | G07-01 | IN SCOPE |
| 54 | ошибка 1С | A_urgent, troubleshooting | B | CORV-C07 | G07-02 | IN SCOPE |
| 55 | сломалась синхронизация | C_integrations | semantic | CORV-C07 | G07-03 | IN SCOPE |
| 56 | не работает обмен | C_integrations | semantic | CORV-C07 | G07-03 | IN SCOPE |
| 57 | ошибка после обновления | A_support, A_urgent | semantic | CORV-C07 | G07-02 | IN SCOPE |
| 58 | восстановление работы | A_urgent | semantic | CORV-C07 | G07-04 | IN SCOPE |
| 59 | ТС ПИОТ | D_ts_piot | C/defer→full scope | CORV-C08 | G08-01 | IN SCOPE |
| 60 | настройка ТС ПИОТ | D_ts_piot | semantic | CORV-C08 | G08-01 | IN SCOPE |
| 61 | интеграция ТС ПИОТ с 1С | D_ts_piot | semantic | CORV-C08 | G08-02 | IN SCOPE |

---

## Phrase-level exclusions (not service removals)

| Phrase class | Action | Example |
|--------------|--------|---------|
| Employment | Reject phrase / campaign negative | «программист 1с вакансия» |
| Training | Reject phrase | «курсы программист 1с» |
| Download/software | Campaign negative | «скачать 1с» |
| Pure regulatory | Reject or Tier 4 test only | «когда начнется маркировка автозапчастей» |
| No-result seed | Alternate phrasing only | «срочно программист 1С» → use «1с не работает» |

---

## Verification

**No operator-provided service direction was removed from architecture.**  
Previous Model A exclusions (marking, integrations, troubleshooting, ТС ПИОТ, product marking, management tasks) are **restored**.
